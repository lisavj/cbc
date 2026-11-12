# Trade Setup Filters sweep -- 2026-11-07 09:51 ET (weekly run 2 -- rerun after data repair; replaces the 11/06 run)

One change at a time on top of each chart's live settings, base exits. Bars Jan 5 -> Nov 6 (2m Jun -> Nov 6). Previous report: 2026-11-06 20:13 ET (pre-repair). **Rerun after the BarFeed bar-data repair (MGC 3m had 5m candles mixed in; 2m/5m/3m gaps on other symbols). This run REPLACES the 11/06 run as weekly run 2** — run history: 11/01 = run 1, this = run 2; no new trading sessions since 11/06 (latest alert 11/06 18:01 ET). A 09:46 ET pass on the repaired bars gave identical results. Effect of the repair vs the 11/06 numbers: 5m outputs unchanged; 3m / 2m moved in the last third only (e.g. MGC 3m current net +186 → +278). Repaired bars checked: no off-grid timestamps on MGC 3m / MES 2m / MES 5m (a few short intraday gaps remain: MGC 3m 173, MES 2m 92, MES 5m 172 over the sample).

## Since last week

Consecutive weekly runs robust in brackets. Δ = net change vs current; thirds = Jan–Mar / Apr–Jun / Jul–now (2m: Jun–Jul / Aug / Sep–now). Comparisons "(11/06 …)" are vs the pre-repair 11/06 numbers.

- **MES 3m:** crosses ≥ 6 block +64, z 1.6, +18 / +33 / +13, promising (unchanged; [0]). Live: would block 1 (−5.0) vs rest 102 ended +14.4 — too few. (Crosses ≥ 4 is noise in the sim; live it would have blocked 14 ended **+51.5** — the good ones.)
- **MGC 3m:** crosses ≥ 4 block +167 (11/06 +183), z 1.8 (2.0), +110 / +54 / **+3** (Jul–now +18 → +3), promising [0]. Live: would block 11 (9 ended, win 33 %, −14.2, avg −1.57) vs rest 68 (60 ended, −23.1, avg −0.38) — agrees per trade but < 20 ended.
- **MES 2m:** all promising [0]: breakout exception OFF +144 (+139), z 1.6, +90 / +28 / +25; breakout window 1 bar +128 (+119), z 1.9, +75 / +28 / +25; CHOP > 58 +135, z 1.8, +22 / +3 / +109; CHOP > 61.8 +68, z 1.4, +25 / +11 / +33; 12-bar range < 3 ATR +154, z 1.6, +26 / +20 / +107. Live: CHOP > 58 blocked 17 ended −4.5 (avg −0.26) vs rest 99 ended −78.7 (avg −0.79); CHOP > 61.8 blocked 8 ended **+5.5**; range < 3 ATR blocked 32 ended **+13.0** (avg +0.41) vs rest −96.2 → live disagrees with all three blocks.
- **MGC 2m:** VWAP −3 / +2 block +71 (+68), z 1.1, +46 / +8 / +17, promising [0]. Live: blocked 21 (19 ended, −19.8, avg −1.04) vs rest 125 ended −43.9 (avg −0.35) — agrees, 19 ended (< 20). Max-SL-cap skip 1.5 +110 (+107), z 1.6, +15 / +20 / +75, promising [0]. Live: blocked 9 ended −15.8 vs rest −48.0.
- **MES 5m:** **ER threshold 0.18 robust [2]** +187, z 2.3, +37 / +51 / +99 (identical to 11/06). **ER 0.20 robust [2]** +137, z 2.2, +29 / +50 / +59. ER filter OFF +282, z 1.9, promising. VWAP stretch 3 / 4 / 6 ATR +161 / +120 / +98, promising. Live stretch: 3 ATR blocked 8 ended −2.4 vs rest −40.1; 4 / 6 ATR blocked 4 ended **+6.5** — live does not support.
- **MGC 5m (identical to 11/06):** ER 0.18 +120, z 1.4; CHOP > 58 +168, z 1.7; VWAP stretch 3 +184, z 1.4; stretch 6 +107, z 1.6; ATR > 1.8 × ATR(100) skip +46, z 1.2; ATR > 1.5 × skip +64, z 1.0 — all promising [0]. Live: CHOP > 58 blocked 12 ended, win 17 %, **−31.0** (avg −2.58) vs rest 37 ended −4.5; stretch 3 blocked 17 ended −30.6 (avg −1.80) vs rest −4.8; stretch 6 blocked 7 ended −7.5. Live agrees strongly but < 20 ended. ATR(100) skips can't be checked live.
- **Confirmed current (still worse when removed):** MGC 3m VWAP stretch OFF −90, MGC 3m ER OFF −89, MGC 2m ER OFF −64, MES 2m flip block OFF −8.

