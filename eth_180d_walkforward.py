"""Walk-forward ETH risk research. Descriptive, never calibrated probability."""
import csv,json,math
from collections import defaultdict
from datetime import datetime,timedelta,timezone
from pathlib import Path
from statistics import mean
from eth_180d_wave_comparison import tags,structure,n
DATA=Path("research_integrated/eth_180d_integrated_1h.csv")
OUT=Path("research_forecasts")
H=(4,12,24)
CUTOFF=datetime(2026,10,1,tzinfo=timezone.utc)
MIN_TRAIN=30
def stats(items):
    if not items:return None
    return {"n":len(items),"up_pct":round(100*sum(x["ret"]>0 for x in items)/len(items),2),"mean_return_pct":round(mean(x["ret"] for x in items),4),"mean_adverse_close_pct":round(mean(x["adverse"] for x in items),4)}
def label(s):
    if not s or s["n"]<MIN_TRAIN:return "판단보류"
    if s["up_pct"]<40 and s["mean_return_pct"]<0:return "위험"
    if s["up_pct"]<48 and s["mean_return_pct"]<0:return "주의"
    if s["up_pct"]>=60 and s["mean_return_pct"]>0:return "안정"
    return "중립"
def main():
    with DATA.open(newline="",encoding="utf-8") as f:rows=sorted(csv.DictReader(f),key=lambda r:r["utc_hour"])
    ts=[datetime.fromisoformat(r["utc_hour"]) for r in rows]
    if len(set(ts))!=len(ts):raise RuntimeError("duplicate timestamps")
    prices=[n(r,"eth_close") for r in rows]
    events=[]
    for i in range(30,len(rows)-26):
        if ts[i]>=CUTOFF:break
        if ts[i+1]!=ts[i]+timedelta(hours=1) or not prices[i+1]:continue
        condition=tags(rows,i)
        if not condition:continue
        wave=structure(prices,i)
        for h in H:
            j=i+h+1
            if ts[j]!=ts[i]+timedelta(hours=h+1) or ts[j]>=CUTOFF:continue
            path=prices[i+1:j+1]
            if any(p is None for p in path):continue
            ret=100*(prices[j]/prices[i+1]-1)
            adverse=min(0,100*(min(path)/prices[i+1]-1))
            for tag in condition:events.append({"t":ts[i],"condition":tag,"wave":wave,"h":h,"ret":ret,"adverse":adverse})
    unique=sorted(set(e["t"] for e in events))
    if len(unique)<60:raise RuntimeError("Insufficient history")
    split=unique[int(len(unique)*0.7)]
    # Purge train events whose future outcome reaches validation period.
    train=[e for e in events if e["t"]+timedelta(hours=e["h"]+1)<split]
    valid=[e for e in events if e["t"]>=split]
    def disjoint(items,h):
        selected=[];last=None
        for e in sorted(items,key=lambda x:x["t"]):
            if last is None or e["t"]>=last+timedelta(hours=h+1):
                selected.append(e);last=e["t"]
        return selected
    result=[]
    for condition in sorted(set(e["condition"] for e in events)):
        for h in H:
            tr=disjoint([e for e in train if e["condition"]==condition and e["h"]==h],h)
            va=disjoint([e for e in valid if e["condition"]==condition and e["h"]==h],h)
            for wave in ("all","higher_high_higher_low","lower_high_lower_low","mixed_or_corrective","unclassified"):
                a=tr if wave=="all" else [e for e in tr if e["wave"]==wave]
                b=va if wave=="all" else [e for e in va if e["wave"]==wave]
                x,y=stats(a),stats(b)
                pred=label(x)
                actual=label(y)
                # The categories are descriptive. Abstain if validation sample too small.
                reliable=bool(x and y and x["n"]>=MIN_TRAIN and y["n"]>=20 and pred==actual)
                result.append({"condition":condition,"horizon_hours":h,"structure":wave,"train":x,"validation":y,"train_risk_label":pred,"validation_risk_label":actual,"label_replicated":reliable,"validated_prediction_probability":None})
    # Current conditions are latest COMPLETE integrated observation, not a live quote.
    now=datetime.now(timezone.utc)
    latest=None
    for i in range(len(rows)-1,30,-1):
        if ts[i]+timedelta(hours=1)>now:continue
        if ts[i-1]!=ts[i]-timedelta(hours=1):continue
        if not tags(rows,i):continue
        latest=i;break
    current=[]
    if latest is not None:
        wave=structure(prices,latest)
        for condition in tags(rows,latest):
            for h in H:
                selected=next((x for x in result if x["condition"]==condition and x["horizon_hours"]==h and x["structure"]==wave),None)
                baseline=next((x for x in result if x["condition"]==condition and x["horizon_hours"]==h and x["structure"]=="all"),None)
                sufficient=bool(selected and selected["label_replicated"])
                current.append({"condition":condition,"horizon_hours":h,"structure":wave,"historical_validation":selected,"baseline_validation":baseline,"decision":selected["train_risk_label"] if sufficient else "판단보류","reason":"Training and validation labels agree with minimum sample counts" if sufficient else "Insufficient independently validated structure-specific evidence; baseline shown for context only"})
    stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    target=OUT/stamp;target.mkdir(parents=True,exist_ok=True)
    report={"generated_utc":now.isoformat(),"training_end_exclusive_utc":split.isoformat(),"validation_start_utc":split.isoformat(),"historical_cutoff_exclusive_utc":CUTOFF.isoformat(),"current_data_last_complete_hour_utc":ts[latest].isoformat() if latest is not None else None,"current_data_staleness_hours":round((now-ts[latest]).total_seconds()/3600,2) if latest is not None else None,"current_is_live":False,"current_usable_for_live_decision":bool(latest is not None and now-ts[latest]<timedelta(hours=3)),"funding_in_october_unavailable":True,"validation_results":result,"current_conditions":current,"limitations":["Historical training and validation are chronological, with purged outcome windows, but market regimes may shift.","Events are thinned per condition/horizon; different conditions still overlap.","Risk labels are research heuristics, NOT calibrated probabilities or proven trading recommendations.","Confirmed swing structure is a proxy, not a formal Elliott wave count.","Current observation is from the collected batch, not streaming real-time data.","October funding cannot be assumed or substituted from September.","No macro, ETF, ETH/BTC, stablecoins, liquidation or 8-indicator weighted score is calculated here.","No fees/slippage and no intrahour drawdown; avoid treating results as executable trades."]}
    (target/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    with (target/"validation.csv").open("w",newline="",encoding="utf-8") as f:
        fields=["condition","horizon_hours","structure","train_risk_label","validation_risk_label","label_replicated","train_n","validation_n","train_up_pct","validation_up_pct","train_mean_return_pct","validation_mean_return_pct"]
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for x in result:
            a=x["train"] or {};b=x["validation"] or {}
            w.writerow({"condition":x["condition"],"horizon_hours":x["horizon_hours"],"structure":x["structure"],"train_risk_label":x["train_risk_label"],"validation_risk_label":x["validation_risk_label"],"label_replicated":x["label_replicated"],"train_n":a.get("n"),"validation_n":b.get("n"),"train_up_pct":a.get("up_pct"),"validation_up_pct":b.get("up_pct"),"train_mean_return_pct":a.get("mean_return_pct"),"validation_mean_return_pct":b.get("mean_return_pct")})
    print(json.dumps({"output":str(target),"split":split.isoformat(),"train_event_rows":len(train),"validation_event_rows":len(valid),"replicated_labels":sum(x["label_replicated"] for x in result),"total_conditions":len(result),"current_data_hour":report["current_data_last_complete_hour_utc"],"current_is_live":False,"current":current},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
