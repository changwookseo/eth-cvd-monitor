"""Collect Binance ETH spot and USD-M perpetual hourly taker flows, last 180 completed UTC days.
No API keys. Does not modify the existing Kraken CVD collector.
"""
import csv
import io
import json
import time
import urllib.error
import urllib.request
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = 'https://data.binance.vision/data'
SYMBOL = 'ETHUSDT'
OUT = Path('research_data')
MARKETS = {'binance_spot': 'spot', 'binance_usdm': 'futures/um'}


def get_zip(url):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'ETH-180D-Research/1.0'})
            with urllib.request.urlopen(req, timeout=45) as res:
                raw = res.read()
            with zipfile.ZipFile(io.BytesIO(raw)) as z:
                files = [n for n in z.namelist() if n.endswith('.csv')]
                if len(files) != 1:
                    raise ValueError('Unexpected ZIP members: ' + str(files))
                return list(csv.reader(io.TextIOWrapper(z.open(files[0]), encoding='utf-8')))
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            error = exc
        except (OSError, ValueError, zipfile.BadZipFile) as exc:
            error = exc
        time.sleep(2 ** attempt)
    raise RuntimeError(f'Could not fetch {url}: {error}')


def month_iter(start, end):
    y, m = start.year, start.month
    while (y, m) <= (end.year, end.month):
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def load_market(kind, path, start, end):
    records, missing = {}, []
    for y, m in month_iter(start, end):
        month_start = datetime(y, m, 1, tzinfo=timezone.utc)
        next_month = datetime(y + (m == 12), 1 if m == 12 else m + 1, 1, tzinfo=timezone.utc)
        if next_month <= datetime(end.year, end.month, 1, tzinfo=timezone.utc) + timedelta(days=1):
            filename = f'{SYMBOL}-1h-{y:04d}-{m:02d}.zip'
            url = f'{ROOT}/{path}/monthly/klines/{SYMBOL}/1h/{filename}'
            rows = get_zip(url)
            if rows is None:
                missing.append(url)
                rows = []
            parse_rows(rows, records, start, end)
        else:
            day = max(start, month_start)
            while day <= end:
                stamp = day.strftime('%Y-%m-%d')
                filename = f'{SYMBOL}-1h-{stamp}.zip'
                url = f'{ROOT}/{path}/daily/klines/{SYMBOL}/1h/{filename}'
                rows = get_zip(url)
                if rows is None:
                    missing.append(url)
                else:
                    parse_rows(rows, records, start, end)
                day += timedelta(days=1)
    return records, missing


def parse_rows(rows, target, start, end):
    for row in rows:
        if len(row) < 11 or not row[0].isdigit():
            continue
        raw_ts = int(row[0])
        # Binance spot archives since 2025 use microseconds; futures use milliseconds.
        ts_ms = raw_ts // 1000 if raw_ts >= 10**14 else raw_ts
        dt = datetime.fromtimestamp(ts_ms / 1000, timezone.utc)
        if not (start <= dt <= end + timedelta(hours=23)):
            continue
        quote = float(row[7]); buy = float(row[10]); sell = quote - buy
        if quote < 0 or buy < -1e-6 or sell < -1e-4:
            raise ValueError(f'Invalid quote/buy volumes at {dt}: {quote}, {buy}')
        target[dt.isoformat()] = {
            'open': float(row[1]), 'high': float(row[2]), 'low': float(row[3]),
            'close': float(row[4]), 'quote_usdt': quote, 'taker_buy_usdt': buy,
            'taker_sell_usdt': max(0, sell), 'delta_usdt': buy - sell,
            'buy_pct': 100 * buy / quote if quote else None,
            'normalized_cvd_pct': 100 * (buy - sell) / quote if quote else None,
        }


def main():
    now = datetime.now(timezone.utc)
    end = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    start = end - timedelta(days=179)
    OUT.mkdir(exist_ok=True)
    result = {}; missing_all = {}
    for name, path in MARKETS.items():
        print('Collecting', name, flush=True)
        records, missing = load_market(name, path, start, end)
        missing_all[name] = missing
        result[name] = records
        cols = ['utc_hour', 'open', 'high', 'low', 'close', 'quote_usdt', 'taker_buy_usdt', 'taker_sell_usdt', 'delta_usdt', 'buy_pct', 'normalized_cvd_pct']
        with (OUT / f'{name}_1h.csv').open('w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=cols); writer.writeheader()
            for stamp, row in sorted(records.items()):
                writer.writerow({'utc_hour': stamp, **row})
    aligned = sorted(set.intersection(*(set(v) for v in result.values())))
    with (OUT / 'eth_aligned_1h.csv').open('w', newline='', encoding='utf-8') as file:
        cols = ['utc_hour', 'eth_close', 'spot_buy_pct', 'spot_cvd_pct', 'spot_delta_usdt', 'futures_buy_pct', 'futures_cvd_pct', 'futures_delta_usdt']
        writer = csv.DictWriter(file, fieldnames=cols); writer.writeheader()
        for t in aligned:
            s = result['binance_spot'][t]; f = result['binance_usdm'][t]
            writer.writerow(dict(utc_hour=t, eth_close=s['close'], spot_buy_pct=s['buy_pct'], spot_cvd_pct=s['normalized_cvd_pct'], spot_delta_usdt=s['delta_usdt'], futures_buy_pct=f['buy_pct'], futures_cvd_pct=f['normalized_cvd_pct'], futures_delta_usdt=f['delta_usdt']))
    expected = 180 * 24
    summary = {'generated_utc': now.isoformat(), 'start_utc': start.isoformat(), 'end_utc_inclusive_day': end.date().isoformat(), 'expected_hourly_bars': expected, 'available_hours': {k: len(v) for k,v in result.items()}, 'aligned_hours': len(aligned), 'missing_archives': missing_all, 'status': 'complete' if len(aligned) == expected and not any(missing_all.values()) else 'incomplete', 'limitations': ['Only Binance spot and Binance USD-M perpetual are included.', 'CVD is taker flow per candle, not price-impact attribution.', 'No historical liquidation, OI, funding, Kraken or Bybit backfill in this first-stage collector.']}
    (OUT / 'collection_status.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(summary, indent=2))
    if summary['status'] != 'complete':
        print('WARNING: missing bars or archives; do not treat as complete 180-day sample.')


if __name__ == '__main__':
    main()
