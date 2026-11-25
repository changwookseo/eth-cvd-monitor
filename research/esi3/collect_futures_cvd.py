"""ETHUSDT USD-M daily futures delta, isolated research outputs."""
import csv, io, hashlib, zipfile, json
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from urllib.request import urlopen

START=date(2020,1,1)
END=date(2026,11,24)
BASE="https://data.binance.vision/data/futures/um/"
OUT=Path("research/esi3/data")
def get(url):
    with urlopen(url,timeout=45) as r:
        return r.read()
def main():
    rows={}
    audit=dict(status="INCOMPLETE",source=BASE,symbol="ETHUSDT",start=str(START),end_exclusive=str(END),archives=[],errors=[])
    d=START
    while d<END:
        monthly=d<END.replace(day=1)
        nxt=(d.replace(day=28)+timedelta(days=4)).replace(day=1) if monthly else d+timedelta(days=1)
        tag=d.strftime("%Y-%m" if monthly else "%Y-%m-%d")
        url=BASE+("monthly" if monthly else "daily")+"/klines/ETHUSDT/1d/ETHUSDT-1d-"+tag+".zip"
        try:
            raw=get(url)
            digest=hashlib.sha256(raw).hexdigest()
            if digest!=get(url+".CHECKSUM").decode().split()[0].lower(): raise ValueError("checksum mismatch")
            batch={}
            with zipfile.ZipFile(io.BytesIO(raw)) as z:
                names=[n for n in z.namelist() if n.endswith(".csv")]
                if len(names)!=1: raise ValueError("archive members")
                for r in csv.reader(io.StringIO(z.read(names[0]).decode("utf-8-sig"))):
                    if r and r[0].lower() in ("open_time","open time"): continue
                    t=int(r[0]); day=datetime.fromtimestamp(t/1000,timezone.utc).date()
                    if t%86400000 or int(r[6])!=t+86399999 or not d<=day<nxt: raise ValueError("timestamp")
                    o,h,l,c,v,b=map(Decimal,[r[1],r[2],r[3],r[4],r[5],r[9]])
                    if not all(x.is_finite() for x in (o,h,l,c,v,b)) or not (0<l<=min(o,c)<=max(o,c)<=h and 0<=b<=v): raise ValueError("invalid values")
                    if day in rows or day in batch: raise ValueError("duplicate date")
                    batch[day]=[day.isoformat()+"T00:00:00+00:00",(day+timedelta(days=1)).isoformat()+"T00:00:00+00:00",o,h,l,c,v,b,v-b,2*b-v,(2*b-v)/v if v else "",b/v if v else "",(v-b)/v if v else ""]
            rows.update(batch)
            audit["archives"].append(dict(url=url,sha256=digest,rows=len(batch)))
        except Exception as e:
            audit["errors"].append(dict(url=url,error=str(e)))
        d=nxt
    expected={START+timedelta(days=i) for i in range((END-START).days)}
    audit.update(rows=len(rows),expected=len(expected),missing_dates=[str(x) for x in sorted(expected-rows.keys())],first=str(min(rows)) if rows else None,last=str(max(rows)) if rows else None)
    OUT.mkdir(parents=True,exist_ok=True)
    dest=OUT/"binance_futures_daily.csv"
    with dest.open("w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["open_utc","close_available_not_before_utc","open","high","low","close","volume_eth","buy_eth","sell_eth","cvd_eth","imbalance","buy_fraction","sell_fraction"])
        w.writerows(rows[k] for k in sorted(rows))
    audit["csv_sha256"]=hashlib.sha256(dest.read_bytes()).hexdigest()
    if not audit["errors"] and not audit["missing_dates"]: audit["status"]="VERIFIED"
    (OUT/"futures_cvd_manifest.json").write_text(json.dumps(audit,indent=2)+"\n")
    return 0 if audit["status"]=="VERIFIED" else 1
if __name__=="__main__":
    raise SystemExit(main())
