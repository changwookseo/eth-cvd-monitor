
import json
import urllib.request
from datetime import datetime, timezone

URL = "https://api.kraken.com/0/public/Trades?pair=ETHUSD"

def get_trades():
    request = urllib.request.Request(
        URL,
        headers={"User-Agent": "ETH-CVD-Monitor/1.0"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)

    if data.get("error"):
        raise RuntimeError(str(data["error"]))

    result = data["result"]
    key = next(k for k in result if k != "last")
    return result[key]

def main():
    trades = get_trades()
    if not trades:
        raise RuntimeError("No trades received")

    buy_volume = 0.0
    sell_volume = 0.0

    for trade in trades:
        volume = float(trade[1])
        side = trade[3]

        if side == "b":
            buy_volume += volume
        elif side == "s":
            sell_volume += volume
        else:
            raise RuntimeError("Unknown trade side")

    timestamps = [float(t[2]) for t in trades]
    total = buy_volume + sell_volume

    result = {
        "exchange": "Kraken Spot",
        "symbol": "ETH/USD",
        "method": "recent_1000_trades",
        "trade_count": len(trades),
        "start_utc": datetime.fromtimestamp(
            min(timestamps), timezone.utc
        ).isoformat(),
        "end_utc": datetime.fromtimestamp(
            max(timestamps), timezone.utc
        ).isoformat(),
        "calculated_at_utc": datetime.now(
            timezone.utc
        ).isoformat(),
        "buy_volume_eth": round(buy_volume, 6),
        "sell_volume_eth": round(sell_volume, 6),
        "cvd_delta_eth": round(
            buy_volume - sell_volume, 6
        ),
        "buy_ratio_pct": round(
            buy_volume / total * 100, 2
        ) if total else None
    }

    with open("cvd_latest.json", "w") as file:
        json.dump(result, file, indent=2)

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
