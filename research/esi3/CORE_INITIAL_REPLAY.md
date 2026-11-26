# Core initial replay — exploratory, not validated
Direct connector calculation on 2519 aligned rows of stage3_extended_daily.csv and binance_spot_daily.csv, 2020-01-01 through 2026-11-23 UTC. No wave gating. Direction d=+1 buy,-1 sell. Targets unique local low/high in symmetric +/-5 bars, d*(close[i+10]/extreme[i]-1)>=0.05. Target indices 5<=i<n-10. Signals indices 10<=i<n-10, minimum 10 bars between signals per rule/direction. All require d*price_log_slope_5<0. A: d*(spot_cvd_normalized_5[i]-spot_cvd_normalized_5[i-1])>0, d*price_log_slope_5_acceleration>0, d*spot_cvd_normalized_5<0. B: d*spot_cvd_normalized_5>0. C: B plus oi_log_slope_5<0; missing values not imputed. Match target j with i<j<=i+5 (same-day UTC open availability may precede intraday extreme, exact time unknown). Return d*(close[i+10]/open[i+1]-1), no costs. 
Results columns signals, targets, matched signals, detected targets, positive returns, mean return:
buy A 112,115,25,25,68,0.027853534919588845
buy B 82,115,15,15,40,0.00968067565665172
buy C 46,115,8,8,22,0.007234083091508226
sell A 83,95,15,15,31,-0.042811295806770906
sell B 161,95,40,40,74,-0.022375895686295038
sell C 84,95,19,19,47,0.022573772502122717
Chronological slices by signal/target date separately (boundary matches excluded):
buy A pre2024 63,67,16,16,42,0.0390182091594337; 2024+ 49,48,9,9,26,0.013498953754074054
buy B pre2024 43,67,6,6,21,0.004143494730950592; 2024+ 39,48,9,9,19,0.015785772574732453
buy C pre2024 22,67,5,5,9,-0.005372937620009122; 2024+ 24,48,3,3,13,0.01879051874373246
sell A pre2024 52,55,10,10,17,-0.0524715393290438; 2024+ 31,40,5,5,14,-0.02660701635005506
sell B pre2024 93,55,25,25,39,-0.03725838286426742; 2024+ 68,40,15,15,35,-0.0020219058693622246
sell C pre2024 35,55,8,8,20,0.03399850496686623; 2024+ 49,40,11,11,27,0.014413249313020193
Limitations: exploratory thresholds chosen for this run, no independent holdout, no no-signal or price-only benchmark, no measured publication latency, no costs, OI missingness affects comparisons, target extreme is retrospective label, no exact intraday lead. No production changes. Calculation performed via connector, executable repository replay and individual event output not yet implemented. Research branch only.
