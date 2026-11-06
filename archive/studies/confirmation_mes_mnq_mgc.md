# 5m-confirmation backtest — MES, MNQ, MGC (11/05/2026)

MNQ: all three charts on 9/20, no gates, base exits (SL1 1.7 ATR min 25 cap 30, TP1 1.7 cap 40, 80 %, BE, trail 1.7); 2m data from Jan. MGC: 3m range gate + VWAP stretch 4 ATR, 2m / 5m no gates, base exits (cap 7 / TP cap 6).

# MES
three thirds; promising = z >= 1 and all three.
Usage: python3 confirm5_study.py   (needs chop_sim.py, mes3_ema_grid.py, late_study.py next to it)

## MES 2m setups confirmed by MES 5m (06/01 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 2m | 1735 | 51% | -126 | -0.07 | -256 / +198 / -68 | -0.43 / +0.36 / -0.12 |
| Confirmed by 5m | 398 | 54% | +81 | +0.20 | +21 / +68 / -8 | +0.17 / +0.54 / -0.05 |
| Not confirmed | 1337 | 50% | -207 | -0.15 | -277 / +131 / -60 | -0.59 / +0.31 / -0.14 |

Confirmed minus unconfirmed avg: +0.36 pts/setup, z +1.3, better in thirds: yes / yes / yes → **promising**. Taking only confirmed setups: +81 vs -126 for all.
Confirmed by trigger: flip 108 / +11 · h20 21 / +4 · h9 74 / +38 · ltf20 195 / +28

## MES 3m setups confirmed by MES 5m (01/06 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 3m | 1654 | 46% | -109 | -0.07 | +228 / -525 / +187 | +0.46 / -0.96 / +0.31 |
| Confirmed by 5m | 464 | 47% | +121 | +0.26 | +187 / -142 / +76 | +1.38 / -0.94 / +0.43 |
| Not confirmed | 1190 | 45% | -230 | -0.19 | +41 / -382 / +111 | +0.11 / -0.97 / +0.26 |

Confirmed minus unconfirmed avg: +0.45 pts/setup, z +1.1, better in thirds: yes / yes / yes → **promising**. Taking only confirmed setups: +121 vs -109 for all.
Confirmed by trigger: flip 70 / -55 · h20 35 / +56 · h9 84 / +75 · ltf20 275 / +45

## MES 5m setups confirmed by MES 2m (06/01 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 5m | 611 | 52% | +97 | +0.16 | +129 / -54 / +23 | +0.66 / -0.26 / +0.11 |
| Confirmed by 2m | 244 | 56% | +80 | +0.33 | +15 / +28 / +38 | +0.18 / +0.36 / +0.43 |
| Not confirmed | 367 | 50% | +17 | +0.05 | +114 / -82 / -15 | +1.00 / -0.62 / -0.13 |

Confirmed minus unconfirmed avg: +0.28 pts/setup, z +0.6, better in thirds: no / yes / yes → **noise**. Taking only confirmed setups: +80 vs +97 for all.
Confirmed by trigger: flip 99 / -9 · h20 11 / +20 · h9 23 / +30 · ltf20 111 / +40

## MES 5m setups confirmed by MES 3m (01/06 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 5m | 1179 | 51% | +13 | +0.01 | -61 / +111 / -37 | -0.16 / +0.29 / -0.09 |
| Confirmed by 3m | 441 | 51% | -43 | -0.10 | +22 / -24 / -41 | +0.15 / -0.17 / -0.27 |
| Not confirmed | 738 | 51% | +56 | +0.08 | -83 / +134 / +4 | -0.35 / +0.56 / +0.02 |

Confirmed minus unconfirmed avg: -0.17 pts/setup, z -0.5, better in thirds: yes / no / no → **worse**. Taking only confirmed setups: -43 vs +13 for all.
Confirmed by trigger: flip 118 / -91 · h20 20 / +14 · h9 57 / -32 · ltf20 246 / +65

