"""Holdout evaluation of the EXISTING ETH wave comparison, without modifying its signals.
This tests whether wave context improves directional forecasts beyond baseline.
"""
import csv,json
from collections import defaultdict
from datetime import datetime,timedelta,timezone
from pathlib import Path
from statistics import mean
ROOT=Path("research_wave_comparison")
MIN_TRAIN=20
SPLIT=datetime(2026,8,1,tzinfo=timezone.utc)
GAP_HOURS=25
def summarize(rows):
    if not rows:return None
    return {"n":len(rows),"up_pct":round(100*mean(float(r["return_pct"])>0 for r in rows),2),"mean_return_pct":round(mean(float(r["return_pct"]) for r in rows),4),"mean_adverse_close_pct":round(mean(float(r["adverse_pct"]) for r in rows),4)}
def main():
    folders=sorted(p for p in ROOT.iterdir() if p.is_dir() and (p/"paired_events.csv").exists())
    if not folders:raise RuntimeError("First run eth_180d_wave_comparison.py")
    source=folders[-1]
    with (source/"paired_events.csv").open(encoding="utf-8",newline="") as f:events=list(csv.DictReader(f))
    groups=defaultdict(list)
    for e in events:
        groups[(e["condition"],int(e["horizon"]))].append(e)
    report=[]
    for (condition,h),items in sorted(groups.items()):
        items.sort(key=lambda e:e["signal_utc"])
        # Nonoverlapping windows, then embargo around the training/test boundary.
        selected=[];last=None
        for e in items:
            t=datetime.fromisoformat(e["signal_utc"])
            if last is None or t>=last+timedelta(hours=h+1):
                selected.append(e);last=t
        train=[e for e in selected if datetime.fromisoformat(e["signal_utc"])+timedelta(hours=h+1)<SPLIT]
        test=[e for e in selected if datetime.fromisoformat(e["signal_utc"])>=SPLIT+timedelta(hours=GAP_HOURS)]
        if not train or not test:
            report.append({"condition":condition,"horizon":h,"status":"insufficient_split_data","train_n":len(train),"test_n":len(test)})
            continue
        base_rate=mean(float(e["return_pct"])>0 for e in train)
        wave_rates={}
        for wave in set(e["wave_structure"] for e in train):
            subset=[e for e in train if e["wave_structure"]==wave]
            if len(subset)>=MIN_TRAIN:
                # Smoothed estimate prevents treating 100% small groups as certainty.
                wave_rates[wave]=(sum(float(e["return_pct"])>0 for e in subset)+2*base_rate)/(len(subset)+2)
        def forecasts(e):
            return base_rate,wave_rates.get(e["wave_structure"],base_rate)
        y=[float(e["return_pct"])>0 for e in test]
        bp=[forecasts(e)[0] for e in test]
        wp=[forecasts(e)[1] for e in test]
        brier=lambda p:mean((a-int(v))**2 for a,v in zip(p,y))
        b=brier(bp);w=brier(wp)
        report.append({"condition":condition,"horizon":h,"status":"evaluated","train_n":len(train),"test_n":len(test),"wave_supported_categories":list(sorted(wave_rates)),"wave_coverage_test_n":sum(e["wave_structure"] in wave_rates for e in test),"baseline_test_brier":round(b,5),"wave_test_brier":round(w,5),"wave_minus_baseline_brier":round(w-b,5),"wave_improved_holdout":w<b,"baseline_test_direction_accuracy_pct":round(100*mean((p>0.5)==v for p,v in zip(bp,y)),2),"wave_test_direction_accuracy_pct":round(100*mean((p>0.5)==v for p,v in zip(wp,y)),2),"test_outcome":summarize(test)})
    result={"generated_utc":datetime.now(timezone.utc).isoformat(),"source":str(source),"training":"before 2026-08-01 UTC, completed outcome required","holdout":"from 2026-08-02 01:00 UTC through September 30","embargo_hours":GAP_HOURS,"method":"Same disjoint signal events for both forecasts; training-only base rate and wave-conditional rates; wave group minimum 20; wave fallback to baseline; Brier lower is better","warnings":["Exploratory fixed holdout only, not statistically validated or production ready.","Multiple conditions overlap; across-condition outcomes not independent.","Wave proxy is confirmed high/low swing structure, not Elliott 1-5/ABC labeling.","Wave was inspected before this holdout design, so selection bias remains.","No trade cost, slippage, macro/ETF/liquidation data or full 8-factor score.","No real-time prediction or risk grade produced by this test."],"comparisons":report}
    target=source/"holdout_evaluation.json"
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"saved":str(target),"comparisons":report,"warnings":result["warnings"]},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
