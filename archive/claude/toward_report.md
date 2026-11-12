# Toward-flip study (all symbols, 2m/3m/5m) — 11/03/2026


Question: CBC skips setups after a TOWARD HTF CBC flip ("Include 'toward' HTF flips" OFF, the default) and, with "toward flip:
allow setups once a candle closes on the away side by (pts)" ON (1 pt), lets them in from the first candle that closes 1 pt beyond
the HTF EMA20 on the away side (that candle also fires the HTF CBC Flip trigger). Toward flip = long flip closing BELOW the HTF
EMA20 (short: above). Should toward flips be allowed, and is the late-away rule worth keeping?
Modes: LIVE = toward off + late-away 1 pt (current defaults) · STRICT = toward off, no late-away · LATE0 = late-away 0 pts ·
ON = toward flips allowed (every trigger, flip trigger on every flip).
Engine: chop_sim (triggers HTF CBC Flip with the live flip gates -- VWAP+EMA200 side 1 pt, VWAP slope, distance 2 ATR / pts floor --
LTF EMA20 Pierce, HTF EMA9 / EMA20 Pierce, 1-bar late; ER 0.23 chop rule with breakout exception; VWAP bounce block; cooldown 10;
opening-range windows; live per-chart gates: range gate MES/MGC 3m, VWAP stretch 4 ATR MGC 3m, 1H MTF gate MES 2m).
Exits: live per symbol -- base SL1 1.7 ATR (cap / minimum per symbol), TP1 1.7 ATR (cap per symbol), 80 % at TP1, BE, trail 1.7;
MES 3m: SL1 3.0 ATR (min 5, no cap), TP1 1.75 ATR (no cap), 100 % at TP1.
Data: server archive (Databento rebuild + BarFeed): 3m / 5m from 01/05, 2m from 06/01; MCL / BTC only since late Oct.
~50 % exact match with live setups: compare modes, not totals. z = change / (SD x sqrt(setups changed)); robust = z >= 2 and
better in all three equal-time thirds; promising = z >= 1 and all three better.
Usage: python3 toward_study.py SYM TF  (needs chop_sim.py next to it)

## MES 2m — 06/01 to 11/03, 76527 candles; HTF flips 2832, toward 1198 (42%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1333 | 49% | -190.5 | -0.14 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 426 / -58.6 (late 19) |
| STRICT: toward off, no late-away | 1187 | 49% | -186.4 | -0.16 | +4.0 | +0.1 | -12.5 / +25.7 / -9.2 | noise | 407 / -71.8 (late 0) |
| Late-away 0 pts | 1337 | 49% | -212.1 | -0.16 | -21.7 | -0.8 | -1.1 / +14.6 / -35.2 | worse | 421 / -76.8 (late 14) |
| ON: toward flips allowed | 1369 | 49% | -199.1 | -0.15 | -8.6 | -0.2 | -22.8 / +30.6 / -16.4 | worse | 413 / -43.4 (late 0) |

ON vs LIVE: 71 setups only with toward ON, net +9.6, win 49% (flip trigger 6 / +28.4); 35 live setups displaced, net +18.2.
Late-away flip setups in LIVE: 19, net +13.2, win 58%.
SUMMARY: none

## MES 3m — 01/05 to 11/03, 98932 candles; HTF flips 3616, toward 1523 (42%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 2222 | 48% | -308.0 | -0.14 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 339 / -329.5 (late 29) |
| STRICT: toward off, no late-away | 1737 | 49% | -45.7 | -0.03 | +262.3 | +1.7 | +71.4 / +56.0 / +134.9 | promising | 310 / -245.7 (late 0) |
| Late-away 0 pts | 2294 | 48% | -397.7 | -0.17 | -89.7 | -1.2 | -28.2 / -41.2 / -20.3 | worse | 336 / -304.4 (late 26) |
| ON: toward flips allowed | 2713 | 49% | -140.7 | -0.05 | +167.3 | +1.0 | -67.5 / +188.8 / +46.0 | noise | 318 / -209.1 (late 0) |

ON vs LIVE: 549 setups only with toward ON, net +83.5, win 49% (flip trigger 8 / +36.6); 58 live setups displaced, net -83.8.
Late-away flip setups in LIVE: 29, net -83.8, win 48%.
SUMMARY: MES 3m: STRICT: toward off, no late-away → +262.3, z +1.7, thirds +71.4 / +56.0 / +134.9 (promising)