## MES 2m setups confirmed by MES 3m (06/01 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 2m | 1744 | 51% | -119 | -0.07 | -263 / +208 / -64 | -0.44 / +0.38 / -0.11 |
| Confirmed by 3m | 523 | 51% | -38 | -0.07 | -52 / -7 / +21 | -0.31 / -0.04 / +0.12 |
| Not confirmed | 1221 | 51% | -81 | -0.07 | -211 / +215 / -85 | -0.49 / +0.58 / -0.20 |

Confirmed minus unconfirmed avg: -0.01 pts/setup, z -0.0, better in thirds: yes / no / yes → **worse**. Taking only confirmed setups: -38 vs -119 for all.
Confirmed by trigger: flip 182 / +71 · h20 31 / -18 · h9 92 / +0 · ltf20 218 / -91

## MES 3m setups confirmed by MES 2m (06/01 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 3m | 894 | 45% | -211 | -0.24 | -414 / -62 / +265 | -1.52 / -0.19 / +0.91 |
| Confirmed by 2m | 424 | 47% | -126 | -0.30 | -264 / -26 / +164 | -2.03 / -0.18 / +1.14 |
| Not confirmed | 470 | 43% | -85 | -0.18 | -150 / -36 / +101 | -1.05 / -0.20 / +0.69 |

Confirmed minus unconfirmed avg: -0.11 pts/setup, z -0.2, better in thirds: no / yes / yes → **worse**. Taking only confirmed setups: -126 vs -211 for all.
Confirmed by trigger: flip 115 / -98 · h20 24 / +15 · h9 59 / +6 · ltf20 226 / -48

## Candidates (robust / promising)

- MES 2m confirmed by 5m: avg +0.20 vs -0.15 unconfirmed, z +1.3, only-confirmed net +81 vs all -126 (promising)
- MES 3m confirmed by 5m: avg +0.26 vs -0.19 unconfirmed, z +1.1, only-confirmed net +121 vs all -109 (promising)

# MNQ

## MNQ 2m setups confirmed by MNQ 5m (01/06 → 10/30)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 2m | 2748 | 47% | -67 | -0.02 | +165 / +227 / -460 | +0.18 / +0.24 / -0.51 |
| Confirmed by 5m | 592 | 47% | +303 | +0.51 | -113 / +351 / +65 | -0.60 / +1.65 / +0.34 |
| Not confirmed | 2156 | 47% | -370 | -0.17 | +278 / -123 / -525 | +0.39 / -0.17 / -0.73 |

Confirmed minus unconfirmed avg: +0.68 pts/setup, z +0.6, better in thirds: no / yes / yes → **noise**. Taking only confirmed setups: +303 vs -67 for all.
Confirmed by trigger: flip 176 / -177 · h20 40 / +119 · h9 103 / +488 · ltf20 273 / -127

## MNQ 3m setups confirmed by MNQ 5m (01/06 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 3m | 1921 | 46% | +136 | +0.07 | +381 / -88 / -156 | +0.65 / -0.14 / -0.22 |
| Confirmed by 5m | 497 | 43% | -782 | -1.57 | -30 / -129 / -623 | -0.21 / -0.70 / -3.68 |
| Not confirmed | 1424 | 47% | +918 | +0.64 | +411 / +40 / +466 | +0.92 / +0.09 / +0.88 |

Confirmed minus unconfirmed avg: -2.22 pts/setup, z -1.5, better in thirds: no / no / no → **worse**. Taking only confirmed setups: -782 vs +136 for all.
Confirmed by trigger: flip 141 / +206 · h20 27 / +344 · h9 77 / -88 · ltf20 252 / -1245

## MNQ 5m setups confirmed by MNQ 2m (01/06 → 10/30)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 5m | 1104 | 47% | +1798 | +1.63 | +872 / +1157 / -231 | +2.53 / +3.01 / -0.61 |
| Confirmed by 2m | 375 | 47% | +346 | +0.92 | -344 / +126 / +564 | -2.91 / +0.89 / +4.86 |
| Not confirmed | 729 | 46% | +1452 | +1.99 | +1215 / +1032 / -795 | +5.35 / +4.25 / -3.07 |

