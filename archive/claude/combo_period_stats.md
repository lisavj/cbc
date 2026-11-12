# Overall performance by period — TP rule, SL rule, both — MES 3m and MGC 3m — 11/08/2026

Same replay as combo_study.py (Jan 5 → Nov 6, live exits). Gross = points before costs; after costs = minus round-trip commission + 1 tick slippage per trade (MES 0.50, MGC 0.22 pts) and 1 more tick per rule exit at the candle close. Max drawdown = largest peak-to-trough drop in cumulative points within the period. Script: perf3.py.

## MES 3m

**Third 1 (01/05–04/17) — gross**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 517 | +236 | +0.46 | 52 % | 1.16 | 135 |
| TP rule alone: TP1 -> 85 % after 18 min | 535 | +319 | +0.60 | 55 % | 1.21 | 106 |
| SL rule alone: half SL1 if negative at 18 min | 523 | +278 | +0.53 | 51 % | 1.19 | 120 |
| Both rules | 541 | +367 | +0.68 | 53 % | 1.26 | 98 |

**Third 1 (01/05–04/17) — after costs**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 517 | -23 | -0.04 | 51 % | 0.99 | 222 |
| TP rule alone: TP1 -> 85 % after 18 min | 535 | +51 | +0.10 | 53 % | 1.03 | 160 |
| SL rule alone: half SL1 if negative at 18 min | 523 | +12 | +0.02 | 50 % | 1.01 | 210 |
| Both rules | 541 | +91 | +0.17 | 52 % | 1.06 | 150 |

**Third 2 (04/17–07/28) — gross**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 563 | -433 | -0.77 | 43 % | 0.76 | 549 |
| TP rule alone: TP1 -> 85 % after 18 min | 586 | -340 | -0.58 | 46 % | 0.81 | 479 |
| SL rule alone: half SL1 if negative at 18 min | 573 | -369 | -0.64 | 41 % | 0.78 | 494 |
| Both rules | 597 | -310 | -0.52 | 43 % | 0.82 | 451 |

**Third 2 (04/17–07/28) — after costs**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 563 | -714 | -1.27 | 42 % | 0.63 | 808 |
| TP rule alone: TP1 -> 85 % after 18 min | 586 | -633 | -1.08 | 45 % | 0.67 | 722 |
| SL rule alone: half SL1 if negative at 18 min | 573 | -662 | -1.15 | 40 % | 0.64 | 747 |
| Both rules | 597 | -615 | -1.03 | 42 % | 0.67 | 696 |

**Third 3 (07/28–11/06) — gross**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 620 | +216 | +0.35 | 52 % | 1.15 | 215 |
| TP rule alone: TP1 -> 85 % after 18 min | 649 | +255 | +0.39 | 54 % | 1.17 | 180 |
| SL rule alone: half SL1 if negative at 18 min | 635 | +223 | +0.35 | 49 % | 1.16 | 179 |
| Both rules | 662 | +237 | +0.36 | 51 % | 1.17 | 151 |

**Third 3 (07/28–11/06) — after costs**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 620 | -94 | -0.15 | 51 % | 0.94 | 344 |
| TP rule alone: TP1 -> 85 % after 18 min | 649 | -70 | -0.11 | 53 % | 0.96 | 298 |
| SL rule alone: half SL1 if negative at 18 min | 635 | -101 | -0.16 | 48 % | 0.94 | 332 |
| Both rules | 662 | -101 | -0.15 | 50 % | 0.94 | 288 |

**Last 4 weeks (10/09–11/06) — gross**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 149 | +250 | +1.68 | 59 % | 1.66 | 60 |
| TP rule alone: TP1 -> 85 % after 18 min | 159 | +230 | +1.45 | 60 % | 1.58 | 75 |
| SL rule alone: half SL1 if negative at 18 min | 152 | +218 | +1.43 | 55 % | 1.57 | 51 |
| Both rules | 162 | +175 | +1.08 | 54 % | 1.43 | 80 |

**Last 4 weeks (10/09–11/06) — after costs**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 149 | +176 | +1.18 | 59 % | 1.43 | 80 |
| TP rule alone: TP1 -> 85 % after 18 min | 159 | +150 | +0.95 | 60 % | 1.35 | 96 |
| SL rule alone: half SL1 if negative at 18 min | 152 | +140 | +0.92 | 55 % | 1.33 | 72 |
| Both rules | 162 | +93 | +0.57 | 54 % | 1.21 | 103 |

**Whole period — gross**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 1700 | +19 | +0.01 | 49 % | 1.00 | 641 |
| TP rule alone: TP1 -> 85 % after 18 min | 1770 | +233 | +0.13 | 52 % | 1.05 | 546 |
| SL rule alone: half SL1 if negative at 18 min | 1731 | +133 | +0.08 | 47 % | 1.03 | 550 |
| Both rules | 1800 | +294 | +0.16 | 49 % | 1.07 | 486 |

**Whole period — after costs**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 1700 | -831 | -0.49 | 48 % | 0.84 | 1088 |
| TP rule alone: TP1 -> 85 % after 18 min | 1770 | -652 | -0.37 | 51 % | 0.87 | 932 |
| SL rule alone: half SL1 if negative at 18 min | 1731 | -751 | -0.43 | 46 % | 0.85 | 982 |
| Both rules | 1800 | -626 | -0.35 | 48 % | 0.87 | 897 |


