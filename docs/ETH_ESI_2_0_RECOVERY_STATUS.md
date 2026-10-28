# ETH ESI 2.0 recovery verification — 2026-10-28 KST

Overall (latest checkpoint 2026-10-29 02:27 KST): PARTIAL RECOVERY, NOT COMPLETE. OKX ETH-USDT-SWAP OI scoped gate now PASSED: independent schedule success, repeated workflow_run collection and JSON commits, and historical real report-output match all verified. Binance OI Cron Secret is still unregistered; do not claim Binance/market-wide OI. OKX indicative funding live push collection and GitHub JSON storage are now verified, but automatic repeated funding collection and real report output are pending. Futures CVD remains unstarted. Historical checkpoints below are preserved.

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
- Prepared eth_oi_cron_import.py and updated the existing manual eth-oi-live.yml to import saved Cron responses with CRONJOB_API_KEY from GitHub Actions Secrets. A Cron API key was subsequently created with user approval; GitHub registration is still incomplete. See the resume checkpoint.
- Simulated-response checks passed for value/symbol/source/job/freshness/status checks and preservation of existing data on failure. These checks are not a live authenticated import.
- Creating a new Cron API key and storing it as repository secret grants GitHub Actions new access to the Cron account and requires user approval before that action.
- Cron API documentation lists a default 100 requests/day limit. Import uses two API requests per snapshot; five-minute imports would require at least 576 requests/day. Actual account quota and a sustainable refresh schedule must be checked before enabling automatic import. No quota upgrade or purchase is authorized or performed.
- No live OI snapshot has yet been automatically committed by this importer. No full report integration is claimed. Funding and futures CVD remain unstarted under the sequential gate.


## RESUME CHECKPOINT — 사용자 요청으로 일시 중단 (2026-10-28 KST)

### 가장 최근 확정 상태
- 사용자는 새 Cron API 키 생성 및 저장소의 `CRONJOB_API_KEY` Secret 등록을 명시적으로 승인했습니다 (“등록해줘”). 같은 범위의 작업을 재개할 때 승인을 반복 요청하지 않습니다.
- cron-job.org Settings에서 API 키 **생성 완료**. 키 제목: `eth-cvd-monitor OI import`.
- 키 값은 채팅, 코드, 이 문서, 로그에 기록하지 않았습니다. 재개 시 같은 제목의 기존 키를 확인하고, 중복 키를 만들지 않습니다.
- GitHub 저장소 Secret **등록 미완료**. 브라우저 GitHub 로그인 시 사이트가 `Incorrect username or password.`를 표시했습니다.
- GitHub 인증을 위해 사용자에게 현재 브라우저 제어를 넘긴 상태입니다. 로그인 성공은 아직 확인되지 않았습니다. 비밀번호·OTP·API 키를 채팅으로 요청하지 않습니다.
- 사용자는 작업을 잠시 중단하고 현재 상태를 저장해 달라고 요청했습니다. 이 문서 저장 후 추가 복구 변경을 진행하지 않습니다.

### 이미 반영된 파일 및 커밋
| 파일 | 상태 |
| --- | --- |
| `eth_oi_live.py` | GitHub 러너 직접 호출 방식. 실제 HTTP 451 확인. 전체 접근 불가로 일반화하지 않음. |
| `eth_oi_cron_import.py` | Cron 응답 조회·원천/종목/시각/값/성공 여부 검증 및 기존 데이터 보존 코드 준비. 실제 인증 조회는 아직 미검증. |
| `.github/workflows/eth-oi-live.yml` | `secrets.CRONJOB_API_KEY`를 사용하는 Cron importer로 수정. 수동 실행 전용, 자동 실행 미활성화. |
| `docs/ETH_ESI_2_0_RECOVERY_STATUS.md` | 본 재개 기준 기록. |

- importer 추가 커밋: `2ef3c7a1b3e615eb2e6823f0985e86c7918e355b`
- workflow 수정 커밋: `b02fe3355000c9758316fd2a23194002111e3e55`
- Cron 실수집 성공 기록 커밋: `caab293425cdb00a2be5bbf2c8612ade6ac901d0`

### Cron 작업 식별자
| 작업 | ID | 마지막 확인 상태 |
| --- | --- | --- |
| Binance ETH OI 5min | 8738287 | 활성화, 5분 주기, 응답 저장 켜짐. 시험 호출 HTTP 200. 예약 실행 성공은 아직 미검증. |
| Binance ETH CVD 5min | 8723157 | 기존 정상, 5분 주기 GitHub dispatch HTTP 204. 변경하지 않음. |
| ETH CVD 5min (Kraken) | 8720420 | 기존 정상, 5분 주기 GitHub dispatch HTTP 204. 변경하지 않음. |

### 재개 순서
1. 이 문서를 읽고 GitHub/Cron 최신 상태와 파일 변경 여부부터 확인합니다.
2. GitHub 브라우저 로그인 완료 여부를 확인합니다. 필요할 때 보안 로그인 흐름으로 재개하고, 잘못된 자격 증명으로 반복 시도하지 않습니다. 브라우저 세션이 보존된다고 가정하지 않습니다.
3. Cron Settings에서 제목 `eth-cvd-monitor OI import`인 기존 API 키를 찾아, 값을 채팅·스크린샷·코드·로그에 노출하지 않고 저장소 `changwookseo/eth-cvd-monitor`의 Actions Secret `CRONJOB_API_KEY`에 등록합니다. 이미 등록되었는지 먼저 확인합니다.
4. Cron OI 작업 8738287의 실제 예약 실행 HTTP 상태와 응답의 관측시각을 확인합니다. 오래된 시험 수치를 현재값으로 사용하지 않습니다.
5. 실제 Cron API 인증 조회 및 `ETH Live OI` 수동 실행을 검증하고, GitHub에 생성된 `eth_oi_latest.json`의 source/시각/단위/값과 원천 Cron 응답을 대조합니다.
6. Cron API의 실제 계정 요청 한도를 확인합니다. 현재 importer는 수집당 API 요청 2회이므로 5분 저장에는 최소 576회/일이 필요합니다. 기본 문서 한도 100회/일과 충돌하므로 한도 확인 없이 5분 자동 import를 켜거나 실시간 완전 복구를 선언하지 않습니다. 유료 변경·구매는 승인되지 않았습니다.
7. 허용되는 주기에서 자동 저장의 다음 실행까지 확인하고, 실제 갱신 시각·GitHub 커밋을 검증합니다. 요구 주기 충족 여부를 명시합니다.
8. 기존 ETH ESI 2.0 보고서에서 OI가 원천·관측시각·단위와 함께 실제 반영되는지 검증합니다. 코드 준비나 문서 추가를 보고서 반영 완료로 처리하지 않습니다.
9. OI의 실제 수집 → GitHub 저장 → 자동 갱신 → 보고서 반영이 모두 검증된 뒤에만 펀딩비, 그 다음 선물 CVD로 진행합니다.

### 유지해야 하는 사용자 원칙
- 기존 코드와 자동화 설정을 먼저 확인하고 필요한 부분만 수정합니다.
- 보고서 정본, 1~13번 양식, 7지표 가중치 20/15/18/20/12/10/5, 기존 180일 백데이터를 변경하지 않습니다.
- 기존 현물 CVD 정상 기능을 훼손하지 않습니다.
- 완료/실패/미검증/미착수를 구분하고 전체 복구 완료를 선포하지 않습니다.
- 현재 전체 상태: **OI 부분 복구 / GitHub 인증 단계에서 중단 / 펀딩비·선물 CVD 미착수**.

재개 요청 예: “ETH ESI 2.0 복구를 저장된 진행 상태부터 이어서 해줘.”


## 자동 복구 점검 추가 — 2026-10-28 11:34 KST

- 사용자가 작업 재개와 화면 이탈 후 복구 시도를 승인했으므로 이전의 "일시 중단" 문구는 과거 체크포인트로만 해석합니다.
- GitHub 기본 브랜치의 기존 Binance OI Cron importer는 그대로 유지했습니다. GitHub Secret `CRONJOB_API_KEY` 등록은 이 실행 환경의 GitHub 커넥터에서 지원되지 않아 인증 수집을 완료하지 못했습니다. Cron 작업의 최신 예약 실행 성공도 직접 확인하지 못했습니다.
- Binance OI REST 엔드포인트는 GitHub hosted runner에서 재시험 결과 HTTP 451이었습니다. `fapi1`/`fapi2`는 HTTP 202 비JSON 응답이었으므로 대체 경로로 사용할 수 없습니다.
- 독립 진단 브랜치 `repair/eth-oi-public-api-probe-20261028`에서 다른 거래소의 공개 OI 경로를 실제 테스트했습니다. OKX ETH-USDT-SWAP는 HTTP 200 및 필드 검증 성공, Bybit는 HTTP 403, Bitget는 HTTP 200이나 현재 검증 로직의 필드 기준 미통과였습니다. 진단 실행: https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40621641014
- **OKX OI는 Binance OI와 다른 시장입니다.** 기존 Binance 수집기를 대체하거나 두 OI를 무조건 합산하지 않습니다.
- OKX 전용 독립 실시간 수집기 `eth_oi_okx_live.py`와 자동 워크플로 `.github/workflows/eth-oi-okx.yml`을 `main`에 추가했습니다. 기존 현물 CVD·기술지표·정본 파일은 수정하지 않았습니다.
- 최초 GitHub Actions push 실행 https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40621692565 은 수집·검증·JSON 커밋 단계까지 모두 성공했습니다.
- 첫 저장 스냅샷 `eth_oi_okx_latest.json`: 2026-10-28T02:34:11.266Z 관측, 642833.886 ETH (OKX ETH-USDT-SWAP 전용), 상태 VERIFIED. 이 값은 해당 시각의 기록이며 현재값으로 재사용하지 않습니다.
- 5분 GitHub schedule은 구성했으나 **다음 예약 실행과 연속 자동 갱신은 아직 검증 전**입니다. GitHub schedule은 지연될 수 있습니다.
- 기존 보고서의 OI 소스 읽기 및 실제 출력 반영은 미검증입니다. OI 전체 게이트 완료 아님; 펀딩비와 선물 CVD는 순차 원칙에 따라 미착수 상태입니다.
- 현재 상태: **OKX OI 실수집 및 GitHub 저장 성공 / 자동 반복 갱신·보고서 반영 미검증 / Binance OI Cron Secret 연동 미완료**.


