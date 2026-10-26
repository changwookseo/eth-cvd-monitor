"""Backfill Binance ETHUSDT USD-M open-interest metrics and funding, 180 completed UTC days.
No API keys. Missing archives and ambiguous timing are explicitly reported.
"""
import csv
import io
import json
import time
import urllib.error
import urllib.request
import zipfile
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = 'https://data.binance.vision/data/futures/um'
SYMBOL = 'ETHUSDT'
OUT = Path('research_derivatives')
# Binance UM metrics create_time labels changed on 2026-06-25. For OI,
# pre-change labels denote snapshot time; post-change denote interval START,
# with snapshot measured at label + 5 minutes. See README notes.
LABEL_CHANGE = datetime(2026, 6, 25, tzinfo=timezone.utc)


def fetch_zip(url):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'ETH-180D-Research/2.0'})
            with urllib.request.urlopen(req, timeout=35) as res:
                payload = res.read()
            with zipfile.ZipFile(io.BytesIO(payload)) as archive:
                names = [n for n in archive.namelist() if n.lower().endswith('.csv')]
                if len(names) != 1:
                    raise ValueError('Unexpected CSV count: ' + str(names))
                return list(csv.DictReader(io.TextIOWrapper(archive.open(names[0]), encoding='utf-8-sig')))
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            err = exc
        except (OSError, ValueError, zipfile.BadZipFile) as exc:
            err = exc
        time.sleep(2 ** attempt)
    raise RuntimeError(f'Unable to fetch {url}: {err}')


def parse_time(value):
    if value is None or not str(value).strip():
        raise ValueError('Missing timestamp')
    value = str(value).strip()
    if value.isdigit():
        num = int(value)
        if num >= 10**14:
            num //= 1000
        return datetime.fromtimestamp(num / 1000, timezone.utc)
    return datetime.fromisoformat(value.replace('Z', '+00:00')).replace(tzinfo=timezone.utc) if '+' not in value and not value.endswith('Z') else datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(timezone.utc)


def number(row, *keys):
    for key in keys:
        if key in row and row[key] not in ('', None):
            return float(row[key])
    return None


def day_range(start, end):
    day = start
    while day <= end:
        yield day
        day += timedelta(days=1)


def funding_urls(start, end):
    month = start.replace(day=1)
    while month <= end:
        next_month = (month.replace(day=28) + timedelta(days=4)).replace(day=1)
        if next_month <= end:
            label = month.strftime('%Y-%m')
            yield f'{ROOT}/monthly/fundingRate/{SYMBOL}/{SYMBOL}-fundingRate-{label}.zip'
        else:
            for day in day_range(max(month, start), end):
                label = day.strftime('%Y-%m-%d')
                yield f'{ROOT}/daily/fundingRate/{SYMBOL}/{SYMBOL}-fundingRate-{label}.zip'
        month = next_month



def fetch_funding_api_day(day):
    """Fallback to official Binance USD-M funding history API for one UTC day."""
    from urllib.parse import urlencode
    start_ms = int(day.timestamp() * 1000)
    end_ms = int((day + timedelta(days=1)).timestamp() * 1000) - 1
    result = []
    cursor = start_ms
    while cursor <= end_ms:
        params = urlencode({'symbol': SYMBOL, 'startTime': cursor, 'endTime': end_ms, 'limit': 1000})
        url = 'https://fapi.binance.com/fapi/v1/fundingRate?' + params
        error = None
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'ETH-180D-Research/2.1'})
                with urllib.request.urlopen(req, timeout=30) as response:
                    payload = json.load(response)
                if not isinstance(payload, list):
                    raise ValueError('Unexpected funding API response')
                result.extend(payload)
                break
            except (urllib.error.HTTPError, urllib.error.URLError, OSError, ValueError) as exc:
                error = exc
                time.sleep(2 ** attempt)
        else:
            raise RuntimeError(f'Funding API unavailable for {day.date()}: {error}')
        if len(payload) < 1000:
            break
        last_ts = max(int(r['fundingTime']) for r in payload)
        if last_ts < cursor:
            raise ValueError('Funding API pagination did not advance')
        cursor = last_ts + 1
    return result

