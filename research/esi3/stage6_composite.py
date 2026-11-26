import json,math
from statistics import mean,median
from stage6_lead import replay
from stage5_pairs import sha,read,num
from stage3_features import D,load
RULES=("baseline","persistent","divergence","spot_reversal","futures_confirm","oi_confirm","funding_confirm")
def signals(e,s,x,idx,av):
 start,end,base,_=replay(e,s,x,idx,av)
 sign=1 if e["direction"]=="up" else -1
 boundary=float(e["pivots"][3-2]["price"])
 out={};invalid=None
 if base is None:return out,invalid
 for i in range(start+1,end+1):
  # Wave4 overlap invalidation proxy: daily extreme crosses wave1 endpoint.
  if (sign==1 and float(s[i]["low"])<=boundary) or (sign==-1 and float(s[i]["high"])>=boundary):
   invalid=i;break
  z=x[i];p=num(z["price_log_slope_5"]);c=num(z["spot_cvd_normalized_5"]);f=num(z["futures_cvd_normalized_5"]);oi=num(z["oi_log_slope_5"]);fund=num(z["funding_daily_slope_5"])
  daily=[sign*float(s[j]["cvd_eth"])/float(s[j]["volume_eth"]) for j in range(i-2,i+1)]
  weak=all(v<base for v in daily) and i>=start+3
  div=weak and p is not None and c is not None and sign*p>0 and sign*c<0
  rev=weak and c is not None and sign*c<0
  tests=dict(baseline=daily[-1]<base,persistent=weak,divergence=div,spot_reversal=rev,futures_confirm=rev and f is not None and sign*f<0,oi_confirm=rev and oi is not None and oi<0,funding_confirm=rev and f is not None and sign*f<0 and oi is not None and oi<0 and fund is not None and sign*fund<0)
  for k,v in tests.items():
   if v and k not in out:out[k]=i
 return out,invalid
def main():
 s,_=load("binance_spot_daily.csv");x=read("stage3_extended_daily.csv")
 p=D/"stage4_wave_candidates.jsonl";a=json.loads((D/"stage4_wave_audit.json").read_text())
 assert sha(p)==a["output_sha256"] and sha(D/"stage3_extended_daily.csv")==a["source_sha256"]
 assert [r["open_utc"] for r in s]==[r["date"] for r in x]
 idx={r["date"]:i for i,r in enumerate(x)};av={r["available_utc"]:i for i,r in enumerate(x)}
 events=list(map(json.loads,p.read_text().splitlines()));rows=[]
 for e in events:
  if e["label"]!="4":continue
  start,end,base,_=replay(e,s,x,idx,av)
  if base is None or end-start<20:continue
  sign=1 if e["direction"]=="up" else -1
  m=[idx[t["pivots"][-1]["date"]] for t in events if t["label"]=="5" and t["scale"]==e["scale"] and t["direction"]==e["direction"] and t["pivots"][:5]==e["pivots"]]
  target=min(m) if m else None
  found,invalid=signals(e,s,x,idx,av)
  for k,i in found.items():assert signals(e,s[:i+1],x[:i+1],idx,av)[0].get(k)==i
  result={}
  for k in RULES:
   i=found.get(k);entry=i+1 if i is not None else None
   result[k]=dict(signal=x[i]["available_utc"] if i is not None else None,early=i is not None and target is not None and i<target<=end,lead=target-i-1 if i is not None and target is not None and i<target<=end else None,returns={str(h):-sign*(float(s[entry+h-1]["close"])/float(s[entry]["open"])-1) if entry is not None and entry+h-1<len(s) else None for h in (1,3,5,10)})
  rows.append(dict(direction=e["direction"],scale=e["scale"],available=e["available_utc"],invalid=x[invalid]["available_utc"] if invalid is not None else None,results=result))
 def summary(g):
  return {k:dict(candidates=len(g),signals=sum(r["results"][k]["signal"] is not None for r in g),early=sum(r["results"][k]["early"] for r in g),returns={str(h):dict(n=len(v),positive=sum(t>0 for t in v),median=median(v) if v else None,mean=mean(v) if v else None) for h in (1,3,5,10) for v in [[r["results"][k]["returns"][str(h)] for r in g if r["results"][k]["returns"][str(h)] is not None]]}) for k in RULES}
 out=D/"stage6_composite_events.jsonl";out.write_text("".join(json.dumps(r)+"\n" for r in rows))
 (D/"stage6_composite_audit.json").write_text(json.dumps(dict(status="EXPLORATORY_COMPOSITE_REPLAY",summary={g:summary([r for r in rows if g=="all" or r["direction"]==g]) for g in ("all","up","down")},chronological={g:summary([r for r in rows if (r["available"][:4]<"2024")== (g=="before2024")]) for g in ("before2024","2024onward")},source_sha256=sha(p),output_sha256=sha(out),limitations=["fixed exploratory rules, not optimized","chronological slices not independent holdout","overlapping candidates remain dependent","missing derivatives suppress corresponding signals","daily availability proxy","no transaction costs","invalidation uses wave1 overlap only"]),indent=2))
if __name__=="__main__":main()
