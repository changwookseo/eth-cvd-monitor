import csv, json, math
from datetime import datetime, timezone, timedelta
from urllib.parse import urlencode
from collect_oi import OUT, get
BASE="https://fapi.binance.com/fapi/v1/fundingRate"
def main():
    m=json.loads((OUT/"funding_manifest.json").read_text())
    oi=json.loads((OUT/"oi_manifest.json").read_text())
    assert m["status"]=="VERIFIED" and oi["status"] in ("VERIFIED","VERIFIED_WITH_GAPS")
    start=datetime.fromisoformat(m["end_exclusive"]).replace(tzinfo=timezone.utc)
    end=datetime.fromisoformat(oi["end_exclusive"]).replace(tzinfo=timezone.utc)
    lo=int(start.timestamp()*1000); hi=int(end.timestamp()*1000)
    events={}; errors=[]
    try:
        cursor=lo
        while cursor<hi:
            q=urlencode(dict(symbol="ETHUSDT",startTime=cursor,endTime=hi-1,limit=1000))
            data=json.loads(get(BASE+"?"+q))
            if not isinstance(data,list): raise ValueError(str(data))
            if not data: break
            last=cursor-1
            for r in data:
                t=int(r["fundingTime"]); v=float(r["fundingRate"])
                if r["symbol"]!="ETHUSDT" or not cursor<=t<hi or t in events or not math.isfinite(v): raise ValueError("invalid event")
                events[t]=v; last=max(last,t)
            cursor=last+1
            if len(data)<1000: break
    except Exception as e: errors.append(str(e))
    step=28800000
    slots=[round(t/step)*step for t in events]
    expected=set(range(lo,hi,step))
    missing=sorted(expected-set(slots))
    if len(set(slots))!=len(slots) or set(slots)-expected or any(abs(t-s)>1000 for t,s in zip(events,slots)): errors.append("unexpected settlement schedule")
    status="VERIFIED" if not errors and not missing else "INCOMPLETE"
    def iso(t): return datetime.fromtimestamp(t/1000,timezone.utc).isoformat()
    with (OUT/"binance_funding_recent_events.csv").open("w",newline="") as f:
        w=csv.writer(f);w.writerow(["observed_utc","funding_rate","interval_hours"]);w.writerows([iso(t),events[t],8] for t in sorted(events))
    (OUT/"funding_recent_manifest.json").write_text(json.dumps(dict(status=status,source=BASE,start=start.isoformat(),end_exclusive=end.isoformat(),rows=len(events),expected=len(expected),missing=[iso(t) for t in missing],errors=errors),indent=2))
    if status!="VERIFIED": raise SystemExit(1)
if __name__=="__main__": main()
