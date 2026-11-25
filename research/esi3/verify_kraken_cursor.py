import json,time
from decimal import Decimal
from pathlib import Path
from urllib.request import urlopen
from datetime import datetime,timezone
p=Path("research/esi3/data/kraken_cursor_audit.json")
a={"status":"INCOMPLETE","checked_utc":datetime.now(timezone.utc).isoformat()}
try:
 def fetch(c):
  with urlopen("https://api.kraken.com/0/public/Trades?pair=ETHUSD"+("&since="+c if c else ""),timeout=30) as f:r=json.load(f)
  if r["error"]:raise ValueError(str(r["error"]))
  d=r["result"];return next(v for k,v in d.items() if k!="last"),str(d["last"])
 rows,c=fetch(None); initial=c; seen={str(r[6]):r for r in rows}; calls=[]
 for i in range(12):
  time.sleep(5)
  rr,n=fetch(c)
  if int(n)<int(c):raise ValueError("cursor regression")
  for r in rr:
   k=str(r[6])
   if k in seen and seen[k]!=r:raise ValueError("conflicting duplicate")
   if r[3] not in ("b","s") or not Decimal(r[1]).is_finite() or Decimal(r[1])<=0:raise ValueError("invalid trade")
   seen[k]=r
  calls.append({"count":len(rr),"cursor":n})
  c=n
  if int(c)>int(initial):break
 end=max(Decimal(str(r[2])) for r in seen.values());start=min(Decimal(str(r[2])) for r in seen.values())
 a.update(initial_cursor=initial,final_cursor=c,calls=calls,unique_count=len(seen),sample_span_seconds=float(end-start),windows={})
 for m in (5,15,60,240,1440):
  if end-start<m*60:a["windows"][str(m)]={"status":"INSUFFICIENT_SPAN"};continue
  subset=[r for r in seen.values() if end-m*60<Decimal(str(r[2]))<=end]
  b=sum((Decimal(r[1]) for r in subset if r[3]=="b"),Decimal(0));s=sum((Decimal(r[1]) for r in subset if r[3]=="s"),Decimal(0))
  a["windows"][str(m)]={"status":"SAMPLE_ONLY","buy_eth":str(b),"sell_eth":str(s),"cvd_eth":str(b-s),"buy_pct":str(b/(b+s)*100) if b+s else None}
 a["status"]="CURSOR_ADVANCED" if int(c)>int(initial) else "CURSOR_UNCHANGED"
 a["continuous_coverage_verified"]=False
except Exception as e:a["error"]=str(e)
p.write_text(json.dumps(a,indent=2))
