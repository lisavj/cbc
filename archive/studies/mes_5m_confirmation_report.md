# MES 5m-confirmation backtest — Thu 11/05/2026 09:04

5m-confirmation backtest (MES) -- 11/05/2026.
Question (from the live 10/19-11/05 combo check): are MES 2m / 3m setups better when a MES 5m setup agrees -- a same-direction
5m setup is open at the setup's entry candle close, or a 5m setup in the same direction started within 10 min before / after?
Also: 5m setups confirmed by 2m / 3m.
Replay (late_study LCase = chop_sim rules, LTF late window 1, NY OR block 30 min, toward flips strict), each chart on its live
settings: MES 3m 9 / 20, range gate 24 / 5 ATR, exits SL 3 / TP1 2.0 / time-of-day close (v10.70); MES 2m slow 14, 1H MTF gate,
base exits (HTF flip counter not modelled); MES 5m 9 / 20, no gates, base exits. 3m / 5m Jan 5 -> now, 2m Jun 1 -> now.
Thirds = equal time over each pair's common period. z = (confirmed avg - all avg) / (SD / sqrt(confirmed n)) style test via the
excluded setups: z = (net(confirmed) - net(all) * share) ... see code. Robust = z >= 2 and confirmed avg > unconfirmed avg in all
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
