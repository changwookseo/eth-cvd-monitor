import csv, io, json, hashlib, zipfile, math
from datetime import date, datetime, timedelta, timezone
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
BASE="https://data.binance.vision/data/futures/um/daily/metrics/ETHUSDT/"
OUT=Path("research/esi3/data")
def get(u):
    with urlopen(u,timeout=25) as r: return r.read()
def day(d):
    u=BASE+f"ETHUSDT-metrics-{d}.zip"
    try:
        raw=get(u)
        sha=hashlib.sha256(raw).hexdigest()
        if sha!=get(u+".CHECKSUM").decode().split()[0].lower(): raise ValueError("checksum")
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            names=[n for n in z.namelist() if n.endswith(".csv")]
            if len(names)!=1: raise ValueError("archive")
            with z.open(names[0]) as f:
                rows=list(csv.DictReader(io.TextIOWrapper(f,encoding="utf-8")))
        samples={}
        for r in rows:
            if r["symbol"]!="ETHUSDT": raise ValueError("symbol")
            t=datetime.fromisoformat(r["create_time"]).replace(tzinfo=timezone.utc)
            v=float(r["sum_open_interest"])
            if t.date()!=d or not math.isfinite(v) or v<=0 or t in samples: raise ValueError("invalid sample")
            samples[t]=v
        if not samples: raise ValueError("empty")
        t=max(samples)
        if t.hour!=23 or t.minute<55: raise ValueError("missing end of day snapshot")
        return {"date":str(d),"timestamp":t.isoformat(),"oi":samples[t],"samples":len(samples),"sha256":sha}
    except Exception as e: return {"date":str(d),"error":str(e)}
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    start=date(2021,12,1)
    end=datetime.now(timezone.utc).date()-timedelta(days=1)
    dates=[start+timedelta(days=i) for i in range((end-start).days)]
    with ThreadPoolExecutor(max_workers=8) as pool: results=list(pool.map(day,dates))
    good=[r for r in results if "oi" in r]
    bad=[r for r in results if "error" in r]
    with (OUT/"binance_oi_daily.csv").open("w",newline="") as f:
        w=csv.writer(f);w.writerow(["date_utc","observed_utc","oi_eth","samples"])
        w.writerows([r["date"],r["timestamp"],r["oi"],r["samples"]] for r in good)
    (OUT/"oi_manifest.json").write_text(json.dumps({"status":"VERIFIED" if good and not bad else "INCOMPLETE","source":BASE,"requested_start":str(start),"end_exclusive":str(end),"rows":len(good),"archives":good,"errors":bad},indent=2))
    if bad or not good: raise SystemExit(1)
if __name__=="__main__": main()