**Live split** (alerts 10/19 -> 11/6, Trade Setup "Filters:" line matched to the first "Setup Ended:" with same symbol, chart TF, direction and entry):

| Chart | Live setups w/ Filters line (first–last) | Candidate block | Would block | Rest |
|---|---|---|---|---|
| MES 3m | 116 (2026-10-19 – 2026-11-06) | X >= 6 (crosses block) | 1 setups, 1 ended, win 0%, net -5.0, avg -5.00 | 115 setups, 102 ended, win 47%, net +14.4, avg +0.14 |
| MES 3m | 116 (2026-10-19 – 2026-11-06) | X >= 4 (crosses block) | 16 setups, 14 ended, win 57%, net +51.5, avg +3.68 | 100 setups, 89 ended, win 45%, net -42.1, avg -0.47 |
| MES 3m | 116 (2026-10-19 – 2026-11-06) | CHOP > 61.8 | 15 setups, 11 ended, win 55%, net -3.6, avg -0.33 | 101 setups, 92 ended, win 46%, net +13.0, avg +0.14 |
| MGC 3m | 79 (2026-10-19 – 2026-11-06) | X >= 4 (crosses block) | 11 setups, 9 ended, win 33%, net -14.2, avg -1.57 | 68 setups, 60 ended, win 43%, net -23.1, avg -0.38 |
| MGC 3m | 79 (2026-10-19 – 2026-11-06) | CHOP > 61.8 | 6 setups, 5 ended, win 60%, net +6.5, avg +1.29 | 73 setups, 64 ended, win 41%, net -43.7, avg -0.68 |
| MES 2m | 126 (2026-10-19 – 2026-11-06) | CHOP > 58 | 21 setups, 17 ended, win 53%, net -4.5, avg -0.26 | 105 setups, 99 ended, win 41%, net -78.7, avg -0.79 |
| MES 2m | 126 (2026-10-19 – 2026-11-06) | CHOP > 61.8 | 10 setups, 8 ended, win 62%, net +5.5, avg +0.69 | 116 setups, 108 ended, win 42%, net -88.7, avg -0.82 |
| MES 2m | 126 (2026-10-19 – 2026-11-06) | Range < 3 ATR | 38 setups, 32 ended, win 53%, net +13.0, avg +0.41 | 88 setups, 84 ended, win 39%, net -96.2, avg -1.14 |
| MGC 2m | 157 (2026-10-19 – 2026-11-06) | VWAP -3/+2 pts (no candle-beyond check) | 21 setups, 19 ended, win 37%, net -19.8, avg -1.04 | 136 setups, 125 ended, win 48%, net -43.9, avg -0.35 |
| MGC 2m | 157 (2026-10-19 – 2026-11-06) | Max SL cap < 1.5 x ATR | 10 setups, 9 ended, win 44%, net -15.8, avg -1.76 | 147 setups, 135 ended, win 47%, net -48.0, avg -0.36 |
| MGC 2m | 157 (2026-10-19 – 2026-11-06) | CHOP > 58 | 31 setups, 29 ended, win 41%, net -24.6, avg -0.85 | 126 setups, 115 ended, win 48%, net -39.2, avg -0.34 |
| MES 5m | 64 (2026-10-20 – 2026-11-06) | VWAP stretch 3 ATR | 8 setups, 8 ended, win 50%, net -2.4, avg -0.31 | 56 setups, 50 ended, win 48%, net -40.1, avg -0.80 |
| MES 5m | 64 (2026-10-20 – 2026-11-06) | VWAP stretch 4 ATR | 4 setups, 4 ended, win 75%, net +6.5, avg +1.63 | 60 setups, 54 ended, win 46%, net -49.1, avg -0.91 |
| MES 5m | 64 (2026-10-20 – 2026-11-06) | VWAP stretch 6 ATR | 4 setups, 4 ended, win 75%, net +6.5, avg +1.63 | 60 setups, 54 ended, win 46%, net -49.1, avg -0.91 |
| MES 5m | 64 (2026-10-20 – 2026-11-06) | CHOP > 61.8 | 9 setups, 8 ended, win 38%, net -19.2, avg -2.40 | 55 setups, 50 ended, win 50%, net -23.4, avg -0.47 |
| MGC 5m | 52 (2026-10-21 – 2026-11-06) | CHOP > 58 | 13 setups, 12 ended, win 17%, net -31.0, avg -2.58 | 39 setups, 37 ended, win 54%, net -4.5, avg -0.12 |
| MGC 5m | 52 (2026-10-21 – 2026-11-06) | CHOP > 61.8 | 5 setups, 5 ended, win 40%, net -1.1, avg -0.23 | 47 setups, 44 ended, win 45%, net -34.3, avg -0.78 |
| MGC 5m | 52 (2026-10-21 – 2026-11-06) | VWAP stretch 3 ATR | 17 setups, 17 ended, win 35%, net -30.6, avg -1.80 | 35 setups, 32 ended, win 50%, net -4.8, avg -0.15 |
| MGC 5m | 52 (2026-10-21 – 2026-11-06) | VWAP stretch 6 ATR | 7 setups, 7 ended, win 43%, net -7.5, avg -1.07 | 45 setups, 42 ended, win 45%, net -27.9, avg -0.66 |