def main():
    now = datetime.now(timezone.utc)
    end = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    start = end - timedelta(days=179)
    end_exclusive = end + timedelta(days=1)
    OUT.mkdir(exist_ok=True)
    missing_metrics, missing_funding, schema_errors = [], [], []
    funding_api_recovered_days, funding_api_failed_days = [], []
    oi_by_hour = defaultdict(list)
    for day in day_range(start, end):
        stamp = day.strftime('%Y-%m-%d')
        url = f'{ROOT}/daily/metrics/{SYMBOL}/{SYMBOL}-metrics-{stamp}.zip'
        rows = fetch_zip(url)
        if rows is None:
            missing_metrics.append(stamp)
            continue
        for row in rows:
            try:
                label = parse_time(row.get('create_time'))
                oi_eth = number(row, 'sum_open_interest')
                oi_usdt = number(row, 'sum_open_interest_value')
                if oi_eth is None or oi_usdt is None:
                    raise ValueError('Missing OI columns: ' + ','.join(row.keys()))
                observed_at = label + (timedelta(minutes=5) if label >= LABEL_CHANGE else timedelta(0))
                if start <= observed_at < end_exclusive:
                    bucket = observed_at.replace(minute=0, second=0, microsecond=0)
                    oi_by_hour[bucket].append((observed_at, oi_eth, oi_usdt))
            except (ValueError, OverflowError, TypeError) as exc:
                if len(schema_errors) < 30:
                    schema_errors.append(f'{stamp}: {exc}')
    oi = {}
    for hour, snapshots in oi_by_hour.items():
        latest = max(snapshots, key=lambda x: x[0])
        oi[hour] = {'oi_observed_at_utc': latest[0].isoformat(), 'oi_eth': latest[1], 'oi_usdt': latest[2], 'oi_samples': len(snapshots)}

    funding = {}
    for url in funding_urls(start, end):
        rows = fetch_zip(url)
        if rows is None:
            # Monthly archives are preferred. For missing daily archives, use the
            # official USD-M funding history endpoint, without fabricating rates.
            try:
                day_label = url.rsplit('-', 3)[-3:]
                day_str = '-'.join(day_label).removesuffix('.zip')
                day = datetime.strptime(day_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
                rows = fetch_funding_api_day(day)
                if rows:
                    funding_api_recovered_days.append(day_str)
                else:
                    missing_funding.append(url)
                    funding_api_failed_days.append(day_str + ': empty API response')
                    continue
            except (RuntimeError, ValueError) as exc:
                missing_funding.append(url)
                funding_api_failed_days.append(str(exc))
                continue
        for row in rows:
            try:
                ts = parse_time(row.get('calc_time') or row.get('fundingTime') or row.get('funding_time'))
                rate = number(row, 'last_funding_rate', 'fundingRate', 'funding_rate')
                if rate is None:
                    raise ValueError('Missing funding rate: ' + ','.join(row.keys()))
                if start <= ts < end_exclusive:
                    funding[ts] = rate
            except (ValueError, OverflowError, TypeError) as exc:
                if len(schema_errors) < 30:
                    schema_errors.append(f'funding: {exc}')

    with (OUT / 'binance_oi_1h.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['utc_hour', 'oi_observed_at_utc', 'oi_eth', 'oi_usdt', 'oi_samples', 'oi_change_1h_pct', 'oi_change_4h_pct'])
        for hour in sorted(oi):
            cur = oi[hour]
            def change(n):
                prev = oi.get(hour - timedelta(hours=n))
                return (cur['oi_eth'] / prev['oi_eth'] - 1) * 100 if prev and prev['oi_eth'] else None
            w.writerow([hour.isoformat(), cur['oi_observed_at_utc'], cur['oi_eth'], cur['oi_usdt'], cur['oi_samples'], change(1), change(4)])
    with (OUT / 'binance_funding_events.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['funding_time_utc', 'funding_rate', 'funding_rate_pct'])
        for ts, rate in sorted(funding.items()):
            w.writerow([ts.isoformat(), rate, rate * 100])
    summary = {
        'generated_utc': now.isoformat(), 'start_utc': start.isoformat(), 'end_utc_exclusive': end_exclusive.isoformat(),
        'expected_hourly_oi_buckets': 4320, 'oi_hourly_buckets': len(oi), 'funding_events': len(funding),
        'missing_metrics_days': missing_metrics, 'missing_funding_archives': missing_funding,
        'funding_api_recovered_days': funding_api_recovered_days, 'funding_api_failed_days': funding_api_failed_days,
        'schema_errors': schema_errors,
        'limitations': [
            'Binance USD-M ETHUSDT only; not market-wide open interest.',
            'OI archive contains 5-minute snapshots; hourly data uses last observed snapshot within the hour.',
            'Binance UM metrics labeling changed on 2026-06-25; post-change OI timestamps are shifted +5m to observation time. Verify archive semantics before high-frequency causal inference.',
            'Funding is settlement-event rate, not an hourly or uniformly 8h-normalized series.',
            'Historical forced-liquidation quantities are NOT collected; OI decrease does not prove liquidation.',
            'Missing or unrecognized archives are not imputed.'
        ]
    }
    (OUT / 'derivatives_status.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
    if missing_metrics or missing_funding or schema_errors or len(oi) != 4320:
        print('WARNING: data incomplete or schema issues; inspect derivatives_status.json', flush=True)


if __name__ == '__main__':
    main()
