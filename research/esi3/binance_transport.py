"""Read Binance USD-M public market data directly or from a saved Cron response."""
import json
import os
import re
from urllib.parse import urlencode
from urllib.request import urlopen

from eth_oi_cron_import import get as cron_get

PATHS = {
    "funding": "/fapi/v1/fundingRate",
    "oi": "/fapi/v1/openInterest",
    "futures_trades": "/fapi/v1/aggTrades",
    "futures_bars": "/fapi/v1/klines",
}


def read_market_data(metric, params, *, cron_job_id=None):
    source = "https://fapi.binance.com" + PATHS[metric] + "?" + urlencode(params)
    if cron_job_id is None:
        with urlopen(source, timeout=25) as response:
            return json.load(response), {"source": source, "transport": "Binance REST"}

    key = os.environ.get("CRONJOB_API_KEY")
    if not key:
        raise ValueError("CRONJOB_API_KEY is not configured")
    history_path = f"/jobs/{cron_job_id}/history"
    history = cron_get(history_path, key).get("history", [])
    if not history:
        raise ValueError("No Cron executions available")
    latest = max(history, key=lambda item: int(item["date"]))
    identifier = latest["identifier"]
    if not re.fullmatch(rf"{cron_job_id}-[0-9-]+", identifier):
        raise ValueError("Unexpected Cron execution identifier")
    detail = cron_get(f"{history_path}/{identifier}", key)["jobHistoryDetails"]
    if (detail.get("jobId") != cron_job_id or detail.get("identifier") != identifier
            or detail.get("url") != source):
        raise ValueError("Cron response does not match the requested job and source")
    if detail.get("status") != 1 or detail.get("httpStatus") != 200:
        raise ValueError("Cron source request failed")
    return json.loads(detail["body"]), {
        "source": source,
        "transport": "cron-job.org saved response",
        "cron_job_id": cron_job_id,
        "cron_execution_id": identifier,
        "cron_executed_at_epoch": int(detail["date"]),
    }
