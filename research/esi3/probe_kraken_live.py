import json, time
from decimal import Decimal
from pathlib import Path
from urllib.request import urlopen, Request
from datetime import datetime, timezone
out=Path("research/esi3/data/kraken_live_probe.json")
out.parent.mkdir(parents=True,exist_ok=True)
audit={"status":"INCOMPLETE","checked_utc":datetime.now(timezone.utc).isoformat(),"source":"https://api.kraken.com/0/public/Trades","pair":"ETHUSD"}
try:
    def fetch(since=None):
        url=audit["source"]+"?pair=ETHUSD"+("&since="+since if since else "")
        with urlopen(Request(url,headers={"User-Agent":"ESI3 research"}),timeout=30) as f:
            r=json.load(f)
        if r["error"]: raise ValueError(str(r["error"]))
        result=r["result"]
        keys=[k for k in result if k!="last"]
        if len(keys)!=1: raise ValueError("unexpected pair")
        return result[keys[0]],str(result["last"])
    rows,cursor=fetch()
    time.sleep(3)
    more,next_cursor=fetch(cursor)
    seen={}
    for r in rows+more:
        p,v,t=map(lambda x:Decimal(str(x)),r[:3])
        if not all(x.is_finite() for x in (p,v,t)) or min(p,v,t)<=0 or r[3] not in ("b","s"): raise ValueError("invalid trade")
        tid=str(r[6])
        if tid in seen and seen[tid]!=r: raise ValueError("conflicting trade ID")
        seen[tid]=r
    if not seen: raise ValueError("empty response")
    audit.update(status="API_SAMPLE_VERIFIED",first_count=len(rows),next_count=len(more),unique_count=len(seen),cursor=cursor,next_cursor=next_cursor,oldest_epoch=min(float(r[2]) for r in seen.values()),newest_epoch=max(float(r[2]) for r in seen.values()),buy_eth=str(sum((Decimal(r[1]) for r in seen.values() if r[3]=="b"),Decimal(0))),sell_eth=str(sum((Decimal(r[1]) for r in seen.values() if r[3]=="s"),Decimal(0))))
    audit["continuous_coverage_verified"]=False
except Exception as e: audit["error"]=str(e)
out.write_text(json.dumps(audit,indent=2))
raise SystemExit(0 if audit["status"]=="API_SAMPLE_VERIFIED" else 1)
