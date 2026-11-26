import csv,json,math,hashlib
from statistics import mean,median
from collections import Counter
from datetime import datetime
from stage3_features import D,load,slope
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(n):return list(csv.DictReader((D/n).open()))
def num(x):return float(x) if x not in ("",None) else None
def leg(a,b,sign,s,f,x):
 # Exclude both pivot dates: intraday pivot times unknown.
 ids=range(a+1,b);n=b-a-1
 r=dict(interior_days=n,calendar_days=b-a,price_directional_log_per_day=sign*math.log(float(s[b]["close"])/float(s[a]["close"]))/(b-a))
 for name,rows in (("spot",s),("futures",f)):
  v=[float(rows[i]["volume_eth"]) for i in ids];c=[float(rows[i]["cvd_eth"]) for i in ids]
  r[name+"_volume"]=sum(v) if n else None
  r[name+"_volume_per_day"]=mean(v) if n else None
  r[name+"_cvd"]=sum(c) if n else None
  r[name+"_cvd_per_day"]=mean(c) if n else None
  r[name+"_directional_imbalance"]=sign*sum(c)/sum(v) if n and sum(v)>0 else None
  cum=[0.]
  for z in c:cum.append(cum[-1]+z)
  r[name+"_directional_cvd_slope"]=sign*slope(cum) if n else None
  r[name+"_directional_cvd_acceleration"]=sign*(mean(c[n//2:])-mean(c[:n//2])) if n>=4 else None
 oi=[num(x[i]["oi_eth"]) for i in ids];fund=[num(x[i]["funding_daily_sum"]) for i in ids]
 r["oi_days"]=sum(v is not None for v in oi);r["funding_days"]=sum(v is not None for v in fund)
 r["oi_log_slope"]=slope([math.log(v) for v in oi]) if n>=2 and all(v is not None for v in oi) else None
 r["oi_change_pct"]=100*(oi[-1]/oi[0]-1) if n>=2 and all(v is not None for v in oi) else None
 r["funding_daily_mean"]=mean(fund) if n and all(v is not None for v in fund) else None
 r["funding_slope"]=slope(fund) if n>=2 and all(v is not None for v in fund) else None
 return r
def main():
 s,_=load("binance_spot_daily.csv");f,_=load("binance_futures_daily.csv");x=read("stage3_extended_daily.csv")
 assert [r["open_utc"] for r in s]==[r["open_utc"] for r in f]==[r["date"] for r in x]
 p=D/"stage4_wave_candidates.jsonl";audit=json.loads((D/"stage4_wave_audit.json").read_text())
 assert sha(p)==audit["output_sha256"]
 assert sha(D/"stage3_extended_daily.csv")==audit["source_sha256"]
 idx={r["open_utc"]:i for i,r in enumerate(s)}
 pairs={}
 for e in map(json.loads,p.read_text().splitlines()):
  if e["label"]!="5":continue
  z=e["pivots"];assert len(z)==6
  ii=[idx[t["date"]] for t in z];assert all(a<b for a,b in zip(ii,ii[1:]))
  assert all(t["confirmed_utc"]<=e["available_utc"] for t in z)
  assert all(x[i]["available_utc"]<=e["available_utc"] for i in range(ii[0],ii[-1]+1))
  key=tuple(ii);sign=1 if e["direction"]=="up" else -1
  if key in pairs:
   pairs[key]["scales"].append(e["scale"]);pairs[key]["available_utc"]=min(pairs[key]["available_utc"],e["available_utc"]);continue
  a=leg(ii[2],ii[3],sign,s,f,x);b=leg(ii[4],ii[5],sign,s,f,x)
  pairs[key]=dict(direction=e["direction"],scales=[e["scale"]],available_utc=e["available_utc"],pivots=[t["date"] for t in z],wave3=a,wave5=b,delta={k:b[k]-a[k] if a[k] is not None and b[k] is not None else None for k in a})
 rows=list(pairs.values())
 assert sum(len(r["scales"]) for r in rows)==40
 # Identical six pivots deduplicated; overlapping but nonidentical sequences retained.
 def summary(group):
  result={}
  for k in group[0]["delta"] if group else []:
   v=[r["delta"][k] for r in group if r["delta"][k] is not None]
   result[k]=dict(n=len(v),lower=sum(t<0 for t in v),equal=sum(t==0 for t in v),higher=sum(t>0 for t in v),median=median(v) if v else None,mean=mean(v) if v else None)
  return result
 out=D/"stage5_wave_pairs.jsonl";out.write_text("".join(json.dumps(r)+"\n" for r in rows))
 (D/"stage5_pair_audit.json").write_text(json.dumps(dict(status="PAIRED_DESCRIPTIVE_VERIFIED",raw_candidates=40,unique_exact_pairs=len(rows),directions=dict(Counter(r["direction"] for r in rows)),summary={g:summary([r for r in rows if g=="all" or r["direction"]==g]) for g in ("all","up","down")},source_sha256=sha(p),output_sha256=sha(out),limitations=["retrospective confirmed waves only; not a predictive signal","overlapping nonidentical pairs are dependent","daily flow excludes both pivot days; price close slope uses endpoint dates","OI and funding missing windows not imputed","liquidation excluded from paired inference due to incomplete continuity","no out-of-sample inference or significance tests yet"]),indent=2))
if __name__=="__main__":main()