Confirmed minus unconfirmed avg: -1.07 pts/setup, z -0.5, better in thirds: no / no / yes → **worse**. Taking only confirmed setups: +346 vs +1798 for all.
Confirmed by trigger: flip 139 / -316 · h20 16 / -59 · h9 46 / +658 · ltf20 174 / +63

## MNQ 5m setups confirmed by MNQ 3m (01/06 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 5m | 1118 | 47% | +2085 | +1.87 | +1048 / +1022 / +15 | +2.91 / +2.68 / +0.04 |
| Confirmed by 3m | 434 | 46% | +440 | +1.01 | +739 / +117 / -417 | +5.40 / +0.78 / -2.86 |
| Not confirmed | 684 | 47% | +1646 | +2.41 | +309 / +905 / +432 | +1.39 / +3.92 / +1.88 |

Confirmed minus unconfirmed avg: -1.39 pts/setup, z -0.7, better in thirds: yes / no / no → **worse**. Taking only confirmed setups: +440 vs +2085 for all.
Confirmed by trigger: flip 141 / -80 · h20 15 / -87 · h9 65 / +842 · ltf20 213 / -235

## MNQ 2m setups confirmed by MNQ 3m (01/05 → 10/30)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 2m | 2752 | 47% | -43 | -0.02 | +207 / +217 / -468 | +0.23 / +0.23 / -0.51 |
| Confirmed by 3m | 989 | 49% | +863 | +0.87 | +458 / -269 / +674 | +1.49 / -0.82 / +1.90 |
| Not confirmed | 1763 | 45% | -906 | -0.51 | -251 / +486 / -1141 | -0.42 / +0.79 / -2.06 |

Confirmed minus unconfirmed avg: +1.39 pts/setup, z +1.4, better in thirds: yes / no / yes → **noise**. Taking only confirmed setups: +863 vs -43 for all.
Confirmed by trigger: flip 334 / +387 · h20 55 / -77 · h9 150 / -165 · ltf20 450 / +717

## MNQ 3m setups confirmed by MNQ 2m (01/05 → 10/30)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 3m | 1889 | 46% | +275 | +0.15 | +457 / -387 / +206 | +0.79 / -0.62 / +0.30 |
| Confirmed by 2m | 878 | 49% | +1316 | +1.50 | +178 / +322 / +817 | +0.63 / +1.08 / +2.77 |
| Not confirmed | 1011 | 43% | -1041 | -1.03 | +279 / -709 / -611 | +0.95 / -2.15 / -1.57 |

Confirmed minus unconfirmed avg: +2.53 pts/setup, z +1.9, better in thirds: no / yes / yes → **noise**. Taking only confirmed setups: +1316 vs +275 for all.
Confirmed by trigger: flip 342 / +664 · h20 36 / +206 · h9 111 / -83 · ltf20 389 / +530

## Candidates (robust / promising)

- none


# MGC

## MGC 2m setups confirmed by MGC 5m (06/01 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 2m | 1471 | 52% | +396 | +0.27 | +55 / +203 / +138 | +0.11 / +0.43 / +0.28 |
| Confirmed by 5m | 286 | 50% | +5 | +0.02 | +12 / +55 / -61 | +0.10 / +0.63 / -0.70 |
| Not confirmed | 1185 | 53% | +391 | +0.33 | +44 / +148 / +199 | +0.11 / +0.38 / +0.49 |

Confirmed minus unconfirmed avg: -0.31 pts/setup, z -1.0, better in thirds: no / yes / no → **worse**. Taking only confirmed setups: +5 vs +396 for all.
Confirmed by trigger: flip 87 / -54 · h20 26 / -24 · h9 59 / +12 · ltf20 114 / +71

