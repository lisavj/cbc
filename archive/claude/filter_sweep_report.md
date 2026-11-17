# Trade Setup Filters sweep -- 2026-11-13 20:13 ET (weekly run 3)

One change at a time on top of each chart's live settings, base exits (ss.QB). Bars Jan 5 -> Nov 13 16:55 ET (2m Jun 1 -> Nov 13). Run history: 11/01 = run 1, 11/07 (repaired-data rerun replacing 11/06) = run 2, this = run 3. **MGC 2m: scripts now include the live range gate (v10.77) → this is MGC 2m run 1**; its "Range gate OFF" row is the pre-v10.77 setting. The third column header still says "Jul–Oct" but the last third runs Jul -> Nov 13.

**Settings check:** settings_sync_report (11/13 16:47) lists 3 MISMATCHes (chop_sim `EXIT` MES 3m 'tod' vs 100 % all day; chop_sim `EXIT` MGC 3m 50 % / trail 3.5 vs FLIP 0 % (v10.96); mes3_ema_grid `LIVE`). This sweep and the range-gate scripts pass base exits (`ss.QB`) to every run, so the chop_sim `EXIT` mismatch does not enter these numbers; gates (`GATE`, filter_sweep `LIVE`) match v10.96.

## Since last week

Consecutive weekly runs robust in [brackets]. Δ = net change vs current; thirds = Jan–Mar / Apr–Jun / Jul–Nov (2m: Jun–Jul / Aug / Sep–Nov). "was" = 11/07 run 2.

- **MES 3m:** crosses ≥ 6 block +64, z 1.5, +18 / +33 / +13, promising [0] (was +64, z 1.6 — unchanged). Live: would block 1 (−5.0) vs rest 107 ended −23.0 — too few. (Crosses ≥ 4 is noise in the sim; live it would block 15 ended **+62.9**, avg +4.20 — the good ones.)
- **MGC 3m:** crosses ≥ 4 block +174, z 1.8, +110 / +54 / +9, promising [0] (was +167, z 1.8, Jul–Nov +3). Live: would block 14 (13 ended, win 46 %, −7.2, avg −0.56) vs rest 76 (67 ended, +13.1, avg +0.20) — agrees per trade but < 20 ended.
- **MES 2m:** **breakout window 1 bar robust [1]** +150, z 2.2, +75 / +28 / +47 (was +128, z 1.9 promising). **CHOP > 58 block robust [1]** +175, z 2.2, +22 / +3 / +149 (was +135, z 1.8). Promising [0]: breakout exception OFF +146, z 1.6, +90 / +28 / +28 (was +144); CHOP > 61.8 +80, z 1.6, +25 / +11 / +45 (was +68); 12-bar range < 3 ATR +183, z 1.8, +26 / +20 / +136 (was +154). Live: CHOP > 58 blocked 21 ended −16.2 (avg −0.77) vs rest 126 ended −87.5 (avg −0.69) — net negative but barely worse per trade than the rest; CHOP > 61.8 blocked 10 ended −10.5 (avg −1.05); range < 3 ATR blocked 41 ended **+16.1** (avg +0.39) vs rest −119.7 → live disagrees with the range block. All are 1 robust run at most → wait.
- **MGC 2m (new run 1, range gate ON):** no candidates. VWAP −3 / +2 block +59, z 0.9, +32 / +8 / +19 → noise (was +71 promising pre-gate); Max-SL-cap skip 1.5 +99, z 1.5, −4 / +35 / +69 → noise (was +110 promising). Live: VWAP −3/+2 blocked 28 ended **+9.3** vs rest −106.8; SL-cap skip blocked 11 ended −16.1. Range gate OFF −24 (−91 / +62 / +5) → gate confirmed.
- **MES 5m:** **ER threshold 0.18 robust [3]** +198, z 2.5, +37 / +51 / +110 (was +187, z 2.3, +99; run 1 +183, z 2.3, +94). **ER 0.20 robust [3]** +148, z 2.3, +29 / +50 / +69. **ER filter OFF robust [1]** +315, z 2.1, +146 / +70 / +99 (was promising). VWAP stretch 3 / 4 / 6 ATR +177 (z 1.6) / +128 (1.5) / +113 (1.9), promising [0]. Live stretch: 3 ATR blocked 10 ended **+7.8** vs rest −26.2; 4 / 6 ATR blocked 5 ended **+12.0** — live does not support a stretch block.
- **MGC 5m:** all promising [0]: ER 0.18 +126, z 1.4, +33 / +64 / +29 (was +120); CHOP > 58 +168, z 1.7, +51 / +51 / +66 (same); VWAP stretch 3 +175, z 1.3, +54 / +66 / +54 (was +184); stretch 6 +105, z 1.5, +11 / +61 / +33 (was +107); ATR > 1.8 × ATR(100) skip +53, z 1.4, +12 / +25 / +16 (was +46); ATR > 1.5 × dropped to noise (+60, z 0.99). Live: CHOP > 58 blocked 14 ended, win 14 %, **−40.4** (avg −2.89) vs rest 55 ended +3.2; stretch 3 blocked 23 ended −26.0 (avg −1.13) vs rest −11.2; stretch 6 blocked 10 ended −10.6. Live agrees strongly, but none is robust in the replay yet. ATR(100) skips can't be checked live.
- **Confirmed current (still worse when removed):** MGC 3m VWAP stretch OFF −77, MGC 3m ER OFF −98, MGC 2m ER OFF −58, MGC 2m range gate OFF −24, MES 2m HTF flip block OFF −13.

