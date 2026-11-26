import csv,json,math
from pathlib import Path
from statistics import mean
D=Path(__file__).parent/"data"
def read(n):
 with (D/n).open() as f:return list(csv.DictReader(f))
BETA1_ALARM_COOLDOWN=3
def run():
 x=read("stage3_extended_daily.csv");s=read("binance_spot_daily.csv")
 assert len(x)==len(s) and all(a["date"]==b["open_utc"] for a,b in zip(x,s))
 n=len(x);out={}
 def v(i,k):return float(x[i][k]) if x[i].get(k) else math.nan
 def share(i):
  q=s[i-2:i+1];return sum(float(r["buy_eth"]) for r in q)/sum(float(r["volume_eth"]) for r in q)
 for d in (1,-1):
  targets=[]
  for i in range(5,n-10):
   a=[float(r["low" if d==1 else "high"]) for r in s[i-5:i+6]]
   if d*a[5]==min(d*z for z in a) and a.count(a[5])==1 and d*(float(s[i+10]["close"])/a[5]-1)>=.05:targets.append(i)
  events=[]
  def c(i):return v(i,"spot_cvd_normalized_5")
  def onset(j):return d*(c(j)-c(j-1))>0 and d*(c(j-1)-c(j-2))<=0
  for i in range(20,n-10):
   p=v(i,"price_log_slope_5");a=v(i,"price_log_slope_5_acceleration");delta=c(i)-c(i-1)
   base=delta>0 and share(i)>share(i-3) if d==1 else c(i)<0
   confirm=delta>0 and a>0 and c(i)<0 if d==1 else c(i)<0 and v(i,"oi_log_slope_5")<0
   lag=next((k for k in range(1,6) if onset(i-k)),None)
   seq=lag is not None and d*(c(i)-c(i-lag-1))>0
   price=d*p<0
   events.append((i,dict(base=price and base,confirm=price and confirm,lag=price and seq,combined=price and base and seq,combinedConfirm=price and confirm and seq,union=price and (base or seq))))
  def stat(ss,tt):
   leads=[j-i-1 for i in ss for j in [next((j for j in tt if i<j<=i+5),None)] if j is not None]
   ret=[d*(float(s[i+10]["close"])/float(s[i+1]["open"])-1) for i in ss]
   return dict(signals=len(ss),targets=len(tt),matched=len(leads),detected=sum(any(i<j<=i+5 for i in ss) for j in tt),positive=sum(z>0 for z in ret),mean=mean(ret) if ret else None,lead=mean(leads) if leads else None)
  for rule in ("base","confirm","lag","combined","combinedConfirm","union"):
   ss=[]
   for i,e in events:
    if e[rule] and (not ss or i-ss[-1]>=(BETA1_ALARM_COOLDOWN if rule=="union" else 10)):ss.append(i)
   out[f"{d}:{rule}"]=dict(all=stat(ss,targets),pre=stat([i for i in ss if x[i]["date"]<"2024"],[i for i in targets if x[i]["date"]<"2024"]),post=stat([i for i in ss if x[i]["date"]>="2024"],[i for i in targets if x[i]["date"]>="2024"]))
 return dict(status="EXPLORATORY",rows=n,out=out)
if __name__=="__main__":
 print(json.dumps(run(),indent=2))
