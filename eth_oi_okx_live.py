"""Independent OKX ETH-USDT-SWAP live OI snapshot; never relabel as Binance OI."""
import json
import math
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = "https://www.okx.com/api/v5/public/open-interest?instType=SWAP&instId=ETH-USDT-SWAP"
OUTPUT = Path("eth_oi_okx_latest.json")
MAX_AGE_SECONDS = 300


def positive_number(item, key):
    value = float(item[key])
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"Invalid {key}")
    return value


def collect(opener=urllib.request.urlopen, now=None):
    req = urllib.request.Request(
        URL, headers={"User-Agent": "eth-cvd-monitor/2.0", "Accept": "application/json"}
    )
    with opener(req, timeout=25) as response:
        payload = json.load(response)
    fetched = now or datetime.now(timezone.utc)
    if not isinstance(payload, dict) or payload.get("code") != "0":
        raise ValueError("OKX did not return a successful response")
    matches = [
        row for row in payload.get("data", [])
        if row.get("instId") == "ETH-USDT-SWAP" and row.get("instType") == "SWAP"
    ]
    if len(matches) != 1:
        raise ValueError("Expected exactly one ETH-USDT-SWAP observation")
    item = matches[0]
    contracts = positive_number(item, "oi")
    base_eth = positive_number(item, "oiCcy")
    usd_value = positive_number(item, "oiUsd")
    observed = datetime.fromtimestamp(int(item["ts"]) / 1000, timezone.utc)
    age = (fetched - observed).total_seconds()
    if not -30 <= age <= MAX_AGE_SECONDS:
        raise ValueError("Stale or future OKX OI observation")
    return {
        "source": URL,
        "exchange": "OKX",
        "symbol": "ETH-USDT-SWAP",
        "observed_at_utc": observed.isoformat(),
        "fetched_at_utc": fetched.isoformat(),
        "timeframe": "snapshot",
        "value": base_eth,
        "unit": "ETH",
        "oi_contracts": contracts,
        "oi_usd": usd_value,
        "status": "VERIFIED",
        "failure_reason": None,
        "scope": "OKX ETH-USDT perpetual swap only; not Binance or market-wide OI",
    }


def main():
    snapshot = collect()
    temporary = OUTPUT.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, OUTPUT)
    print(json.dumps(snapshot, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