**Live split** (alerts 10/19 -> 11/13, near-copies de-duplicated per DATA_NOTES; Trade Setup "Filters:" line matched to the first "Setup Ended:" with same symbol, chart TF, direction and entry; where two ends arrived for one MGC 3m setup the "0.5×" one is used — MGC 3m results 11/09-11/12 are partly on old exits):

| Chart | Live setups w/ Filters line (first–last) | Candidate block | Would block | Rest |
|---|---|---|---|---|
| MES 3m | 121 (2026-10-19 – 2026-11-13) | X >= 6 (crosses block) | 1 setups, 1 ended, win 0%, net -5.0, avg -5.00 | 120 setups, 107 ended, win 47%, net -23.0, avg -0.21 |
| MES 3m | 121 (2026-10-19 – 2026-11-13) | X >= 4 (crosses block) | 17 setups, 15 ended, win 60%, net +62.9, avg +4.20 | 104 setups, 93 ended, win 44%, net -90.9, avg -0.98 |
| MGC 3m | 90 (2026-10-19 – 2026-11-13) | X >= 4 (crosses block) | 14 setups, 13 ended, win 46%, net -7.2, avg -0.56 | 76 setups, 67 ended, win 48%, net +13.1, avg +0.20 |
| MES 2m | 159 (2026-10-19 – 2026-11-13) | CHOP > 58 | 27 setups, 21 ended, win 48%, net -16.2, avg -0.77 | 132 setups, 126 ended, win 43%, net -87.5, avg -0.69 |
| MES 2m | 159 (2026-10-19 – 2026-11-13) | CHOP > 61.8 | 13 setups, 10 ended, win 50%, net -10.5, avg -1.05 | 146 setups, 137 ended, win 43%, net -93.2, avg -0.68 |
| MES 2m | 159 (2026-10-19 – 2026-11-13) | Range < 3 ATR | 49 setups, 41 ended, win 54%, net +16.1, avg +0.39 | 110 setups, 106 ended, win 40%, net -119.7, avg -1.13 |
| MGC 2m | 227 (2026-10-19 – 2026-11-13) | VWAP -3/+2 pts (no candle-beyond check) | 32 setups, 28 ended, win 54%, net +9.3, avg +0.33 | 195 setups, 180 ended, win 44%, net -106.8, avg -0.59 |
| MGC 2m | 227 (2026-10-19 – 2026-11-13) | Max SL cap < 1.5 x ATR | 12 setups, 11 ended, win 45%, net -16.1, avg -1.46 | 215 setups, 197 ended, win 46%, net -81.4, avg -0.41 |
| MES 5m | 81 (2026-10-20 – 2026-11-12) | VWAP stretch 3 ATR | 11 setups, 10 ended, win 60%, net +7.8, avg +0.78 | 70 setups, 61 ended, win 51%, net -26.2, avg -0.43 |
| MES 5m | 81 (2026-10-20 – 2026-11-12) | VWAP stretch 4 ATR | 6 setups, 5 ended, win 80%, net +12.0, avg +2.39 | 75 setups, 66 ended, win 50%, net -30.3, avg -0.46 |
| MES 5m | 81 (2026-10-20 – 2026-11-12) | VWAP stretch 6 ATR | 6 setups, 5 ended, win 80%, net +12.0, avg +2.39 | 75 setups, 66 ended, win 50%, net -30.3, avg -0.46 |
| MGC 5m | 75 (2026-10-21 – 2026-11-13) | CHOP > 58 | 15 setups, 14 ended, win 14%, net -40.4, avg -2.89 | 60 setups, 55 ended, win 53%, net +3.2, avg +0.06 |
| MGC 5m | 75 (2026-10-21 – 2026-11-13) | VWAP stretch 3 ATR | 24 setups, 23 ended, win 39%, net -26.0, avg -1.13 | 51 setups, 46 ended, win 48%, net -11.2, avg -0.24 |
| MGC 5m | 75 (2026-10-21 – 2026-11-13) | VWAP stretch 6 ATR | 11 setups, 10 ended, win 40%, net -10.6, avg -1.06 | 64 setups, 59 ended, win 46%, net -26.6, avg -0.45 |

