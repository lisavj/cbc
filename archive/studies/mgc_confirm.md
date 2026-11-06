# MGC 5m-confirmation backtest — Thu 11/05/2026 09:10

5m-confirmation backtest (MGC) -- 11/05/2026.
Question (from the live 10/19-11/05 combo check): are MGC 2m / 3m setups better when a MGC 5m setup agrees -- a same-direction
5m setup is open at the setup's entry candle close, or a 5m setup in the same direction started within 10 min before / after?
Also: 5m setups confirmed by 2m / 3m.
Replay (late_study LCase = chop_sim rules, LTF late window 1, NY OR block 30 min, toward flips strict), each chart on its live
settings: MGC 3m 9 / 20, range gate 24 / 5 ATR, exits SL 3 / TP1 2.0 / time-of-day close (v10.70); MGC 2m slow 14, 1H MTF gate,
base exits (HTF flip counter not modelled); MGC 5m 9 / 20, no gates, base exits. 3m / 5m Jan 5 -> now, 2m Jun 1 -> now.
Thirds = equal time over each pair's common period. z = (confirmed avg - all avg) / (SD / sqrt(confirmed n)) style test via the
excluded setups: z = (net(confirmed) - net(all) * share) ... see code. Robust = z >= 2 and confirmed avg > unconfirmed avg in all
three thirds; promising = z >= 1 and all three.
Usage: python3 confirm5_study.py   (needs chop_sim.py, mes3_ema_grid.py, late_study.py next to it)

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

