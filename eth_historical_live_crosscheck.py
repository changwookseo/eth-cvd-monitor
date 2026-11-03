"""As-of cross-check of historical ETH signals and Elliott-style swing structure.
No live API: latest integrated row is NOT automatically real-time.
"""
import csv,json
from collections import defaultdict
from datetime import datetime,timezone,timedelta
from pathlib import Path
from statistics import mean
SOURCE=Path("research_integrated/eth_180d_integrated_1h.csv")
OUT=Path("research_predictions")
HORIZONS=(4,12,24)
CUTOFF=datetime(2026,10,1,tzinfo=timezone.utc)
def num(r,k):
    try:return float(r[k])
    except (KeyError,TypeError,ValueError):return None
def conditions(rows,i):
    r=rows[i];prev=rows[i-1];t=datetime.fromisoformat(r["utc_hour"])
    o,old=num(r,"oi_eth"),num(prev,"oi_eth")
    s,f=num(r,"spot_cvd_pct"),num(r,"futures_cvd_pct")
    if None in (o,old,s,f) or old<=0:return []
    obs=r.get("oi_observed_at_utc")
    if not obs or datetime.fromisoformat(obs)>t+timedelta(hours=1):return []
    change=o/old-1
    tags=[]
    if s>0 and change>0:tags.append("spot_buy_oi_up")
    if s>0 and change<0:tags.append("spot_buy_oi_down")
    if s<0 and change>0:tags.append("spot_sell_oi_up")
    if s*f<0:
        tags.append("spot_buy_futures_sell" if s>0 else "spot_sell_futures_buy")
    age,rate=num(r,"funding_age_hours"),num(r,"last_settled_funding_rate_pct")
    if age is not None and 0<=age<=24 and rate is not None and change>0:
        tags.append("negative_funding_oi_up" if rate<0 else "positive_funding_oi_up" if rate>0 else "zero_funding_oi_up")
    return tags
def swing_context(rows,at,window=12):
    # Mechanical pivots, NOT a definitive Elliott 1-5 or ABC wave count.
    close=[num(r,"eth_close") for r in rows[:at+1]]
    pivots=[]
    for i in range(window,len(close)-window):
        segment=close[i-window:i+window+1]
        if any(x is None for x in segment):continue
        if close[i]==max(segment) and segment.count(close[i])==1:pivots.append({"time":rows[i]["utc_hour"],"kind":"high","price":close[i]})
        elif close[i]==min(segment) and segment.count(close[i])==1:pivots.append({"time":rows[i]["utc_hour"],"kind":"low","price":close[i]})
    # At evaluation time, each pivot has right-side confirmation.
    return {"method":"12-hour confirmed close pivots; wave count not asserted","recent_confirmed_pivots":pivots[-8:],"elliott_count":"unconfirmed","limitations":"Hourly close pivots only; daily/weekly OHLCV and alternative wave scenarios required for Elliott validation"}
def main():
    with SOURCE.open(encoding="utf-8",newline="") as f:rows=sorted(csv.DictReader(f),key=lambda r:r["utc_hour"])
    now=datetime.now(timezone.utc)
    if len(rows)<50:raise RuntimeError("Insufficient data")
    ts=[datetime.fromisoformat(r["utc_hour"]) for r in rows]
    if len(set(ts))!=len(ts):raise RuntimeError("Duplicate hours")
    # One common historical cutoff for all conditions. No future leakage beyond Sep 30.
    hist=defaultdict(list)
    for i in range(1,len(rows)-25):
        t=ts[i]
        if t>=CUTOFF:break
        if ts[i+1]!=t+timedelta(hours=1):continue
        for h in HORIZONS:
            j=i+h+1
            if ts[j]!=t+timedelta(hours=h+1) or ts[j]>=CUTOFF:continue
            entry,exit=num(rows[i+1],"eth_close"),num(rows[j],"eth_close")
            if entry is None or exit is None or entry<=0:continue
            for tag in conditions(rows,i):hist[(tag,h)].append((t,100*(exit/entry-1)))
    # Disjoint signal windows: one event per horizon per condition.
    stats={}
    for (tag,h),values in hist.items():
        unique=[];last=None
        for t,r in values:
            if last is None or t>=last+timedelta(hours=h+1):unique.append(r);last=t
        stats.setdefault(tag,{})[str(h)]={"raw_hours":len(values),"nonoverlapping_events":len(unique),"up_pct":round(100*sum(x>0 for x in unique)/len(unique),2),"mean_return_pct":round(mean(unique),4)} if unique else None
    latest=ts[-1]
    # If current integrated data is stale, explicitly abstain.
    age=(now-latest).total_seconds()/3600
    current_tags=conditions(rows,len(rows)-1) if len(rows)>1 else []
    matches={tag:stats.get(tag,{}) for tag in current_tags}
    result={"generated_utc":now.isoformat(),"historical_cutoff_exclusive_utc":CUTOFF.isoformat(),"historical_method":"Same cutoff for all features; nonoverlapping event windows; no fees or out-of-sample calibration","historical_stats":stats,"latest_integrated_hour":latest.isoformat(),"latest_data_age_hours":round(age,2),"current_conditions":current_tags if 0<=age<=2 else [],"historical_matches":matches if 0<=age<=2 else {},"wave_context":swing_context(rows,len(rows)-1),"decision":{"status":"insufficient_current_data" if age>2 or age<0 else "unvalidated_observation_only","risk_level":"unrated","response":"관망 및 최신 데이터 확보" if age>2 or age<0 else "8지표·거시·청산 검증 전 매매 판단 보류","reason":"No live source and no validated calibrated decision thresholds; never infer confidence from raw hit rates."}}
    OUT.mkdir(exist_ok=True)
    stamp=now.strftime("%Y%m%dT%H%M%SZ")
    path=OUT/("crosscheck_"+stamp+".json")
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"saved":str(path),"latest_data_age_hours":result["latest_data_age_hours"],"current_conditions":result["current_conditions"],"decision":result["decision"],"historical_stats":stats},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
