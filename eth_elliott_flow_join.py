"""Research-only join of as-of daily ETH wave context with historical hourly spot/OI/funding.
No production report modifications; no prediction probability claims.
"""
import csv,json
from collections import defaultdict
from datetime import datetime,timedelta,timezone
from pathlib import Path
from statistics import mean
ROOT=Path("research_elliott")
SOURCE=Path("research_integrated/eth_180d_integrated_1h.csv")
def load(path):
    with path.open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def num(row,key):
    try:return float(row[key])
    except (ValueError,KeyError,TypeError):return None
def main():
    daily=load(ROOT/"eth_daily.csv")
    hourly=load(SOURCE)
    if not daily or not hourly:raise RuntimeError("Missing daily or hourly input")
    dates=[datetime.fromisoformat(r["utc_date"]).date() for r in daily]
    if any((b-a).days!=1 for a,b in zip(dates,dates[1:])):raise RuntimeError("Daily history gaps")
    day_idx={r["utc_date"]:i for i,r in enumerate(daily)}
    grouped=defaultdict(list)
    for r in hourly:
        t=datetime.fromisoformat(r["utc_hour"])
        if t.tzinfo is None:raise RuntimeError("Hourly timestamps must be timezone aware")
        grouped[t.date().isoformat()].append(r)
    output=[]
    for day in sorted(grouped):
        d=datetime.fromisoformat(day).date()
        previous=(d-timedelta(days=1)).isoformat()
        if previous not in day_idx:continue
        idx=day_idx[previous]
        # Only yesterday's completed daily candle is known at the start of day d.
        if idx<365:continue
        window=daily[idx-365:idx+1]
        trough=min(window,key=lambda r:float(r["low"]))
        after=[r for r in window if r["utc_date"]>=trough["utc_date"]]
        peak=max(after,key=lambda r:float(r["high"]))
        valid=peak["utc_date"]>trough["utc_date"] and float(peak["high"])>float(trough["low"])
        prior30=daily[max(0,idx-30):idx]
        if not valid or not prior30:continue
        close=float(daily[idx]["close"])
        low30=min(float(r["low"]) for r in prior30)
        top=float(peak["high"]);bottom=float(trough["low"])
        # Both scenarios remain hypotheses. These labels are observable context, not trades.
        context=("bullish_origin_broken" if close<bottom else
                 "bearish_continuation_reference" if close<low30 else
                 "bullish_breakout_reference" if close>top else
                 "both_scenarios_open")
        hours=sorted(grouped[day],key=lambda r:r["utc_hour"])
        complete=[]
        for r in hours:
            t=datetime.fromisoformat(r["utc_hour"])
            # The hour must be fully completed by the end of its UTC hour.
            obs=r.get("oi_observed_at_utc","")
            if obs:
                observed=datetime.fromisoformat(obs)
                if observed>t+timedelta(hours=1):continue
            complete.append(r)
        if not complete:continue
        spot=[num(r,"spot_delta_usdt") for r in complete]
        future=[num(r,"futures_delta_usdt") for r in complete]
        spot=[v for v in spot if v is not None];future=[v for v in future if v is not None]
        oi=[(datetime.fromisoformat(r["utc_hour"]),num(r,"oi_eth")) for r in complete if num(r,"oi_eth") is not None]
        oi_change=None
        if len(oi)>=2 and oi[0][1]>0:oi_change=(oi[-1][1]/oi[0][1]-1)*100
        funding=[]
        for r in complete:
            age=num(r,"funding_age_hours");rate=num(r,"last_settled_funding_rate_pct")
            t=datetime.fromisoformat(r["utc_hour"])
            if t<datetime(2026,10,1,tzinfo=timezone.utc) and age is not None and 0<=age<=24 and rate is not None:
                funding.append(rate)
        spot_net=sum(spot) if spot else None
        future_net=sum(future) if future else None
        evidence=("missing" if spot_net is None or oi_change is None else
                  "spot_buy_oi_up" if spot_net>0 and oi_change>0 else
                  "spot_buy_oi_down" if spot_net>0 and oi_change<0 else
                  "spot_sell_oi_up" if spot_net<0 and oi_change>0 else
                  "spot_sell_oi_down" if spot_net<0 and oi_change<0 else "neutral")
        output.append({"utc_date":day,"context_asof_utc":previous+"T23:59:59+00:00","context":context,"prior_close":round(close,5),"origin_low":bottom,"rally_high":top,"prior_30d_low":low30,"hours_observed":len(complete),"spot_delta_usdt":round(spot_net,2) if spot_net is not None else "","futures_delta_usdt":round(future_net,2) if future_net is not None else "","oi_change_first_to_last_pct":round(oi_change,5) if oi_change is not None else "","funding_last_settled_pct":funding[-1] if funding else "","funding_available":bool(funding),"flow_evidence":evidence})
    ROOT.mkdir(exist_ok=True)
    fields=["utc_date","context_asof_utc","context","prior_close","origin_low","rally_high","prior_30d_low","hours_observed","spot_delta_usdt","futures_delta_usdt","oi_change_first_to_last_pct","funding_last_settled_pct","funding_available","flow_evidence"]
    with (ROOT/"wave_flow_daily_join.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(output)
    counts=defaultdict(lambda:defaultdict(int))
    for r in output:counts[r["context"]][r["flow_evidence"]]+=1
    result={"generated_utc":datetime.now(timezone.utc).isoformat(),"joined_days":len(output),"first_date":output[0]["utc_date"] if output else None,"last_date":output[-1]["utc_date"] if output else None,"context_by_flow_counts":{k:dict(v) for k,v in counts.items()},"funding_days_available":sum(r["funding_available"] for r in output),"days_with_full_24_hours":sum(r["hours_observed"]==24 for r in output),"notes":["Daily wave context computed strictly from previous completed UTC daily candle; hourly flow evidence belongs to the named day and is only available after its hours complete.","This is descriptive co-occurrence, NOT predictive validation or a contemporaneous morning signal.","OI first-to-last daily change uses observed hourly snapshots and may omit missing hours.","Funding is explicitly excluded on and after 2026-10-01 due to unavailable verified archives.","No probability, causal inference, formal Elliott 1-5/ABC labels, or trade performance.","Missing inputs remain missing; no fabricated funding or Kraken CVD.","No existing 8-factor weights or scheduled reports changed."]}
    (ROOT/"wave_flow_join_summary.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
