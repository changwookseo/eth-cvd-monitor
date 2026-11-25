import json, urllib.request, urllib.parse, xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime,timezone
p=Path("research/esi3/data/liquidation_archive_inventory.json")
a={"status":"INCOMPLETE","checked_utc":datetime.now(timezone.utc).isoformat(),"sources":{}}
for period in ("daily","monthly"):
 prefix=f"data/futures/um/{period}/liquidationSnapshot/ETHUSDT/"
 keys=[]; marker=None; rec={"keys":keys}; a["sources"][period]=rec
 try:
  while True:
   q={"prefix":prefix,"max-keys":1000}
   if marker:q["marker"]=marker
   with urllib.request.urlopen("https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?"+urllib.parse.urlencode(q),timeout=60) as f:root=ET.fromstring(f.read())
   if not root.tag.endswith("ListBucketResult"):raise ValueError("unexpected listing")
   batch=[e.text for e in root.findall(".//{*}Contents/{*}Key")]
   keys.extend(batch)
   if root.findtext("{*}IsTruncated")!="true":break
   n=root.findtext("{*}NextMarker") or (batch[-1] if batch else None)
   if not n or n==marker:raise ValueError("pagination stalled")
   marker=n
  rec["zip_count"]=sum(k.endswith(".zip") for k in keys)
  rec["listing_complete"]=True
 except Exception as e:rec["error"]=str(e)
if all(r.get("listing_complete") for r in a["sources"].values()):a["status"]="INVENTORY_VERIFIED"
p.write_text(json.dumps(a,indent=2))
