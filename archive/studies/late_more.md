# LTF EMA20 Pierce late-confirm window — Thu 11/05/2026 08:35

LTF EMA20 Pierce late-confirm window study -- 11/05/2026.
Question: CBC "LTF pierce late-confirm window (bars)" = 1 (one setting for every chart). If the pierce candle does not close back
beyond the slow chart EMA, the next N candles may (first close back beyond the line, HTF direction unchanged). Best N per chart?
Engine: mes3_ema_grid MCase (chop_sim rules), LTF late window = N (0 = pierce candle only). Charts on live settings:
MES 3m slow 14 and slow 20 (live exits SL 3 / TP1 2.0 / time-of-day close), MGC 3m slow 20 (range gate + VWAP stretch 4 ATR,
base exits). Jan 5 -> now. z / robust / promising as in the other studies (thirds = equal time).
Usage: python3 late_study.py   (needs chop_sim.py + mes3_ema_grid.py next to it)

## MES 2m slow 14 (MTF gate) — 77883 candles

| Window | Setups | Win % | Net | Avg | Δ vs 1 (current) | z | Δ by third | Verdict | LTF20 setups / net (late ones) | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1662 | 51% | -151 | -0.09 | -31 | -0.5 | -44 / +7 / +5 | worse | 695 / +106 (late 0 / +0) | +1.1 |
| 1 (current) | 1744 | 51% | -119 | -0.07 | +0 | +0.0 | +0 / +0 / +0 | baseline | 795 / +110 (late 135 / +25) | +0.0 |
| 2 | 1777 | 51% | -123 | -0.07 | -3 | -0.1 | +17 / -3 / -17 | worse | 836 / +85 (late 192 / +8) | -6.7 |
| 3 | 1791 | 51% | -90 | -0.05 | +29 | +0.6 | +32 / +7 / -10 | noise | 854 / +112 (late 214 / +31) | -8.2 |
| 4 | 1798 | 51% | -110 | -0.06 | +9 | +0.2 | +17 / +1 / -9 | noise | 865 / +93 (late 227 / +15) | +1.4 |
| 5 | 1801 | 51% | -133 | -0.07 | -13 | -0.2 | +14 / -4 / -23 | worse | 870 / +79 (late 232 / +1) | -2.1 |

## MGC 2m slow 20 — 77940 candles

| Window | Setups | Win % | Net | Avg | Δ vs 1 (current) | z | Δ by third | Verdict | LTF20 setups / net (late ones) | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1416 | 52% | +351 | +0.25 | -46 | -0.9 | -36 / -7 / -2 | worse | 543 / +293 (late 0 / +0) | +6.4 |
| 1 (current) | 1471 | 52% | +396 | +0.27 | +0 | +0.0 | +0 / +0 / +0 | baseline | 613 / +341 (late 80 / +47) | +0.0 |
| 2 | 1500 | 52% | +396 | +0.26 | -1 | -0.0 | +3 / +27 / -30 | worse | 652 / +341 (late 131 / +56) | -1.2 |
| 3 | 1506 | 52% | +393 | +0.26 | -3 | -0.1 | -8 / +35 / -30 | worse | 662 / +342 (late 147 / +47) | +0.9 |
| 4 | 1515 | 52% | +384 | +0.25 | -13 | -0.2 | -24 / +35 / -23 | worse | 671 / +336 (late 158 / +40) | +6.4 |
| 5 | 1519 | 52% | +376 | +0.25 | -20 | -0.4 | -20 / +32 / -33 | worse | 678 / +313 (late 165 / +17) | -5.6 |

## MES 5m slow 20 — 59865 candles

| Window | Setups | Win % | Net | Avg | Δ vs 1 (current) | z | Δ by third | Verdict | LTF20 setups / net (late ones) | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1123 | 51% | -41 | -0.04 | -54 | -1.0 | -35 / +5 / -24 | worse | 485 / -164 (late 0 / +0) | -0.3 |
| 1 (current) | 1179 | 51% | +13 | +0.01 | +0 | +0.0 | +0 / +0 / +0 | baseline | 547 / -107 (late 70 / +51) | +0.0 |
| 2 | 1202 | 51% | -41 | -0.03 | -54 | -1.3 | -34 / -1 / -20 | worse | 575 / -171 (late 104 / +12) | -4.4 |
| 3 | 1214 | 51% | -74 | -0.06 | -87 | -1.7 | -19 / -29 / -38 | worse | 589 / -209 (late 121 / -8) | -12.4 |
| 4 | 1220 | 51% | -59 | -0.05 | -72 | -1.3 | -3 / -29 / -40 | worse | 597 / -192 (late 131 / +6) | -20.6 |
| 5 | 1223 | 51% | -68 | -0.06 | -81 | -1.5 | -3 / -25 / -53 | worse | 600 / -201 (late 134 / -3) | -26.5 |

## MGC 5m slow 20 — 59772 candles

| Window | Setups | Win % | Net | Avg | Δ vs 1 (current) | z | Δ by third | Verdict | LTF20 setups / net (late ones) | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1095 | 52% | -1 | -0.00 | +84 | +1.3 | +20 / +39 / +25 | promising | 475 / +55 (late 0 / +0) | +30.2 |
| 1 (current) | 1153 | 51% | -85 | -0.07 | +0 | +0.0 | +0 / +0 / +0 | baseline | 543 / -25 (late 76 / -80) | +0.0 |
| 2 | 1173 | 52% | -60 | -0.05 | +25 | +0.6 | -25 / +4 / +47 | noise | 567 / -25 (late 103 / -89) | +24.9 |
| 3 | 1180 | 52% | -37 | -0.03 | +48 | +1.0 | -32 / +20 / +60 | noise | 575 / -4 (late 115 / -70) | +29.8 |
| 4 | 1185 | 52% | -20 | -0.02 | +66 | +1.3 | -22 / +20 / +68 | noise | 580 / +13 (late 121 / -63) | +29.8 |
| 5 | 1187 | 52% | -10 | -0.01 | +76 | +1.4 | -29 / +44 / +61 | noise | 582 / +24 (late 125 / -66) | +29.8 |

## Candidates (robust / promising)

- MGC 5m slow 20: window 0 → +84, z +1.3, thirds +20 / +39 / +25 (promising)