**Verdict: no change yet.** Only MES 5m ER 0.18 / 0.20 is robust, at 2 weekly runs (11/01 and this repaired-data rerun replacing 11/06). It is a loosening change, so live can't be checked; its recent third has been positive on both runs (+94, +99) and neighbour 0.20 is also robust. If it is robust again on the next Friday run (with the Nov 9-13 week in the data) it qualifies: ③ Trade Setup Filters → "Block in chop: Efficiency Ratio below" = 0.18 on the MES 5m chart's CBC only (the input is one value for all charts, so set it only on the MES 5m chart's CBC instance, or add a per-symbol list in a new CBC version), then recreate the MES 5m TradingView alert. MGC 3m crosses ≥ 4 slipped to z 1.8 with Jul–now down to +3.

---

## MES 3m — current (ER 0.23 + breakout 3 bars, range gate 24 / 20 % / 5 ATR): 1719 setups, win 50%, net +16

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1830 | 49% | -92 | -108 | -1.4 | -87 / -46 / +25 | worse |
| ER threshold 0.20 | 1792 | 50% | -28 | -44 | -0.7 | -63 / -1 / +20 | worse |
| ER threshold 0.26 | 1655 | 50% | -11 | -26 | -0.5 | -0 / -19 / -7 | worse |
| ER threshold 0.30 | 1587 | 50% | +22 | +6 | +0.1 | +40 / -6 / -27 | noise |
| ER filter OFF | 2117 | 50% | +1 | -14 | -0.1 | -95 / +21 / +59 | worse |
| ER breakout exception OFF | 1223 | 50% | -96 | -111 | -0.8 | -90 / +12 / -33 | worse |
| ER breakout window 1 bar | 1463 | 50% | -3 | -18 | -0.2 | -21 / +6 / -3 | worse |
| Choppiness Index > 61.8 block | 1602 | 50% | +101 | +85 | +1.3 | -24 / +34 / +75 | noise |
| Choppiness Index > 58 block | 1459 | 49% | -35 | -51 | -0.5 | -47 / -13 / +9 | worse |
| ADX < 20 block | 1173 | 48% | -167 | -183 | -1.4 | -70 / -64 / -50 | worse |
| ADX < 15 block | 1569 | 49% | -84 | -100 | -1.4 | -37 / -44 / -19 | worse |
| EMA20 / VWAP crosses >= 4 block | 1480 | 51% | +160 | +145 | +1.5 | -5 / +162 / -12 | noise |
| EMA20 / VWAP crosses >= 6 block | 1688 | 50% | +80 | +64 | +1.6 | +18 / +33 / +13 | promising |
| HTF EMA20 slope < 0.3 ATR block | 1226 | 49% | -35 | -51 | -0.4 | -19 / -18 / -13 | worse |
| HTF EMA20 slope < 0.2 ATR block | 1410 | 49% | +21 | +5 | +0.0 | +16 / -0 / -10 | noise |
| 12-bar range < 2 ATR block | 1695 | 50% | -29 | -45 | -1.6 | -40 / -15 / +10 | worse |
| 12-bar range < 3 ATR block | 1252 | 48% | -266 | -282 | -2.2 | -84 / -71 / -127 | worse |
| VWAP stretch 3 ATR | 1069 | 50% | +21 | +6 | +0.0 | -59 / +95 / -30 | noise |
| VWAP stretch 4 ATR | 1280 | 49% | -78 | -93 | -0.8 | -81 / +9 / -22 | worse |
| VWAP stretch 6 ATR | 1508 | 50% | -28 | -44 | -0.6 | -42 / -21 / +19 | worse |
| Range gate OFF | 2004 | 52% | +127 | +111 | +0.9 | +130 / +71 / -90 | noise |
| Range gate 24 / 20 % / 4 ATR | 1868 | 51% | +62 | +46 | +0.5 | +62 / +43 / -59 | noise |
| Range gate 24 / 20 % / 6 ATR | 1651 | 49% | -26 | -42 | -0.7 | +17 / -27 / -32 | worse |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1494 | 50% | -12 | -27 | -0.3 | -94 / +19 / +48 | worse |
| Block if EMA200 -3 / +2 pts | 1509 | 51% | +71 | +55 | +0.7 | -12 / +2 / +65 | noise |
| HTF flips >= 2 in 8 block | 674 | 48% | -58 | -74 | -0.4 | -51 / +174 / -197 | worse |
| HTF flips >= 3 in 8 block | 1417 | 50% | +59 | +43 | +0.4 | -16 / +93 / -35 | noise |
| HTF flips >= 4 in 8 block | 1663 | 50% | -14 | -30 | -0.6 | -9 / +13 / -33 | worse |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 1419 | 49% | +96 | +80 | +0.9 | -18 / +101 / -4 | noise |
| Skip while ATR > 1.8 x ATR(100) | 1655 | 50% | +21 | +5 | +0.1 | -33 / +57 / -19 | noise |
| Skip while ATR > 1.5 x ATR(100) | 1558 | 50% | +32 | +17 | +0.2 | +26 / +59 / -68 | noise |

Candidates: EMA20 / VWAP crosses >= 6 block → +64, z +1.6, +18 / +33 / +13 (promising)

## MGC 3m — current (ER 0.23 + breakout 3 bars, range gate 24 / 20 % / 5 ATR, VWAP stretch 4.0 ATR): 1180 setups, win 51%, net +278

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1266 | 50% | +235 | -42 | -0.6 | +6 / -6 / -43 | worse |
| ER threshold 0.20 | 1237 | 50% | +257 | -21 | -0.3 | +18 / -11 / -27 | worse |
| ER threshold 0.26 | 1146 | 51% | +299 | +22 | +0.5 | +33 / +18 / -29 | noise |
| ER threshold 0.30 | 1100 | 50% | +277 | -1 | -0.0 | +31 / +11 / -43 | worse |
| ER filter OFF | 1450 | 50% | +189 | -89 | -0.7 | -103 / +56 / -42 | worse |
| ER breakout exception OFF | 839 | 50% | +55 | -222 | -1.8 | -144 / -47 / -31 | worse |
| ER breakout window 1 bar | 1016 | 50% | +134 | -143 | -1.6 | -103 / +8 / -48 | worse |
| Choppiness Index > 61.8 block | 1118 | 51% | +306 | +28 | +0.5 | +3 / +45 / -20 | noise |
| Choppiness Index > 58 block | 1036 | 52% | +269 | -8 | -0.1 | -22 / +78 / -63 | worse |
| ADX < 20 block | 799 | 49% | +46 | -232 | -2.0 | -142 / -18 / -72 | worse |
| ADX < 15 block | 1104 | 51% | +264 | -13 | -0.2 | -84 / +3 / +67 | worse |
| EMA20 / VWAP crosses >= 4 block | 997 | 52% | +445 | +167 | +1.8 | +110 / +54 / +3 | promising |
| EMA20 / VWAP crosses >= 6 block | 1155 | 51% | +303 | +26 | +0.7 | +15 / -2 / +13 | noise |
| HTF EMA20 slope < 0.3 ATR block | 672 | 51% | +237 | -40 | -0.3 | -4 / +25 / -61 | worse |
| HTF EMA20 slope < 0.2 ATR block | 850 | 50% | +177 | -100 | -0.8 | -31 / -26 / -44 | worse |
| 12-bar range < 2 ATR block | 1171 | 50% | +240 | -37 | -1.8 | -23 / -10 / -4 | worse |
| 12-bar range < 3 ATR block | 894 | 51% | +171 | -106 | -1.0 | -125 / +33 / -14 | worse |
| VWAP stretch 3 ATR | 989 | 51% | +206 | -72 | -0.8 | -39 / -53 / +20 | worse |
| VWAP stretch 6 ATR | 1460 | 50% | +168 | -109 | -1.0 | -103 / +54 / -60 | worse |
| VWAP stretch OFF | 1753 | 50% | +187 | -90 | -0.6 | -67 / +62 / -85 | worse |
| Range gate OFF | 1342 | 52% | +353 | +76 | +0.7 | +97 / -53 / +32 | noise |
| Range gate 24 / 20 % / 4 ATR | 1277 | 51% | +370 | +92 | +1.2 | +83 / -28 / +37 | noise |
| Range gate 24 / 20 % / 6 ATR | 1124 | 50% | +215 | -63 | -1.0 | -28 / -18 / -17 | worse |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1022 | 52% | +375 | +98 | +1.2 | +25 / +95 / -22 | noise |
| Block if EMA200 -3 / +2 pts | 1021 | 51% | +267 | -11 | -0.1 | -61 / +23 / +27 | worse |
| HTF flips >= 2 in 8 block | 391 | 50% | +115 | -163 | -1.0 | -73 / +73 / -162 | worse |
| HTF flips >= 3 in 8 block | 902 | 51% | +210 | -68 | -0.6 | -55 / +74 / -87 | worse |
| HTF flips >= 4 in 8 block | 1126 | 50% | +255 | -22 | -0.5 | +1 / +18 / -41 | worse |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 733 | 49% | +136 | -142 | -1.1 | -76 / -28 / -39 | worse |
| Skip while ATR > 1.8 x ATR(100) | 1144 | 50% | +234 | -43 | -1.1 | -19 / -23 / -1 | worse |
| Skip while ATR > 1.5 x ATR(100) | 1073 | 50% | +234 | -43 | -0.6 | -12 / -42 / +10 | worse |

Candidates: EMA20 / VWAP crosses >= 4 block → +167, z +1.8, +110 / +54 / +3 (promising)

## MES 2m — current (ER 0.23 + breakout 3 bars, 1H MTF gate, HTF flips >= 4 in 8): 1173 setups, win 49%, net -186

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1250 | 49% | -201 | -15 | -0.2 | -7 / -37 / +29 | worse |
| ER threshold 0.20 | 1219 | 48% | -223 | -37 | -0.7 | -42 / -25 / +30 | worse |
| ER threshold 0.26 | 1122 | 49% | -184 | +2 | +0.0 | -19 / -1 / +23 | noise |
| ER threshold 0.30 | 1071 | 49% | -164 | +21 | +0.3 | +0 / +1 / +20 | noise |
| ER filter OFF | 1426 | 51% | -10 | +176 | +1.5 | +100 / -6 / +82 | noise |
| ER breakout exception OFF | 917 | 50% | -42 | +144 | +1.6 | +90 / +28 / +25 | promising |
| ER breakout window 1 bar | 1060 | 50% | -58 | +128 | +1.9 | +75 / +28 / +25 | promising |
| Choppiness Index > 61.8 block | 1108 | 49% | -117 | +68 | +1.4 | +25 / +11 / +33 | promising |
| Choppiness Index > 58 block | 997 | 50% | -51 | +135 | +1.8 | +22 / +3 / +109 | promising |
| ADX < 20 block | 798 | 48% | -193 | -8 | -0.1 | +18 / +2 / -28 | worse |
| ADX < 15 block | 1073 | 49% | -160 | +26 | +0.5 | -4 / +17 / +12 | noise |
| EMA20 / VWAP crosses >= 4 block | 1021 | 47% | -240 | -54 | -0.7 | -18 / -43 / +7 | worse |
| EMA20 / VWAP crosses >= 6 block | 1140 | 48% | -231 | -45 | -1.2 | -43 / -18 / +16 | worse |
| HTF EMA20 slope < 0.3 ATR block | 943 | 48% | -145 | +41 | +0.4 | +76 / -42 / +7 | noise |
| HTF EMA20 slope < 0.2 ATR block | 1055 | 48% | -172 | +13 | +0.2 | +58 / -29 / -16 | noise |
| 12-bar range < 2 ATR block | 1158 | 49% | -189 | -3 | -0.2 | +4 / -3 / -4 | worse |
| 12-bar range < 3 ATR block | 849 | 51% | -32 | +154 | +1.6 | +26 / +20 / +107 | promising |
| VWAP stretch 3 ATR | 531 | 49% | -130 | +56 | +0.5 | +50 / -53 / +59 | noise |
| VWAP stretch 4 ATR | 664 | 49% | -108 | +78 | +0.7 | +22 / -19 / +75 | noise |
| VWAP stretch 6 ATR | 874 | 49% | -148 | +37 | +0.4 | -3 / -27 / +67 | noise |
| Range gate 24 / 20 % / 4 ATR | 1098 | 49% | -126 | +60 | +1.1 | +62 / -14 / +12 | noise |
| Range gate 24 / 20 % / 5 ATR | 1025 | 48% | -161 | +25 | +0.3 | +9 / -10 / +25 | noise |
| Range gate 24 / 20 % / 6 ATR | 975 | 47% | -208 | -22 | -0.2 | -34 / -23 / +35 | worse |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1061 | 49% | -134 | +52 | +1.0 | +55 / -14 / +11 | noise |
| Block if EMA200 -3 / +2 pts | 1066 | 49% | -180 | +6 | +0.1 | +2 / -11 / +14 | noise |
| HTF flips >= 2 in 8 block | 457 | 47% | -148 | +38 | +0.3 | +28 / -55 / +64 | noise |
| HTF flips >= 3 in 8 block | 1004 | 49% | -146 | +40 | +0.6 | +1 / +1 / +38 | noise |
| HTF flips block OFF | 1226 | 49% | -194 | -8 | -0.2 | -16 / +2 / +6 | worse |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 1079 | 48% | -163 | +22 | +0.5 | +96 / -51 / -22 | noise |
| Skip while ATR > 1.8 x ATR(100) | 1148 | 49% | -180 | +6 | +0.2 | +52 / -36 / -11 | noise |
| Skip while ATR > 1.5 x ATR(100) | 1116 | 49% | -170 | +15 | +0.4 | +76 / -78 / +17 | noise |

Candidates: ER breakout exception OFF → +144, z +1.6, +90 / +28 / +25 (promising); ER breakout window 1 bar → +128, z +1.9, +75 / +28 / +25 (promising); Choppiness Index > 61.8 block → +68, z +1.4, +25 / +11 / +33 (promising); Choppiness Index > 58 block → +135, z +1.8, +22 / +3 / +109 (promising); 12-bar range < 3 ATR block → +154, z +1.6, +26 / +20 / +107 (promising)

## MGC 2m — current (ER 0.23 + breakout 3 bars): 1499 setups, win 52%, net +340

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1618 | 52% | +340 | -0 | -0.0 | +59 / -29 / -30 | worse |
| ER threshold 0.20 | 1571 | 52% | +352 | +11 | +0.2 | +38 / -8 / -19 | noise |
| ER threshold 0.26 | 1432 | 52% | +374 | +34 | +0.6 | +14 / +5 / +14 | noise |
| ER threshold 0.30 | 1347 | 53% | +401 | +60 | +0.7 | -20 / +27 / +53 | noise |
| ER filter OFF | 1864 | 51% | +276 | -64 | -0.4 | -20 / +27 / -71 | worse |
| ER breakout exception OFF | 1179 | 52% | +210 | -130 | -1.2 | -97 / -28 / -5 | worse |
| ER breakout window 1 bar | 1366 | 52% | +254 | -86 | -1.1 | -75 / -1 / -9 | worse |
| Choppiness Index > 61.8 block | 1421 | 52% | +365 | +24 | +0.4 | -71 / +65 / +30 | noise |
| Choppiness Index > 58 block | 1325 | 53% | +433 | +92 | +1.2 | -25 / +46 / +71 | noise |
| ADX < 20 block | 1038 | 52% | +365 | +25 | +0.2 | +10 / -57 / +72 | noise |
| ADX < 15 block | 1363 | 52% | +298 | -42 | -0.6 | -65 / +6 / +16 | worse |
| EMA20 / VWAP crosses >= 4 block | 1300 | 51% | +295 | -45 | -0.5 | +16 / -41 / -21 | worse |
| EMA20 / VWAP crosses >= 6 block | 1469 | 52% | +338 | -2 | -0.1 | -23 / +4 / +17 | worse |
| HTF EMA20 slope < 0.3 ATR block | 1022 | 50% | +170 | -170 | -1.3 | +60 / -81 / -149 | worse |
| HTF EMA20 slope < 0.2 ATR block | 1209 | 52% | +310 | -31 | -0.3 | +94 / +3 / -128 | worse |
| 12-bar range < 2 ATR block | 1488 | 52% | +338 | -2 | -0.1 | -6 / +10 / -6 | worse |
| 12-bar range < 3 ATR block | 1157 | 54% | +440 | +99 | +0.9 | -40 / +58 / +82 | noise |
| VWAP stretch 3 ATR | 731 | 53% | +275 | -66 | -0.5 | +89 / -119 / -36 | worse |
| VWAP stretch 4 ATR | 857 | 53% | +300 | -41 | -0.3 | +69 / -91 / -18 | worse |
| VWAP stretch 6 ATR | 1058 | 52% | +306 | -34 | -0.3 | +9 / -60 / +16 | worse |
| Range gate 24 / 20 % / 4 ATR | 1408 | 52% | +352 | +11 | +0.2 | +50 / -49 / +9 | noise |
| Range gate 24 / 20 % / 5 ATR | 1291 | 52% | +386 | +46 | +0.4 | +91 / -62 / +17 | noise |
| Range gate 24 / 20 % / 6 ATR | 1229 | 52% | +356 | +16 | +0.1 | +53 / -40 / +2 | noise |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1380 | 52% | +412 | +71 | +1.1 | +46 / +8 / +17 | promising |
| Block if EMA200 -3 / +2 pts | 1311 | 51% | +225 | -116 | -1.5 | -36 / -8 / -72 | worse |
| HTF flips >= 2 in 8 block | 519 | 50% | +89 | -251 | -1.5 | -72 / -120 / -59 | worse |
| HTF flips >= 3 in 8 block | 1179 | 52% | +292 | -48 | -0.5 | +62 / -65 / -45 | worse |
| HTF flips >= 4 in 8 block | 1438 | 52% | +325 | -15 | -0.3 | +15 / -12 / -19 | worse |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 1329 | 53% | +451 | +110 | +1.6 | +15 / +20 / +75 | promising |
| Skip while ATR > 1.8 x ATR(100) | 1467 | 52% | +346 | +6 | +0.2 | -21 / -7 / +34 | noise |
| Skip while ATR > 1.5 x ATR(100) | 1392 | 52% | +305 | -35 | -0.6 | -46 / -22 / +32 | worse |

Candidates: Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) → +71, z +1.1, +46 / +8 / +17 (promising); Skip if Max ATR SL1 cap < 1.5 x ATR → +110, z +1.6, +15 / +20 / +75 (promising)

