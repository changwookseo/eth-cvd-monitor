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
- Next prerequisite: an authorized execution environment able to access the Binance futures API. Re-run this first gate there, verify saved data and a subsequent automatic refresh, then connect the verified snapshot to the existing report without changing its layout.

## Sequential gate
Funding and futures CVD recovery have NOT been started because OI has not passed the full live collection → GitHub storage → automatic refresh → report integration gate. Other indicators remain pending.

## Existing functionality
Existing spot collectors/workflows were not edited.
Following the collector commit, existing spot workflows succeeded:
- Kraken: https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40616918089
- Binance: https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40616917304

Canonical report, call rules, validation contract, 7 indicator weights (20/15/18/20/12/10/5), and historical research/backtest data were not edited. Research-only snapshots and artifacts must not be claimed as a production real-time pipeline.
