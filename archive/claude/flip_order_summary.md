# Setup order (summary) since the HTF CBC flip -- MES + MGC 2m / 3m / 5m -- 2026-11-12 14:48 ET

Full tables (every chart, both counts, both exits, per setup type): flip_order_report.md, delivered in chat 11/12 (too large for the project). Script: claude/flip_order_study.py (`python3 flip_order_study.py MES:3 MGC:3 ...`, needs chop_sim.py, stretch_study.py, all_alerts_study.py).

Signals in the HTF direction numbered from the flip candle; same-type repeats within 7 candles ignored unless the earlier trade had closed. SHARED count. Avg pts / trade after costs (n), replay Jan 5 -> 11/12 (2m Jun 1 ->), live alerts 10/19 -> 11/12 (every directional alert type).

| Chart | Exits | Data | #1 | #2 | #3 | #4 | #5 | #6+ |
|---|---|---|---|---|---|---|---|---|
| MES 3m | bot | replay | -0.45 (1645) | -0.38 (766) | +0.26 (294) | -0.03 (113) | -0.09 (43) | -2.81 (19) |
| MES 3m | bot | live | +0.07 (286) | -0.69 (251) | -0.69 (203) | -0.14 (132) | -1.30 (122) | -0.87 (422) |
| MES 3m | chart | replay | -0.45 (1645) | -0.32 (766) | +0.34 (292) | +0.10 (112) | -0.21 (42) | -3.17 (18) |
| MES 3m | chart | live | +0.35 (286) | -0.19 (251) | -0.79 (203) | -0.05 (136) | -2.05 (120) | -1.20 (400) |
| MGC 3m | bot | replay | +0.44 (1251) | +0.74 (489) | -0.59 (142) | -3.62 (44) | +5.06 (13) | -3.62 (4) |
| MGC 3m | bot | live | -0.39 (364) | -0.29 (269) | -0.79 (229) | +0.46 (163) | +0.20 (122) | +0.30 (449) |
| MGC 3m | chart | replay | +0.29 (1251) | +0.67 (488) | -1.48 (144) | -0.86 (43) | -1.25 (14) | -0.40 (4) |
| MGC 3m | chart | live | -0.21 (364) | +0.72 (272) | -0.11 (229) | -0.33 (167) | +0.18 (123) | -0.07 (456) |
| MES 2m | bot | replay | -0.36 (1135) | -0.53 (619) | -0.77 (266) | -0.40 (112) | -0.55 (50) | -0.75 (43) |
| MES 2m | bot | live | -0.52 (544) | -0.51 (460) | -0.55 (323) | -0.97 (236) | -1.06 (199) | -1.20 (638) |
| MES 2m | chart | replay | -0.72 (1135) | -0.52 (619) | -0.67 (268) | -0.37 (112) | -0.20 (50) | -0.07 (42) |
| MES 2m | chart | live | -0.31 (544) | -0.61 (462) | -0.32 (325) | -0.60 (229) | -0.71 (198) | -1.09 (634) |
| MGC 2m | bot | replay | +0.04 (1284) | +0.05 (569) | -0.30 (223) | -0.28 (72) | -1.05 (23) | +0.77 (19) |
| MGC 2m | bot | live | +0.48 (454) | -0.27 (394) | +0.05 (295) | -0.48 (228) | -0.01 (196) | +0.17 (766) |
| MGC 2m | chart | replay | +0.05 (1284) | -0.13 (564) | -0.05 (219) | -0.70 (73) | +0.23 (22) | +0.54 (17) |
| MGC 2m | chart | live | +0.05 (454) | -0.66 (394) | -0.17 (298) | -0.43 (223) | +0.28 (193) | -0.13 (767) |
| MES 5m | bot | replay | -0.36 (1095) | -1.00 (561) | -0.87 (228) | -1.17 (79) | +0.47 (43) | -1.19 (23) |
| MES 5m | bot | live | -0.89 (187) | -0.24 (179) | -0.94 (131) | -0.82 (105) | -2.37 (97) | -0.87 (337) |
| MES 5m | chart | replay | -0.32 (1095) | -0.76 (565) | -0.70 (227) | -1.36 (79) | +0.85 (43) | -0.26 (24) |
| MES 5m | chart | live | -0.12 (188) | -0.93 (179) | -0.22 (140) | -0.14 (108) | -0.71 (99) | -0.84 (337) |
| MGC 5m | bot | replay | +0.68 (1061) | +0.08 (573) | -0.39 (219) | +3.24 (81) | -6.31 (23) | -9.30 (19) |
| MGC 5m | bot | live | +0.36 (202) | -1.98 (172) | +0.25 (115) | +1.12 (113) | +0.09 (83) | +0.05 (308) |
| MGC 5m | chart | replay | -0.09 (1061) | -0.36 (577) | -0.86 (224) | -0.69 (82) | -1.19 (23) | -2.31 (19) |
| MGC 5m | chart | live | +0.48 (202) | -0.98 (172) | +0.15 (120) | +0.32 (114) | +0.20 (86) | -0.56 (306) |

