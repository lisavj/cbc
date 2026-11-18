Prior day / week / month high-low levels in CBC EMA Slope 3m -- MES / MGC / MNQ / M2K -- 11/18/2026.
Base = current 3m settings (claude/noflip_study.py CH = v1.19 logic = v1.23). Replay Jan 5 -> now, net after costs.
Levels (CME session days from 18:00 ET, completed periods only): PDH/PDL = prior session day, PWH/PWL = prior week, PMH/PML = prior month.
Gates (one at a time):
 R<k> <set>: skip when the nearest level of <set> in the trade direction is within k x TP1 distance (long: level above entry).
 X <set>: skip trades against an accepted break -- long while close < prior low, short while close > prior high.
 M  : prior-day midpoint side -- long only above (PDH+PDL)/2, short only below.
Exits:
 T1 : if a D/W/M level sits between entry and TP1 (and >= 0.5 x TP1 away), TP1 moves to that level minus 0.1 ATR.
 T2 : (ride trades, MES flip) close at the first D/W/M level reached (minus 0.1 ATR) instead of riding to the HTF flip.
 S1 : if a D/W/M level sits between entry and SL1 (>= 0.5 x SL1 away), SL1 moves to 0.25 ATR beyond that level (tighter only).
z = Δ / (SD x sqrt(trades changed)); robust = z >= 2, all thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds.

## MES 3m (bars to 11/18)

Base: 711 trades, net +780, win 51 %, thirds +370 / +98 / +312, last 4 wk +202, max DD 142.

Base trades by room to the nearest D/W/M level (in TP1 units):

| Room | Trades | Net | Avg |
|---|---|---|---|
| 0.0-0.5 | 35 | +50 | +1.44 |
| 0.5-1.0 | 37 | +44 | +1.20 |
| 1.0-1.5 | 33 | +45 | +1.37 |
| 1.5-3.0 | 89 | +121 | +1.36 |
| 3.0-up | 445 | +329 | +0.74 |

| Change | Trades | Net | vs base | Changed | z | Change by third | Last 4 wk | Max DD (vs base) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| R0.5 D: skip if D level within 0.5 x TP1 | 691 | +769 | -11 | 30 | -0.2 | -11 / +11 / -11 | -10 | 128 (-14) | worse |
| R0.5 W: skip if W level within 0.5 x TP1 | 704 | +743 | -37 | 9 | -1.3 | -19 / -13 / -5 | -11 | 143 (+1) | worse |
| R0.5 M: skip if M level within 0.5 x TP1 | 707 | +756 | -25 | 4 | -1.3 | -20 / +0 / -4 | -11 | 142 (+0) | worse |
| R0.5 DWM: skip if DWM level within 0.5 x TP1 | 682 | +730 | -50 | 41 | -0.8 | -50 / +9 / -9 | -20 | 129 (-12) | worse |
| R1.0 D: skip if D level within 1.0 x TP1 | 665 | +736 | -45 | 62 | -0.6 | -32 / +7 / -20 | +0 | 124 (-17) | worse |
| R1.0 W: skip if W level within 1.0 x TP1 | 696 | +723 | -57 | 19 | -1.3 | -75 / +11 / +7 | +1 | 130 (-11) | worse |
| R1.0 M: skip if M level within 1.0 x TP1 | 703 | +763 | -18 | 8 | -0.6 | -25 / +0 / +7 | +4 | 142 (+0) | worse |
| R1.0 DWM: skip if DWM level within 1.0 x TP1 | 648 | +697 | -83 | 83 | -0.9 | -112 / +29 / -1 | +4 | 113 (-28) | worse |
| R1.5 D: skip if D level within 1.5 x TP1 | 647 | +683 | -98 | 88 | -1.1 | -51 / -17 / -30 | +3 | 122 (-20) | worse |
| R1.5 W: skip if W level within 1.5 x TP1 | 688 | +706 | -74 | 29 | -1.4 | -85 / +8 / +3 | +1 | 116 (-25) | worse |
| R1.5 M: skip if M level within 1.5 x TP1 | 699 | +766 | -14 | 12 | -0.4 | -24 / +7 / +3 | +4 | 142 (+0) | worse |
| R1.5 DWM: skip if DWM level within 1.5 x TP1 | 620 | +636 | -144 | 119 | -1.4 | -140 / +11 / -15 | +7 | 97 (-45) | worse |
| X D: skip trades against an accepted prior-day break | 706 | +775 | -5 | 7 | -0.2 | -8 / +11 / -8 | +0 | 131 (-11) | worse |
| X W: skip trades against an accepted prior-week break | 653 | +610 | -170 | 66 | -2.2 | -85 / -38 / -48 | -36 | 122 (-20) | robustly worse |
| X M: skip trades against an accepted prior-month break | 623 | +763 | -17 | 88 | -0.2 | -16 / +3 / -4 | -36 | 142 (+0) | worse |
| M: long only above prior-day midpoint, short only below | 552 | +496 | -285 | 175 | -2.2 | -126 / -15 / -143 | -79 | 107 (-35) | robustly worse |
| T1: TP1 at the D/W/M level when it sits inside TP1 | 712 | +779 | -1 | 18 | -0.0 | -8 / +8 / -1 | +0 | 143 (+1) | worse |
| S1: SL1 just beyond the D/W/M level when it sits inside SL1 | 712 | +789 | +9 | 16 | +0.2 | +2 / +2 / +5 | +19 | 139 (-3) | noise |
| T2: flip-ride trades close at the first D/W/M level | 726 | +643 | -137 | 40 | -2.2 | -55 / -61 / -21 | +12 | 163 (+21) | robustly worse |

