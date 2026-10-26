"""ETH daily/weekly technical indicators from Coinbase Exchange ETH-USD daily candles.
Run: python eth_technical_indicators.py
No third-party dependencies. Output: eth_technical_latest.json.
"""
import json
import math
import os
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

PAIR = "ETH-USD"
URL = "https://api.exchange.coinbase.com/products/ETH-USD/candles"
OUTPUT = Path("eth_technical_latest.json")
MIN_DAYS = 1600
REQUIRED_DAILY = 250
REQUIRED_WEEKLY = 210


def fetch_daily(now=None, opener=urlopen):
    now = now or datetime.now(timezone.utc)
    end = now.replace(hour=0, minute=0, second=0, microsecond=0)
    start = end - timedelta(days=MIN_DAYS)
    candles = {}
    cursor = start
    while cursor < end:
        nxt = min(cursor + timedelta(days=299), end)
        qs = urlencode({"granularity": 86400, "start": cursor.isoformat(), "end": nxt.isoformat()})
        req = Request(URL + "?" + qs, headers={"User-Agent": "eth-esi-technical/1.0", "Accept": "application/json"})
        with opener(req, timeout=25) as resp:
            rows = json.load(resp)
        if not isinstance(rows, list):
            raise ValueError("Unexpected Coinbase response")
        for row in rows:
            ts, low, high, opened, close, volume = row[:6]
            stamp = datetime.fromtimestamp(int(ts), timezone.utc)
            if start <= stamp < end:
                candles[stamp] = {"time": stamp.isoformat(), "close": float(close), "high": float(high), "low": float(low), "volume": float(volume)}
        cursor = nxt
        time.sleep(0.15)
    result = [candles[k] for k in sorted(candles)]
    if len(result) < MIN_DAYS - 10:
        raise ValueError(f"Insufficient daily candles: {len(result)}")
    for prev, cur in zip(result, result[1:]):
        if (datetime.fromisoformat(cur["time"]) - datetime.fromisoformat(prev["time"])).days != 1:
            raise ValueError("Gap in daily OHLCV history")
    return result, end


def weekly_from_daily(daily, end):
    weeks = {}
    for row in daily:
        dt = datetime.fromisoformat(row["time"])
        monday = (dt - timedelta(days=dt.weekday())).date().isoformat()
        weeks.setdefault(monday, []).append(row)
    result = []
    for monday in sorted(weeks):
        start = datetime.fromisoformat(monday).replace(tzinfo=timezone.utc)
        if start + timedelta(days=7) > end:
            continue
        rows = weeks[monday]
        if len(rows) != 7:
            continue
        result.append({"time": (start + timedelta(days=6)).isoformat(), "close": rows[-1]["close"], "high": max(x["high"] for x in rows), "low": min(x["low"] for x in rows), "volume": sum(x["volume"] for x in rows)})
    return result


def ema(values, period):
    if len(values) < period:
        raise ValueError("Insufficient EMA history")
    alpha = 2 / (period + 1)
    out = [None] * (period - 1)
    prev = sum(values[:period]) / period
    out.append(prev)
    for value in values[period:]:
        prev = alpha * value + (1 - alpha) * prev
        out.append(prev)
    return out


def rsi(values, period=14):
    if len(values) <= period:
        raise ValueError("Insufficient RSI history")
    diffs = [values[i] - values[i - 1] for i in range(1, len(values))]
    gains = [max(x, 0) for x in diffs]
    losses = [max(-x, 0) for x in diffs]
    gain, loss = sum(gains[:period]) / period, sum(losses[:period]) / period
    out = [None] * period
    def score(g, l):
        return 100.0 if l == 0 else 100 - 100 / (1 + g / l)
    out.append(score(gain, loss))
    for g, l in zip(gains[period:], losses[period:]):
        gain = (gain * (period - 1) + g) / period
        loss = (loss * (period - 1) + l) / period
        out.append(score(gain, loss))
    return out


def calculate(candles):
    closes = [x["close"] for x in candles]
    if len(closes) < 210:
        raise ValueError("Insufficient history for SMA200 and MACD")
    fast, slow = ema(closes, 12), ema(closes, 26)
    macd = [None if a is None or b is None else a - b for a, b in zip(fast, slow)]
    valid = [x for x in macd if x is not None]
    signals = [None] * 25 + ema(valid, 9)
    rsis = rsi(closes)
    i = len(closes) - 1
    prev = i - 1
    def record(k):
        m, s = macd[k], signals[k]
        return {"rsi14": round(rsis[k], 4), "macd": round(m, 6), "signal": round(s, 6), "histogram": round(m - s, 6)}
    latest = record(i)
    prior = record(prev)
    latest["sma"] = {str(n): round(sum(closes[-n:]) / n, 4) for n in (20, 50, 100, 200)}
    latest["close"] = closes[-1]
    latest["candle_end_utc"] = (datetime.fromisoformat(candles[-1]["time"]) + timedelta(days=1)).isoformat()
    latest["macd_cross"] = ("bullish" if prior["macd"] <= prior["signal"] and latest["macd"] > latest["signal"] else "bearish" if prior["macd"] >= prior["signal"] and latest["macd"] < latest["signal"] else "none")
    latest["previous"] = prior
    latest["candle_count"] = len(candles)
    return latest


def main():
    observed = datetime.now(timezone.utc)
    result = {"generated_at_utc": observed.isoformat(), "source": "Coinbase Exchange public ETH-USD daily OHLCV", "method": "Wilder RSI14; EMA12-EMA26 MACD; EMA9 signal; UTC daily candles; complete Monday-Sunday UTC weekly candles; SMA", "status": "UNAVAILABLE"}
    try:
        daily, end = fetch_daily(observed)
        weekly = weekly_from_daily(daily, end)
        if len(daily) < REQUIRED_DAILY or len(weekly) < REQUIRED_WEEKLY:
            raise ValueError(f"Insufficient data: daily={len(daily)}, weekly={len(weekly)}")
        result.update({"status": "VERIFIED", "daily": calculate(daily), "weekly": calculate(weekly), "daily_completed_through_utc": end.isoformat()})
    except Exception as exc:
        result["failure_reason"] = f"{type(exc).__name__}: {exc}"
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "failure_reason": result.get("failure_reason"), "daily": result.get("daily"), "weekly": result.get("weekly")}, ensure_ascii=False))
    if result["status"] != "VERIFIED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
