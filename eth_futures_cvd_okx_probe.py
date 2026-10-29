"""Read-only OKX ETH-USDT-SWAP public-trades CVD feasibility probe.

This samples two history pages only. It does NOT claim complete 5m/24h
coverage, historical backfill, or report-ready futures CVD.
"""
import json
import math
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

INST = "ETH-USDT-SWAP"
ROOT = "https://www.okx.com/api/v5"
OUTPUT = Path("eth_futures_cvd_okx_probe_latest.json")


def get_json(path, params):
    url = ROOT + path + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url, headers={"User-Agent": "eth-cvd-monitor/2.0", "Accept": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=25) as response:
        payload = json.load(response)
    if not isinstance(payload, dict) or payload.get("code") != "0":
        raise ValueError("OKX public API did not return code 0")
    if not isinstance(payload.get("data"), list):
        raise ValueError("OKX data is not a list")
    return payload["data"]


def positive(value, name):
    result = float(value)
    if not math.isfinite(result) or result <= 0:
        raise ValueError("Invalid " + name)
    return result


def main():
    instruments = get_json("/public/instruments", {"instType": "SWAP", "instId": INST})
    matches = [x for x in instruments if x.get("instId") == INST and x.get("instType") == "SWAP"]
    if len(matches) != 1:
        raise ValueError("Expected one OKX swap instrument")
    instrument = matches[0]
    if instrument.get("ctValCcy") != "ETH" or instrument.get("ctType") != "linear":
        raise ValueError("Unexpected contract unit or type; no ETH conversion")
    eth_per_contract = positive(instrument["ctVal"], "ctVal")
    pages = []
    params = {"instId": INST, "limit": "100"}
    for i in range(2):
        rows = get_json("/market/history-trades", params)
        if not rows:
            raise ValueError("Empty public trade history page")
        pages.append(rows)
        ids = [int(x["tradeId"]) for x in rows]
        if len(set(ids)) != len(ids):
            raise ValueError("Duplicate trade IDs within a page")
        if i == 0:
            params["after"] = str(min(ids))
    first_ids = {x["tradeId"] for x in pages[0]}
    second_ids = {x["tradeId"] for x in pages[1]}
    if first_ids & second_ids:
        raise ValueError("Pagination overlaps; do not infer complete history")
    if max(int(x["tradeId"]) for x in pages[1]) >= min(int(x["tradeId"]) for x in pages[0]):
        raise ValueError("Second page not strictly older by trade ID")
    all_rows = pages[0] + pages[1]
    now = datetime.now(timezone.utc)
    buy = sell = 0.0
    stamps = []
    for row in all_rows:
        if row.get("instId") != INST or row.get("side") not in ("buy", "sell"):
            raise ValueError("Unexpected trade instrument or aggressor side")
        eth = positive(row["sz"], "sz") * eth_per_contract
        stamp = datetime.fromtimestamp(int(row["ts"]) / 1000, timezone.utc)
        age = (now - stamp).total_seconds()
        if not -60 <= age <= 93 * 86400:
            raise ValueError("Invalid trade observation timestamp")
        stamps.append(stamp)
        if row["side"] == "buy":
            buy += eth
        else:
            sell += eth
    # Aggregated per-contract taker volume is a possible scalable alternative
    # to hundreds of raw trade-history pages. Do not infer field order yet.
    rubik_5m = get_json("/rubik/stat/taker-volume-contract", {
        "instId": INST, "period": "5m", "unit": "1", "limit": "10"
    })
    if not rubik_5m or not all(isinstance(x, list) and len(x) >= 3 for x in rubik_5m):
        raise ValueError("Unexpected contract taker-volume schema")
    result = {
        "status": "DIAGNOSTIC_ONLY",
        "report_eligible": False,
        "complete_window": False,
        "exchange": "OKX",
        "symbol": INST,
        "market": "perpetual_swap",
        "unit": "ETH",
        "eth_per_contract": eth_per_contract,
        "rubik_5m_rows_returned": len(rubik_5m),
        "rubik_5m_first_3_raw_rows": rubik_5m[:3],
        "rubik_contract_taker_volume_source": ROOT + "/rubik/stat/taker-volume-contract?instId=" + INST + "&period=5m&unit=1",
        "rubik_column_semantics_verified": False,
        "sample_pages": len(pages),
        "sample_trade_count": len(all_rows),
        "sample_oldest_trade_utc": min(stamps).isoformat(),
        "sample_newest_trade_utc": max(stamps).isoformat(),
        "sample_coverage_seconds": (max(stamps) - min(stamps)).total_seconds(),
        "sample_taker_buy_eth": buy,
        "sample_taker_sell_eth": sell,
        "sample_cvd_eth": buy - sell,
        "fetched_at_utc": now.isoformat(),
        "source": ROOT + "/market/history-trades?instId=" + INST,
        "limitations": [
            "Two-page sample only, not an exhaustive time window.",
            "No 5m/15m/1h/4h/24h CVD claim.",
            "No Binance or market-wide futures CVD claim.",
            "No report integration until full pagination, continuity and historical coverage are verified."
        ]
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
