"""Collect and validate the funding interval between the monthly and OI datasets."""
import argparse
import csv
import hashlib
import io
import json
import sys
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from research.esi3.binance_transport import read_market_data

OUT = Path(__file__).resolve().parent / "data"
STEP = 8 * 60 * 60 * 1000
TIMESTAMP_TOLERANCE_MS = 1000
# Research sanity threshold in raw rate units. 0.01 represents 1%.
RATE_SANITY_LIMIT = Decimal("0.01")


def iso(milliseconds):
    return datetime.fromtimestamp(milliseconds / 1000, timezone.utc).isoformat()


def collect(start, end, cron_job_id):
    expected = set(range(start, end, STEP))
    events = {}
    pages = []
    cursor = start
    while cursor < end:
        params = dict(symbol="ETHUSDT", startTime=cursor, endTime=end - 1, limit=1000)
        data, provenance = read_market_data("funding", params, cron_job_id=cron_job_id)
        if not isinstance(data, list):
            raise ValueError("Expected a Binance funding event array")
        pages.append(provenance)
        last = cursor - 1
        for row in data:
            timestamp = row["fundingTime"]
            rate = Decimal(row["fundingRate"])
            if (row["symbol"] != "ETHUSDT" or type(timestamp) is not int
                    or not cursor <= timestamp < end or timestamp in events):
                raise ValueError("Invalid or duplicate Binance funding event")
            if not rate.is_finite() or abs(rate) > RATE_SANITY_LIMIT:
                raise ValueError(f"Invalid funding rate at {iso(timestamp)}")
            events[timestamp] = rate
            last = max(last, timestamp)
        if len(data) < params["limit"]:
            break
        if cron_job_id is not None:
            raise ValueError("A fixed Cron URL cannot provide a second funding page")
        cursor = last + 1

    slots = [(timestamp, ((timestamp + STEP // 2) // STEP) * STEP)
             for timestamp in events]
    covered = {slot for _, slot in slots}
    if len(covered) != len(events):
        raise ValueError("Duplicate 8-hour funding slot")
    if covered - expected or any(abs(ts - slot) > TIMESTAMP_TOLERANCE_MS for ts, slot in slots):
        raise ValueError("Unexpected funding settlement timestamp")
    missing = sorted(expected - covered)
    if missing:
        raise ValueError(f"Missing {len(missing)} funding slots, first: {iso(missing[0])}")

    csv_buffer = io.StringIO(newline="")
    writer = csv.writer(csv_buffer, lineterminator="\n")
    writer.writerow(["observed_utc", "funding_rate", "interval_hours"])
    writer.writerows((iso(ts), str(events[ts]), 8) for ts in sorted(events))
    csv_text = csv_buffer.getvalue()
    return csv_text, {
        "status": "VERIFIED",
        "source": "https://fapi.binance.com/fapi/v1/fundingRate",
        "start": iso(start),
        "end_exclusive": iso(end),
        "rows": len(events),
        "expected": len(expected),
        "missing": [],
        "duplicates": 0,
        "invalid": 0,
        "errors": [],
        "rate_min": str(min(events.values())),
        "rate_max": str(max(events.values())),
        "rate_abs_sanity_limit": str(RATE_SANITY_LIMIT),
        "max_slot_offset_ms": max(abs(ts - slot) for ts, slot in slots),
        "csv_sha256": hashlib.sha256(csv_text.encode()).hexdigest(),
        "requests": pages,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cron-job-id", type=int)
    args = parser.parse_args()
    funding = json.loads((OUT / "funding_manifest.json").read_text())
    oi = json.loads((OUT / "oi_manifest.json").read_text())
    if funding["status"] != "VERIFIED" or oi["status"] not in ("VERIFIED", "VERIFIED_WITH_GAPS"):
        raise ValueError("Funding archive and OI coverage must be verified first")
    bounds = [int(datetime.fromisoformat(item["end_exclusive"]).replace(
        tzinfo=timezone.utc).timestamp() * 1000) for item in (funding, oi)]
    if bounds[0] >= bounds[1] or any(bound % STEP for bound in bounds):
        raise ValueError("Expected increasing UTC eight-hour boundaries")
    csv_text, manifest = collect(*bounds, args.cron_job_id)
    (OUT / "binance_funding_recent_events.csv").write_text(csv_text, encoding="utf-8", newline="")
    (OUT / "funding_recent_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
