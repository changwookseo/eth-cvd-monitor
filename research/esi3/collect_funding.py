import csv, io, json, hashlib, zipfile, math
from datetime import datetime, timezone, date
from collect_oi import OUT, get
BASE="https://data.binance.vision/data/futures/um/monthly/fundingRate/ETHUSDT/"
def main():
    oi=json.loads((OUT/"oi_manifest.json").read_text())
    assert oi["status"] in ("VERIFIED","VERIFIED_WITH_GAPS")
    start=date(2021,12,1)
    today=datetime.now(timezone.utc).date().replace(day=1)
    d=start
    events={}; errors=[]; archives=[]
    while d<today:
        month=d.strftime("%Y-%m")
        nxt=date(d.year+(d.month==12),d.month%12+1,1)
        u=BASE+f"ETHUSDT-fundingRate-{month}.zip"
        try:
            raw=get(u); sha=hashlib.sha256(raw).hexdigest()
            if sha!=get(u+".CHECKSUM").decode().split()[0].lower(): raise ValueError("checksum")
            local={}
            with zipfile.ZipFile(io.BytesIO(raw)) as z:
                names=[n for n in z.namelist() if n.endswith(".csv")]
                if len(names)!=1: raise ValueError("archive")
                with z.open(names[0]) as f:
                    for r in csv.DictReader(io.TextIOWrapper(f,encoding="utf-8-sig")):
                        t=datetime.fromtimestamp(int(r["calc_time"])/1000,timezone.utc)
                        rate=float(r["last_funding_rate"]); interval=int(r["funding_interval_hours"])
                        if not d<=t.date()<nxt or not math.isfinite(rate) or interval<=0 or t in local: raise ValueError("invalid event")
                        local[t]=(rate,interval)
            if not local: raise ValueError("empty")
            if set(local)&set(events): raise ValueError("duplicate")
            events.update(local); archives.append({"month":month,"sha256":sha,"rows":len(local)})
        except Exception as e: errors.append({"month":month,"error":str(e)})
        d=nxt
    ts=sorted(events)
    gaps=[]
    for a,b in zip(ts,ts[1:]):
        if (b-a).total_seconds()!=events[b][1]*3600: gaps.append({"previous":a.isoformat(),"next":b.isoformat()})
    if not ts or ts[0].date()!=start or ts[-1].date()!=(today.fromordinal(today.toordinal()-1)): errors.append({"error":"boundary coverage"})
    status="VERIFIED" if not errors and not gaps else "INCOMPLETE"
    with (OUT/"binance_funding_monthly_events.csv").open("w",newline="") as f:
        w=csv.writer(f);w.writerow(["observed_utc","funding_rate","interval_hours"]);w.writerows([t.isoformat(),*events[t]] for t in ts)
    (OUT/"funding_manifest.json").write_text(json.dumps({"status":status,"source":BASE,"start":str(start),"end_exclusive":str(today),"rows":len(ts),"archives":archives,"errors":errors,"gaps":gaps,"scope":"completed months only; current month not yet collected"},indent=2))
    if status!="VERIFIED": raise SystemExit(1)
if __name__=="__main__": main()