**Verdict: UPDATE WARRANTED — MES 5m.** "ER threshold 0.18" is robust on 3 consecutive weekly runs (11/01 +183 z 2.3; 11/07 +187 z 2.3; 11/13 +198 z 2.5, better in every third each time), its neighbour 0.20 is also robust (+148, z 2.3), and since it loosens the filter the live check is replaced by the most recent third: +94 / +99 / +110 — positive on all 3 runs. Change: ③ Trade Setup Filters → **"Block in chop: Efficiency Ratio below" = 0.18 on the MES 5m chart only**. That input is one value for all charts, so set it on the MES 5m chart's CBC instance only (no CBC version needed; a per-symbol ER list would need a new CBC version if you want it on a shared layout). Then recreate the MES 5m TradingView alert. (ER filter OFF is now robust too, +315, but only for 1 run — keep watching; 0.18 is the qualified step.)
All other charts: **no change yet** — MES 2m breakout window 1 bar and CHOP > 58 are robust for the first time (1 of 3 runs; live CHOP > 58 only slightly negative); MGC 3m crosses ≥ 4 and all MGC 5m candidates still promising, not robust.

---

## MES 3m — current (ER 0.23 + breakout 3 bars, range gate 24 / 20 % / 5 ATR): 1756 setups, win 50%, net -3

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1874 | 49% | -147 | -144 | -1.8 | -87 / -46 / -12 | worse |
| ER threshold 0.20 | 1833 | 50% | -74 | -71 | -1.1 | -63 / -1 / -7 | worse |
| ER threshold 0.26 | 1690 | 50% | -23 | -20 | -0.3 | -0 / -19 / -1 | worse |
| ER threshold 0.30 | 1620 | 50% | +14 | +17 | +0.2 | +40 / -6 / -17 | noise |
| ER filter OFF | 2168 | 50% | -25 | -22 | -0.1 | -95 / +21 / +52 | worse |
| ER breakout exception OFF | 1255 | 50% | -102 | -99 | -0.7 | -90 / +12 / -21 | worse |
| ER breakout window 1 bar | 1498 | 50% | -22 | -19 | -0.2 | -21 / +6 / -4 | worse |
| Choppiness Index > 61.8 block | 1637 | 50% | +71 | +73 | +1.1 | -24 / +34 / +63 | noise |
| Choppiness Index > 58 block | 1490 | 49% | -77 | -75 | -0.8 | -47 / -13 / -14 | worse |
| ADX < 20 block | 1199 | 48% | -173 | -170 | -1.3 | -70 / -64 / -37 | worse |
| ADX < 15 block | 1603 | 49% | -122 | -119 | -1.6 | -37 / -44 / -38 | worse |
| EMA20 / VWAP crosses >= 4 block | 1509 | 51% | +139 | +142 | +1.5 | -5 / +162 / -14 | noise |
| EMA20 / VWAP crosses >= 6 block | 1725 | 50% | +61 | +64 | +1.5 | +18 / +33 / +13 | promising |
| HTF EMA20 slope < 0.3 ATR block | 1254 | 49% | -59 | -56 | -0.4 | -19 / -18 / -19 | worse |
| HTF EMA20 slope < 0.2 ATR block | 1444 | 49% | -4 | -1 | -0.0 | +16 / -0 / -17 | worse |
| 12-bar range < 2 ATR block | 1732 | 50% | -48 | -45 | -1.6 | -40 / -15 / +10 | worse |
| 12-bar range < 3 ATR block | 1282 | 48% | -306 | -303 | -2.4 | -84 / -71 / -148 | worse |
| VWAP stretch 3 ATR | 1090 | 50% | +37 | +40 | +0.3 | -59 / +95 / +5 | noise |
| VWAP stretch 4 ATR | 1305 | 49% | -54 | -51 | -0.4 | -81 / +9 / +21 | worse |
| VWAP stretch 6 ATR | 1536 | 50% | -34 | -31 | -0.4 | -42 / -21 / +33 | worse |
| Range gate OFF | 2046 | 52% | +136 | +139 | +1.1 | +130 / +71 / -63 | noise |
| Range gate 24 / 20 % / 4 ATR | 1909 | 51% | +65 | +68 | +0.7 | +62 / +43 / -36 | noise |
| Range gate 24 / 20 % / 6 ATR | 1686 | 49% | -45 | -42 | -0.7 | +17 / -27 / -32 | worse |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1528 | 50% | -38 | -35 | -0.4 | -94 / +19 / +40 | worse |
| Block if EMA200 -3 / +2 pts | 1545 | 50% | +34 | +37 | +0.4 | -12 / +2 / +47 | noise |
| HTF flips >= 2 in 8 block | 691 | 48% | -57 | -54 | -0.3 | -51 / +174 / -177 | worse |
| HTF flips >= 3 in 8 block | 1446 | 50% | +61 | +64 | +0.6 | -16 / +93 / -14 | noise |
| HTF flips >= 4 in 8 block | 1697 | 50% | -22 | -19 | -0.4 | -9 / +13 / -22 | worse |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 1441 | 49% | +65 | +68 | +0.7 | -18 / +101 / -15 | noise |
| Skip while ATR > 1.8 x ATR(100) | 1690 | 50% | +5 | +8 | +0.2 | -33 / +57 / -16 | noise |
| Skip while ATR > 1.5 x ATR(100) | 1588 | 50% | +24 | +27 | +0.4 | +26 / +59 / -58 | noise |

