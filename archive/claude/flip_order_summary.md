# Setup order since the HTF CBC flip -- 2026-11-15 13:23 ET

STUDY SETTINGS STALE: settings sync 11/13 lists chop_sim.py `EXIT` MISMATCHes for MES 3m (part 'tod' 80/100 % vs live 100 % at TP1 all day, v10.95) and MGC 3m (50 % + trail 3.5 vs live FLIP 0 % / no trail, v10.96). The CHART-exit rows for MES 3m and MGC 3m below still use the old exits; BOT-exit rows and 2m / 5m are unaffected. Fix (not applied, read-only run): settings_sync_report.md section C items 2-3.

Script: claude/flip_order_study.py (unchanged, ran clean). Full report (~180 KB, every chart / both counts / both exits / per type) not saved to the project. Replay Jan 5 -> 11/13 (2m Jun 1 ->), live alerts 10/19 -> 11/13 (every directional alert type; duplicates collapse to one signal per candle / direction / type). Data notes: MGC 3m BarFeed gaps 11/08 22:12 -> 11/09 06:21 and 11/09 13:06 -> 11/10 01:33 -- live MGC 3m alerts in those hours have no candles and are dropped. Live alerts are re-scored with the study's own exits, so the old-exit second MGC 3m alert (11/09-11/12) does not affect the numbers.

SHARED count, avg pts / trade after costs (n):

| Chart | Exits | Data | #1 | #2 | #3 | #4 | #5 | #6+ |
|---|---|---|---|---|---|---|---|---|
| MES 3m | bot | replay | -0.49 (1649) | -0.41 (768) | +0.29 (295) | -0.03 (113) | -0.09 (43) | -2.81 (19) |
| MES 3m | bot | live | +0.22 (296) | -0.91 (261) | -0.68 (208) | +0.09 (136) | -1.05 (125) | -0.85 (424) |
| MES 3m | chart* | replay | -0.49 (1649) | -0.34 (768) | +0.36 (293) | +0.10 (112) | -0.21 (42) | -3.17 (18) |
| MES 3m | chart* | live | +0.53 (296) | -0.33 (260) | -0.77 (207) | +0.15 (141) | -1.80 (123) | -1.15 (403) |
| MGC 3m | bot | replay | +0.45 (1260) | +0.74 (491) | -0.59 (142) | -3.62 (44) | +5.06 (13) | -3.62 (4) |
| MGC 3m | bot | live | -0.42 (379) | -0.16 (286) | -0.81 (243) | +0.31 (172) | +0.08 (133) | +0.36 (496) |
| MGC 3m | chart* | replay | +0.29 (1260) | +0.66 (490) | -1.48 (144) | -0.86 (43) | -1.25 (14) | -0.40 (4) |
| MGC 3m | chart* | live | -0.25 (379) | +0.69 (289) | -0.13 (243) | -0.36 (176) | -0.01 (134) | -0.04 (504) |
| MES 2m | bot | replay | -0.34 (1137) | -0.54 (621) | -0.76 (268) | -0.31 (114) | -0.55 (50) | -0.75 (43) |
| MES 2m | bot | live | -0.50 (563) | -0.56 (478) | -0.43 (338) | -0.97 (251) | -0.93 (215) | -1.05 (688) |
| MES 2m | chart | replay | -0.72 (1137) | -0.54 (621) | -0.67 (270) | -0.30 (114) | -0.20 (50) | -0.07 (42) |
| MES 2m | chart | live | -0.29 (562) | -0.59 (480) | -0.20 (340) | -0.71 (246) | -0.84 (211) | -0.97 (686) |
| MGC 2m | bot | replay | +0.03 (1307) | +0.02 (581) | -0.27 (224) | -0.28 (72) | -1.05 (23) | +0.77 (19) |
| MGC 2m | bot | live | +0.31 (497) | -0.24 (433) | -0.01 (321) | -0.46 (251) | +0.09 (210) | +0.20 (817) |
| MGC 2m | chart | replay | +0.05 (1307) | -0.16 (576) | -0.02 (220) | -0.70 (73) | +0.23 (22) | +0.54 (17) |
| MGC 2m | chart | live | -0.06 (496) | -0.54 (432) | -0.22 (324) | -0.37 (248) | +0.35 (207) | -0.16 (817) |
| MES 5m | bot | replay | -0.41 (1099) | -1.04 (562) | -0.95 (229) | -1.17 (79) | +0.47 (43) | -1.19 (23) |
| MES 5m | bot | live | -0.80 (190) | -0.25 (180) | -0.87 (132) | -0.22 (110) | -2.34 (98) | -0.88 (341) |
| MES 5m | chart | replay | -0.34 (1099) | -0.78 (566) | -0.73 (228) | -1.36 (79) | +0.85 (43) | -0.26 (24) |
| MES 5m | chart | live | -0.04 (190) | -0.89 (180) | -0.12 (142) | +0.17 (113) | -0.66 (100) | -0.85 (341) |
| MGC 5m | bot | replay | +0.68 (1066) | +0.08 (573) | -0.39 (219) | +3.24 (81) | -6.31 (23) | -9.30 (19) |
| MGC 5m | bot | live | +0.17 (213) | -2.17 (184) | +0.08 (123) | +1.04 (119) | +0.27 (89) | -0.02 (346) |
| MGC 5m | chart | replay | -0.09 (1066) | -0.36 (577) | -0.86 (224) | -0.69 (82) | -1.19 (23) | -2.31 (19) |
| MGC 5m | chart | live | +0.35 (213) | -1.20 (184) | +0.07 (128) | +0.22 (120) | +0.00 (91) | -0.69 (344) |

