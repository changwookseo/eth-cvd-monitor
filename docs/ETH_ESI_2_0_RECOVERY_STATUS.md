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
