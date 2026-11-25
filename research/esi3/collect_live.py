"""Collect a verified Binance USD-M ETHUSDT research snapshot."""
import json
import os
import time
from decimal import Decimal
from pathlib import Path

from .binance_transport import read_market_data

SYMBOL = {"symbol": "ETHUSDT"}
BAR_MS = 300_000
OUT = Path(__file__).resolve().parent / "data" / "binance_live_latest.json"


def quantity(value):
    value = Decimal(value)
    if not value.is_finite() or value < 0:
        raise ValueError("Invalid trade quantity")
    return value


def collect():
    # Optionally reuse the existing five-minute Cron OI job.
    job_id = os.environ.get("ESI3_OI_CRON_JOB_ID")
    oi, oi_source = read_market_data("oi", SYMBOL, cron_job_id=int(job_id) if job_id else None)
    funding_job = os.environ.get("ESI3_FUNDING_CRON_JOB_ID")
    bars_job = os.environ.get("ESI3_FUTURES_BARS_CRON_JOB_ID")
    rates, rate_source = read_market_data(
        "funding", {**SYMBOL, "limit": 3}, cron_job_id=int(funding_job) if funding_job else None
    )
    bars, bar_source = read_market_data(
        "futures_bars", {**SYMBOL, "interval": "5m", "limit": 3},
        cron_job_id=int(bars_job) if bars_job else None,
    )
    now = time.time_ns() // 1_000_000
    interest = quantity(oi["openInterest"])
    if oi["symbol"] != SYMBOL["symbol"] or interest <= 0 or not -30_000 <= now - oi["time"] <= 600_000:
        raise ValueError("Invalid or stale OI")
    rate = max(rates, key=lambda row: row["fundingTime"])
    funding_rate = Decimal(rate["fundingRate"])
    if (rate["symbol"] != SYMBOL["symbol"] or not funding_rate.is_finite()
            or abs(funding_rate) > Decimal("0.01")
            or not -1000 <= now - rate["fundingTime"] <= 28_860_000):
        raise ValueError("Invalid or stale funding")
    for provenance in (oi_source, rate_source, bar_source):
        execution = provenance.get("cron_executed_at_epoch")
        if execution is not None and not -30_000 <= now - execution * 1000 <= 2 * BAR_MS:
            raise ValueError("Stale or future Cron response")
    # A bar still open when Cron captured it remains incomplete in that payload.
    captured_at = min(now, bar_source.get("cron_executed_at_epoch", now // 1000 + 1) * 1000)
    bar = max((row for row in bars if row[6] < captured_at), key=lambda row: row[0])
    if bar[6] - bar[0] != BAR_MS - 1 or not 0 < now - bar[6] <= 2 * BAR_MS:
        raise ValueError("Invalid or stale completed Binance futures bar")
    volume, buy = quantity(bar[5]), quantity(bar[9])
    if buy > volume:
        raise ValueError("Taker buy volume exceeds total volume")
    sell = volume - buy
    return {
        "exchange": "Binance USD-M", "symbol": SYMBOL["symbol"], "collected_epoch_ms": now,
        "open_interest": {"epoch_ms": oi["time"], "eth": str(interest), **oi_source},
        "funding": {"epoch_ms": rate["fundingTime"], "rate": str(funding_rate), **rate_source},
        "futures_cvd_5m": {"open_epoch_ms": bar[0], "end_exclusive_epoch_ms": bar[6] + 1,
                           "taker_buy_eth": str(buy), "taker_sell_eth": str(sell),
                           "net_eth": str(buy - sell), **bar_source},
    }


if __name__ == "__main__":
    snapshot = collect()
    temporary = OUT.with_suffix(".tmp")
    temporary.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    temporary.replace(OUT)
