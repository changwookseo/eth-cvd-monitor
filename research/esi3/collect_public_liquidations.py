import csv,io,json,hashlib,urllib.request
from pathlib import Path
from decimal import Decimal
from collections import defaultdict
from datetime import datetime,timezone
base="https://huggingface.co/datasets/ochinimus/crypto-liquidation-ticks/resolve/main/"
out=Path("research/esi3/data")
audit={"source":base,"license":"CC BY 4.0","attribution":"ochinimus/crypto-liquidation-ticks","status":"INCOMPLETE"}
try:
 with urllib.request.urlopen(base+"liquidations_full_20260807.csv",timeout=180) as f:raw=f.read()
 audit["sha256"]=hashlib.sha256(raw).hexdigest()
 rows=[];seen=set();dup=0;bad=0
 for x in csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))):
  if x["exchange"]!="binance" or x["symbol"]!="ETHUSDT":continue
  try:
   ts=int(x["ts_ms"]);q=Decimal(x["size"]);p=Decimal(x["price"]);u=Decimal(x["usd"])
   if not all(v.is_finite() and v>0 for v in (q,p,u)) or x["event"] not in ("long_liquidated","short_liquidated"):raise ValueError()
   day=datetime.fromtimestamp(ts/1000,timezone.utc).date().isoformat()
   if not "2026-07-08"<=day<="2026-08-06":raise ValueError()
   key=tuple(x.items())
   if key in seen:dup+=1;continue
   seen.add(key);rows.append((day,x))
  except Exception:bad+=1
 daily=defaultdict(lambda:[0,Decimal(0),Decimal(0)])
 for day,x in rows:
  k=(day,x["event"]);daily[k][0]+=1;daily[k][1]+=Decimal(x["size"]);daily[k][2]+=Decimal(x["usd"])
 with (out/"public_liquidation_daily.csv").open("w",newline="") as f:
  w=csv.writer(f);w.writerow(["date","side","observed_rows","eth","reported_usd","coverage"])
  for (day,side),v in sorted(daily.items()):w.writerow([day,side,*v,"UNVERIFIED_CONTINUITY"])
 audit.update(status="PARSED_REVIEW_REQUIRED" if rows else "EMPTY",rows=len(rows),duplicates=dup,invalid=bad,observed_days=len(set(d for d,x in rows)),first_ms=min((int(x["ts_ms"]) for d,x in rows),default=None),last_ms=max((int(x["ts_ms"]) for d,x in rows),default=None))
except Exception as e:audit["error"]=str(e)
audit["note"]="Separate source; no overlapping rows added to Tardis. No complete daily coverage inferred; first day partial."
(out/"public_liquidation_audit.json").write_text(json.dumps(audit,indent=2))