Candidates: EMA20 / VWAP crosses >= 6 block → +64, z +1.5, +18 / +33 / +13 (promising)

## MGC 3m — current (ER 0.23 + breakout 3 bars, range gate 24 / 20 % / 5 ATR, VWAP stretch 4.0 ATR): 1199 setups, win 51%, net +320

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1289 | 51% | +279 | -42 | -0.5 | +6 / -6 / -42 | worse |
| ER threshold 0.20 | 1258 | 51% | +300 | -21 | -0.3 | +18 / -11 / -27 | worse |
| ER threshold 0.26 | 1165 | 51% | +339 | +19 | +0.4 | +33 / +18 / -31 | noise |
| ER threshold 0.30 | 1119 | 51% | +317 | -4 | -0.1 | +31 / +11 / -46 | worse |
| ER filter OFF | 1476 | 50% | +222 | -98 | -0.7 | -103 / +56 / -51 | worse |
| ER breakout exception OFF | 854 | 50% | +78 | -242 | -1.9 | -144 / -47 / -51 | worse |
| ER breakout window 1 bar | 1031 | 50% | +158 | -163 | -1.8 | -103 / +8 / -68 | worse |
| Choppiness Index > 61.8 block | 1137 | 51% | +347 | +26 | +0.4 | +3 / +45 / -22 | noise |
| Choppiness Index > 58 block | 1053 | 52% | +303 | -17 | -0.2 | -22 / +78 / -72 | worse |
| ADX < 20 block | 812 | 49% | +45 | -276 | -2.3 | -142 / -18 / -116 | worse |
| ADX < 15 block | 1123 | 51% | +307 | -13 | -0.2 | -84 / +3 / +67 | worse |
| EMA20 / VWAP crosses >= 4 block | 1015 | 52% | +494 | +174 | +1.8 | +110 / +54 / +9 | promising |
| EMA20 / VWAP crosses >= 6 block | 1174 | 51% | +346 | +26 | +0.7 | +15 / -2 / +13 | noise |
| HTF EMA20 slope < 0.3 ATR block | 685 | 51% | +274 | -46 | -0.3 | -4 / +25 / -67 | worse |
| HTF EMA20 slope < 0.2 ATR block | 864 | 50% | +208 | -113 | -0.9 | -31 / -26 / -56 | worse |
| 12-bar range < 2 ATR block | 1190 | 51% | +283 | -37 | -1.8 | -23 / -10 / -4 | worse |
| 12-bar range < 3 ATR block | 908 | 51% | +196 | -124 | -1.1 | -125 / +33 / -32 | worse |
| VWAP stretch 3 ATR | 1004 | 51% | +237 | -83 | -0.9 | -39 / -53 / +8 | worse |
| VWAP stretch 6 ATR | 1483 | 50% | +206 | -115 | -1.1 | -103 / +54 / -65 | worse |
| VWAP stretch OFF | 1783 | 50% | +243 | -77 | -0.5 | -67 / +62 / -72 | worse |
| Range gate OFF | 1364 | 52% | +370 | +50 | +0.5 | +97 / -53 / +6 | noise |
| Range gate 24 / 20 % / 4 ATR | 1297 | 51% | +385 | +64 | +0.8 | +83 / -28 / +9 | noise |
| Range gate 24 / 20 % / 6 ATR | 1142 | 50% | +264 | -57 | -0.9 | -28 / -18 / -11 | worse |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1041 | 52% | +418 | +98 | +1.2 | +25 / +95 / -22 | noise |
| Block if EMA200 -3 / +2 pts | 1039 | 51% | +310 | -10 | -0.1 | -61 / +23 / +27 | worse |
| HTF flips >= 2 in 8 block | 400 | 50% | +127 | -193 | -1.1 | -73 / +73 / -193 | worse |
| HTF flips >= 3 in 8 block | 919 | 51% | +245 | -75 | -0.7 | -55 / +74 / -94 | worse |
| HTF flips >= 4 in 8 block | 1145 | 51% | +298 | -22 | -0.5 | +1 / +18 / -41 | worse |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 750 | 49% | +156 | -164 | -1.3 | -76 / -28 / -61 | worse |
| Skip while ATR > 1.8 x ATR(100) | 1163 | 51% | +277 | -43 | -1.1 | -19 / -23 / -1 | worse |
| Skip while ATR > 1.5 x ATR(100) | 1091 | 50% | +262 | -59 | -0.8 | -12 / -42 / -5 | worse |

