import csv, math, json, hashlib
from pathlib import Path
from datetime import datetime,timedelta
from statistics import mean
D=Path("research/esi3/data")
def load(name):
 p=D/name
 rows=list(csv.DictReader(p.open()))
 dates=[datetime.fromisoformat(r["open_utc"]) for r in rows]
 assert len(set(dates))==len(dates)
 assert all(b-a==timedelta(days=1) for a,b in zip(dates,dates[1:]))
 assert all(datetime.fromisoformat(r["close_available_not_before_utc"])>=d+timedelta(days=1) for r,d in zip(rows,dates))
 return rows,hashlib.sha256(p.read_bytes()).hexdigest()
def slope(v):
 n=len(v);m=(n-1)/2
 return sum((i-m)*(x-mean(v)) for i,x in enumerate(v))/sum((i-m)**2 for i in range(n))
def features(s,f):
 assert [r["open_utc"] for r in s]==[r["open_utc"] for r in f]
 price=[math.log(float(r["close"])) for r in s]
 hi=[float(r["high"]) for r in s];lo=[float(r["low"]) for r in s]
 cvds=[[float(r["cvd_eth"]) for r in rows] for rows in (s,f)]
 vols=[[float(r["volume_eth"]) for r in rows] for rows in (s,f)]
 assert all(math.isfinite(x) for arr in [price,hi,lo,*cvds,*vols] for x in arr)
 assert all(x>0 for arr in vols for x in arr)
 for i,r in enumerate(s):
  o={"date":r["open_utc"],"available_utc":max(datetime.fromisoformat(r["close_available_not_before_utc"]),datetime.fromisoformat(f[i]["close_available_not_before_utc"])).isoformat()}
  for k in (3,5,10):
   j=i-k
   for label,v,cmp in (("high",hi,max),("low",lo,min)):
    window=v[j-k:i+1] if j>=k else []
    o[f"pivot_{label}_{k}"]=s[j]["open_utc"] if window and v[j]==cmp(window) and window.count(v[j])==1 else ""
  for n in (5,10,20):
   if i<n-1:continue
   a=i-n+1
   p=slope(price[a:i+1]);o[f"price_log_slope_{n}"]=p
   for label,c,v in zip(("spot","futures"),cvds,vols):
    cum=[0.]
    for x in c[a:i+1]:cum.append(cum[-1]+x)
    z=slope(cum);o[f"{label}_cvd_slope_{n}"]=z
    o[f"{label}_cvd_normalized_{n}"]=z/mean(v[a:i+1])
    o[f"{label}_divergence_{n}"]=int(p*z<0)
  yield o
def main():
 s,sh=load("binance_spot_daily.csv");f,fh=load("binance_futures_daily.csv")
 rows=list(features(s,f))
 for n in (20,100,len(rows)//2):
  assert list(features(s[:n],f[:n]))==rows[:n], "future leakage"
 assert abs(slope([1,3,5])-2)<1e-12
 fields=list(dict.fromkeys(k for r in rows for k in r))
 p=D/"stage3_features_daily.csv"
 with p.open("w",newline="") as h:
  w=csv.DictWriter(h,fieldnames=fields);w.writeheader();w.writerows(rows)
 audit={"status":"BASELINE_VERIFIED","rows":len(rows),"spot_sha256":sh,"futures_sha256":fh,"output_sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"prefix_invariance_tests":3,"pivot_counts":{k:sum(bool(r.get(k)) for r in rows) for k in fields if k.startswith("pivot_")},"pending":["OI and funding point-in-time joins","slope acceleration","synthetic pivot edge cases","parameter validation"],"note":"Daily baseline only; not stage 3 completion."}
 (D/"stage3_feature_audit.json").write_text(json.dumps(audit,indent=2))
if __name__=="__main__":main()
