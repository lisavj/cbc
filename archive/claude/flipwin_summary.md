# MES 3m flip exit by bot window -- 2026-11-14 (baseline, run 1)

Script: claude/flipwin_study.py. Weekly, Tuesdays ~5:25 PM ET. Baseline = current MES 3m filters + HTF EMA20 slope 0.3 (CBC EMA Slope v1.01), live exits.

| Window (candle close, ET) | Flip setups | TP1 exit | Flip + SL | Δ | Δ by third | Δ last 4 wk | z |
|---|---|---|---|---|---|---|---|
| 03:00-09:30 (bot window, TP1 bracket now) | 50 | -3 | +57 | +60 | +12 / +18 / +30 | +15 | +1.2 |
| 09:30-16:00 (bot flip-only window now) | 53 | -16 | +134 | +149 | +3 / -14 / +160 | +27 | +2.9 |
| 18:30-22:00 (bot window, TP1 bracket now) | 14 | -49 | -64 | -15 | -14 / -15 / +14 | +0 | -0.6 |
| other hours (bot does not trade) | 53 | -57 | -6 | +50 | +8 / +33 / +9 | -1 | +1.0 |

TOTAL: -107 -> +138, Δ +245, z 3.7, thirds +9 / +22 / +213, last 4 wk +41.

| Run | 03:00-09:30 Δ | 09:30-16:00 Δ | 18:30-22:00 Δ | TOTAL Δ | Tallies | Verdict |
|---|---|---|---|---|---|---|
| 11/14 | +60, z 1.2, all thirds + | +149, z 2.9 | -15 | +245, z 3.7 | 03:00-09:30: 0/3 (z < 1.5) | no change; branch flip exit HELD |
