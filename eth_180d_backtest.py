"""Reproducible exploratory ETH 180d event study. No trading-performance claims."""
import csv, json, math
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import mean
DATA=Path("research_integrated/eth_180d_integrated_1h.csv")
OUT=Path("research_backtests")
HORIZONS=(4,12,24)
def number(row,key):
    try: return float(row[key])
    except (KeyError,ValueError,TypeError): return None
def read():
    with DATA.open(newline="",encoding="utf-8") as f: return list(csv.DictReader(f))
def main():
    rows=sorted(read(),key=lambda r:r["utc_hour"])
    if not rows: raise RuntimeError("Empty integration data")
    times=[datetime.fromisoformat(r["utc_hour"]) for r in rows]
    if len(set(times))!=len(times): raise RuntimeError("Duplicate hours")
    # All features refer to a completed hour; decision at next hour opening.
    # Conservative execution uses NEXT hourly close, not signal-hour close.
    bytime={t:i for i,t in enumerate(times)}
    prices=[number(r,"eth_close") for r in rows]
    oi=[number(r,"oi_eth") for r in rows]
    signals=[]
    for i in range(4,len(rows)-25):
        t=times[i]
        if any(times[i-j]!=t-timedelta(hours=j) for j in (1,4)):continue
        if prices[i] is None or prices[i+1] is None or prices[i+1]<=0:continue
        if oi[i] is None or oi[i-1] in (None,0):continue
        observed=rows[i].get("oi_observed_at_utc")
        if not observed or datetime.fromisoformat(observed)>t+timedelta(hours=1):continue
        spot=number(rows[i],"spot_cvd_pct")
        future=number(rows[i],"futures_cvd_pct")
        if spot is None or future is None:continue
        oichange=(oi[i]/oi[i-1]-1)*100
        tags=[]
        if spot>0 and oichange>0:tags.append("spot_buy_oi_up")
        if spot>0 and oichange<0:tags.append("spot_buy_oi_down")
        if spot<0 and oichange>0:tags.append("spot_sell_oi_up")
        if spot*future<0:tags.append("spot_futures_divergence")
        # Funding features only before October and only if settlement is fresh.
        fund_age=number(rows[i],"funding_age_hours")
        fund=number(rows[i],"last_settled_funding_rate_pct")
        if t<datetime(2026,10,1,tzinfo=timezone.utc) and fund_age is not None and 0<=fund_age<=24 and fund is not None:
            if fund>0 and oichange>0:tags.append("positive_funding_oi_up")
            if fund<0 and oichange>0:tags.append("negative_funding_oi_up")
        for tag in tags:
            for horizon in HORIZONS:
                j=bytime.get(t+timedelta(hours=horizon+1))
                if j is None or prices[j] is None:continue
                # Entry at close of next completed hour (i+1), exit h hours later.
                if times[i+1]!=t+timedelta(hours=1):continue
                ret=(prices[j]/prices[i+1]-1)*100
                path=[prices[bytime[t+timedelta(hours=k)]] for k in range(1,horizon+2) if t+timedelta(hours=k) in bytime]
                if len(path)!=horizon+1 or any(p is None for p in path):continue
                adverse=(min(path)/prices[i+1]-1)*100
                signals.append({"signal_utc_hour":t.isoformat(),"condition":tag,"horizon_hours":horizon,"entry_utc_hour":times[i+1].isoformat(),"exit_utc_hour":times[j].isoformat(),"return_pct":round(ret,6),"max_adverse_close_pct":round(min(0,adverse),6)})
    # Avoid false confidence from overlapping events: count all, label as dependent.
    grouped={}
    for s in signals:grouped.setdefault((s["condition"],s["horizon_hours"]),[]).append(s)
    stats=[]
    for (condition,h),values in sorted(grouped.items()):
        returns=[v["return_pct"] for v in values]
        stats.append({"condition":condition,"horizon_hours":h,"events":len(values),"up_pct":round(100*sum(v>0 for v in returns)/len(returns),2),"mean_return_pct":round(mean(returns),4),"mean_max_adverse_close_pct":round(mean(v["max_adverse_close_pct"] for v in values),4),"first_signal":values[0]["signal_utc_hour"],"last_signal":values[-1]["signal_utc_hour"]})
    OUT.mkdir(exist_ok=True)
    stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    target=OUT/stamp
    target.mkdir()
    with (target/"events.csv").open("w",newline="",encoding="utf-8") as f:
        fields=["signal_utc_hour","condition","horizon_hours","entry_utc_hour","exit_utc_hour","return_pct","max_adverse_close_pct"]
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(signals)
    with (target/"summary.csv").open("w",newline="",encoding="utf-8") as f:
        fields=["condition","horizon_hours","events","up_pct","mean_return_pct","mean_max_adverse_close_pct","first_signal","last_signal"]
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(stats)
    metadata={"generated_utc":datetime.now(timezone.utc).isoformat(),"data_first_hour":times[0].isoformat(),"data_last_hour":times[-1].isoformat(),"input_rows":len(rows),"signal_records":len(signals),"funding_cutoff_exclusive_utc":"2026-10-01T00:00:00+00:00","limitations":["Exploratory event study, NOT validated prediction probabilities or trade returns.","Overlapping signals and forward windows are statistically dependent.","No fees, slippage, funding payments, liquidity or execution constraints.","Entry uses next hour close to avoid signal-hour close lookahead; results are not directly executable.","Funding only before October 2026, maximum settlement age 24 hours; no fabricated October funding.","Funding history completeness before October not independently verified.","OI and flow are completed-hour features; ensure observation timestamps are available at decision time.","Maximum adverse movement uses hourly closes, not intrahour lows.","Binance-only taker flow proxy; not trade-by-trade or multi-exchange CVD.","Condition thresholds are exploratory and were not pre-registered or out-of-sample validated."],"summary":stats}
    (target/"metadata.json").write_text(json.dumps(metadata,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps({"run":str(target),"input_rows":len(rows),"signal_records":len(signals),"summary":stats,"limitations":metadata["limitations"]},indent=2,ensure_ascii=False))
if __name__=="__main__":main()