## MGC 3m (bars to 11/18)

Base: 624 trades, net +1740, win 26 %, thirds +1037 / +134 / +569, last 4 wk +161, max DD 114.

Base trades by room to the nearest D/W/M level (in TP1 units):

| Room | Trades | Net | Avg |
|---|---|---|---|
| 0.0-0.5 | 27 | -51 | -1.90 |
| 0.5-1.0 | 25 | +2 | +0.08 |
| 1.0-1.5 | 30 | +74 | +2.45 |
| 1.5-3.0 | 70 | +156 | +2.23 |
| 3.0-up | 436 | +1572 | +3.61 |

| Change | Trades | Net | vs base | Changed | z | Change by third | Last 4 wk | Max DD (vs base) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| R0.5 D: skip if D level within 0.5 x TP1 | 607 | +1801 | +61 | 21 | +0.7 | +11 / +42 / +8 | +6 | 114 (+0) | noise |
| R0.5 W: skip if W level within 0.5 x TP1 | 620 | +1744 | +4 | 8 | +0.1 | -7 / +0 / +11 | +0 | 114 (+0) | noise |
| R0.5 M: skip if M level within 0.5 x TP1 | 622 | +1744 | +4 | 2 | +0.2 | +0 / +4 / +0 | +0 | 114 (+0) | noise |
| R0.5 DWM: skip if DWM level within 0.5 x TP1 | 601 | +1809 | +69 | 31 | +0.7 | +3 / +46 / +19 | +6 | 114 (+0) | noise |
| R1.0 D: skip if D level within 1.0 x TP1 | 586 | +1760 | +20 | 44 | +0.2 | +19 / +3 / -1 | -5 | 106 (-7) | noise |
| R1.0 W: skip if W level within 1.0 x TP1 | 615 | +1752 | +12 | 17 | +0.2 | -16 / +10 / +19 | +0 | 106 (-7) | noise |
| R1.0 M: skip if M level within 1.0 x TP1 | 622 | +1744 | +4 | 2 | +0.2 | +0 / +4 / +0 | +0 | 114 (+0) | noise |
| R1.0 DWM: skip if DWM level within 1.0 x TP1 | 578 | +1764 | +24 | 58 | +0.2 | -5 / +17 / +12 | -5 | 106 (-7) | noise |
| R1.5 D: skip if D level within 1.5 x TP1 | 563 | +1695 | -45 | 69 | -0.3 | +25 / +21 / -91 | +7 | 106 (-7) | worse |
| R1.5 W: skip if W level within 1.5 x TP1 | 611 | +1728 | -12 | 19 | -0.1 | -25 / +9 / +4 | +0 | 106 (-7) | worse |
| R1.5 M: skip if M level within 1.5 x TP1 | 618 | +1752 | +12 | 6 | +0.3 | +7 / +4 / +0 | +0 | 114 (+0) | noise |
| R1.5 DWM: skip if DWM level within 1.5 x TP1 | 548 | +1682 | -57 | 88 | -0.3 | -0 / +35 / -92 | +7 | 106 (-7) | worse |
| X D: skip trades against an accepted prior-day break | 584 | +1755 | +16 | 42 | +0.1 | -13 / +8 / +20 | +7 | 113 (-0) | noise |
| X W: skip trades against an accepted prior-week break | 570 | +1778 | +38 | 54 | +0.3 | +14 / +3 / +22 | +16 | 92 (-22) | noise |
| X M: skip trades against an accepted prior-month break | 560 | +1622 | -118 | 66 | -0.8 | +15 / -36 / -97 | -13 | 114 (+0) | worse |
| M: long only above prior-day midpoint, short only below | 406 | +1441 | -299 | 230 | -1.1 | -165 / -44 / -90 | +32 | 89 (-25) | worse |
| T1: TP1 at the D/W/M level when it sits inside TP1 | 624 | +1744 | +4 | 1 | +0.2 | +0 / +0 / +4 | +0 | 114 (+0) | noise |
| S1: SL1 just beyond the D/W/M level when it sits inside SL1 | 624 | +1730 | -10 | 7 | -0.2 | +0 / +3 / -12 | -4 | 114 (+0) | worse |

