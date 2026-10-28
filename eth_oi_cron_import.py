"""Import current Binance OI from a saved cron-job.org response.
Requires CRONJOB_API_KEY in the process environment. No credentials are logged.
This importer only reads Cron; it never changes account settings or jobs.
"""
import json
import math
import os
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.cron-job.org"
JOB_ID = 8738287
SOURCE = "https://fapi.binance.com/fapi/v1/openInterest?symbol=ETHUSDT"
MAX_AGE_SECONDS = 600


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def get(path, key):
    req = urllib.request.Request(API + path, headers={
        "Authorization": "Bearer " + key, "User-Agent": "eth-cvd-monitor/2.0"
    })
    with urllib.request.build_opener(NoRedirect).open(req, timeout=30) as response:
        return json.load(response)


def validate(item, now):
    if item.get("jobId") != JOB_ID or item.get("url") != SOURCE:
        raise ValueError("Cron job/source mismatch")
    if item.get("status") != 1 or item.get("httpStatus") != 200:
        raise ValueError("Cron source request did not succeed")
    data = json.loads(item["body"])
    if data.get("symbol") != "ETHUSDT":
        raise ValueError("Unexpected source symbol")
    value = float(data["openInterest"])
    observed = datetime.fromtimestamp(int(data["time"]) / 1000, timezone.utc)
    executed = datetime.fromtimestamp(int(item["date"]), timezone.utc)
    if not math.isfinite(value) or value <= 0:
        raise ValueError("Invalid OI value")
    for timestamp in (observed, executed):
        if not -30 <= (now - timestamp).total_seconds() <= MAX_AGE_SECONDS:
            raise ValueError("Stale or future OI/Cron observation")
    if abs((executed - observed).total_seconds()) > 60:
        raise ValueError("Cron response timing mismatch")
    return {
        "source": SOURCE, "transport": "cron-job.org saved response",
        "cron_job_id": JOB_ID, "cron_execution_id": item["identifier"],
        "exchange": "Binance USD-M", "symbol": "ETHUSDT",
        "observed_at_utc": observed.isoformat(), "fetched_at_utc": now.isoformat(),
        "cron_executed_at_utc": executed.isoformat(), "timeframe": "snapshot",
        "value": value, "unit": "ETH", "status": "VERIFIED", "failure_reason": None,
        "scope": "Binance ETHUSDT perpetual only; not market-wide OI"
    }


def collect():
    key = os.environ.get("CRONJOB_API_KEY")
    if not key:
        raise ValueError("CRONJOB_API_KEY is not configured")
    listing = get(f"/jobs/{JOB_ID}/history", key)
    history = listing.get("history", [])
    if not history:
        raise ValueError("No Cron executions available")
    latest = max(history, key=lambda item: int(item["date"]))
    identifier = latest["identifier"]
    if not re.fullmatch(str(JOB_ID) + r"-[0-9-]+", identifier):
        raise ValueError("Invalid Cron execution identifier")
    detail = get(f"/jobs/{JOB_ID}/history/{identifier}", key)["jobHistoryDetails"]
    if detail.get("identifier") != identifier:
        raise ValueError("Cron execution mismatch")
    return validate(detail, datetime.now(timezone.utc))


def main():
    try:
        snapshot = collect()
    except Exception as error:
        # HTTP errors expose status only; no request headers or key are written.
        reason = ("HTTP " + str(error.code)) if isinstance(error, urllib.error.HTTPError) else type(error).__name__
        print("OI import failed; prior snapshot preserved: " + reason)
        raise SystemExit(1)
    output = Path("eth_oi_latest.json")
    temporary = output.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    temporary.replace(output)
    print(json.dumps(snapshot, indent=2))


if __name__ == "__main__":
    main()
