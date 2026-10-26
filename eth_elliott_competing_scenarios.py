"""Two competing ETH medium-term scenarios, computed from completed daily candles.
Research-only: conditional price levels, not Elliott wave-count claims or probabilities.
"""
import csv,json
from datetime import datetime,timezone,timedelta
from pathlib import Path
ROOT=Path("research_elliott")
def main():
    with (ROOT/"eth_daily.csv").open(newline="",encoding="utf-8") as f:
        rows=[{**r,**{k:float(r[k]) for k in ("open","high","low","close","volume")}} for r in csv.DictReader(f)]
    if len(rows)<365:raise RuntimeError("Insufficient daily history")
    dates=[datetime.fromisoformat(r["utc_date"]).date() for r in rows]
    if any((b-a).days!=1 for a,b in zip(dates,dates[1:])):
        raise RuntimeError("Daily data has gaps; refuse to construct scenario")
    end=dates[-1]
    window=[r for r,d in zip(rows,dates) if d>=end-timedelta(days=365)]
    trough=min(window,key=lambda r:r["low"])
    subsequent=[r for r in window if r["utc_date"]>=trough["utc_date"]]
    peak=max(subsequent,key=lambda r:r["high"])
    latest=rows[-1]
    span=peak["high"]-trough["low"]
    valid=peak["utc_date"]>trough["utc_date"] and span>0
    recent=[r for r in rows if r["utc_date"]>=end-timedelta(days=30)]
    recent_low=min(recent,key=lambda r:r["low"])
    recent_high=max(recent,key=lambda r:r["high"])
    retracements={str(level):round(peak["high"]-span*level,2) for level in (0.382,0.5,0.618)} if valid else {}
    if valid:
        bullish={"name":"medium_term_bullish_pullback_hypothesis","hypothesis":"The advance from the trailing-year low to the subsequent high may be the start of a larger advance; current decline may be corrective.","hard_invalidation":{"rule":"completed_daily_close_below_origin_low","price":round(trough["low"],2),"triggered":latest["close"]<trough["low"]},"early_warning":{"rule":"completed_daily_close_below_recent_30d_low_prior_to_today","price":None,"triggered":None},"confirmation_reference":{"rule":"completed_daily_close_above_prior_swing_high","price":round(peak["high"],2),"triggered":latest["close"]>peak["high"]},"retracement_levels":retracements}
        bearish={"name":"medium_term_bearish_countertrend_hypothesis","hypothesis":"The advance may have been a countertrend rally within a larger bearish market.","weakening_reference":{"rule":"completed_daily_close_above_recent_rally_high","price":round(peak["high"],2),"triggered":latest["close"]>peak["high"]},"continuation_reference":{"rule":"completed_daily_close_below_recent_30d_low_prior_to_today","price":None,"triggered":None},"hard_invalidation":None,"hard_invalidation_reason":"A definitive long-cycle bearish Elliott count and its origin have not been established; a new high alone cannot formally invalidate every bearish count."}
        prior=[r for r in recent if r["utc_date"]<latest["utc_date"]]
        if prior:
            low=min(r["low"] for r in prior)
            bullish["early_warning"].update(price=round(low,2),triggered=latest["close"]<low)
            bearish["continuation_reference"].update(price=round(low,2),triggered=latest["close"]<low)
    else:
        bullish=bearish=None
    freshness=json.loads((ROOT/"current_month_status.json").read_text()) if (ROOT/"current_month_status.json").exists() else {}
    structural=json.loads((ROOT/"multi_timeframe_scenarios.json").read_text()) if (ROOT/"multi_timeframe_scenarios.json").exists() else {}
    output={"generated_utc":datetime.now(timezone.utc).isoformat(),"last_daily_candle_utc":latest["utc_date"],"latest_daily_close":latest["close"],"data_current_through_yesterday":freshness.get("current_through_yesterday",False),"anchor_method":"Trailing 365 calendar days: lowest low followed by highest high; fixed as of latest completed daily candle; descriptive, not an objective Elliott count.","anchor_valid":valid,"anchors":{"low":{"date":trough["utc_date"],"price":trough["low"]},"subsequent_high":{"date":peak["utc_date"],"price":peak["high"]}},"last_30d_range":{"low":recent_low["low"],"high":recent_high["high"]},"context_structures":{k:v.get("structure") for k,v in structural.get("timeframes",{}).items()},"scenarios":{"bullish":bullish,"bearish":bearish},"decision":"not_confirmed","risk_note":"No probabilistic advantage or trade recommendation inferred. Both scenarios can coexist. Invalidation references apply only to the stated hypotheses.","warnings":["365-day anchor changes when rolling window moves; historical scenario evaluation must recompute using each historical as-of date.","No formal Elliott 1-5/ABC wave counting.","Daily-close confirmation only; intraday breaches are not equivalent.","No CVD, OI, funding, ETF, macro or other 8-factor data combined yet.","If archive freshness is false, do not describe output as current market conditions."]}
    ROOT.mkdir(exist_ok=True)
    (ROOT/"competing_scenarios.json").write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(output,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
