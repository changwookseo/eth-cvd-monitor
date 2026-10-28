"""Collect Binance ETHUSDT open interest independently; never replace good data on failure."""
import json
import math
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = "https://fapi.binance.com/fapi/v1/openInterest?symbol=ETHUSDT"


def collect():
    request = urllib.request.Request(URL, headers={"User-Agent": "eth-cvd-monitor/2.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    fetched = datetime.now(timezone.utc)
    if payload.get("symbol") != "ETHUSDT":
        raise ValueError("Unexpected symbol")
    value = float(payload["openInterest"])
    observed = datetime.fromtimestamp(int(payload["time"]) / 1000, timezone.utc)
    age = (fetched - observed).total_seconds()
    if not math.isfinite(value) or value <= 0 or not -30 <= age <= 300:
        raise ValueError("Invalid or stale OI observation")
    return {
        "source": URL, "exchange": "Binance USD-M", "symbol": "ETHUSDT",
        "observed_at_utc": observed.isoformat(), "fetched_at_utc": fetched.isoformat(),
        "timeframe": "snapshot", "value": value, "unit": "ETH",
        "status": "VERIFIED", "failure_reason": None,
        "scope": "Binance ETHUSDT perpetual only; not market-wide OI"
    }


def main():
    attempt = {"source": URL, "fetched_at_utc": datetime.now(timezone.utc).isoformat()}
    try:
        snapshot = collect()
    except Exception as error:
        attempt.update(status="UNAVAILABLE", failure_reason=str(error))
        Path("eth_oi_attempt.json").write_text(json.dumps(attempt, indent=2) + "\n")
        raise
    Path("eth_oi_latest.json").write_text(json.dumps(snapshot, indent=2) + "\n")
    attempt.update(status="VERIFIED", failure_reason=None)
    Path("eth_oi_attempt.json").write_text(json.dumps(attempt, indent=2) + "\n")
    print(json.dumps(snapshot, indent=2))


if __name__ == "__main__":
    main()
