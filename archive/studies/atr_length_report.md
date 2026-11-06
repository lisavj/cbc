# ATR length study — Thu 11/05/2026 13:10

ATR length study, MES 3m and MGC 3m -- 11/05/2026.
CBC "ATR length" (Auto Trade Setup, default 14) sizes SL1 / TP1 / trail and the ATR-based gates (range gate width, flip
distance 2 ATR, VWAP stretch). Tested lengths 5 / 7 / 10 / 14 / 20 / 30 / 50, two ways: (1) EXITS only (gates keep ATR 14),
(2) ALL (exits + gates). Replay (chop_sim rules, late window 1, NY OR block 30) on live settings: MES 3m 9 / 20, range gate,
SL1 3 x ATR min 5 / TP1 2 x ATR / time-of-day close; MGC 3m range gate + VWAP stretch 4 ATR, SL1 1.7 ATR min 5 cap 7 /
TP1 1.7 ATR cap 6 / 80 % + BE + trail 1.7. Jan 5 -> now. z / robust / promising as in the other studies.

## MES 3m — current ATR 14: 1662 setups, net -53

| ATR length | Applied to | Setups | Win % | Net | Δ vs 14 | z | Δ by third | Verdict | Last 4 wk Δ | Median SL1 / TP1 (pts) |
|---|---|---|---|---|---|---|---|---|---|---|
| 5 | exits | 1667 | 46% | -76 | -23 | -0.5 | -39 / +45 / -29 | worse | -23.6 | 9.0 / 6.0 |
| 7 | exits | 1665 | 46% | -113 | -60 | -1.4 | -58 / +44 / -46 | worse | -15.0 | 9.0 / 6.0 |
| 10 | exits | 1663 | 46% | -68 | -15 | -0.5 | -48 / +48 / -16 | worse | -4.5 | 8.9 / 5.9 |
| 14 (current) | exits | 1662 | 46% | -53 | +0 | +0.0 | +0 / +0 / +0 | baseline | +0.0 | 8.9 / 5.9 |
| 20 | exits | 1660 | 46% | -94 | -41 | -1.5 | -10 / +44 / -75 | worse | -36.8 | 9.0 / 6.0 |
| 30 | exits | 1657 | 45% | -120 | -67 | -1.3 | +11 / +48 / -126 | worse | -58.5 | 9.1 / 6.1 |
| 50 | exits | 1655 | 45% | -34 | +19 | +0.3 | +13 / +84 / -78 | noise | -50.8 | 9.2 / 6.1 |
| 5 | exits + gates | 1661 | 46% | -21 | +32 | +0.3 | -48 / +113 / -34 | noise | -26.3 | 8.9 / 5.9 |
| 7 | exits + gates | 1662 | 46% | -17 | +36 | +0.4 | -36 / +149 / -77 | noise | -28.7 | 8.9 / 5.9 |
| 10 | exits + gates | 1666 | 46% | -26 | +27 | +0.5 | -53 / +114 / -34 | noise | -18.4 | 8.9 / 5.9 |
| 20 | exits + gates | 1666 | 46% | -117 | -64 | -1.1 | -25 / +43 / -82 | worse | -42.2 | 9.0 / 6.0 |
| 30 | exits + gates | 1665 | 45% | -141 | -88 | -1.0 | -6 / +53 / -135 | worse | -64.2 | 9.1 / 6.1 |
| 50 | exits + gates | 1662 | 46% | +47 | +100 | +0.9 | +33 / +120 / -53 | noise | -52.2 | 9.2 / 6.1 |

## MGC 3m — current ATR 14: 1693 setups, net +223

| ATR length | Applied to | Setups | Win % | Net | Δ vs 14 | z | Δ by third | Verdict | Last 4 wk Δ | Median SL1 / TP1 (pts) |
|---|---|---|---|---|---|---|---|---|---|---|
| 5 | exits | 1679 | 50% | +195 | -28 | -0.8 | +10 / -0 / -38 | worse | -6.9 | 6.9 / 6.0 |
| 7 | exits | 1682 | 50% | +203 | -20 | -0.7 | +4 / +2 / -25 | worse | +7.6 | 7.0 / 6.0 |
| 10 | exits | 1688 | 50% | +247 | +24 | +1.2 | +5 / +22 / -3 | noise | +2.3 | 6.9 / 6.0 |
| 14 (current) | exits | 1693 | 50% | +223 | +0 | +0.0 | +0 / +0 / +0 | baseline | +0.0 | 6.9 / 6.0 |
| 20 | exits | 1694 | 50% | +195 | -28 | -1.7 | -2 / -13 / -13 | worse | -12.5 | 6.9 / 6.0 |
| 30 | exits | 1695 | 50% | +196 | -27 | -1.1 | +3 / -36 / +7 | worse | -11.9 | 6.9 / 6.0 |
| 50 | exits | 1693 | 49% | +38 | -185 | -5.4 | -18 / -86 / -81 | worse | -21.2 | 6.9 / 6.0 |
| 5 | exits + gates | 1683 | 50% | +267 | +44 | +0.6 | +54 / +9 / -19 | noise | -2.2 | 6.8 / 6.0 |
| 7 | exits + gates | 1684 | 50% | +206 | -17 | -0.3 | +12 / -13 / -16 | worse | +6.8 | 7.0 / 6.0 |
| 10 | exits + gates | 1690 | 50% | +241 | +18 | +0.4 | +20 / +3 / -4 | noise | +0.5 | 6.9 / 6.0 |
| 20 | exits + gates | 1688 | 50% | +199 | -24 | -0.6 | -11 / -3 / -11 | worse | -8.8 | 6.9 / 6.0 |
| 30 | exits + gates | 1682 | 49% | +201 | -22 | -0.4 | -2 / -24 / +4 | worse | -15.8 | 6.9 / 6.0 |
| 50 | exits + gates | 1674 | 49% | +102 | -121 | -1.7 | -20 / -59 / -42 | worse | -47.0 | 6.9 / 6.0 |

## Candidates

- none
