## 자동 복구 점검 — 2026-11-20 03:45 KST
- 최신 02:44 KST 체크포인트를 먼저 읽고 OI만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. OKX 공개 API `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 거래소 관측시각·300초 신선도 검증 코드 확인. 워크플로에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 683266.807 ETH**, 거래소 관측 `2026-11-19T18:41:09.073Z` (03:41:09.073 KST), 수집 `18:41:09.163368Z`, blob SHA `b45f9cfc1b3f21f501860d66e1d1ddedf902a1e5`. 직전 02:40:58 KST 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- Actions 최신 목록에서 독립 `schedule` 성공 [#44589494460](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44589494460) (18:35:53 UTC) **1건 확인**. 인접 독립 schedule 2회 연속 성공은 미입증. 보조 `workflow_run` [#44590372674](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44590372674) (18:40:53 UTC) 및 [#44589464634](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44589464634) (18:35:42 UTC) success. 18:45:48 UTC 보조 실행 #44591225584는 조회 당시 결론 미확정.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 `VERIFIED`는 전체 게이트 통과 증거가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-20 02:44 KST
- 최신 01:17 KST 체크포인트를 먼저 확인한 뒤 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`는 OKX 공개 API `ETH-USDT-SWAP` 단일 종목 `oiCcy`(ETH), 응답 `code=0`, 거래소 시각과 300초 신선도 검사를 수행함. `.github/workflows/eth-oi-okx.yml`에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main `eth_oi_okx_latest.json`: **OKX 단일 거래소 ETH-USDT-SWAP OI 690236.480 ETH**, 관측 `2026-11-19T17:40:58.147Z` (02:40:58.147 KST), 수집 `17:40:58.230412Z`, 내부 `status=VERIFIED`. 이전 01:15:59 KST보다 관측시각 진전. Binance OI나 시장 전체 OI 아님.
- Actions 최근 목록의 OKX [#44579773166](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44579773166) (17:40:51 UTC), [#44578870203](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44578870203) (17:35:45 UTC) 및 [#44577991218](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44577991218) (17:30:56 UTC)는 모두 `workflow_run` success. 이는 보조 실행의 연속 성공이지 독립 `schedule` 5분 간격 2회 연속 성공 증거가 아님.
- 별도 OKX 원시 HTTP 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서에 최신 OI 실측 반영은 미검증. JSON의 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-20 01:17 KST
- 직전 00:22 KST 체크포인트를 먼저 확인한 뒤 OI 선행 게이트를 재점검. `eth_oi_okx_live.py`의 OKX 공개 API 단일 `ETH-USDT-SWAP` `oiCcy`(ETH), 응답 `code=0`, 거래소 관측시각 및 300초 신선도 검증 코드 확인. `.github/workflows/eth-oi-okx.yml`의 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존 확인.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 711483.076 ETH**, 거래소 관측 `2026-11-19T16:15:59.308Z` (2026-11-20 01:15:59.308 KST), 수집 `16:15:59.392022Z`, 내부 `status=VERIFIED`. 직전 00:20:59 KST 관측 이후 갱신. Binance OI나 시장 전체 OI 아님.
- Actions 전체 최신 목록의 OKX OI [#44564086703](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44564086703) (16:15:48 UTC), [#44563147948](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44563147948) (16:10:49 UTC), [#44562195831](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44562195831) (16:05:46 UTC) 모두 `workflow_run` success. 약 5분 간격 보조 실행은 확인되나 **독립 schedule 2회 연속 성공은 미입증**. 별도로 펀딩 및 선물 CVD 후보 워크플로의 실행 흔적도 목록에 존재하지만 OI 전체 게이트 통과 또는 해당 지표의 보고서 실측 복구 완료 증거로 인정하지 않으며 이 단계에서는 수정·승격하지 않음.
- 별도 OKX 원시 HTTP 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED만으로 OI 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 순차 복구 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-20 00:22 KST
- 직전 2026-11-19 23:26 KST 체크포인트를 먼저 읽고 OI 전체 게이트만 재검증. main 수집기 `eth_oi_okx_live.py`는 OKX 공개 API `ETH-USDT-SWAP` 단일 행의 `oiCcy`(ETH), `code=0`, 거래소 관측시각 및 300초 신선도를 검증. 워크플로 `.github/workflows/eth-oi-okx.yml`에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 716554.594 ETH**, 관측 `2026-11-19T15:20:59.557000+00:00` (2026-11-20 00:20:59.557 KST), 수집 `2026-11-19T15:20:59.674062+00:00`, 내부 `status=VERIFIED`, blob SHA `1b1dda805bdd46c47f1e79b74b870c3cc91df9ee`. 이전 23:25 KST 관측보다 갱신. Binance OI나 전체 시장 OI가 아님.
- Actions 전체 최신 실행 목록: [#44553754152](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44553754152) (15:20:52 UTC) 및 [#44552799083](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44552799083) (15:15:48 UTC) 모두 OKX OI **보조 `workflow_run` success**. 이 둘은 독립 `schedule` 5분 간격 2회 연속 성공 증거가 아님. 이번 조회의 최신 실행 목록에는 인접 독립 예약 성공 2회가 확인되지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 이번 실행 원문 로그↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. 수집기 내부 VERIFIED만으로 OI 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 23:26 KST
- 최신 22:18 KST 체크포인트를 먼저 확인하고 OI 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. 수집 코드는 OKX 공개 API `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 거래소 관측시각 및 300초 신선도 검증을 유지. 워크플로는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`을 병행.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 718831.707 ETH**, 거래소 관측 `2026-11-19T14:25:42.797Z` (23:25:42.797 KST), 수집 `14:25:42.901974Z`, 내부 `status=VERIFIED`, blob SHA `e8c20b3fec67f59b53616bb16c583e00b5b39462`. 직전 22:15 관측 이후 갱신. Binance OI 또는 시장 전체 OI가 아님.
- 최신 OKX Actions [#44543605137](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44543605137) (14:25:35 UTC), [#44542716069](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44542716069) (14:20:44 UTC) 모두 `workflow_run` success. 5분 부근 연속 보조 실행 성공 및 최신 JSON 갱신을 확인했으나, 이것은 독립 예약 성공 2회가 아님.
- 최근 전체 `event=schedule` 목록에서 최신 OKX 독립 예약 성공은 [#44496406941](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44496406941) (09:26:18 UTC), 이전 [#44437128461](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44437128461) (01:28:12 UTC). **독립 `schedule` 5분 간격 인접 2회 성공 미입증**. 다른 워크플로의 예약 성공과 구분함.
- 이번 회차 별도 OKX 원시 HTTP 응답 본문 교차검증, 최신 job 로그↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED만으로 OI 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 22:18 KST
- 직전 21:20 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py` 및 `.github/workflows/eth-oi-okx.yml` 확인: OKX 공개 API ETH-USDT-SWAP 단일 거래소 `oiCcy`(ETH), `code=0`, 300초 신선도 검증, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 716944.253 ETH**, 거래소 관측 `2026-11-19T13:15:52.192000+00:00` (22:15:52.192 KST), 수집 `2026-11-19T13:15:52.288391+00:00`, 내부 `status=VERIFIED`, blob SHA `72a7c987a75db87d64299b96a5b1aae82dd7e9b3`. 직전 21:15 관측보다 갱신. Binance OI 또는 전체 시장 OI가 아님.
- GitHub Actions 전체 `event=schedule` 최신 목록에서 OKX 독립 예약 성공 [#44496406941](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44496406941) (09:26:18 UTC), 그 이전 [#44437128461](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44437128461) (01:28:12 UTC). 인접한 독립 예약 5분 간격 2회 연속 성공은 여전히 미입증. 다른 워크플로의 예약 성공 및 보조 workflow_run 성공을 독립 OKX 예약으로 혼동하지 않음.
- 이번 점검은 수집 코드·워크플로·저장 JSON 및 Actions 예약 목록 직접 확인에 한정. 별도 OKX 원시 HTTP 응답 대조, 최신 실행 원문 로그↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서 최신 OI 실측 반영은 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 21:20 KST
- 최신 21:12 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`은 OKX 공개 API ETH-USDT-SWAP 단일 거래소 `oiCcy`(ETH), `code=0`, 거래소 관측시각·300초 신선도 검사를 유지. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 717645.027 ETH**, 관측 `2026-11-19T12:15:50.502Z` (21:15:50.502 KST), 수집 `12:15:50.562981Z`, 내부 `status=VERIFIED`, blob SHA `5c05ef25b860d8cac28e8fb4808bebf346b6de2f`. 직전 21:10 관측 이후 갱신; Binance OI 또는 전체 시장 OI가 아님.
- 보조 `workflow_run` [#44522232299](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44522232299) (12:15:42 UTC)와 [#44521474357](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44521474357) (12:10:47 UTC) 모두 success. 최신 실행 job #135553504952의 API 수집·신선도 검사·JSON 커밋 단계 success 및 원문 로그의 OI/관측·수집시각과 main JSON 값 일치, `STORED: verified OKX OI observation committed to main` 확인. 전체 바이트 SHA 비교는 수행하지 않음.
- `event=schedule` 최근 100건 중 OKX 독립 예약 성공 최신 [#44496406941](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44496406941) (09:26:18 UTC), 이전 [#44437128461](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44437128461) (01:28:12 UTC). **5분 간격 독립 예약 인접 2회 성공 미입증**. 보조 실행 연속 성공과 혼동하지 않음.
- 별도 OKX 원시 HTTP 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 21:12 KST
- 19:42 KST 최신 체크포인트를 먼저 확인하고 OI 게이트만 점검. main의 수집기 `eth_oi_okx_live.py`, 워크플로 `.github/workflows/eth-oi-okx.yml`, 저장 `eth_oi_okx_latest.json`을 재조회. OKX 공개 API `ETH-USDT-SWAP` 단일 거래소 `oiCcy`(ETH), `code=0`, 300초 신선도 검증 코드 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 717357.630 ETH**, 관측 `2026-11-19T12:10:54.074Z` (21:10:54.074 KST), 수집 `12:10:54.177003Z`, 내부 `status=VERIFIED`, blob SHA `d38578ee90ca7d44c3119cb7af8ab1a02c3918bf`. 직전 19:40 관측보다 갱신. Binance OI 또는 전체 시장 OI가 아님.
- 보조 `workflow_run` [#44521474357](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44521474357) (12:10:47 UTC) 및 [#44520676406](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44520676406) (12:05:40 UTC) 모두 success. 각각 jobs API의 수집·신선도 검사·JSON 커밋 단계 success 확인. 단계 성공만으로 실제 신규 커밋 또는 출력과 저장 바이트 SHA 일치까지 단정하지 않음.
- 전체 `event=schedule` 최근 100건에서 OKX 독립 예약 성공 [#44496406941](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44496406941) (09:26:18 UTC), 이전 [#44437128461](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44437128461) (01:28:12 UTC). **독립 예약 인접 5분 2회 연속 성공 미입증**. 보조 실행 성공과 혼동하지 않음.
- 별도 OKX 원시 HTTP 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영 미검증. 수집기 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 19:42 KST
- 최신 18:22 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. OKX 공개 API `ETH-USDT-SWAP` 단일 거래소 `oiCcy`(ETH), code=0·300초 신선도 검사 로직과 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존 확인.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 719339.954 ETH**, 관측 `2026-11-19T10:40:52.278Z` (19:40:52.278 KST), 수집 `10:40:52.355745Z`, 내부 `status=VERIFIED`. 직전 18:20 관측보다 갱신. Binance OI 또는 시장 전체 OI가 아님.
- 보조 `workflow_run` [#44507883372](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44507883372) (10:40:45 UTC) 및 [#44507103628](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44507103628) (10:35:36 UTC) 모두 success. 두 실행의 jobs API에서 API 수집·신선도 검증·JSON 커밋 단계 success 확인. 두 실행 모두 독립 `schedule`이 아니며 단계 success는 개별 신규 커밋의 증거와 구별.
- **미검증:** 독립 `schedule`의 5분 간격 인접 2회 연속 성공, 별도 OKX 원시 HTTP 응답 직접 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이번 변경은 상태 문서에 한정하고 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 18:22 KST
- 최신 17:18 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. OKX 공개 API 단일 ETH-USDT-SWAP `oiCcy`(ETH), 응답 code=0·300초 신선도 검사 로직 및 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존 확인.
- main JSON **OKX ETH-USDT-SWAP 단일 거래소 OI 715072.266 ETH**, 거래소 관측 `2026-11-19T09:20:50.413Z` (18:20:50.413 KST), 수집 `09:20:50.500079Z`, 내부 `status=VERIFIED`, blob SHA `8f6644440093ab0eb512935f002e1901b0cd2b0f`. 직전 17:15 관측 이후 갱신. Binance OI나 시장 전체 OI 아님.
- 보조 `workflow_run` [#44495550665](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44495550665) (09:20:43 UTC) 및 [#44494780417](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44494780417) (09:15:42 UTC) 모두 success. Jobs API에서 두 실행의 API 수집·신선도 검증·JSON 저장 단계 success 확인. 단계 성공은 개별 신규 커밋 증거와 구분.
- 전체 `event=schedule` 최근 40건 중 OKX 독립 예약 성공 최신 [#44437128461](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44437128461) (01:28:12 UTC), 이전 [#44381683375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44381683375) (전날 19:33:08 UTC). 독립 schedule 5분 간격 인접 2회 연속 성공 미입증. 다른 워크플로의 schedule 실행과 혼동하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 여전히 미검증. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 이번 변경은 상태 문서에 한정; 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 17:18 KST
- 16:44 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main 수집기 및 워크플로의 OKX 단일 `ETH-USDT-SWAP` 공개 API, 300초 신선도 검사, 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 구성을 재확인.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 713064.890 ETH**, 관측 `2026-11-19T08:15:49.913Z` (17:15:49.913 KST), 수집 `08:15:50.022275Z`, 내부 `status=VERIFIED`. 직전 16:40 관측 이후 갱신. Binance OI나 전체 시장 OI 아님.
- 보조 `workflow_run` [#44486109987](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44486109987) (08:15:43 UTC), [#44485416917](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44485416917) (08:10:43 UTC) 모두 success. Jobs의 API 수집·신선도·JSON 저장 단계 성공 확인. 두 실행 모두 독립 `schedule`이 아니므로 독립 예약 인접 2회 성공 증거가 아님.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 16:44 KST
- 16:10 KST 최신 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 거래소 관측시각 및 300초 신선도 검증 로직 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 708384.781 ETH**, 관측 `2026-11-19T07:40:57.232Z` (16:40:57.232 KST), 수집 `07:40:57.327643Z`, 내부 `status=VERIFIED`, blob SHA `da7c2f278bfe892fae74ca3560e23b2d20c8ee65`. 16:05 관측 이후 갱신. Binance OI 또는 전체 시장 OI 아님.
- 보조 `workflow_run` [#44481459263](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44481459263) (07:40:43 UTC) 및 [#44480823327](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44480823327) (07:35:42 UTC) 모두 success. 두 실행의 jobs API에서 API 수집·신선도 검증·JSON 커밋 단계 success 확인. 이는 독립 `schedule` 성공 증거가 아니며, 단계 success만으로 개별 신규 커밋을 확정하지 않음.
- 독립 `schedule`의 인접 5분 2회 연속 성공, 별도 OKX 원시 HTTP 본문 직접 대조, 최신 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 16:10 KST
- 직전 14:25 KST 체크포인트를 먼저 확인하고 OI 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. OKX 공개 API 단일 `ETH-USDT-SWAP` `oiCcy`(ETH), 거래소 관측시각 및 300초 신선도 검증 로직 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 705481.810 ETH**, 관측 `2026-11-19T07:05:56.290000+00:00` (16:05:56.290 KST), 수집 `07:05:56.343465Z`, 내부 `status=VERIFIED`. 14:20 관측 이후 갱신. Binance OI 또는 전체 시장 OI 아님.
- 보조 `workflow_run` [#44476979430](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44476979430) (07:05:48 UTC) 및 [#44476376206](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44476376206) (07:01:00 UTC) 모두 success. 각 jobs API에서 API 수집·신선도 검사·JSON 저장 단계 success 확인. 최신 07:10:42 UTC 보조 실행 #44477601034는 조회 당시 진행 중이므로 성공으로 간주하지 않음.
- 독립 `schedule`의 인접 5분 2회 연속 성공은 이번 조회에서 확인되지 않음. 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영도 미검증. collector 내부 VERIFIED와 보조 실행 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 복구 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 14:25 KST
- 직전 13:22 KST 체크포인트를 먼저 확인하고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 거래소 관측시각 및 300초 신선도 검증 로직 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 699559.431 ETH**, 관측 `2026-11-19T05:20:56.158Z` (14:20:56.158 KST), 수집 `05:20:56.242715Z`, 내부 `status=VERIFIED`. 직전 13:20 관측보다 갱신됨. Binance OI 또는 시장 전체 OI 아님.
- 보조 `workflow_run` [#44464523795](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44464523795) (05:20:47 UTC) 및 [#44463944242](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44463944242) (05:15:44 UTC) 모두 success. 양쪽 jobs에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 최신 실행 job 원문 로그에서 관측시각·OI·USD·수집시각이 main JSON과 일치하며 `STORED: verified OKX OI observation committed to main` 출력 확인. 이는 별도 API 원시 HTTP 본문 또는 전체 바이트 SHA 대조가 아님.
- 전체 `event=schedule` 최근 100건 중 OKX 독립 예약 성공 최신 [#44437128461](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44437128461) (01:28:12 UTC), 이전 [#44381683375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44381683375) (전날 19:33:08 UTC). 약 5시간 55분 간격으로 **독립 schedule 인접 5분 2회 연속 성공 미입증**.
- 미검증: 별도 OKX 원시 HTTP 응답 본문 직접 대조, job stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영. 수집기 내부 VERIFIED와 보조 실행 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 13:22 KST
- 직전 12:30 KST 체크포인트를 먼저 확인하고 OI 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 재조회. 수집기는 OKX 공개 API의 `ETH-USDT-SWAP` 단일 종목 `oiCcy`(ETH), 거래소 관측시각 및 300초 신선도 검사 유지. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 692677.716 ETH**, 관측 `2026-11-19T04:20:49.641000+00:00` (13:20:49.641 KST), 수집 `04:20:49.723315+00:00`, 내부 `status=VERIFIED`, blob SHA `b07616bdf4d067a51cff3d84c9e5e4bf5b4ae98d`. 직전 12:25 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- 최근 보조 `workflow_run` [#44457670515](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44457670515) (04:20:43 UTC), [#44457114996](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44457114996) (04:15:54 UTC) 모두 success. 각 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 다만 단계 성공만으로 해당 실행의 신규 저장 커밋이나 전체 바이트 SHA 일치를 확정하지 않음.
- 최근 전체 `event=schedule` 100건 중 OKX 독립 예약 성공 최신 [#44437128461](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44437128461) (01:28:12 UTC), 이전 [#44381683375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44381683375) (11/18 19:33:08 UTC). 약 5시간 55분 간격으로 **독립 schedule 인접 5분 2회 연속 성공 미입증**.
- 미검증: 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 job stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영. 호출 규칙의 OKX 참조 지침만으로 완성 보고서 반영을 인정하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 12:30 KST
- 직전 11:36 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 재조회. 수집기는 OKX 공개 API `ETH-USDT-SWAP` 단일 종목의 `oiCcy`(ETH), 거래소 관측시각과 300초 신선도 검사 유지. 워크플로의 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 설정 유지.
- main JSON 실측: **OKX ETH-USDT-SWAP 단일 거래소 OI 692178.554 ETH**, 관측 `2026-11-19T03:25:49.148Z` (12:25:49.148 KST), 수집 `03:25:49.199079Z`, 내부 `status=VERIFIED`, blob SHA `2efcd3b20337edb03c1d79520b9f6281ebd6901c`. 직전 11:35 관측 이후 갱신. Binance OI 또는 전체 시장 OI 아님.
- 최근 보조 `workflow_run` [#44451350553](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44451350553) (03:25:41 UTC) 및 [#44450778276](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44450778276) (03:20:46 UTC) 모두 success. 각 jobs API에서 수집·신선도 검사·JSON 저장 단계 success 확인. 03:30:51 UTC [#44451956195](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44451956195)는 조회 당시 진행 중이므로 성공으로 간주하지 않음.
- 최근 전체 `event=schedule` 100건 중 OKX 독립 예약 성공 최신 [#44437128461](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44437128461) (01:28:12 UTC), 이전 [#44381683375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44381683375) (11/18 19:33:08 UTC). 약 5시간 55분 간격이므로 **독립 schedule의 5분 간격 인접 2회 연속 성공은 미입증**.
- 미검증: 별도 OKX 원시 HTTP 응답 직접 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 실측 OI 반영. collector 내부 VERIFIED와 jobs success만으로 OI 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 11:36 KST
- 최신 10:43 KST 체크포인트를 먼저 읽고 OI 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 확인. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- 최신 main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 688403.045 ETH**, 거래소 관측 `2026-11-19T02:35:56.031Z` (11:35:56.031 KST), 수집 `02:35:56.090298Z`, 내부 `status=VERIFIED`, blob SHA `cbb1e5867278f567039f86df175730477a6f7326`. 직전 10:40 관측보다 갱신. Binance OI 또는 전체 시장 OI 아님.
- 최신 보조 `workflow_run` [#44445459585](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44445459585) (02:35:43 UTC), [#44444865159](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44444865159) (02:30:49 UTC) 모두 success. jobs API에서 각각 수집·신선도 검사·JSON 저장 단계 success 확인. 단계 성공만으로 신규 저장 커밋 또는 전체 바이트 SHA 일치를 확정하지 않음.
- 최근 전체 `event=schedule` 100건 중 OKX 독립 예약 성공 최신 [#44437128461](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44437128461) (01:28:12 UTC), 이전 [#44381683375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44381683375) (11/18 19:33:08 UTC). 약 5시간 55분 간격으로 **독립 schedule 인접 5분 2회 연속 성공은 미입증**.
- 미검증: 별도 OKX 원시 HTTP 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영. collector 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 10:43 KST
- 직전 10:08 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `.github/workflows/eth-oi-okx.yml`에 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run`이 병존함을 재확인.
- main 최신 `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 687735.750 ETH**, 거래소 관측 `2026-11-19T01:40:54.357Z` (10:40:54.357 KST), 수집 `01:40:54.434419Z`, 내부 `status=VERIFIED`. 10:05 관측보다 갱신. Binance OI 또는 전체 시장 OI 아님.
- [#44438707170](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44438707170) (01:40:47 UTC), [#44438069146](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44438069146) (01:35:37 UTC) 모두 **보조 `workflow_run` success**. 두 실행 jobs API에서 API 수집·신선도 검증·JSON 저장 단계 success 확인. 단계 success는 각 실행에서 실제 신규 커밋 발생을 보장하지 않음.
- 이번 점검에서는 **독립 `schedule` 인접 2회 연속 성공 미입증**, 별도 OKX 원시 HTTP 응답 본문 대조 미검증, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조 미검증, 완성 ETH ESI 2.0 보고서의 실측 OI 반영 미검증. collector 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 10:08 KST
- 직전 08:41 KST 체크포인트를 먼저 확인한 후 OI 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 직접 조회. 워크플로에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 689389.865 ETH**, 거래소 관측 `2026-11-19T01:05:53.221Z` (10:05:53.221 KST), 수집 `01:05:53.274627Z`, 내부 `status=VERIFIED`, blob SHA `fa13478e5c13b6653dafaa358c8a00bf7e2f9b41`. 이전 08:40 관측보다 진전. Binance OI나 시장 전체 OI가 아님.
- 보조 `workflow_run` [#44434228903](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44434228903) (01:05:38 UTC), [#44433600225](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44433600225) (01:00:59 UTC) 모두 success. 각 jobs API에서 수집·신선도 검사·JSON 저장 단계 success 확인. 최신 실행 **원문 job 로그**에서 `69b0ab7` 커밋을 main에 push하고 `STORED`를 출력한 사실도 확인. 단계 성공만이 아닌 실제 신규 저장 커밋 확인 진척.
- 최근 `event=schedule` 목록에서 OKX 독립 예약 성공 최신 [#44381683375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44381683375) (11/18 19:33:08 UTC), 이전 [#44295145521](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44295145521) (11:29:24 UTC). 약 8시간 4분 간격. **5분 간격 독립 schedule 인접 2회 연속 성공은 여전히 미입증**.
- 별도 OKX 원시 HTTP 본문 직접 대조, 최신 stdout과 저장 JSON의 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 08:41 KST
- 최신 07:48 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 수집기는 OKX 공개 API ETH-USDT-SWAP의 `oiCcy`(ETH), 관측시각, 300초 신선도 검사를 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- 최신 main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 690731.361 ETH**, 거래소 관측 `2026-11-18T23:40:52.654Z` (08:40:52.654 KST), 수집 `23:40:52.761705Z`, 내부 `status=VERIFIED`, blob SHA `8d1c9fb355e7135c9334f13c3e9384b0b3afbc4d`. 07:45 관측 이후 갱신됨. Binance OI 또는 전체 시장 OI가 아님.
- 최근 보조 `workflow_run` [#44422786753](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44422786753) (23:40:46 UTC) 및 [#44422087688](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44422087688) (23:35:45 UTC) 모두 success. 개별 jobs API에서 수집·신선도 검증·JSON 커밋 단계 success 확인. 저장 단계 success가 반드시 신규 커밋 또는 stdout과 저장 파일의 전체 SHA 일치를 뜻하지는 않음.
- 최근 전체 `event=schedule` 100건에서 OKX 독립 예약 성공 최신 [#44381683375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44381683375) (19:33:08 UTC), 이전 [#44295145521](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44295145521) (11:29:24 UTC). 약 8시간 4분 간격이므로 **독립 schedule의 인접 5분 2회 연속 성공 미입증**.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 job stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영 미검증. 내부 VERIFIED는 전체 OI 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 07:48 KST
- 직전 06:51 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 확인. 수집기는 OKX 공개 API `ETH-USDT-SWAP` 단일 종목의 `oiCcy`(ETH), 거래소 관측시각 및 300초 신선도 검사 로직을 유지. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 693412.819 ETH**, 거래소 관측 `2026-11-18T22:45:49.370Z` (07:45:49.370 KST), 수집 `22:45:49.465014Z`, 내부 `status=VERIFIED`, blob SHA `90a1d5affc3cb5be95ac593545055af0cad9091f`. 이전 06:45 관측 이후 갱신. Binance OI 또는 시장 전체 OI가 아님.
- 최신 보조 `workflow_run` [#44414622674](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44414622674) (22:45:42 UTC), [#44413855411](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44413855411) (22:40:44 UTC) 모두 success. 각 jobs API에서 API 수집, 신선도 검증, JSON 저장 단계 success. 단계 성공은 반드시 신규 커밋이 생겼음을 의미하지 않음.
- 최근 전체 `event=schedule` 100건 중 OKX 독립 예약 성공 최신 [#44381683375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44381683375) (19:33:08 UTC), 이전 [#44295145521](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44295145521) (11:29:24 UTC). 약 8시간 간격이므로 **5분 간격 인접 독립 schedule 2회 연속 성공 미입증**.
- 별도 OKX 원시 HTTP 응답 본문 직접 교차검증, 최신 job stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 점검에서 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 06:51 KST
- 최신 05:12 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 조회. 워크플로에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main JSON 실측: **OKX ETH-USDT-SWAP 단일 거래소 OI 692996.827 ETH**, 관측 `2026-11-18T21:45:51.817Z` (06:45:51.817 KST), 수집 `21:45:51.903539Z`, 내부 `status=VERIFIED`. 직전 05:10 관측 이후 갱신. Binance OI나 시장 전체 OI가 아님.
- 보조 `workflow_run` [#44405650297](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44405650297) (21:50:48 UTC) 및 [#44404786526](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44404786526) (21:45:45 UTC) success. 두 실행의 jobs API에서 API 수집·신선도 검사·JSON 저장 단계 모두 success. 단계 성공은 실제 신규 커밋을 보장하지 않으며 최신 JSON 관측시각은 21:45 UTC.
- 최근 OKX 실행 5건은 모두 `workflow_run`. 독립 `schedule` 인접 2회 연속 성공은 미입증. 별도 OKX 원시 HTTP 응답 직접 대조, 최신 job stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영도 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 05:12 KST
- 최신 04:34 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 695318.493 ETH**, 거래소 관측 `2026-11-18T20:10:56.471Z` (05:10:56.471 KST), 수집 `20:10:56.530206Z`, 내부 `status=VERIFIED`, blob SHA `d2b7c231399b35fc0fbfb108bb18934f010541eb`. 직전 04:33 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- 보조 `workflow_run` [#44388258388](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44388258388) (20:10:47 UTC) 및 [#44387353640](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44387353640) (20:05:42 UTC) success. 최신 실행 jobs API에서 수집·신선도 검사·JSON 저장 단계 success 직접 확인. 최근 독립 `schedule` 성공 [#44381683375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44381683375) (19:33:08 UTC) 및 이전 [#44295145521](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44295145521) (11:29:24 UTC)은 약 8시간 간격으로, 인접 5분 독립 예약 2회 연속 성공 미입증.
- 별도 실행환경에서 OKX 공개 API 직접 HTTP 호출은 DNS 해석 오류로 실패. 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조 및 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영도 미검증. 내부 VERIFIED와 보조 실행 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 04:34 KST
- 최신 03:31 KST 체크포인트를 먼저 읽고 OI 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 재조회. 수집기는 OKX 공개 API `ETH-USDT-SWAP` 단일 종목의 `oiCcy`(ETH)와 거래소 시각 및 300초 신선도 검사를 구현. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 695348.846 ETH**, 거래소 관측 `2026-11-18T19:33:15.438Z` (04:33:15.438 KST), 수집 `19:33:15.522743Z`, 내부 `status=VERIFIED`, blob SHA `0eba8f2b1f09e07a6217ac1dad19552c6fbdc692`. 03:31 관측보다 갱신됨. Binance OI나 전체 시장 OI가 아님.
- **새로운 진척:** 독립 `schedule` [#44381683375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44381683375) (19:33:08 UTC) **success** 확인. jobs API의 수집·신선도·JSON 저장 단계 모두 success. 직전 보조 `workflow_run` [#44381333706](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44381333706) (19:30:53 UTC)도 success. 독립 schedule 성공 1건 추가로 **인접 독립 schedule 2회 연속 성공은 아직 미입증**. 단계 성공만으로 실제 신규 커밋과 전체 SHA 대조를 확정하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 이번 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 03:31 KST
- 직전 02:37 KST 체크포인트를 먼저 확인하고 OI 게이트만 재검증. main의 `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 조회. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 695100.033 ETH**, 거래소 관측 `2026-11-18T18:31:03.742000+00:00` (03:31:03.742 KST), 수집 `2026-11-18T18:31:03.828649+00:00`, 내부 `status=VERIFIED`. 직전 02:36:11 KST 관측 이후 갱신. Binance OI 또는 시장 전체 OI가 아님.
- 보조 `workflow_run` [#44370544430](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44370544430) (18:30:56 UTC) 및 [#44369585127](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44369585127) (18:25:39 UTC) success. 최신 run jobs API에서 API 수집·신선도 검사·JSON 저장 단계 success. 이는 독립 예약 실행 2회 연속 성공 증거가 아님.
- GitHub 전체 `event=schedule` 최근 100건 재조회: OKX 독립 예약 성공 최신 [#44295145521](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44295145521) (11:29:24 UTC) 및 이전 [#44227117999](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44227117999) (02:58:46 UTC). 인접 5분 독립 schedule 2회 성공 미입증.
- 별도 OKX 원시 HTTP 응답 직접 대조, 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 실측 OI 반영은 이번 회차 미검증. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출 없음. 상태 문서 외 기존 수집기·현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 02:37 KST
- 최신 01:16 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 수집기는 OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 관측시각 및 300초 신선도 검사를 수행. 워크플로에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 690029.687 ETH**, 거래소 관측 `2026-11-18T17:36:11.074Z` (02:36:11.074 KST), 수집 `17:36:11.153362Z`, 내부 `status=VERIFIED`, blob SHA `18db776f8125c5151905628830cf02d76305fc97`. 직전 01:15 관측 이후 갱신. Binance OI나 전체 시장 OI가 아님.
- 최신 보조 `workflow_run` [#44360472680](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44360472680) (17:36:04 UTC), 직전 [#44359564555](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44359564555) (17:31:09 UTC) 모두 success. 최신 run jobs API에서 API 수집·신선도 검사·JSON 저장 단계 success 확인. 최근 조회된 OKX 실행 10건 모두 보조 `workflow_run`이므로 독립 `schedule` 연속 성공과 구분.
- GitHub 전체 `event=schedule` 최근 100건 중 OKX 독립 예약 성공 [#44295145521](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44295145521) (11:29:24 UTC) 및 [#44227117999](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44227117999) (02:58:46 UTC) 확인. 약 8시간 31분 간격으로 **인접 5분 독립 예약 2회 연속 성공은 미입증**.
- 이번 회차 별도 OKX 원시 HTTP 응답 본문 직접 대조, 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED 및 보조 실행 성공만으로 전체 OI 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 01:16 KST
- 직전 01:09 KST 체크포인트를 먼저 읽고 OI 게이트만 점검. main의 `.github/workflows/eth-oi-okx.yml`과 `eth_oi_okx_latest.json`을 재조회. 워크플로에 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 699382.443 ETH**, 거래소 관측 `2026-11-18T16:15:57.574Z` (01:15:57.574 KST), 수집 `16:15:57.627937Z`, 내부 `status=VERIFIED`. 직전 01:05:54.887 KST 관측 이후 갱신. Binance OI나 시장 전체 OI 아님.
- [#44345165812](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44345165812) (16:15:49 UTC), [#44344231104](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44344231104) (16:11:06 UTC) 모두 `workflow_run` success. 최신 실행 jobs API에서 API 수집·신선도 검증·JSON 저장 단계 success 확인. 두 실행 모두 독립 `schedule`이 아니므로 인접 2회 독립 예약 성공은 미입증.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 이번 실행 원문 로그↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED 및 성공 단계만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 이외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 01:09 KST
- 직전 00:06 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. OKX 공개 API `ETH-USDT-SWAP` 단일 종목 `oiCcy`(ETH), `code=0`, 거래소 관측시각·300초 신선도 검사 로직 확인. 워크플로에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 699190.069 ETH**, 관측 `2026-11-18T16:05:54.887Z` (01:05:54.887 KST), 수집 `16:05:54.968268Z`, 내부 `status=VERIFIED`. 직전 00:05 관측 이후 갱신. Binance OI나 전체 시장 OI가 아님.
- [#44343196904](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44343196904) (16:05:47 UTC) 및 [#44342283127](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44342283127) (16:01:08 UTC) 모두 `workflow_run` success. 각 jobs API에서 API 수집·출력 신선도 검사·JSON 저장 단계 success 확인. 최근 12개 OKX 실행 모두 보조 `workflow_run`으로, **독립 schedule 인접 2회 연속 성공은 미입증**. 단계 성공만으로 신규 커밋이나 원문 SHA 일치가 보장되지는 않음.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 이번 실행 로그 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-19 00:06 KST
- 직전 2026-11-18 22:15 KST 체크포인트 선확인. main의 OKX OI JSON과 워크플로 재조회. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존. 
- 최신 main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 692115.610 ETH**, 거래소 관측 `2026-11-18T15:05:55.493Z` (2026-11-19 00:05:55.493 KST), 수집 `15:05:55.606956Z`, 내부 `status=VERIFIED`. 직전 22:15 관측 이후 갱신. Binance OI 또는 시장 전체 OI 아님.
- Actions 최신 실행 목록에서 [#44331631402](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44331631402) (15:05:48 UTC), [#44330770089](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44330770089) (15:01:22 UTC) 모두 `workflow_run` success 확인. 보조 경로 연속 성공으로서 독립 `schedule` 인접 2회 성공의 증거가 아님. 최신 5개 OI 실행 모두 `workflow_run`이었음.
- 이번 점검에서 독립 OKX 원시 HTTP 응답 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 검증하지 못함. 전체 OI 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 이외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 22:15 KST
- 직전 21:48 KST 체크포인트를 먼저 확인하고 OI 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. collector는 OKX 공개 API의 단일 `ETH-USDT-SWAP` `oiCcy`(ETH), `code=0`, 거래소 관측시각과 300초 신선도 검사. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 690558.802 ETH**, 거래소 관측 `2026-11-18T13:15:55.284Z` (22:15:55.284 KST), 수집 `13:15:55.365413Z`, 내부 `status=VERIFIED`. 직전 21:45 관측 이후 갱신. Binance OI 또는 시장 전체 OI 아님.
- 최근 [#44311926430](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44311926430) (13:15:47 UTC) 및 [#44311093656](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44311093656) (13:10:55 UTC)는 모두 보조 `workflow_run` success. 두 실행의 jobs API 검증 결과를 별도 확인. 인접 독립 `schedule` 2회 연속 성공은 미입증.
- 별도 OKX 원시 HTTP 응답 본문 직접 교차검증, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. 내부 VERIFIED 및 보조 실행 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 21:48 KST
- 직전 21:12 KST 체크포인트를 먼저 확인하고 OI 전체 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 재조회. 수집기는 OKX 공개 API의 ETH-USDT-SWAP 단일 종목 `oiCcy`(ETH), 응답 `code=0`, 거래소 관측시각과 300초 신선도 검사를 수행. 워크플로에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON 실측: **OKX ETH-USDT-SWAP 단일 거래소 OI 690293.782 ETH**, 거래소 관측 `2026-11-18T12:45:57.064Z` (21:45:57.064 KST), 수집 `12:45:57.145293Z`, 내부 `status=VERIFIED`. 직전 21:10 관측 이후 갱신. Binance OI나 시장 전체 OI가 아님.
- 보조 `workflow_run` [#44307025009](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44307025009) (12:45:49 UTC) 및 [#44306223692](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44306223692) (12:40:48 UTC) success. 두 실행 jobs API에서 API 수집·신선도 검증·JSON 커밋 단계 success 확인. 성공 단계는 반드시 신규 커밋이나 원문 SHA 일치를 의미하지 않음.
- 독립 `schedule` 성공 [#44295145521](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44295145521) (11:29:24 UTC) 추가 확인; jobs 단계 success. 직전 독립 예약 성공 #44227117999 (02:58:46 UTC)와 약 8시간 31분 간격으로 **인접 5분 독립 예약 2회 연속 성공 미입증**.
- 별도 OKX 원시 HTTP 본문 교차검증, 이번 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. collector 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 21:12 KST
- 직전 19:28 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 재조회. 수집기에서 OKX 공개 API `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 관측시각과 300초 신선도 검사를 확인. 워크플로에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 691806.729 ETH**, 거래소 관측 `2026-11-18T12:10:50.228Z` (21:10:50.228 KST), 수집 `12:10:50.313159Z`, 내부 `status=VERIFIED`. 이전 19:25 관측보다 갱신. Binance OI 또는 시장 전체 OI 아님.
- 보조 `workflow_run` [#44301437383](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44301437383) (12:10:42 UTC) 및 [#44300640236](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44300640236) (12:05:42 UTC) success. 두 실행 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 성공 단계가 실제 신규 커밋이나 원문 SHA 일치까지 보장하지는 않음. 둘 다 보조 실행이므로 독립 schedule 인접 2회 연속 성공 미입증.
- 별도 OKX 원시 HTTP 본문 직접 대조, 최신 job stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 점검에서 미검증. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 복구 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 19:28 KST
- 직전 18:15 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재점검. main의 `eth_oi_okx_latest.json` 및 `.github/workflows/eth-oi-okx.yml` 직접 조회. 워크플로에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 690039.583 ETH**, 거래소 관측 `2026-11-18T10:25:54.883Z` (19:25:54.883 KST), 수집 `10:25:54.934803Z`, 내부 `status=VERIFIED`. 이전 18:10:59.132 KST 관측 이후 갱신. Binance OI 또는 시장 전체 OI 아님.
- 보조 `workflow_run` [#44285320365](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44285320365) (10:25:46 UTC) 및 [#44284527842](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44284527842) (10:20:49 UTC) 모두 success. 두 실행의 jobs API에서 API 수집·신선도 검사·JSON 저장 단계 success 직접 확인. 성공한 저장 단계는 신규 커밋 자체를 보장하지 않음. 두 실행 모두 보조 실행이므로 **독립 schedule 인접 2회 연속 성공은 미입증**.
- 별도 OKX 원시 HTTP 응답 본문 교차검증, 최신 job stdout↔저장 JSON 전체 바이트 SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 복구 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 18:15 KST
- 최신 17:14 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재점검. main의 `eth_oi_okx_latest.json` 및 `.github/workflows/eth-oi-okx.yml` 직접 조회. 워크플로에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 688456.360 ETH**, 거래소 관측 `2026-11-18T09:10:59.132Z` (18:10:59.132 KST), 수집 `09:10:59.205954Z`, 내부 `status=VERIFIED`. 직전 17:10:53.150 KST보다 갱신됨. Binance OI나 전체 시장 OI가 아님.
- 보조 `workflow_run` [#44273493934](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44273493934) (09:10:51 UTC), [#44272726231](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44272726231) (09:05:54 UTC) 모두 success. 각 jobs API에서 수집·신선도 검증·JSON 커밋 단계 success 확인. **독립 schedule 인접 2회 연속 성공은 미입증**.
- 별도 OKX 원시 HTTP 응답 본문 대조, 최신 job stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 17:14 KST
- 직전 16:47 KST 체크포인트 선확인. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. OKX 단일 `ETH-USDT-SWAP` `oiCcy`(ETH), `code=0`, 300초 신선도 검사 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON의 **OKX ETH-USDT-SWAP 단일 거래소 OI 684981.499 ETH**, 거래소 관측 `2026-11-18T08:10:53.150Z` (17:10:53.150 KST), 수집 `08:10:53.237451Z`, 내부 `status=VERIFIED`. 직전 16:45:54.784 KST 관측보다 갱신. Binance OI 또는 전체 시장 OI 아님.
- 보조 `workflow_run` [#44264768053](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44264768053) (08:10:45 UTC), [#44264040060](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44264040060) (08:05:39 UTC) 모두 success. 두 실행의 jobs API에서 수집·신선도·저장 단계 success 확인. 최신 실행 원문 job 로그에서 `STORED` 및 OI 저장 커밋 [c7916a1](https://github.com/changwookseo/eth-cvd-monitor/commit/c7916a1) 확인. 연속 보조 실행 성공은 독립 schedule 성공으로 오인하지 않음.
- 최근 전체 Actions 100건 조회 중 OKX 독립 `schedule`의 인접 2회 연속 성공 미입증. 별도 OKX 원시 HTTP 본문 직접 대조, 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 수집기 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 16:47 KST
- 직전 15:42 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 확인. 수집기는 OKX 공개 API의 단일 `ETH-USDT-SWAP` `oiCcy`(ETH), `code=0`, 관측시각과 300초 신선도를 검사. 워크플로에 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 682642.409 ETH**, 관측 `2026-11-18T07:45:54.784Z` (16:45:54.784 KST), 수집 `07:45:54.858622Z`, 내부 `status=VERIFIED`. 직전 15:40 관측 이후 갱신. Binance OI 또는 시장 전체 OI가 아님.
- 보조 `workflow_run` [#44261405459](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44261405459) (07:45:46 UTC), [#44260764449](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44260764449) (07:40:49 UTC) 모두 success. 두 실행 jobs API의 API 수집·신선도 검증·JSON 커밋 단계 success 직접 확인. 다만 성공 단계가 각 실행의 신규 커밋이나 출력↔저장 SHA 일치를 입증하지는 않음.
- 최근 100건 `event=schedule`에서 OKX 독립 예약 성공은 [#44227117999](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44227117999) (02:58:46 UTC), [#44178408246](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44178408246) (전날 21:18:24 UTC). **인접 5분 독립 schedule 2회 연속 성공은 미입증.**
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 job stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 15:42 KST
- 직전 14:19 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 직접 확인. OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), 응답 `code=0`, 거래소 시각 및 300초 신선도 검사 코드 유지. 워크플로는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 681779.625 ETH**, 관측 `2026-11-18T06:40:57.092Z` (15:40:57.092 KST), 수집 `06:40:57.191849Z`, 내부 `status=VERIFIED`. 직전 14:15 관측보다 진전. Binance OI 또는 전체 시장 OI 아님.
- 최근 보조 `workflow_run` [#44253117088](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44253117088) (06:40:49 UTC), [#44252488950](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44252488950) (06:35:41 UTC) 모두 success. 인접 5분 보조 실행은 독립 schedule 성공의 증거가 아님.
- 최근 조회된 `event=schedule` 목록의 OKX 독립 실행 성공은 [#44227117999](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44227117999) (02:58:46 UTC)와 [#44178408246](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44178408246) (전날 21:18:24 UTC)로, **독립 schedule 인접 2회 연속 성공은 미입증**.
- 이번 점검에서 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 확인되지 않음. 내부 VERIFIED는 전체 게이트 통과를 의미하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 14:19 KST
- 직전 13:49 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_latest.json`과 `.github/workflows/eth-oi-okx.yml` 직접 조회. 워크플로는 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 680648.962 ETH**, 관측 `2026-11-18T05:15:58.412Z` (14:15:58.412 KST), 수집 `05:15:58.473895Z`, 내부 `status=VERIFIED`. 직전 13:45 관측보다 진전. Binance OI나 시장 전체 OI 아님.
- 최근 보조 `workflow_run` [#44243019575](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44243019575) (05:15:50 UTC), [#44242402030](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44242402030) (05:10:47 UTC) 모두 success. 두 실행 jobs API에서 API 수집·신선도 검증·JSON 커밋 단계 success 확인. 둘 다 독립 `schedule` 실행이 아니므로 인접 독립 예약 2회 연속 성공으로 인정하지 않음.
- 이번 점검에서 독립 schedule 인접 2회 성공, 별도 OKX 원시 HTTP 응답 직접 대조, job stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 확인되지 않음. collector 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 13:49 KST
- 직전 13:01 KST 체크포인트를 먼저 확인하고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 관측시각과 300초 신선도 검사 로직 유지.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 680331.213 ETH**, 관측 `2026-11-18T04:45:55.174Z` (13:45:55.174 KST), 수집 `04:45:55.250207Z`, 내부 `status=VERIFIED`, blob SHA `9dfecd667efb03c4683745fb428d609f5819f949`. 직전 13:01 관측보다 진전. Binance 또는 전체 시장 OI가 아님.
- 최근 보조 `workflow_run` [#44239556384](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44239556384) (04:45:47 UTC) 및 [#44238994285](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44238994285) (04:40:53 UTC) success. 최근 `event=schedule` 100건 조회에서 OKX 독립 예약 최신 성공 [#44227117999](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44227117999) (02:58:46 UTC), 그 이전 [#44178408246](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44178408246) (전날 21:18:24 UTC). **인접 독립 schedule 2회 연속 성공은 미입증.**
- 이번 회차 별도 OKX 원시 HTTP 응답 본문 직접 대조, 실행 원문 로그↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서 최신 OI 실측 반영은 미검증. 내부 VERIFIED 및 보조 workflow 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 13:01 KST
- 직전 11:26 KST 체크포인트 선확인 후 OI만 재점검. main의 `eth_oi_okx_latest.json`에서 **OKX ETH-USDT-SWAP 단일 거래소 OI 678988.639 ETH**, 관측 `2026-11-18T04:01:09.043000+00:00` (13:01:09.043 KST), 수집 `2026-11-18T04:01:09.128783+00:00`, 내부 `status=VERIFIED` 확인. Binance OI 또는 전체 시장 OI가 아님. 이전 11:25 관측보다 진전됨.
- `.github/workflows/eth-oi-okx.yml`에서 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존 확인. GitHub Actions 독립 schedule [#44227117999](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44227117999) (02:58:46 UTC) 및 [#44178408246](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44178408246) (전날 21:18:24 UTC)는 success; 두 실행의 API 수집·신선도 검사·JSON 커밋 단계 success를 jobs API에서 확인. 다만 **인접한 5분 독립 schedule 2회 연속 성공은 여전히 입증되지 않음**. 단계 성공이 신규 JSON 커밋 또는 출력↔저장 바이트 일치를 보장하지 않음.
- 이번 점검에서 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. JSON 내부 VERIFIED는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 11:26 KST
- 최신 10:30 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 조회. OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), 거래소 관측시각, 300초 신선도 검사 코드 유지.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 677527.277 ETH**, 관측 `2026-11-18T02:25:59.822Z` (11:25:59.822 KST), 수집 `02:25:59.907391Z`, 내부 `status=VERIFIED`. 직전 10:25 관측 이후 갱신. Binance OI나 시장 전체 OI가 아님.
- GitHub Actions [#44223187164](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44223187164) (02:25:51 UTC), [#44222564284](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44222564284) (02:20:48 UTC)는 모두 **보조 `workflow_run` success**. 두 실행 jobs API에서 API 수집, 신선도 검사, JSON 커밋 단계 success 확인. 커밋 단계 성공만으로 각 실행의 신규 저장 및 stdout↔저장 SHA 일치를 확정하지 않음.
- 최근 100건 `event=schedule` 조회에서 OKX 독립 예약 최신 성공 [#44178408246](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44178408246) (2026-11-17 21:18:24 UTC), 이전 [#44083887275](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44083887275) (12:31:09 UTC). **인접 독립 schedule 2회 연속 성공은 입증되지 않음.**
- 별도 OKX 원시 HTTP 응답 본문 대조, 최신 job stdout↔저장 JSON 전체 바이트 SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 10:30 KST
- 직전 10:11 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. 수집기는 OKX 공개 API `ETH-USDT-SWAP` 단일 계약 `oiCcy`(ETH)와 거래소 관측시각 및 300초 신선도 검사; 워크플로에는 독립 `schedule` 및 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 670858.370 ETH**, 거래소 관측 `2026-11-18T01:25:51.093Z` (10:25:51.093 KST), 수집 `01:25:51.187180Z`, 내부 `status=VERIFIED`. 직전 10:06 관측보다 갱신됨. Binance OI 또는 시장 전체 OI가 아님.
- GitHub Actions [#44215733666](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44215733666) (01:25:43 UTC) 및 [#44215091182](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44215091182) (01:20:48 UTC)는 모두 **보조 `workflow_run` success**. 독립 `schedule`의 인접 2회 연속 성공 증거가 아님. 현재 실행들의 개별 job 원문 로그와 출력↔저장 JSON SHA 대조는 미수행.
- 별도 OKX 원시 HTTP 응답 본문 교차검증, 독립 예약 인접 2회 성공, 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 10:11 KST
- 08:13 KST 체크포인트 선확인 후 OI만 검증. main JSON OKX ETH-USDT-SWAP 단일 거래소 OI **668850.195 ETH**, 관측 2026-11-18T01:06:03.267Z (10:06:03.267 KST), 내부 VERIFIED. Binance/전체 시장 OI 아님.
- 보조 workflow_run [#44213122568](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44213122568) 및 [#44212500748](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44212500748) success; #44213780033 조회 당시 진행 중. 독립 schedule 인접 2회 성공, 원시 API 직접 대조, stdout↔JSON 전체 SHA 대조, 완성 보고서 OI 반영은 미검증.
- **OI 게이트 미통과, 펀딩비·선물 CVD 미진입, 전체 미완료.** Secret 미등록 유지·우회 없음. 상태 문서 외 변경 없음.

## 자동 복구 점검 — 2026-11-18 08:13 KST
- 최신 07:39 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 재조회. OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), 응답 `code=0`, 관측시각 및 300초 신선도 검사 코드 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 663990.310 ETH**, 관측 `2026-11-17T23:11:01.197Z` (08:11:01.197 KST), 수집 `23:11:01.275440Z`, 내부 `status=VERIFIED`. 직전 07:35 관측 이후 갱신. Binance OI나 시장 전체 OI가 아님.
- 보조 `workflow_run` [#44197054977](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44197054977) (23:10:53 UTC) 및 [#44196250958](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44196250958) (23:05:43 UTC) 모두 success. jobs API에서 수집·신선도 검사·JSON 커밋 단계 모두 success 확인. 다만 단계 success는 실제 신규 커밋을 각각 보장하지 않으며 두 실행은 독립 `schedule` 인접 2회 성공의 증거가 아님.
- 이번 회차 독립 `schedule` 인접 2회 연속 성공, 별도 OKX 원시 HTTP 응답 본문 대조, 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 07:39 KST
- 최신 07:12 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 OKX 전용 워크플로는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`을 함께 정의하며, JSON 저장 전에 ETH-USDT-SWAP 단일 거래소·300초 신선도를 검사함.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 665678.791 ETH**, 거래소 관측 `2026-11-17T22:35:56.007Z` (07:35:56.007 KST), 수집 `22:35:56.088701Z`, 내부 `status=VERIFIED`. 07:11 관측보다 갱신됨. Binance OI 또는 전체 시장 OI가 아님.
- [#44191580031](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44191580031) (22:35:47 UTC) 및 [#44190805124](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44190805124) (22:31:00 UTC)는 모두 **보조 `workflow_run` success**. 각 jobs API에서 수집·신선도 검사·JSON 커밋 단계 success 확인. 두 실행은 독립 예약 `schedule` 2회 연속 성공의 증거가 아님.
- 여전히 미검증: 독립 `schedule` 인접 2회 연속 성공, 별도 OKX 원시 HTTP 본문 교차검증, 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영. 내부 `VERIFIED`는 전체 OI 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이 체크포인트 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 07:12 KST
- 직전 06:08 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. OKX 공개 API `ETH-USDT-SWAP` 단일 계약의 `oiCcy`(ETH), 응답 `code=0`, 관측시각 및 300초 신선도 검사 로직 유지. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 665718.568 ETH**, 관측 `2026-11-17T22:11:12.409Z` (2026-11-18 07:11:12.409 KST), 수집 `22:11:12.464120Z`, 내부 `status=VERIFIED`, blob SHA `6fc7a3944de8cf32c2eb546dc2d96c2c3bab972e`. 06:06 관측보다 갱신. Binance OI 또는 전체 시장 OI 아님.
- 보조 `workflow_run` [#44187453434](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44187453434) (22:10:54 UTC) 및 [#44186584804](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44186584804) (22:05:47 UTC) 모두 success. 두 jobs의 API 수집·신선도 검사·커밋 단계 success 확인. 그러나 성공 단계가 각각 신규 저장 및 stdout↔저장 JSON 전체 바이트 SHA 일치를 입증하지는 않음.
- 최근 독립 `schedule` 성공 [#44178408246](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44178408246) (21:18:24 UTC) 확인; jobs 수집·검사·커밋 단계 success. 이전 독립 schedule 성공은 #44083887275 (12:31:09 UTC). **인접 5분 독립 schedule 2회 연속 성공은 미입증**.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영 미검증. collector 내부 VERIFIED는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 06:08 KST
- 최신 05:11 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 확인. 수집기는 OKX 공개 API `ETH-USDT-SWAP` 단일 계약의 `oiCcy`(ETH), `code=0`, 관측시각 및 300초 신선도를 검사. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 665594.026 ETH**, 관측 `2026-11-17T21:06:07.479Z` (2026-11-18 06:06:07.479 KST), 수집 `21:06:07.563426Z`, 내부 `status=VERIFIED`, blob SHA `6db872da8cf9687ca7be3ae53590529eeaf96b30`. 직전 05:10 관측보다 갱신. Binance OI 또는 전체 시장 OI 아님.
- Actions [#44176201546](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44176201546) (21:05:53 UTC) 및 [#44175360652](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44175360652) (21:01:09 UTC) 모두 **보조 `workflow_run` success**. 독립 예약 `schedule` 최근 100건에서 최신 OKX 실행 [#44083887275](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44083887275) (전날 12:31 UTC), 이전 #44011834416 (03:40 UTC) 확인; 인접 독립 예약 2회 연속 성공 미입증.
- 이번 회차 별도 OKX 원시 HTTP 응답 직접 대조, 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영 미검증. JSON 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 05:11 KST
- 최신 03:14 KST 체크포인트를 먼저 확인한 후 OI 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. collector는 OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 관측시각과 300초 신선도를 검사. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 668032.737 ETH**, 거래소 관측 `2026-11-17T20:10:56.579Z` (2026-11-18 05:10:56.579 KST), 수집 `20:10:56.667276Z`, 내부 `status=VERIFIED`. 직전 체크포인트 03:11 관측보다 갱신. Binance OI나 전체 시장 OI가 아님.
- Actions [#44166527360](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44166527360) (20:10:50 UTC) 및 [#44165615879](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44165615879) (20:05:43 UTC) 모두 **보조 `workflow_run` success**. 두 실행의 jobs API에서 API 수집·신선도 검증·JSON 커밋 단계 success 확인. 그러나 독립 `schedule` 인접 2회 성공 증거는 아니며 커밋 단계 success가 반드시 신규 저장을 뜻하지 않음.
- 별도 OKX 원시 HTTP 응답 본문 직접 교차검증, 최신 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 이번 회차 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 03:14 KST
- 직전 02:50 KST 체크포인트를 먼저 읽고 OI 게이트만 점검. main의 `eth_oi_okx_latest.json` 및 `.github/workflows/eth-oi-okx.yml` 재조회. 워크플로에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 670009.387 ETH**, 거래소 관측 `2026-11-17T18:11:14.262Z` (2026-11-18 03:11:14.262 KST), 수집 `18:11:14.316113Z`, 내부 `status=VERIFIED`. 직전 02:46 관측보다 갱신. Binance OI나 시장 전체 OI 아님.
- Actions [#44145041901](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44145041901) (18:10:55 UTC) 및 [#44144145969](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44144145969) (18:05:55 UTC)는 모두 **보조 `workflow_run` success**. 양쪽 jobs API에서 수집·신선도 검사·JSON 커밋 단계 success 확인. 독립 `schedule` 최근 100건 중 OKX 최신 성공은 [#44083887275](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44083887275) (전날 12:31:09 UTC), 그 전 #44011834416 (03:40:21 UTC). 인접 독립 예약 2회 성공 미입증.
- 별도 OKX 원시 HTTP 응답 본문 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 직접 대조, 완성 ETH ESI 2.0 보고서 최신 OI 실측 반영은 미검증. collector 내부 VERIFIED나 job 단계 success만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 02:50 KST
- 01:27 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 수집기는 OKX 공개 API의 ETH-USDT-SWAP 단일 계약 `oiCcy`(ETH), `code=0`, 관측시각 및 300초 신선도를 검사. 워크플로는 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 670401.835 ETH**, 관측 `2026-11-17T17:46:05.143Z` (02:46:05.143 KST), 수집 `17:46:05.224233Z`, 내부 `status=VERIFIED`. 직전 01:26 관측 이후 갱신. Binance OI 또는 전체 시장 OI 아님.
- 최신 [#44140554784](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44140554784) (17:45:57 UTC), 직전 [#44139650311](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44139650311) (17:40:57 UTC)는 모두 **보조 `workflow_run` success**. 각 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 성공 단계만으로 신규 커밋 또는 전체 바이트 SHA 일치까지 입증하지 않음. 독립 `schedule` 인접 2회 성공은 확인되지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서 최신 실측 OI 반영은 미검증. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 01:27 KST
- 직전 00:30 KST 체크포인트를 먼저 읽고 OI 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. 수집기는 OKX 공개 API의 단일 ETH-USDT-SWAP `oiCcy`(ETH), 응답 code=0, 관측시각 및 300초 신선도를 검사하며 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 670586.578 ETH**, 관측 `2026-11-17T16:26:05.567Z` (2026-11-18 01:26:05.567 KST), 수집 `16:26:05.662527Z`, 내부 `status=VERIFIED`. 직전 00:26 관측보다 갱신. Binance OI나 전체 시장 OI 아님.
- 최근 [#44125686707](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44125686707) (16:25:56 UTC), [#44124756957](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44124756957) (16:21:06 UTC) 모두 **보조 `workflow_run` success**. 두 실행의 jobs API에서 수집·신선도 검사·JSON 커밋 단계 success 확인. 최신 전체 실행 목록의 OKX 실행들은 보조 실행이며 독립 `schedule` 인접 2회 성공은 확인되지 않음. 커밋 단계 success만으로 매 실행의 신규 저장 또는 전체 바이트 SHA 일치를 단정하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 조회는 DNS 해석 오류로 실패. 실행 stdout↔저장 JSON 전체 바이트 SHA 대조 및 실제 완성 ETH ESI 2.0 보고서 최신 실측 OI 반영 미검증. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-18 00:30 KST
- 직전 2026-11-17 23:27 KST 체크포인트를 먼저 확인하고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 수집기는 OKX 공개 ETH-USDT-SWAP 단일 계약 `oiCcy`(ETH), `code=0`, 관측시각과 300초 신선도 검사. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 674331.739000001 ETH**, 관측 `2026-11-17T15:26:17.465000+00:00` (2026-11-18 00:26:17.465 KST), 수집 `15:26:17.520820Z`, 내부 `status=VERIFIED`. 이전 23:25 관측보다 갱신. Binance OI 또는 전체 시장 OI 아님.
- [#44114290723](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44114290723) (15:26:08 UTC)와 [#44113287240](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44113287240) (15:20:57 UTC) 모두 **보조 `workflow_run` success**. 두 실행의 jobs API에서 수집·신선도 검증·JSON 커밋 단계 success 확인. 최근 전체 실행 목록에서 인접한 독립 `schedule` 성공 2회는 확인되지 않음. 단계 success만으로 신규 커밋이나 전체 바이트 SHA 일치를 단정하지 않음.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 회차 미검증. JSON 내부 VERIFIED는 전체 게이트 통과를 의미하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 23:27 KST
- 직전 22:38 KST 체크포인트를 먼저 확인한 뒤 OI 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON blob `27f001c80a69d4a024c03dd5d6acd921b406d9f2`: **OKX ETH-USDT-SWAP 단일 거래소 OI 676391.058 ETH**, 관측 `2026-11-17T14:25:51.332Z` (23:25:51.332 KST), 수집 `14:25:51.426846Z`, 내부 `status=VERIFIED`. 이전 22:36 관측 이후 갱신. Binance OI나 전체 시장 OI가 아님.
- 최근 [#44102987777](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44102987777) (14:25:40 UTC) 및 [#44102082924](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44102082924) (14:20:46 UTC)는 모두 **보조 workflow_run success**. 두 실행 jobs API에서 API 수집, 신선도 검사, JSON 커밋 단계 success 확인. 보조 실행을 독립 schedule 2회 연속 성공으로 인정하지 않음.
- 별도 OKX 원시 HTTP 직접 조회는 실행환경 DNS 해석 실패로 대조 불가. 최신 실행 출력↔저장 JSON 전체 바이트 SHA 대조, 인접 독립 schedule 2회 성공, 완성 ETH ESI 2.0 보고서 최신 실측 반영은 미검증. collector 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 22:38 KST
- 직전 21:22 KST 체크포인트 확인 후 OI 선행 게이트만 재검증. main의 OKX 전용 workflow는 독립 schedule 및 보조 workflow_run을 병행하며, OKX ETH-USDT-SWAP 단일 거래소 자료임.
- main 최신 eth_oi_okx_latest.json: OKX OI **674424.489 ETH**, 거래소 관측 **2026-11-17T13:36:03.667Z** (22:36:03.667 KST), 수집 13:36:03.753920Z, 내부 status VERIFIED. 이전 21:20 관측 이후 갱신. Binance OI나 시장 전체 OI가 아님. 최신 저장 커밋 [a8fdf90](https://github.com/changwookseo/eth-cvd-monitor/commit/a8fdf90c6c63e2f1e9b415aa9938e33c7c7aeaae), 직전 [7bc81bc](https://github.com/changwookseo/eth-cvd-monitor/commit/7bc81bcf9df9911f5b8d1a6b346f0313edc4e34e)으로 5분 간격 연속 JSON 갱신 확인.
- 최신 OKX Actions [#44094308417](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44094308417) 및 [#44093477499](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44093477499) 모두 workflow_run success. 독립 schedule 인접 2회 연속 성공 증거가 아니므로 해당 게이트 미통과.
- 별도 OKX 원시 HTTP 본문 직접 대조, 실행 stdout과 저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과를 의미하지 않음. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.**
- Binance Cron CRONJOB_API_KEY Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 21:22 KST
- 직전 20:42 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 재조회. 수집기는 OKX 공개 API의 단일 ETH-USDT-SWAP `oiCcy`(ETH), `code=0`, 관측시각·300초 신선도를 검사. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON blob `7f2798ebb64d6be9f69c3a2b83c56f19a459bcab`: **OKX ETH-USDT-SWAP 단일 거래소 OI 671804.608 ETH**, 거래소 관측 `2026-11-17T12:20:57.851Z` (21:20:57.851 KST), 수집 `12:20:57.932412Z`, 내부 `status=VERIFIED`. 직전 20:40 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- 최근 보조 `workflow_run` [#44082272041](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44082272041) (12:20:51 UTC), [#44081479836](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44081479836) (12:15:45 UTC) 모두 `success`. 최근 100개 전체 Actions 실행 중 확인된 OKX 실행 12건은 모두 보조 `workflow_run`으로, 독립 `schedule` 인접 2회 연속 성공의 증거가 아님. 최신 JSON의 관측시각 진전으로 연속 갱신 확인.
- 이번 점검에서 별도 OKX 원시 HTTP 응답 본문 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 실측 OI 반영은 검증되지 않음. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.**
- Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 20:42 KST
- 직전 19:38 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 수집기는 OKX 공개 API `ETH-USDT-SWAP` 단일 계약의 `oiCcy`(ETH), `code=0`, 거래소 관측시각과 300초 신선도를 검사하며, 워크플로는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`을 병행.
- main 최신 JSON blob `2064ddc8f49df0648007167ff2103e616811b99d`: **OKX ETH-USDT-SWAP 단일 거래소 OI 677132.258 ETH**, 거래소 관측 `2026-11-17T11:40:57.048Z` (20:40:57.048 KST), 수집 `11:40:57.130291Z`, 내부 `status=VERIFIED`. 직전 19:35 관측 이후 갱신. Binance OI 또는 시장 전체 OI가 아님.
- 보조 `workflow_run` [#44076181067](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44076181067) (11:40:50 UTC)와 [#44075436235](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44075436235) (11:35:43 UTC) 모두 success. 두 실행의 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 커밋 단계 success만으로 각 실행의 신규 커밋이나 출력↔저장 파일 전체 바이트 SHA 일치를 단정하지 않음.
- 최근 전체 `event=schedule` 실행 목록에서 OKX 독립 예약 성공 최신 [#44011834416](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44011834416) (03:40:21 UTC), 이전 [#43954833115](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43954833115) (전날 20:55:55 UTC). 인접 독립 schedule 2회 연속 성공 미입증.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 job stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.**
- Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 19:38 KST
- 최신 19:00 KST 체크포인트를 먼저 확인. main의 OKX OI 워크플로에서 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존을 재확인.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 687587.514 ETH**, 거래소 관측 `2026-11-17T10:35:47.347Z` (19:35:47.347 KST), 수집 `10:35:47.401627Z`, 내부 status=VERIFIED. 직전 18:55 관측 이후 갱신. Binance 또는 시장 전체 OI가 아님.
- 최근 [#44066265842](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44066265842) (10:35:39 UTC), [#44065560838](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44065560838) (10:31:09 UTC) 모두 보조 `workflow_run` success. 최근 목록에서 연속 갱신 정황 확인; 독립 `schedule` 인접 2회 성공 증거가 아님.
- 별도 OKX 원시 HTTP 응답 본문 대조, 실행 출력↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 반영은 미검증. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.**
- Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 19:00 KST
- 직전 18:07 KST 체크포인트를 먼저 확인하고 OI 게이트만 점검. main의 `.github/workflows/eth-oi-okx.yml`은 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run`을 병행.
- main `eth_oi_okx_latest.json` blob SHA `5c94d2e7d8633793c072349d64e6c95852bae5eb`: **OKX ETH-USDT-SWAP 단일 거래소 OI 678108.141 ETH**, 관측 `2026-11-17T09:55:52.940Z` (18:55:52.940 KST), 수집 `09:55:53.020123Z`, 내부 status=VERIFIED. 직전 18:05 관측 이후 갱신됨. Binance OI 또는 시장 전체 OI 아님.
- 보조 `workflow_run` [#44060066752](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44060066752) (09:55:46 UTC), [#44059328624](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44059328624) (09:50:55 UTC) 모두 success. 각각 jobs API에서 수집·신선도 검증·커밋 단계 success. 최신 전체 실행 100건 중 OKX 실행 12건 모두 보조 workflow_run이며 독립 schedule 인접 2회 연속 성공 증거는 없음.
- 별도 OKX 원시 HTTP 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. JSON 내부 VERIFIED나 단계 success만으로 전체 게이트 통과 인정하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 18:07 KST
- 직전 16:17 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. OKX 공개 ETH-USDT-SWAP 단일 거래소 `oiCcy`(ETH), code=0, 300초 신선도 검사 로직과 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존 확인.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 671719.171 ETH**, 거래소 관측 `2026-11-17T09:05:58.275000+00:00` (18:05:58.275 KST), 수집 `09:05:58.334235+00:00`, 내부 `status=VERIFIED`. 직전 16:15 관측보다 갱신. Binance OI 또는 전체 시장 OI 아님.
- [#44052410837](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44052410837) (09:05:51 UTC) 및 [#44051676066](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44051676066) (09:00:58 UTC)는 모두 **보조 `workflow_run` success**. 각각 jobs API에서 수집·신선도 검증·JSON 커밋 단계 success 확인. 단계 성공만으로 각 실행의 신규 저장 커밋이나 전체 바이트 SHA 일치를 단정하지 않음.
- 독립 `schedule`의 인접 2회 연속 성공, 별도 OKX 원시 HTTP 본문 직접 대조, 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 16:17 KST
- 직전 15:28 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON blob `25c20f8f67202fc1f6ca6a333f4af9b9f1a49efc`: **OKX ETH-USDT-SWAP 단일 거래소 OI 669217.703 ETH**, 거래소 관측 `2026-11-17T07:15:51.899000+00:00` (16:15:51.899 KST), 수집 `2026-11-17T07:15:51.950794+00:00`, 내부 `status=VERIFIED`. 15:25 관측 이후 갱신. Binance OI 또는 전체 시장 OI 아님.
- 보조 `workflow_run` [#44037331978](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44037331978) (07:15:44 UTC), [#44036692720](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44036692720) (07:10:48 UTC) 모두 success. 각 jobs API에서 수집·신선도 검증·JSON 커밋 단계 success 확인. 커밋 단계 성공만으로 실제 신규 커밋 발생이나 전체 바이트 SHA 일치를 단정하지 않음. 최근 전체 실행 목록 100건의 OKX 실행은 보조 경로이며 독립 `schedule` 인접 2회 성공 증거는 확인되지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 실행 stdout↔저장 JSON 전체 바이트 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 15:28 KST
- 최신 15:11 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 확인. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON blob `181e20a0604885665eb8417092ab4342788a9818`: **OKX ETH-USDT-SWAP 단일 거래소 OI 676192.574 ETH**, 거래소 관측 `2026-11-17T06:25:43.629Z` (15:25:43.629 KST), 수집 `06:25:43.680692Z`, 내부 `status=VERIFIED`. 직전 15:11 관측 이후 갱신. Binance OI 또는 전체 시장 OI 아님.
- 보조 `workflow_run` [#44031117014](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44031117014) (06:25:34 UTC) 및 [#44030515168](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44030515168) (06:20:44 UTC) 모두 success. 각 jobs API에서 API 수집·신선도 검증·JSON 커밋 단계 success 확인. 최신 원문 job 로그에서 main 저장 커밋 `5fa81dd` 및 `STORED` 확인. 이는 보조 실행의 연속 갱신 증거이며 독립 예약 연속 성공 증거가 아님.
- 전체 `event=schedule` 최근 100건 조회에서 OKX 독립 예약 성공 최신 [#44011834416](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44011834416) (03:40:21 UTC), 이전 [#43954833115](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43954833115) (11/16 20:55:55 UTC). **인접 독립 schedule 2회 연속 성공 미입증**.
- 별도 OKX 원시 HTTP 본문 직접 대조, 실행 출력과 저장 JSON의 전체 바이트 SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 15:11 KST
- 최신 13:34 KST 체크포인트를 먼저 읽고 OI 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존, API code=0/ETH-USDT-SWAP 단일 관측/300초 신선도 검사 로직 유지.
- main JSON blob `590ca5e2aa987f12d02b197412c272d45757a7e0`: **OKX ETH-USDT-SWAP 단일 거래소 OI 677158.375 ETH**, 거래소 관측 `2026-11-17T06:11:01.090Z` (15:11:01.090 KST), 수집 `06:11:01.182008Z`, 내부 status=VERIFIED. 이전 13:31 관측보다 갱신됨. Binance OI 또는 전체 시장 OI가 아님.
- 최신 보조 `workflow_run` [#44029310783](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44029310783) (06:10:55 UTC) 및 [#44028663275](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44028663275) (06:05:37 UTC) 모두 success. 두 실행의 jobs API에서 수집·신선도 검사·JSON 커밋 단계 success 확인. 조회된 최근 5개 OKX 실행 모두 보조 workflow_run; **독립 schedule 인접 2회 연속 성공은 미입증**.
- 별도 OKX 원시 HTTP 본문 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED 및 단계 success만으로 전체 게이트 통과로 인정하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 13:34 KST
- 직전 12:48 KST 체크포인트를 먼저 확인하고 OI 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. OKX 공개 ETH-USDT-SWAP 단일 거래소 `oiCcy`(ETH), API code=0 및 300초 신선도 검증 로직, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 구성 유지.
- main 최신 JSON blob `f7132dc49782c995423eab7e5a61fb0014c28011`: **OKX ETH-USDT-SWAP 단일 거래소 OI 670544.814 ETH**, 거래소 관측 `2026-11-17T04:31:06.262Z` (13:31:06.262 KST), 수집 `04:31:06.343715Z`, 내부 status=VERIFIED. 이전 12:45 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- GitHub Actions 최근 보조 `workflow_run` [#44017708647](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44017708647) (04:30:57 UTC) 및 [#44017097126](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44017097126) (04:25:36 UTC) 모두 success. 전체 `event=schedule` 최근 100건 중 OKX 독립 예약 성공 최신 [#44011834416](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44011834416) (03:40:21 UTC), 직전 [#43954833115](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43954833115) (11/16 20:55:55 UTC). **인접한 독립 schedule 2회 연속 성공은 미입증**. 최근 보조 성공은 독립 예약 성공으로 취급하지 않음.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 점검에서 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 12:48 KST
- 직전 11:47 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 공개 OKX ETH-USDT-SWAP 단일 거래소 `oiCcy`(ETH), code=0, 관측시각 및 300초 신선도 검증 로직과 독립 `schedule: 2-59/5 * * * *`·보조 `workflow_run` 구성 유지.
- main JSON blob `346bb34f6caae68a5d7bcb948c4cc4471c322c78`: **OKX ETH-USDT-SWAP 단일 거래소 OI 666583.017 ETH**, 거래소 관측 `2026-11-17T03:45:56.228Z` (12:45:56.228 KST), 수집 `03:45:56.286740Z`, 내부 status=VERIFIED. 이전 11:45 관측 이후 갱신. Binance OI나 시장 전체 OI 아님.
- 독립 `schedule` 실행 [#44011834416](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44011834416) (03:40:21 UTC) **success** 신규 확인. 보조 `workflow_run` [#44011880856](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44011880856) (03:40:44 UTC), [#44012454712](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44012454712) (03:45:47 UTC) 모두 success. 세 실행의 jobs API에서 API 수집, 출력 신선도 검증, JSON 커밋 단계 모두 success 확인. 다만 인접한 독립 schedule 두 번의 연속 성공은 아직 입증되지 않음.
- 별도 OKX 원시 HTTP 응답 본문 대조, 이번 실행 stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 11:47 KST
- 직전 10:54 KST 체크포인트를 먼저 읽고 OI 게이트만 재점검. main 워크플로의 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존 확인.
- main 최신 `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 669005.213 ETH**, 거래소 관측 `2026-11-17T02:45:52.078Z` (11:45:52.078 KST), 수집 `02:45:52.179689Z`, 내부 `status=VERIFIED`. 이전 10:50 관측 이후 갱신. Binance 또는 전체 시장 OI 아님.
- GitHub Actions 전체 최신 실행 조회에서 [#44005336541](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44005336541) (02:45:45 UTC), [#44004741889](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/44004741889) (02:40:43 UTC) 등 최근 5건 OKX OI 실행 모두 `workflow_run` success. 독립 `schedule`의 인접 2회 연속 성공 증거는 아님. 이전 체크포인트의 독립 예약 성공 기록만 유지.
- 별도 OKX 원시 HTTP 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 10:54 KST
- 직전 09:26 KST 체크포인트를 먼저 읽고 OI 게이트만 재점검. main의 `.github/workflows/eth-oi-okx.yml`은 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`을 함께 사용하며, 검증·커밋 단계를 유지함.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 663756.963 ETH**, 관측 `2026-11-17T01:50:52.230Z` (10:50:52.230 KST), 수집 `01:50:52.285463Z`, 내부 `status=VERIFIED`. 이전 09:25 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- 최근 보조 `workflow_run` [#43998618773](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43998618773) (01:50:45 UTC), [#43998010974](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43998010974) (01:45:43 UTC) 모두 completed/success. 다만 이는 독립 예약 연속 성공이 아님.
- 전체 `event=schedule` 최근 100건에서 OKX OI 독립 예약 성공 최신 [#43954833115](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43954833115) (11/16 20:55:55 UTC), 이전 [#43853421423](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43853421423) (11/16 10:57:26 UTC). **인접 독립 schedule 2회 연속 성공 미입증**.
- 별도 OKX 원시 HTTP 본문 직접 대조, 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 점검에서 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 09:26 KST
- 직전 08:23 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 원문 확인. OKX 공개 API의 단일 `ETH-USDT-SWAP` `oiCcy`(ETH) 및 300초 신선도 검증 로직, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON blob `a6f7e955b2a7af18a721e78cb602fdcfc84e81da`: **OKX ETH-USDT-SWAP 단일 거래소 OI 661622.563 ETH**, 관측 `2026-11-17T00:25:52.624Z` (09:25:52.624 KST), 수집 `00:25:52.677910Z`, 내부 `status=VERIFIED`. 이전 08:20 관측 이후 갱신. Binance 또는 시장 전체 OI 아님.
- 보조 `workflow_run` [#43987530450](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43987530450) (00:25:41 UTC), [#43986870331](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43986870331) (00:20:47 UTC) 모두 success. 최신 job #133719428979의 수집·신선도·커밋 단계 success, 원문 로그의 `PASS`, 실제 main 저장 커밋 [31ac7d7](https://github.com/changwookseo/eth-cvd-monitor/commit/31ac7d7), `STORED` 확인. 다만 실행 출력↔저장 파일 전체 바이트 SHA 직접 대조는 별도 미실시.
- 최근 전체 `event=schedule` 100건에서 OKX 독립 예약 최신 성공 [#43954833115](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43954833115) (11/16 20:55:55 UTC), 직전 [#43853421423](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43853421423) (11/16 10:57:26 UTC). **인접 독립 schedule 2회 연속 성공 미입증**. 별도 OKX 원시 HTTP 본문 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영도 미검증.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 08:23 KST
- 최신 07:34 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml` 원문 재확인: OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), 300초 신선도 검사, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json` blob `d79fb6a209f624cc1641df8250998c0657ff769e`: **OKX ETH-USDT-SWAP 단일 거래소 OI 659079.224 ETH**, 관측 `2026-11-16T23:20:56.973Z` (08:20:56.973 KST), 수집 `23:20:57.035867Z`, 내부 `status=VERIFIED`. 이전 07:30 관측보다 갱신. Binance OI 또는 시장 전체 OI 아님.
- 보조 [#43978476534](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43978476534) (23:20:49 UTC) 및 [#43977723279](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43977723279) (23:15:44 UTC) 모두 `workflow_run` success. 최신 job #133688483720 원문에서 수집 출력값·관측시각이 main JSON과 일치하고 `PASS`, 실제 커밋 [0f89ef4](https://github.com/changwookseo/eth-cvd-monitor/commit/0f89ef4), `HEAD -> main`, `STORED` 확인. 단 전체 JSON 바이트 SHA 비교는 별도 미실시.
- 최근 `event=schedule` 조회의 OKX 독립 예약 성공 최신은 [#43954833115](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43954833115) (11/16 20:55:55 UTC), 직전 [#43853421423](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43853421423) (10:57:26 UTC). **인접 독립 schedule 2회 연속 성공 미입증**. 별도 OKX 원시 HTTP 본문 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영도 미검증.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 07:34 KST
- 직전 06:31 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 검증. main 워크플로의 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 설정 유지.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 659175.343 ETH**, 관측 `2026-11-16T22:30:59.678Z` (07:30:59.678 KST), 수집 `22:30:59.752182Z`, 내부 `status=VERIFIED`. 직전 06:31 관측보다 갱신. Binance 또는 전체 시장 OI 아님.
- 최신 [#43970777628](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43970777628) (22:30:53 UTC), 직전 [#43969944972](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43969944972) (22:25:40 UTC)는 모두 **보조 workflow_run success**. 두 실행의 jobs 단계 상태: [[["Set up job","success"],["Run actions/checkout@v4","success"],["Run actions/setup-python@v5","success"],["Fetch and validate OKX ETH swap OI","success"],["Validate output contract and freshness","success"],["Commit verified OKX OI snapshot","success"],["Post Run actions/setup-python@v5","success"],["Post Run actions/checkout@v4","success"],["Complete job","success"]],[["Set up job","success"],["Run actions/checkout@v4","success"],["Run actions/setup-python@v5","success"],["Fetch and validate OKX ETH swap OI","success"],["Validate output contract and freshness","success"],["Commit verified OKX OI snapshot","success"],["Post Run actions/setup-python@v5","success"],["Post Run actions/checkout@v4","success"],["Complete job","success"]]]. 독립 schedule 인접 2회 성공으로 인정하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 실측 OI 반영은 미검증. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.**
- Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 06:31 KST
- 직전 05:52 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml` 원문 재확인: OKX 공개 API ETH-USDT-SWAP 단일 상품, `oiCcy`(ETH), `code=0`·300초 신선도 검사, 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json` blob `a33866242d61c5afc1059e02a3199dc26e19ea50`: **OKX ETH-USDT-SWAP 단일 거래소 OI 660202.453 ETH**, 관측 `2026-11-16T21:31:12.502Z` (06:31:12.502 KST), 수집 `21:31:12.597650Z`, 내부 `status=VERIFIED`. 직전 05:50 관측 이후 갱신. Binance OI나 전체 시장 OI 아님.
- 독립 `schedule` 성공 [#43954833115](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43954833115) (20:55:55 UTC) 1건 새로 확인. 최근 보조 `workflow_run` [#43959980841](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43959980841) (21:25:41 UTC), [#43960879318](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43960879318) (21:31:05 UTC) 모두 success. 세 실행 모두 jobs API의 수집·신선도·커밋 단계 success. 최신 job #133627612857 원문 로그에서 실제 저장 커밋 [d607f6a](https://github.com/changwookseo/eth-cvd-monitor/commit/d607f6a) 및 `STORED` 확인.
- 독립 `schedule` **인접 2회 연속 성공 미입증**. 별도 OKX 원시 HTTP 응답 본문 직접 대조, 실행 stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영도 미검증. 내부 VERIFIED 및 보조 실행 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 05:52 KST
- 직전 04:22 체크포인트를 먼저 확인하고 OI 선행 게이트만 재검증. `eth_oi_okx_live.py` 및 `.github/workflows/eth-oi-okx.yml` 원문 확인: OKX 공개 API의 ETH-USDT-SWAP 단일 상품 `oiCcy`(ETH), 응답 코드·300초 신선도 검사, 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json` blob `1a87de89a737ee2295da7f98250300cdb3ba5906`: **OKX ETH-USDT-SWAP 단일 거래소 OI 659327.116 ETH**, 거래소 관측 `2026-11-16T20:50:55.661Z` (05:50:55.661 KST), 수집 `20:50:55.746186Z`, 내부 `status=VERIFIED`. 직전 04:20 관측보다 갱신. Binance OI나 전체 시장 OI 아님.
- Actions [#43953974091](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43953974091) (20:50:48 UTC), [#43953097526](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43953097526) (20:45:42 UTC)는 모두 보조 `workflow_run` success; 수집·검증·커밋 단계 success. 최신 job #133603507892 원문 로그에서 push 충돌 후 재시도 및 실제 main 저장 커밋 `539dba5`, `STORED` 확인.
- 독립 `schedule`의 인접 2회 연속 성공, 별도 OKX 원시 HTTP 응답 본문 직접 대조, 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 아직 미검증. 보조 workflow_run 연속 성공이나 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 04:22 KST
- 직전 04:10 KST 체크포인트 확인 후 OI 선행 게이트만 검증. main 수집기 `eth_oi_okx_live.py`는 OKX 공개 API의 단일 `ETH-USDT-SWAP` 상품 `oiCcy`(ETH), `code=0`, 거래소 시각 및 300초 신선도를 검사. 워크플로 `.github/workflows/eth-oi-okx.yml`에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 662393.017 ETH**, 관측 `2026-11-16T19:20:52.550Z` (04:20:52.550 KST), 수집 `19:20:52.629606Z`, 내부 `status=VERIFIED`. 직전 04:05 관측 이후 갱신. Binance 또는 전체 시장 OI 아님.
- Actions [#43938358537](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43938358537) (19:20:44 UTC), [#43937472436](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43937472436) (19:15:44 UTC)는 모두 **보조 `workflow_run` success**. 각 jobs API에서 수집·신선도 검사·JSON 커밋 단계 success 확인. 단계 성공만으로 실제 신규 커밋을 단정하지 않음.
- `event=schedule` 최근 100건에서 OKX 독립 예약 성공 최신 [#43853421423](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43853421423) (11/16 10:57:26 UTC), 직전 #43795139612 (02:56:25 UTC). 인접 독립 schedule 2회 연속 성공은 미입증.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 04:10 KST
- 직전 02:48 KST 체크포인트 확인 후 OI 선행 게이트만 점검. main 수집기 `eth_oi_okx_live.py`는 OKX 공개 API `ETH-USDT-SWAP` 단일 상품의 `oiCcy`(ETH), `code=0`, 관측시각 및 300초 신선도를 검증. `.github/workflows/eth-oi-okx.yml`에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 661129.732 ETH**, 관측 `2026-11-16T19:05:50.196Z` (04:05:50.196 KST), 수집 `19:05:50.272808Z`, 내부 `status=VERIFIED`. 이전 02:45 관측보다 갱신. Binance OI나 시장 전체 OI 아님.
- Actions [#43935696792](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43935696792) (19:05:41 UTC), [#43934878164](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43934878164) (19:01:03 UTC) 모두 **보조 `workflow_run` success**. 각 jobs API에서 수집·신선도 검사·JSON 커밋 단계 success 확인. 다만 커밋 단계 success는 반드시 신규 저장을 의미하지 않음.
- `event=schedule` 최근 100건 중 OKX 독립 예약 성공 최신 [#43853421423](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43853421423) (11/16 10:57:26 UTC), 직전 [#43795139612](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43795139612) (02:56:25 UTC). 인접 독립 schedule 2회 연속 성공은 미입증.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. JSON 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 02:48 KST
- 최신 01:27 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`는 OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), 응답 `code=0`, 거래소 관측시각 및 300초 신선도 검사를 수행. `.github/workflows/eth-oi-okx.yml`에 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run`이 병존함을 확인.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 666233.138 ETH**, 거래소 관측 `2026-11-16T17:45:56.674Z` (02:45:56.674 KST), 수집 `17:45:56.753043Z`, 내부 `status=VERIFIED`. 이전 01:26 관측 이후 갱신됨. Binance OI 또는 전체 시장 OI가 아님.
- Actions 최근 100건 중 OKX [#43921760413](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43921760413) (17:45:48 UTC), [#43920896154](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43920896154) (17:40:47 UTC), [#43920009079](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43920009079) (17:35:41 UTC) 모두 `workflow_run` success. 독립 `schedule` 인접 2회 연속 성공 증거로 인정하지 않음.
- 이번 회차에는 독립 OKX 원시 HTTP 응답 본문 직접 대조, 최신 job 원문↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 실측 OI 반영, 독립 schedule 인접 2회 연속 성공은 검증되지 않음. collector의 내부 VERIFIED는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 01:27 KST
- 최신 01:17 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 재검증. main 수집기 `eth_oi_okx_live.py` 및 워크플로 `.github/workflows/eth-oi-okx.yml` 내용 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json` blob `4f87563a6fdfbbdd7f918d7b05d41e167342c670`: **OKX ETH-USDT-SWAP 단일 거래소 OI 667340.012 ETH**, 관측 `2026-11-16T16:26:04.758Z` (01:26:04.758 KST), 수집 `16:26:04.821783Z`, 내부 `status=VERIFIED`. 이전 01:15:59 관측보다 갱신. Binance OI 또는 전체 시장 OI 아님.
- [#43907414401](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43907414401) (16:25:57 UTC) 및 [#43906493019](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43906493019) (16:21:02 UTC)는 모두 보조 `workflow_run` success; jobs API에서 수집·신선도 검사·커밋 단계 success 확인. 최신 job #133439865720 원문 로그에서 push 충돌 후 재시도, 실제 main 저장 커밋 `3f8922a` 및 `STORED` 확인.
- **미검증:** 독립 schedule 인접 2회 연속 성공, 별도 OKX 원시 HTTP 본문 직접 대조, 실행 stdout↔저장 JSON 전체 SHA 바이트 대조, 완성 ETH ESI 2.0 보고서의 실측 OI 반영. 보고서 호출 규칙에 OKX 보조 원천이 명시된 사실은 확인했으나 실제 보고서 출력 증거는 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-17 01:17 KST
- 직전 2026-11-16 23:30 KST 체크포인트 확인 후 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`(blob `6661e379f516b2457ab112a5dee3f4a6a1a41c78`)와 `.github/workflows/eth-oi-okx.yml`(blob `e83eda4680206efbc50952e4e0dde49a501a2c06`) 원문 확인. OKX 공개 API ETH-USDT-SWAP 단일 상품 `oiCcy`(ETH), 관측시각 및 300초 신선도 검사, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json` blob `acc75c8cf46089e7d6409b27d4578580208d9164`: **OKX ETH-USDT-SWAP 단일 거래소 OI 669588.994 ETH**, 거래소 관측 `2026-11-16T16:15:59.958Z` (2026-11-17 01:15:59.958 KST), 수집 `16:16:00.022147Z`, 내부 `status=VERIFIED`. 전 체크포인트 23:25 관측보다 갱신. Binance OI 또는 시장 전체 OI 아님.
- 보조 [#43905548654](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43905548654) (16:15:52 UTC), [#43904656489](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43904656489) (16:11:06 UTC) 모두 `workflow_run` success. 개별 jobs API에서 API 수집, 신선도 검사, JSON 커밋 단계 success 확인. 이 성공만으로 실제 신규 커밋 또는 전체 SHA 대조가 입증되는 것은 아님.
- 최근 `event=schedule` 100건에서 OKX 독립 예약 성공 최신 [#43853421423](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43853421423) (2026-11-16 10:57:26 UTC), 그 전 #43795139612 (02:56:25 UTC). 인접한 독립 schedule 2회 연속 성공 미입증.
- 별도 OKX 원시 HTTP 본문 직접 대조, 이번 실행 stdout↔저장 JSON 전체 SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 23:30 KST
- 직전 22:28 KST 체크포인트를 먼저 읽고 OI 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml` 원문 확인: OKX 공개 API ETH-USDT-SWAP 단일 상품 `oiCcy`(ETH), 300초 신선도 검사, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 677776.684 ETH**, 관측 `2026-11-16T14:25:49.015Z` (23:25:49.015 KST), 수집 `14:25:49.109404Z`, 내부 `status=VERIFIED`. 22:25 관측 이후 갱신. Binance OI 또는 시장 전체 OI 아님.
- [#43885605570](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43885605570) (14:25:42 UTC)와 [#43885251997](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43885251997) (14:23:42 UTC)는 모두 **보조 `workflow_run` success**. 두 실행 jobs API에서 수집·신선도 검사·커밋 단계 success 확인. 최신 job #133362779256 원문 로그에서 `PASS`, 커밋 `511847c`, `HEAD -> main`, `STORED` 확인. 직전 job #133361521143에서는 push 충돌 후 재시도 성공(`0d40418`). 이로써 보조 경로의 실제 연속 저장 및 충돌 복구 진척 확인.
- 이번 조회의 최신 Actions 목록에는 OKX 독립 `schedule` 인접 2회 성공 증거가 없음. 별도 OKX 원시 HTTP 본문 직접 대조, 로그↔JSON 전체 SHA 바이트 대조, 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영도 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** 다른 파생 후보 워크플로의 실행 성공을 복구 완료로 간주하지 않음. Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 22:28 KST
- 최신 21:32 KST 체크포인트 확인 후 OI 게이트만 재검증. main 수집기 `eth_oi_okx_live.py`와 워크플로 `.github/workflows/eth-oi-okx.yml` 유지. OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), 거래소 시각 및 300초 신선도 검사; 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 679384.709 ETH**, 거래소 관측 `2026-11-16T13:25:52.731Z` (22:25:52.731 KST), 수집 `13:25:52.811483Z`, 내부 `status=VERIFIED`. 21:31 관측보다 진전. Binance 또는 전체 시장 OI 아님.
- GitHub Actions [#43875659821](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43875659821) (13:25:46 UTC), [#43874887937](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43874887937) (13:20:51 UTC) 모두 `workflow_run` success. 개별 jobs API에서 수집·신선도·JSON 커밋 단계 success 확인. 두 보조 실행은 독립 `schedule` 인접 2회 연속 성공 증거가 아님.
- 이번 회차 별도 OKX 원시 HTTP 응답 본문 직접 교차검증, 실행 stdout↔저장 JSON 전체 SHA 대조, 독립 예약 2회 연속 성공, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. JSON 내부 VERIFIED 및 커밋 단계 success만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 21:32 KST
- 최신 상태 문서 체크포인트(17:23 KST)를 읽고 OI 게이트만 점검. main 수집기 `eth_oi_okx_live.py` blob `6661e379f516b2457ab112a5dee3f4a6a1a41c78`, 워크플로 `.github/workflows/eth-oi-okx.yml` blob `e83eda4680206efbc50952e4e0dde49a501a2c06` 확인. 공개 OKX ETH-USDT-SWAP 단일 상품 `oiCcy` ETH, 300초 신선도 검사, 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json` blob `cc6c1e6e39f7e325db7aa039afd93adc89bdffb7`: **OKX ETH-USDT-SWAP 단일 거래소 OI 681073.165 ETH**, 거래소 관측 `2026-11-16T12:31:03.446Z` (21:31:03.446 KST), 수집 `12:31:03.505247Z`, 내부 `status=VERIFIED`. 이전 17:20 관측보다 진전. Binance OI 또는 전체 시장 OI가 아님.
- GitHub Actions 최근 전체 실행 목록에서 [#43867262400](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43867262400) (12:30:55 UTC) 및 [#43866474618](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43866474618) (12:25:42 UTC) 모두 `workflow_run` success 확인. 독립 `schedule` 인접 2회 성공으로 인정하지 않음. 이번 회차 개별 jobs 원문, API 원시 HTTP 본문, 실행 stdout↔저장 JSON 전체 SHA, 완성 보고서의 실측 반영은 검증하지 못함.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 17:23 KST
- 직전 16:39 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`(blob `6661e379f516b2457ab112a5dee3f4a6a1a41c78`) 및 `.github/workflows/eth-oi-okx.yml`(blob `e83eda4680206efbc50952e4e0dde49a501a2c06`) 확인. OKX 공개 API 단일 ETH-USDT-SWAP `oiCcy`(ETH), 관측시각 및 300초 신선도 검사; 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 `eth_oi_okx_latest.json` blob `28b91c35e1b0f2e4704a8481fef5bdb0eb6ebbad`: **OKX ETH-USDT-SWAP 단일 거래소 OI 684769.482 ETH**, 관측 `2026-11-16T08:20:56.555Z` (17:20:56.555 KST), 수집 `08:20:56.630410Z`, 내부 `status=VERIFIED`. 직전 16:35 관측 이후 갱신. Binance OI나 전체 시장 OI 아님.
- [#43830470167](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43830470167) (08:20:49 UTC)와 [#43829833387](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43829833387) (08:15:52 UTC)는 모두 **보조 `workflow_run` success**. 두 실행의 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 단계 성공만으로 실제 신규 커밋 및 전체 JSON SHA 대조까지 입증하지 않음.
- 최근 `event=schedule` 100건 중 OKX 독립 예약 성공 최신 [#43795139612](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43795139612) (02:56:25 UTC), 이전 #43774432171 (전날 23:22:13 UTC). 인접 독립 예약 2회 연속 성공 미입증. 별도 OKX 원시 HTTP 응답 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영도 미검증.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 16:39 KST
- 직전 15:29 KST 체크포인트 확인 후 OI 게이트만 재검증. main의 수집기 blob `6661e379f516b2457ab112a5dee3f4a6a1a41c78`, 워크플로 blob `e83eda4680206efbc50952e4e0dde49a501a2c06` 유지. OKX 공개 API ETH-USDT-SWAP 단일 거래소 `oiCcy`(ETH) 및 300초 신선도 검사; 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON blob `dbc28d2b2897e5fc9b22efddca05f77b72a4ff40`: **OKX ETH-USDT-SWAP 단일 거래소 OI 681965.413 ETH**, 관측 `2026-11-16T07:35:55.703Z` (16:35:55.703 KST), 수집 `07:35:55.755603Z`, 내부 `status=VERIFIED`. 직전 15:25 관측 이후 갱신. Binance OI/시장 전체 OI 아님.
- 보조 [#43824950169](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43824950169) (07:35:40 UTC)와 [#43824405861](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43824405861) (07:30:53 UTC) 모두 `workflow_run` success; 수집·신선도·커밋 단계 success. **이번에는 최신 job #133156452577 원문 로그를 직접 확인**: 출력 `value=681965.4130000011`은 main JSON과 일치하며 `a5d604c` 커밋 생성 및 `HEAD -> main`, `STORED` 메시지 확인. 단 전체 JSON 바이트 SHA 직접 대조는 별도 미완료.
- `event=schedule` 최근 100건의 OKX 독립 예약 성공 최신은 [#43795139612](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43795139612) (02:56:25 UTC), 이전 #43774432171 (전날 23:22:13 UTC). 인접 독립 예약 2회 연속 성공 미입증. 별도 OKX 원시 HTTP 응답 본문 직접 대조 및 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영 미검증.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 15:29 KST
- 직전 14:42 KST 체크포인트 확인 후 OI 선행 게이트만 재검증. main 수집기 `eth_oi_okx_live.py`(blob `6661e379f516b2457ab112a5dee3f4a6a1a41c78`)와 워크플로 `.github/workflows/eth-oi-okx.yml`(blob `e83eda4680206efbc50952e4e0dde49a501a2c06`) 재조회. OKX 공개 API ETH-USDT-SWAP 단일 상품의 `oiCcy`(ETH), 관측시각·300초 신선도 검사; 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 `eth_oi_okx_latest.json` blob `5a066c88f6c1b081502e8e83ae1905fc586c6e63`: **OKX ETH-USDT-SWAP 단일 거래소 OI 686863.612 ETH**, 거래소 관측 `2026-11-16T06:25:53.499Z` (15:25:53.499 KST), 수집 `06:25:53.550966Z`, 내부 `status=VERIFIED`. 직전 14:40 관측보다 갱신. Binance 또는 전체 시장 OI가 아님.
- 보조 [#43816673730](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43816673730) (06:25:44 UTC) 및 [#43816117774](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43816117774) (06:20:46 UTC) 모두 `workflow_run` success. 각 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 단계 success만으로 신규 커밋이나 원문 로그↔저장 SHA 일치를 단정하지 않음.
- 최근 GitHub Actions `event=schedule` 100건 중 OKX 독립 예약 성공 최신은 [#43795139612](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43795139612) (02:56:25 UTC), 이전 [#43774432171](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43774432171) (전날 23:22:13 UTC). 인접한 독립 schedule 2회 연속 성공은 입증되지 않음.
- 별도 OKX 원시 HTTP 본문 직접 대조, 최신 실행 원문 stdout↔저장 JSON 전체 SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 회차 미검증. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 14:42 KST
- 최신 13:16 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`(blob `6661e379f516b2457ab112a5dee3f4a6a1a41c78`), `.github/workflows/eth-oi-okx.yml`(blob `e83eda4680206efbc50952e4e0dde49a501a2c06`) 확인. OKX 공개 API 단일 ETH-USDT-SWAP의 `oiCcy`(ETH), 관측시각·300초 신선도 검사 및 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json` blob `70e42a582151e24eb056b255fd1316bf228f46d0`: **OKX ETH-USDT-SWAP 단일 거래소 OI 682159.019 ETH**, 거래소 관측 `2026-11-16T05:40:54.323Z` (14:40:54.323 KST), 수집 `05:40:54.406546Z`, 내부 `status=VERIFIED`. 직전 13:15 관측 이후 갱신. Binance 또는 전체 시장 OI가 아님.
- [#43811808375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43811808375) (05:40:48 UTC) 및 [#43811246242](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43811246242) (05:35:38 UTC) 모두 **보조 `workflow_run` success**. jobs API에서 각각 API 수집·신선도 검증·JSON 커밋 단계 success 확인. `event=schedule` 최근 100건 중 OKX 독립 성공 최신은 [#43795139612](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43795139612) (02:56:25 UTC), 이전 #43774432171 (전날 23:22:13 UTC): 인접 독립 예약 2회 연속 성공은 입증되지 않음.
- 별도 OKX 원시 HTTP 응답 직접 호출은 실행 환경 DNS 해석 오류로 실패. 최신 job stdout↔저장 JSON 전체 SHA 직접 대조 및 완성 ETH ESI 2.0 보고서 최신 실측 OI 반영도 미검증. jobs의 커밋 단계 성공만으로 신규 커밋 또는 stdout 일치를 단정하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 13:16 KST
- 직전 12:56 KST 체크포인트 확인 후 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py` (blob `6661e379f516b2457ab112a5dee3f4a6a1a41c78`), `.github/workflows/eth-oi-okx.yml` (blob `e83eda4680206efbc50952e4e0dde49a501a2c06`) 및 JSON을 직접 조회. OKX 공개 ETH-USDT-SWAP 단일 상품 `oiCcy`(ETH), 300초 신선도 검사, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존 확인.
- main `eth_oi_okx_latest.json` blob `e8162ed28829ee5da84b598902ed7e6e1b5497f4`: **OKX ETH-USDT-SWAP 단일 거래소 OI 677852.002 ETH**, 거래소 관측 `2026-11-16T04:15:50.167Z` (13:15:50.167 KST), 수집 `04:15:50.243417Z`, 내부 `status=VERIFIED`. 직전 12:55 관측 이후 갱신. Binance OI 또는 시장 전체 OI가 아님.
- 보조 [#43803011912](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43803011912) (04:15:43 UTC) 및 [#43802481712](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43802481712) (04:10:43 UTC) 모두 `workflow_run` success. 각각 jobs API에서 API 수집·신선도 검증·JSON 커밋 단계 success 확인. 새 독립 `schedule` 성공 [#43795139612](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43795139612) (02:56:25 UTC)도 jobs 단계 success 확인. 하지만 인접한 독립 예약 2회 연속 성공은 입증되지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 stdout↔저장 JSON 전체 SHA 직접 대조, 완성 ETH ESI 2.0 보고서 최신 실측 OI 반영은 미검증. jobs의 커밋 단계 success만으로 실제 신규 저장 커밋과 stdout 일치를 단정하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 12:56 KST
- 직전 11:38 KST 체크포인트 확인 후 OI 선행 게이트만 재검증. main의 `eth_oi_okx_latest.json` 거래소 관측 `2026-11-16T03:55:49.911Z` (12:55:49.911 KST), 수집 `03:55:50.015271Z`, **OKX ETH-USDT-SWAP 단일 거래소 OI 677425.789 ETH**, 내부 `status=VERIFIED`. 직전 11:35 관측 이후 갱신. Binance OI 또는 전체 시장 OI 아님.
- main `.github/workflows/eth-oi-okx.yml`의 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 설정 재확인. [#43801011924](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43801011924) (03:55:43 UTC), [#43800549827](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43800549827) (03:50:46 UTC)는 **모두 보조 workflow_run success**. 두 jobs API에서 API 수집·신선도 검증·JSON 커밋 단계 success 확인. 보조 성공을 독립 schedule 연속 성공으로 오인하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 독립 `schedule` 인접 2회 성공, 최신 stdout↔저장 JSON 전체 SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. JSON 내부 VERIFIED와 jobs success만으로 전체 OI 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 11:38 KST
- 직전 10:13 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py` 및 `.github/workflows/eth-oi-okx.yml` 확인: OKX ETH-USDT-SWAP 단일 거래소 공개 API, `oiCcy`(ETH), 관측시각·300초 신선도 검증, 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json` blob SHA `294c20f3fb2de3c7a0bd256546eee95ea507d6ac`: **OKX ETH-USDT-SWAP 단일 거래소 OI 674192.715000001 ETH**, 관측 `2026-11-16T02:35:49.321000+00:00` (11:35:49.321 KST), 수집 `2026-11-16T02:35:49.399139+00:00`, 내부 `status=VERIFIED`. 직전 10:11 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- [#43793119815](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43793119815) (02:35:42 UTC), [#43792636889](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43792636889) (02:30:56 UTC) 모두 **보조 `workflow_run` success**. 각 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 두 성공을 독립 `schedule` 연속 성공으로 인정하지 않음. 조회된 최근 5개 OKX 실행 모두 보조 실행.
- 미검증: 독립 `schedule` 인접 2회 연속 성공, 별도 OKX 원시 HTTP 본문 직접 대조, 최신 job stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서 최신 실측 OI 반영. 내부 `VERIFIED` 및 jobs 단계 success만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 10:13 KST
- 직전 09:43 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 점검. main 수집기 `eth_oi_okx_live.py`(blob `6661e379f516b2457ab112a5dee3f4a6a1a41c78`)와 워크플로 `.github/workflows/eth-oi-okx.yml`(blob `e83eda4680206efbc50952e4e0dde49a501a2c06`) 확인: OKX 공개 API 단일 ETH-USDT-SWAP `oiCcy`(ETH), 거래소 관측시각·300초 신선도 검사; 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json` blob `f20cdc0ed21d7918bf4f3e972b149804fdb9899e`: **OKX ETH-USDT-SWAP 단일 거래소 OI 671741.759000001 ETH**, 관측 `2026-11-16T01:11:12.082Z` (10:11:12.082 KST), 수집 `01:11:12.135053Z`, 내부 `status=VERIFIED`. 직전 09:41 관측보다 갱신. Binance 또는 시장 전체 OI가 아님.
- 보조 [#43784726695](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43784726695) (01:10:57 UTC) 및 [#43784204941](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43784204941) (01:05:47 UTC) 모두 `workflow_run` success. 최신 실행 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 단계 성공만으로 신규 커밋 또는 stdout↔저장 SHA 직접 일치가 입증되지는 않음.
- 최근 `event=schedule` 100건 중 OKX 독립 예약 성공 최신은 [#43774432171](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43774432171) (23:22:13 UTC), 이전 [#43750090961](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43750090961) (19:02:03 UTC). 인접 독립 예약 2회 연속 성공 미입증. 별도 OKX 원시 HTTP 본문 직접 대조, 최신 job stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서 최신 실측 반영 미검증.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 09:43 KST
- 직전 09:00 KST 체크포인트를 먼저 확인. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. 수집기는 OKX 공개 ETH-USDT-SWAP 단일 상품의 `oiCcy`(ETH) 및 300초 신선도 검사. 워크플로에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main JSON blob SHA `7475e714b97bb43b60890b475266837ccc720f32`: **OKX ETH-USDT-SWAP 단일 거래소 OI 671499.235 ETH**, 거래소 관측 `2026-11-16T00:41:00.529Z` (09:41:00.529 KST), 수집 `00:41:00.581673Z`, 내부 `status=VERIFIED`. 직전 08:55:50.773 KST 관측 이후 갱신. Binance 또는 전체 시장 OI 아님.
- 보조 `workflow_run` [#43781806487](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43781806487) (00:40:52 UTC), [#43781298021](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43781298021) (00:35:43 UTC) success. #43781806487의 수집·신선도·JSON 커밋 단계 success 확인. 성공 단계가 반드시 신규 커밋 생성 및 출력 SHA 일치를 증명하지는 않음.
- 최근 `event=schedule` 100건의 OKX 독립 예약 성공 최신은 #43774432171 (23:22:13 UTC), 이전 #43750090961 (19:02:03 UTC). 인접 독립 예약 2회 연속 성공 미입증. 별도 OKX 원시 HTTP 본문 직접 대조, 최신 job 원문 출력↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 실측 반영도 미검증.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 09:00 KST
- 07:29 KST 최신 체크포인트를 먼저 확인하고 main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재검증. 공개 OKX API `ETH-USDT-SWAP`의 `oiCcy` ETH, 관측시각 및 300초 신선도 검사 로직 유지. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main JSON blob SHA `b2e0e8e4d6cc831843500e546467eb5ab5f18676`: **OKX ETH-USDT-SWAP 단일 거래소 OI 667638.512 ETH**, 거래소 관측 `2026-11-15T23:55:50.773Z` (08:55:50.773 KST), 수집 `23:55:50.828308Z`, 내부 `status=VERIFIED`. 이전 07:25 관측보다 갱신. Binance OI 또는 시장 전체 OI가 아님.
- 보조 `workflow_run` [#43777420308](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43777420308) (23:55:42 UTC) 및 [#43776992726](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43776992726) (23:50:47 UTC) 모두 success. 두 실행 jobs API에서 API 수집·출력 신선도 검사·JSON 커밋 단계 success 확인. 독립 schedule 연속 성공으로 인정하지 않음.
- 새로운 독립 `schedule` 성공 [#43774432171](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43774432171) (23:22:13 UTC), jobs 단계 모두 success 확인. 이전 독립 성공 #43750090961 (19:02:03 UTC)과 인접 5분 실행이 아니므로 독립 예약 2회 연속 성공 미입증.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 job stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서에 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 07:29 KST
- 직전 06:16 KST 체크포인트를 먼저 확인하고 OI 전체 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 재조회. collector는 OKX 공개 API의 단일 `ETH-USDT-SWAP` `oiCcy`(ETH), API code=0, 거래소 관측시각, 300초 신선도 검사. workflow에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main 최신 JSON blob SHA `3d5e8cfe4ae68490c40f56452946c702603aa331`: **OKX ETH-USDT-SWAP 단일 거래소 OI 670581.455 ETH**, 관측 `2026-11-15T22:25:56.722Z` (07:25:56.722 KST), 수집 `22:25:56.816298Z`, 내부 `status=VERIFIED`. 직전 06:10 관측보다 갱신. Binance OI나 전체 시장 OI가 아님.
- 최신 보조 `workflow_run` [#43769243077](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43769243077) (22:25:48 UTC) 및 [#43768764680](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43768764680) (22:20:40 UTC) 모두 success. 이는 독립 schedule의 인접 2회 성공이 아님.
- 최근 전체 `event=schedule` 목록에서 OKX 독립 예약 성공 최신은 [#43750090961](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43750090961) (19:02:03 UTC), 그 이전 [#43713612207](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43713612207) (12:23:42 UTC). 인접한 독립 예약 2회 연속 성공은 미입증. 별도 OKX 원시 HTTP 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영도 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 06:16 KST
- 직전 06:02 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 수집기, 워크플로 및 JSON 확인: OKX 공개 API ETH-USDT-SWAP 단일 거래소 `oiCcy`(ETH), 300초 신선도 검사; 독립 `schedule`과 보조 `workflow_run` 병존.
- main JSON blob SHA `b2c6f71a1c0729cff8b846b4bc84efef24afbdc3`: **OKX ETH-USDT-SWAP 단일 거래소 OI 670444.661 ETH**, 거래소 관측 `2026-11-15T21:10:59.129Z` (06:10:59.129 KST), 수집 `21:10:59.213881Z`, 내부 `status=VERIFIED`. 06:01 관측 이후 갱신. Binance 또는 전체 시장 OI 아님.
- 보조 `workflow_run` [#43762221791](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43762221791) (21:10:46 UTC), [#43761732661](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43761732661) (21:05:41 UTC) 모두 success. 21:15:47 UTC 보조 실행 #43762696948은 조회 당시 in_progress. 독립 예약 2회 연속 성공 증거가 아님.
- 최근 `event=schedule` 조회의 OKX 독립 예약 성공은 #43750090961 (19:02:03 UTC) 등이며 인접한 2회 연속 성공은 확인되지 않음. 별도 OKX 원시 HTTP 본문 교차검증, 최신 job stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 실측 OI 반영은 미검증.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 06:02 KST
- 최신 04:51 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), 관측시각, 300초 신선도 검증 로직과 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main 최신 JSON blob SHA `88e4f7906bea483e6df2340981f7dddda5e4fd86`: **OKX ETH-USDT-SWAP 단일 거래소 OI 670075.426 ETH**, 거래소 관측 `2026-11-15T21:01:10.830Z` (06:01:10.830 KST), 수집 `21:01:10.888957Z`, 내부 `status=VERIFIED`. 직전 04:51 관측보다 갱신. Binance OI 또는 시장 전체 OI 아님.
- 보조 `workflow_run` [#43761264560](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43761264560) (21:01:01 UTC) 및 [#43760782320](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43760782320) (20:55:42 UTC) 모두 success. 두 실행 jobs API에서 수집·신선도 검사·JSON 커밋 단계 success 확인. 단계 성공만으로 새 커밋 발생이나 로그↔저장 SHA 일치가 입증되지는 않음.
- 최근 전체 `event=schedule` 100건의 OKX 독립 예약 성공 최신은 [#43750090961](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43750090961) (19:02:03 UTC), 이전 #43713612207 (12:23:42 UTC). **인접 독립 예약 2회 연속 성공 미입증**.
- 별도 OKX 원시 HTTP 응답 본문 대조, 최신 job stdout↔저장 JSON 전체 SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED와 보조 실행 성공만으로 OI 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 04:51 KST
- 최신 03:22 KST 체크포인트를 먼저 읽고 OI 전체 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 직접 확인. OKX 공개 API `ETH-USDT-SWAP`의 `oiCcy`(ETH), 관측시각 및 300초 신선도 검사 로직 유지. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main JSON blob SHA `98720b31889ec825ca4fb8c0f9e253ca6f706a31`: **OKX ETH-USDT-SWAP 단일 거래소 OI 674247.018 ETH**, 거래소 관측 `2026-11-15T19:51:03.941Z` (04:51:03.941 KST), 수집 `19:51:03.993773Z`, 내부 `status=VERIFIED`. 이전 03:20 관측보다 갱신. Binance OI나 시장 전체 OI가 아님.
- 보조 `workflow_run` [#43754688258](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43754688258) (19:50:48 UTC) 및 [#43754219612](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43754219612) (19:45:47 UTC) 모두 success. jobs API에서 수집·신선도 검사·JSON 커밋 단계 success 확인. 이 두 실행은 독립 schedule이 아님.
- 새 독립 `schedule` 성공 [#43750090961](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43750090961) (19:02:03 UTC) 확인, 해당 jobs 단계도 success. 직전 독립 예약 성공 #43713612207 (12:23:42 UTC)과 인접 5분 실행이 아니므로 **독립 schedule 인접 2회 연속 성공은 여전히 미입증**.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 job 원문 stdout↔저장 JSON 전체 SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED 및 단계 success만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 03:22 KST
- 직전 03:00 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 OKX OI JSON과 workflow 정의 확인: 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 676355.381 ETH**, 거래소 관측 `2026-11-15T18:20:58.533Z` (03:20:58.533 KST), 수집 `18:20:58.589474Z`, 내부 `status=VERIFIED`. 직전 02:55 관측 이후 갱신. Binance OI나 전체 시장 OI 아님.
- [#43746234366](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43746234366) (18:20:48 UTC), [#43745760875](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43745760875) (18:15:54 UTC) 모두 **보조 `workflow_run` success**. 두 jobs API에서 API 수집, 출력 신선도 검사, JSON 저장 단계 success 확인. 이는 독립 schedule 연속 성공을 증명하지 않음.
- `event=schedule` 최근 100건 중 OKX 독립 예약 성공 최근 2건은 [#43713612207](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43713612207) (12:23:42 UTC), [#43678396890](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43678396890) (04:49:05 UTC). 인접 독립 예약 2회 연속 성공은 미입증.
- 별도 OKX 원시 HTTP 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이번에는 상태 문서만 수정하며 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 03:00 KST
- 직전 01:12 KST 체크포인트 확인 후 OI 선행 게이트만 점검. main 워크플로는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병용. OKX ETH-USDT-SWAP 단일 거래소 OI만 대상.
- main `eth_oi_okx_latest.json`: **676164.872 ETH**, 거래소 관측 `2026-11-15T17:55:56.362Z` (02:55:56.362 KST), 수집 `17:55:56.415329Z`, 내부 `status=VERIFIED`. 직전 01:11 관측 이후 갱신. Binance OI나 시장 전체 OI 아님.
- 보조 `workflow_run` [#43743842355](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43743842355) (17:55:47 UTC) 및 [#43743397287](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43743397287) (17:50:54 UTC) 모두 success. 보조 실행은 독립 schedule의 연속 성공 증거가 아님.
- 별도 OKX 원시 HTTP 응답 직접 교차검증, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 독립 schedule 인접 2회 성공, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 01:12 KST
- 직전 00:35 KST 체크포인트를 먼저 확인하고 OI 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 수집기는 OKX 공개 ETH-USDT-SWAP 응답의 `oiCcy`(ETH), 거래소 관측시각 및 300초 신선도 검사를 수행하며 워크플로는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`을 병용.
- main JSON blob SHA `8e4b73ccee729d73315c898cbaa3d9daccef7a3b`: **OKX ETH-USDT-SWAP 단일 거래소 OI 685943.543 ETH**, 거래소 관측 `2026-11-15T16:11:02.367Z` (01:11:02.367 KST), 수집 `16:11:02.477399Z`, 내부 `status=VERIFIED`. 00:35 관측 이후 갱신. Binance OI 또는 시장 전체 OI 아님.
- [#43734010801](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43734010801) (16:10:54 UTC), [#43733514184](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43733514184) (16:05:40 UTC) 모두 **보조 `workflow_run` success**; jobs API에서 수집·신선도 검증·커밋 단계 모두 success. 직전 미확정 [#43730760046](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43730760046)도 success로 확정. 단계 success는 신규 커밋이나 출력↔저장 SHA 직접 일치를 보장하지 않음.
- 최근 조회된 `event=schedule` 100건의 OKX OI 독립 예약 성공은 #43713612207 (12:23:42 UTC), #43678396890 (04:49:05 UTC) 등이며, **인접 독립 예약 2회 연속 성공은 미입증**. 다른 OKX Funding/Futures CVD 워크플로의 독립 예약 성공은 OI의 성공으로 계산하지 않음.
- 별도 OKX 원시 HTTP 응답 본문 직접 교차검증, 최신 job stdout↔저장 JSON 전체 SHA 대조, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. 보고서 호출 규칙의 OKX OI 참조 조항만 확인했으며 완성 보고서 반영으로 간주하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 복구 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 이번 변경은 상태 문서만이며 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-16 00:35 KST
- 직전 2026-11-15 23:47 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. 수집기는 OKX 공개 ETH-USDT-SWAP `oiCcy`(ETH), 거래소 관측시각 및 300초 신선도 검사를 수행하며 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main 최신 JSON blob SHA `236dc0c9979c59ba648e8997108a0e3cffa4daab`: **OKX ETH-USDT-SWAP 단일 거래소 OI 685261.361 ETH**, 관측 `2026-11-15T15:35:52.693000+00:00` (00:35:52.693 KST), 수집 `2026-11-15T15:35:52.744603+00:00`, 내부 `status=VERIFIED`. 이전 23:46 KST 관측보다 갱신됨. Binance OI나 시장 전체 OI 아님.
- [#43730312010](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43730312010) (15:31:04 UTC) 및 [#43729821379](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43729821379) (15:25:43 UTC)는 보조 `workflow_run` success. [#43730760046](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43730760046) (15:35:44 UTC)는 조회 시 완료 결론 없음. 보조 성공을 독립 예약 성공으로 간주하지 않음.
- 최근 `event=schedule` 100건 중 OKX 독립 예약 성공은 #43713612207 (12:23:42 UTC), #43678396890 (04:49:05 UTC) 등이며 인접한 독립 예약 2회 연속 성공 미입증.
- 별도 OKX 원시 HTTP 응답 본문 대조, 이번 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영 미검증. 내부 VERIFIED는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 23:47 KST
- 직전 22:47 KST 체크포인트를 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 직접 확인. OKX 공개 API ETH-USDT-SWAP의 `oiCcy`(ETH), 거래소 관측시각, 300초 신선도 검증과 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 설정 유지.
- main JSON blob SHA `0ee77dcce48ece04dd9edd12a5376f1bf9411d4a`: **OKX ETH-USDT-SWAP 단일 거래소 OI 683136.495 ETH**, 거래소 관측 `2026-11-15T14:46:11.546Z` (23:46:11.546 KST), 수집 `14:46:11.627101Z`, 내부 `status=VERIFIED`. 22:45 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- [#43726140948](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43726140948) (14:46:03 UTC) 및 [#43725676675](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43725676675) (14:40:56 UTC) 모두 **보조 `workflow_run` success**. 두 실행의 jobs API에서 수집·신선도 검사·JSON 커밋 단계 success 확인. 단계 성공은 실제 신규 커밋이나 전체 SHA 대조의 직접 증거가 아님.
- `event=schedule` 최근 100건에서 OKX 독립 예약 최근 성공은 [#43713612207](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43713612207) (12:23:42 UTC), 이전 [#43678396890](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43678396890) (04:49:05 UTC). 인접 독립 예약 2회 연속 성공 미입증.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영 미검증. 내부 VERIFIED 및 보조 실행 성공만으로 전체 OI 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이번 변경은 상태 문서만이며 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 22:47 KST
- 최신 21:50 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. 공개 OKX API `ETH-USDT-SWAP`의 `oiCcy`(ETH), 관측시각, 300초 신선도 검사 및 독립 `schedule: 2-59/5 * * * *` + 보조 `workflow_run` 설정 유지.
- main JSON blob SHA `c6589a5e4e979809e5f2bdc6a5875d723784b9b4`: **OKX ETH-USDT-SWAP 단일 거래소 OI 682428.332 ETH**, 거래소 관측 `2026-11-15T13:45:58.847Z` (22:45:58.847 KST), 수집 `13:45:58.902355Z`, 내부 `status=VERIFIED`. 21:45 관측 대비 갱신됨. Binance OI 또는 전체 시장 OI가 아님.
- 최신 [#43720684474](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43720684474) (13:45:49 UTC) 및 [#43720257727](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43720257727) (13:40:52 UTC) 모두 **보조 `workflow_run` success**. 최근 전체 실행 30건의 OKX 5건 모두 보조 실행.
- `event=schedule` 최근 100건에서 새로 확인된 OKX 독립 예약 성공 [#43713612207](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43713612207) (12:23:42 UTC). 직전 확인된 독립 성공 [#43678396890](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43678396890) (04:49:05 UTC)과 5분 간격 인접 실행이 아니므로 **독립 예약 2회 연속 성공 미입증**.
- 이번 회차 별도 OKX 원시 HTTP 응답 직접 대조, 최신 job stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. API 코드 및 저장 JSON의 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 이번 변경은 상태 문서만이며 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 21:50 KST
- 직전 20:27 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 점검. main의 `.github/workflows/eth-oi-okx.yml`에는 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run`이 병존함.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 681479.942 ETH**, 거래소 관측 `2026-11-15T12:45:56.668Z` (21:45:56.668 KST), 수집 `12:45:56.739539Z`, 내부 `status=VERIFIED`. 직전 20:26 관측 이후 갱신. Binance OI 또는 시장 전체 OI 아님.
- 최근 [#43715486024](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43715486024) (12:45:47 UTC), [#43715075664](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43715075664) (12:40:51 UTC)는 모두 **보조 `workflow_run` success**. 각각 jobs API에서 API 수집·신선도 검증·JSON 저장 단계 success 확인. 이는 독립 예약의 인접 2회 연속 성공을 입증하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 stdout↔저장 JSON 전체 SHA 대조, 독립 `schedule` 인접 2회 연속 성공, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED 및 보조 실행 성공만으로 OI 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 20:27 KST
- 19:48 KST 체크포인트를 먼저 읽고 OI 게이트만 점검. main 수집기 `eth_oi_okx_live.py`와 워크플로 `.github/workflows/eth-oi-okx.yml` 확인: OKX public `ETH-USDT-SWAP`의 `oiCcy`(ETH), 300초 신선도 검사, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main `eth_oi_okx_latest.json` blob SHA `ef4aaa5b631bcaa11b6cce5d2ba847d6856f9690`: **OKX 단일 거래소 ETH-USDT-SWAP OI 681802.614 ETH**, 거래소 관측 `2026-11-15T11:26:01.761Z` (20:26:01.761 KST), 수집 `11:26:01.856774Z`, 내부 `status=VERIFIED`. 이전 19:45:56 관측 이후 갱신. Binance OI 또는 전체 시장 OI 아님.
- GitHub Actions 최근 [#43708874607](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43708874607) (11:25:46 UTC) 및 [#43708483781](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43708483781) (11:20:53 UTC)은 모두 **보조 `workflow_run` success**. 최근 30개 전체 실행 목록에 나타난 OKX 실행 5건 모두 보조 실행. 독립 예약의 연속 성공으로 인정하지 않음.
- `event=schedule` 최근 100건에서 OKX 독립 예약 성공은 최근 [#43678396890](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43678396890) (04:49:05 UTC), 이전 [#43655293571](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43655293571) (전일 23:51:20 UTC). 인접 5분 독립 예약 2회 연속 성공 미입증.
- 이번 회차 별도 OKX 원시 HTTP 본문 직접 대조, 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED와 보조 실행 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 이번 변경은 상태 문서만이며 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 19:48 KST
- 최신 18:51 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py` 및 `.github/workflows/eth-oi-okx.yml` 확인: OKX 공개 API ETH-USDT-SWAP 단일 거래소 `oiCcy` ETH, 300초 신선도 검사, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 유지.
- main `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 681885.221 ETH**, 거래소 관측 `2026-11-15T10:45:56.271Z` (19:45:56.271 KST), 수집 `10:45:56.342229Z`, 내부 `status=VERIFIED`. 직전 18:51 관측 이후 갱신. Binance OI 또는 시장 전체 OI 아님.
- [#43705637411](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43705637411) (10:45:47 UTC)와 [#43705243653](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43705243653) (10:40:48 UTC) 모두 **보조 `workflow_run` success**. 두 실행의 jobs API에서 API 수집·출력 신선도 검증·JSON 커밋 단계 success 확인. 단계 성공만으로 신규 커밋과 로그↔저장 전체 SHA 대조를 입증하지 않음.
- 최근 조회된 실행 5건은 모두 보조 `workflow_run`. **독립 `schedule` 인접 2회 연속 성공 미입증**. 별도 OKX 원시 HTTP 응답 본문 대조, 최신 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영도 미검증.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이번 변경은 상태 문서만이며 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 18:51 KST
- 직전 17:22 KST 체크포인트를 확인하고 OI 게이트만 점검. main의 수집 코드 및 workflow 설정은 OKX 공개 API `ETH-USDT-SWAP` 단일 거래소 `oiCcy`(ETH), 300초 신선도 검증, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`을 유지함.
- main `eth_oi_okx_latest.json` blob SHA `cb8bc33b3b9e4255f2648171059c01353076b2d4`: **OKX ETH-USDT-SWAP 단일 거래소 OI 680053.262 ETH**, 거래소 관측 `2026-11-15T09:51:00.472Z` (18:51:00.472 KST), 수집 `09:51:00.529251Z`, 내부 `status=VERIFIED`. 이전 17:20 관측 대비 갱신됨. Binance 또는 전체 시장 OI 아님.
- [#43701198403](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43701198403) (09:50:49 UTC), [#43700801654](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43700801654) (09:45:51 UTC) 모두 **보조 `workflow_run` success**. 각각 jobs API의 API 수집·신선도 검증·JSON 커밋 단계 success 확인. 단계 성공만으로 신규 저장 커밋이나 전체 JSON SHA 일치 입증 불가.
- `event=schedule` 최근 100건의 OKX 독립 예약 성공 최근 [#43678396890](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43678396890) (04:49:05 UTC), 이전 [#43655293571](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43655293571) (전일 23:51:20 UTC). **인접 5분 독립 예약 2회 연속 성공 미입증**.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 이번 변경은 상태 문서에만 한정하고 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터를 변경하지 않음.

## 자동 복구 점검 — 2026-11-15 17:22 KST
- 16:34 KST 최신 체크포인트를 먼저 확인하고 OI 선행 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 직접 조회. OKX 공개 API의 ETH-USDT-SWAP 단일 거래소 `oiCcy`(ETH) 및 300초 신선도 검증 코드, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 구성 유지.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 682234.762 ETH**, 관측 `2026-11-15T08:20:59.574Z` (17:20:59.574 KST), 수집 `08:20:59.646542Z`, 내부 `status=VERIFIED`. 이전 16:31 관측 이후 갱신. Binance OI 또는 시장 전체 OI 아님.
- [#43694068197](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43694068197) (08:20:50 UTC) 및 [#43693672722](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43693672722) (08:15:48 UTC)는 모두 보조 `workflow_run` success. 두 실행 jobs API에서 수집·신선도 검사·JSON 커밋 단계 success 확인. 단, 커밋 단계 성공만으로 신규 저장 또는 전체 SHA 동일성 입증 불가.
- `event=schedule` 최근 100건 중 OKX 독립 예약 성공 최근 [#43678396890](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43678396890) (04:49:05 UTC), 이전 [#43655293571](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43655293571) (23:51:20 UTC). 인접 5분 독립 예약 2회 연속 성공은 미입증. 보조 실행을 독립 예약으로 간주하지 않음.
- 별도 OKX 원시 HTTP 본문 직접 교차검증, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 16:34 KST
- 최신 15:45 KST 체크포인트를 먼저 확인하고 OI 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 및 보고서 호출 규칙을 재조회. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON blob SHA `dac56aafa1dce93abd15ebc5b3d7c6478a085dac`: **OKX ETH-USDT-SWAP 단일 거래소 OI 685793.107 ETH**, 거래소 관측 `2026-11-15T07:31:06.940Z` (16:31:06.940 KST), 수집 `07:31:06.993178Z`, 내부 `status=VERIFIED`. 이전 15:41 관측보다 갱신. Binance OI 또는 전체 시장 OI 아님.
- 보조 `workflow_run` [#43690275511](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43690275511) (07:30:54 UTC), [#43689899455](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43689899455) (07:25:42 UTC) 모두 success. jobs API에서 각각 API 수집, 신선도 검사, JSON 커밋 단계 success 확인. 단, 단계 success만으로 신규 저장 커밋이나 stdout↔저장 JSON 전체 SHA 동일성은 입증되지 않음.
- `event=schedule` 최근 100건 중 OKX 독립 예약 성공 최근 [#43678396890](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43678396890) (04:49:05 UTC), 그 이전 [#43655293571](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43655293571) (23:51:20 UTC). 인접한 5분 독립 예약 2회 연속 성공은 미입증. 보조 실행을 독립 예약으로 오인하지 않음.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영 미검증. 보고서 호출 규칙에 OI 참조 지시가 존재하는 것은 실제 보고서 반영 증거가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 15:45 KST
- 직전 14:30 KST 체크포인트를 먼저 확인. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`과 보고서 호출 규칙을 재조회. 수집기는 OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 관측시각 및 300초 신선도를 검증. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON blob SHA `2b5ae7971ce73bd71db236a2b7ec1fa44fa04418`: **OKX ETH-USDT-SWAP 단일 거래소 OI 682710.791 ETH**, 거래소 관측 `2026-11-15T06:41:08.260000+00:00` (15:41:08.260 KST), 수집 `06:41:08.313327Z`, 내부 `status=VERIFIED`. 직전 14:25 관측보다 갱신. Binance OI 또는 시장 전체 OI 아님.
- 보조 `workflow_run` [#43686546069](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43686546069) (06:40:51 UTC) 및 [#43686164617](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43686164617) (06:35:47 UTC) 모두 success. 두 실행의 jobs API에서 API 수집·신선도 검증·JSON 커밋 단계 success 확인. 단계 성공만으로 stdout↔JSON 전체 SHA 동일성은 입증되지 않음.
- 최근 `event=schedule` 100건에서 OKX 독립 예약 성공은 [#43678396890](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43678396890) (04:49:05 UTC), 이전 [#43655293571](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43655293571) (23:51:20 UTC). 인접한 5분 독립 schedule 2회 연속 성공 미입증. 보조 workflow_run을 독립 예약으로 간주하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 보고서 호출 규칙에 OKX OI 조회 지시가 존재하지만 실제 보고서 반영의 증거는 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 복구 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 14:30 KST
- 직전 13:22 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON **OKX ETH-USDT-SWAP 단일 거래소 OI 687744.775 ETH**, 거래소 관측 `2026-11-15T05:25:58.859Z` (14:25:58.859 KST), 수집 `05:25:58.934122Z`, 내부 `status=VERIFIED`, blob SHA `433f443634f424b525572f3ed4e904c888458e95`. 이전 13:20 관측보다 갱신. Binance OI나 전체 시장 OI가 아님.
- [#43681045499](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43681045499) (05:25:49 UTC), [#43680681331](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43680681331) (05:20:48 UTC) 모두 **보조 `workflow_run` success**. 두 실행의 API 수집·신선도 검증·JSON 저장 job 단계 success 확인. 최신 #43681045499의 원문 job 로그에 출력된 OI·관측·수집 시각·필드가 main JSON과 일치하고 로그에 저장 커밋 `225e5af` 및 `STORED` 확인. 전체 JSON blob SHA와 원시 HTTP 본문 독립 대조까지 확인한 것은 아님.
- `event=schedule` 최근 목록에서 OKX 독립 예약 성공 [#43678396890](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43678396890) (04:49:05 UTC) 확인. 그 이전은 [#43655293571](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43655293571) (전일 23:51:20 UTC). **인접 5분 독립 schedule 2회 연속 성공은 미입증**. GitHub schedule 지연·누락 여부 원인 미확정.
- 별도 OKX 원시 HTTP 응답 직접 교차검증 및 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영 미검증. collector 내부 VERIFIED와 보조 실행 성공만으로 전체 OI 게이트를 통과시키지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 복구 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 13:22 KST
- 최신 12:34 KST 체크포인트를 먼저 읽고 OI 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 686111.765 ETH**, 거래소 관측 `2026-11-15T04:20:58.361Z` (13:20:58.361 KST), 수집 `04:20:58.413387Z`, 내부 `status=VERIFIED`. 12:31 관측 이후 갱신. Binance OI 또는 시장 전체 OI가 아님.
- GitHub Actions [#43676355763](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43676355763) (04:20:48 UTC) 및 [#43675984087](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43675984087) (04:15:45 UTC) 모두 **보조 `workflow_run` success**. 두 실행의 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 독립 예약 2회 연속 성공의 증거는 아님. 이번 조회 최신 100개 전체 실행에서 OKX 독립 schedule의 인접 2회 성공 확인되지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서에 최신 실측 OI 반영은 미검증. `VERIFIED`는 collector 내부 상태이며 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 12:34 KST
- 직전 12:03 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 조회. 워크플로는 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 682151.239 ETH**, 거래소 관측 `2026-11-15T03:31:07.965Z` (12:31:07.965 KST), 수집 `03:31:08.048919Z`, 내부 `status=VERIFIED`, blob SHA `f4b7a1e6460cdb434788ed12154ed3793d741ee3`. 이전 12:01 관측 이후 갱신. Binance OI 또는 전체 시장 OI 아님.
- GitHub Actions 최근 [#43672709643](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43672709643) (03:31:01 UTC) 및 [#43672319703](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43672319703) (03:25:46 UTC)은 모두 `workflow_run` success. 이는 독립 schedule 인접 2회 성공의 증거가 아님.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 실행 stdout↔저장 JSON 전체 SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 점검에서 미검증. 독립 schedule의 인접 2회 연속 성공도 미입증. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 12:03 KST
- 최신 10:21 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 수집기는 OKX 공개 API의 단일 `ETH-USDT-SWAP` `oiCcy`(ETH), 응답 code=0, 거래소 관측시각과 300초 신선도를 검사하며 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run`이 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 680268.144 ETH**, 거래소 관측 `2026-11-15T03:01:22.137Z` (12:01:22.137 KST), 수집 `03:01:22.218759Z`, 내부 `status=VERIFIED`, blob SHA `9373b3921d0092ebc3228198dc074cc76c4a528c`. 10:21 관측보다 갱신됨. Binance OI나 시장 전체 OI 아님.
- 보조 `workflow_run` [#43670417826](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43670417826) (03:01:13 UTC) 및 [#43670014340](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43670014340) (02:55:43 UTC) 모두 success. 두 실행의 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 그러나 `Commit` 단계 success만으로 신규 커밋 생성 및 stdout↔저장 JSON 전체 SHA 일치를 확정하지 않음.
- 최근 전체 `event=schedule` 100건에서 OKX 독립 예약 성공은 [#43655293571](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43655293571) (23:51:20 UTC) 및 [#43635097141](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43635097141) (20:00:07 UTC). 인접 5분 독립 예약 2회 연속 성공은 미입증. 보조 실행과 구분.
- 별도 OKX 원시 HTTP 직접 요청은 DNS `Temporary failure in name resolution`로 실패. 최신 실행 원문↔저장 JSON 전체 SHA 직접 대조 및 완성 ETH ESI 2.0 보고서의 실측 OI 반영도 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 10:21 KST
- 최신 10:09 KST 체크포인트를 먼저 확인하고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. 수집 코드는 OKX 공개 API `ETH-USDT-SWAP` 단일 상품의 `oiCcy`(ETH), `code=0`, 거래소 관측시각, 300초 신선도 검사를 수행. 워크플로에는 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run`이 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 688725.996 ETH**, 관측 `2026-11-15T01:21:04.142Z` (10:21:04.142 KST), 수집 `01:21:04.218492Z`, 내부 `status=VERIFIED`, blob SHA `91edbbfb9a748c5fcb8c00dcd3369d9b76f3ccee`. 직전 10:06 관측 이후 갱신. Binance OI나 전체 시장 OI가 아님.
- Actions 최근 보조 `workflow_run` [#43662665047](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43662665047) (01:20:54 UTC)와 [#43662261642](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43662261642) (01:15:53 UTC)는 모두 `success`. 최근 전체 `event=schedule` 100건 중 OKX 독립 예약 성공은 [#43655293571](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43655293571) (23:51:20 UTC), 이전 [#43635097141](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43635097141) (20:00:07 UTC). **인접 독립 예약 2회 연속 성공은 미입증**. 보조 실행 성공을 독립 예약 성공으로 오인하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 교차검증, 이번 실행의 원문 로그↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED 및 Actions 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 10:09 KST
- 최신 체크포인트(08:53 KST)를 먼저 확인하고 OI 선행 게이트만 재검증. `eth_oi_okx_live.py`는 OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 거래소 관측시각 및 300초 신선도를 검증. 워크플로는 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run`을 함께 정의.
- main 최신 `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 684784.545 ETH**, 거래소 관측 `2026-11-15T01:06:03.662Z` (10:06:03.662 KST), 수집 `01:06:03.744393Z`, 내부 `VERIFIED`, blob SHA `85e4288354003de84a41cdc15aed92848a9fa579`. 이전 08:51 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- 보조 `workflow_run` [#43661438391](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43661438391) (01:05:57 UTC)와 [#43661025113](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43661025113) (01:00:59 UTC)는 모두 success. jobs API에서 수집·신선도 검증·커밋 단계 모두 success 확인. 단, 이 둘은 독립 schedule이 아님.
- 최근 `event=schedule` 100건에서 OKX 독립 예약 성공은 [#43655293571](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43655293571) (23:51:20 UTC), 이전 [#43635097141](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43635097141) (20:00:07 UTC). **인접 독립 예약 2회 연속 성공은 미입증**.
- 별도 OKX 원시 HTTP 응답 본문 직접 교차검증, 최신 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. job 단계 성공과 collector 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 이번에는 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 08:53 KST
- 최신 체크포인트 확인 후 OI 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. OKX 공개 API 단일 ETH-USDT-SWAP의 `oiCcy`(ETH), `code=0`, 관측시각 및 300초 신선도 검증 코드 유지. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 설정 확인.
- main JSON의 **OKX ETH-USDT-SWAP 단일 거래소 OI 683739.694 ETH**, 거래소 관측 `2026-11-14T23:51:28.673Z` (08:51:28.673 KST), 수집 `23:51:28.729571Z`, 내부 `VERIFIED`, blob SHA `8e9b205c19a3c1b7dfc7101412fb9f762cb5af2e`. 이전 07:46 관측보다 갱신. Binance OI 또는 시장 전체 OI 아님.
- 새 독립 `event=schedule` [#43655293571](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43655293571) (23:51:20 UTC / 08:51:20 KST) **success**, jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 모두 success. 이전 독립 예약 성공 [#43635097141](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43635097141) (20:00:07 UTC)과는 약 3시간 51분 간격이므로 **인접한 5분 독립 예약 2회 연속 성공은 여전히 미입증**. 보조 workflow_run과 구분.
- 별도 OKX 원시 HTTP 응답 직접 교차검증, 최신 실행 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. job 단계 성공은 전체 게이트 통과의 충분조건이 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 06:20 KST

## 자동 복구 점검 — 2026-11-15 07:47 KST
- 최신 체크포인트를 먼저 읽고 OI 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 재조회. 공개 OKX ETH-USDT-SWAP 단일 거래소 OI 수집, 응답 code=0·관측시각·300초 신선도 검증 로직 및 독립 `schedule: 2-59/5 * * * *` + 보조 `workflow_run` 설정 유지.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 680698.840 ETH**, 거래소 관측 `2026-11-14T22:46:04.030Z` (07:46:04.030 KST), 수집 `22:46:04.090526Z`, `status=VERIFIED`, blob SHA `550c24b74f9dfbe1ede191465ce8c67a141437b5`. 이전 06:16 관측보다 갱신. Binance OI 또는 시장 전체 OI 아님.
- 보조 `workflow_run` [#43649787205](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43649787205) (22:45:55 UTC) 및 [#43649353146](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43649353146) (22:40:53 UTC) 모두 success; jobs API에서 API 수집·신선도 검증·커밋 단계 각각 success. 단계 성공만으로 각 실행의 신규 커밋이나 전체 SHA 대조를 입증하지 않음.
- 최근 `event=schedule` 100건 중 OKX 독립 예약 성공 [#43635097141](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43635097141) (20:00:07 UTC)과 이전 [#43609708642](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43609708642) (15:21:04 UTC) 확인. **인접 5분 독립 예약 2회 연속 성공 미입증**.
- 별도 OKX 원시 HTTP 응답 본문 교차검증, 최신 실행 원문 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

- 직전 05:49 KST 체크포인트를 먼저 확인. `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 재조회. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존하고 수집기는 OKX 공개 API의 ETH-USDT-SWAP 단일 상품 `oiCcy`(ETH), 응답 코드, 관측시각, 300초 신선도를 검증.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 680693.275 ETH**, 관측 `2026-11-14T21:16:08.370Z` (06:16:08.370 KST), 수집 `21:16:08.445872Z`; 05:46 관측보다 갱신. Binance 또는 전체 시장 OI 아님.
- 보조 `workflow_run` [#43641888110](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43641888110) (21:16 UTC), [#43641440093](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43641440093) (21:11 UTC) 모두 success. 최신 실행 job 원문 로그에서 수집·신선도 PASS와 `STORED` 커밋 `7588aa3` 확인. 로그 출력의 관측시각·OI·USD·수집시각이 main JSON과 일치. 저장 JSON의 전체 SHA 및 별도 OKX 원시 HTTP 본문 직접 대조는 미완료.
- 최근 `event=schedule` 목록의 OKX 독립 예약 성공 [#43635097141](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43635097141) (20:00:07 UTC) 및 이전 [#43609708642](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43609708642) (15:21:04 UTC). 인접 5분 간격 독립 schedule 2회 연속 성공은 입증되지 않음. 최신 독립 실행의 수집·신선도·저장 job 단계는 모두 success.
- 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영 미검증. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 05:49 KST
- 최신 04:17 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 재조회. 수집기는 OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), 응답 코드 및 거래소 관측시각·300초 신선도를 검사함. 워크플로에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 707463.435 ETH**, 거래소 관측 `2026-11-14T20:46:04.873Z` (05:46:04.873 KST), 수집 `20:46:04.925024Z`, 내부 `VERIFIED`, blob SHA `2d62015a139f24059d555f5ef42c191bf063de41`. 04:15 관측 이후 갱신됨. Binance OI 또는 시장 전체 OI 아님.
- Actions [#43639208189](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43639208189) (20:45:50 UTC) 및 [#43638764005](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43638764005) (20:40:47 UTC)는 모두 **보조 `workflow_run` success**. jobs API에서 두 실행의 API 수집·신선도 검증·JSON 커밋 단계 success 확인. 단계 성공만으로 실제 신규 커밋이나 stdout↔저장 JSON SHA 동일성을 입증하지 않음.
- 추가로 **독립 `schedule` 실행 [#43635097141](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43635097141)** (20:00:07 UTC, 05:00:07 KST) success 및 jobs의 세 단계 success 확인. 이전 독립 schedule 성공은 [#43609708642](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43609708642) (15:21:04 UTC). 독립 예약의 인접 2회 연속 성공은 여전히 미입증.
- 별도 OKX 원시 HTTP 응답 직접 교차검증, 최신 job 원문 stdout↔저장 JSON 전체 SHA 대조, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 `VERIFIED`는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이번에는 상태 문서만 수정하고 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 04:17 KST
- 직전 03:44 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. OKX 공개 API ETH-USDT-SWAP 단일 상품 `oiCcy`(ETH), 응답 코드·관측시각·300초 신선도 검사 구현 및 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 설정 확인.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 705743.700 ETH**, 거래소 관측 `2026-11-14T19:15:52.964Z` (04:15:52.964 KST), 수집 `19:15:53.035406Z`, 내부 `VERIFIED`, blob SHA `be76d837f8f9dce21bba924925dd345a45b15768`. 03:40 관측보다 갱신됨. Binance OI나 시장 전체 OI가 아님.
- Actions [#43631123242](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43631123242) (19:15:45 UTC) 및 [#43630665769](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43630665769) (19:10:45 UTC) 모두 **보조 `workflow_run` success**. 두 실행 jobs API의 API 수집·신선도 검사·JSON 저장 단계 success 확인. 이는 독립 예약 실행 2회 연속 성공 증거가 아님.
- 최근 전체 `event=schedule` 100건 중 가장 최근 OKX 독립 예약 성공은 [#43609708642](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43609708642) (15:21:04 UTC), 이전 [#43576665342](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43576665342) (08:36:59 UTC). **인접한 독립 schedule 2회 연속 성공 미입증**.
- 별도 환경에서 OKX 원시 HTTP 호출을 시도했으나 DNS 이름 해석 실패. 최신 job stdout↔저장 JSON 전체 SHA 직접 대조, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 03:44 KST
- 직전 02:19 KST 체크포인트를 먼저 읽고 OI 전체 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`, 보고서 호출 규칙을 재조회. 수집기는 OKX 공개 API 단일 ETH-USDT-SWAP `oiCcy`(ETH), `code=0`, 관측시각 및 300초 신선도 검사 구현. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 설정 유지.
- main JSON의 **OKX ETH-USDT-SWAP 단일 거래소 OI 704832.441 ETH**, 관측 `2026-11-14T18:40:50.096000+00:00` (03:40:50.096 KST), 수집 `18:40:50.176909Z`, 내부 `VERIFIED`, blob SHA `da08315f2aa7dea9afbf6577bd543643254b2cae`. 직전 02:15 관측보다 갱신. Binance OI 또는 전체 시장 OI 아님.
- Actions [#43627935446](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43627935446) (18:40:43 UTC), [#43627466168](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43627466168) (18:35:39 UTC) 모두 **보조 `workflow_run` success**. 최신 실행 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 이는 독립 schedule 2회 연속 성공 증거가 아님.
- 최근 전체 `event=schedule` 100건 조회에서 가장 최근 독립 OKX 예약 성공은 [#43609708642](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43609708642) (15:21:04 UTC), 그 전 [#43576665342](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43576665342) (08:36:59 UTC). **독립 예약 인접 2회 연속 성공 미입증**.
- 별도 OKX 원시 HTTP 응답 직접 교차검증, 최신 job stdout↔저장 JSON 전체 SHA 직접 대조, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 보고서 호출 규칙에 OKX 단일 거래소 OI 참조 조항이 있으나 실제 보고서 반영 증거는 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이번에는 상태 문서만 갱신하며 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 02:19 KST
- 직전 02:06 KST 체크포인트를 먼저 읽고 OI 전체 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 재조회. collector의 OKX 공개 API `ETH-USDT-SWAP` 단일 상품 `oiCcy`(ETH), 응답 `code=0`, 거래소 관측시각 및 300초 신선도 검사 구현 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON **OKX ETH-USDT-SWAP 단일 거래소 OI 707339.047 ETH**, 거래소 관측 `2026-11-14T17:15:52.375Z` (02:15:52.375 KST), 수집 `17:15:52.474148Z`, 내부 `VERIFIED`, blob SHA `1a467af981d1faca4f88636ae7b6e8adf2bb3aec`. 이전 02:06 관측 이후 갱신. Binance OI나 시장 전체 OI 아님.
- Actions [#43620129804](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43620129804) (17:15:45 UTC), [#43619688939](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43619688939) (17:10:51 UTC) 모두 **보조 `workflow_run` success**. 각 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 이는 독립 `schedule`의 인접 2회 연속 성공 증거가 아님.
- **미검증:** 독립 예약 2회 연속 성공, 별도 OKX 원시 HTTP 응답 본문 직접 교차검증, 이번 실행 원문 stdout↔저장 JSON 전체 SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영. collector 내부 VERIFIED 및 job 단계 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 02:06 KST
- 직전 01:07 KST 체크포인트를 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. 수집기는 OKX 공개 API의 ETH-USDT-SWAP 단일 상품 `oiCcy`(ETH), 응답 `code=0`, 관측시각 및 300초 신선도를 검사하도록 구현되어 있음.
- main JSON의 **OKX ETH-USDT-SWAP 단일 거래소 OI 706460.911 ETH**, 거래소 관측 `2026-11-14T17:06:02.854Z` (02:06:02.854 KST), 수집 `17:06:02.938309Z`, 내부 `VERIFIED`, blob SHA `749fc5c39641e89463c287a8b9fbe364b37a03fc`. 직전 01:05 관측보다 갱신됨. Binance OI 또는 시장 전체 OI가 아님.
- 보조 Actions [#43619224708](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43619224708) (17:05:56 UTC) 및 [#43618759823](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43618759823) (17:01:04 UTC) 모두 `workflow_run` success. 두 실행의 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 모두 success 확인. 단계 성공만으로 실제 신규 커밋이나 실행 stdout↔저장 JSON SHA 대조까지 입증되지는 않음.
- 전체 최근 100건의 `event=schedule` 목록에서 가장 최근 OKX 독립 예약 성공은 [#43609708642](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43609708642) (15:21:04 UTC), 그 전 [#43576665342](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43576665342) (08:36:59 UTC). **인접한 독립 schedule 2회 연속 성공 미입증**. 보조 workflow_run 성공과 구분.
- 별도 OKX 원시 HTTP 응답 본문 직접 대조, 최신 실행 원문 stdout↔저장 JSON 전체 SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 회차 미검증. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-15 01:07 KST
- 직전 2026-11-14 23:40 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 직접 재조회. 수집기는 OKX 공개 API ETH-USDT-SWAP 단일 상품의 `oiCcy`(ETH), 응답 `code=0`, 거래소 관측시각 및 300초 신선도를 검사하도록 구현됨. 워크플로에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 704757.920 ETH**, 관측 `2026-11-14T16:05:49.009Z` (2026-11-15 01:05:49.009 KST), 수집 `16:05:49.092724Z`, 내부 `VERIFIED`. 직전 23:35 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- Actions [#43613706418](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43613706418) (16:05:42 UTC) 및 [#43613262991](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43613262991) (16:01:01 UTC)는 모두 보조 `workflow_run` success. OI JSON 저장 커밋 [edb8a83](https://github.com/changwookseo/eth-cvd-monitor/commit/edb8a83a508576651e82f69449bfef7ed2f67cc0) (16:05:49 UTC), [52bf7ad](https://github.com/changwookseo/eth-cvd-monitor/commit/52bf7adf9988271008fbf9b7ea09451237e4d2e7) (16:01:12 UTC) 확인. 저장 커밋의 존재는 확인했지만 실행 원문 stdout과 JSON 전체 SHA 대조까지 입증하지 않음.
- 최근 100건의 전체 `event=schedule` 목록에서 가장 최근 OKX 독립 예약 성공 [#43609708642](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43609708642) (15:21:04 UTC), 그 전 [#43576665342](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43576665342) (08:36:59 UTC). **5분 주기의 인접 독립 schedule 2회 연속 성공은 여전히 미입증**. 보조 workflow_run을 독립 예약으로 간주하지 않음.
- 별도 OKX 원시 HTTP 응답 본문 직접 교차검증, 최신 실행 stdout↔저장 JSON 전체 SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서에 최신 실측 OI 반영은 이번 회차 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 23:40 KST
- 직전 22:50 KST 체크포인트 확인 후 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. 수집기는 OKX 공개 API `ETH-USDT-SWAP` 단일 상품의 `oiCcy`(ETH), 응답 `code=0`, 거래소 관측시각 및 300초 신선도를 검사하도록 구현됨.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 694299.778 ETH**, 관측 `2026-11-14T14:35:49.184Z` (23:35:49.184 KST), 수집 `14:35:49.244393Z`, 내부 `VERIFIED`, blob SHA `ae974813530d4a8fb655b439c405a8862da01870`. 22:45 관측보다 갱신됨. Binance OI 또는 전체 시장 OI가 아님.
- [#43605679408](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43605679408) (14:35:41 UTC) 및 [#43605263750](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43605263750) (14:31:03 UTC)는 모두 보조 `workflow_run` success. 최신 #43605679408의 API 수집·신선도 검사·JSON 커밋 단계 success를 jobs API에서 확인. 단계 success만으로 실행 원문과 저장 파일 전체 SHA 대조가 입증되는 것은 아님.
- 최근 100개 전체 `event=schedule` 중 OKX 독립 예약 실행은 [#43576665342](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43576665342) (08:36:59 UTC)와 [#43543037732](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43543037732) (01:51:26 UTC) 등이 success이나 수시간 간격. **설정된 5분 주기의 인접 독립 schedule 2회 연속 성공은 미입증**.
- 별도 OKX 원시 HTTP 본문 직접 교차대조, 최신 stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이번에는 상태 문서만 변경하고 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 22:50 KST
- 직전 21:55 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 확인. OKX 공개 API 단일 ETH-USDT-SWAP `oiCcy`(ETH), `code=0`, 거래소 관측시각 및 300초 신선도 검사 구현 유지.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 709913.640 ETH**, 거래소 관측 `2026-11-14T13:45:49.355Z` (22:45:49.355 KST), 수집 `13:45:49.430316Z`, 내부 `VERIFIED`, blob SHA `dfe3dc1ddcb3a810cb846e17372e5bfaf0b914cd`. 이전 21:55 관측 대비 갱신. Binance OI 또는 시장 전체 OI가 아님.
- 보조 Actions [#43601376609](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43601376609) (13:45:42 UTC) 및 [#43600964028](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43600964028) (13:40:42 UTC) 모두 `workflow_run` success. #43601376609 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 성공 단계만으로 신규 커밋이나 stdout↔JSON 전체 SHA 대조가 입증되지는 않음.
- 최근 전체 `event=schedule` 100건 중 OKX 독립 예약 성공은 [#43576665342](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43576665342) (08:36:59 UTC), 이전 [#43543037732](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43543037732) (01:51:26 UTC) 등으로 간격이 수시간. **설정된 5분 주기의 인접 독립 schedule 2회 연속 성공 미입증**. 보조 workflow_run 연속 성공과 구분.
- 미검증: 별도 OKX 원시 HTTP 본문 직접 교차대조, 최신 실행 원문 stdout↔저장 JSON 전체 SHA 대조, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이번에는 상태 문서만 변경하며 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 21:55 KST
- 직전 20:46 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. collector는 OKX 공개 API 단일 ETH-USDT-SWAP `oiCcy`(ETH), `code=0`, 거래소 관측시각 및 300초 신선도를 검증하도록 구현됨.
- main JSON의 **OKX ETH-USDT-SWAP 단일 거래소 OI 705368.241 ETH**, 관측 `2026-11-14T12:55:45.629000+00:00` (21:55:45.629 KST), 수집 `2026-11-14T12:55:45.684377+00:00`, 내부 `VERIFIED`, blob SHA `5e86f6621796c1073e8622179e437f0adc24dd9c`. 이전 20:45 관측보다 갱신. Binance OI 또는 전체 시장 OI가 아님.
- Actions [#43596792278](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43596792278) (12:50:42 UTC) 및 [#43597181681](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43597181681) (12:55:37 UTC) 모두 보조 `workflow_run` success. OI JSON 저장 커밋 [6492a15](https://github.com/changwookseo/eth-cvd-monitor/commit/6492a15f89679c5ef479fd896e14acddc39b1db0) (12:50:51 UTC), [aebec14](https://github.com/changwookseo/eth-cvd-monitor/commit/aebec14d2efc66070a4f917e6de2766cba3b85e7) (12:55:46 UTC) 확인. JSON 파일 조회와 커밋 목록의 시간 관계는 확인했으나 실행 원문↔저장 전체 SHA 대조는 미완료.
- 전체 최근 100건 `event=schedule` 조회에서 가장 최근 OKX 독립 예약 성공 [#43576665342](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43576665342) (08:36:59 UTC), 이전 [#43543037732](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43543037732) (01:51:26 UTC). 인접 독립 예약 2회 연속 성공 미입증. 보조 `workflow_run`은 독립 예약으로 간주하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 교차검증, 최신 실행 원문 stdout↔저장 JSON 전체 SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 수집기 내부 `VERIFIED`는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 20:46 KST
- 직전 19:26 KST 체크포인트를 먼저 읽고 OI 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재확인. collector는 OKX 공개 API의 단일 ETH-USDT-SWAP `oiCcy`(ETH), `code=0`, 거래소 관측시각 및 300초 신선도를 검증하도록 구현되어 있음.
- main JSON의 **OKX ETH-USDT-SWAP 단일 거래소 OI 706685.857 ETH**, 관측 `2026-11-14T11:45:52.501Z` (20:45:52.501 KST), 수집 `11:45:52.581573Z`, 내부 `VERIFIED`, blob SHA `d743def97d51a311127d20437d78625bde2fabd5`. 19:25 관측 대비 갱신. Binance OI나 전체 시장 OI가 아님.
- Actions [#43591554622](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43591554622) (11:45:45 UTC) 및 [#43591161933](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43591161933) (11:40:43 UTC) 모두 보조 `workflow_run` success. 각 실행의 수집·신선도 검사·커밋 단계가 jobs API에서 success. 단, 단계 성공만으로 신규 JSON 커밋 및 stdout↔blob SHA 일치를 입증하지 않음.
- 최근 100개 `event=schedule` 조회 중 OKX 독립 예약 성공은 [#43576665342](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43576665342) (08:36:59 UTC), 이전 [#43543037732](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43543037732) (01:51:26 UTC). 인접 독립 schedule 2회 연속 성공은 미입증. `workflow_run`을 독립 예약으로 계산하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 교차대조, 최신 실행 stdout↔저장 JSON 전체 SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 점검에서 검증되지 않음. 내부 `VERIFIED`는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 이외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 19:26 KST
- 직전 18:16 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 직접 확인. 수집기는 OKX 공개 API 단일 ETH-USDT-SWAP의 `oiCcy`(ETH), 응답 `code=0`, 관측시각 및 300초 신선도를 검사. 워크플로에는 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run`이 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 705680.736 ETH**, 거래소 관측 `2026-11-14T10:25:42.223Z` (19:25:42.223 KST), 수집 `10:25:42.304720Z`, 내부 `VERIFIED`, blob SHA `6318a320bc44a143fdf94227e030631c040a4362`. 18:15 관측보다 갱신. Binance OI나 전체 시장 OI가 아님.
- 보조 Actions [#43585221661](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43585221661) (10:25:35 UTC) 및 [#43584829023](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43584829023) (10:20:41 UTC)는 모두 `workflow_run` success. 최신 실행의 수집·신선도·JSON 커밋 단계 success를 jobs API로 확인. 실제 OI JSON 저장 커밋 [e7e0e2d](https://github.com/changwookseo/eth-cvd-monitor/commit/e7e0e2d1c24b4b2aa87fc0e60a7be33df8197c67) (10:25:46 UTC) 및 이전 [b0ae59d](https://github.com/changwookseo/eth-cvd-monitor/commit/b0ae59debff458189a8c210be946aef2beb7bd50) (10:20:50 UTC) 확인. 최신 커밋 diff의 OI·관측시각이 main JSON과 일치. 실행 원문 stdout↔저장 전체 SHA 직접 대조까지는 아님.
- 최근 100개 전체 `event=schedule` 실행 중 OKX 독립 예약 성공은 [#43576665342](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43576665342) (08:36:59 UTC) 및 이전 #43543037732 (01:51:26 UTC). **독립 schedule의 인접 2회 연속 성공 미입증**. 보조 실행 성공과 혼동하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 교차대조, 최신 실행 원문 stdout↔저장 JSON 전체 SHA 대조, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 18:16 KST
- 직전 18:07 KST 체크포인트 확인 후 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 재조회. 수집기는 OKX 공개 API 단일 ETH-USDT-SWAP의 `oiCcy`(ETH), `code=0`, 관측시각 및 300초 신선도를 검사. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 709349.181 ETH**, 관측 `2026-11-14T09:15:50.315Z` (18:15:50.315 KST), 수집 `09:15:50.391019Z`, 내부 `VERIFIED`, blob SHA `13cca852a22c1ae6e20af583ed212cbf881c399c`. 직전 18:05 관측보다 갱신됨. Binance OI나 시장 전체 OI 아님.
- Actions [#43579709840](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43579709840) (09:15:42 UTC), [#43579298440](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43579298440) (09:10:40 UTC) 모두 보조 `workflow_run` success. 확인된 독립 `schedule` 성공 [#43576665342](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43576665342) (08:36:59 UTC)은 인접 독립 예약 2회 연속 성공의 증거가 아님.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 실행 원문 로그↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서에 최신 OI 실측 반영은 미검증. 수집기 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 18:07 KST
- 직전 16:28 KST 체크포인트를 먼저 읽고 OI 전체 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 및 보고서 호출 규칙 재조회. collector는 OKX 공개 API ETH-USDT-SWAP 단일 계약의 `oiCcy`(ETH), 응답 code=0, 관측시각과 300초 신선도를 검사. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 설정 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 707834.270 ETH**, 관측 `2026-11-14T09:05:46.878Z` (18:05:46.878 KST), 수집 `09:05:46.963499Z`, 내부 `status=VERIFIED`. 직전 16:25 관측보다 갱신. Binance OI나 전체 시장 OI 아님.
- [#43578888972](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43578888972) (09:05:39 UTC)와 [#43578496900](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43578496900) (09:00:57 UTC)는 모두 보조 `workflow_run` success. 최신 실행의 수집·신선도 검증·커밋 단계 success 확인. 이는 개별 신규 JSON 커밋과 stdout SHA 대조를 자동 입증하지 않음.
- 새롭게 확인한 독립 `schedule` 성공은 [#43576665342](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43576665342) (08:36:59 UTC). 이전 독립 예약 성공은 #43543037732 (01:51:26 UTC). 최근 100건 예약 목록에서 **인접 독립 예약 2회 연속 성공 미입증**.
- 별도 OKX 원시 HTTP 응답 직접 교차검증, 최신 job 원문↔저장 JSON 전체 SHA 직접 대조, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 미검증. 보고서 규칙의 OKX OI 참조 조항은 확인했으나 실제 보고서 반영 성공과 구분.
- **OI 전체 게이트 미통과. 펀딩비·선물 CVD 단계 미진입, 전체 복구 미완료, 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 16:28 KST
- 직전 15:48 KST 체크포인트를 읽고 OI 게이트만 재점검. main `eth_oi_okx_latest.json`에 OKX ETH-USDT-SWAP 단일 거래소 OI **703764.466 ETH**, 관측 `2026-11-14T07:25:50.944Z` (16:25:50.944 KST), 수집 `07:25:51.038878Z`, 내부 `VERIFIED` 확인. 직전 15:45 관측보다 갱신됨. Binance OI 또는 전체 시장 OI 아님.
- Actions 최신 실행 #43571052561 (07:25:44 UTC), #43570665538 (07:20:48 UTC) `workflow_run` success 확인. 같은 시각 다수 보조 실행이 발생하며, 독립 `schedule` 인접 2회 성공 증거가 아님.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 job 원문↔저장 JSON SHA 직접 대조, 독립 schedule 인접 2회 연속 성공, 완성 ETH ESI 2.0 보고서의 실측 반영은 이번 회차 미검증. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 완료 알림 금지.** Binance Cron Secret 미등록 유지, 우회·노출·변경 없음. 기존 지표·보고서·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 15:48 KST
- 최신 14:54 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. OKX 공개 API 단일 ETH-USDT-SWAP의 `oiCcy`(ETH), 거래소 관측시각과 300초 신선도 검증 코드 유지. 워크플로는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 704573.876 ETH**, 관측 `2026-11-14T06:45:46.494Z` (15:45:46.494 KST), 수집 `06:45:46.575258Z`, 내부 `VERIFIED`, blob SHA `f0fe23bbeb3f7c6cb00d61378859aeadcc105b1f`. 이전 14:50 관측 이후 갱신. Binance 또는 전체 시장 OI 아님.
- Actions [#43567903375](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43567903375) (06:45:40 UTC) 및 [#43567511445](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43567511445) (06:40:43 UTC)는 모두 **보조 `workflow_run` success**. 최신 100개 `event=schedule` 조회에서 OKX 독립 예약 성공은 #43543037732 (01:51:26 UTC), 이전 #43512670076 (전날 21:39:44 UTC)로, 인접 독립 schedule 2회 연속 성공은 미입증.
- 별도 OKX 원시 HTTP 본문 대조, 최신 job stdout↔저장 JSON 전체 SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 회차 미검증. 수집기 내부 VERIFIED와 보조 실행 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 14:54 KST
- 직전 13:33 KST 체크포인트를 먼저 확인한 후 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 수집기는 OKX 공개 API `ETH-USDT-SWAP` 단일 행의 `oiCcy` ETH 및 300초 신선도 검사 구현; 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 702082.733 ETH**, 거래소 관측 `2026-11-14T05:50:54.132Z` (14:50:54.132 KST), 수집 `05:50:54.206318Z`, 내부 `VERIFIED`, blob SHA `bca6bc4b6eece331560cefd7196a1cec5af794a4`. 직전 13:31 관측 이후 갱신. Binance OI나 전체 시장 OI가 아님.
- Actions [#43563471005](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43563471005) (05:50:47 UTC) 및 [#43563083076](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43563083076) (05:45:48 UTC)는 모두 보조 `workflow_run` success. 양쪽 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 최근 100개 `event=schedule` 중 OKX 독립 예약 성공은 [#43543037732](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43543037732) (01:51:26 UTC), 이전 #43512670076 (전날 21:39:44 UTC); **인접 독립 schedule 2회 연속 성공 미입증**.
- 이번 회차 별도 OKX 원시 HTTP 본문 교차대조, 최신 실행 원문 stdout↔저장 JSON SHA 대조, 실제 완성 ETH ESI 2.0 보고서에 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED 및 보조 실행 success만으로 전체 OI 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 13:33 KST
- 직전 12:40 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. 수집기는 OKX 공개 API `ETH-USDT-SWAP`의 `oiCcy` ETH, `code=0`, 300초 신선도 검증 구현. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main 저장 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 701074.366 ETH**, 관측 `2026-11-14T04:31:14.391Z` (13:31:14.391 KST), 수집 `04:31:14.444899Z`, 내부 `VERIFIED`, blob SHA `3e0f14de065ccd45e00c7cc4d7664f5ff6a4c14a`. 직전 12:36 관측 이후 갱신. Binance OI나 전체 시장 OI 아님.
- GitHub Actions 최근 [#43557032574](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43557032574) (04:30:59 UTC), [#43556611247](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43556611247) (04:25:49 UTC), [#43556186819](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43556186819) (04:20:49 UTC) 모두 `workflow_run` success. 독립 `schedule` 인접 2회 성공을 증명하지 않음.
- 별도 OKX 원시 HTTP 응답 본문 대조, 최신 job stdout↔저장 JSON 전체 SHA 대조, 실제 완성 ETH ESI 2.0 보고서에 최신 실측 OI 반영은 이번 회차 미검증. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 12:40 KST
- 직전 11:38 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재점검. main의 `.github/workflows/eth-oi-okx.yml`에 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존 확인.
- main 최신 `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 690014.321 ETH**, 관측 `2026-11-14T03:36:05.905Z` (12:36:05.905 KST), 수집 `03:36:05.994784Z`, 내부 `status=VERIFIED`. 직전 11:35 관측 이후 갱신됨. Binance OI나 전체 시장 OI가 아님.
- 최근 [#43552463922](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43552463922) (03:35:58 UTC), [#43552017633](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43552017633) (03:30:54 UTC)는 모두 **보조 `workflow_run` success**. 최근 100개 `event=schedule` 중 최신 OKX 독립 예약 성공 [#43543037732](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43543037732) (01:51:26 UTC), 이전 #43512670076 (전날 21:39:44 UTC). 인접한 독립 예약 2회 연속 성공은 입증되지 않음.
- 이번 회차 별도 OKX 원시 HTTP 응답 직접 대조, 최신 job stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 실측 OI 반영은 미검증. GitHub 저장 JSON 내부 VERIFIED 및 보조 실행 성공만으로 전체 OI 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 11:38 KST
- 10:51 KST 최신 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 확인. 수집기는 OKX 공개 API의 단일 ETH-USDT-SWAP `oiCcy`(ETH), `code=0`, 거래소 관측시각과 300초 신선도 검사를 구현하며 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main 저장 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 680229.218 ETH**, 관측 `2026-11-14T02:35:55.111Z` (11:35:55.111 KST), 수집 `02:35:55.189323Z`, 내부 `VERIFIED`, blob SHA `088383d042f96f2c7e46c4cb3fc9ca19f8189c4a`. 직전 10:50 관측 이후 갱신됨. Binance OI나 시장 전체 OI가 아님.
- Actions 최근 실행 [#43547183635](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43547183635) (02:35:47 UTC), [#43546785327](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43546785327) (02:31:31 UTC) 모두 `workflow_run` success. 최신 독립 예약 성공 [#43543037732](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43543037732) (01:51:26 UTC), 이전 [#43512670076](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43512670076) (전날 21:39:44 UTC) 확인. 조회된 인접 독립 schedule 2회 연속 성공은 입증되지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 job stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 실측 OI 반영은 이번 회차 미검증. collector 내부 VERIFIED 및 보조 실행 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 10:51 KST
- 최신 09:16 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 재점검. main의 `.github/workflows/eth-oi-okx.yml`에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존을 재확인.
- main 저장 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 696114.797 ETH**, 거래소 관측 `2026-11-14T01:50:54.508000+00:00` (10:50:54.508 KST), 수집 `2026-11-14T01:50:54.589963+00:00`, 내부 `VERIFIED`, blob SHA `846199fa965b8a75ebf2f214b9bb8567563f3120`. 직전 09:15 관측보다 갱신. Binance OI나 전체 시장 OI가 아님.
- GitHub Actions 최근 실행 목록에서 [#43542497583](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43542497583) (01:45:41 UTC), [#43542020771](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43542020771) (01:40:45 UTC)는 `workflow_run` success. 01:50 UTC 실행 #43542977828은 앞선 조회 당시 결론 미확정. 보조 실행을 독립 `schedule` 성공으로 오인하지 않음.
- 독립 `schedule` 인접 2회 연속 성공, 별도 OKX 원시 HTTP 본문 대조, 최신 job stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서에 최신 실측 OI 반영은 이번 점검에서 입증되지 않음. JSON 내부 VERIFIED만으로 전체 게이트를 통과시키지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 09:16 KST
- 최신 08:45 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 확인. 수집기는 OKX 공개 API 단일 ETH-USDT-SWAP의 `oiCcy`(ETH), `code=0`, 거래소 관측시각 및 300초 신선도를 검증하며 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 691295.748 ETH**, 관측 `2026-11-14T00:15:57.192Z` (09:15:57.192 KST), 수집 `00:15:57.253608Z`, 내부 `VERIFIED`, blob SHA `3a32028fa8beb5896672c74bfd1340d9f523db35`. 이전 체크포인트보다 관측시각 갱신. Binance OI나 전체 시장 OI 아님.
- GitHub Actions [#43532989442](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43532989442) (00:15:48 UTC) 및 [#43532400587](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43532400587) (00:10:47 UTC)는 모두 보조 `workflow_run` success. 최근 100개 `event=schedule` 조회에서 최신 OKX 독립 예약 성공은 [#43512670076](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43512670076) (전날 21:39:44 UTC), 이전 #43454729243 (15:39:04 UTC). 인접한 독립 예약 2회 연속 성공 미입증. #43512670076 jobs API에서 수집·신선도 검사·JSON 커밋 단계 success 확인.
- 별도 OKX 원시 HTTP 요청은 DNS 해석 실패로 원문 응답 직접 대조 불가. 최신 job stdout↔저장 JSON 전체 SHA 직접 대조 및 **실제 완성 ETH ESI 2.0 보고서에 최신 OI 실측 반영**은 미검증. 보고서 호출 규칙의 OKX 단일 거래소 보조 원천 지침은 확인했으나 실측 보고서 실행의 증거는 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 상태 유지, 우회·노출·등록 없음. 이번에는 상태 문서만 갱신하고 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 08:45 KST
- 직전 08:05 KST 체크포인트 확인 후 OI 게이트만 점검. main의 OKX OI 워크플로는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`을 유지.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 691940.976 ETH**, 거래소 관측 `2026-11-13T23:45:51+00:00` (08:40:58.574 KST), 수집 `2026-11-13T23:45:51.063447+00:00`, 내부 `VERIFIED`, blob SHA `bb0a90dffd443864329f408949ba11111056bf79`. 08:05 체크포인트보다 관측시각이 갱신됨. Binance OI나 시장 전체 OI가 아님.
- [#43528894597](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43528894597) (23:40:50 UTC) 및 [#43528268670](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43528268670) (23:35:39 UTC)은 보조 `workflow_run` 성공. 최신 실행 jobs API에서 수집·신선도 검증·JSON 커밋 단계 success 확인. 이는 독립 schedule 연속 성공을 뜻하지 않으며 commit 단계 success만으로 신규 저장 SHA 대조까지 증명되지 않음.
- 최근 100건 `event=schedule` 중 최신 OKX 독립 예약 성공은 [#43512670076](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43512670076) (21:39:44 UTC), 직전은 #43454729243 (15:39:04 UTC). 인접 5분 독립 예약 2회 연속 성공은 확인되지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 이번 실행 stdout↔저장 JSON SHA 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` 미등록 상태 유지, 우회·노출·수정 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 08:05 KST
- 직전 06:47 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 수집기는 OKX ETH-USDT-SWAP 단일 종목의 공개 API `oiCcy`(ETH), `code=0`, 관측시각과 300초 신선도 검사를 구현. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 689661.468 ETH**, 관측 `2026-11-13T23:05:52.745Z` (08:05:52.745 KST), 수집 `23:05:52.808442Z`, 내부 `VERIFIED`, blob SHA `69e0f1d9b5d94644e8775dd2e9b071131ab1620e`. 이전 06:45 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- Actions 전체 최근 목록에서 [#43524473048](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43524473048) (23:05:44 UTC) 및 [#43523864109](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43523864109) (23:01:02 UTC) 모두 `workflow_run` success. 최근 schedule 전용 목록에서 최신 OKX 독립 예약 성공은 [#43512670076](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43512670076) (21:39:44 UTC), 그 이전 #43454729243 (15:39:04 UTC). **인접 독립 schedule 2회 연속 성공 미입증**.
- 이번 회차 별도 OKX 원시 HTTP 응답 본문 대조, 최신 job stdout↔저장 JSON 전체 SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영 미검증. 수집기 내부 VERIFIED 및 보조 실행 성공만으로 OI 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 이번에는 상태 문서만 갱신하며 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 06:47 KST
- 05:46 KST 최신 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`, 보고서 호출 규칙 직접 조회. 수집기는 OKX 공개 API 단일 ETH-USDT-SWAP `oiCcy`(ETH), code=0, 거래소 관측시각과 300초 신선도 검사를 구현. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 691000.954 ETH**, 관측 `2026-11-13T21:45:59.169Z` (06:45:59.169 KST), 수집 `21:45:59.253556Z`, 내부 `VERIFIED`, blob SHA `304219492dfe5469fef69cd900d4025ffc229f77`. 05:45 관측보다 갱신됨. Binance OI나 전체 시장 OI가 아님.
- GitHub Actions 최근 목록에서 [#43513562162](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43513562162) (21:45:51 UTC), [#43512845107](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43512845107) (21:40:54 UTC) 모두 보조 `workflow_run` success. [#43512670076](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43512670076) (21:39:44 UTC)은 독립 `schedule` success로 확인되어 **새로운 독립 예약 실행 성공 1건**을 추가 확보. 그러나 인접한 독립 예약 실행 2회 연속 성공은 여전히 미입증.
- 이번 점검에서는 별도 OKX 원시 HTTP 응답 본문 대조, 최신 실행 stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영이 검증되지 않음. 수집기 내부 VERIFIED 및 워크플로 success만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 상태 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 05:46 KST
- 최신 04:35 KST 체크포인트 확인 후 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 확인. OKX 단일 ETH-USDT-SWAP `oiCcy` ETH, 거래소 관측시각 및 300초 신선도 검증 로직 유지; 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 695585.009 ETH**, 관측 `2026-11-13T20:45:52.776Z` (05:45:52.776 KST), 수집 `20:45:52.858628Z`, 내부 `VERIFIED`, blob SHA `a285255c9783b2c54935995888f5103b3e6346ec`. 이전 05:40:55.061 KST 관측의 695732.133 ETH보다 갱신. Binance OI/전체 시장 OI 아님.
- [#43504520904](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43504520904) (20:45:45 UTC) 및 [#43503765906](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43503765906) (20:40:46 UTC)는 모두 보조 `workflow_run` success. jobs API에서 수집·신선도 검사·JSON 저장 단계 성공 확인. 최신 job 원문에서 0d11a50 커밋 및 `STORED` 메시지 확인; 최신 stdout의 관측시각·OI 값과 main JSON 일치. 직전 job 원문에서도 20:40:55.061Z, 695732.133 ETH 및 `STORED` 확인. 원시 HTTP 응답 본문을 별도로 취득한 것은 아님.
- 최근 100건 `event=schedule` 조회에서 OKX 독립 schedule 성공 [#43454729243](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43454729243) (2026-11-13 15:39:04 UTC), 이전 [#43385969455](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43385969455) (07:28:11 UTC) 확인. **인접한 독립 schedule 2회 연속 성공 미입증**.
- 별도 OKX 원시 HTTP 응답 본문 교차검증, 최신 실행 stdout↔저장 파일 전체 SHA 동일성 검증, 완성 ETH ESI 2.0 보고서에 최신 OI 실측 반영 검증은 미완료. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 04:35 KST
- 직전 03:26 KST 체크포인트를 먼저 확인하고 OI 전체 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 재조회. 수집기는 OKX 공개 API의 ETH-USDT-SWAP 단일 상품 `oiCcy`(ETH), API code=0, 관측시각 및 300초 신선도 검사를 구현. 워크플로에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 698558.856 ETH**, 관측 `2026-11-13T19:35:49.617Z` (04:35:49.617 KST), 수집 `19:35:49.697486Z`, 내부 `status=VERIFIED`, blob SHA `fc4fcea8604509cf131162fb665febe627089736`. 직전 03:25 관측보다 갱신됨. Binance OI 또는 전체 시장 OI가 아님.
- Actions [#43493688369](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43493688369) (19:35:41 UTC) 및 [#43492912725](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43492912725) (19:30:53 UTC)는 모두 **보조 `workflow_run` success**. 양쪽 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 커밋 단계 success만으로 실제 신규 저장 커밋을 확정하지 않음. 최근 100건 중 조회된 OKX 실행은 보조 `workflow_run`이며 독립 `schedule`의 인접 2회 연속 성공은 미입증.
- 별도 OKX 원시 HTTP 본문 직접 교차검증, 최신 실행 stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 점검에서 확인하지 못함. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 복구 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 03:26 KST
- 직전 02:19 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 수집기는 OKX 공개 API `ETH-USDT-SWAP`의 `oiCcy`(ETH), 거래소 관측시각, 300초 신선도 검사를 구현; 워크플로에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 701200.329 ETH**, 거래소 관측 `2026-11-13T18:25:47.152Z` (2026-11-14 03:25:47.152 KST), 수집 `18:25:47.207910Z`, 내부 `status=VERIFIED`, blob SHA `8deb6874cc2eddaff5e787d9f8347c824deaf215`. 이전 02:15 관측보다 갱신됨. Binance OI 또는 전체 시장 OI가 아님.
- GitHub Actions [#43482519377](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43482519377) (18:25:36 UTC), [#43481733397](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43481733397) (18:20:47 UTC)는 모두 **보조 `workflow_run` success**. 두 실행의 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 다만 커밋 단계 성공은 실제 신규 커밋을 보장하지 않으며 독립 `schedule` 인접 2회 성공 증거가 아님.
- 별도 실행환경에서 OKX 원시 HTTP 요청은 DNS 해석 오류로 실패. 최신 실행 원문 stdout↔저장 JSON SHA 직접 대조 및 실제 완성 ETH ESI 2.0 보고서의 실측 OI 반영은 미검증. **OI 전체 게이트 미통과; 펀딩비·선물 CVD 복구 단계 미진입; 전체 복구 미완료; 완료 알림 금지.**
- Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이번에는 상태 문서만 갱신하며 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 02:19 KST
- 최신 01:31 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 코드에는 OKX 공개 API 단일 ETH-USDT-SWAP `oiCcy`(ETH), `code=0`, 관측시각과 300초 신선도 검사가 구현되어 있고 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run`이 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 700513.028 ETH**, 관측 `2026-11-13T17:15:54.111Z` (2026-11-14 02:15:54.111 KST), 수집 `17:15:54.186984Z`, 내부 `status=VERIFIED`, blob SHA `f8bee5db466146a0c2e78d72c8c7eba2284d4806`. 직전 01:31 관측보다 진전됨. Binance OI 또는 전체 시장 OI가 아님.
- GitHub Actions [#43471036871](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43471036871) (17:15:45 UTC) 및 [#43470196388](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43470196388) (17:10:50 UTC) 모두 **보조 `workflow_run` success**. 최신 실행 jobs API에서 수집·신선도 검사·JSON 커밋 단계 모두 success 확인. 커밋 단계 success는 신규 저장을 보장하지 않음. 인접 독립 `schedule` 2회 연속 성공은 미입증.
- 이번 회차 별도 OKX 원시 HTTP 응답 직접 교차검증, 최신 실행 stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. 내부 VERIFIED만으로 전체 OI 게이트를 통과시키지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-14 01:31 KST
- 최신 00:23 KST 체크포인트를 먼저 확인하고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 조회. 수집기는 OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), 거래소 관측시각 및 300초 신선도 검사를 수행하도록 구현. 워크플로에 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 697677.882 ETH**, 관측 `2026-11-13T16:31:10.613Z` (2026-11-14 01:31:10.613 KST), 수집 `16:31:10.699411Z`, 내부 `status=VERIFIED`, blob SHA `25d57717b04ad260bccae48da76315f880faa12b`. 직전 00:21 관측 이후 갱신. Binance OI 또는 전체 시장 OI 아님.
- GitHub Actions [#43463475898](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43463475898) (16:31:03 UTC) 및 [#43462630476](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43462630476) (16:25:47 UTC)는 모두 **보조 `workflow_run` success**. 두 실행 jobs API에서 API 수집·출력 신선도 검사·JSON 커밋 단계 success 확인. 다만 커밋 단계 성공만으로 신규 커밋 발생은 확정되지 않으며, 두 실행은 독립 예약 실행 연속 성공의 증거가 아님.
- 이번 회차 **독립 `schedule` 인접 2회 연속 성공, 별도 OKX 원시 HTTP 본문 대조, 실행 stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증**. collector 내부 VERIFIED만으로 전체 게이트를 통과시키지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 이번에는 상태 문서만 갱신하고 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터는 변경하지 않음.

## 자동 복구 점검 — 2026-11-14 00:23 KST
- 직전 2026-11-13 23:22 KST 체크포인트를 먼저 확인하고 OI 게이트만 재검증. main의 `eth_oi_okx_latest.json`, `.github/workflows/eth-oi-okx.yml` 직접 조회. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON의 **OKX ETH-USDT-SWAP 단일 거래소 OI 699406.816 ETH**, 거래소 관측 `2026-11-13T15:21:14.165Z` (2026-11-14 00:21:14.165 KST), 수집 `15:21:14.263865Z`, 내부 `status=VERIFIED`. 직전 23:20 관측 이후 갱신. Binance OI 또는 전체 시장 OI 아님.
- 최근 OKX 실행 [#43451728631](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43451728631) (15:21:04 UTC) 및 [#43450851238](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43450851238) (15:15:57 UTC)는 모두 **보조 `workflow_run` success**. OI 저장 커밋 [0b9547e](https://github.com/changwookseo/eth-cvd-monitor/commit/0b9547e98dcd098229829d2921dd8ec04548d11e) (15:21:14 UTC), [970dafb](https://github.com/changwookseo/eth-cvd-monitor/commit/970dafb537298b52b99f6059b6f5876592879d73) (15:16:07 UTC) 확인. 5분 전후 간격의 연속 JSON 갱신 증거이나 독립 예약 연속 성공은 아님.
- 조회된 `event=schedule` 최근 목록의 OKX 독립 성공은 #43385969455 (07:28 UTC), #43339979206 (00:48 UTC) 등이며 **인접 독립 예약 2회 연속 성공 미입증**. 이번 회차 별도 OKX 원시 HTTP 본문 대조, 최신 실행 stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영도 미검증. JSON 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 23:22 KST
- 직전 22:33 KST 체크포인트를 먼저 확인하고 OI 게이트만 재검증. main의 `eth_oi_okx_latest.json`과 `.github/workflows/eth-oi-okx.yml` 직접 조회. 워크플로는 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 병존.
- main JSON의 **OKX ETH-USDT-SWAP 단일 거래소 OI 701398.431 ETH**, 거래소 관측 `2026-11-13T14:20:58.519Z` (23:20:58.519 KST), 수집 `14:20:58.602491Z`, 내부 `status=VERIFIED`. 이전 22:31 관측 이후 갱신됨. Binance OI 또는 전체 시장 OI 아님.
- GitHub Actions 최신 OKX 실행 [#43441843897](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43441843897) (14:20:49 UTC) 및 [#43441070924](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43441070924) (14:15:52 UTC) 모두 **보조 `workflow_run` success**. 최신 실행의 jobs API에서 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 이는 독립 `schedule` 인접 2회 성공을 입증하지 않으며 커밋 단계 성공만으로 새 커밋을 확정하지 않음.
- 이번 점검에서 별도 OKX 원시 HTTP 응답 본문 대조, 최신 job stdout↔저장 JSON SHA 직접 대조, 독립 schedule 인접 2회 성공, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 확인되지 않음. JSON 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 22:33 KST
- 직전 22:07 KST 체크포인트를 먼저 읽고 main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 및 보고서 호출 규칙을 직접 재조회. OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 거래소 관측시각과 300초 신선도 검사 로직 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 704284.816 ETH**, 거래소 관측 `2026-11-13T13:31:13.118Z` (22:31:13.118 KST), 수집 `13:31:13.209717Z`, 내부 `status=VERIFIED`, blob SHA `55348b5aaf949e98dd8d842c94bfd1fda1662d4c`. 이전 22:05 관측 이후 갱신됨. Binance OI 또는 전체 시장 OI가 아님.
- Actions 최근 100개 실행 중 OKX `workflow_run` [#43434325127](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43434325127) (13:31:05 UTC), [#43433554868](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43433554868) (13:25:42 UTC) 모두 success. 최신 실행의 jobs API에서 API 수집, 신선도 검증, JSON 커밋 단계 success 확인. 그러나 이 두 실행은 **독립 schedule이 아닌 보조 workflow_run**이며 커밋 단계 success만으로 신규 저장 여부를 확정하지 않음.
- 별도 환경의 OKX 원시 HTTP 요청은 DNS 해석 실패. 최신 job stdout↔저장 JSON SHA 직접 대조, 독립 schedule의 인접 2회 연속 성공, **실제로 생성된 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영**은 여전히 미검증. 보고서 호출 규칙에 OKX OI 참조가 있음은 확인했으나 실제 완성 보고서 반영 증거는 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 복구 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 22:07 KST
- 최신 20:48 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 및 보고서 호출 규칙을 직접 조회. 수집기는 OKX 공개 API 단일 ETH-USDT-SWAP의 `oiCcy`(ETH), `code=0`, 관측시각 및 300초 신선도를 검증하도록 구현. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 713294.059 ETH**, 거래소 관측 `2026-11-13T13:05:53.557Z` (22:05:53.557 KST), 수집 `13:05:53.616902Z`, 내부 `status=VERIFIED`. 이전 20:45 KST 관측보다 갱신됨. Binance OI 또는 전체 시장 OI 아님.
- Actions 보조 `workflow_run` [#43430682368](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43430682368) (13:05:44 UTC) 및 [#43430011328](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43430011328) (13:01:04 UTC) 모두 success; 두 실행의 수집·신선도 검증·커밋 단계 모두 success. 단계 성공이 반드시 새 커밋을 뜻하지는 않음.
- Actions `event=schedule` 최근 100건의 OKX 독립 예약 실행은 #43385969455 (07:28:11 UTC), #43339979206 (00:48:23 UTC) 등으로 성공했지만 인접 5분 간격 독립 예약 2회 연속 성공은 미입증. 다른 워크플로 예약 실행 및 보조 workflow_run을 합산하지 않음.
- 이번 회차 별도 OKX 원시 HTTP 응답 직접 대조, 최신 실행 stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 20:48 KST
- 최신 20:09 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. 수집기는 OKX 공개 API의 단일 `ETH-USDT-SWAP` 상품 `oiCcy`(ETH), 응답 code=0, 거래소 관측시각 및 300초 신선도를 검사. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 717882.860 ETH**, 거래소 관측 `2026-11-13T11:45:51.078000+00:00`, 수집 `2026-11-13T11:45:51.165710+00:00`, 내부 status=`VERIFIED`, blob SHA `68df9a6dabfe81f93be79c1eb1e66ff77cffb6f0`. 직전 20:05 KST 관측보다 갱신됨. Binance OI 또는 시장 전체 OI가 아님.
- GitHub Actions 최근 보조 실행 [#43419625796](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43419625796) (11:45:43 UTC), [#43418981324](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43418981324) (11:40:48 UTC) 모두 `workflow_run` success. 이는 독립 예약 실행 연속 성공 증거가 아님.
- GitHub Actions 전체 `event=schedule` 최근 100건에서 OKX 독립 예약 성공은 [#43385969455](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43385969455) (07:28:11 UTC), [#43339979206](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43339979206) (00:48:23 UTC) 등으로, **5분 간격 인접 독립 schedule 2회 연속 성공은 입증되지 않음**.
- 이번 점검에서 별도 OKX 원시 HTTP 응답 본문, 최신 실행 stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 검증하지 못함. 내부 VERIFIED는 전체 OI 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 20:09 KST
- 직전 18:59 KST 체크포인트 확인 후 OI 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 및 보고서 호출 규칙 직접 조회. OKX 공개 API `ETH-USDT-SWAP` 단일 상품 `oiCcy`(ETH), `code=0`, 거래소 관측시각과 300초 신선도 검사 로직 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 717493.860 ETH**, 관측 `2026-11-13T11:05:55.898Z` (20:05:55.898 KST), 수집 `11:05:55.976961Z`, 내부 `status=VERIFIED`, blob SHA `eb9a9c519238fb4fd0b59589c42f06f8dee51023`. 직전 18:55 관측 이후 갱신. Binance OI나 시장 전체 OI 아님.
- GitHub Actions [#43414259433](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43414259433) (11:05:47 UTC), [#43413601532](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43413601532) (11:00:59 UTC) 모두 `workflow_run` success. 각 jobs API에서 API 수집·신선도 검증·커밋 단계 success. 독립 예약 실행 연속 성공으로 간주하지 않음.
- 전체 `event=schedule` 조회에서 가장 최근 OKX 독립 예약 성공은 [#43385969455](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43385969455) (07:28:11 UTC), 그 이전 [#43339979206](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43339979206) (00:48:23 UTC). 5분 간격 인접 독립 schedule 2회 성공 미입증. 다른 워크플로의 schedule 성공은 제외.
- 별도 실행환경 OKX 원시 HTTP 요청은 DNS 해석 실패. 이번 실행의 원문 stdout↔저장 JSON SHA 직접 대조 및 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영 미검증. `VERIFIED`는 수집기 내부 상태이며 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서만 갱신하며 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 18:59 KST
- 최신 17:43 KST 체크포인트를 먼저 읽고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 및 보고서 호출 규칙을 직접 조회. 수집기는 OKX 공개 API `ETH-USDT-SWAP` 단일 종목의 `oiCcy`(ETH), `code=0`, 관측시각 및 300초 신선도를 검증하도록 구현되어 있음. 워크플로에는 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run`이 병존.
- main JSON의 **OKX ETH-USDT-SWAP 단일 거래소 OI 719511.309 ETH**, 거래소 관측 `2026-11-13T09:55:51.087Z` (18:55:51.087 KST), 수집 `09:55:51.167985Z`, 내부 `status=VERIFIED`, blob SHA `4570a87662ac37c67ff1790af787b300ea3ed847`. 이전 17:40 관측 대비 갱신. Binance OI나 전체 시장 OI가 아님.
- 실제 OI JSON 저장 커밋 [3a9d758](https://github.com/changwookseo/eth-cvd-monitor/commit/3a9d758c33a1d73e9a1aca6742908e7d38d5b181) 및 [555b747](https://github.com/changwookseo/eth-cvd-monitor/commit/555b747051a6030802adef6d17bec73936363501)의 diff를 직접 확인. 각각 18:50:54→18:55:51, 18:45:54→18:50:54 KST의 관측시각 및 OI 수치가 갱신되었으며 최신 커밋 diff는 main JSON과 일치. **연속 저장 확인은 독립 schedule 연속 성공 증거가 아님**.
- 이번 커넥터 도구에는 Actions 전체 실행 목록 조회가 없어 최신 실행의 `event=schedule` 여부 및 인접 독립 예약 2회 성공을 재입증하지 못함. 최신 job 원문 stdout↔저장 JSON SHA 직접 대조, 별도 OKX 원시 HTTP 응답 대조, 실제 완성 ETH ESI 2.0 보고서의 실측 OI 반영도 미검증. 보고서 호출 규칙의 OKX 참조 지시만으로 실측 반영을 인정하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 17:43 KST
- 직전 16:58 KST 체크포인트를 먼저 읽고 OI 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 및 보고서 호출 규칙을 직접 재조회. OKX 공개 API 단일 `ETH-USDT-SWAP`의 `oiCcy`(ETH), `code=0`, 거래소 관측시각 및 300초 신선도 검사 로직 유지.
- main JSON의 **OKX ETH-USDT-SWAP 단일 거래소 OI 712825.850 ETH**, 거래소 관측 `2026-11-13T08:40:58.208Z` (17:40:58.208 KST), 수집 `08:40:58.283718Z`, 내부 `status=VERIFIED`, blob SHA `6f9f874b21ab5e7dd6560198cc7a25f0e3c43be7`. 16:55 KST 관측 이후 갱신. Binance OI 또는 전체 시장 OI가 아님.
- GitHub Actions 최신 OKX 보조 `workflow_run` [#43395106807](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43395106807) (08:40:50 UTC)와 [#43394449629](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43394449629) (08:35:46 UTC) 모두 success. 독립 `schedule` 최근 성공 [#43385969455](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43385969455) (07:28:11 UTC) 및 [#43339979206](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43339979206) (00:48:23 UTC)은 인접한 5분 간격 실행이 아니므로 **독립 예약 2회 연속 성공 미입증**. 다른 워크플로의 예약 성공을 OKX 성공으로 계산하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 대조, 최신 job stdout↔저장 JSON SHA 직접 대조, 실제 생성된 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 이번 점검에서 입증하지 못함. 보고서 호출 규칙의 OKX 참조 지시만으로 실측 반영을 인정하지 않음. GitHub Actions 예약 실행 간격은 설정값과 실제 실행 시각이 다름; 근거 없는 성공 판정이나 무검증 코드 변경을 하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 16:58 KST
- 최신 15:45 KST 체크포인트를 먼저 읽고 OI 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 직접 조회. collector는 OKX 공개 API `ETH-USDT-SWAP` 단일 상품의 `oiCcy`(ETH), 응답 `code=0`, 관측시각 및 300초 신선도를 검사. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 709963.354 ETH**, 거래소 관측 `2026-11-13T07:55:54.388Z` (16:55:54.388 KST), 수집 `07:55:54.443907Z`, 내부 `status=VERIFIED`, blob SHA `b8dffd62da56c0b8330c20aa90723a8e7d70e21e`. 이전 15:40 KST 관측 대비 갱신. Binance OI 또는 전체 시장 OI 아님.
- GitHub Actions 최근 100건에서 보조 `workflow_run` [#43389272875](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43389272875) (07:55:45 UTC)와 [#43388675427](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43388675427) (07:50:49 UTC) success. 추가로 독립 `schedule` [#43385969455](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43385969455) (07:28:11 UTC) success 확인. 하지만 **독립 schedule의 인접 2회 연속 성공은 여전히 미입증**. workflow_run 성공을 schedule 성공으로 계산하지 않음.
- 별도 환경 OKX 원시 HTTP 요청은 DNS 해석 오류로 실패. 이번 실행의 job 원문 stdout↔저장 JSON SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영 미검증. JSON 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 상태 문서 외 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 15:45 KST
- 최신 14:31 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 확인. OKX 공개 API ETH-USDT-SWAP 단일 종목의 `oiCcy`(ETH), 응답 code=0, 관측시각 및 300초 신선도 검증 로직 유지. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- 조회 시점 main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 707633.577 ETH**, 관측 `2026-11-13T06:40:59.797Z` (15:40:59.797 KST), 수집 `06:40:59.855279Z`, 내부 `status=VERIFIED`, blob SHA `3765e398fb40c34c1d100574d7e0e1f5969f2132`. 14:25 KST 대비 갱신. Binance OI 또는 전체 시장 OI 아님.
- 보조 `workflow_run` [#43380379819](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43380379819) (06:40:51 UTC)와 [#43379783229](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43379783229) (06:35:40 UTC) success; jobs API에서 수집·신선도 검사·JSON 커밋 단계 모두 success 확인. 연속 실제 저장 커밋 [43ec0b1](https://github.com/changwookseo/eth-cvd-monitor/commit/43ec0b1b62d6e27bbbdd0c84d7c9ab064bd6f580) (06:41 UTC), [eba9768](https://github.com/changwookseo/eth-cvd-monitor/commit/eba97685b1fc74c5a8f93d4af3f96321ae920689) (06:35 UTC) 확인. 최신 커밋 diff의 OI 및 관측시각은 조회한 main JSON과 일치. 이는 독립 schedule 연속 성공이 아님.
- 전체 `event=schedule` 최근 100건에서 OKX 독립 예약 성공은 #43339979206 (00:48:23 UTC), #43293980765 (전날 19:48:48 UTC)로 인접 5분 예약 2회 연속 성공 미입증. 별도 OKX 원시 HTTP 응답 본문 대조, 최신 job stdout↔저장 JSON SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영도 미검증. 내부 VERIFIED만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 이번에는 상태 문서만 수정하고 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터는 변경하지 않음.

## 자동 복구 점검 — 2026-11-13 14:31 KST
- 직전 13:28 KST 체크포인트를 먼저 읽고 OI 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 직접 확인. 수집기는 OKX 공개 API `ETH-USDT-SWAP`의 `oiCcy`(ETH), 응답 `code=0`, 거래소 관측시각 및 300초 신선도를 검사. 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 709400.001 ETH**, 거래소 관측 `2026-11-13T05:25:51.966Z` (14:25:51.966 KST), 수집 `05:25:52.049006Z`, 내부 `status=VERIFIED`, blob SHA `16594aaf08b1b492878d3054211e47b32951afd1`. 직전 13:25 관측 대비 갱신. Binance OI 또는 전체 시장 OI 아님.
- [#43371966780](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43371966780) (05:25:45 UTC), [#43372534220](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43372534220) (05:31:07 UTC) 모두 보조 `workflow_run` success. 두 실행의 수집·신선도·커밋 단계 success 확인. 커밋 단계 success만으로 실제 신규 커밋을 뜻하지 않으며, 05:31 실행의 최신 저장 결과는 이번 점검에서 확인하지 못함.
- 독립 `schedule` 인접 2회 연속 성공 미입증. 별도 OKX 원시 HTTP 응답 직접 대조, 실행 원문 stdout↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영 미검증. 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 13:28 KST
- 직전 12:49 KST 체크포인트를 먼저 확인하고 OI 전체 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. collector는 OKX 공개 API의 ETH-USDT-SWAP 단일 종목 `oiCcy`(ETH), 응답 code=0, 관측시각 및 300초 신선도를 검사하며 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 설정이 유지됨.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 693020.604 ETH**, 관측 `2026-11-13T04:25:52.397Z` (13:25:52.397 KST), 수집 `04:25:52.475174Z`, 내부 `status=VERIFIED`, blob SHA `6c83a4aafdd60aad878d2c02214c018e8ea12614`. 직전 12:45 관측보다 갱신됨. Binance OI나 전체 시장 OI 아님.
- Actions 최근 실행 [#43365453308](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43365453308) (04:25:40 UTC) 및 [#43364907392](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43364907392) (04:20:46 UTC)는 모두 보조 `workflow_run` success. 연속 실행은 관측되지만 독립 예약 2회 성공으로 간주하지 않음.
- 전체 `event=schedule` 최근 100건에서 가장 최근 OKX 독립 예약 성공은 [#43339979206](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43339979206) (00:48:23 UTC), 그 전은 #43293980765 (전날 19:48:48 UTC). 5분 간격 인접 독립 예약 2회 성공은 입증되지 않음.
- 별도 OKX 원시 HTTP 본문 교차검증, 이번 실행 원문 로그↔저장 JSON SHA 직접 대조, 실제 완성 ETH ESI 2.0 보고서의 최신 OI 실측 반영은 이번 점검에서 확인되지 않음. collector 내부 VERIFIED는 전체 게이트 통과가 아님.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 12:49 KST
- 직전 12:02 KST 체크포인트를 먼저 읽고 OI 선행 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 및 보고서 호출 규칙을 직접 조회. 코드의 OKX 공개 API 단일 ETH-USDT-SWAP `oiCcy`(ETH), `code=0`, 거래소 관측시각, 300초 신선도 검증 로직 유지.
- main 최신 JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 656356.139 ETH**, 거래소 관측 `2026-11-13T03:45:56.095Z` (12:45:56.095 KST), 수집 `03:45:56.168883Z`, 내부 `status=VERIFIED`, blob SHA `5e9a3eb4de7783f92b6e3f7eeaf6515d16411dff`. 직전 12:01 관측 대비 연속 갱신. Binance 또는 시장 전체 OI 아님.
- 보조 `workflow_run` [#43361096419](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43361096419) (03:45:49 UTC) success; jobs API에서 API 수집·신선도 검증·JSON 커밋 단계 모두 success. 03:40:56 UTC [#43360574642](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43360574642) 역시 보조 `workflow_run` success. 성공한 커밋 단계가 반드시 신규 저장을 뜻하지는 않음(동일/더 최신 관측이면 SKIP 가능).
- GitHub 전체 `event=schedule` 최근 목록에서 OKX 독립 예약 성공 [#43339979206](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43339979206) (00:48:23 UTC)와 [#43293980765](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43293980765) (전날 19:48:48 UTC) 확인; 두 실행의 jobs 단계는 모두 success. 다만 5분 간격 인접 예약 2회가 아니며, 독립 schedule이 설정된 5분 주기대로 연속 실행되는 것은 입증되지 않음. 실제 연속 수집은 주로 보조 workflow_run 경로에서 관측.
- 별도 실행환경의 OKX 원시 HTTP 직접 요청은 DNS 해석 오류로 실패. 최신 실행 stdout↔저장 JSON SHA 직접 대조 및 실제 생성된 완성 ETH ESI 2.0 보고서의 실측 OI 반영도 미검증. 보고서 호출 규칙에 OKX OI 참조가 있다는 사실만으로 완성 보고서 반영을 인정하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 단계 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 이번에는 상태 문서만 수정하며 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터는 변경하지 않음.

## 자동 복구 점검 — 2026-11-13 12:02 KST
- 직전 10:53 KST 체크포인트 확인 후 OI 게이트만 재점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json` 재조회. 수집 코드는 OKX 공개 API의 ETH-USDT-SWAP `oiCcy`(ETH)와 관측시각·300초 신선도 검사를 수행하며, 워크플로에는 독립 `schedule`과 보조 `workflow_run`이 병존.
- 최신 main JSON: **OKX ETH-USDT-SWAP 단일 거래소 OI 658346.240 ETH**, 관측 `2026-11-13T03:01:09.945Z` (12:01:09.945 KST), 수집 `03:01:10.038530Z`, 내부 `status=VERIFIED`, blob SHA `018f9f7236603c6d44ec45782222653d5606acb4`. 10:50 관측보다 갱신됨. Binance OI나 전체 시장 OI 아님.
- [#43356071535](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43356071535) (03:01:02 UTC) 및 [#43355493378](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43355493378) (02:55:47 UTC)는 모두 **보조 `workflow_run` success**. 두 실행 jobs API에서 API 수집, 출력 신선도 검사, JSON 커밋 단계 모두 success 확인. 단, 단계 success는 실제 신규 커밋 발생 및 로그↔저장 SHA 대조까지 자동으로 입증하지 않음.
- 이번 조회의 최근 100개 전체 `event=schedule` 중 OKX 독립 예약 성공 [#43339979206](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43339979206) (00:48:23 UTC)을 추가 확인. 그 전 OKX 독립 예약 성공은 #43293980765 (전날 19:48:48 UTC). **인접한 독립 예약 2회 연속 성공은 확인되지 않음**.
- 별도 OKX 원시 HTTP 본문 대조, 이번 실행 stdout↔저장 JSON SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector 내부 VERIFIED는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 10:53 KST
- 직전 09:47 KST 체크포인트를 먼저 확인하고 OI 게이트만 재검증. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml`, `eth_oi_okx_latest.json`을 직접 조회. 독립 `schedule: 2-59/5 * * * *` 및 보조 `workflow_run` 설정 유지.
- main JSON 실측: **OKX ETH-USDT-SWAP 단일 거래소 OI 667991.613 ETH**, 관측 `2026-11-13T01:50:50.686Z` (10:50:50.686 KST), 수집 `01:50:50.767199Z`, `status=VERIFIED`, blob SHA `2bce438c37f284837e587af3849b117a2fa3d420`. 이전 09:45 관측 이후 갱신. Binance 또는 전체 시장 OI가 아님.
- 최근 [#43347276065](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43347276065) (01:45:40 UTC), [#43347873868](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43347873868) (01:50:43 UTC)는 모두 **보조 `workflow_run` success**. 각 jobs API에서 수집·신선도 검증·JSON 커밋 단계 success 확인. 독립 `schedule` 2회 연속 성공 증거로 인정하지 않음.
- 별도 환경에서 OKX 공개 API 원시 HTTP 호출 시 DNS 해석 오류로 실패. 이번 실행의 stdout↔저장 JSON SHA 직접 대조, 독립 예약 실행 인접 2회 연속 성공, 완성 ETH ESI 2.0 보고서에 최신 실측 OI 반영은 미검증. JSON의 내부 VERIFIED는 전체 게이트 통과를 뜻하지 않음.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지; 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 09:47 KST
- 최신 08:40 KST 체크포인트를 먼저 읽고 OI 게이트만 재점검. main의 `eth_oi_okx_live.py`와 `.github/workflows/eth-oi-okx.yml` 직접 확인. OKX public ETH-USDT-SWAP `oiCcy`(ETH), 관측시각, 300초 신선도 검사; 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 661973.990 ETH**, 관측 `2026-11-13T00:45:49.792Z` (09:45:49.792 KST), 수집 `00:45:49.879168Z`, 내부 `status=VERIFIED`, blob SHA `8782e0c24d55509644c49155802473339cabeacf`. 직전 08:35 대비 관측시각 갱신. Binance OI나 시장 전체 OI가 아님.
- 최근 [#43338965366](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43338965366) (00:40:48 UTC) 및 [#43339630087](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43339630087) (00:45:44 UTC) 모두 **보조 `workflow_run` success**. jobs API에서 두 실행 모두 API 수집·신선도 검사·JSON 커밋 단계 success 확인. 독립 `schedule`의 연속 성공으로 인정하지 않음.
- 이번 점검에서는 별도 OKX 원시 HTTP 본문 대조, 최신 stdout↔저장 JSON SHA 직접 대조, 독립 `schedule` 인접 2회 연속 성공, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 검증되지 않음. collector 내부 VERIFIED와 보조 workflow 성공만으로 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

## 자동 복구 점검 — 2026-11-13 08:40 KST
- 최신 07:47 KST 체크포인트를 먼저 확인하고 OI 선행 게이트만 점검. main의 `eth_oi_okx_live.py`, `.github/workflows/eth-oi-okx.yml` 검증: OKX 공개 API 단일 ETH-USDT-SWAP, `oiCcy` ETH, 거래소 시각 및 300초 신선도 검사, 독립 `schedule: 2-59/5 * * * *`와 보조 `workflow_run` 병존.
- main 최신 `eth_oi_okx_latest.json`: **OKX ETH-USDT-SWAP 단일 거래소 OI 663411.188 ETH**, 거래소 관측 `2026-11-12T23:35:41.422Z` (08:35:41.422 KST), 수집 `23:35:41.505593Z`, 내부 `status=VERIFIED`, blob SHA `c4140d6eb372e4d73f3e2f530a74fd129b5f19d5`. 07:45 대비 갱신. Binance 또는 전체 시장 OI가 아님.
- 최근 OKX 보조 실행 [#43330154133](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43330154133) (23:35:34 UTC) `workflow_run` success. 23:30 UTC 부근 보조 실행들도 success. 이는 독립 예약 실행 검증이 아님.
- GitHub Actions 전체 `event=schedule` 목록을 100건씩 3페이지 확인하고 OKX 워크플로 경로로 필터링: 최근 독립 OKX 예약 실행은 [#43293980765](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43293980765) (19:48:48 UTC, success), 그 이전 [#43213235886](https://github.com/changwookseo/eth-cvd-monitor/actions/runs/43213235886) (11:54:59 UTC, success). 독립 `schedule` 인접 2회 연속 성공은 미입증. 다른 워크플로의 `schedule` 성공을 OKX 성공으로 오인하지 않음.
- 별도 OKX 원시 HTTP 응답 직접 교차검증, 이번 실행 stdout↔저장 SHA 직접 대조, 완성 ETH ESI 2.0 보고서의 최신 실측 OI 반영은 미검증. collector의 `VERIFIED`만으로 OI 전체 게이트 통과 불가.
- **OI 전체 게이트 미통과; 펀딩비·선물 CVD 미진입; 전체 복구 미완료; 완료 알림 금지.** Binance Cron importer `CRONJOB_API_KEY` Secret 미등록 체크포인트 유지, 우회·노출·등록 없음. 기존 현물 CVD·기술지표·보고서 정본·7지표 가중치·180일 백데이터 변경 없음.

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