Candidates: EMA20 / VWAP crosses >= 4 block → +174, z +1.8, +110 / +54 / +9 (promising)

## MES 2m — current (ER 0.23 + breakout 3 bars, 1H MTF gate, HTF flips >= 4 in 8): 1224 setups, win 49%, net -217

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1302 | 49% | -240 | -23 | -0.4 | -7 / -37 / +21 | worse |
| ER threshold 0.20 | 1271 | 48% | -258 | -41 | -0.8 | -42 / -25 / +26 | worse |
| ER threshold 0.26 | 1170 | 49% | -207 | +9 | +0.2 | -19 / -1 / +30 | noise |
| ER threshold 0.30 | 1115 | 49% | -180 | +37 | +0.5 | +0 / +1 / +36 | noise |
| ER filter OFF | 1482 | 51% | -66 | +151 | +1.2 | +100 / -6 / +56 | noise |
| ER breakout exception OFF | 952 | 50% | -70 | +146 | +1.6 | +90 / +28 / +28 | promising |
| ER breakout window 1 bar | 1101 | 50% | -67 | +150 | +2.2 | +75 / +28 / +47 | robust |
| Choppiness Index > 61.8 block | 1156 | 49% | -137 | +80 | +1.6 | +25 / +11 / +45 | promising |
| Choppiness Index > 58 block | 1039 | 50% | -42 | +175 | +2.2 | +22 / +3 / +149 | robust |
| ADX < 20 block | 828 | 48% | -236 | -19 | -0.2 | +18 / +2 / -39 | worse |
| ADX < 15 block | 1116 | 49% | -209 | +8 | +0.1 | -4 / +17 / -6 | noise |
| EMA20 / VWAP crosses >= 4 block | 1067 | 47% | -271 | -54 | -0.7 | -18 / -43 / +7 | worse |
| EMA20 / VWAP crosses >= 6 block | 1189 | 48% | -260 | -43 | -1.1 | -43 / -18 / +18 | worse |
| HTF EMA20 slope < 0.3 ATR block | 983 | 47% | -195 | +22 | +0.2 | +76 / -42 / -12 | noise |
| HTF EMA20 slope < 0.2 ATR block | 1098 | 48% | -227 | -10 | -0.1 | +58 / -29 / -39 | worse |
| 12-bar range < 2 ATR block | 1208 | 49% | -212 | +5 | +0.2 | +4 / -3 / +4 | noise |
| 12-bar range < 3 ATR block | 880 | 51% | -34 | +183 | +1.8 | +26 / +20 / +136 | promising |
| VWAP stretch 3 ATR | 554 | 49% | -112 | +104 | +0.8 | +50 / -53 / +108 | noise |
| VWAP stretch 4 ATR | 693 | 49% | -87 | +130 | +1.2 | +22 / -19 / +127 | noise |
| VWAP stretch 6 ATR | 907 | 49% | -131 | +86 | +1.0 | -3 / -27 / +116 | noise |
| Range gate 24 / 20 % / 4 ATR | 1147 | 49% | -175 | +42 | +0.7 | +62 / -14 / -6 | noise |
| Range gate 24 / 20 % / 5 ATR | 1073 | 48% | -194 | +23 | +0.3 | +9 / -10 / +24 | noise |
| Range gate 24 / 20 % / 6 ATR | 1021 | 47% | -224 | -7 | -0.1 | -34 / -23 / +50 | worse |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1110 | 49% | -170 | +47 | +0.9 | +55 / -14 / +6 | noise |
| Block if EMA200 -3 / +2 pts | 1116 | 49% | -208 | +9 | +0.2 | +2 / -11 / +18 | noise |
| HTF flips >= 2 in 8 block | 477 | 47% | -187 | +30 | +0.2 | +28 / -55 / +56 | noise |
| HTF flips >= 3 in 8 block | 1048 | 49% | -184 | +33 | +0.4 | +1 / +1 / +31 | noise |
| HTF flips block OFF | 1280 | 49% | -230 | -13 | -0.3 | -16 / +2 / +1 | worse |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 1118 | 48% | -202 | +15 | +0.3 | +96 / -51 / -30 | noise |
| Skip while ATR > 1.8 x ATR(100) | 1197 | 48% | -221 | -5 | -0.2 | +52 / -36 / -21 | worse |
| Skip while ATR > 1.5 x ATR(100) | 1162 | 48% | -225 | -8 | -0.2 | +76 / -78 / -6 | worse |