## MNQ 3m (bars to 11/18)

Base: 448 trades, net +6455, win 33 %, thirds +2270 / +2386 / +1798, last 4 wk +1473, max DD 278.

Base trades by room to the nearest D/W/M level (in TP1 units):

| Room | Trades | Net | Avg |
|---|---|---|---|
| 0.0-0.5 | 27 | +519 | +19.22 |
| 0.5-1.0 | 19 | +741 | +38.98 |
| 1.0-1.5 | 17 | +164 | +9.63 |
| 1.5-3.0 | 52 | +991 | +19.05 |
| 3.0-up | 273 | +4024 | +14.74 |

| Change | Trades | Net | vs base | Changed | z | Change by third | Last 4 wk | Max DD (vs base) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| R0.5 D: skip if D level within 0.5 x TP1 | 436 | +6266 | -189 | 18 | -0.6 | -44 / -160 / +15 | +37 | 278 (+0) | worse |
| R0.5 W: skip if W level within 0.5 x TP1 | 447 | +6335 | -120 | 5 | -0.7 | +0 / -85 / -35 | +0 | 287 (+9) | worse |
| R0.5 M: skip if M level within 0.5 x TP1 | 442 | +6317 | -138 | 12 | -0.5 | -86 / +12 / -64 | +0 | 271 (-7) | worse |
| R0.5 DWM: skip if DWM level within 0.5 x TP1 | 429 | +6008 | -447 | 35 | -1.0 | -130 / -233 / -84 | +37 | 285 (+7) | worse |
| R1.0 D: skip if D level within 1.0 x TP1 | 425 | +5736 | -719 | 37 | -1.5 | -310 / -232 / -177 | +38 | 321 (+42) | worse |
| R1.0 W: skip if W level within 1.0 x TP1 | 442 | +6197 | -258 | 14 | -0.9 | +41 / -155 / -144 | -134 | 326 (+47) | worse |
| R1.0 M: skip if M level within 1.0 x TP1 | 439 | +6333 | -122 | 11 | -0.5 | -84 / +27 / -64 | +0 | 271 (-7) | worse |
| R1.0 DWM: skip if DWM level within 1.0 x TP1 | 411 | +5338 | -1116 | 55 | -2.0 | -392 / -340 / -385 | -96 | 294 (+15) | worse |
| R1.5 D: skip if D level within 1.5 x TP1 | 419 | +5576 | -879 | 45 | -1.7 | -305 / -339 / -235 | +38 | 321 (+42) | worse |
| R1.5 W: skip if W level within 1.5 x TP1 | 438 | +6007 | -448 | 24 | -1.2 | +42 / -405 / -85 | -77 | 326 (+47) | worse |
| R1.5 M: skip if M level within 1.5 x TP1 | 435 | +6345 | -109 | 17 | -0.3 | -76 / +20 / -54 | +10 | 271 (-7) | worse |
| R1.5 DWM: skip if DWM level within 1.5 x TP1 | 397 | +5182 | -1273 | 75 | -1.9 | -379 / -537 / -357 | -28 | 294 (+15) | worse |
| X D: skip trades against an accepted prior-day break | 443 | +6106 | -349 | 9 | -1.5 | -291 / -58 / +1 | +1 | 278 (+0) | worse |
| X W: skip trades against an accepted prior-week break | 412 | +5208 | -1247 | 38 | -2.6 | -543 / -199 / -505 | -572 | 339 (+61) | robustly worse |
| X M: skip trades against an accepted prior-month break | 409 | +5618 | -836 | 41 | -1.7 | -23 / -216 / -598 | -573 | 278 (+0) | worse |
| M: long only above prior-day midpoint, short only below | 388 | +4634 | -1820 | 68 | -2.9 | -870 / -984 / +34 | +140 | 428 (+150) | worse |
| T1: TP1 at the D/W/M level when it sits inside TP1 | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 278 (+0) | noise |
| S1: SL1 just beyond the D/W/M level when it sits inside SL1 | 449 | +6314 | -141 | 8 | -0.7 | +9 / -160 / +10 | +9 | 307 (+28) | worse |

