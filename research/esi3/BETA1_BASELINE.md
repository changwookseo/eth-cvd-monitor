# ETH ESI 3.0 BETA 1

User-selected research baseline, not production deployment or integrated validation.

- Alarm: original OR rule in core_lead_lag.py and CORE_LEAD_LAG_REPLAY.json; historical recall buy 40.0%, sell 55.8%, matching next 1–5 bars (includes zero full-day lead). Recent stricter A replay recall 26.3%,39.4% under different cohort and 2–5 bar match.
- Buy confirmation: A baseline, normalized spot CVD improvement while negative, positive price slope acceleration, negative price slope; 5-day win 70/110, mean +1.6957% (CORE_ABC_REPLAY.json).
- Sell confirmation: positive 5-day price slope, negative normalized spot CVD and OI slope, close below 60-day prior close; 8-day win 30/40, mean +5.5775% (CORE_WAVE_HORIZON_REPLAY.json).
- B/C filters excluded; preserve research. Elliott and wave duration auxiliary only.
- Keep main and ESI2 unchanged. Metrics are separate exploratory cohorts, no costs or independent validation. Alarm is not a mandatory trade gate until sequential replay validates it.
- Future detection research: freeze baseline, compare on identical eligible dates, report 1–5 and 2–5 bar recall separately, precision, false alarms, lead, missed events; investigate slope window and onset horizon one at a time, then validate chronological robustness and publication latency. Prefer meaningful improvements; proposed 10 percentage point threshold is a review criterion, not proof of significance. No live deployment.
