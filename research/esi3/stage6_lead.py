import json,math
from collections import Counter
from statistics import median
from stage5_pairs import sha,read
from stage3_features import D,load
def replay(e,s,x,idx,available):
 sign=1 if e["direction"]=="up" else -1
 p=e["pivots"];a,b=[idx[t["date"]] for t in p[2:4]]
 start=available[e["available_utc"]]
 v=sum(float(s[i]["volume_eth"]) for i in range(a+1,b))
 base=sign*sum(float(s[i]["cvd_eth"]) for i in range(a+1,b))/v if v>0 else None
 end=min(start+20,len(s)-1);signal=None
 if base is not None:
  for i in range(start+1,end+1):
   assert x[i]["available_utc"]>e["available_utc"]
   if sign*float(s[i]["cvd_eth"])/float(s[i]["volume_eth"])<base:
    signal=i;break
 return start,end,base,signal
def main():
 s,_=load("binance_spot_daily.csv");x=read("stage3_extended_daily.csv")
 p=D/"stage4_wave_candidates.jsonl";audit=json.loads((D/"stage4_wave_audit.json").read_text())
 assert sha(p)==audit["output_sha256"] and sha(D/"stage3_extended_daily.csv")==audit["source_sha256"]
 assert [r["open_utc"] for r in s]==[r["date"] for r in x]
 idx={r["date"]:i for i,r in enumerate(x)};av={r["available_utc"]:i for i,r in enumerate(x)}
 events=list(map(json.loads,p.read_text().splitlines()))
 def key(e):return (e["scale"],e["direction"],tuple(t["date"] for t in e["pivots"][:5]))
 matches={}
 for e in events:
  if e["label"]=="5":matches.setdefault(key(e),[]).append(e)
 rows=[]
 for e in events:
  if e["label"]!="4":continue
  start,end,base,signal=replay(e,s,x,idx,av)
  # Retrospective label only: earliest matching endpoint, even if before confirmation.
  m=sorted(matches.get(key(e),[]),key=lambda z:z["pivots"][-1]["date"])
  target=idx[m[0]["pivots"][-1]["date"]] if m else None
  in_window=target is not None and target<=end and target>start
  status="no_baseline" if base is None else "right_censored" if end-start<20 else "matched_before_or_at_confirmation" if target is not None and target<=start else "matched_in_window" if in_window else "no_matched_endpoint_in_window"
  lead=target-signal-1 if signal is not None and in_window else None
  sign=1 if e["direction"]=="up" else -1
  # Signal known at daily close; next-day open is executable-price proxy.
  entry=signal+1 if signal is not None else None
  returns={str(h):-sign*(float(s[entry+h-1]["close"])/float(s[entry]["open"])-1) if entry is not None and entry+h-1<len(s) else None for h in (1,3,5,10)}
  rows.append(dict(scale=e["scale"],direction=e["direction"],pivots=[t["date"] for t in e["pivots"]],available=e["available_utc"],baseline=base,signal_available=x[signal]["available_utc"] if signal is not None else None,target_date=x[target]["date"] if target is not None else None,status=status,lead_full_days=lead,strict_early=lead is not None and lead>=0,reversal_returns=returns))
  # Prefix replay must preserve a signal already emitted.
  if signal is not None:assert replay(e,s[:signal+1],x[:signal+1],idx,av)[3]==signal
 assert len(rows)==75
 def summarize(g):
  eligible=[r for r in g if r["status"] in ("matched_in_window","no_matched_endpoint_in_window")]
  matched=[r for r in eligible if r["status"]=="matched_in_window"];early=[r for r in matched if r["strict_early"]]
  return dict(total=len(g),statuses=dict(Counter(r["status"] for r in g)),eligible=len(eligible),matched=len(matched),early=len(early),median_full_days=median(r["lead_full_days"] for r in early) if early else None,unmatched_signals=sum(r["signal_available"] is not None for r in eligible if r["status"]=="no_matched_endpoint_in_window"),returns={str(h):dict(n=len(v),positive=sum(t>0 for t in v),median=median(v) if v else None) for h in (1,3,5,10) for v in [[r["reversal_returns"][str(h)] for r in eligible if r["reversal_returns"][str(h)] is not None]]})
 out=D/"stage6_lead_events.jsonl";out.write_text("".join(json.dumps(r)+"\n" for r in rows))
 (D/"stage6_lead_audit.json").write_text(json.dumps(dict(status="INITIAL_CAUSAL_REPLAY",summary={g:summarize([r for r in rows if g=="all" or r["direction"]==g]) for g in ("all","up","down")},source_sha256=sha(p),output_sha256=sha(out),limitations=["20 daily bars fixed exploratory horizon","overlapping candidates dependent","unmatched signals are not necessarily false price reversal signals","no active invalidation yet","daily close availability proxy; no costs","spot-only baseline; OI and funding incremental tests pending","no holdout yet"]),indent=2))
if __name__=="__main__":main()