## MES 5m — 01/05 to 11/03, 59353 candles; HTF flips 2177, toward 928 (43%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1503 | 50% | -90.7 | -0.06 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 338 / -24.8 (late 27) |
| STRICT: toward off, no late-away | 1174 | 51% | +14.5 | +0.01 | +105.3 | +1.0 | +40.0 / +57.1 / +8.1 | noise | 311 / -31.1 (late 0) |
| Late-away 0 pts | 1531 | 50% | -69.0 | -0.05 | +21.7 | +0.4 | -16.6 / +19.0 / +19.3 | noise | 333 / -3.3 (late 22) |
| ON: toward flips allowed | 1807 | 51% | +23.9 | +0.01 | +114.6 | +0.9 | +122.8 / -10.0 / +1.7 | noise | 317 / -23.7 (late 0) |

ON vs LIVE: 396 setups only with toward ON, net +109.8, win 54% (flip trigger 6 / +7.4); 92 live setups displaced, net -4.8.
Late-away flip setups in LIVE: 27, net +6.3, win 56%.
SUMMARY: none

## MGC 2m — 06/01 to 11/03, 76584 candles; HTF flips 2814, toward 1214 (43%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1961 | 51% | +398.2 | +0.20 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 552 / +62.4 (late 75) |
| STRICT: toward off, no late-away | 1459 | 52% | +352.5 | +0.24 | -45.7 | -0.4 | +17.8 / -113.9 / +50.4 | worse | 477 / +11.1 (late 0) |
| Late-away 0 pts | 2022 | 51% | +440.0 | +0.22 | +41.8 | +0.6 | +49.5 / -14.9 / +7.2 | noise | 540 / +52.8 (late 63) |
| ON: toward flips allowed | 2402 | 51% | +490.8 | +0.20 | +92.6 | +0.7 | +75.3 / -58.2 / +75.5 | noise | 498 / +13.0 (late 0) |

ON vs LIVE: 607 setups only with toward ON, net +141.9, win 52% (flip trigger 21 / +1.9); 166 live setups displaced, net +49.3.
Late-away flip setups in LIVE: 75, net +51.3, win 60%.
SUMMARY: none

## MGC 3m — 01/05 to 11/03, 98712 candles; HTF flips 3662, toward 1519 (41%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1677 | 50% | +144.4 | +0.09 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 235 / +142.4 (late 28) |
| STRICT: toward off, no late-away | 1157 | 51% | +240.6 | +0.21 | +96.3 | +0.7 | +71.9 / +8.0 / +16.4 | noise | 207 / +142.6 (late 0) |
| Late-away 0 pts | 1724 | 50% | +147.9 | +0.09 | +3.5 | +0.1 | +14.3 / +8.3 / -19.1 | noise | 234 / +195.6 (late 27) |
| ON: toward flips allowed | 2163 | 50% | +241.1 | +0.11 | +96.7 | +0.7 | +141.6 / +20.9 / -65.7 | noise | 218 / +156.1 (late 0) |

ON vs LIVE: 586 setups only with toward ON, net +77.3, win 51% (flip trigger 11 / +13.5); 100 live setups displaced, net -19.4.
Late-away flip setups in LIVE: 28, net -0.2, win 50%.
SUMMARY: none

## MGC 5m — 01/05 to 11/03, 59229 candles; HTF flips 2221, toward 967 (44%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1546 | 52% | +95.0 | +0.06 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 353 / +78.0 (late 37) |
| STRICT: toward off, no late-away | 1155 | 51% | -81.1 | -0.07 | -176.0 | -1.4 | -80.8 / +59.1 / -154.4 | worse | 316 / +80.1 (late 0) |
| Late-away 0 pts | 1580 | 52% | +92.1 | +0.06 | -2.9 | -0.0 | +34.7 / -5.3 / -32.2 | worse | 348 / +78.8 (late 32) |
| ON: toward flips allowed | 1928 | 52% | +18.4 | +0.01 | -76.6 | -0.5 | -57.1 / -3.4 / -16.2 | worse | 324 / +62.9 (late 0) |

ON vs LIVE: 484 setups only with toward ON, net -81.6, win 50% (flip trigger 8 / -17.2); 102 live setups displaced, net -5.0.
Late-away flip setups in LIVE: 37, net -2.1, win 51%.
SUMMARY: none

