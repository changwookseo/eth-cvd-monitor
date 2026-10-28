# ETH ESI 2.0 recovery verification — 2026-10-28 KST

Overall: RECOVERY RESUMED, NOT COMPLETE. Independent OKX OI live collection has passed its first GitHub Actions run; repeated scheduled refresh and actual report output remain unverified. Binance Cron Secret registration remains pending. Historical pause checkpoint is preserved below.

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
