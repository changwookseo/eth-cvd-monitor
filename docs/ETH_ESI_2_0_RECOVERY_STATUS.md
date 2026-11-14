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
