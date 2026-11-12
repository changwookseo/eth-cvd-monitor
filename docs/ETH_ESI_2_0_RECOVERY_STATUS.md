## 자동 복구 점검 — 2026-11-13 07:47 KST
- 직전 06:18 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 검증. main의 `.github/workflows/eth-oi-okx.yml`에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존함을 확인.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 663635.226 ETH**, 거래소 관측 `2026-11-12T22:45:54.198Z` (07:45:54.198 KST), 수집 `22:45:54.252066Z`, 내부 `status=VERIFIED`. Binance 또는 시장 전체 OI가 아님. 06:15 관측 이후 갱신.
- [#43322104330](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43322104330) (22:40:42 UTC), [#43322859084](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43322859084) (22:45:39 UTC)는 모두 **보조 `workflow_run` success**. 각각 jobs API에서 API 수집·출력 신선도 검사·JSON 커밋 단계 success 확인. 독립 `schedule`의 인접 2회 연속 성공으로 인정하지 않음.
- 이번 회차 별도 OKX 원시 HTTP 본문 교차검증, job 원문 stdout↔저장 JSON SHA 직접 대조, 완성 보고서의 실측 OI 반영은 미검증. 저장 JSON과 job 단계 성공만으로 전체 OI 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 06:18 KST
- 최신 05:13 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`와 `.github/workflows/eth-oi-okx.yml` 직접 재확인: OKX public API code=0, ETH-USDT-SWAP 단일 행, oi/oiCcy/oiUsd, 거래소 관측시각, 300초 신선도 검증; 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 668744.491 ETH**, 관측 `2026-11-12T21:15:47.283Z` (06:15:47.283 KST), 수집 `21:15:47.376527Z`, 내부 `status=VERIFIED`. 05:10 관측 이후 갱신. Binance OI 또는 시장 전체 OI 아님.
- Actions 전체 최근 실행 조회: [#43307638256](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43307638256) (21:10:44 UTC), [#43308481756](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43308481756) (21:15:41 UTC) 모두 `workflow_run` success. 보조 실행 연속 성공은 독립 schedule 연속 성공으로 인정하지 않음.
- Actions `event=schedule` 최근 50건 조회: 가장 최근 OKX 독립 schedule 성공은 [#43293980765](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43293980765) (19:48:48 UTC), 이전 OKX schedule 성공은 #43213235886 (11:54:59 UTC). **인접 독립 schedule 2회 연속 성공 미입증**. 이는 조회된 범위의 관찰이며 모든 과거 실행의 부재를 단정하지 않음.
- 이번 회차에는 별도 OKX 원시 HTTP 응답 직접 대조, 최신 job stdout↔저장 JSON SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영 검증이 이뤄지지 않음. collector 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과. 펀딩비·선물 CVD 미진입, 전체 복구 미완료, 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 05:13 KST
- 직전 04:54 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`와 `.github/workflows/eth-oi-okx.yml`을 재확인. API `code=0`, ETH-USDT-SWAP 단일 행, `oi`/`oiCcy`/`oiUsd`, 거래소 관측시각 및 300초 신선도 검증 로직과 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 구성 유지.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 669070.525 ETH**, 관측 `2026-11-12T20:10:54.520Z` (05:10:54.520 KST), 수집 `20:10:54.573120Z`, `status=VERIFIED`. 직전 04:50 관측 이후 갱신. Binance 또는 시장 전체 OI가 아님.
- GitHub Actions 최신 전체 실행 목록 및 개별 run 상세에서 [#43296809004](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43296809004) (20:05:36 UTC), [#43297673857](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43297673857) (20:10:45 UTC)의 `ETH OKX Live OI` 실행이 모두 **`workflow_run` success**임을 확인. 인접 5분 구간의 성공은 보조 실행이며 독립 `schedule` 2회 연속 성공으로 인정할 수 없음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 job stdout↔저장 JSON SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 이번 회차에 검증되지 않음. `VERIFIED`는 collector 내부 검증이며 전체 게이트 통과를 의미하지 않음.
- **OI 전체 게이트 미통과. 펀딩비·선물 CVD 복구 단계 미진입, 전체 복구 미완료, 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 04:54 KST
- 최신 03:43 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`는 OKX public API 응답의 `code=0`, 단일 `ETH-USDT-SWAP` 행, `oi`·`oiCcy`·`oiUsd`, 거래소 타임스탬프와 300초 신선도를 검사함. `.github/workflows/eth-oi-okx.yml`은 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run`을 정의함.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 668636.490 ETH**, 관측 `2026-11-12T19:50:49.704Z` (04:50:49.704 KST), 수집 `19:50:49.784791Z`, `status=VERIFIED`. Binance OI나 전체 시장 OI가 아님. 직전 03:40 KST 대비 관측시각 진전.
- GitHub Actions 전체 실행 목록에서 **독립 `schedule` 실행 [#43293980765](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43293980765)** (19:48:48 UTC, success)와 보조 `workflow_run` [#43294301966](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43294301966) (19:50:43 UTC, success) 확인. 최근 조회된 OKX 전용 실행에는 독립 schedule 성공 1건만 확인되어 **인접 독립 schedule 2회 연속 성공은 미입증**. 전체 실행 목록의 최근 구간만 조회했으므로 과거 전체 실행 부재를 의미하지 않음.
- OI 파일 저장 커밋 [516743c](https://github.com/changwookseo/eth-cvd-monitor/commit/516743c0fb5652de0edecd3608676c496ba52bcb) (19:45:46 UTC), [eab494c](https://github.com/changwookseo/eth-cvd-monitor/commit/eab494c06a9d0f1539ee451611a931183f2389fb) (19:48:56 UTC), [8d51539](https://github.com/changwookseo/eth-cvd-monitor/commit/8d515397edbcb419a6212bef96b8a4d5d4c1934f) (19:50:50 UTC) 확인. 최신 커밋의 JSON diff와 main JSON의 관측시각·OI가 일치. 연속 저장은 확인되나 실행 원문 로그와 저장 SHA의 이번 회차 직접 대조는 미수행.
- 미검증: 독립 schedule 인접 2회 연속 성공, 별도 OKX 원시 HTTP 응답 직접 대조, 최신 job stdout↔저장 SHA 직접 대조, **실제로 생성된 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영**. 보고서 호출 규칙의 OKX 보조 원천 참조 지침만 확인했으며 보고서 실측 반영 성공으로 간주하지 않음.
- **OI 전체 게이트 미통과. 펀딩비·선물 CVD 미진입, 전체 복구 미완료, 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 상태 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 03:43 KST
- 직전 02:14 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. `eth_oi_okx_live.py`는 OKX public API `ETH-USDT-SWAP`의 `oiCcy`(ETH), `oi`(계약), `oiUsd`와 거래소 타임스탬프를 검증하고 300초 신선도 제한을 적용. 워크플로는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`을 함께 정의함.
- main `eth_oi_okx_latest.json` 실측: **OKX ETH-USDT-SWAP 단일 거래소 OI 676609.442 ETH**, 관측 `2026-11-12T18:40:49.426Z` (03:40:49.426 KST), 수집 `18:40:49.505023Z`, `status=VERIFIED`. Binance OI 또는 전체 시장 OI가 아님. 직전 체크포인트 02:10:52.512 KST보다 관측시각이 진전됨.
- GitHub 커넥터에서 최신 OI 파일과 워크플로 본문을 읽고, OI 저장 커밋 [c9e8c96](https://github.com/changwookseo/eth-cvd-monitor/commit/c9e8c96b502a96651533c5418be245b496efdecf) 및 [687aa5d](https://github.com/changwookseo/eth-cvd-monitor/commit/687aa5dc3e699dfc16067ed8521adcbdb93cd357)의 존재 및 OI JSON 파일 변경을 확인. 다만 이번 점검에서는 최신 개별 실행의 event 종류·성공 여부·job 원문을 조회하지 못했으므로 두 커밋을 독립 예약 실행 2회 성공의 증거로 간주하지 않음.
- **미검증 게이트:** 인접한 독립 `schedule` 2회 연속 성공, 별도 OKX 원시 HTTP 응답 대조, 최신 실행 로그↔저장 JSON SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영. 내부 `VERIFIED`만으로 전체 게이트를 통과시키지 않음.
- **OI 전체 게이트 미통과. 펀딩비·선물 CVD 미진입, 전체 복구 미완료, 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 02:14 KST
- 최신 체크포인트(01:14 KST)를 먼저 읽고 OKX OI 선행 게이트 재검증. `eth_oi_okx_live.py`의 OKX public open-interest API, 300초 신선도 검사, `.github/workflows/eth-oi-okx.yml`의 `schedule: 2-59/5 * * * *` 및 `workflow_run` 구성 확인. 실제 최근 두 실행은 독립 `schedule`이 아닌 `workflow_run`.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 682972.325 ETH**, 관측 `2026-11-12T17:10:52.512Z` (02:10:52.512 KST), 수집 `17:10:52.593491Z`, `status=VERIFIED`. Binance OI 또는 전체 시장 OI가 아님.
- [#43265743724](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43265743724) (17:05 UTC)와 [#43266642603](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43266642603) (17:10 UTC)는 모두 `workflow_run` success. jobs API의 API 수집·신선도·JSON 저장 단계 성공과 **원문 job 로그**를 확인. 로그에 출력된 JSON의 관측시각·OI·USD·수집시각·필드가 각각 저장 커밋 [0b7b1e7](https://github.com/changwookseo/eth-cvd-monitor/commit/0b7b1e7) 및 [59cf942](https://github.com/changwookseo/eth-cvd-monitor/commit/59cf942)의 `eth_oi_okx_latest.json` 내용과 일치함을 직접 대조. 5분 간격 연속 갱신 및 실행 출력↔저장 파일 대조 검증 진척.
- 독립 `schedule` 인접 2회 연속 성공은 미확인. 별도 실행환경에서 OKX API 원시 HTTP 직접 호출은 DNS 해석 오류로 실패해 독립 응답 교차검증 미완료. `docs/ETH_ESI_2_0_REPORT_CALL_RULES.md`의 OKX OI 단일 거래소 실측 참조 규칙은 확인했지만 **실제로 생성된 완성 보고서의 최신 OI 반영은 검증하지 못함**. 원문 job 로그는 collector가 출력한 파싱 결과이며 별도 원시 HTTP 응답 본문 자체는 아님.
- **OI 전체 게이트 미통과. 펀딩비 및 선물 CVD 복구 단계로 넘어가지 않음. 전체 복구 미완료, 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 상태 유지, 우회·노출·수정 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.



## 자동 복구 점검 — 2026-11-13 01:14 KST
- 최신 체크포인트(2026-11-13 00:21 KST) 확인 후 OI 선행 게이트만 재검증. main의 OKX 전용 워크플로 `.github/workflows/eth-oi-okx.yml`에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존함을 확인.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 681220.455 ETH**, 관측 `2026-11-12T16:11:01.816Z` (2026-11-13 01:11:01.816 KST), 수집 `16:11:01.891253Z`, 내부 `status=VERIFIED`. Binance OI 또는 시장 전체 OI 아님.
- 보조 `workflow_run` [#43254892803](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43254892803) (16:05:43 UTC) 및 [#43255825527](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43255825527) (16:10:53 UTC) 모두 success. 각 실행의 API 수집, 출력·신선도 검증, JSON 저장 단계 success를 jobs API로 직접 확인. 연속 저장 커밋 [555e711](https://github.com/changwookseo/eth-cvd-monitor/commit/555e711ddf52c01eada2d0e9e19e2b4a00062600) (16:05:55 UTC), [a88531d](https://github.com/changwookseo/eth-cvd-monitor/commit/a88531d4a829aa60d715863bb08bd657b92ae7b0) (16:11:11 UTC) 확인. 이는 독립 schedule 연속 성공 증거가 아님.
- 여전히 미검증: 독립 `schedule` 인접 2회 성공, 외부 OKX 원시 HTTP 응답 직접 대조, 실행 stdout ↔ 저장 JSON SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영. JSON 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 순차 복구 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.
