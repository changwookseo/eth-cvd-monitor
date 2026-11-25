import csv, io, json, hashlib, zipfile, math
from datetime import date, datetime, timezone, timedelta
from collections import Counter
from collect_oi import BASE, OUT, get

def repair(d):
    u=BASE+f"ETHUSDT-metrics-{d}.zip"
    audit={"date":d}
    try:
        raw=get(u)
        sha=hashlib.sha256(raw).hexdigest()
        if sha!=get(u+".CHECKSUM").decode().split()[0].lower(): raise ValueError("checksum")
        audit["sha256"]=sha
        samples={}
        issues=Counter()
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            names=[n for n in z.namelist() if n.endswith(".csv")]
            if len(names)!=1: raise ValueError("archive")
            with z.open(names[0]) as f:
                for r in csv.DictReader(io.TextIOWrapper(f,encoding="utf-8")):
                    if r["symbol"]!="ETHUSDT": issues["wrong_symbol"]+=1; continue
                    try:
                        t=datetime.fromisoformat(r["create_time"])
                        t=t.replace(tzinfo=timezone.utc) if t.tzinfo is None else t.astimezone(timezone.utc)
                        v=float(r["sum_open_interest"])
                    except (ValueError,TypeError): issues["parse_error"]+=1; continue
                    if str(t.date())!=d: issues["outside_date"]+=1; continue
                    if not math.isfinite(v) or v<=0: issues["invalid_value"]+=1; continue
                    if t in samples:
                        issues["identical_duplicate" if samples[t]==v else "conflicting_duplicate"]+=1
                    else: samples[t]=v
        audit["issues"]=dict(issues)
        audit["samples"]=len(samples)
        audit["last_observed"]=max(samples).isoformat() if samples else None
        target=datetime.fromisoformat(d+"T23:55:00+00:00")
        if any(v for k,v in issues.items() if k not in ("identical_duplicate","invalid_value")): raise ValueError("unresolved invalid or conflicting samples")
        if target not in samples: raise ValueError("missing exact 23:55 UTC snapshot")
        audit.update(timestamp=target.isoformat(),oi=samples[target])
    except Exception as e: audit["error"]=str(e)
    return audit

def main():
    p=OUT/"oi_manifest.json"
    c=OUT/"binance_oi_daily.csv"
    m=json.loads(p.read_text())
    with c.open(newline="") as f: rows=list(csv.DictReader(f))
    existing={r["date_utc"]:r for r in rows}
    archives={r["date"]:r for r in m["archives"]}
    assert len(existing)==len(rows)==m["rows"]==len(archives)
    assert set(existing)==set(archives)
    start=date.fromisoformat(m["requested_start"])
    end=date.fromisoformat(m["end_exclusive"])
    expected={str(start+timedelta(days=i)) for i in range((end-start).days)}
    assert set(existing)<=expected
    results=[repair(d) for d in sorted(expected-set(existing))]
    for r in results:
        if "error" not in r:
            d=r["date"]
            existing[d]={"date_utc":d,"observed_utc":r["timestamp"],"oi_eth":str(r["oi"]),"samples":str(r["samples"])}
            archives[d]=r
    missing=sorted(expected-set(existing))
    m.update(status="VERIFIED" if not missing else "VERIFIED_WITH_GAPS" if set(missing)=={"2022-03-07","2024-02-16"} else "INCOMPLETE",rows=len(existing),archives=[archives[d] for d in sorted(archives)],errors=[r for r in results if "error" in r],missing_dates=missing)
    (OUT/"oi_repair_audit.json").write_text(json.dumps(results,indent=2))
    with c.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["date_utc","observed_utc","oi_eth","samples"]);w.writeheader();w.writerows(existing[d] for d in sorted(existing))
    p.write_text(json.dumps(m,indent=2))
    if m["status"]=="INCOMPLETE": raise SystemExit(1)
if __name__=="__main__": main()
