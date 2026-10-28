# ETH ESI 2.0 recovery verification — 2026-10-28 KST

Overall: BLOCKED, NOT COMPLETE.

## OI: first verification gate
- Added an independent collector: `eth_oi_live.py`.
- Source: https://fapi.binance.com/fapi/v1/openInterest?symbol=ETHUSDT
- Scope: Binance USD-M ETHUSDT perpetual, ETH units; not total-market OI.
- Local response-validation checks passed: positive finite value, correct symbol, freshness; stale/zero/NaN/wrong-symbol responses rejected. These are simulated-response checks, not live collection success.
- Actual local API request: HTTP 451.
- Actual GitHub Actions run: https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40616919861
- Runner: GitHub hosted ubuntu-24.04, Azure eastus.
- Actual API collection step: FAILED, HTTP 451 at 2026-10-28T01:45:24Z (10:45:24 KST).
- Failure artifact uploaded: eth-oi-failure-40616919861, artifact ID 12786120409.
- Verified snapshot commit: SKIPPED. No successful live OI data was stored.
- Scheduled refresh: NOT VERIFIED. New OI workflow is manual-only while source access is blocked.
- Report integration: NOT COMPLETED. No unverified OI is inserted into the report.
- Next investigation: reuse the previously working Binance Vision public-data routes before concluding an execution-environment change is required. The REST OI route remains blocked; historical archives are accessible but do not establish real-time recovery.

## Sequential gate
Funding and futures CVD recovery have NOT been started because OI has not passed the full live collection → GitHub storage → automatic refresh → report integration gate. Other indicators remain pending.

## Existing functionality
Existing spot collectors/workflows were not edited.
Following the collector commit, existing spot workflows succeeded:
- Kraken: https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40616918089
- Binance: https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40616917304

Canonical report, call rules, validation contract, 7 indicator weights (20/15/18/20/12/10/5), and historical research/backtest data were not edited. Research-only snapshots and artifacts must not be claimed as a production real-time pipeline.

## Follow-up: previously successful Binance access routes

The initial statement that changing execution environment was required was premature. Existing successful routes were checked:
- Spot CVD uses https://data-api.binance.vision/api/v3/aggTrades (binance_cvd.py); this is the spot market-data route, not evidence of a working futures OI endpoint.
- Historical futures OI uses https://data.binance.vision/data/futures/um/daily/metrics/ETHUSDT/ETHUSDT-metrics-YYYY-MM-DD.zip through eth_180d_derivatives.py.
- Past run #2 https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40284914578 logged 4,320 OI hourly buckets and no missing metrics days.
- Past run #3 https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40286041200 also logged 4,320 OI buckets, but 465 funding events with missing October archives and funding REST fallback HTTP 451. Workflow success alone did NOT establish complete funding data.
- Follow-up actual archive download: 2026-10-26 and 2026-10-25 OI metrics archives both returned HTTP 200 with 288 CSV rows each in the current environment. This confirms archive access only; row timing/completeness has not been independently verified in this follow-up.
- The 2026-10-27 metrics archive returned HTTP 404 in the current environment.
- Binance documents daily public archives as becoming available the next day: https://github.com/binance/binance-public-data . Archive results must retain observation times and must not be represented as live snapshots.
- Overall real-time OI gate remains incomplete. Original report layout, weights and 180-day data are unchanged.
