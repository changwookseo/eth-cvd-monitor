"""Independent long-horizon ETH spot OHLCV collection (Binance public monthly archives).
Research only. Never silently fill missing months or use unfinished candles.
"""
import csv,io,json,urllib.request,urllib.error,zipfile,calendar
from datetime import datetime,timezone,timedelta
from pathlib import Path
START=(2018,1)
OUT=Path("research_elliott")
FIELDS=["utc_date","open","high","low","close","volume"]
def months(start,end):
    y,m=start
    while (y,m)<=end:
        yield y,m
        m+=1
        if m==13:y,m=y+1,1
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"eth-elliott-research/1.0"}),timeout=35) as r:return r.read()
def main():
    now=datetime.now(timezone.utc)
    # Complete months only. Current partial month deliberately excluded.
    last=(now.year,now.month-1) if now.month>1 else (now.year-1,12)
    candles={};missing=[];available=[]
    for y,m in months(START,last):
        key=f"{y}-{m:02d}"
        url=f"https://data.binance.vision/data/spot/monthly/klines/ETHUSDT/1d/ETHUSDT-1d-{key}.zip"
        try:
            raw=get(url)
            with zipfile.ZipFile(io.BytesIO(raw)) as z:
                name=next(x for x in z.namelist() if x.endswith(".csv"))
                data=list(csv.reader(io.TextIOWrapper(z.open(name),encoding="utf-8-sig")))
            count=0
            for row in data:
                if len(row)<6:continue
                try:
                    timestamp=int(row[0])
                    if timestamp>10**14:timestamp//=1000
                    day=datetime.fromtimestamp(timestamp/1000,timezone.utc).date().isoformat()
                    vals=[float(row[k]) for k in (1,2,3,4,5)]
                except (ValueError,OverflowError):continue
                if vals[2]>min(vals[0],vals[3],vals[1]) or vals[1]<max(vals[0],vals[3],vals[2]):raise ValueError("Invalid OHLC")
                candles[day]=dict(zip(FIELDS,[day]+vals));count+=1
            if count==0:raise ValueError("No candles")
            available.append(key)
        except (urllib.error.HTTPError,urllib.error.URLError,zipfile.BadZipFile,ValueError,StopIteration) as e:
            missing.append({"month":key,"error":str(e)[:150]})
    OUT.mkdir(exist_ok=True)
    days=sorted(candles)
    with (OUT/"eth_daily.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(candles[d] for d in days)
    gaps=[]
    for a,b in zip(days,days[1:]):
        delta=(datetime.fromisoformat(b)-datetime.fromisoformat(a)).days
        if delta!=1:gaps.append({"after":a,"before":b,"missing_days":delta-1})
    status={"generated_utc":now.isoformat(),"source":"Binance public spot ETHUSDT 1d monthly klines","first_date":days[0] if days else None,"last_date":days[-1] if days else None,"daily_rows":len(days),"months_loaded":len(available),"missing_months":missing,"daily_gaps":gaps,"complete":bool(days) and not missing and not gaps,"notes":["Current partial month excluded.","Historical Binance ETHUSDT begins after 2018-01; early 404 months are reported, not imputed.","No guarantee exchange spot prices equal aggregate ETH market."]}
    (OUT/"coverage.json").write_text(json.dumps(status,indent=2),encoding="utf-8")
    print(json.dumps(status,ensure_ascii=False,indent=2))
    if len(days)<365*3:raise RuntimeError("Less than three years of daily data")
if __name__=="__main__":main()
