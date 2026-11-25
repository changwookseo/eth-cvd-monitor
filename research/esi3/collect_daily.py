"""Download completed monthly and daily Binance spot klines; no ESI2 writes."""
import csv, io, hashlib, zipfile, json, math
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.request import urlopen

BASE = "https://data.binance.vision/data/spot/"
OUT = Path("research/esi3/data")
START = date(2020,1,1)

def get(url):
    with urlopen(url, timeout=45) as response:
        return response.read()

def read_archive(url, interval, start, end):
    raw = get(url)
    digest = hashlib.sha256(raw).hexdigest()
    if digest != get(url+".CHECKSUM").decode().split()[0].lower():
        raise ValueError("checksum mismatch "+url)
    result=[]
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        names=[n for n in z.namelist() if n.endswith(".csv")]
        if len(names)!=1: raise ValueError("unexpected archive")
        with z.open(names[0]) as f:
            for r in csv.reader(io.TextIOWrapper(f, encoding="utf-8")):
                if r[0] in ("open_time","open time"): continue
                t=int(r[0]); divisor=1000000 if t>=10**15 else 1000
                dt=datetime.fromtimestamp(t/divisor,timezone.utc)
                if not start<=dt.date()<end: raise ValueError("date outside archive")
                o,h,l,c,v,b=map(float,[r[1],r[2],r[3],r[4],r[5],r[9]])
                if not all(map(math.isfinite,[o,h,l,c,v,b])) or not (0<l<=min(o,c)<=max(o,c)<=h and 0<=b<=v):
                    raise ValueError("invalid candle")
                if int(dt.timestamp())%interval: raise ValueError("misaligned candle")
                result.append([dt.isoformat(),(dt+timedelta(seconds=interval)).isoformat(),o,h,l,c,v,b,v-b,2*b-v,(2*b-v)/v if v else None])
    return result,digest

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    today=datetime.now(timezone.utc).date()
    month=today.replace(day=1)
    end=today-timedelta(days=1) # allow publication lag; exclusive
    manifest={"status":"INCOMPLETE","source":BASE,"requested_start":str(START),"end_exclusive":str(end),"archives":[],"errors":[]}
    rows={}
    d=START
    while d<end:
        monthly=d<month and d.day==1
        nxt=(d.replace(day=28)+timedelta(days=4)).replace(day=1) if monthly else d+timedelta(days=1)
        tag=d.strftime("%Y-%m" if monthly else "%Y-%m-%d")
        url=BASE+("monthly" if monthly else "daily")+"/klines/ETHUSDT/1d/ETHUSDT-1d-"+tag+".zip"
        try:
            batch,digest=read_archive(url,86400,d,nxt)
            for r in batch:
                if r[0] in rows: raise ValueError("duplicate timestamp")
                rows[r[0]]=r
            manifest["archives"].append({"url":url,"sha256":digest,"rows":len(batch)})
        except Exception as e:
            manifest["errors"].append({"url":url,"error":str(e)})
        d=nxt
    expected={(START+timedelta(days=i)).isoformat() for i in range((end-START).days)}
    missing=sorted(expected-{k[:10] for k in rows})
    manifest.update(rows=len(rows),missing_dates=missing,first=min(rows,default=None),last=max(rows,default=None))
    if not missing and not manifest["errors"]: manifest["status"]="VERIFIED"
    with (OUT/"binance_spot_daily.csv").open("w",newline="") as f:
        w=csv.writer(f); w.writerow(["open_utc","close_available_not_before_utc","open","high","low","close","volume_eth","buy_eth","sell_eth","cvd_eth","imbalance"]); w.writerows(rows[k] for k in sorted(rows))
    (OUT/"manifest.json").write_text(json.dumps(manifest,indent=2))
    if manifest["status"]!="VERIFIED": raise SystemExit(1)

if __name__=="__main__": main()
