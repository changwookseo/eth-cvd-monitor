"""Read-only OKX ETH-USDT-SWAP taker-volume-contract schema/continuity diagnostic.

No production CVD output, no report integration, no backfill claim. In particular
raw arrays are interpreted only after cross-unit and completed-bucket checks.
"""
import json
import math
import urllib.parse
import urllib.request
import urllib.error
import time
from datetime import datetime, timezone
from pathlib import Path

INST = "ETH-USDT-SWAP"
URL = "https://www.okx.com/api/v5/rubik/stat/taker-volume-contract"
OUT = Path("eth_futures_cvd_okx_rubik_diagnostic.json")
PERIOD_MS = {"5m": 300000, "1H": 3600000, "1D": 86400000}


def request(period, unit, limit):
    url = URL + "?" + urllib.parse.urlencode({
        "instId": INST, "period": period, "unit": str(unit), "limit": str(limit)
    })
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
            time.sleep(2 + attempt * 2)
    time.sleep(0.65)  # OKX public Rubik endpoint has per-IP request limits
    if not isinstance(obj, dict) or obj.get("code") != "0":
        raise ValueError("OKX nonzero API code: " + str(obj.get("code")))
    rows = obj.get("data")
    if not isinstance(rows, list) or len(rows) < 2:
        raise ValueError("Insufficient OKX Rubik rows")
    parsed = {}
    alignment_offset = None
    for row in rows:
        if not isinstance(row, list) or len(row) < 3:
            raise ValueError("Unexpected Rubik row shape")
        ts = int(row[0])
        vals = [float(row[1]), float(row[2])]
        offset = ts % PERIOD_MS[period]
        if alignment_offset is None:
            alignment_offset = offset
        if offset != alignment_offset or ts in parsed:
            raise ValueError("Inconsistent/duplicate bucket timestamp")
        if any(not math.isfinite(v) or v < 0 for v in vals):
            raise ValueError("Invalid taker volume")
        parsed[ts] = vals
    return parsed


def main():
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    raw = {}
    for period, limit in (("5m", 48), ("1H", 6), ("1D", 3)):
        raw[period] = {}
        for unit in ("0", "1"):
            raw[period][unit] = request(period, unit, limit)

    results = {}
    issues = []
    for period in PERIOD_MS:
        step = PERIOD_MS[period]
        zero, one = raw[period]["0"], raw[period]["1"]
        shared = sorted(set(zero) & set(one))
        closed = [t for t in shared if t + step <= now_ms - 60000]
        if len(closed) < 2:
            issues.append(period + ": insufficient closed shared buckets")
        gaps = [(a, b) for a, b in zip(closed, closed[1:]) if b - a != step]
        if gaps:
            issues.append(period + ": gaps between closed buckets")
        ratios = []
        for t in closed:
            for i in (0, 1):
                if one[t][i] > 0 and zero[t][i] > 0:
                    ratios.append(zero[t][i] / one[t][i])
        if not ratios:
            issues.append(period + ": no positive volume pairs to infer unit scaling")
        results[period] = {
            "unit0_rows": len(zero), "unit1_rows": len(one),
            "bucket_alignment_offset_ms": min(one) % step,
            "shared_closed_bucket_count": len(closed),
            "first_closed_bucket_utc": datetime.fromtimestamp(min(closed) / 1000, timezone.utc).isoformat() if closed else None,
            "last_closed_bucket_utc": datetime.fromtimestamp(max(closed) / 1000, timezone.utc).isoformat() if closed else None,
            "gap_count": len(gaps),
            "unit0_to_unit1_min_ratio": min(ratios) if ratios else None,
            "unit0_to_unit1_max_ratio": max(ratios) if ratios else None,
            "latest_three_raw_unit1_rows": [[t, *one[t]] for t in sorted(one, reverse=True)[:3]],
            "latest_three_raw_unit0_rows": [[t, *zero[t]] for t in sorted(zero, reverse=True)[:3]]
        }

    # Compare complete 1H buckets with their twelve 5m sub-buckets, on the
    # SAME unit and SAME raw column. This tests source consistency without
    # presuming which column is sell or buy.
    cross = []
    for t, hourly in sorted(raw["1H"]["1"].items()):
        if t + 3600000 > now_ms - 60000:
            continue
        sub = [raw["5m"]["1"].get(t + i * 300000) for i in range(12)]
        if any(v is None for v in sub):
            continue
        summed = [sum(v[i] for v in sub) for i in (0, 1)]
        relative = [abs(summed[i] - hourly[i]) / max(hourly[i], 1e-9) for i in (0, 1)]
        cross.append({"hour_start_utc": datetime.fromtimestamp(t / 1000, timezone.utc).isoformat(),
                      "hourly_raw_unit1": hourly, "sum_5m_raw_unit1": summed,
                      "relative_difference": relative})
        if max(relative) > 0.05:
            issues.append("5m/1H same-unit same-column aggregate mismatch >5%")
    if not cross:
        issues.append("No complete hour with twelve 5m buckets available for comparison")

    result = {
        "status": "DIAGNOSTIC_ONLY", "report_eligible": False,
        "exchange": "OKX", "instrument": INST, "source": URL,
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "raw_column_order": "not independently established for ETH; external documentation suggests [ts,sell,buy]",
        "unit_1": "coin (ETH) per external documentation; cross-unit ratio measured below",
        "period_results": results, "cross_period_checks": cross, "issues": issues,
        "limitations": [
            "No full-window trade-tape reconciliation of ETH aggressor side.",
            "Closed buckets and historical coverage do not establish continuous automated capture.",
            "No 180-day futures CVD or production/report integration.",
            "Not Binance futures or aggregate-market CVD."
        ]
    }
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
