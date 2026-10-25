
import json
import urllib.request
from datetime import datetime, timezone

SYMBOL = "ETHUSDT"
URL = (
    "https://api.binance.com/api/v3/klines"
    "?symbol=ETHUSDT&interval=1m&limit=1000"
)

def get_klines():
    request = urllib.request.Request(
        URL, headers={"User-Agent": "ETH-CVD-Monitor/1.0"}
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)

def calculate_cvd(klines, minutes):
    selected = klines[-minutes:]
    delta = 0.0
    volume = 0.0

    for candle in selected:
        total_volume = float(candle[5])
        taker_buy_volume = float(candle[9])
        delta += 2 * taker_buy_volume - total_volume
        volume += total_volume

    return {
        "cvd_eth": round(delta, 4),
        "volume_eth": round(volume, 4),
        "buy_ratio_pct": round(
            100 * (volume + delta) / (2 * volume), 2
        ) if volume else None
    }

def main():
    klines = get_klines()
    # Exclude the currently forming candle.
    klines = klines[:-1]

    result = {
        "symbol": SYMBOL,
        "exchange": "Binance Spot",
        "calculated_at_utc": datetime.now(
            timezone.utc
        ).isoformat(),
        "intervals": {}
    }

    for label, minutes in {
        "5m": 5,
        "15m": 15,
        "1h": 60,
        "4h": 240
    }.items():
        result["intervals"][label] = calculate_cvd(
            klines, minutes
        )

    with open("cvd_latest.json", "w") as file:
        json.dump(result, file, indent=2)

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