## MES 5m — current (ER 0.23 + breakout 3 bars): 1183 setups, win 51%, net -9

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1256 | 52% | +179 | +187 | +2.3 | +37 / +51 / +99 | robust |
| ER threshold 0.20 | 1228 | 52% | +128 | +137 | +2.2 | +29 / +50 / +59 | robust |
| ER threshold 0.26 | 1139 | 51% | -53 | -44 | -0.7 | +23 / -71 / +4 | worse |
| ER threshold 0.30 | 1087 | 50% | -61 | -52 | -0.6 | +46 / -103 / +5 | worse |
| ER filter OFF | 1438 | 53% | +273 | +282 | +1.9 | +146 / +70 / +66 | promising |
| ER breakout exception OFF | 875 | 51% | -121 | -112 | -0.9 | +39 / -78 / -73 | worse |
| ER breakout window 1 bar | 1042 | 51% | -113 | -104 | -1.2 | +5 / -93 / -16 | worse |
| Choppiness Index > 61.8 block | 1102 | 52% | +93 | +102 | +1.5 | +33 / -9 / +78 | noise |
| Choppiness Index > 58 block | 1005 | 52% | +42 | +51 | +0.5 | -42 / +29 / +64 | noise |
| ADX < 20 block | 784 | 51% | +42 | +51 | +0.4 | +20 / +61 / -30 | noise |
| ADX < 15 block | 1065 | 51% | +35 | +44 | +0.6 | +32 / -31 / +43 | noise |
| EMA20 / VWAP crosses >= 4 block | 966 | 50% | -102 | -93 | -0.8 | -0 / -129 / +36 | worse |
| EMA20 / VWAP crosses >= 6 block | 1148 | 51% | -68 | -59 | -1.1 | -49 / -41 / +32 | worse |
| HTF EMA20 slope < 0.3 ATR block | 848 | 49% | -109 | -100 | -0.7 | +16 / -82 / -35 | worse |
| HTF EMA20 slope < 0.2 ATR block | 962 | 50% | -111 | -102 | -0.9 | +39 / -117 / -24 | worse |
| 12-bar range < 2 ATR block | 1169 | 51% | +24 | +33 | +1.3 | +20 / -1 / +14 | noise |
| 12-bar range < 3 ATR block | 867 | 51% | -7 | +2 | +0.0 | -34 / -2 / +38 | noise |
| VWAP stretch 3 ATR | 894 | 53% | +153 | +161 | +1.5 | +97 / +7 / +58 | promising |
| VWAP stretch 4 ATR | 1008 | 52% | +112 | +120 | +1.5 | +97 / +13 / +10 | promising |
| VWAP stretch 6 ATR | 1109 | 52% | +89 | +98 | +1.7 | +32 / +55 / +11 | promising |
| Range gate 24 / 20 % / 4 ATR | 1099 | 50% | -42 | -33 | -0.5 | +30 / -37 / -26 | worse |
| Range gate 24 / 20 % / 5 ATR | 999 | 50% | +18 | +26 | +0.2 | +56 / -38 / +8 | noise |
| Range gate 24 / 20 % / 6 ATR | 966 | 50% | +70 | +79 | +0.7 | +69 / +8 / +1 | noise |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1031 | 51% | -84 | -76 | -0.9 | -31 / +69 / -114 | worse |
| Block if EMA200 -3 / +2 pts | 1090 | 52% | +55 | +64 | +1.0 | +42 / +12 / +10 | noise |
| HTF flips >= 2 in 8 block | 441 | 49% | -156 | -147 | -0.9 | +3 / -83 / -67 | worse |
| HTF flips >= 3 in 8 block | 967 | 50% | -133 | -125 | -1.3 | -19 / -29 / -77 | worse |
| HTF flips >= 4 in 8 block | 1137 | 51% | -4 | +4 | +0.1 | -16 / +23 / -2 | noise |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 790 | 48% | -25 | -16 | -0.1 | +89 / -152 / +47 | worse |
| Skip while ATR > 1.8 x ATR(100) | 1114 | 50% | -82 | -73 | -1.3 | +12 / -26 / -59 | worse |
| Skip while ATR > 1.5 x ATR(100) | 1010 | 50% | -45 | -36 | -0.4 | +23 / -92 / +34 | worse |