## MNQ 2m — 06/01 to 10/30, 75134 candles; HTF flips 2820, toward 1230 (44%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1995 | 46% | -595.3 | -0.30 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 558 / +395.6 (late 72) |
| STRICT: toward off, no late-away | 1448 | 46% | -2.4 | -0.00 | +592.9 | +1.0 | +120.0 / +163.0 / +309.9 | noise | 486 / +684.4 (late 0) |
| Late-away 0 pts | 2009 | 46% | -601.2 | -0.30 | -5.9 | -0.0 | +12.9 / +28.3 / -47.2 | worse | 559 / +371.3 (late 73) |
| ON: toward flips allowed | 2373 | 45% | -1021.2 | -0.43 | -425.9 | -0.6 | +253.3 / -235.9 / -443.3 | worse | 500 / +865.1 (late 0) |

ON vs LIVE: 531 setups only with toward ON, net -574.2, win 44% (flip trigger 14 / +180.7); 153 live setups displaced, net -148.3.
Late-away flip setups in LIVE: 72, net -288.8, win 43%.
SUMMARY: none

## MNQ 3m — 01/05 to 11/03, 98919 candles; HTF flips 3748, toward 1655 (44%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 2594 | 45% | -1366.0 | -0.53 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 725 / +587.2 (late 72) |
| STRICT: toward off, no late-away | 1943 | 46% | +152.2 | +0.08 | +1518.2 | +2.1 | +442.8 / +377.3 / +698.1 | robust | 653 / +534.2 (late 0) |
| Late-away 0 pts | 2603 | 45% | -1374.4 | -0.53 | -8.4 | -0.1 | +67.4 / -22.7 / -53.2 | worse | 722 / +548.1 (late 69) |
| ON: toward flips allowed | 3138 | 45% | -1829.0 | -0.58 | -463.0 | -0.5 | +428.6 / -0.3 / -891.3 | worse | 670 / +649.3 (late 0) |

ON vs LIVE: 729 setups only with toward ON, net -820.9, win 44% (flip trigger 17 / +115.1); 185 live setups displaced, net -357.9.
Late-away flip setups in LIVE: 72, net +53.0, win 47%.
SUMMARY: MNQ 3m: STRICT: toward off, no late-away → +1518.2, z +2.1, thirds +442.8 / +377.3 / +698.1 (robust)

## MNQ 5m — 01/05 to 11/03, 59360 candles; HTF flips 2191, toward 964 (44%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1503 | 47% | +2735.9 | +1.82 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 320 / +638.6 (late 30) |
| STRICT: toward off, no late-away | 1123 | 47% | +2078.1 | +1.85 | -657.8 | -1.1 | -167.8 / +39.4 / -529.4 | worse | 290 / +380.6 (late 0) |
| Late-away 0 pts | 1510 | 47% | +2768.3 | +1.83 | +32.4 | +0.2 | -28.3 / -10.6 / +71.2 | noise | 320 / +692.3 (late 30) |
| ON: toward flips allowed | 1823 | 47% | +3059.5 | +1.68 | +323.6 | +0.5 | +289.6 / +175.1 / -141.1 | noise | 295 / +292.6 (late 0) |

ON vs LIVE: 405 setups only with toward ON, net +917.2, win 49% (flip trigger 5 / -88.0); 85 live setups displaced, net +593.6.
Late-away flip setups in LIVE: 30, net +258.0, win 57%.
SUMMARY: none

## M2K 2m — 06/01 to 11/03, 76236 candles; HTF flips 2925, toward 1266 (43%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1660 | 52% | -32.7 | -0.02 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 352 / -50.4 (late 30) |
| STRICT: toward off, no late-away | 1341 | 51% | -59.8 | -0.04 | -27.1 | -0.6 | -0.3 / -23.4 / -3.4 | worse | 322 / -43.3 (late 0) |
| Late-away 0 pts | 1831 | 52% | -71.8 | -0.04 | -39.0 | -1.0 | -6.2 / -17.9 / -14.9 | worse | 346 / -58.0 (late 24) |
| ON: toward flips allowed | 2202 | 52% | -65.1 | -0.03 | -32.4 | -0.5 | +8.1 / -0.9 / -39.6 | worse | 326 / -50.9 (late 0) |

ON vs LIVE: 623 setups only with toward ON, net -16.2, win 54% (flip trigger 4 / -7.6); 81 live setups displaced, net +16.3.
Late-away flip setups in LIVE: 30, net -7.1, win 53%.
SUMMARY: none

