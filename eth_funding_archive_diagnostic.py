"""Diagnose missing Binance ETHUSDT USD-M funding archives, without altering existing data."""
import json
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = "https://data.binance.vision/data/futures/um"
OUT = Path("research_diagnostics")
START = datetime(2026, 10, 1, tzinfo=timezone.utc)
END = datetime(2026, 10, 25, tzinfo=timezone.utc)

def probe(url):
    # HEAD checks existence without downloading large ZIP archives.
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "ETH-Funding-Diagnostics/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return {"status": response.status, "content_length": response.headers.get("Content-Length")}
    except urllib.error.HTTPError as exc:
        return {"status": exc.code, "error": str(exc)}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"status": None, "error": str(exc)}

def main():
    day = START
    daily = []
    while day <= END:
        stamp = day.strftime("%Y-%m-%d")
        url = f"{ROOT}/daily/fundingRate/ETHUSDT/ETHUSDT-fundingRate-{stamp}.zip"
        daily.append({"date": stamp, "url": url, **probe(url)})
        day += timedelta(days=1)
    monthly_url = f"{ROOT}/monthly/fundingRate/ETHUSDT/ETHUSDT-fundingRate-2026-10.zip"
    result = {
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "purpose": "Archive availability diagnosis only; not a funding backfill",
        "monthly_october": {"url": monthly_url, **probe(monthly_url)},
        "daily_october_1_to_25": daily,
        "daily_status_counts": {str(code): sum(x["status"] == code for x in daily) for code in sorted({x["status"] for x in daily}, key=lambda v: str(v))},
        "caveats": [
            "HTTP 200 means the archive URL responds, not that ETH funding events are complete or valid.",
            "HTTP 404 may mean unpublished archive; HTTP 451 indicates legal/access restriction.",
            "No API calls, no fabricated rates, and no changes to existing collectors or datasets.",
            "This is a fixed historical date-range diagnostic."
        ]
    }
    OUT.mkdir(exist_ok=True)
    (OUT / "october_funding_archive_diagnostic.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