Candidates: ER threshold 0.18 → +187, z +2.3, +37 / +51 / +99 (robust); ER threshold 0.20 → +137, z +2.2, +29 / +50 / +59 (robust); ER filter OFF → +282, z +1.9, +146 / +70 / +66 (promising); VWAP stretch 3 ATR → +161, z +1.5, +97 / +7 / +58 (promising); VWAP stretch 4 ATR → +120, z +1.5, +97 / +13 / +10 (promising); VWAP stretch 6 ATR → +98, z +1.7, +32 / +55 / +11 (promising)

## MGC 5m — current (ER 0.23 + breakout 3 bars): 1173 setups, win 51%, net -117

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1250 | 52% | +3 | +120 | +1.4 | +33 / +64 / +23 | promising |
| ER threshold 0.20 | 1216 | 52% | -74 | +43 | +0.6 | +15 / +22 / +6 | noise |
| ER threshold 0.26 | 1116 | 51% | -33 | +84 | +1.4 | -13 / +84 / +13 | noise |
| ER threshold 0.30 | 1060 | 51% | -85 | +32 | +0.4 | -16 / +35 / +13 | noise |
| ER filter OFF | 1477 | 52% | -61 | +56 | +0.3 | -29 / +47 / +38 | noise |
| ER breakout exception OFF | 866 | 52% | -79 | +38 | +0.3 | +69 / -51 / +20 | noise |
| ER breakout window 1 bar | 1019 | 51% | -197 | -80 | -0.8 | -6 / -40 / -34 | worse |
| Choppiness Index > 61.8 block | 1087 | 51% | -44 | +74 | +1.0 | +21 / +30 / +22 | noise |
| Choppiness Index > 58 block | 994 | 52% | +51 | +168 | +1.7 | +51 / +51 / +66 | promising |
| ADX < 20 block | 768 | 52% | +62 | +179 | +1.3 | +114 / -47 / +112 | noise |
| ADX < 15 block | 1064 | 51% | -94 | +23 | +0.3 | -4 / +15 / +11 | noise |
| EMA20 / VWAP crosses >= 4 block | 976 | 51% | -57 | +60 | +0.5 | -27 / +7 / +80 | noise |
| EMA20 / VWAP crosses >= 6 block | 1139 | 51% | -169 | -51 | -1.0 | -2 / -49 / -0 | worse |
| HTF EMA20 slope < 0.3 ATR block | 823 | 51% | -25 | +92 | +0.6 | +22 / -85 / +155 | noise |
| HTF EMA20 slope < 0.2 ATR block | 965 | 50% | -106 | +11 | +0.1 | -1 / -88 / +100 | noise |
| 12-bar range < 2 ATR block | 1157 | 51% | -125 | -8 | -0.2 | -12 / -3 / +7 | worse |
| 12-bar range < 3 ATR block | 826 | 51% | -23 | +94 | +0.7 | +49 / +40 / +5 | noise |
| VWAP stretch 3 ATR | 783 | 53% | +67 | +184 | +1.4 | +54 / +66 / +63 | promising |
| VWAP stretch 4 ATR | 929 | 51% | -60 | +57 | +0.5 | +15 / -4 / +46 | noise |
| VWAP stretch 6 ATR | 1070 | 52% | -11 | +107 | +1.6 | +11 / +61 / +35 | promising |
| Range gate 24 / 20 % / 4 ATR | 1105 | 51% | -74 | +43 | +0.5 | -47 / +23 / +68 | noise |
| Range gate 24 / 20 % / 5 ATR | 1018 | 51% | -49 | +68 | +0.6 | -89 / +43 / +113 | noise |
| Range gate 24 / 20 % / 6 ATR | 977 | 51% | -38 | +79 | +0.6 | -80 / -9 / +168 | noise |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1082 | 51% | -76 | +41 | +0.6 | +34 / +52 / -45 | noise |
| Block if EMA200 -3 / +2 pts | 1109 | 51% | -145 | -28 | -0.5 | +25 / -32 / -22 | worse |
| HTF flips >= 2 in 8 block | 405 | 48% | -142 | -25 | -0.1 | +75 / -99 / -1 | worse |
| HTF flips >= 3 in 8 block | 933 | 49% | -300 | -183 | -1.7 | -96 / -23 / -64 | worse |
| HTF flips >= 4 in 8 block | 1117 | 50% | -189 | -72 | -1.2 | -14 / -22 / -35 | worse |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 456 | 49% | -5 | +112 | +0.6 | +109 / -92 / +95 | noise |
| Skip while ATR > 1.8 x ATR(100) | 1148 | 51% | -71 | +46 | +1.2 | +12 / +25 / +9 | promising |
| Skip while ATR > 1.5 x ATR(100) | 1104 | 51% | -53 | +64 | +1.0 | +27 / +22 / +15 | promising |

Candidates: ER threshold 0.18 → +120, z +1.4, +33 / +64 / +23 (promising); Choppiness Index > 58 block → +168, z +1.7, +51 / +51 / +66 (promising); VWAP stretch 3 ATR → +184, z +1.4, +54 / +66 / +63 (promising); VWAP stretch 6 ATR → +107, z +1.6, +11 / +61 / +35 (promising); Skip while ATR > 1.8 x ATR(100) → +46, z +1.2, +12 / +25 / +9 (promising); Skip while ATR > 1.5 x ATR(100) → +64, z +1.0, +27 / +22 / +15 (promising)