## MGC 3m setups confirmed by MGC 5m (01/05 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 3m | 1687 | 50% | +224 | +0.13 | +72 / +126 / +25 | +0.12 / +0.23 / +0.05 |
| Confirmed by 5m | 399 | 51% | +144 | +0.36 | +69 / +52 / +24 | +0.59 / +0.37 / +0.17 |
| Not confirmed | 1288 | 50% | +80 | +0.06 | +4 / +74 / +2 | +0.01 / +0.18 / +0.00 |

Confirmed minus unconfirmed avg: +0.30 pts/setup, z +0.9, better in thirds: yes / yes / yes → **noise**. Taking only confirmed setups: +144 vs +224 for all.
Confirmed by trigger: flip 74 / -5 · h20 34 / +1 · h9 81 / +119 · ltf20 210 / +29

## MGC 5m setups confirmed by MGC 2m (06/01 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 5m | 576 | 51% | -23 | -0.04 | +64 / +85 / -172 | +0.32 / +0.46 / -0.88 |
| Confirmed by 2m | 203 | 52% | -15 | -0.07 | +20 / +8 / -44 | +0.30 / +0.12 / -0.68 |
| Not confirmed | 373 | 50% | -8 | -0.02 | +44 / +77 / -128 | +0.34 / +0.68 / -0.97 |

Confirmed minus unconfirmed avg: -0.05 pts/setup, z -0.1, better in thirds: no / no / yes → **worse**. Taking only confirmed setups: -15 vs -23 for all.
Confirmed by trigger: flip 80 / -38 · h20 10 / +19 · h9 22 / -18 · ltf20 91 / +22

## MGC 5m setups confirmed by MGC 3m (01/05 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 5m | 1153 | 51% | -85 | -0.07 | -147 / +115 / -54 | -0.37 / +0.31 / -0.14 |
| Confirmed by 3m | 362 | 47% | -262 | -0.72 | -113 / -18 / -132 | -0.98 / -0.15 / -1.04 |
| Not confirmed | 791 | 53% | +176 | +0.22 | -34 / +133 / +77 | -0.12 / +0.52 / +0.31 |

Confirmed minus unconfirmed avg: -0.95 pts/setup, z -2.4, better in thirds: no / no / no → **worse**. Taking only confirmed setups: -262 vs -85 for all.
Confirmed by trigger: flip 110 / -85 · h20 23 / -25 · h9 50 / -66 · ltf20 179 / -86

## MGC 2m setups confirmed by MGC 3m (06/01 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 2m | 1471 | 52% | +396 | +0.27 | +55 / +203 / +138 | +0.11 / +0.43 / +0.28 |
| Confirmed by 3m | 381 | 51% | +88 | +0.23 | +12 / +4 / +71 | +0.09 / +0.03 / +0.57 |
| Not confirmed | 1090 | 52% | +308 | +0.28 | +43 / +199 / +67 | +0.12 / +0.56 / +0.18 |

Confirmed minus unconfirmed avg: -0.05 pts/setup, z -0.2, better in thirds: no / no / yes → **worse**. Taking only confirmed setups: +88 vs +396 for all.
Confirmed by trigger: flip 142 / +9 · h20 25 / -1 · h9 61 / -5 · ltf20 153 / +86

## MGC 3m setups confirmed by MGC 2m (06/01 → 11/05)

| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |
|---|---|---|---|---|---|---|
| All 3m | 849 | 49% | +99 | +0.12 | +107 / -122 / +115 | +0.37 / -0.47 / +0.39 |
| Confirmed by 2m | 348 | 49% | +32 | +0.09 | +17 / -74 / +89 | +0.14 / -0.65 / +0.79 |
| Not confirmed | 501 | 49% | +67 | +0.13 | +90 / -48 / +26 | +0.53 / -0.33 / +0.14 |

Confirmed minus unconfirmed avg: -0.04 pts/setup, z -0.1, better in thirds: no / no / yes → **worse**. Taking only confirmed setups: +32 vs +99 for all.
Confirmed by trigger: flip 109 / +7 · h20 26 / +36 · h9 60 / +31 · ltf20 153 / -42

## Candidates (robust / promising)

- none

