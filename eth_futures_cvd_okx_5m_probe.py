"""Strict OKX ETH-USDT-SWAP rolling 5-minute taker CVD feasibility collector.

Reads complete public trade-history pages until the start boundary is crossed.
Only a *single* verified 5-minute rolling window, not 24h/7d/14d, and
not a production report source. No existing spot/derivatives files are edited.
"""
import json
import math
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

INST = "ETH-USDT-SWAP"
ROOT = "https://www.okx.com/api/v5"
OUTPUT = Path("eth_futures_cvd_okx_5m_probe_latest.json")
MAX_PAGES = 400
WINDOW_SECONDS = 300


def api(path, params):
    url = ROOT + path + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url, headers={"User-Agent": "eth-cvd-monitor/2.0", "Accept": "application/json"}
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=25) as response:
                payload = json.load(response)
            if not isinstance(payload, dict) or payload.get("code") != "0":
                raise ValueError("OKX API did not return code 0: " + str(payload.get("code")))
            data = payload.get("data")
            if not isinstance(data, list):
                raise ValueError("Invalid OKX data")
            return data
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 3:
                raise
            time.sleep(1 + 2 * attempt)
    raise RuntimeError("Unreachable retry exit")


def finite_positive(value, label):
    n = float(value)
    if not math.isfinite(n) or n <= 0:
        raise ValueError("Invalid " + label)
    return n


def main():
    instruments = api("/public/instruments", {"instType": "SWAP", "instId": INST})
    matches = [x for x in instruments if x.get("instId") == INST and x.get("instType") == "SWAP"]
    if len(matches) != 1:
        raise ValueError("Unexpected instrument response")
    instrument = matches[0]
    if instrument.get("ctValCcy") != "ETH" or instrument.get("ctType") != "linear":
        raise ValueError("Cannot safely convert contracts to ETH")
    eth_per_contract = finite_positive(instrument["ctVal"], "ctVal")

    page_params = {"instId": INST, "limit": "100"}
    seen = set()
    rows = []
    last_min_id = None
    newest_ts = None
    boundary_ms = None
    oldest_ms = None
    pages = 0
    complete = False

    for page_index in range(MAX_PAGES):
        page = api("/market/history-trades", page_params)
        if not page:
            raise ValueError("Empty page before reaching 5m boundary")
        page_ids = [int(x["tradeId"]) for x in page]
        if len(set(page_ids)) != len(page_ids) or set(page_ids) & seen:
            raise ValueError("Duplicate trade IDs across history pages")
        if last_min_id is not None and max(page_ids) >= last_min_id:
            raise ValueError("History pagination failed to move strictly older")
        seen.update(page_ids)
        last_min_id = min(page_ids)
        page_stamps = [int(x["ts"]) for x in page]
        if newest_ts is None:
            newest_ts = max(page_stamps)
            boundary_ms = newest_ts - WINDOW_SECONDS * 1000
            if (datetime.now(timezone.utc).timestamp() * 1000 - newest_ts) > 60000:
                raise ValueError("Latest trade is stale")
        if max(page_stamps) > newest_ts + 1000:
            raise ValueError("Unexpected newer trades on an older history page")
        for trade in page:
            if trade.get("instId") != INST or trade.get("side") not in ("buy", "sell"):
                raise ValueError("Unexpected instrument or trade aggressor side")
            finite_positive(trade["sz"], "sz")
            if int(trade["ts"]) <= 0:
                raise ValueError("Invalid trade time")
        rows.extend(page)
        pages += 1
        oldest_ms = min(page_stamps)
        if oldest_ms <= boundary_ms:
            complete = True
            break
        if len(page) < 100:
            raise ValueError("Short history page before covering 5m window")
        page_params["after"] = str(last_min_id)
        time.sleep(0.12)

    if not complete:
        raise ValueError("Pagination cap reached without complete 5m coverage")
    in_window = [x for x in rows if boundary_ms < int(x["ts"]) <= newest_ts]
    if not in_window:
        raise ValueError("No trades in complete window")
    buy = sum(float(x["sz"]) * eth_per_contract for x in in_window if x["side"] == "buy")
    sell = sum(float(x["sz"]) * eth_per_contract for x in in_window if x["side"] == "sell")
    total = buy + sell
    result = {
        "status": "VERIFIED_5M_WINDOW_ONLY",
        "report_eligible": False,
        "exchange": "OKX",
        "symbol": INST,
        "market": "perpetual_swap",
        "unit": "ETH",
        "eth_per_contract": eth_per_contract,
        "window_start_utc": datetime.fromtimestamp(boundary_ms / 1000, timezone.utc).isoformat(),
        "window_end_utc": datetime.fromtimestamp(newest_ts / 1000, timezone.utc).isoformat(),
        "oldest_fetched_trade_utc": datetime.fromtimestamp(oldest_ms / 1000, timezone.utc).isoformat(),
        "complete_window": True,
        "history_pages": pages,
        "total_unique_fetched_trades": len(rows),
        "window_trade_count": len(in_window),
        "taker_buy_eth": buy,
        "taker_sell_eth": sell,
        "total_eth": total,
        "taker_buy_pct": buy / total * 100,
        "taker_sell_pct": sell / total * 100,
        "cvd_eth": buy - sell,
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": ROOT + "/market/history-trades?instId=" + INST,
        "limitations": [
            "Only this rolling 5m window is covered; 15m/1h/4h/24h/7d/14d not verified.",
            "Continuous scheduled capture, inter-run gaps and historical backfill not verified.",
            "Not Binance or total-market futures CVD; not yet eligible for ESI report."
        ]
    }
    temp = OUTPUT.with_suffix(".json.tmp")
    temp.write_text(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    os.replace(temp, OUTPUT)
    print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