Candidates: ER breakout exception OFF → +146, z +1.6, +90 / +28 / +28 (promising); ER breakout window 1 bar → +150, z +2.2, +75 / +28 / +47 (robust); Choppiness Index > 61.8 block → +80, z +1.6, +25 / +11 / +45 (promising); Choppiness Index > 58 block → +175, z +2.2, +22 / +3 / +149 (robust); 12-bar range < 3 ATR block → +183, z +1.8, +26 / +20 / +136 (promising)

## MGC 2m — current (ER 0.23 + breakout 3 bars, range gate 24 / 20 % / 5 ATR): 1353 setups, win 52%, net +384

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1470 | 52% | +409 | +25 | +0.3 | +60 / -4 / -30 | noise |
| ER threshold 0.20 | 1420 | 52% | +392 | +7 | +0.1 | +27 / +8 / -28 | noise |
| ER threshold 0.26 | 1291 | 52% | +429 | +45 | +0.9 | +23 / +7 / +15 | noise |
| ER threshold 0.30 | 1223 | 52% | +429 | +44 | +0.6 | -22 / +36 / +30 | noise |
| ER filter OFF | 1725 | 51% | +326 | -58 | -0.4 | +27 / +24 / -109 | worse |
| ER breakout exception OFF | 967 | 52% | +188 | -196 | -1.8 | -136 / -39 / -21 | worse |
| ER breakout window 1 bar | 1177 | 51% | +207 | -177 | -2.2 | -106 / -37 / -34 | worse |
| Choppiness Index > 61.8 block | 1281 | 52% | +392 | +8 | +0.2 | -83 / +58 / +33 | noise |
| Choppiness Index > 58 block | 1184 | 52% | +426 | +41 | +0.5 | -81 / +43 / +79 | noise |
| ADX < 20 block | 955 | 52% | +338 | -47 | -0.4 | -40 / -42 / +36 | worse |
| ADX < 15 block | 1240 | 52% | +371 | -14 | -0.2 | -65 / +4 / +47 | worse |
| EMA20 / VWAP crosses >= 4 block | 1198 | 51% | +324 | -60 | -0.8 | -23 / -32 / -5 | worse |
| EMA20 / VWAP crosses >= 6 block | 1334 | 51% | +354 | -30 | -1.1 | -23 / -5 / -2 | worse |
| HTF EMA20 slope < 0.3 ATR block | 932 | 50% | +258 | -127 | -1.1 | +36 / -38 / -124 | worse |
| HTF EMA20 slope < 0.2 ATR block | 1077 | 51% | +391 | +7 | +0.1 | +63 / +22 / -78 | noise |
| 12-bar range < 2 ATR block | 1342 | 52% | +389 | +5 | +0.2 | -11 / +10 / +6 | noise |
| 12-bar range < 3 ATR block | 1026 | 53% | +456 | +72 | +0.7 | -99 / +62 / +109 | noise |
| VWAP stretch 3 ATR | 675 | 52% | +281 | -103 | -0.8 | +18 / -79 / -42 | worse |
| VWAP stretch 4 ATR | 780 | 52% | +274 | -110 | -0.9 | -14 / -74 / -22 | worse |
| VWAP stretch 6 ATR | 961 | 52% | +335 | -49 | -0.5 | -25 / -44 / +20 | worse |
| Range gate OFF | 1572 | 52% | +360 | -24 | -0.2 | -91 / +62 / +5 | worse |
| Range gate 24 / 20 % / 4 ATR | 1477 | 52% | +373 | -11 | -0.1 | -41 / +13 / +16 | worse |
| Range gate 24 / 20 % / 6 ATR | 1289 | 51% | +340 | -44 | -0.8 | -38 / +22 / -29 | worse |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1222 | 52% | +443 | +59 | +0.9 | +32 / +8 / +19 | noise |
| Block if EMA200 -3 / +2 pts | 1159 | 51% | +262 | -122 | -1.6 | -44 / +4 / -82 | worse |
| HTF flips >= 2 in 8 block | 496 | 51% | +148 | -237 | -1.6 | -110 / -66 / -60 | worse |
| HTF flips >= 3 in 8 block | 1082 | 52% | +386 | +2 | +0.0 | +60 / -35 / -23 | noise |
| HTF flips >= 4 in 8 block | 1302 | 52% | +392 | +8 | +0.2 | +13 / -5 / +0 | noise |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 1194 | 53% | +483 | +99 | +1.5 | -4 / +35 / +69 | noise |
| Skip while ATR > 1.8 x ATR(100) | 1321 | 52% | +402 | +17 | +0.6 | -21 / -7 / +45 | noise |
| Skip while ATR > 1.5 x ATR(100) | 1252 | 52% | +382 | -2 | -0.0 | -33 / -14 / +44 | worse |

Candidates: none