## Verdict lines from the script

**MES 3m**

- BOT exits / SHARED count: replay -- cut after #4: signals #5+ = 62 trades -57 (thirds -28 / -7 / -22), kept avg -0.34 vs all -0.36
-     live avg/trade: 1-1 +0.07, 1-2 -0.28, 1-3 -0.40, 1-4 -0.36, 1-5 -0.47; #6+ -0.87 (422); all -0.59 (1416)
- BOT exits / PER-TYPE count: replay -- cut after #2: signals #3+ = 32 trades -47 (thirds -2 / -16 / -29), kept avg -0.34 vs all -0.36
-     live avg/trade: 1-1 -0.44, 1-2 -0.60, 1-3 -0.58, 1-4 -0.59, 1-5 -0.59; #6+ -; all -0.59 (1416)
- CHART exits / SHARED count: replay -- cut after #4: signals #5+ = 60 trades -66 (thirds -28 / -10 / -28), kept avg -0.31 vs all -0.33
-     live avg/trade: 1-1 +0.35, 1-2 +0.10, 1-3 -0.14, 1-4 -0.13, 1-5 -0.36; #6+ -1.20 (400); all -0.60 (1396)
- CHART exits / PER-TYPE count: replay -- no cut-off where every later signal loses in all three thirds
-     live avg/trade: 1-1 -0.35, 1-2 -0.58, 1-3 -0.59, 1-4 -0.60, 1-5 -0.60; #6+ -; all -0.60 (1396)

**MGC 3m**

- BOT exits / SHARED count: replay -- cut after #2: signals #3+ = 203 trades -192 (thirds -60 / -110 / -22), kept avg +0.53 vs all +0.37
-     live avg/trade: 1-1 -0.39, 1-2 -0.35, 1-3 -0.47, 1-4 -0.32, 1-5 -0.26; #6+ +0.30 (449); all -0.11 (1596)
- BOT exits / PER-TYPE count: replay -- no cut-off where every later signal loses in all three thirds
-     live avg/trade: 1-1 -0.25, 1-2 -0.19, 1-3 -0.19, 1-4 -0.12, 1-5 -0.11; #6+ +1.02 (6); all -0.11 (1596)
- CHART exits / SHARED count: replay -- cut after #2: signals #3+ = 205 trades -269 (thirds -123 / -91 / -55), kept avg +0.40 vs all +0.22
-     live avg/trade: 1-1 -0.21, 1-2 +0.19, 1-3 +0.11, 1-4 +0.04, 1-5 +0.05; #6+ -0.07 (456); all +0.02 (1611)
- CHART exits / PER-TYPE count: replay -- cut after #1: signals #2+ = 125 trades -140 (thirds -62 / -62 / -16), kept avg +0.31 vs all +0.22
-     live avg/trade: 1-1 +0.06, 1-2 +0.03, 1-3 -0.00, 1-4 +0.01, 1-5 +0.01; #6+ +1.02 (7); all +0.02 (1611)

**MES 2m**

- BOT exits / SHARED count: replay -- cut after #1: signals #2+ = 1090 trades -640 (thirds -345 / -20 / -275), kept avg -0.36 vs all -0.47
-     live avg/trade: 1-1 -0.52, 1-2 -0.52, 1-3 -0.52, 1-4 -0.59, 1-5 -0.64; #6+ -1.20 (638); all -0.79 (2400)
- BOT exits / PER-TYPE count: replay -- no cut-off where every later signal loses in all three thirds
-     live avg/trade: 1-1 -0.66, 1-2 -0.76, 1-3 -0.79, 1-4 -0.79, 1-5 -0.79; #6+ +0.29 (4); all -0.79 (2400)
- CHART exits / SHARED count: replay -- no cut-off where every later signal loses in all three thirds
-     live avg/trade: 1-1 -0.31, 1-2 -0.45, 1-3 -0.42, 1-4 -0.44, 1-5 -0.47; #6+ -1.09 (634); all -0.64 (2392)
- CHART exits / PER-TYPE count: replay -- no cut-off where every later signal loses in all three thirds
-     live avg/trade: 1-1 -0.57, 1-2 -0.61, 1-3 -0.63, 1-4 -0.64, 1-5 -0.64; #6+ -1.12 (4); all -0.64 (2392)

