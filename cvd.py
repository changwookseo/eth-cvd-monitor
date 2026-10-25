import json
import os
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

API = 'https://api.kraken.com/0/public/Trades'
PAIR = 'ETHUSD'
STATE = 'cvd_state.json'
OUTPUT = 'cvd_latest.json'
WINDOWS = {'5m': 300, '15m': 900, '1h': 3600, '4h': 14400, '24h': 86400}
MAX_PAGES = 40
MAX_AGE_SECONDS = 86400 + 600
# This is a conservative freshness threshold, not proof of exchange completeness.
MAX_STALENESS_SECONDS = 600


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).isoformat() if ts is not None else None


def fetch(cursor):
    params = {'pair': PAIR}
    if cursor is not None:
        params['since'] = str(cursor)
    url = API + '?' + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={'User-Agent': 'ETH-CVD-Monitor/2.0'})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if payload.get('error'):
        raise RuntimeError(f"Kraken API error: {payload['error']}")
    result = payload['result']
    key = next(k for k in result if k != 'last')
    return result[key], str(result['last'])


def trade_key(trade):
    # Kraken may provide a trade ID at index 6. For legacy records, retain their key.
    if len(trade) > 6 and trade[6] is not None:
        return 'id:' + str(trade[6])
    # Identical records without IDs cannot be distinguished perfectly.
    return 'record:' + json.dumps(trade, separators=(',', ':'), ensure_ascii=False)


def main():
    now = time.time()
    previous = {}
    if os.path.exists(STATE):
        with open(STATE, encoding='utf-8') as file:
            previous = json.load(file)

    cursor = previous.get('cursor')
    old_trades = previous.get('trades', [])
    records = {row[0]: row for row in old_trades if len(row) >= 4}
    previous_latest = max((float(row[1]) for row in old_trades), default=None)
    continuity_start = previous.get('continuity_start_utc_timestamp')
    # Older state has no continuity metadata. Start a new tracked period rather
    # than claiming its historical 24-hour coverage was verified.
    if continuity_start is None:
        continuity_start = now

    pages = 0
    page_limit_hit = False
    cursor_stalled = False
    request_failed = False
    new_trades = 0
    seen_cursors = set()
    error_message = None
    first_batch_earliest = None
    latest_fetched = None

    try:
        while pages < MAX_PAGES:
            batch, next_cursor = fetch(cursor)
            pages += 1
            if batch:
                timestamps = [float(t[2]) for t in batch]
                first_batch_earliest = min(timestamps) if first_batch_earliest is None else first_batch_earliest
                latest_fetched = max(max(timestamps), latest_fetched or 0)
            for trade in batch:
                key = trade_key(trade)
                if key not in records:
                    new_trades += 1
                records[key] = [key, float(trade[2]), float(trade[1]), str(trade[3])]

            # The cursor, rather than the batch length, is the authoritative
            # pagination progress signal. A short batch normally indicates
            # the head of the feed has been reached.
            if not batch:
                cursor = next_cursor
                break
            if next_cursor == cursor or next_cursor in seen_cursors:
                cursor_stalled = True
                break
            seen_cursors.add(next_cursor)
            cursor = next_cursor
            if len(batch) < 1000:
                break
        else:
            page_limit_hit = True
    except Exception as exc:
        request_failed = True
        error_message = str(exc)

    # If an old state has no cursor, the initial Kraken response is only a
    # recent slice of history. Never label older windows complete on that basis.
    # Likewise, a fetch failure or paging cap breaks our continuity claim.
    if request_failed or page_limit_hit or cursor_stalled:
        continuity_start = now

    cutoff = now - MAX_AGE_SECONDS
    stored = sorted((row for row in records.values() if cutoff <= row[1] <= now), key=lambda row: row[1])
    latest_trade = stored[-1][1] if stored else None
    fresh = latest_trade is not None and now - latest_trade <= MAX_STALENESS_SECONDS

    # If data stops arriving, mark continuity as broken. A 10-minute stale
    # threshold is operational monitoring, not an exchange-side guarantee.
    if not fresh:
        continuity_start = now

    # Guard against a persisted cursor with an unexpectedly old next batch.
    # This detects some (not all) missed-fetch situations.
    potential_gap = (previous_latest is not None and first_batch_earliest is not None
                     and first_batch_earliest > previous_latest + MAX_STALENESS_SECONDS)
    if potential_gap:
        continuity_start = now

    windows = {}
    for name, seconds in WINDOWS.items():
        subset = [row for row in stored if now - seconds <= row[1] <= now]
        buy = sum(row[2] for row in subset if row[3] == 'b')
        sell = sum(row[2] for row in subset if row[3] == 's')
        covered = (not request_failed and not page_limit_hit and not cursor_stalled
                   and fresh and not potential_gap and now - continuity_start >= seconds)
        windows[name] = {
            'buy_volume_eth': round(buy, 6),
            'sell_volume_eth': round(sell, 6),
            'cvd_delta_eth': round(buy - sell, 6),
            'trade_count': len(subset),
            'coverage_status': 'provisionally_complete' if covered else 'unverified'
        }

    state = {
        'cursor': cursor,
        'trades': stored,
        'continuity_start_utc_timestamp': continuity_start
    }
    output = {
        'exchange': 'Kraken Spot',
        'symbol': 'ETH/USD',
        'calculated_at_utc': iso(now),
        'earliest_trade_utc': iso(stored[0][1]) if stored else None,
        'latest_trade_utc': iso(latest_trade),
        'stored_trade_count': len(stored),
        'new_trade_count': new_trades,
        'pages_fetched': pages,
        'page_limit_hit': page_limit_hit,
        'cursor_stalled': cursor_stalled,
        'request_failed': request_failed,
        'error_message': error_message,
        'possible_gap_detected': potential_gap,
        'continuity_tracking_started_utc': iso(continuity_start),
        'data_completeness': 'provisionally_complete' if all(
            w['coverage_status'] == 'provisionally_complete' for w in windows.values()
        ) else 'unverified',
        'coverage_note': 'Provisional status tracks uninterrupted polling; it does not independently audit Kraken trade completeness.',
        'windows': windows
    }

    # Avoid advancing the stored cursor on failed/partial API retrieval. The
    # existing state remains intact for a future retry in these cases.
    if request_failed or page_limit_hit or cursor_stalled:
        print(json.dumps(output, indent=2))
        raise RuntimeError('Collection incomplete; previous state preserved: ' + (error_message or 'pagination issue'))

    for path, payload in ((STATE, state), (OUTPUT, output)):
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as file:
            json.dump(payload, file, indent=2 if path == OUTPUT else None, ensure_ascii=False)
        os.replace(tmp, path)
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