## MES 5m — current (ER 0.23 + breakout 3 bars): 1208 setups, win 51%, net +18

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1281 | 53% | +217 | +198 | +2.5 | +37 / +51 / +110 | robust |
| ER threshold 0.20 | 1253 | 52% | +166 | +148 | +2.3 | +29 / +50 / +69 | robust |
| ER threshold 0.26 | 1163 | 51% | -31 | -49 | -0.8 | +23 / -71 / -1 | worse |
| ER threshold 0.30 | 1110 | 50% | -44 | -62 | -0.7 | +46 / -103 / -5 | worse |
| ER filter OFF | 1466 | 54% | +334 | +315 | +2.1 | +146 / +70 / +99 | robust |
| ER breakout exception OFF | 893 | 51% | -95 | -114 | -0.9 | +39 / -78 / -75 | worse |
| ER breakout window 1 bar | 1063 | 51% | -94 | -113 | -1.3 | +5 / -93 / -25 | worse |
| Choppiness Index > 61.8 block | 1125 | 52% | +110 | +92 | +1.4 | +33 / -9 / +67 | noise |
| Choppiness Index > 58 block | 1027 | 52% | +65 | +47 | +0.5 | -42 / +29 / +60 | noise |
| ADX < 20 block | 804 | 52% | +63 | +45 | +0.3 | +20 / +61 / -36 | noise |
| ADX < 15 block | 1090 | 52% | +62 | +44 | +0.6 | +32 / -31 / +43 | noise |
| EMA20 / VWAP crosses >= 4 block | 988 | 51% | -74 | -93 | -0.8 | -0 / -129 / +36 | worse |
| EMA20 / VWAP crosses >= 6 block | 1171 | 51% | -43 | -62 | -1.2 | -49 / -41 / +29 | worse |
| HTF EMA20 slope < 0.3 ATR block | 868 | 50% | -102 | -120 | -0.9 | +16 / -82 / -55 | worse |
| HTF EMA20 slope < 0.2 ATR block | 984 | 50% | -104 | -123 | -1.1 | +39 / -117 / -45 | worse |
| 12-bar range < 2 ATR block | 1193 | 52% | +47 | +28 | +1.1 | +20 / -1 / +9 | noise |
| 12-bar range < 3 ATR block | 886 | 52% | +14 | -5 | -0.0 | -34 / -2 / +31 | worse |
| VWAP stretch 3 ATR | 910 | 53% | +196 | +177 | +1.6 | +97 / +7 / +73 | promising |
| VWAP stretch 4 ATR | 1025 | 53% | +147 | +128 | +1.5 | +97 / +13 / +18 | promising |
| VWAP stretch 6 ATR | 1130 | 52% | +131 | +113 | +1.9 | +32 / +55 / +25 | promising |
| Range gate 24 / 20 % / 4 ATR | 1123 | 51% | -20 | -39 | -0.5 | +30 / -37 / -32 | worse |
| Range gate 24 / 20 % / 5 ATR | 1022 | 50% | +28 | +10 | +0.1 | +56 / -38 / -8 | noise |
| Range gate 24 / 20 % / 6 ATR | 989 | 51% | +81 | +62 | +0.5 | +69 / +8 / -15 | noise |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1054 | 51% | -69 | -88 | -1.0 | -31 / +69 / -126 | worse |
| Block if EMA200 -3 / +2 pts | 1114 | 52% | +77 | +58 | +0.9 | +42 / +12 / +4 | noise |
| HTF flips >= 2 in 8 block | 453 | 49% | -129 | -147 | -0.9 | +3 / -83 / -67 | worse |
| HTF flips >= 3 in 8 block | 988 | 50% | -132 | -150 | -1.5 | -19 / -29 / -102 | worse |
| HTF flips >= 4 in 8 block | 1161 | 51% | +18 | -0 | -0.0 | -16 / +23 / -7 | worse |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 802 | 49% | -17 | -36 | -0.3 | +89 / -152 / +27 | worse |
| Skip while ATR > 1.8 x ATR(100) | 1135 | 50% | -62 | -81 | -1.4 | +12 / -26 / -67 | worse |
| Skip while ATR > 1.5 x ATR(100) | 1029 | 50% | -21 | -40 | -0.5 | +23 / -92 / +29 | worse |

Candidates: ER threshold 0.18 → +198, z +2.5, +37 / +51 / +110 (robust); ER threshold 0.20 → +148, z +2.3, +29 / +50 / +69 (robust); ER filter OFF → +315, z +2.1, +146 / +70 / +99 (robust); VWAP stretch 3 ATR → +177, z +1.6, +97 / +7 / +73 (promising); VWAP stretch 4 ATR → +128, z +1.5, +97 / +13 / +18 (promising); VWAP stretch 6 ATR → +113, z +1.9, +32 / +55 / +25 (promising)

