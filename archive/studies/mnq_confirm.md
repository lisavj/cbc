# MNQ 5m-confirmation backtest — Thu 11/05/2026 09:10

5m-confirmation backtest (MNQ) -- 11/05/2026.
Question (from the live 10/19-11/05 combo check): are MNQ 2m / 3m setups better when a MNQ 5m setup agrees -- a same-direction
5m setup is open at the setup's entry candle close, or a 5m setup in the same direction started within 10 min before / after?
Also: 5m setups confirmed by 2m / 3m.
Replay (late_study LCase = chop_sim rules, LTF late window 1, NY OR block 30 min, toward flips strict), each chart on its live
settings: MNQ 3m 9 / 20, range gate 24 / 5 ATR, exits SL 3 / TP1 2.0 / time-of-day close (v10.70); MNQ 2m slow 14, 1H MTF gate,
base exits (HTF flip counter not modelled); MNQ 5m 9 / 20, no gates, base exits. 3m / 5m Jan 5 -> now, 2m Jun 1 -> now.
Thirds = equal time over each pair's common period. z = (confirmed avg - all avg) / (SD / sqrt(confirmed n)) style test via the
excluded setups: z = (net(confirmed) - net(all) * share) ... see code. Robust = z >= 2 and confirmed avg > unconfirmed avg in all
three thirds; promising = z >= 1 and all three.
Usage: python3 confirm5_study.py   (needs chop_sim.py, mes3_ema_grid.py, late_study.py next to it)

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

