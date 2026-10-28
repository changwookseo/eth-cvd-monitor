# ETH ESI 2.0 recovery verification — 2026-10-28 KST

Overall: IN PROGRESS, NOT COMPLETE. Cron-side live Binance OI access succeeded; automatic GitHub import and report verification remain pending.

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

## Cron-side live OI recovery — 2026-10-28

- Signed-in Cron console confirmed existing Kraken job 8720420 and Binance spot job 8723157 enabled, each running every five minutes. Both returned GitHub dispatch HTTP 204; corresponding GitHub spot workflows succeeded.
- The prior direct GitHub runner OI HTTP 451 is not a complete diagnosis of source availability.
- A real Cron test run against the exact Binance OI source returned HTTP 200 at 2026-10-28T01:54:24Z, with body:
  {"symbol":"ETHUSDT","openInterest":"2354781.565","time":1793152461259}
- Observation time: 2026-10-28T01:54:21.259Z (10:54:21.259 KST). Scope: Binance USD-M ETHUSDT perpetual, unit ETH. Do not interpret as market-wide or USD-denominated OI.
- Created independent Cron job 8738287, title Binance ETH OI 5min, enabled, schedule */5 * * * *, Asia/Seoul, saveResponses=true. Existing CVD jobs unchanged.
- First scheduled execution was planned for 11:00 KST. At preparation time, its success had not yet been verified.
- Prepared eth_oi_cron_import.py and updated the existing manual eth-oi-live.yml to import saved Cron responses with CRONJOB_API_KEY from GitHub Actions Secrets. No key has been created or registered by this recovery work.
- Simulated-response checks passed for value/symbol/source/job/freshness/status checks and preservation of existing data on failure. These checks are not a live authenticated import.
- Creating a new Cron API key and storing it as repository secret grants GitHub Actions new access to the Cron account and requires user approval before that action.
- Cron API documentation lists a default 100 requests/day limit. Import uses two API requests per snapshot; five-minute imports would require at least 576 requests/day. Actual account quota and a sustainable refresh schedule must be checked before enabling automatic import. No quota upgrade or purchase is authorized or performed.
- No live OI snapshot has yet been automatically committed by this importer. No full report integration is claimed. Funding and futures CVD remain unstarted under the sequential gate.