## MGC 5m — current (ER 0.23 + breakout 3 bars): 1194 setups, win 51%, net -107

| Change (one at a time) | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| ER threshold 0.18 | 1271 | 52% | +19 | +126 | +1.4 | +33 / +64 / +29 | promising |
| ER threshold 0.20 | 1237 | 52% | -64 | +43 | +0.6 | +15 / +22 / +6 | noise |
| ER threshold 0.26 | 1137 | 51% | -21 | +86 | +1.4 | -13 / +84 / +15 | noise |
| ER threshold 0.30 | 1079 | 51% | -84 | +23 | +0.3 | -16 / +35 / +4 | noise |
| ER filter OFF | 1502 | 52% | -34 | +73 | +0.4 | -29 / +47 / +55 | noise |
| ER breakout exception OFF | 883 | 51% | -85 | +22 | +0.2 | +69 / -51 / +4 | noise |
| ER breakout window 1 bar | 1038 | 51% | -191 | -84 | -0.9 | -6 / -40 / -38 | worse |
| Choppiness Index > 61.8 block | 1105 | 51% | -41 | +67 | +0.9 | +21 / +30 / +15 | noise |
| Choppiness Index > 58 block | 1012 | 52% | +61 | +168 | +1.7 | +51 / +51 / +66 | promising |
| ADX < 20 block | 781 | 52% | +71 | +178 | +1.3 | +114 / -47 / +111 | noise |
| ADX < 15 block | 1082 | 51% | -94 | +13 | +0.2 | -4 / +15 / +2 | noise |
| EMA20 / VWAP crosses >= 4 block | 990 | 51% | -22 | +85 | +0.8 | -27 / +7 / +105 | noise |
| EMA20 / VWAP crosses >= 6 block | 1156 | 51% | -133 | -26 | -0.5 | -2 / -49 / +25 | worse |
| HTF EMA20 slope < 0.3 ATR block | 839 | 51% | -0 | +107 | +0.8 | +22 / -85 / +170 | noise |
| HTF EMA20 slope < 0.2 ATR block | 983 | 50% | -89 | +18 | +0.2 | -1 / -88 / +107 | noise |
| 12-bar range < 2 ATR block | 1178 | 51% | -115 | -8 | -0.2 | -12 / -3 / +7 | worse |
| 12-bar range < 3 ATR block | 841 | 51% | -16 | +91 | +0.7 | +49 / +40 / +2 | noise |
| VWAP stretch 3 ATR | 796 | 53% | +67 | +175 | +1.3 | +54 / +66 / +54 | promising |
| VWAP stretch 4 ATR | 945 | 51% | -64 | +43 | +0.4 | +15 / -4 / +33 | noise |
| VWAP stretch 6 ATR | 1087 | 52% | -2 | +105 | +1.5 | +11 / +61 / +33 | promising |
| Range gate 24 / 20 % / 4 ATR | 1124 | 51% | -68 | +39 | +0.5 | -47 / +23 / +63 | noise |
| Range gate 24 / 20 % / 5 ATR | 1034 | 51% | -46 | +61 | +0.5 | -89 / +43 / +106 | noise |
| Range gate 24 / 20 % / 6 ATR | 992 | 51% | -47 | +60 | +0.5 | -80 / -9 / +149 | noise |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1102 | 51% | -61 | +46 | +0.6 | +34 / +52 / -40 | noise |
| Block if EMA200 -3 / +2 pts | 1128 | 51% | -126 | -19 | -0.3 | +25 / -32 / -12 | worse |
| HTF flips >= 2 in 8 block | 414 | 48% | -138 | -31 | -0.2 | +75 / -99 / -7 | worse |
| HTF flips >= 3 in 8 block | 953 | 49% | -295 | -188 | -1.7 | -96 / -23 / -69 | worse |
| HTF flips >= 4 in 8 block | 1138 | 50% | -179 | -72 | -1.3 | -14 / -22 / -35 | worse |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 468 | 49% | +2 | +109 | +0.6 | +109 / -92 / +92 | noise |
| Skip while ATR > 1.8 x ATR(100) | 1168 | 51% | -54 | +53 | +1.4 | +12 / +25 / +16 | promising |
| Skip while ATR > 1.5 x ATR(100) | 1123 | 51% | -47 | +60 | +1.0 | +27 / +22 / +10 | noise |

Candidates: ER threshold 0.18 → +126, z +1.4, +33 / +64 / +29 (promising); Choppiness Index > 58 block → +168, z +1.7, +51 / +51 / +66 (promising); VWAP stretch 3 ATR → +175, z +1.3, +54 / +66 / +54 (promising); VWAP stretch 6 ATR → +105, z +1.5, +11 / +61 / +33 (promising); Skip while ATR > 1.8 x ATR(100) → +53, z +1.4, +12 / +25 / +16 (promising)

