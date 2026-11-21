"""Integrate 180-day Binance hourly spot/futures taker flow, OI and settled funding.
All observations are timestamp-aligned; no missing values are fabricated.
"""
import csv
import json
from bisect import bisect_right
from datetime import datetime, timedelta, timezone
from pathlib import Path

OUT = Path("research_integrated")

def load(path):
    with Path(path).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def val(x):
    return float(x) if x not in (None, "") else None

def main():
    flows = load("research_data/eth_aligned_1h.csv")
    oi_rows = load("research_derivatives/binance_oi_1h.csv")
    funding_rows = load("research_derivatives/binance_funding_events.csv")
    oi = {r["utc_hour"]: r for r in oi_rows}
    events = sorted(
        (datetime.fromisoformat(r["funding_time_utc"]), r)
        for r in funding_rows
    )
    event_times = [t for t, _ in events]
    fields = [
        "utc_hour", "eth_close", "spot_buy_pct", "spot_cvd_pct",
        "spot_delta_usdt", "futures_buy_pct", "futures_cvd_pct",
        "futures_delta_usdt", "oi_eth", "oi_usdt", "oi_observed_at_utc",
        "oi_change_1h_pct", "oi_change_4h_pct",
        "last_settled_funding_time_utc", "last_settled_funding_rate_pct",
        "funding_age_hours", "flow_divergence"
    ]
    output = []
    for f in sorted(flows, key=lambda x: x["utc_hour"]):
        hour = datetime.fromisoformat(f["utc_hour"])
        o = oi.get(f["utc_hour"], {})
        # Use the last settled funding event as of the beginning of the hour,
        # never the next future settlement.
        i = bisect_right(event_times, hour) - 1
        funding_time, funding = events[i] if i >= 0 else (None, None)
        s, future = val(f["spot_cvd_pct"]), val(f["futures_cvd_pct"])
        divergence = "none"
        if s is not None and future is not None:
            if s > 0 and future < 0:
                divergence = "spot_buy_futures_sell"
            elif s < 0 and future > 0:
                divergence = "spot_sell_futures_buy"
        row = {k: f.get(k, "") for k in fields}
        for k in ("oi_eth", "oi_usdt", "oi_observed_at_utc",
                  "oi_change_1h_pct", "oi_change_4h_pct"):
            row[k] = o.get(k, "")
        row["last_settled_funding_time_utc"] = funding_time.isoformat() if funding_time else ""
        row["last_settled_funding_rate_pct"] = funding["funding_rate_pct"] if funding else ""
        row["funding_age_hours"] = round((hour - funding_time).total_seconds() / 3600, 3) if funding_time else ""
        row["flow_divergence"] = divergence
        output.append(row)
    OUT.mkdir(exist_ok=True)
    with (OUT / "eth_180d_integrated_1h.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(output)
    hours = {r["utc_hour"] for r in output}
    status = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "expected_hours": 4320,
        "flow_hours": len(output),
        "unique_flow_hours": len(hours),
        "oi_matched_hours": sum(bool(oi.get(r["utc_hour"])) for r in output),
        "funding_events": len(events),
        "fully_matched_180d": len(hours) == 4320 and all(t in oi for t in hours),
        "notes": [
            "Only Binance ETHUSDT; Kraken CVD not backfilled.",
            "CVD here is candle-derived taker volume imbalance, not trade-by-trade CVD.",
            "OI is an hourly last snapshot; it may occur after the hour's opening.",
            "Funding is the last settled event known by the hour's start, not a forecast.",
            "OI decrease is not proof of forced liquidation.",
            "Check both upstream status JSON files for missing archives before backtesting.",
            "No prediction probabilities or validated backtest results are implied."
        ]
    }
    (OUT / "integration_status.json").write_text(
        json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(status, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