\* chart exits for MES 3m / MGC 3m are the stale chop_sim EXIT values (see top).

## Verdict (rule checked for every N = 1..5; (a) replay #N+1+ negative in all 3 thirds under bot AND chart exits, (b) live #N+1+ (30+) net negative and below live 1..N, (c) kept 1..N avg beats all -- (b) and (c) required under both exits)

- **MES 3m -- N=4 meets the rule this week.** Replay #5+ bot 62 trades -57 (thirds -28 / -7 / -22), chart 60 trades -66 (-28 / -10 / -28); live #5+ bot -0.89 (549) vs 1-4 -0.33, chart -1.30 (526) vs -0.07; kept 1-4 beats all by only +0.01 (bot -0.37 vs -0.38). Tiny replay sample (62 of ~2,870); chart-exit rows on stale exits.
- **MGC 3m -- no.** Replay says "first 2 only" (#3+ bot -192, chart -269, all thirds negative) but live #3+ is positive under bot exits (+0.04, 1,044 trades vs 1-2 -0.31). Same disagreement as 11/12.
- **MES 2m -- no** (near miss at N=1). Bot exits pass (replay #2+ -345 / -20 / -266; live #2+ -0.80 vs #1 -0.50), but under chart exits keeping only #1 is worse than all (-0.72 vs -0.62).
- **MGC 2m -- no.** Replay #2+ positive in the middle and last thirds; live #N+1+ positive under bot exits for N >= 2.
- **MES 5m -- N=1 meets the rule this week.** Replay #2+ bot 936 trades -899 (-448 / -391 / -60), chart 940 trades -682 (-370 / -149 / -164); live #2+ bot -0.83 (861) vs #1 -0.80, chart -0.59 vs -0.04; kept #1 beats all (bot -0.41 vs -0.66, chart -0.34 vs -0.52). Caveat: #1 alone is still negative -- the cut loses less, it does not make the chart profitable. The bot-exit live gap is small (-0.83 vs -0.80).
- **MGC 5m -- no.** Replay agrees on N=2 (bot -103 / -36 / -5, chart -119 / -130 / -71) but live #3+ is positive under bot exits (+0.22 vs 1-2 -0.91).

If adopted, it needs a CBC Pine change -- no input exists today. Sketch (not built): under ▶ Bot / Trade Setups, an input "Max setups per HTF flip (0 = off)" plus an optional per symbol/timeframe list (e.g. "MES 3m 4, MES 5m 1"); CBC keeps a counter reset on every HTF CBC flip, increments it on each setup drawn in the HTF direction (same-type repeats within 7 candles not counted unless the earlier trade closed), and blocks the setup / bot order when the counter exceeds N (with a "Setup Blocked: past Nth since flip" alert).

## Tally (weeks qualifying, same N, consecutive runs; 3/3 needed)

| Chart | Weeks qualifying |
|---|---|
| MES 3m | N=4 1/3 (11/12 baseline numbers also fit the rule but the baseline did not count it -- 2/3 if counted) |
| MGC 3m | 0/3 |
| MES 2m | 0/3 |
| MGC 2m | 0/3 |
| MES 5m | N=1 1/3 (11/12 baseline numbers also fit the rule but the baseline did not count it -- 2/3 if counted) |
| MGC 5m | 0/3 |

## History (shared count, bot exits unless noted)

| Run | Data to | Qualifying this run | Notes |
|---|---|---|---|
| 2026-11-12 14:48 ET (week 0 baseline) | 11/12 | none (as judged then) | MGC 3m "first 2" replay -192 bot / -269 chart, live #4+ positive; MES 3m live #1 +0.07 vs #6+ -0.87; MES 2m live -0.52 -> -1.20 after #3; MES 5m negative everywhere |
| 2026-11-15 13:23 ET | 11/13 | MES 3m N=4; MES 5m N=1 | Settings stale (chop_sim EXIT MES 3m / MGC 3m). MES 3m live #1 +0.22 (bot) / +0.53 (chart) vs #6+ -0.85 / -1.15; MES 2m fails only on chart-exit (c); MGC 3m / MGC 5m replay vs live still disagree |
