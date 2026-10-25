

import json
import os
import time
import urllib.request
from datetime import datetime, timezone

API = "https://api.kraken.com/0/public/Trades?pair=ETHUSD"
STATE = "cvd_state.json"
WINDOWS = {
    "5m": 300,
    "15m": 900,
    "1h": 3600,
    "4h": 14400,
    "24h": 86400
}

def utc(t):
    return datetime.fromtimestamp(
        t, timezone.utc
    ).isoformat()

def fetch(cursor):
    url = API
    if cursor:
        url += "&since=" + str(cursor)

    req = urllib.request.Request(
        url, headers={"User-Agent": "ETH-CVD-Monitor"}
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)

    if data.get("error"):
        raise RuntimeError(str(data["error"]))

    result = data["result"]
    pair = next(k for k in result if k != "last")
    return result[pair], str(result["last"])

def main():
    now = time.time()
    state = {"cursor": None, "trades": []}

    if os.path.exists(STATE):
        with open(STATE) as f:
            state.update(json.load(f))

    previous_cursor = state["cursor"]
    cursor = previous_cursor
    records = {t[0]: t for t in state["trades"]}
    pages = 0
    page_limit = 30
    limit_hit = False
    seen = set()

    while pages < page_limit:
        trades, next_cursor = fetch(cursor)
        pages += 1

        for trade in trades:
            if len(trade) > 6 and trade[6] is not None:
                key = "id:" + str(trade[6])
            else:
                key = "record:" + json.dumps(
                    trade, separators=(",", ":")
                )

            records[key] = [
                key,
                float(trade[2]),
                float(trade[1]),
                str(trade[3])
            ]

        if (not trades or next_cursor == cursor
                or next_cursor in seen):
            cursor = next_cursor
            break

        seen.add(next_cursor)
        cursor = next_cursor

        if len(trades) < 1000:
            break
    else:
        limit_hit = True

    cutoff = now - 86400 - 300
    stored = [
        t for t in records.values()
        if t[1] >= cutoff
    ]
    stored.sort(key=lambda t: t[1])

    windows = {}
    for name, seconds in WINDOWS.items():
        subset = [
            t for t in stored
            if now - seconds <= t[1] <= now
        ]
        buy = sum(
            t[2] for t in subset if t[3] == "b"
        )
        sell = sum(
            t[2] for t in subset if t[3] == "s"
        )
        windows[name] = {
            "buy_volume_eth": round(buy, 6),
            "sell_volume_eth": round(sell, 6),
            "cvd_delta_eth": round(buy - sell, 6),
            "trade_count": len(subset),
            "coverage_status": "unverified"
        }

    state = {
        "cursor": cursor,
        "trades": stored
    }
    output = {
        "exchange": "Kraken Spot",
        "symbol": "ETH/USD",
        "calculated_at_utc": utc(now),
        "earliest_trade_utc": (
            utc(stored[0][1]) if stored else None
        ),
        "latest_trade_utc": (
            utc(stored[-1][1]) if stored else None
        ),
        "stored_trade_count": len(stored),
        "pages_fetched": pages,
        "page_limit_hit": limit_hit,
        "data_completeness": "unverified",
        "windows": windows
    }

    with open(STATE, "w") as f:
        json.dump(state, f, separators=(",", ":"))

    with open("cvd_latest.json", "w") as f:
        json.dump(output, f, indent=2)

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