## MGC 3m

**Third 1 (01/05–04/17) — gross**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 596 | +68 | +0.11 | 52 % | 1.04 | 145 |
| TP rule alone: TP1 -> 65 % after 21 min | 604 | +97 | +0.16 | 53 % | 1.06 | 137 |
| SL rule alone: cut if < 25 % of TP1 at 18 min | 609 | +117 | +0.19 | 51 % | 1.08 | 92 |
| Both rules | 610 | +143 | +0.23 | 52 % | 1.10 | 92 |

**Third 1 (01/05–04/17) — after costs**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 596 | -63 | -0.11 | 51 % | 0.96 | 170 |
| TP rule alone: TP1 -> 65 % after 21 min | 604 | -36 | -0.06 | 52 % | 0.98 | 160 |
| SL rule alone: cut if < 25 % of TP1 at 18 min | 609 | -27 | -0.04 | 49 % | 0.98 | 121 |
| Both rules | 610 | -1 | -0.00 | 50 % | 1.00 | 124 |

**Third 2 (04/17–07/28) — gross**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 551 | +124 | +0.23 | 50 % | 1.09 | 65 |
| TP rule alone: TP1 -> 65 % after 21 min | 566 | +121 | +0.21 | 52 % | 1.09 | 65 |
| SL rule alone: cut if < 25 % of TP1 at 18 min | 571 | +130 | +0.23 | 48 % | 1.11 | 56 |
| Both rules | 576 | +145 | +0.25 | 49 % | 1.13 | 59 |

**Third 2 (04/17–07/28) — after costs**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 551 | +3 | +0.01 | 50 % | 1.00 | 111 |
| TP rule alone: TP1 -> 65 % after 21 min | 566 | -3 | -0.01 | 51 % | 1.00 | 115 |
| SL rule alone: cut if < 25 % of TP1 at 18 min | 571 | -8 | -0.01 | 47 % | 0.99 | 88 |
| Both rules | 576 | +5 | +0.01 | 48 % | 1.00 | 74 |

**Third 3 (07/28–11/06) — gross**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 558 | +45 | +0.08 | 48 % | 1.03 | 116 |
| TP rule alone: TP1 -> 65 % after 21 min | 575 | +26 | +0.04 | 50 % | 1.02 | 122 |
| SL rule alone: cut if < 25 % of TP1 at 18 min | 576 | +114 | +0.20 | 48 % | 1.10 | 78 |
| Both rules | 583 | +94 | +0.16 | 49 % | 1.08 | 69 |

**Third 3 (07/28–11/06) — after costs**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 558 | -77 | -0.14 | 47 % | 0.94 | 169 |
| TP rule alone: TP1 -> 65 % after 21 min | 575 | -101 | -0.18 | 50 % | 0.93 | 187 |
| SL rule alone: cut if < 25 % of TP1 at 18 min | 576 | -25 | -0.04 | 45 % | 0.98 | 125 |
| Both rules | 583 | -46 | -0.08 | 46 % | 0.96 | 137 |

**Last 4 weeks (10/09–11/06) — gross**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 154 | +64 | +0.42 | 49 % | 1.19 | 54 |
| TP rule alone: TP1 -> 65 % after 21 min | 159 | +54 | +0.34 | 51 % | 1.16 | 63 |
| SL rule alone: cut if < 25 % of TP1 at 18 min | 161 | +79 | +0.49 | 50 % | 1.28 | 51 |
| Both rules | 164 | +77 | +0.47 | 51 % | 1.27 | 48 |

**Last 4 weeks (10/09–11/06) — after costs**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 154 | +30 | +0.20 | 49 % | 1.09 | 67 |
| TP rule alone: TP1 -> 65 % after 21 min | 159 | +19 | +0.12 | 51 % | 1.05 | 76 |
| SL rule alone: cut if < 25 % of TP1 at 18 min | 161 | +41 | +0.25 | 47 % | 1.13 | 66 |
| Both rules | 164 | +37 | +0.23 | 48 % | 1.12 | 63 |

**Whole period — gross**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 1705 | +237 | +0.14 | 50 % | 1.06 | 145 |
| TP rule alone: TP1 -> 65 % after 21 min | 1745 | +244 | +0.14 | 52 % | 1.06 | 145 |
| SL rule alone: cut if < 25 % of TP1 at 18 min | 1756 | +361 | +0.21 | 49 % | 1.10 | 106 |
| Both rules | 1769 | +382 | +0.22 | 50 % | 1.10 | 113 |

**Whole period — after costs**

| Exits | Trades | Net pts | Avg / trade | Win % | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| Current exits | 1705 | -138 | -0.08 | 49 % | 0.97 | 285 |
| TP rule alone: TP1 -> 65 % after 21 min | 1745 | -140 | -0.08 | 51 % | 0.97 | 313 |
| SL rule alone: cut if < 25 % of TP1 at 18 min | 1756 | -60 | -0.03 | 47 % | 0.99 | 237 |
| Both rules | 1769 | -42 | -0.02 | 48 % | 0.99 | 244 |

