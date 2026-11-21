"""Research-only live ETH hourly condition snapshot. No trade recommendations or alerts.
Requires Binance spot/futures public endpoints; fail closed on errors or stale data.
"""
import json,urllib.request,urllib.parse
from datetime import datetime,timezone,timedelta
from pathlib import Path
NOW=datetime.now(timezone.utc)
OUT=Path("research_live")
def get(base,path,params):
    url=base+path+"?"+urllib.parse.urlencode(params)
    req=urllib.request.Request(url,headers={"User-Agent":"eth-cvd-monitor-research/1.0"})
    with urllib.request.urlopen(req,timeout=20) as resp:
        return json.load(resp)
def taker(k,kind):
    # Binance spot kline: quote vol index 7, taker buy quote index 10.
    # Binance futures kline: same indices.
    quote=float(k[7]);buy=float(k[10])
    return 100*(2*buy-quote)/quote if quote>0 else None
def main():
    report={"generated_utc":NOW.isoformat(),"status":"unavailable","source":"Binance public REST spot/futures; 1h completed candle proxies, not Kraken trade CVD","conditions":[],"errors":[]}
    try:
        spot=get("https://api.binance.com","/api/v3/klines",{"symbol":"ETHUSDT","interval":"1h","limit":5})
        fut=get("https://fapi.binance.com","/fapi/v1/klines",{"symbol":"ETHUSDT","interval":"1h","limit":5})
        oi=get("https://fapi.binance.com","/futures/data/openInterestHist",{"symbol":"ETHUSDT","period":"1h","limit":5})
        funding=get("https://fapi.binance.com","/fapi/v1/fundingRate",{"symbol":"ETHUSDT","limit":3})
        # A candle is complete only after its end timestamp.
        s={int(k[0]):k for k in spot if int(k[6])<int(NOW.timestamp()*1000)}
        f={int(k[0]):k for k in fut if int(k[6])<int(NOW.timestamp()*1000)}
        common=sorted(set(s)&set(f))
        if not common:raise ValueError("No common completed spot/futures hour")
        hour=common[-1];end=datetime.fromtimestamp((hour+3600000)/1000,timezone.utc)
        age=(NOW-end).total_seconds()/3600
        if age<0 or age>2:raise ValueError("Completed-hour data stale")
        # OI snapshot at/near the same completed hour; refuse mismatched observations.
        ois=sorted([(int(x["timestamp"]),float(x["sumOpenInterest"])) for x in oi])
        current=[(t,v) for t,v in ois if hour+3600000<=t<=hour+7200000]
        previous=[(t,v) for t,v in ois if hour<=t<hour+3600000]
        if not current or not previous:raise ValueError("No OI observations aligned to completed hour")
        old=previous[-1][1];new=current[0][1]
        if old<=0:raise ValueError("Invalid OI baseline")
        oi_pct=100*(new/old-1)
        spot_pct=taker(s[hour],"spot");fut_pct=taker(f[hour],"futures")
        if spot_pct is None or fut_pct is None:raise ValueError("Missing taker quote volume")
        tags=[]
        if spot_pct>0 and oi_pct>0:tags.append("spot_buy_oi_up")
        if spot_pct>0 and oi_pct<0:tags.append("spot_buy_oi_down")
        if spot_pct<0 and oi_pct>0:tags.append("spot_sell_oi_up")
        if spot_pct*fut_pct<0:tags.append("spot_futures_divergence")
        valid_funding=sorted([(int(x["fundingTime"]),float(x["fundingRate"])*100) for x in funding if int(x["fundingTime"])<=int(end.timestamp()*1000)])
        last=valid_funding[-1] if valid_funding else None
        if last and 0<=(end.timestamp()*1000-last[0])/3600000<=24 and oi_pct>0:
            if last[1]>0:tags.append("positive_funding_oi_up")
            if last[1]<0:tags.append("negative_funding_oi_up")
        report.update({"status":"observation_only","completed_hour_utc":datetime.fromtimestamp(hour/1000,timezone.utc).isoformat(),
                       "data_age_hours":round(age,3),"spot_cvd_pct":round(spot_pct,5),"futures_cvd_pct":round(fut_pct,5),
                       "oi_change_pct":round(oi_pct,5),"oi_observed_previous_utc":datetime.fromtimestamp(previous[-1][0]/1000,timezone.utc).isoformat(),
                       "oi_observed_current_utc":datetime.fromtimestamp(current[0][0]/1000,timezone.utc).isoformat(),
                       "funding_last_settled_pct":last[1] if last else None,
                       "funding_settled_utc":datetime.fromtimestamp(last[0]/1000,timezone.utc).isoformat() if last else None,
                       "conditions":tags,"interpretation":"Unvalidated live observation only; do not map historical win rates directly to probability."})
    except Exception as exc:
        report["errors"].append(str(exc))
    OUT.mkdir(exist_ok=True)
    (OUT/"eth_live_condition_snapshot.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
