import csv,json,hashlib
from collections import Counter
from datetime import datetime
from stage3_features import D,load
def classify(p):
 # Direction-normalized prices; strict non-diagonal, non-truncated baseline.
 if len(p)<2:return None
 direction=1 if p[0][1]=="low" else -1
 x=[direction*z[2] for z in p]
 if any((b-a)*((-1)**i)<=0 for i,(a,b) in enumerate(zip(x,x[1:]))):return None
 if len(x)>=3 and x[2]<=x[0]:return None
 if len(x)>=4 and x[3]<=x[1]:return None
 if len(x)>=5 and x[4]<=x[1]:return None
 if len(x)>=6 and (x[5]<=x[3] or x[3]-x[2]<min(x[1]-x[0],x[5]-x[4])):return None
 # Zigzag-like correction only, not all Elliott correction families.
 if len(x)>=7 and x[6]<=x[0]:return None
 if len(x)>=8 and x[7]>=x[5]:return None
 if len(x)>=9 and x[8]>=x[6]:return None
 return direction
def scan(rows,prices):
 events=[]
 for k in (3,5,10):
  piv=[];emitted=set()
  for r in rows:
   available=r["available_utc"]
   found=[(r[f"pivot_{kind}_{k}"],kind) for kind in ("high","low") if r[f"pivot_{kind}_{k}"]]
   if len(found)!=1:continue # intraday order unknown for dual pivots
   d,kind=found[0];price=float(prices[d][kind]);p=(d,kind,price,available)
   assert d<available
   if piv and piv[-1][1]==kind:
    if (price>piv[-1][2] if kind=="high" else price<piv[-1][2]):piv[-1]=p
    else:continue
   else:piv.append(p)
   for n in range(2,min(9,len(piv))+1):
    seq=piv[-n:];direction=classify(seq)
    if direction is None:continue
    key=tuple((z[0],z[1]) for z in seq)
    if key in emitted:continue
    emitted.add(key)
    events.append(dict(scale=k,direction="up" if direction==1 else "down",label=str(n-1) if n<=6 else "ABC"[n-7],status="candidate",available_utc=available,pivots=[dict(date=z[0],kind=z[1],price=z[2],confirmed_utc=z[3]) for z in seq]))
 return sorted(events,key=lambda e:(e["available_utc"],e["scale"],e["label"]))
def main():
 s,_=load("binance_spot_daily.csv");prices={r["open_utc"]:r for r in s}
 path=D/"stage3_extended_daily.csv";rows=list(csv.DictReader(path.open()))
 assert [r["date"] for r in rows]==list(prices)
 audit=json.loads((D/"stage3_extended_audit.json").read_text())
 assert hashlib.sha256(path.read_bytes()).hexdigest()==audit["sha256"][path.name]
 def seq(x):return [(str(i),"low" if i%2==0 else "high",v,"") for i,v in enumerate(x)]
 assert classify(seq([100,120,110,150,130,160]))==1
 assert classify(seq([100,120,90])) is None
 assert classify(seq([100,120,110,150,119])) is None
 assert classify(seq([100,130,125,145,135,165])) is None
 assert classify(seq([100,120,110,150,130,145])) is None
 assert classify(seq([100,120,110,150,130,160,140,150,135]))==1
 assert classify([(d,"high" if k=="low" else "low",300-v,t) for d,k,v,t in seq([100,120,110,150,130,160])])==-1
 events=scan(rows,prices)
 for n in (100,500,1000,2000):
  assert scan(rows[:n],prices)==[e for e in events if e["available_utc"]<=rows[n-1]["available_utc"]]
 for e in events:
  assert all(p["confirmed_utc"]<=e["available_utc"] for p in e["pivots"])
 out=D/"stage4_wave_candidates.jsonl"
 out.write_text("".join(json.dumps(e,separators=(",",":"))+"\n" for e in events))
 counts=Counter(f'{e["scale"]}:{e["direction"]}:{e["label"]}' for e in events)
 (D/"stage4_wave_audit.json").write_text(json.dumps(dict(status="BASELINE_VERIFIED",rows=len(rows),events=len(events),counts=dict(counts),synthetic_tests=7,prefix_tests=4,source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),output_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),limitations=["overlapping candidates not unique waves","historical candidate events immutable; not current active labels","strict standard impulse and zigzag-like correction only","no diagonals, truncations, nested degree inference or probability calibration","daily extremes cannot resolve dual-pivot intraday order","parameter efficacy and independent label validation pending"]),indent=2))
if __name__=="__main__":main()
