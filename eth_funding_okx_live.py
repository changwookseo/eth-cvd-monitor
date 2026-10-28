"""Independent OKX ETH-USDT-SWAP indicative funding-rate snapshot.

This is NOT Binance funding, not market-wide, and not a realized settlement rate.
No API credentials required. Existing historical Binance funding is untouched.
"""
import json
import math
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = "https://www.okx.com/api/v5/public/funding-rate?instId=ETH-USDT-SWAP"
OUTPUT = Path("eth_funding_okx_latest.json")
MAX_AGE_SECONDS = 300


def finite_rate(value, field):
    result = float(value)
    if not math.isfinite(result) or abs(result) > 0.05:
        raise ValueError(f"Invalid {field}")
    return result


def timestamp_ms(value, field):
    try:
        stamp = int(value)
        if stamp <= 0:
            raise ValueError()
        return datetime.fromtimestamp(stamp / 1000, timezone.utc)
    except (TypeError, ValueError, OverflowError, OSError) as exc:
        raise ValueError(f"Invalid {field}") from exc


def collect(opener=urllib.request.urlopen, now=None):
    req = urllib.request.Request(
        URL, headers={"User-Agent": "eth-cvd-monitor/2.0", "Accept": "application/json"}
    )
    with opener(req, timeout=25) as response:
        payload = json.load(response)
    fetched = now or datetime.now(timezone.utc)
    if not isinstance(payload, dict) or payload.get("code") != "0":
        raise ValueError("OKX funding API did not return success")
    rows = payload.get("data")
    if not isinstance(rows, list) or len(rows) != 1:
        raise ValueError("Expected exactly one OKX funding observation")
    item = rows[0]
    if item.get("instId") != "ETH-USDT-SWAP" or item.get("instType") != "SWAP":
        raise ValueError("Unexpected funding instrument")
    observed = timestamp_ms(item.get("ts"), "ts")
    age = (fetched - observed).total_seconds()
    if not -30 <= age <= MAX_AGE_SECONDS:
        raise ValueError(f"Stale/future funding observation: {age:.1f}s")
    funding_time = timestamp_ms(item.get("fundingTime"), "fundingTime")
    if not -86400 <= (funding_time - fetched).total_seconds() <= 172800:
        raise ValueError("Funding settlement time outside plausible window")
    rate = finite_rate(item["fundingRate"], "fundingRate")
    next_time = (
        timestamp_ms(item["nextFundingTime"], "nextFundingTime").isoformat()
        if item.get("nextFundingTime") not in (None, "") else None
    )
    settled = (
        finite_rate(item["settFundingRate"], "settFundingRate")
        if item.get("settFundingRate") not in (None, "") else None
    )
    return {
        "source": URL,
        "exchange": "OKX",
        "symbol": "ETH-USDT-SWAP",
        "observed_at_utc": observed.isoformat(),
        "fetched_at_utc": fetched.isoformat(),
        "funding_rate_decimal": rate,
        "funding_rate_pct": rate * 100,
        "funding_time_utc": funding_time.isoformat(),
        "next_funding_time_utc": next_time,
        "settlement_state": item.get("settState"),
        "last_settlement_rate_decimal": settled,
        "rate_type": "indicative_current_period_not_realized",
        "status": "VERIFIED",
        "scope": "OKX ETH-USDT-SWAP only; not Binance or market-wide funding",
        "note": "Current-period indicative rate may change before settlement; not annualized or 8h-normalized.",
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