## M2K 3m — 01/05 to 11/03, 97644 candles; HTF flips 3803, toward 1608 (42%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 2229 | 54% | +83.1 | +0.04 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 548 / +45.7 (late 40) |
| STRICT: toward off, no late-away | 1795 | 54% | +73.2 | +0.04 | -9.8 | -0.2 | +25.4 / -5.5 / -29.8 | worse | 508 / +26.2 (late 0) |
| Late-away 0 pts | 2375 | 53% | +49.2 | +0.02 | -33.9 | -0.7 | +10.3 / +0.1 / -44.2 | worse | 541 / +40.8 (late 33) |
| ON: toward flips allowed | 2897 | 53% | +25.1 | +0.01 | -58.0 | -0.7 | -7.8 / +4.8 / -54.9 | worse | 515 / +22.4 (late 0) |

ON vs LIVE: 786 setups only with toward ON, net -39.0, win 52% (flip trigger 7 / -3.8); 118 live setups displaced, net +19.0.
Late-away flip setups in LIVE: 40, net +19.5, win 68%.
SUMMARY: none

## M2K 5m — 01/05 to 11/03, 59359 candles; HTF flips 2208, toward 951 (43%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1417 | 55% | +46.7 | +0.03 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 246 / +77.3 (late 14) |
| STRICT: toward off, no late-away | 1099 | 55% | +75.5 | +0.07 | +28.8 | +0.5 | +2.4 / +16.5 / +9.9 | noise | 232 / +103.3 (late 0) |
| Late-away 0 pts | 1483 | 54% | +54.3 | +0.04 | +7.6 | +0.2 | -2.0 / -33.2 / +42.7 | noise | 242 / +87.9 (late 10) |
| ON: toward flips allowed | 1803 | 55% | +69.3 | +0.04 | +22.5 | +0.3 | +16.3 / -14.4 / +20.6 | noise | 233 / +99.7 (late 0) |

ON vs LIVE: 447 setups only with toward ON, net -30.8, win 54% (flip trigger 1 / -3.6); 61 live setups displaced, net -53.3.
Late-away flip setups in LIVE: 14, net -25.9, win 29%.
SUMMARY: none

## MCL 2m — 10/25 to 11/03, 4630 candles; HTF flips 121, toward 53 (44%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 68 | 50% | +2.0 | +0.03 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 0 / +0.0 (late 0) |
| STRICT: toward off, no late-away | 68 | 50% | +2.0 | +0.03 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | noise | 0 / +0.0 (late 0) |
| Late-away 0 pts | 101 | 53% | +2.9 | +0.03 | +0.8 | +0.6 | +0.6 / +0.8 / -0.5 | noise | 0 / +0.0 (late 0) |
| ON: toward flips allowed | 128 | 57% | +4.6 | +0.04 | +2.5 | +1.4 | +1.4 / +1.0 / +0.1 | promising | 0 / +0.0 (late 0) |

ON vs LIVE: 60 setups only with toward ON, net +2.5, win 65% (flip trigger 0 / +0.0); 0 live setups displaced, net +0.0.
Late-away flip setups in LIVE: 0, net +0.0, win 0%.
SUMMARY: MCL 2m: ON: toward flips allowed → +2.5, z +1.4, thirds +1.4 / +1.0 / +0.1 (promising)

## MCL 3m — 10/25 to 11/03, 3088 candles; HTF flips 95, toward 37 (39%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 50 | 64% | +3.0 | +0.06 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 1 / +0.1 (late 0) |
| STRICT: toward off, no late-away | 50 | 64% | +3.0 | +0.06 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | noise | 1 / +0.1 (late 0) |
| Late-away 0 pts | 59 | 64% | +3.6 | +0.06 | +0.6 | +0.8 | +0.3 / +0.6 / -0.3 | noise | 1 / +0.1 (late 0) |
| ON: toward flips allowed | 70 | 61% | +3.1 | +0.04 | +0.1 | +0.1 | +0.5 / +1.4 / -1.8 | noise | 1 / +0.1 (late 0) |

ON vs LIVE: 20 setups only with toward ON, net +0.1, win 55% (flip trigger 0 / +0.0); 0 live setups displaced, net +0.0.
Late-away flip setups in LIVE: 0, net +0.0, win 0%.
SUMMARY: none

