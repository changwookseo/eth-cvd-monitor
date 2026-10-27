"""As-of-safe multi-timeframe Elliott-inspired scenario map, NOT definitive wave counts."""
import csv,json
from datetime import datetime,timezone
from pathlib import Path
from collections import defaultdict
ROOT=Path("research_elliott")
def read():
    with (ROOT/"eth_daily.csv").open(newline="",encoding="utf-8") as f:
        return [{**r,**{k:float(r[k]) for k in ("open","high","low","close","volume")}} for r in csv.DictReader(f)]
def period(date,frame):
    d=datetime.fromisoformat(date).date()
    if frame=="daily":return date
    if frame=="weekly":return (d.fromordinal(d.toordinal()-d.weekday())).isoformat()
    return date[:7]
def aggregate(rows,frame):
    buckets=defaultdict(list)
    for r in rows:buckets[period(r["utc_date"],frame)].append(r)
    # Omit last bucket for weekly/monthly unless a later bucket exists.
    keys=sorted(buckets)
    if frame=="weekly" and datetime.fromisoformat(buckets[keys[-1]][-1]["utc_date"]).weekday()!=6:keys=keys[:-1]
    result=[]
    for key in keys:
        b=buckets[key]
        result.append({"date":key,"open":b[0]["open"],"high":max(x["high"] for x in b),"low":min(x["low"] for x in b),"close":b[-1]["close"],"volume":sum(x["volume"] for x in b)})
    return result
def pivots(rows,width):
    # Confirmation occurs only after 'width' complete candles to the right.
    out=[]
    for i in range(width,len(rows)-width):
        b=rows[i-width:i+width+1]
        highs=[x["high"] for x in b];lows=[x["low"] for x in b]
        kind=None
        if rows[i]["high"]==max(highs) and highs.count(rows[i]["high"])==1:kind="high"
        if rows[i]["low"]==min(lows) and lows.count(rows[i]["low"])==1:
            if kind:continue
            kind="low"
        if kind:
            out.append({"pivot_date":rows[i]["date"],"confirmed_date":rows[i+width]["date"],"kind":kind,"price":rows[i][kind]})
    clean=[]
    for p in out:
        if clean and clean[-1]["kind"]==p["kind"]:
            if (p["kind"]=="high" and p["price"]>clean[-1]["price"]) or (p["kind"]=="low" and p["price"]<clean[-1]["price"]):clean[-1]=p
        else:clean.append(p)
    return clean
def evaluate(rows,width):
    ps=pivots(rows,width);recent=ps[-8:]
    highs=[p for p in ps if p["kind"]=="high"];lows=[p for p in ps if p["kind"]=="low"]
    state="unclassified";invalidations={}
    if len(highs)>=2 and len(lows)>=2:
        hh=highs[-1]["price"]>highs[-2]["price"]
        hl=lows[-1]["price"]>lows[-2]["price"]
        lh=highs[-1]["price"]<highs[-2]["price"]
        ll=lows[-1]["price"]<lows[-2]["price"]
        state="uptrend_candidate" if hh and hl else "downtrend_candidate" if lh and ll else "corrective_or_transition_candidate"
        invalidations={"bullish_scenario_below":lows[-1]["price"],"bearish_scenario_above":highs[-1]["price"]}
    fib={}
    if len(ps)>=2:
        a,b=ps[-2],ps[-1]
        if a["kind"]!=b["kind"]:
            distance=abs(b["price"]-a["price"])
            if b["kind"]=="high":
                fib={"38.2pct_retracement":round(b["price"]-distance*.382,2),"50pct_retracement":round(b["price"]-distance*.5,2),"61.8pct_retracement":round(b["price"]-distance*.618,2)}
            else:
                fib={"38.2pct_retracement":round(b["price"]+distance*.382,2),"50pct_retracement":round(b["price"]+distance*.5,2),"61.8pct_retracement":round(b["price"]+distance*.618,2)}
    current=rows[-1] if rows else None
    last_pivot=ps[-1] if ps else None
    ongoing=None
    if current and last_pivot:
        tail=[x for x in rows if x["date"]>=last_pivot["pivot_date"]]
        highest=max(tail,key=lambda x:x["high"])
        lowest=min(tail,key=lambda x:x["low"])
        ongoing={"status":"unconfirmed","from_last_confirmed_pivot":last_pivot,"highest_since_pivot":{"date":highest["date"],"price":highest["high"]},"lowest_since_pivot":{"date":lowest["date"],"price":lowest["low"]},"latest_close":current["close"],"last_close_date":current["date"],"above_last_confirmed_high":bool(highs and current["close"]>highs[-1]["price"]),"below_last_confirmed_low":bool(lows and current["close"]<lows[-1]["price"])}
    return {"ongoing_unconfirmed_move":ongoing,"last_complete_candle":rows[-1]["date"] if rows else None,"candles":len(rows),"pivot_confirmation_bars":width,"structure":state,"last_confirmed_pivots":recent,"scenario_invalidation_reference":invalidations,"fibonacci_reference":fib,"elliott_1_to_5_or_abc_count":"not_determined","warning":"Candidates only; no retrospective pivot can be used before its confirmed_date."}
def main():
    rows=read()
    if not rows:raise RuntimeError("Missing ETH daily data")
    coverage=json.loads((ROOT/"coverage.json").read_text())
    current_path=ROOT/"current_month_status.json"
    freshness=json.loads(current_path.read_text()) if current_path.exists() else {"current_through_yesterday":False,"warning":"Current month archive not fetched"}
    results={}
    for frame,width in (("daily",5),("weekly",2),("monthly",1)):
        data=aggregate(rows,frame)
        if frame=="monthly" and data and data[-1]["date"]==rows[-1]["utc_date"][:7]:data=data[:-1]
        results[frame]=evaluate(data,width)
    result={"generated_utc":datetime.now(timezone.utc).isoformat(),"market":"Binance spot ETHUSDT","historical_month_coverage_complete":coverage["complete"],"latest_daily_archive_status":freshness,"timeframes":results,"interpretation":"Weekly/monthly are trend context; daily is structural confirmation; hourly CVD/OI/funding remain independent.","warnings":["NOT formal Elliott 1-5/ABC count. No deterministic full-wave classification is claimed.","Levels are scenario references, not executable signals or probabilities.","Weekly incomplete current candle excluded; current partial month not used for confirmed monthly bars.","Ongoing moves are unconfirmed and must not be treated as confirmed Elliott waves.","Missing data or exchange-specific price can change conclusions.","Existing 8-factor weights and production reports unchanged."]}
    (ROOT/"multi_timeframe_scenarios.json").write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print(json.dumps(result,indent=2,ensure_ascii=False))
if __name__=="__main__":main()
