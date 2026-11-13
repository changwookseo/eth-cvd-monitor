"""Paired ETH baseline versus Elliott-inspired confirmed swing-context experiment.
Exploratory research, not a validated trading strategy or definitive Elliott wave count.
"""
import csv,json
from collections import defaultdict
from datetime import datetime,timedelta,timezone
from pathlib import Path
from statistics import mean
DATA=Path("research_integrated/eth_180d_integrated_1h.csv")
OUT=Path("research_wave_comparison")
END=datetime(2026,10,1,tzinfo=timezone.utc)
H=(4,12,24)
def n(r,k):
    try:return float(r[k])
    except (KeyError,ValueError,TypeError):return None
def tags(rows,i):
    a,b=rows[i],rows[i-1]
    s,f,o,p=n(a,"spot_cvd_pct"),n(a,"futures_cvd_pct"),n(a,"oi_eth"),n(b,"oi_eth")
    if any(v is None for v in (s,f,o,p)) or p<=0:return []
    t=datetime.fromisoformat(a["utc_hour"])
    obs=a.get("oi_observed_at_utc")
    if not obs or datetime.fromisoformat(obs)>t+timedelta(hours=1):return []
    d=o/p-1;out=[]
    if s>0 and d>0:out.append("spot_buy_oi_up")
    if s>0 and d<0:out.append("spot_buy_oi_down")
    if s<0 and d>0:out.append("spot_sell_oi_up")
    if s*f<0:out.append("spot_futures_divergence")
    age,rate=n(a,"funding_age_hours"),n(a,"last_settled_funding_rate_pct")
    if age is not None and 0<=age<=24 and rate is not None and d>0:
        if rate<0:out.append("negative_funding_oi_up")
        if rate>0:out.append("positive_funding_oi_up")
    return out
def structure(prices,i,width=12):
    """Only pivots whose right confirmation is already known by signal hour i."""
    piv=[]
    for j in range(width,i-width+1):
        segment=prices[j-width:j+width+1]
        if any(v is None for v in segment):continue
        if prices[j]==max(segment) and segment.count(prices[j])==1:piv.append((j,"high",prices[j]))
        elif prices[j]==min(segment) and segment.count(prices[j])==1:piv.append((j,"low",prices[j]))
    # Alternating most-recent confirmed turning points; ambiguous configurations abstain.
    clean=[]
    for p in piv:
        if clean and p[1]==clean[-1][1]:
            if (p[1]=="high" and p[2]>clean[-1][2]) or (p[1]=="low" and p[2]<clean[-1][2]):clean[-1]=p
        else:clean.append(p)
    if len(clean)<4:return "unclassified"
    last=clean[-4:]
    highs=[p[2] for p in last if p[1]=="high"]
    lows=[p[2] for p in last if p[1]=="low"]
    if len(highs)!=2 or len(lows)!=2:return "unclassified"
    if highs[-1]>highs[0] and lows[-1]>lows[0]:return "higher_high_higher_low"
    if highs[-1]<highs[0] and lows[-1]<lows[0]:return "lower_high_lower_low"
    return "mixed_or_corrective"
def summarize(events):
    if not events:return None
    returns=[x["return_pct"] for x in events]
    return {"events":len(events),"up_pct":round(100*sum(r>0 for r in returns)/len(returns),2),"mean_return_pct":round(mean(returns),4),"mean_adverse_close_pct":round(mean(x["adverse_pct"] for x in events),4)}
def main():
    with DATA.open(newline="",encoding="utf-8") as f:rows=sorted(csv.DictReader(f),key=lambda r:r["utc_hour"])
    ts=[datetime.fromisoformat(r["utc_hour"]) for r in rows]
    if len(set(ts))!=len(ts):raise RuntimeError("Duplicate hours")
    price=[n(r,"eth_close") for r in rows]
    events=[]
    for i in range(30,len(rows)-26):
        if ts[i]>=END:break
        if ts[i+1]!=ts[i]+timedelta(hours=1):continue
        entry=price[i+1]
        if entry is None or entry<=0:continue
        current_tags=tags(rows,i)
        if not current_tags:continue
        wave=structure(price,i)
        for h in H:
            j=i+1+h
            if ts[j]!=ts[i]+timedelta(hours=h+1) or ts[j]>=END:continue
            path=price[i+1:j+1]
            if any(x is None for x in path):continue
            ret=100*(price[j]/entry-1)
            adverse=100*(min(path)/entry-1)
            for tag in current_tags:
                events.append({"signal_utc":ts[i].isoformat(),"condition":tag,"wave_structure":wave,"horizon":h,"return_pct":round(ret,6),"adverse_pct":round(min(0,adverse),6)})
    # Exactly same observations for baseline and wave subsets; non-overlap within each tag+h.
    buckets=defaultdict(list)
    for e in events:buckets[(e["condition"],e["horizon"])].append(e)
    results=[]
    for (tag,h),items in sorted(buckets.items()):
        disjoint=[];last=None
        for e in items:
            t=datetime.fromisoformat(e["signal_utc"])
            if last is None or t>=last+timedelta(hours=h+1):disjoint.append(e);last=t
        base=summarize(disjoint)
        groups={}
        for wave in ("higher_high_higher_low","lower_high_lower_low","mixed_or_corrective","unclassified"):
            subset=[e for e in disjoint if e["wave_structure"]==wave]
            groups[wave]=summarize(subset)
        results.append({"condition":tag,"horizon_hours":h,"baseline":base,"wave_conditioned":groups,"warning":"Wave subset is a partition of baseline, not an independent trial. Small subsets unreliable."})
    stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    target=OUT/stamp;target.mkdir(parents=True,exist_ok=True)
    with (target/"paired_events.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["signal_utc","condition","wave_structure","horizon","return_pct","adverse_pct"]);w.writeheader();w.writerows(events)
    report={"generated_utc":datetime.now(timezone.utc).isoformat(),"cutoff_exclusive_utc":END.isoformat(),"method":"Confirmed 12h left/right close pivots, as-of signal hour; alternate pivot structure, NOT an Elliott 1-5/ABC count.","comparison":"Same events, same cutoff, non-overlapping windows per condition/horizon. Wave groups partition baseline.","limitations":["No formal Elliott wave labels; proxy swing structure only.","No out-of-sample performance test; no claim of predictive improvement.","Same event may appear under multiple conditions; not independent.","Funding unavailable in October; compare only through September.","No execution costs; hourly close not intrahour risk.","Pivot right-confirmation delay is enforced; wave labels may still be ambiguous."],"results":results}
    (target/"comparison.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps({"output":str(target),"event_rows":len(events),"results":results,"limitations":report["limitations"]},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