## M2K 3m (bars to 11/18)

Base: 367 trades, net +214, win 40 %, thirds +86 / +100 / +28, last 4 wk +8, max DD 47.

Base trades by room to the nearest D/W/M level (in TP1 units):

| Room | Trades | Net | Avg |
|---|---|---|---|
| 0.0-0.5 | 13 | +20 | +1.53 |
| 0.5-1.0 | 16 | -4 | -0.25 |
| 1.0-1.5 | 21 | +36 | +1.72 |
| 1.5-3.0 | 48 | +25 | +0.52 |
| 3.0-up | 244 | +144 | +0.59 |

| Change | Trades | Net | vs base | Changed | z | Change by third | Last 4 wk | Max DD (vs base) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| R0.5 D: skip if D level within 0.5 x TP1 | 359 | +194 | -20 | 10 | -1.3 | -4 / -14 / -2 | +0 | 47 (+0) | worse |
| R0.5 W: skip if W level within 0.5 x TP1 | 363 | +215 | +2 | 4 | +0.2 | -6 / -0 / +8 | +0 | 47 (+0) | noise |
| R0.5 M: skip if M level within 0.5 x TP1 | 366 | +215 | +1 | 1 | +0.3 | +0 / +0 / +1 | +1 | 47 (+0) | noise |
| R0.5 DWM: skip if DWM level within 0.5 x TP1 | 355 | +192 | -22 | 14 | -1.2 | -10 / -19 / +7 | +1 | 47 (+0) | worse |
| R1.0 D: skip if D level within 1.0 x TP1 | 349 | +190 | -24 | 22 | -1.0 | -6 / -15 / -3 | -2 | 47 (+0) | worse |
| R1.0 W: skip if W level within 1.0 x TP1 | 358 | +210 | -3 | 13 | -0.2 | -9 / -6 / +12 | +0 | 45 (-2) | worse |
| R1.0 M: skip if M level within 1.0 x TP1 | 366 | +215 | +1 | 1 | +0.3 | +0 / +0 / +1 | +1 | 47 (+0) | noise |
| R1.0 DWM: skip if DWM level within 1.0 x TP1 | 342 | +194 | -19 | 33 | -0.7 | -12 / -18 / +11 | -0 | 45 (-2) | worse |
| R1.5 D: skip if D level within 1.5 x TP1 | 334 | +203 | -10 | 37 | -0.3 | -5 / -9 / +3 | -2 | 47 (-0) | worse |
| R1.5 W: skip if W level within 1.5 x TP1 | 350 | +208 | -6 | 17 | -0.3 | -13 / -6 / +13 | -0 | 44 (-3) | worse |
| R1.5 M: skip if M level within 1.5 x TP1 | 365 | +215 | +2 | 2 | +0.2 | +0 / +0 / +1 | +1 | 47 (+0) | noise |
| R1.5 DWM: skip if DWM level within 1.5 x TP1 | 319 | +206 | -8 | 52 | -0.2 | -14 / -11 / +17 | -1 | 44 (-3) | worse |
| X D: skip trades against an accepted prior-day break | 361 | +172 | -41 | 6 | -3.4 | +2 / -42 / -1 | -1 | 47 (+0) | worse |
| X W: skip trades against an accepted prior-week break | 330 | +213 | -1 | 37 | -0.0 | +6 / -25 / +18 | +9 | 45 (-2) | worse |
| X M: skip trades against an accepted prior-month break | 314 | +158 | -56 | 53 | -1.6 | -25 / -39 / +8 | +4 | 36 (-11) | worse |
| M: long only above prior-day midpoint, short only below | 276 | +179 | -35 | 91 | -0.7 | -14 / -35 / +14 | +7 | 43 (-4) | worse |
| T1: TP1 at the D/W/M level when it sits inside TP1 | 368 | +219 | +5 | 4 | +0.6 | +0 / +3 / +2 | +0 | 44 (-3) | noise |
| S1: SL1 just beyond the D/W/M level when it sits inside SL1 | 367 | +213 | -1 | 6 | -0.1 | -2 / +0 / +1 | +1 | 47 (+0) | worse |
