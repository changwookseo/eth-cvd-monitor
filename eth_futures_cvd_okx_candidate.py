"""Provisional OKX ETH-USDT-SWAP taker-volume CVD collector.

This is an independent candidate pipeline, NOT a report-approved futures CVD.
unit=0 was cross-checked against OKX 24h base-volume ticker on 2026-10-29.
The raw array [ts,sell,buy] mapping and unit=0 Crypto are confirmed in
OKX's official Trading Statistics API schema. An ETH raw-tape cross-check,
missing-bucket recovery and finished-report verification remain pending.
"""
import json
import math
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

INST = "ETH-USDT-SWAP"
ROOT = "https://www.okx.com/api/v5"
OUTPUT = Path("eth_futures_cvd_okx_candidate.json")
FIVE = 300000
HOUR = 3600000


def api(path, params):
    url = ROOT + path + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Accept": "application/json", "User-Agent": "eth-cvd-monitor/2.0"
    })
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=25) as response:
                obj = json.load(response)
            break
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == 4:
                raise
            time.sleep(2 + 2 * attempt)
    if obj.get("code") != "0" or not isinstance(obj.get("data"), list):
        raise ValueError("OKX API failure: " + str(obj.get("code")))
    return obj["data"]


def buckets(period, limit, step):
    rows = api("/rubik/stat/taker-volume-contract", {
        "instId": INST, "period": period, "unit": "0", "limit": str(limit)
    })
    if len(rows) < 25:
        raise ValueError("Too few OKX Rubik buckets")
    result = {}
    for row in rows:
        if not isinstance(row, list) or len(row) < 3:
            raise ValueError("Unexpected OKX taker row")
        ts = int(row[0])
        if ts % step != 0 or ts in result:
            raise ValueError("Unaligned or duplicate OKX bucket")
        sell, buy = float(row[1]), float(row[2])
        if not all(math.isfinite(v) and v >= 0 for v in (sell, buy)):
            raise ValueError("Invalid taker volume")
        result[ts] = (sell, buy)
    return result


def window(source, end, step, count):
    times = [end - (count - i) * step for i in range(count)]
    if not all(t in source for t in times):
        raise ValueError("Missing closed source bucket")
    sell = sum(source[t][0] for t in times)
    buy = sum(source[t][1] for t in times)
    total = buy + sell
    if total <= 0:
        raise ValueError("Zero total taker volume")
    return {
        "start_utc": datetime.fromtimestamp(times[0] / 1000, timezone.utc).isoformat(),
        "end_utc": datetime.fromtimestamp(end / 1000, timezone.utc).isoformat(),
        "bucket_count": count, "taker_buy_eth_provisional": buy,
        "taker_sell_eth_provisional": sell, "total_eth": total,
        "buy_pct_provisional": buy / total * 100,
        "sell_pct_provisional": sell / total * 100,
        "cvd_eth_provisional": buy - sell,
    }


def collect():
    fetched = datetime.now(timezone.utc)
    now_ms = int(fetched.timestamp() * 1000)
    five = buckets("5m", 100, FIVE)
    hour = buckets("1H", 30, HOUR)
    # Exclude the active candle AND wait 60 seconds for the last closed bucket.
    end5 = max(t + FIVE for t in five if t + FIVE <= now_ms - 60000)
    end1 = max(t + HOUR for t in hour if t + HOUR <= now_ms - 60000)
    if not 0 <= now_ms - end5 <= 12 * 60000:
        raise ValueError("Stale OKX 5m bucket")
    if not 0 <= now_ms - end1 <= 75 * 60000:
        raise ValueError("Stale OKX 1H bucket")

    windows = {
        "5m": window(five, end5, FIVE, 1),
        "15m": window(five, end5, FIVE, 3),
        "1h": window(five, end5, FIVE, 12),
        "4h": window(hour, end1, HOUR, 4),
        "24h": window(hour, end1, HOUR, 24),
    }
    # Independently compare unit=0 24h ETH volumes with the OKX swap ticker.
    ticker_rows = api("/market/ticker", {"instId": INST})
    if len(ticker_rows) != 1 or ticker_rows[0].get("instId") != INST:
        raise ValueError("Wrong OKX ticker")
    ticker = ticker_rows[0]
    ticker_eth = float(ticker["volCcy24h"])
    ticker_contracts = float(ticker["vol24h"])
    if not math.isfinite(ticker_eth) or ticker_eth <= 0 or ticker_contracts <= 0:
        raise ValueError("Invalid OKX ticker")
    ratio = windows["24h"]["total_eth"] / ticker_eth
    # The ticker is a rolling 24h window ending now, while the Rubik 24h
    # total ends at the last completed hour. During a sharp volume surge,
    # this alignment difference can exceed 20% without a unit error.
    # This broad check rejects gross (e.g. 10x) unit mistakes only.
    if not 0.5 <= ratio <= 1.5:
        raise ValueError("Gross OKX 24h volume/unit discrepancy")
    # Completed hour comparison is diagnostic; recently closed buckets can be revised.
    cross = None
    try:
        five_hour = window(five, end1, FIVE, 12)
        hourly = window(hour, end1, HOUR, 1)
        cross = {
            "hour_end_utc": hourly["end_utc"],
            "relative_total_difference": abs(
                five_hour["total_eth"] - hourly["total_eth"]
            ) / hourly["total_eth"],
        }
    except ValueError:
        pass
    return {
        "status": "PROVISIONAL_NOT_REPORT_VERIFIED",
        "report_eligible": False,
        "exchange": "OKX", "symbol": INST,
        "market": "perpetual_swap", "unit": "ETH",
        "source": ROOT + "/rubik/stat/taker-volume-contract",
        "observed_at_utc": windows["5m"]["end_utc"],
        "fetched_at_utc": fetched.isoformat(),
        "raw_array_semantics": "[ts,sell,buy] confirmed by official OKX API schema; ETH tape cross-check pending",
        "official_schema": "https://www.okx.com/docs-v5/en/#trading-statistics-rest-api-get-contract-taker-volume",
        "unit_mapping": "unit=0 base ETH; 24h independent OKX ticker cross-check",
        "ticker_24h_eth": ticker_eth, "ticker_24h_contracts": ticker_contracts,
        "closed_hourly_24h_to_ticker_eth_ratio": ratio,
        "volume_comparison_warning": not 0.9 <= ratio <= 1.1,
        "volume_comparison_alignment": "closed hourly 24h versus rolling ticker 24h; not identical endpoints",
        "last_complete_hour_consistency": cross,
        "windows": windows,
        "limitations": [
            "Provisional directional mapping; do not use as official ESI CVD.",
            "5m/15m/1h and 4h/24h use distinct closed-bucket end times.",
            "Historical 180-day futures CVD not backfilled.",
            "Rolling ticker and closed-hourly 24h volume may diverge during high volatility.",
            "No continuous schedule or report integration verified yet.",
            "Not Binance futures or market-wide futures CVD."
        ]
    }


def main():
    result = collect()
    tmp = OUTPUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                   encoding="utf-8")
    os.replace(tmp, OUTPUT)
    print(json.dumps(result, ensure_ascii=False, allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
