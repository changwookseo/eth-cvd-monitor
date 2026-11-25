import csv,gzip,io,json,hashlib,urllib.request
from decimal import Decimal
from pathlib import Path
from datetime import datetime,timezone
out=Path("research/esi3/data")
audit={"checked_utc":datetime.now(timezone.utc).isoformat(),"status":"INCOMPLETE","samples":[]}
for day in ("2020/01/01","2021/05/01","2025/11/01","2026/11/01"):
 url="https://datasets.tardis.dev/v1/binance-futures/liquidations/"+day+"/ETHUSDT.csv.gz"
 r={"url":url,"date":day};audit["samples"].append(r)
 try:
  with urllib.request.urlopen(url,timeout=60) as f: raw=f.read()
  rows=list(csv.DictReader(io.StringIO(gzip.decompress(raw).decode())))
  totals={"buy":Decimal(0),"sell":Decimal(0)}
  for x in rows:
   if x["exchange"]!="binance-futures" or x["symbol"]!="ETHUSDT" or x["side"] not in totals:raise ValueError("unexpected instrument or side")
   q=Decimal(x["amount"]);p=Decimal(x["price"])
   if not q.is_finite() or not p.is_finite() or min(q,p)<=0:raise ValueError("nonpositive or invalid")
   totals[x["side"]]+=q
  r.update(status="SAMPLE_PARSED" if rows else "EMPTY_UNVERIFIED",rows=len(rows),sha256=hashlib.sha256(raw).hexdigest(),long_eth=str(totals["sell"]),short_eth=str(totals["buy"]))
 except Exception as e:r["error"]=str(e)
audit["status"]="SAMPLE_AVAILABLE" if any(r.get("status")=="SAMPLE_PARSED" for r in audit["samples"]) else "INCOMPLETE"
audit["coverage_note"]="Sample snapshots only; not complete exchange liquidation totals. No continuous coverage inferred."
(out/"tardis_liquidation_probe.json").write_text(json.dumps(audit,indent=2))
