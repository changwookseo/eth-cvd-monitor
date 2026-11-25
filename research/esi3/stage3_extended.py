import csv,json,math,hashlib
from collections import defaultdict
from datetime import datetime,timedelta
from stage3_features import D,load,features,slope
def read(n):return list(csv.DictReader((D/n).open()))
def dt(x):return datetime.fromisoformat(x)
def sha(n):return hashlib.sha256((D/n).read_bytes()).hexdigest()
def inputs():
 oi={}
 for r in read("binance_oi_daily.csv"):
  d=r["date_utc"];t=dt(r["observed_utc"]);v=float(r["oi_eth"])
  assert d not in oi and t.date().isoformat()==d and math.isfinite(v) and v>0
  oi[d]=(t,v)
 fund=defaultdict(list);seen=set()
 for n in ("binance_funding_monthly_events.csv","binance_funding_recent_events.csv"):
  for r in read(n):
   t=dt(r["observed_utc"]);v=float(r["funding_rate"]);h=float(r["interval_hours"])
   assert t not in seen and math.isfinite(v) and abs(v)<=.01 and h>0
   seen.add(t);fund[t.date().isoformat()].append((t,v,h))
 return oi,fund, len(seen)
def extend(base,oi,fund):
 history=[];prev={}
 for row in base:
  r=dict(row);d=r["date"][:10];end=dt(r["available_utc"]);start=dt(r["date"])
  x=oi.get(d);ev=[e for e in fund.get(d,[]) if start<=e[0]<min(end,start+timedelta(days=1))]
  ov=x[1] if x and x[0]<end else None
  # Only full 8h schedules with one event per slot; other schedules remain missing.
  fv=sum(e[1] for e in ev) if len(ev)==3 and all(e[2]==8 for e in ev) and sorted(e[0].hour for e in ev)==[0,8,16] and all(e[0].minute==0 and e[0].second==0 for e in ev) else None
  r.update(oi_eth=ov,funding_daily_sum=fv,funding_events=len(ev))
  history.append((math.log(ov) if ov is not None else None,fv))
  for n in (5,10,20):
   for j,label in enumerate(("oi_log","funding_daily")):
    v=[x[j] for x in history[-n:]]
    k=f"{label}_slope_{n}"
    r[k]=slope(v) if len(v)==n and all(x is not None for x in v) else None
   for label in ("price_log","spot_cvd","futures_cvd","oi_log","funding_daily"):
    k=f"{label}_slope_{n}";v=r.get(k);old=prev.get(k)
    r[k+"_acceleration"]=v-old if v is not None and old is not None else None
  prev=r;yield r
def main():
 s,_=load("binance_spot_daily.csv");f,_=load("binance_futures_daily.csv")
 oi,fund,count=inputs();base=list(features(s,f));rows=list(extend(base,oi,fund))
 assert len(oi)==1817 and count==5457
 missing=[r["date"][:10] for r in rows if r["date"][:10]>="2021-12-01" and r["oi_eth"] is None]
 assert missing==["2022-03-07","2024-02-16"],missing
 for n in (20,100,1000,2000):
  assert list(extend(list(features(s[:n],f[:n])),oi,fund))==rows[:n]
 # synthetic strict pivots: unique center, ties, flat, endpoints
 def sample(vals):
  return [dict(open_utc=f"2020-01-{i+1:02d}T00:00:00+00:00",close_available_not_before_utc=f"2020-01-{i+2:02d}T00:00:00+00:00",close=str(v),high=str(v),low=str(v),cvd_eth="0",volume_eth="1") for i,v in enumerate(vals)]
 for vals,high,low in [([1,2,3,4,3,2,1],True,False),([4,3,2,1,2,3,4],False,True),([1,2,4,4,3,2,1],False,False),([2]*7,False,False)]:
  a=sample(vals);z=list(features(a,a));assert not any(r["pivot_high_3"] or r["pivot_low_3"] for r in z[:-1]);assert bool(z[-1]["pivot_high_3"])==high and bool(z[-1]["pivot_low_3"])==low
 assert abs(slope([1,3,5])-2)<1e-12 and slope([3,3,3])==0
 fields=list(dict.fromkeys(k for r in rows for k in r));name="stage3_extended_daily.csv"
 with (D/name).open("w",newline="") as h:
  w=csv.DictWriter(h,fieldnames=fields);w.writeheader();w.writerows(rows)
 audit=dict(status="EXTENDED_FUNCTIONS_VERIFIED",rows=len(rows),oi_rows=len(oi),funding_events=count,oi_missing=missing,funding_complete_days=sum(r["funding_daily_sum"] is not None for r in rows),prefix_tests=4,synthetic_pivot_tests=4,coverage={k:sum(r.get(k) is not None for r in rows) for k in fields if "slope" in k},sha256={n:sha(n) for n in ("binance_spot_daily.csv","binance_futures_daily.csv","binance_oi_daily.csv","binance_funding_monthly_events.csv","binance_funding_recent_events.csv",name)},pending=["out-of-sample parameter efficacy; not established by function tests"],note="OI observation and funding settlement timestamps used as availability proxies; publication latency not measured. Missing windows blank.")
 (D/"stage3_extended_audit.json").write_text(json.dumps(audit,indent=2))
if __name__=="__main__":main()
