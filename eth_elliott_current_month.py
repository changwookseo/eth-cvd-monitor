"""Append completed current-month daily ETH candles from official Binance daily archives.
Never substitute missing dates. Archive downloads can lag by one or more days.
"""
import csv,io,json,urllib.request,urllib.error,zipfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
PATH=Path("research_elliott/eth_daily.csv")
FIELDS=["utc_date","open","high","low","close","volume"]
def main():
    with PATH.open(newline="",encoding="utf-8") as f:
        original=list(csv.DictReader(f))
    if not original:raise RuntimeError("No monthly baseline")
    rows={r["utc_date"]:r for r in original}
    now=datetime.now(timezone.utc)
    start=datetime.fromisoformat(max(rows)).date()+timedelta(days=1)
    end=now.date()-timedelta(days=1)
    missing=[];added=[]
    for offset in range(max(0,(end-start).days+1)):
        day=start+timedelta(days=offset)
        key=day.isoformat()
        url=f"https://data.binance.vision/data/spot/daily/klines/ETHUSDT/1d/ETHUSDT-1d-{key}.zip"
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"eth-elliott-research/1.0"})
            with urllib.request.urlopen(req,timeout=20) as response:blob=response.read()
            with zipfile.ZipFile(io.BytesIO(blob)) as z:
                name=next(x for x in z.namelist() if x.endswith(".csv"))
                data=list(csv.reader(io.TextIOWrapper(z.open(name),encoding="utf-8-sig")))
            parsed=[]
            for r in data:
                if len(r)<6:continue
                try:
                    t=int(r[0]);t=t//1000 if t>10**14 else t
                    dt=datetime.fromtimestamp(t/1000,timezone.utc).date().isoformat()
                    vals=[float(r[i]) for i in (1,2,3,4,5)]
                except (ValueError,OverflowError):continue
                if dt!=key:continue
                if vals[1]<max(vals[0],vals[3],vals[2]) or vals[2]>min(vals[0],vals[3],vals[1]):raise ValueError("Invalid OHLC")
                parsed.append(dict(zip(FIELDS,[dt]+vals)))
            if len(parsed)!=1:raise ValueError("Expected one complete daily candle")
            rows[key]=parsed[0];added.append(key)
        except (urllib.error.HTTPError,urllib.error.URLError,zipfile.BadZipFile,ValueError,StopIteration) as e:
            missing.append({"date":key,"reason":str(e)[:120]})
    with PATH.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows[k] for k in sorted(rows))
    status={"generated_utc":now.isoformat(),"last_complete_utc_date_expected":end.isoformat(),"last_available_utc_date":max(rows),"added_days":len(added),"missing_daily_archives":missing,"current_through_yesterday":max(rows)==end.isoformat(),"notes":["Missing dates are never interpolated.","If daily archives lag, last available candle is stale; do not label as real-time."]}
    Path("research_elliott/current_month_status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(status,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