## 자동 점검 실행 — 2026-10-28 12:24 KST (03:24 UTC)

- OI 선행 게이트를 유지했으며 펀딩비·선물 CVD 수집기는 수정하거나 실행하지 않았습니다.
- GitHub Actions 실행 목록을 직접 조회한 결과, 최초 OKX OI push 성공(02:34 UTC) 이후 03:23 UTC까지 **OKX OI의 `schedule` 이벤트 실행이 없었습니다**. 현물 CVD 워크플로의 5분 `workflow_dispatch` 성공은 OKX OI 예약 실행 증거가 아닙니다.
- OKX OI 워크플로의 예약 cron을 혼잡한 정각/5분 경계 `*/5 * * * *`에서 `2-59/5 * * * *`으로 최소 수정했습니다. 파일: `.github/workflows/eth-oi-okx.yml`, 커밋 `bc78ac36275ac7324c2bcc562cc750fc50843e10`. 기존 현물 CVD, 기술지표, 보고서 정본, 가중치, 백데이터는 변경하지 않았습니다.
- 수정 push로 발생한 GitHub Actions 실행 [40626442990](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40626442990)은 `success`로 종료됐습니다. 이는 **push 실행 성공이며 예약 실행 성공은 아닙니다**.
- 저장 JSON `eth_oi_okx_latest.json`이 실제로 새로 갱신됨을 재조회했습니다. 새 관측시각 `2026-10-28T03:23:59.771Z` (12:23:59.771 KST), OKX `ETH-USDT-SWAP` OI `646687.426 ETH`, `status=VERIFIED`, JSON blob SHA `3fc2a28ca698a7238b4ade8e1e71e79ab745f752`. 기존 11:34 KST 관측값과 다른 **두 번째 성공한 수집·커밋**입니다. Binance 또는 전체 시장 OI가 아닙니다.
- **남은 OI 게이트**: 변경된 cron으로 실제 `event=schedule` 실행이 발생하는지, 예약 실행이 다음 주기에서도 연속 성공하며 JSON이 갱신되는지, 실제 ETH ESI 2.0 보고서 출력에 관측시각·거래소 범위와 함께 반영되는지 검증. Binance Cron importer의 `CRONJOB_API_KEY` Secret은 미등록이며, 이를 우회하거나 자격증명을 출력하지 않았습니다.
- 현재 판정: OKX OI 공개 API 실제 수집 및 GitHub JSON 저장 **2회 확인**(서로 다른 push 기반 실행). **자동 예약 실행·연속 갱신·실제 보고서 출력 반영 미검증**. OI 전체 완료 아님; 펀딩비·선물 CVD 미착수; 완료 알림 금지.

## 자동 점검 실행 — 2026-10-28 13:52 KST (04:52 UTC)

- 앞선 12:24 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재점검했습니다. 펀딩비·선물 CVD는 변경하거나 시작하지 않았습니다.
- GitHub 기본 브랜치의 `.github/workflows/eth-oi-okx.yml`은 여전히 `schedule: 2-59/5 * * * *`, `workflow_dispatch`, 제한된 `push` 이벤트를 선언합니다. 이는 예약 설정의 존재이지 예약 실행 성공 증거가 아닙니다.
- `eth_oi_okx_latest.json`을 다시 읽었으나 관측시각은 여전히 **2026-10-28T03:23:59.771Z (12:23:59.771 KST)**, **646687.426 ETH**, `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `status=VERIFIED`, blob SHA `3fc2a28ca698a7238b4ade8e1e71e79ab745f752`로 변함없었습니다. 현재 실행 시각보다 약 88분 오래된 기록이며 **현재 실시간값으로 사용할 수 없습니다**. Binance OI나 전체 시장 OI가 아닙니다.
- GitHub 커밋 검색에서 `Update verified OKX ETH OI`는 02:34 UTC와 03:24 UTC의 **2건만** 확인했습니다. 03:24 UTC 이후 새 OKX OI 저장 커밋은 발견되지 않았습니다. 기존 push 실행 [40626442990](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40626442990)의 collect 잡 성공(수집·검증·커밋)은 재확인했으나 이는 예약 실행 증거가 아닙니다.
- 현 시점 GitHub 커넥터는 전체 Actions 실행 목록에서 이벤트 종류(`schedule`)를 조회하는 기능이 없고 공개 Actions URL 조회도 실패했습니다. 따라서 **예약 실행이 전혀 발생하지 않았다고 확정하지는 않습니다**. 다만 최신 JSON·커밋으로는 5분 주기 자동 저장과 연속 갱신을 검증할 수 없습니다.
- 보고서 호출 규칙에는 OKX OI 읽기 지침이 존재하지만, 실제 보고서 출력에 최신 실측치가 사용됐다는 실행 증거는 없습니다. 코드·보고서 정본·가중치·180일 백데이터는 변경하지 않았습니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 등록 미완료이며 우회하거나 자격증명을 요청/노출하지 않았습니다.
- 판정: **OI 전체 게이트 미통과**(5분 예약 연속 갱신 및 실제 보고서 출력 미검증). 펀딩비·선물 CVD 미착수. 전체 완료 알림 금지. 다음 실행에서는 먼저 Actions `schedule` 이벤트 로그에 접근 가능한지와 새 JSON/커밋의 갱신 여부를 확인하고, 확인되지 않은 상태에서 성공으로 표기하지 않습니다.

## 자동 점검 실행 — 2026-10-28 14:53 KST (05:53 UTC)

- 이전 13:52 KST 체크포인트와 main의 실제 `eth_oi_okx_latest.json`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_live.py`, 보고서 호출 규칙 및 정본을 재조회했습니다.
- OKX OI JSON은 여전히 `observed_at_utc=2026-10-28T03:23:59.771000+00:00` (12:23:59.771 KST), `value=646687.4260000017 ETH`, `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `status=VERIFIED`, blob SHA `3fc2a28ca698a7238b4ade8e1e71e79ab745f752`로 **변화가 없습니다**. 이 관측은 이번 점검보다 약 2시간 30분 오래되었으므로 현재 실시간값으로 사용할 수 없습니다. Binance 또는 시장 전체 OI로 표기하지 않습니다.
- GitHub 커밋 검색에서 `Update verified OKX ETH OI`는 기존 2건(`1c13dee0...`, `39ae1316...`)뿐이었고 새로운 OKX OI JSON 커밋은 확인되지 않았습니다. 같은 기간 기존 Kraken/Binance 현물 CVD JSON 커밋은 다수 확인되어 저장소 전체의 변경이 멈춘 것은 아닙니다.
- OKX 워크플로의 `schedule: 2-59/5 * * * *` 설정은 그대로 존재하지만, 현재 제공된 GitHub 커넥터에는 워크플로별 실행 목록과 트리거 이벤트를 조회하는 기능이 없습니다. 공개 GitHub Actions API 접근도 실패했습니다. 따라서 예약 실행 발생 여부 자체는 확정하지 않되, **5분 자동 연속 저장은 검증되지 않았고 최신 JSON으로는 갱신 성공 증거가 없습니다**.
- OKX 수집기는 실제 API 응답의 성공 코드, 정확한 종목, 양수·유한 OI, 300초 신선도를 검증하도록 작성돼 있음을 확인했습니다. 그러나 이번 점검에서 새로운 API 성공 응답을 직접 검증한 것은 아닙니다.
- 보고서 호출 규칙에 OKX OI 보조 원천을 읽는 조건이 있는 것은 확인했으나, 최신 실측값이 ETH ESI 2.0의 **실제 출력 결과에 반영된 실행 증거는 여전히 없습니다**. 오래된 값을 현재값으로 대체하지 않습니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 등록 미완료이며 우회·노출·재발급하지 않았습니다. 기존 현물 CVD·기술지표·정본·7지표 가중치·180일 백데이터는 변경하지 않았습니다.
- **판정: OI 전체 게이트 미통과**(예약 실행 연속 갱신 및 실제 보고서 출력 미검증). 펀딩비·선물 CVD 미착수. 전체 완료 알림 금지. 다음 실행에서는 우선 새로운 OKX OI JSON 관측시각과 커밋을 재확인하고, 가능하면 `schedule` 트리거의 Actions 실행 로그를 확인합니다.

## 자동 복구 점검 — 2026-10-28 15:47 KST (06:47 UTC)

- 이전 14:53 KST 체크포인트를 먼저 읽고 OI 선행 게이트를 재검증했습니다.
- 이번 실행에서는 GitHub REST Actions 전체 실행 목록 `GET /repos/changwookseo/eth-cvd-monitor/actions/runs?event=schedule&per_page=100`에 접근하여 **총 17건의 schedule 이벤트 전체를 확인**했습니다. 이 중 `ETH OKX Live OI` 실행은 **0건**이었습니다. 기존 기술지표와 Schedule Test의 예약 실행은 확인되어 저장소의 모든 schedule이 중단된 것은 아닙니다. 5분 간격 OKX 예약 실행은 실제로 작동했다고 확인할 수 없습니다.
- 기존 Binance Spot CVD는 외부 Cron이 약 5분마다 `workflow_dispatch`하는 실제 성공 실행이 확인됐습니다(예: [40645778581](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40645778581), 06:45 UTC, success). 간헐적인 실패도 있어 이 성공을 OKX 성공으로 대체하지 않습니다.
- **OI만 최소 수정:** `.github/workflows/eth-oi-okx.yml`에 기존 `schedule: 2-59/5 * * * *`를 유지하면서 `workflow_run`(Binance Spot CVD 완료, main)을 보조 트리거로 추가했습니다. 선행 현물 워크플로가 성공한 경우에만 OKX 수집 잡을 실행하도록 조건을 설정했습니다. 기존 Binance Spot CVD 워크플로는 수정하지 않았습니다. 수정 커밋: [09709a3](https://github.com/changwookseo/eth-cvd-monitor/commit/09709a3c647f04cd8cb00463dd5d35869ffffb59).
- 수정으로 발생한 **push** 실행 [40645957118](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40645957118)은 success로 종료됐습니다. API 수집·신선도 검증·JSON 커밋 잡 단계도 성공했습니다. JSON을 다시 읽어 `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `status=VERIFIED`, `unit=ETH`, `observed_at_utc=2026-10-28T06:47:06.884000+00:00` (15:47:06.884 KST), `value=651390.976000002 ETH`, blob SHA `ec90268f89fc4f619260bfa040ae4335c0726d66`을 확인했습니다. **OKX 단일 거래소 스냅샷**이며 Binance 또는 전체 시장 OI가 아닙니다.
- 이번 신규 성공은 **push 기반 실행**이며 자동 예약 또는 `workflow_run` 성공을 증명하지 않습니다. 다음 Binance Spot CVD 성공 종료 후 OKX `event=workflow_run` 발생 여부와 두 번 이상의 연속 자동 JSON 갱신·커밋을 확인해야 합니다.
- 실제 ETH ESI 2.0 보고서 **출력**에서 최신 OKX OI가 관측시각·범위와 함께 사용됐다는 증거는 여전히 없습니다. 보고서 호출 규칙에 OKX 파일을 읽는 조건만 확인했습니다. 따라서 OI 전체 게이트는 미통과입니다.
- `CRONJOB_API_KEY` Secret은 여전히 미등록으로 취급하며 접근·우회·노출·재발급하지 않았습니다. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터는 수정하지 않았습니다.
- **판정: OI 부분 복구 진전 / 자동 연속 갱신 및 보고서 실측 반영 미검증 / 펀딩비·선물 CVD 미착수 / 전체 완료 알림 금지.**