**MGC 2m**

- BOT exits / SHARED count: replay -- cut after #4: signals #5+ = 42 trades -10 (thirds -1 / -9 / -0), kept avg -0.01 vs all -0.01
-     live avg/trade: 1-1 +0.48, 1-2 +0.13, 1-3 +0.11, 1-4 +0.01, 1-5 +0.01; #6+ +0.17 (766); all +0.06 (2333)
- BOT exits / PER-TYPE count: replay -- no cut-off where every later signal loses in all three thirds
-     live avg/trade: 1-1 -0.09, 1-2 +0.04, 1-3 +0.05, 1-4 +0.05, 1-5 +0.06; #6+ +1.01 (5); all +0.06 (2333)
- CHART exits / SHARED count: replay -- no cut-off where every later signal loses in all three thirds
-     live avg/trade: 1-1 +0.05, 1-2 -0.28, 1-3 -0.25, 1-4 -0.28, 1-5 -0.21; #6+ -0.13 (767); all -0.18 (2329)
- CHART exits / PER-TYPE count: replay -- no cut-off where every later signal loses in all three thirds
-     live avg/trade: 1-1 -0.28, 1-2 -0.18, 1-3 -0.19, 1-4 -0.19, 1-5 -0.18; #6+ -0.42 (2); all -0.18 (2329)

**MES 5m**

- BOT exits / SHARED count: replay -- cut after #1: signals #2+ = 934 trades -855 (thirds -448 / -391 / -16), kept avg -0.36 vs all -0.61
-     live avg/trade: 1-1 -0.89, 1-2 -0.57, 1-3 -0.67, 1-4 -0.70, 1-5 -0.93; #6+ -0.87 (337); all -0.91 (1036)
- BOT exits / PER-TYPE count: replay -- no cut-off where every later signal loses in all three thirds
-     live avg/trade: 1-1 -0.78, 1-2 -0.99, 1-3 -0.94, 1-4 -0.90, 1-5 -0.89; #6+ -5.56 (5); all -0.91 (1036)
- CHART exits / SHARED count: replay -- cut after #1: signals #2+ = 938 trades -665 (thirds -370 / -149 / -147), kept avg -0.32 vs all -0.50
-     live avg/trade: 1-1 -0.12, 1-2 -0.51, 1-3 -0.43, 1-4 -0.38, 1-5 -0.43; #6+ -0.84 (337); all -0.56 (1051)
- CHART exits / PER-TYPE count: replay -- cut after #1: signals #2+ = 219 trades -184 (thirds -113 / -10 / -60), kept avg -0.46 vs all -0.50
-     live avg/trade: 1-1 -0.52, 1-2 -0.61, 1-3 -0.57, 1-4 -0.53, 1-5 -0.52; #6+ -7.98 (5); all -0.56 (1051)

**MGC 5m**

- BOT exits / SHARED count: replay -- cut after #2: signals #3+ = 342 trades -144 (thirds -103 / -36 / -5), kept avg +0.47 vs all +0.31
-     live avg/trade: 1-1 +0.36, 1-2 -0.71, 1-3 -0.49, 1-4 -0.18, 1-5 -0.15; #6+ +0.05 (308); all -0.09 (993)
- BOT exits / PER-TYPE count: replay -- cut after #1: signals #2+ = 216 trades -256 (thirds -37 / -176 / -44), kept avg +0.50 vs all +0.31
-     live avg/trade: 1-1 -0.16, 1-2 -0.17, 1-3 -0.09, 1-4 -0.10, 1-5 -0.09; #6+ -; all -0.09 (993)
- CHART exits / SHARED count: replay -- cut after #1: signals #2+ = 925 trades -529 (thirds -307 / -130 / -92), kept avg -0.09 vs all -0.32
-     live avg/trade: 1-1 +0.48, 1-2 -0.19, 1-3 -0.11, 1-4 -0.03, 1-5 +0.00; #6+ -0.56 (306); all -0.17 (1000)
- CHART exits / PER-TYPE count: replay -- cut after #1: signals #2+ = 226 trades -232 (thirds -84 / -138 / -10), kept avg -0.23 vs all -0.32
-     live avg/trade: 1-1 +0.08, 1-2 -0.05, 1-3 -0.13, 1-4 -0.15, 1-5 -0.17; #6+ -0.28 (2); all -0.17 (1000)