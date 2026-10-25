
import json
import urllib.request

url = "https://api.kraken.com/0/public/Trades?pair=ETHUSD"

request = urllib.request.Request(
    url,
    headers={"User-Agent": "ETH-CVD-Monitor/1.0"}
)

try:
    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.load(response)

    if data.get("error"):
        raise RuntimeError(data["error"])

    trades = next(
        value for key, value in data["result"].items()
        if key != "last"
    )

    print("KRAKEN API SUCCESS")
    print("Received trades:", len(trades))
    print("First trade sample:", trades[0] if trades else "none")

except Exception as error:
    print("KRAKEN API FAILED:", repr(error))
    raise
