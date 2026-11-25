import csv,gzip,io,json,hashlib,urllib.request,time
from decimal import Decimal
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
out=Path("research/esi3/data")
days=[f"{y}-{m:02d}-01" for y in range(2020,2027) for m in range(1,13) if (y,m)<=(2026,11)]
def fetch(day):
 url="https://datasets.tardis.dev/v1/binance-futures/liquidations/"+day.replace("-","/")+"/ETHUSDT.csv.gz"
 r={"date":day,"url":url}
 for attempt in range(3):
  try:
   with urllib.request.urlopen(url,timeout=45) as f:raw=f.read()
   rows=list(csv.DictReader(io.StringIO(gzip.decompress(raw).decode())))
   sums={s:[Decimal(0),Decimal(0)] for s in ("buy","sell")}
   seen=set(); dup=0
   start=int(datetime.fromisoformat(day).replace(tzinfo=timezone.utc).timestamp()*1000000)
   for x in rows:
    if x["exchange"]!="binance-futures" or x["symbol"]!="ETHUSDT" or x["side"] not in sums:raise ValueError("instrument/side")
    q,p=Decimal(x["amount"]),Decimal(x["price"])
    if not q.is_finite() or not p.is_finite() or min(q,p)<=0:raise ValueError("quantity/price")
    if not start<=int(x["local_timestamp"])<start+86400000000:raise ValueError("capture date")
    int(x["timestamp"])
    key=tuple(x.items())
    if key in seen:dup+=1
    seen.add(key)
    sums[x["side"]][0]+=q;sums[x["side"]][1]+=q*p
   return dict(r,status="VERIFIED_SAMPLE" if rows and not dup else "REVIEW",rows=len(rows),exact_duplicate_rows=dup,sha256=hashlib.sha256(raw).hexdigest(),long_eth=str(sums["sell"][0]),short_eth=str(sums["buy"][0]),long_notional_usdt=str(sums["sell"][1]),short_notional_usdt=str(sums["buy"][1]))
  except Exception as e:
   r["error"]=str(e);time.sleep(2**attempt)
 return dict(r,status="FAILED")
with ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(fetch,days))
ok=[r for r in results if r["status"]=="VERIFIED_SAMPLE"]
manifest={"checked_utc":datetime.now(timezone.utc).isoformat(),"status":"FREE_SAMPLE_VERIFIED" if len(ok)==len(days) else "PARTIAL","target_days":len(days),"verified_days":len(ok),"research_days":2519,"uncovered_days":2519-len(ok),"coverage_note":"Monthly first-day samples only; Binance published forceOrder snapshots, not all liquidation events. Grouped by UTC capture date. Exact duplicate rows flagged, not silently removed. Notional is reported amount times reported price, not verified executed value. Raw files not redistributed.","sources":results}
(out/"tardis_free_liquidation_manifest.json").write_text(json.dumps(manifest,indent=2))
fields=["date","rows","long_eth","short_eth","long_notional_usdt","short_notional_usdt","sha256"]
with (out/"tardis_free_liquidation_daily.csv").open("w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(ok)
