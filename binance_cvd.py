"""Binance Vision ETHUSDT spot aggregate-trade CVD collector.

CVD uses taker buy volume minus taker sell volume, measured in ETH.
Only the Binance Vision public market-data endpoint is used.
"""
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

API = 'https://data-api.binance.vision/api/v3/aggTrades'
STATE = 'binance_cvd_state.json'
OUTPUT = 'binance_cvd_latest.json'
WINDOWS = {'5m': 300, '15m': 900, '1h': 3600, '4h': 14400, '24h': 86400}
MAX_PAGES = 120
STALE_SECONDS = 600
KEEP_SECONDS = 86400 + 600


def iso(seconds):
    return datetime.fromtimestamp(seconds, timezone.utc).isoformat() if seconds is not None else None


def request_trades(params):
    url = API + '?' + urllib.parse.urlencode({'symbol': 'ETHUSDT', 'limit': 1000, **params})
    req = urllib.request.Request(url, headers={'User-Agent': 'ETH-CVD-Monitor/1.0'})
    with urllib.request.urlopen(req, timeout=25) as response:
        payload = json.load(response)
    if not isinstance(payload, list):
        raise RuntimeError('Unexpected Binance response: ' + str(payload)[:300])
    return payload


def normalized(t):
    # Binance m=True means buyer is maker, therefore taker is seller.
    return [int(t['a']), int(t['T']) / 1000, float(t['q']), 'sell' if t['m'] else 'buy']


def main():
    now = time.time()
    state = {}
    if os.path.exists(STATE):
        with open(STATE, encoding='utf-8') as f:
            state = json.load(f)
    previous = {int(t[0]): t for t in state.get('trades', [])}
    last_id = state.get('last_agg_trade_id')
    continuity_start = state.get('continuity_start_timestamp', now)
    pages = 0
    new_count = 0
    expected_id = int(last_id) + 1 if last_id is not None else None
    first_fetch = last_id is None
    gap = False
    try:
        while pages < MAX_PAGES:
            params = {} if expected_id is None else {'fromId': expected_id}
            batch = request_trades(params)
            pages += 1
            if not batch:
                break
            rows = [normalized(t) for t in batch]
            if expected_id is not None and rows[0][0] != expected_id:
                gap = True
                raise RuntimeError(f'Aggregate trade ID gap: expected {expected_id}, got {rows[0][0]}')
            for i in range(1, len(rows)):
                if rows[i][0] != rows[i - 1][0] + 1:
                    gap = True
                    raise RuntimeError('Aggregate trade IDs are not consecutive')
            for row in rows:
                if row[0] not in previous:
                    new_count += 1
                previous[row[0]] = row
            expected_id = rows[-1][0] + 1
            # Binance returns up to 1000 records. Fewer indicates caught up.
            if len(rows) < 1000:
                break
        else:
            raise RuntimeError('Page cap reached; refusing incomplete update')
        if not previous:
            raise RuntimeError('No trades returned')
        last_row = max(previous.values(), key=lambda r: r[0])
        # First run only starts continuity. No historical 24h coverage claim.
        if first_fetch:
            continuity_start = now
        latest_time = max(t[1] for t in previous.values())
        fresh = now - latest_time <= STALE_SECONDS
        if not fresh:
            continuity_start = now
        cutoff = now - KEEP_SECONDS
        stored = sorted((t for t in previous.values() if cutoff <= t[1] <= now), key=lambda r: r[0])
        windows = {}
        for label, duration in WINDOWS.items():
            rows = [t for t in stored if now - duration <= t[1] <= now]
            buy = sum(t[2] for t in rows if t[3] == 'buy')
            sell = sum(t[2] for t in rows if t[3] == 'sell')
            covered = fresh and not gap and now - continuity_start >= duration
            windows[label] = {
                'buy_volume_eth': round(buy, 6),
                'sell_volume_eth': round(sell, 6),
                'cvd_delta_eth': round(buy - sell, 6),
                'trade_count': len(rows),
                'coverage_status': 'provisionally_complete' if covered else 'unverified',
            }
        output = {
            'exchange': 'Binance Spot', 'symbol': 'ETH/USDT',
            'calculated_at_utc': iso(now),
            'earliest_trade_utc': iso(min(t[1] for t in stored)) if stored else None,
            'latest_trade_utc': iso(latest_time),
            'last_agg_trade_id': last_row[0],
            'stored_trade_count': len(stored), 'new_trade_count': new_count,
            'pages_fetched': pages, 'possible_gap_detected': gap,
            'continuity_tracking_started_utc': iso(continuity_start),
            'data_completeness': 'provisionally_complete' if all(
                v['coverage_status'] == 'provisionally_complete' for v in windows.values()
            ) else 'unverified',
            'coverage_note': 'Provisional continuity only; no independent exchange-side completeness audit. '
                             'Aggregated trade quantity in ETH, taker direction inferred from buyer-maker flag.',
            'windows': windows,
        }
        next_state = {
            'last_agg_trade_id': last_row[0],
            'continuity_start_timestamp': continuity_start,
            'trades': stored,
        }
        for path, data in ((STATE, next_state), (OUTPUT, output)):
            tmp = path + '.tmp'
            with open(tmp, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2 if path == OUTPUT else None)
            os.replace(tmp, path)
        print(json.dumps(output, ensure_ascii=False, indent=2))
    except (urllib.error.URLError, ValueError, RuntimeError, KeyError) as exc:
        # No writes on failed collection; next run retries from saved ID.
        raise SystemExit(f'Binance collection failed; previous state preserved: {exc}') from exc


if __name__ == '__main__':
    main()

