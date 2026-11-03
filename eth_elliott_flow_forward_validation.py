"""As-of daily ETH structure + observed flow, forward 7/14/30d research evaluation.
The flow of UTC day D is known no earlier than the end of D; outcomes start at D close.
Chronological holdout, and horizon-spaced observations to reduce overlapping outcomes.
"""
import csv,json,math
from collections import Counter,defaultdict
from datetime import datetime,timezone,timedelta
from pathlib import Path
from statistics import mean
ROOT=Path("research_elliott")
HORIZONS=(7,14,30)
def read(path):
    with path.open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def value(r,k):
    try:
        x=float(r[k])
        return x if math.isfinite(x) else None
    except (KeyError,ValueError,TypeError):return None
def structure(prices,i):
    # All references from completed daily bars through i; no future pivots.
    if i<90:return None
    today=prices[i]
    close=value(today,"close")
    prior=prices[i-30:i]
    prior_hi=max(value(r,"high") for r in prior)
    prior_lo=min(value(r,"low") for r in prior)
    last90=prices[i-90:i+1]
    low=min(last90,key=lambda r:value(r,"low"))
    high=max(last90,key=lambda r:value(r,"high"))
    span=value(high,"high")-value(low,"low")
    if close is None or span<=0:return None
    if close>prior_hi:return "30d_breakout"
    if close<prior_lo:return "30d_breakdown"
    # Use most recent 90-day high and low, and the position in their range.
    location=(close-value(low,"low"))/span
    if location>=0.618:return "upper_range"
    if location<=0.382:return "lower_range"
    return "middle_range"
def main():
    prices=read(ROOT/"eth_daily.csv")
    flows=read(ROOT/"wave_flow_daily_join.csv")
    if len(prices)<365:raise RuntimeError("Insufficient daily history")
    dates=[datetime.fromisoformat(r["utc_date"]).date() for r in prices]
    if any((b-a).days!=1 for a,b in zip(dates,dates[1:])):raise RuntimeError("Missing daily candles")
    index={r["utc_date"]:i for i,r in enumerate(prices)}
    events=[]
    for f in flows:
        day=f["utc_date"];i=index.get(day)
        if i is None or i<90:continue
        # Exclude any day whose hourly evidence is not complete.
        if int(f["hours_observed"])!=24:continue
        label=structure(prices,i)
        if label is None:continue
        flow=f["flow_evidence"]
        if flow not in ("spot_buy_oi_up","spot_buy_oi_down","spot_sell_oi_up","spot_sell_oi_down"):continue
        base=value(prices[i],"close")
        if base is None or base<=0:continue
        event={"date":day,"structure":label,"flow":flow,"group":label+"|"+flow,"close":base}
        for h in HORIZONS:
            if i+h>=len(prices):
                event[f"ret_{h}d"]=None
                event[f"adverse_{h}d"]=None
                continue
            future=prices[i+1:i+h+1]
            event[f"ret_{h}d"]=(value(prices[i+h],"close")/base-1)*100
            event[f"adverse_{h}d"]=(min(value(r,"low") for r in future)/base-1)*100
        events.append(event)
    events.sort(key=lambda e:e["date"])
    # The last 30% of event dates are held out; earlier events with horizons
    # crossing the split are purged from the training statistics.
    split=int(len(events)*0.7)
    split_day=events[split]["date"] if len(events)>=10 else None
    report=[]
    for h in HORIZONS:
        def eligible(e):
            return e[f"ret_{h}d"] is not None
        train=[e for e in events[:split] if eligible(e) and
               (datetime.fromisoformat(e["date"]).date()+timedelta(days=h)).isoformat()<split_day] if split_day else []
        test=[e for e in events[split:] if eligible(e)]
        def select_nonoverlap(rows):
            last=None;selected=[]
            for e in rows:
                day=datetime.fromisoformat(e["date"]).date()
                if last is None or (day-last).days>=h:
                    selected.append(e);last=day
            return selected
        # Global horizon-spaced selection prevents multiple outcomes sharing the
        # same price interval. This is conservative and can yield small samples.
        train=select_nonoverlap(train)
        test=select_nonoverlap(test)
        def stats(rows):
            if not rows:return None
            returns=[r[f"ret_{h}d"] for r in rows]
            return {"n":len(rows),"up_pct":round(sum(v>0 for v in returns)/len(returns)*100,2),
                    "mean_return_pct":round(mean(returns),4),
                    "mean_adverse_low_pct":round(mean(r[f"adverse_{h}d"] for r in rows),4)}
        baseline=stats(test)
        # Learn the historically best category by training mean only.
        # Report its held-out result; not enough for strategy claims.
        train_groups=defaultdict(list)
        for e in train:train_groups[e["group"]].append(e)
        qualified={g:rows for g,rows in train_groups.items() if len(rows)>=5}
        selected=max(qualified,key=lambda g:mean(r[f"ret_{h}d"] for r in qualified[g])) if qualified else None
        held=[e for e in test if e["group"]==selected] if selected else []
        groups=defaultdict(list)
        for e in test:groups[e["group"]].append(e)
        report.append({"horizon_days":h,"split_date":split_day,"train_nonoverlap_n":len(train),"test_nonoverlap_n":len(test),
                       "test_baseline":baseline,"train_selected_group":selected,
                       "train_selected_group_n":len(qualified[selected]) if selected else 0,
                       "selected_group_test":stats(held),
                       "holdout_by_group":{g:stats(rows) for g,rows in sorted(groups.items())},
                       "interpretation":"insufficient_for_predictive_claim" if not selected or len(held)<10 else "descriptive_holdout_only"})
    result={"generated_utc":datetime.now(timezone.utc).isoformat(),"events":len(events),"last_event_date":events[-1]["date"] if events else None,
            "structure_definition":"Completed-day 30d breakout/breakdown, else position within trailing 90d high-low range (upper >=61.8%, lower <=38.2%). Objective proxy, not formal Elliott count.",
            "horizons":report,"limitations":["The day D spot/OI flow is not known until day D closes. Return from D close is a research approximation; executable entry would occur later and incur costs.","Non-overlap selection is global per horizon, reducing sample size; category counts are exploratory.","The selected category is chosen on chronological training only; no claim of statistical significance.","30-day forward outcomes for recent October dates are unavailable and excluded.","No October verified funding; funding excluded from this validation.","No CVD/OI forward causality established; historical exchange data availability and timestamp alignment still require audit.","No modifications to production scores or alerts."]}
    ROOT.mkdir(exist_ok=True)
    (ROOT/"wave_flow_forward_validation.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