## 자동 복구 점검 — 2026-10-28 16:13 KST (07:13 UTC)

- 15:47 KST 체크포인트를 먼저 확인하고, 기존 OKX OI 보조 트리거의 **실제 무인 연속 실행 성공**을 새로 검증했습니다. GitHub Actions REST 전체 실행 목록에서 OKX OI `event=workflow_run`, `conclusion=success` 실행 5건을 확인했습니다: [06:50 UTC #40646333805](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40646333805), [06:55 UTC #40646833463](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40646833463), [07:00 UTC #40647365664](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40647365664), [07:05 UTC #40647854990](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40647854990), [07:10 UTC #40648395512](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40648395512). 이 실행들은 기존 Binance Spot CVD의 성공 완료 뒤 자동으로 시작됐으며 **push나 `schedule` 실행이 아닙니다**.
- 최근 두 자동 실행의 GitHub Actions jobs 상세에서 `Fetch and validate OKX ETH swap OI`, `Validate output contract and freshness`, `Commit verified OKX OI snapshot` 단계가 모두 `success`임을 확인했습니다. 각각 [07:05 실행](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40647854990) 및 [07:10 실행](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40648395512).
- 자동 실행에 대응하는 JSON 커밋의 변경 파일이 `eth_oi_okx_latest.json` 하나임을 확인했습니다. 서로 다른 저장 스냅샷은 다음과 같습니다(모두 **OKX ETH-USDT-SWAP 단일 거래소, ETH 단위**, status=VERIFIED): 06:50:47.699 UTC **651268.997 ETH** (commit `f7e0cc7`); 06:55:39.010 UTC **651133.429 ETH** (`d244cf8`); 07:01:02.196 UTC **650791.559 ETH** (`5650dfa`); 07:05:40.662 UTC **651185.097 ETH** (`569ed6b`); 07:10:45.242 UTC **651091.057 ETH** (`1a521da`). 각 커밋 참조로 JSON의 실제 `observed_at_utc`, `value`, `exchange`, `status`를 재조회했습니다.
- 최신 main JSON은 `observed_at_utc=2026-10-28T07:10:45.242Z` (16:10:45.242 KST), `value=651091.057 ETH`, `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `unit=ETH`, `status=VERIFIED`, blob SHA `d86088bfd28068743cd9fdbce845a19c3d289c72`. 이는 해당 관측시각의 실제 저장값이며 Binance OI나 전체 시장 OI가 아닙니다.
- **검증 결과의 정확한 범위:** OKX OI의 기존 `workflow_run` 보조 트리거에 의한 약 5분 간격 자동 수집→검증→JSON 저장·연속 커밋은 확인됐습니다. GitHub 자체 `event=schedule` cron의 성공은 이번에도 확인하지 못했으며, OKX 자동 수집은 Binance Spot CVD 성공에 종속됩니다. 따라서 독립 cron 예약 실행 성공으로 오인하지 않습니다.
- 보고서 호출 규칙의 `2-1`에 OKX OI JSON의 신선도·거래소 범위 확인 지침이 있음을 재확인했으나, **실제 ETH ESI 2.0 보고서 출력**에서 이 실측값이 표시됐다는 증거는 아직 없습니다. 저장소에는 별도 보고서 생성 실행기가 없으며 문서 지침만으로 자동 반영을 단정할 수 없습니다. OI 전체 게이트는 **자동 갱신까지 통과, 실제 보고서 출력 반영 검증 대기**입니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 미등록이며 접근·우회·노출·재발급하지 않았습니다. 기존 현물 CVD, 기술지표, 보고서 정본, 7지표 가중치(20/15/18/20/12/10/5), 180일 백데이터 및 기존 수집 코드는 수정하지 않았습니다.
- **순차 판정:** OI 전체 게이트 미통과(보고서 실제 출력 반영 미검증). 펀딩비·선물 CVD는 미착수 상태를 유지합니다. 전체 복구 완료 알림 금지. 다음 실행에서 최신 OI JSON의 지속 갱신과 실제 보고서 출력 증거를 우선 확인합니다.

## 자동 복구 점검 — 2026-10-28 17:27 KST (08:27 UTC)

- 이전 16:13 KST 체크포인트를 먼저 읽고 OI 선행 게이트를 다시 검증했습니다. 펀딩비·선물 CVD는 시작하지 않았습니다.
- GitHub Actions 전체 실행 목록의 최신 OKX OI 실행 [40656683719](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40656683719)은 08:25:31 UTC에 `event=workflow_run`으로 시작되어 `conclusion=success`로 종료되었습니다. 직전 [40656098812](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40656098812)(08:20:39 UTC), [40655508110](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40655508110)(08:15:37 UTC)도 동일하게 `workflow_run` 성공입니다. 두 최신 실행의 jobs API에서 `Fetch and validate OKX ETH swap OI`, `Validate output contract and freshness`, `Commit verified OKX OI snapshot` 단계 모두 success를 확인했습니다. 이는 기존 Binance Spot CVD 성공 완료를 이용한 보조 트리거이며, **GitHub 자체 `schedule` 이벤트의 성공을 의미하지 않습니다**.
- 실제 저장된 서로 다른 세 JSON 버전을 커밋 SHA로 읽었습니다. 모두 `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `unit=ETH`, `status=VERIFIED`입니다: 08:15:43.285 UTC **651379.418 ETH** (commit `6f48b1b`); 08:20:45.659 UTC **651514.837 ETH** (`94d32c4`); 08:25:39.904 UTC **652661.245 ETH** (`4b444b8`). 마지막 시각은 17:25:39.904 KST이며, 이번 점검 시각보다 약 2분 전입니다. 값은 **OKX ETH-USDT-SWAP 단일 거래소 OI**이며 Binance OI 또는 전체 시장 OI가 아닙니다.
- 마지막 [JSON 변경 커밋](https://github.com/changwookseo/eth-cvd-monitor/commit/4b444b8c26a6ce67fe16ebaaba600fa99baf1ca4)의 변경 파일이 `eth_oi_okx_latest.json` 하나임을 확인했습니다. 최신 main JSON의 blob SHA는 `bea0a715ca29bd7d3edda7b09f64eda6c4cb6584`입니다. 자동 실행 → 수집기/신선도 검증 → JSON 저장·커밋 → 연속 갱신 게이트는 보조 트리거 기준으로 계속 통과 중입니다. 별도의 원천 API 수동 직접 호출은 이번 점검에서 수행하지 않았으며 Actions 수집 단계의 성공 및 저장값으로 검증했습니다.
- 보고서 호출 규칙 `docs/ETH_ESI_2_0_REPORT_CALL_RULES.md`의 2-1에 OKX OI를 읽고 신선도·거래소 범위를 검증하라는 지침이 있음을 재확인했습니다. 그러나 저장소 루트에는 독립적인 보고서 생성 실행기가 확인되지 않았고, **ETH ESI 2.0 실제 보고서 출력에 이 최신 OI 실측값이 반영된 실행 증거는 확보하지 못했습니다**. 문서 지침만으로 보고서 반영 완료라고 선언하지 않습니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 미등록으로 취급합니다. 우회·조회·재발급·노출하지 않았습니다. 기존 현물 CVD·기술지표·정본·7지표 가중치(20/15/18/20/12/10/5)·180일 백데이터는 변경하지 않았습니다.
- **판정: OI 자동 수집·연속 저장은 검증됨 / 실제 보고서 출력 반영 미검증 → OI 전체 게이트 미통과.** 펀딩비·선물 CVD 미착수. 전체 복구 완료 알림 금지. 다음 실행에서는 최신 JSON 연속 갱신과 보고서 실제 출력의 확인 가능한 증거를 우선 조사합니다.


## 자동 복구 점검 — 2026-10-28 18:56 KST (09:56 UTC)

- 직전 17:27 KST 체크포인트를 먼저 읽고 OKX OI 선행 게이트만 확인했습니다. 기존 코드/워크플로의 변경은 하지 않았으며 펀딩비·선물 CVD는 미착수입니다.
- `eth_oi_okx_latest.json`의 최신 main 저장값: `observed_at_utc=2026-10-28T09:55:42.053000+00:00` (18:55:42.053 KST), `fetched_at_utc=2026-10-28T09:55:42.142059+00:00`, `value=652145.178 ETH`, `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `unit=ETH`, `status=VERIFIED`, blob SHA `41d0c5ad3e63ffa63bf6ea9a5263f3b897c9c6ab`. OKX 단일 거래소의 해당 시각 관측값이며 Binance 또는 전체 시장 OI가 아닙니다.
- GitHub Actions bot의 서로 다른 세 저장 커밋에서 5분 간격으로 관측시각·OI 값·JSON blob이 연속 갱신됨을 직접 대조했습니다: 18:45:48.495 KST **651789.205 ETH** ([ada711d](https://github.com/changwookseo/eth-cvd-monitor/commit/ada711dd886d7470db66d9d589c6894c5b3c979c)); 18:50:46.827 KST **652955.330 ETH** ([4f43105](https://github.com/changwookseo/eth-cvd-monitor/commit/4f43105672ca2481d15833c105996c205731fc21)); 18:55:42.053 KST **652145.178 ETH** ([03f9143](https://github.com/changwookseo/eth-cvd-monitor/commit/03f9143b3381ae2431c4bc254b0bf9d5147b62e3)). 최근 두 커밋은 변경 파일이 `eth_oi_okx_latest.json` 하나이며 author/committer는 `github-actions[bot]`입니다.
- `.github/workflows/eth-oi-okx.yml`에서 `schedule: 2-59/5 * * * *` 및 기존 Binance Spot CVD 완료 성공에 연결된 `workflow_run` 보조 트리거가 그대로 유지됨을 확인했습니다. 이전 실행에서 `workflow_run` 자동 성공을 검증했고 이번 실행에서는 자동 bot JSON 커밋 3건을 확인했습니다. 단, **이번 실행에서 각 최근 Actions run의 event=workflow_run 또는 event=schedule은 별도 조회하지 못했으므로 독립 GitHub schedule 성공으로 표기하지 않습니다.**
- `eth_oi_okx_live.py`의 공개 OKX API 응답 코드·정확한 종목·양수/유한값·300초 신선도 검사 및 JSON 저장 경로를 재확인했습니다. 이번 실행에서 API를 직접 별도 호출한 것은 아니며, 실제 수집의 증거는 최신 저장값과 GitHub Actions bot 연속 커밋입니다.
- 보고서 호출 규칙 `docs/ETH_ESI_2_0_REPORT_CALL_RULES.md`의 2-1에 OKX OI JSON 조회·신선도·단일 거래소 범위 규칙이 존재합니다. 정본 `docs/ETH_ESI_2_0_CANONICAL_REPORT.md`는 7지표와 1~13번 형식을 유지합니다. 그러나 **최신 OI가 ETH ESI 2.0의 실제 완성 보고서 출력에 사용된 실행 증거는 여전히 없습니다.** 문서 규칙의 존재를 보고서 실측 반영 완료로 처리하지 않습니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 등록 미완료로 취급하고 조회·우회·노출·재발급하지 않았습니다. 현물 CVD·기술지표·보고서 정본·가중치(20/15/18/20/12/10/5)·180일 백데이터를 변경하지 않았습니다.
- **판정: OKX OI 연속 자동 JSON 갱신 지속 확인 / 실제 보고서 출력 반영 미검증 → OI 전체 게이트 미통과.** 펀딩비·선물 CVD 미착수. 전체 복구 완료 알림 금지. 다음 실행에서는 보고서의 실제 최신 OI 출력 증거 및 Actions 트리거별 실행을 확인합니다.


## 자동 복구 점검 — 2026-10-28 20:06 KST (11:06 UTC)

- 18:56 KST 최신 체크포인트를 먼저 읽고 OI 선행 게이트만 점검했습니다. 펀딩비·선물 CVD는 시작하지 않았습니다.
- OKX 전용 수집기 `eth_oi_okx_live.py`, 자동 워크플로 `.github/workflows/eth-oi-okx.yml`, 실제 JSON `eth_oi_okx_latest.json`, 보고서 호출 규칙·정본·검증 계약을 재조회했습니다. 기존 현물 CVD·기술지표·정본·가중치(20/15/18/20/12/10/5)·180일 백데이터는 수정하지 않았습니다.
- GitHub Actions 봇의 서로 다른 JSON 커밋 3건을 SHA별로 읽어 관측시각과 값이 연속 변경된 사실을 확인했습니다(모두 `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `unit=ETH`, `status=VERIFIED`): **19:50:46.640 KST 653166.742 ETH** ([f9bd3c5](https://github.com/changwookseo/eth-cvd-monitor/commit/f9bd3c5c2cc6b58d9edd6efd829a8dde90bd4758)), **19:55:38.657 KST 653203.088 ETH** ([dabd070](https://github.com/changwookseo/eth-cvd-monitor/commit/dabd070fedd17e8ab7c702b150cdfb79c8e4b755)), **20:01:03.006 KST 652795.324 ETH** ([99068fe](https://github.com/changwookseo/eth-cvd-monitor/commit/99068fe16cd4e0794215162087a9823c97f7eff5)). 각 커밋의 변경 파일은 `eth_oi_okx_latest.json` 하나였고 작성자는 `github-actions[bot]`이었습니다.
- 이어서 main JSON을 다시 읽어 **20:05:43.367 KST (2026-10-28T11:05:43.367Z) 651626.658 ETH**, blob SHA `2f763460fb464f795bdf5114584a7b22fe1b6c18`로 추가 갱신된 사실을 확인했습니다. 이 값은 **OKX ETH-USDT-SWAP 단일 거래소 OI**이며 Binance OI 또는 전체 시장 OI가 아닙니다. 당시의 저장 관측값이며 이후 시점의 현재값으로 재사용하지 않습니다.
- 워크플로에는 `schedule: 2-59/5 * * * *` 및 Binance Spot CVD 성공 완료 시 `workflow_run` 트리거가 유지됩니다. 이번 점검은 자동 봇의 서로 다른 연속 커밋을 검증했으나, 각 실행의 GitHub Actions `event`를 별도 조회하지 못했으므로 **독립 `schedule` 예약 실행 성공은 여전히 입증하지 않습니다**. 직전 체크포인트에서 확인된 `workflow_run` 연속 실행과도 구분합니다.
- 실제 원천 OKX API를 이번 실행에서 독립적으로 재호출한 것은 아닙니다. 수집 코드의 원천 URL·종목·응답 성공·관측 신선도 검사와, 실제 GitHub 자동 봇이 저장한 서로 다른 JSON 관측값을 확인했습니다.
- 보고서 호출 규칙의 2-1에 OKX OI 신선도·범위 검사 지침이 있지만 **실제 완성된 ETH ESI 2.0 보고서의 출력에 이 최신 실측값이 사용됐다는 실행 증거는 여전히 없습니다**. 정본·검증 계약은 문서이며 자동 보고서 생성기 실행 증거가 아닙니다. 이 상태를 보고서 반영 완료로 표기하지 않습니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 미등록으로 취급하고 등록을 우회하거나 자격증명을 조회·노출하지 않았습니다.
- **판정: OKX OI 수집 데이터의 약 5분 간격 자동 저장·연속 변경은 재검증됨 / GitHub 자체 schedule 이벤트 및 실제 완성 보고서 반영은 미검증 → OI 전체 게이트 미통과. 펀딩비·선물 CVD 미착수. 전체 완료 알림 금지.**

## 자동 복구 점검 — 2026-10-28 20:43 KST (11:43 UTC)

- 직전 20:06 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 검증했습니다. 펀딩비·선물 CVD는 미착수이며 기존 수집 코드, 워크플로, 정본, 7지표 가중치, 180일 백데이터를 수정하지 않았습니다.
- `eth_oi_okx_latest.json`의 main 최신 저장값은 **2026-10-28T11:40:42.608Z (20:40:42.608 KST) 649350.408 ETH**, `fetched_at_utc=2026-10-28T11:40:42.693134Z`, `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `unit=ETH`, `status=VERIFIED`, blob SHA `c7c63f9912f265e90443e56a5d281888760f8a4c`입니다. **OKX 단일 거래소 OI**이며 Binance 또는 시장 전체 OI가 아닙니다.
- 서로 다른 Actions bot 저장 커밋을 실제 JSON ref로 조회했습니다: 20:25:39.823 KST **650990.079 ETH** ([248c4cb](https://github.com/changwookseo/eth-cvd-monitor/commit/248c4cb60be0f7136e9d92712b82d4afd7f63cc8)), 20:35:40.537 KST **650077.543 ETH** ([f49f475](https://github.com/changwookseo/eth-cvd-monitor/commit/f49f475eb3bc1116062fa943e9ff9150034bc0d2)), 20:40:42.608 KST **649350.408 ETH** ([ab2463a](https://github.com/changwookseo/eth-cvd-monitor/commit/ab2463a48f928eab4e5d7970706d6a359cb103b1)). 최신 두 커밋의 author/committer는 `github-actions[bot]`이며 변경 파일은 `eth_oi_okx_latest.json` 하나였습니다. 최신 커밋 diff에서 관측시각과 OI 값이 실제로 달라졌음을 확인했습니다. 20:30 부근 저장 간격이 약 10분으로 늘어난 구간이 있으므로 **정확히 매 5분 무결점 실행이라고 주장하지 않습니다**.
- `.github/workflows/eth-oi-okx.yml`의 `schedule: 2-59/5 * * * *`와 기존 Binance Spot CVD 성공 완료에 종속된 `workflow_run` 트리거가 유지됩니다. **이번 실행에서는 Actions run의 실제 event와 job 로그를 직접 조회하지 못했으므로 독립 `schedule` 성공을 입증하지 않습니다.** 이전 체크포인트에서 확인된 `workflow_run` 성공과 구분합니다.
- `eth_oi_okx_live.py`에서 OKX 공개 API 응답 코드·종목·양수/유한값·300초 신선도 검사 및 원자적 JSON 저장 구현을 재확인했습니다. 이번 점검의 수집 증거는 GitHub bot의 실제 연속 JSON 변경이며 원천 API를 별도로 직접 재호출한 것은 아닙니다.
- 보고서 호출 규칙 `docs/ETH_ESI_2_0_REPORT_CALL_RULES.md` 2-1에 OKX OI를 신선도·범위 확인 후 읽으라는 지침이 유지됩니다. 그러나 **ETH ESI 2.0 완성 보고서의 실제 출력에 최신 OI 실측값이 반영됐다는 실행 증거는 확보하지 못했습니다**. 코드 검색에서도 독립 보고서 실행 증거가 확보되지 않았으므로 지침만으로 보고서 반영을 완료 처리하지 않습니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 미등록으로 취급하며 우회·조회·노출·재발급하지 않았습니다.
- **판정: OKX OI GitHub JSON의 자동 연속 갱신 재확인 / 독립 GitHub schedule 실행 및 실제 보고서 출력 반영 미검증 → OI 전체 게이트 미통과. 펀딩비·선물 CVD 미착수. 전체 복구 완료 알림 금지.**

## 자동 복구 점검 — 2026-10-28 21:34 KST (12:34 UTC)

- 기존 복구 상태 문서의 20:43 KST 체크포인트를 먼저 읽고, OI 선행 게이트만 다시 점검했습니다. 펀딩비·선물 CVD는 미착수이며 기존 수집기·워크플로·보고서 정본·7지표 가중치(20/15/18/20/12/10/5)·180일 백데이터는 변경하지 않았습니다.
- main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`, `docs/ETH_ESI_2_0_REPORT_CALL_RULES.md`, `docs/ETH_ESI_2_0_CANONICAL_REPORT.md`를 재조회했습니다. OKX API 응답의 `code=0`, 정확한 `ETH-USDT-SWAP` 종목, 양수/유한값, 최대 300초 신선도 검사를 수집기에서 확인했습니다. 최신 Actions 작업 로그에는 실제 수집 JSON과 검증 PASS가 기록됐으나 원시 HTTP 상태 코드를 별도 출력하지는 않았습니다.
- GitHub Actions REST 전체 실행 목록에서 **12:20:43, 12:25:35, 12:30:49 UTC** 시작한 `ETH OKX Live OI` 실행 [40687025994](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40687025994), [40687696921](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40687696921), [40688413207](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40688413207)의 `event=workflow_run`, `conclusion=success`를 직접 확인했습니다. 최근 세 실행의 jobs API에서 `Fetch and validate OKX ETH swap OI`, `Validate output contract and freshness`, `Commit verified OKX OI snapshot` 모두 success입니다.
- 각 GitHub Actions bot 커밋에 고정된 실제 JSON을 다시 읽어 **21:20:50.112 KST 631966.084 ETH** ([ab65fcc](https://github.com/changwookseo/eth-cvd-monitor/commit/ab65fcc8fce46dea47d67c00fc7b02e18a6b5048)), **21:25:43.069 KST 633037.058 ETH** ([a7d142d](https://github.com/changwookseo/eth-cvd-monitor/commit/a7d142d4845fa1f33a9e35003f636f9001d381b1)), **21:30:58.259 KST 633847.340 ETH** ([122678c](https://github.com/changwookseo/eth-cvd-monitor/commit/122678cefcbc8734bbd84ff204bf657381c432b6))로 연속 갱신됨을 확인했습니다. 모두 `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `unit=ETH`, `status=VERIFIED`이며 **OKX 단일 거래소 OI**입니다. Binance 또는 전체 시장 OI로 재표기하지 않습니다. 최신 main JSON blob SHA는 `6656d9ffeeef64858f726eba95b63b5e33f1f590`입니다.
- 최신 실행 [40688413207](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40688413207)의 job 로그에서 실제 API 수집 결과 JSON 출력, `PASS: OKX OI verified`, `git commit`, `git push origin HEAD:main` 성공까지 확인했습니다. 자동 수집·신선도 검증·JSON 커밋의 연결이 실측으로 검증됩니다.
- **트리거 구분:** 위 세 실행은 모두 기존 Binance Spot CVD 성공 완료에 연동된 `workflow_run`이며 독립 GitHub `schedule` 성공이 아닙니다. 최근 Actions 실행 목록에서 OKX `schedule` 성공은 확인하지 못했습니다. 11:55 UTC Binance Spot CVD 실패 때 OKX 실행 [40683696492](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40683696492)가 skipped인 사례도 있어, 외부 트리거 종속성과 누락 가능성을 유지합니다. 정확히 매 5분 무결점 실행이라고 단정하지 않습니다.
- **실제 보고서 출력 게이트 미통과:** 보고서 호출 규칙 2-1에 OKX OI 실측 조회 지침은 있으나, 최신 실측 OI가 ETH ESI 2.0 완성 보고서의 5번 항목에 표시된 실제 실행 증거는 확인되지 않았습니다. 예약 보고서의 최근 확인된 결과는 2026-10-27 실행으로, OKX OI 수집 도입 이전이므로 이 게이트의 증거가 될 수 없습니다. 지침·JSON 저장만으로 실제 보고서 반영 완료라고 표기하지 않습니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 미등록으로 취급합니다. 조회·우회·등록 시도·노출·재발급하지 않았습니다.
- **판정: OKX OI 실수집 → `workflow_run` 자동 반복 실행 → JSON 저장·연속 갱신 검증 / 독립 GitHub `schedule` 성공 및 ETH ESI 2.0 실제 보고서 출력 반영 미검증. OI 전체 게이트 미통과 → 펀딩비·선물 CVD 미착수. 전체 복구 완료 알림 금지.** 다음 실행에서 최신 자동 갱신 및 보고서 실제 출력 반영을 먼저 확인합니다.


## 자동 복구 점검 — 2026-10-28 23:05 KST (14:05 UTC)

- 직전 21:34 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증했습니다. 펀딩비·선물 CVD는 미착수이며 기존 수집기·워크플로·현물 CVD·기술지표·보고서 정본·7지표 가중치(20/15/18/20/12/10/5)·180일 백데이터는 수정하지 않았습니다.
- GitHub Actions 전체 실행 목록에서 OKX OI [40700949047](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40700949047) (13:55:35 UTC), [40701799534](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40701799534) (14:00:57 UTC), [40702551305](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40702551305) (14:05:35 UTC)가 모두 `event=workflow_run`, `conclusion=success`임을 직접 확인했습니다. 마지막 실행 jobs API에서 `Fetch and validate OKX ETH swap OI`, `Validate output contract and freshness`, `Commit verified OKX OI snapshot` 모두 성공했습니다. 이는 Binance Spot CVD 완료를 통한 **자동 반복 실행**이며 OKX 독립 `schedule` 이벤트 성공은 아닙니다.
- 서로 다른 GitHub Actions bot 커밋의 실제 JSON을 재조회했습니다: 22:55:42.626 KST **627318.591 ETH** ([051fb64](https://github.com/changwookseo/eth-cvd-monitor/commit/051fb64e04facc79299ad1c59dfaa6f1744c4985)), 23:01:03.676 KST **628213.309 ETH** ([1e016cb](https://github.com/changwookseo/eth-cvd-monitor/commit/1e016cb27e6b0253c6ee93a5cb6ca9a103eafdd8)), 23:05:41.858 KST **627482.011 ETH** ([0eeb326](https://github.com/changwookseo/eth-cvd-monitor/commit/0eeb326f260fad2b2bef4420fe6068e7e4b0519b)). 최신 main JSON blob SHA `1597617b4f13a150513acc931cea8073b2be5e16`. 모두 `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `unit=ETH`, `status=VERIFIED`입니다. **OKX 단일 거래소 OI**이며 Binance/전체 시장 OI가 아닙니다. 원천 API 직접 별도 HTTP 재호출은 이번 점검에서 하지 않았으며 Actions 실제 수집·검증 단계와 저장 JSON으로 확인했습니다.
- **새로운 중요한 검증 진척 — 실제 보고서 출력 반영 확인:** 예약 보고서 자동화의 2026-10-28 22:07 KST 실행 결과를 조회했습니다(실행 ID `7d7d2d46-bea8-8325-8803-b03d0a52ef57`, 13:07:42~13:09:24 UTC 실행). 보고서 제목 `ETH ESI 2.0 | 7지표 통합 상세 보고서`의 **5. OI·펀딩비 및 선물 CVD** 항목에 `OKX ETH-USDT-SWAP · 22:05:44 KST`, `630,332.863 ETH`, `OKX 단일 거래소 OI · VERIFIED`가 실제로 출력됐습니다. 이를 당시 저장 JSON [b1ecf5a](https://github.com/changwookseo/eth-cvd-monitor/blob/b1ecf5ab2f130fe7fa0fffc6ef99c9aed5c95953/eth_oi_okx_latest.json)의 `2026-10-28T13:05:44.094Z`, `630332.863 ETH`와 **시각·수치 일치**로 교차 확인했습니다. 이 보고서는 그 시각의 스냅샷을 정확히 반영한 것이며 23:05의 최신값이 과거 22:07 보고서에 반영됐다고 주장하지 않습니다. 예약 보고서 실행 결과 확인은 채팅/자동화 기록 조회이며 GitHub 자체 보고서 생성기 증거는 아닙니다.
- GitHub Actions 목록의 [Schedule Test 40701314349](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40701314349)는 `event=schedule`, `success`였지만 **다른 워크플로**입니다. 이를 OKX OI 자체의 `schedule` 성공으로 혼동하지 않습니다. 확인한 최근 OKX OI 실행은 모두 `workflow_run`이며 OKX 독립 GitHub cron `schedule` 성공은 아직 미검증입니다. 정확한 매 5분 무결점 갱신도 주장하지 않습니다.
- Binance Cron importer `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 미등록으로 취급합니다. 조회·우회·노출·재발급·등록 시도를 하지 않았습니다.
- **현재 OI 판정:** 공개 API 실수집·검증, GitHub 자동 반복 수집·연속 JSON 저장, 그리고 **22:07 KST 완성 보고서 5번 항목의 실제 실측 반영까지 검증**. 다만 사용자가 명시적으로 요구한 OKX 워크플로 자체 `schedule` 예약 실행 성공은 아직 검증되지 않아 **OI 전체 게이트를 최종 통과로 선언하지 않습니다**. 펀딩비·선물 CVD는 미착수 유지. 전체 복구 완료 알림 금지.


## 자동 복구 점검 — 2026-10-28 23:13 KST (14:13 UTC)

- 23:05 KST 체크포인트를 먼저 읽고 OKX OI 선행 게이트만 검증했습니다. 펀딩비·선물 CVD는 미착수 상태이며 수집 코드·워크플로·현물 CVD·기술지표·정본·7지표 가중치(20/15/18/20/12/10/5)·180일 백데이터는 수정하지 않았습니다.
- GitHub Actions REST 전체 실행 목록 최근 50건을 실제 조회했습니다. 최근 OKX OI 실행 17건은 모두 `event=workflow_run`이었고 그중 16건 success, 13:00:56 UTC 실행 [40692629374](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40692629374) 1건 skipped였습니다. 조회 범위에서 OKX 자체 `event=schedule` 성공은 **0건**입니다. 다른 워크플로 `Schedule Test`의 schedule 성공은 OKX OI의 성공으로 취급하지 않습니다. 이 조회만으로 저장소 전체 역사에 OKX schedule이 전혀 없었다고 단정하지 않습니다.
- 최신 14:10:41 UTC OKX OI 실행 [40703377602](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40703377602)는 `event=workflow_run`, `conclusion=success`. Jobs API에서 API 수집, 데이터 검증, JSON 커밋 단계 모두 success를 확인했습니다. 실제 job 로그에는 원천 수집 결과의 관측시각·값, `PASS: OKX OI verified`, `git commit`, `git push origin HEAD:main` 성공이 있습니다. 이는 **독립 schedule 성공이 아닌 Binance Spot CVD 성공 완료에 연동된 자동 실행**입니다.
- 세 고정 커밋의 실제 JSON을 대조했습니다: **22:50:54.817 KST 625450.292 ETH** ([c35c589](https://github.com/changwookseo/eth-cvd-monitor/commit/c35c589313d285360205216a874afeba2f7aa5e2)); **23:05:41.858 KST 627482.011 ETH** ([0eeb326](https://github.com/changwookseo/eth-cvd-monitor/commit/0eeb326f260fad2b2bef4420fe6068e7e4b0519b)); **23:10:48.086 KST 629307.997 ETH** ([8a93654](https://github.com/changwookseo/eth-cvd-monitor/commit/8a93654f5c24678b75cbb694548ae720c112ffe2)). 최신 JSON blob SHA `703d1c1161efdc87ba07c7d023bf46f480238df1`, `fetched_at_utc=2026-10-28T14:10:48.175659Z`, `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `unit=ETH`, `status=VERIFIED`. **OKX 단일 거래소 OI**이며 Binance OI나 전체 시장 OI가 아닙니다. 이 값은 23:10 관측 스냅샷이며 이후 시각의 현재값으로 재사용하지 않습니다.
- 23:05 체크포인트의 **22:07 KST 완성 보고서 5번 항목 OI 630332.863 ETH(22:05:44 KST)와 당시 원본 JSON의 실제 일치**는 이미 검증된 사실로 유지합니다. 이번 점검에서 새 보고서를 생성하거나 23:10 값을 보고서에 출력했다고 주장하지 않습니다.
- `.github/workflows/eth-oi-okx.yml`의 `schedule: 2-59/5 * * * *`와 `workflow_run` 보조 트리거를 재확인했습니다. 실제 자동 갱신은 작동하지만 독립 schedule 실행 증거가 없고 일부 skipped 사례가 있으므로 5분 무결점·독립 예약 실행 성공을 주장하지 않습니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 미등록 상태로 취급하고 우회·노출·재발급·등록을 시도하지 않았습니다. **OI 전체 게이트 미통과**(독립 schedule 미검증) → 펀딩비·선물 CVD 미착수. 전체 복구 완료 알림 금지. 다음 실행에서는 OKX 독립 schedule 이벤트의 실제 성공 여부를 먼저 확인합니다.


## 자동 복구 점검 — 2026-10-29 00:42 KST (2026-10-28 15:42 UTC)

- 2026-10-28 23:13 KST 체크포인트를 먼저 읽고 **OI 선행 게이트만** 재검증했습니다. 펀딩비·선물 CVD는 시작하지 않았습니다.
- GitHub Actions REST 최근 100건 중 `ETH OKX Live OI` 33건을 실행 이벤트별로 직접 조회했습니다. **33건 전부 `event=workflow_run`**, 이 중 **31건 success / 2건 skipped**이며, 조회 범위의 OKX 자체 `event=schedule` 실행은 **0건**입니다. 다른 `Schedule Test` 워크플로의 `event=schedule` 성공 1건은 OKX 자체 예약 실행 증거가 아닙니다. 조회 범위 밖까지 `schedule` 부재를 단정하지 않습니다.
- 최근 자동 실행 [40716714955](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40716714955), [40717521522](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40717521522), [40718374864](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40718374864)는 모두 `workflow_run` 성공이며 수집·신선도 검증·JSON 커밋 작업 단계가 모두 success입니다. 마지막 [40718374864](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40718374864)의 실제 job 로그에서 OKX API 수집 결과 JSON, `PASS: OKX OI verified`, `git push origin HEAD:main` 성공을 확인했습니다. 원시 HTTP 상태 코드 숫자는 로그에서 별도로 확인하지 못했으므로 HTTP 200 직접 관측으로 표현하지 않습니다.
- 서로 다른 Actions bot 저장 커밋의 고정 JSON 3건을 대조했습니다. **00:30:57.904 KST 631495.928 ETH** ([43306fb](https://github.com/changwookseo/eth-cvd-monitor/commit/43306fb747c44faeae53fd4bafaa9e2d1f6c5c59)), **00:35:41.566 KST 630198.863 ETH** ([01bcaed](https://github.com/changwookseo/eth-cvd-monitor/commit/01bcaede015c4da2bb5a739b10b2da3aa8b9d39f)), **00:40:47.880 KST 630724.470 ETH** ([3e8a779](https://github.com/changwookseo/eth-cvd-monitor/commit/3e8a7792d9815e212943d1b394229086bba304e0)). 최신 main JSON blob SHA `7f1785e3416135654ec3acacfd2f73b9cfa966ed`, `status=VERIFIED`, `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `unit=ETH`입니다. **OKX 단일 거래소 OI**이며 Binance OI나 전체 시장 OI가 아닙니다.
- `.github/workflows/eth-oi-okx.yml`에는 `schedule: 2-59/5 * * * *`와 `workflow_run`이 계속 설정되어 있습니다. 현재 확인된 성공은 외부 Binance Spot CVD 완료에 연동된 **자동 실행**이지 OKX 자체 **독립 schedule 예약 실행 성공**이 아닙니다. 일부 skipped가 있으므로 매 5분 무결점이라고 주장하지 않습니다.
- 이전 23:05 KST 체크포인트의 **22:07 KST 완성 ETH ESI 2.0 보고서에 OKX OI 실측값과 당시 GitHub JSON이 일치했다는 검증**은 유지합니다. 이번 점검에서 새 보고서 출력은 생성·검증하지 않았으며 00:40의 새 값이 보고서에 출력됐다고 주장하지 않습니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 미등록으로 취급합니다. 자격증명 조회·우회·노출·재발급·등록 시도 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치(20/15/18/20/12/10/5)·180일 백데이터 및 OI 수집 코드/워크플로는 수정하지 않았습니다.
- **판정: OKX OI 실수집 → `workflow_run` 자동 연속 갱신 → JSON 저장 → 과거 완성 보고서 실측 반영은 검증. 독립 `schedule` 성공은 미검증 → OI 전체 게이트 미통과. 펀딩비·선물 CVD 미착수. 전체 복구 완료 알림 금지.**


## 자동 복구 점검 — 2026-10-29 02:07 KST 이후 (2026-10-28 17:07 UTC 이후)

- 직전 2026-10-29 00:42 KST 체크포인트를 먼저 읽고 OKX OI 게이트를 재검증했습니다. **새로운 핵심 증거:** [OKX OI Actions #40727280108](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40727280108)는 `event=schedule`, `conclusion=success`, 시작 `2026-10-28T16:34:23Z` (01:34:23 KST)로 **독립 GitHub 예약 실행이 실제 성공**했습니다. 이 워크플로의 job #122953824955에서 공개 OKX API 수집, 신선도 검증, JSON 커밋이 모두 success입니다. 로그의 관측값은 `2026-10-28T16:34:32.444Z`, `630847.565 ETH`이며 `PASS: OKX OI verified`, GitHub bot commit `af353d0`, `HEAD -> main` push까지 확인했습니다. 단일 거래소 `OKX ETH-USDT-SWAP` OI이며 Binance/시장 전체 OI가 아닙니다.
- 추가로 [OKX OI #40731596780](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40731596780)은 `event=workflow_run`, success이며 `2026-10-28T17:01:05.384Z` (02:01:05.384 KST) **625449.205 ETH**를 API에서 수집·검증하고 JSON을 main에 push했습니다(commit `3d2a2f9`). 서로 다른 자동 트리거와 시각의 JSON 갱신이 검증됩니다. 일부 workflow_run은 skipped였으므로 정확한 5분 무결점 갱신은 주장하지 않습니다.
- 기존 2026-10-28 22:07 KST ETH ESI 2.0 **완성 보고서 5번 항목**에 표시된 `OKX 630332.863 ETH, 관측 22:05:44 KST`가 당시 고정 JSON과 정확히 일치했다는 검증은 유지합니다. 새 02시대 보고서를 생성했다고 주장하지 않습니다.
- **OKX OI 범위의 전체 게이트 통과:** 공개 API 실측 → 검증 → GitHub JSON 저장 → 독립 `schedule` 성공 및 반복 `workflow_run` 갱신 → 실제 완성 보고서 출력 일치가 모두 확인됐습니다. 이것은 OKX 단일 거래소 OI의 수집 파이프라인 통과이며 **Binance OI 복구나 시장 전체 OI 수집 완료를 의미하지 않습니다.**
- 순차 원칙에 따라 이제 **펀딩비 단계만 착수**했습니다. 기존 Binance 180일 파생 아카이브·진단 파일을 검토했으나 현재 Binance REST 펀딩 API HTTP 451 및 아카이브 공백을 실시간 펀딩으로 둔갑시키지 않았습니다. 새 독립 OKX 공개 API 수집기 `eth_funding_okx_live.py`(commit `cbee4d2`)와 워크플로 `.github/workflows/eth-funding-okx.yml`(commit `d108d2e`)을 추가했습니다. 기존 현물 CVD·기술지표·정본·7지표 가중치(20/15/18/20/12/10/5)·180일 백데이터는 변경하지 않았습니다.
- [Funding 첫 실제 push 실행 #40732490344](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40732490344)의 API 수집, 검증, JSON 저장 작업이 모두 success였습니다. [저장 commit 537e9da](https://github.com/changwookseo/eth-cvd-monitor/commit/537e9da)의 `eth_funding_okx_latest.json`에서 `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `status=VERIFIED`, `observed_at_utc=2026-10-28T17:06:06.591Z`, `fetched_at_utc=2026-10-28T17:06:30.924859Z`, **현재 기간 예상 펀딩비 0.00759496207693%**, 정산 예정 `2026-10-29T00:00:00Z`(09:00 KST), 별도 직전 정산값 `0.0000719253722218` (decimal)을 확인했습니다. **OKX의 현재 기간 예상치**이며 확정 정산값, Binance 펀딩비, 시장 전체 펀딩비 또는 8시간 정규화 수치가 아닙니다. 원시 HTTP 상태코드 숫자는 로그에서 별도 확인하지 않았으나 실제 응답 파싱과 API 수집 성공·JSON push는 확인했습니다.
- 두 번째 funding push 실행 [#40732597561](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40732597561)도 API 수집·검증·JSON 저장 단계 success입니다. 이때 `fetched_at_utc=2026-10-28T17:07:14.698217Z`로 변경됐으나 `observed_at_utc`와 예상 펀딩비는 원천 OKX에서 동일하게 반환되어 **독립적인 새 관측값으로 과장하지 않습니다**.
- 첫 실수집 성공 후에만 funding 워크플로에 `schedule: 4-59/5 * * * *` 및 기존 Binance Spot CVD 성공에 연동되는 `workflow_run` 보조 트리거를 추가했습니다([commit 5a229d5](https://github.com/changwookseo/eth-cvd-monitor/commit/5a229d5150c8c5a252440c87ba8cd3fd63f3560f)). **펀딩비의 실제 예약 실행·자동 연속 갱신은 아직 미검증**입니다. 독립 예약 실행 성공이 아닌 push 실행을 schedule 성공으로 표기하지 않습니다.
- 보고서 정본은 수정하지 않고 `docs/ETH_ESI_2_0_REPORT_CALL_RULES.md`의 기존 2-1 OI 규칙 뒤에 2-2 OKX 펀딩비 조회·신선도·예상/정산 구분 지침만 추가했습니다([commit 9811c6f](https://github.com/changwookseo/eth-cvd-monitor/commit/9811c6f4b18d251d6b9688c441e5d81b3d42d584)). **실제 완성 보고서에 펀딩비가 반영됐다는 증거는 아직 없으며** 문서 지침만으로 보고서 반영 완료라고 판정하지 않습니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 미등록으로 취급하고 우회·조회·노출·재발급·등록하지 않았습니다.
- **판정: OKX OI 범위 게이트 통과 / 펀딩비 실수집·JSON 저장 성공, 자동 반복·실제 보고서 출력 미검증 / 선물 CVD 미착수 / 전체 복구 미완료. 완료 알림 금지.** 다음 실행에서는 펀딩비 자체 schedule 또는 workflow_run 자동 실행과 서로 다른 관측시각의 연속 JSON 갱신을 먼저 검증하고, 실제 ETH ESI 2.0 완성 보고서 출력 반영을 확인한 뒤에만 선물 CVD 단계로 넘어갑니다.

### 추가 검증 — 2026-10-29 02:11 KST

- Funding 워크플로의 첫 자동 `workflow_run` [#40733182668](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40733182668)은 02:10:39 KST에 생성됐지만 `skipped`입니다. 부모 Binance Spot CVD [#40733124401](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40733124401)이 실패했기 때문에 성공 부모 조건이 충족되지 않았습니다. **이를 funding 자동 수집 성공으로 세지 않습니다.**
- Binance Spot CVD 부모의 실패는 이번 로그상 API 수집이 아니라 `Save Binance CVD` 단계의 GitHub push 충돌입니다. 로그: `cannot lock ref 'refs/heads/main': is at a13f74b... but expected 970ea2f...`, `failed to push some refs`. 문서 수정 등 동시 커밋과의 경쟁 상태이며 API 장애로 단정하지 않습니다. 기존 Binance 현물 CVD 수집 코드/워크플로는 변경하지 않았습니다.
- Funding 자체 `event=schedule` 성공과 실제 연속 관측값 갱신은 여전히 미검증입니다. OI schedule 실증과 혼동하지 않습니다. 다음 주기에서 다시 확인합니다. 전체 복구 완료 알림 금지.


## 자동 복구 점검 — 2026-10-29 02:27 KST (2026-10-28 17:27 UTC)

- 최신 상태 문서를 먼저 읽고 OI → 펀딩비 순서를 유지했습니다. 이전 체크포인트에서 OKX OI 단일 거래소 게이트(실제 API·독립 schedule 성공·연속 저장·22:07 KST 완성 보고서 실측 일치)는 통과한 것으로 검증됐습니다. 이번 조회의 main OI JSON은 `observed_at_utc=2026-10-28T17:15:49.274Z`(02:15:49 KST), `624996.633 ETH`, `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `status=VERIFIED`였습니다. 이는 OKX 단일 거래소 OI이며 Binance 또는 시장 전체 OI가 아닙니다. 이번 시각의 5분 무결점 OI 연속 갱신을 새로 입증한 것은 아닙니다.
- 펀딩비는 `eth_funding_okx_latest.json`을 main과 4개 고정 커밋에서 직접 읽었습니다. 첫 수집 [537e9da](https://github.com/changwookseo/eth-cvd-monitor/commit/537e9da3c48582b20822ee72f45474634ca44f1c): 02:06:06.591 KST 관측, 예상 `+0.00759496207693%`. 두 번째 [351b03a](https://github.com/changwookseo/eth-cvd-monitor/commit/351b03aad8a2670fbb38f6cc06d63dc9cbc38074)는 02:07:14 KST 재수집이지만 원천 관측시각과 값이 같으므로 새 관측으로 세지 않습니다. [966e1a8](https://github.com/changwookseo/eth-cvd-monitor/commit/966e1a89caa67bd39749400baaee070b3adc9809)는 **02:15:27.648 KST 관측, +0.00754106371927%**, [91db01e](https://github.com/changwookseo/eth-cvd-monitor/commit/91db01e700799d7de451ff12e3e82b386a19b9b4)는 **02:25:20.644 KST 관측, +0.00765373056548%**로, 서로 다른 실제 원천 관측시각과 값의 갱신을 확인했습니다. 마지막 fetch는 02:25:49.847 KST입니다. 모두 `exchange=OKX`, `symbol=ETH-USDT-SWAP`, `status=VERIFIED`, `rate_type=indicative_current_period_not_realized`이며 **OKX 현재 기간 예상 펀딩비**입니다. 확정 정산값, Binance 또는 전체 시장 펀딩비가 아닙니다.
- 위 02:15·02:25 두 커밋의 GitHub 메타데이터를 별도 조회해 **github-actions[bot] 작성·커밋** 및 변경 파일이 `eth_funding_okx_latest.json` 하나뿐임을 확인했습니다. 수집 워크플로에는 `schedule: 4-59/5 * * * *`와 성공한 Binance Spot CVD에 연동된 `workflow_run`이 설정돼 있습니다. 그러나 이번 실행 환경의 GitHub 커넥터는 해당 신규 실행들의 이벤트 종류 및 jobs 로그를 직접 열람할 수 있는 **실행 목록 조회 기능이 없어**, 이 두 새 커밋이 각각 독립 `schedule`인지 `workflow_run`인지 확정하지 않습니다. GitHub 봇의 서로 다른 시각 자동 JSON 저장은 확인되지만, **펀딩비 자체 schedule 성공은 미검증**으로 남깁니다. 앞서 첫 push 실행 [#40732490344](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40732490344)의 실제 API·검증·저장 성공은 이전 체크포인트에서 이미 확인했습니다.
- 보고서 호출 규칙의 `2-2`에 OKX 예상 펀딩비 반영 지침은 존재하지만, **완성된 ETH ESI 2.0 보고서 출력에 새 펀딩비 수치가 실제 표시됐다는 실행 증거는 아직 없습니다.** 규칙 저장만으로 보고서 반영 완료라고 판정하지 않습니다. 펀딩비 전체 게이트 미통과이므로 **선물 CVD 미착수**를 유지합니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 이전 체크포인트대로 미등록으로 취급하고 조회·우회·노출·등록·재발급을 시도하지 않았습니다. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치(20/15/18/20/12/10/5)·180일 백데이터 및 수집기·워크플로 코드는 변경하지 않았습니다. **전체 복구 미완료, 완료 알림 금지.** 다음에는 funding Actions의 실제 `schedule` 이벤트·로그를 확인하고 완성 보고서의 펀딩비 실측 출력 일치를 검증한 후에만 선물 CVD로 진행합니다.


## 자동 복구 점검 — 2026-10-29 03:24 KST (2026-10-28 18:24 UTC)

- 먼저 직전 02:27 KST 체크포인트를 확인했습니다. OKX OI 단일 거래소 게이트는 이전 독립 `schedule` 성공([#40727280108](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40727280108)), 반복 자동 JSON 갱신, 22:07 KST 완성 보고서 OI 실측 일치로 이미 통과한 범위입니다. **Binance OI 또는 시장 전체 OI가 아닙니다.** 이번에는 이후 발견된 저장 경쟁으로 인한 OI 연속성 저하부터 점검·최소 수정했습니다.
- Actions 실제 실행·잡·로그 재조회: [OI #40744224870](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40744224870) (03:20 KST)과 [#40743449306](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40743449306) (03:15 KST)은 API 수집 및 신선도 검증 단계는 success였지만 **GitHub push 단계가 failure**였습니다. #40744224870 로그에는 `cannot lock ref 'refs/heads/main'`(원격 head가 갱신됨) 오류가 명시되어 있습니다. API 장애가 아닌 다른 수집기와의 동시 main 쓰기 경쟁입니다. 이전 성공 [OI #40741881193](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40741881193)은 03:05 KST 관측값을 저장했습니다.
- `.github/workflows/eth-oi-okx.yml`의 **JSON commit/push 단계만** 원격 main fetch→rebase→push를 최대 8회 재시도하도록 수정했습니다([커밋 8336e70](https://github.com/changwookseo/eth-cvd-monitor/commit/8336e70080396cf6db39473e022ef8d8488dfdc6)). 기존 API·검증·cron·트리거·다른 수집기·보고서 정본은 변경하지 않았습니다. 수정으로 발생한 [OI push 실행 #40744576765](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40744576765)은 **전체 success**, API 수집·검증·JSON 저장 잡 단계도 success입니다. 저장 JSON `observed_at_utc=2026-10-28T18:23:03.836Z` (03:23:03.836 KST), `value=618073.880 ETH`, `status=VERIFIED`, `exchange=OKX`, `symbol=ETH-USDT-SWAP`를 재조회했습니다. 이는 수정 후 **1회 성공**이며 장기 무결점 반복 성공을 뜻하지 않습니다.
- 펀딩비는 기존 자동 `workflow_run`에서 [#40744224929](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40744224929) (03:20 KST) success였고 원천 관측 `2026-10-28T18:20:19.136Z`, 예상 펀딩비 **+0.00859605666033%**를 JSON에 저장했습니다. 반면 [#40741881371](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40741881371)에서는 API·검증 success 뒤 `git push`가 경합으로 실패했습니다. 이에 `.github/workflows/eth-funding-okx.yml`의 **JSON push 단계만** 동일한 제한적 재시도를 추가했습니다([커밋 d59e2b2](https://github.com/changwookseo/eth-cvd-monitor/commit/d59e2b2109af63ae3a301cb09f22a08bdbf7a26d)). 수정 후 [Funding push 실행 #40744634537](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40744634537)은 **전체 success**. 최신 저장 JSON `observed_at_utc=2026-10-28T18:23:21.646Z` (03:23:21.646 KST), **+0.00876561583728%**, `rate_type=indicative_current_period_not_realized`, `status=VERIFIED`. 이는 **OKX ETH-USDT-SWAP 현재 기간 예상 펀딩비**로 Binance/시장 전체 또는 확정 정산값이 아닙니다.
- Actions REST `event=schedule` 필터로 저장소 전체의 21개 예약 실행을 재조회했습니다. **OKX OI 독립 schedule 성공 2건**([#40727280108](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40727280108), [#40668318853](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/40668318853))은 확인되나 **Funding 자체 독립 `schedule` 성공은 0건**입니다. Funding의 `workflow_run` 반복 수집·서로 다른 원천 관측값 저장은 확인되지만 독립 예약 트리거 성공을 혼동하지 않습니다. 5분 무결점 갱신은 보장하지 않습니다.
- Funding의 최신 예상값이 **ETH ESI 2.0 완성 보고서 출력에 실제로 표시되고 해당 시각의 JSON과 일치한다는 증거는 아직 없습니다**. 규칙 문서의 2-2 추가만으로 출력 반영을 완료 처리하지 않습니다. 따라서 **펀딩비 전체 게이트 미통과 → 선물 CVD 미착수 → 전체 복구 미완료 / 완료 알림 금지**입니다. 다음에는 Funding 독립 schedule 성공 및 실제 완성 보고서 반영을 검증합니다.
- Binance Cron importer의 `CRONJOB_API_KEY` Secret은 미등록으로 유지하며 조회·우회·노출·재발급·등록 시도를 하지 않았습니다. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치(20/15/18/20/12/10/5)·180일 백데이터는 변경하지 않았습니다.