## MCL 5m — 10/25 to 11/03, 1853 candles; HTF flips 54, toward 23 (43%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 30 | 60% | +1.7 | +0.06 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 2 / -0.0 (late 0) |
| STRICT: toward off, no late-away | 30 | 60% | +1.7 | +0.06 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | noise | 2 / -0.0 (late 0) |
| Late-away 0 pts | 35 | 57% | +1.3 | +0.04 | -0.4 | -0.6 | +0.2 / -0.6 / +0.0 | worse | 2 / -0.0 (late 0) |
| ON: toward flips allowed | 46 | 54% | +1.3 | +0.03 | -0.4 | -0.3 | -0.3 / +0.3 / -0.4 | worse | 2 / -0.0 (late 0) |

ON vs LIVE: 16 setups only with toward ON, net -0.4, win 44% (flip trigger 0 / +0.0); 0 live setups displaced, net +0.0.
Late-away flip setups in LIVE: 0, net +0.0, win 0%.
SUMMARY: none

## BTC 2m — 06/01 to 10/23, 64496 candles; HTF flips 4101, toward 1879 (46%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1369 | 51% | -12561.9 | -9.18 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 572 / -6165.2 (late 77) |
| STRICT: toward off, no late-away | 1023 | 51% | -9193.1 | -8.99 | +3368.8 | +1.2 | +1299.6 / +659.2 / +1410.0 | promising | 495 / -6199.3 (late 0) |
| Late-away 0 pts | 1373 | 51% | -12787.7 | -9.31 | -225.7 | -0.5 | -202.4 / +1.7 / -25.0 | worse | 572 / -6494.0 (late 77) |
| ON: toward flips allowed | 1647 | 50% | -17740.5 | -10.77 | -5178.6 | -1.6 | -4096.0 / +2821.2 / -3903.7 | worse | 523 / -6951.2 (late 0) |

ON vs LIVE: 385 setups only with toward ON, net -5285.9, win 48% (flip trigger 28 / -751.9); 107 live setups displaced, net -107.3.
Late-away flip setups in LIVE: 77, net +34.1, win 60%.
SUMMARY: BTC 2m: STRICT: toward off, no late-away → +3368.8, z +1.2, thirds +1299.6 / +659.2 / +1410.0 (promising)

## BTC 3m — 01/05 to 10/23, 89942 candles; HTF flips 4996, toward 2210 (44%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1992 | 52% | -11126.0 | -5.59 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 678 / -6749.8 (late 66) |
| STRICT: toward off, no late-away | 1519 | 52% | -10757.6 | -7.08 | +368.4 | +0.1 | +3529.9 / -2700.7 / -460.9 | noise | 612 / -6348.2 (late 0) |
| Late-away 0 pts | 1999 | 52% | -11256.1 | -5.63 | -130.1 | -0.2 | +17.5 / -285.0 / +137.5 | worse | 676 / -6625.3 (late 64) |
| ON: toward flips allowed | 2432 | 52% | -17432.7 | -7.17 | -6306.7 | -1.3 | -3802.2 / +1358.1 / -3862.5 | worse | 639 / -7736.3 (late 0) |

ON vs LIVE: 581 setups only with toward ON, net -7334.6, win 52% (flip trigger 27 / -1388.1); 141 live setups displaced, net -1027.9.
Late-away flip setups in LIVE: 66, net -401.6, win 62%.
SUMMARY: none

## BTC 5m — 01/05 to 10/23, 57473 candles; HTF flips 3017, toward 1330 (44%)

| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |
|---|---|---|---|---|---|---|---|---|---|
| LIVE: toward off + late-away 1 pt | 1218 | 50% | -13207.6 | -10.84 | +0.0 | +0.0 | +0.0 / +0.0 / +0.0 | baseline | 328 / -8405.5 (late 27) |
| STRICT: toward off, no late-away | 932 | 50% | -7701.4 | -8.26 | +5506.2 | +1.5 | -381.1 / +1152.1 / +4735.1 | noise | 301 / -5817.9 (late 0) |
| Late-away 0 pts | 1218 | 50% | -12514.4 | -10.27 | +693.2 | +1.6 | +0.0 / +0.0 / +693.2 | noise | 327 / -8509.9 (late 26) |
| ON: toward flips allowed | 1520 | 51% | -13391.4 | -8.81 | -183.8 | -0.0 | -3234.1 / +3475.5 / -425.2 | worse | 305 / -5184.2 (late 0) |

ON vs LIVE: 371 setups only with toward ON, net -2975.8, win 54% (flip trigger 4 / +633.7); 69 live setups displaced, net -2792.0.
Late-away flip setups in LIVE: 27, net -2587.6, win 33%.
SUMMARY: none

