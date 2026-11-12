# CBC room-to-first-level check -- 2026-11-12 09:46 ET (manual re-run for the failed 11/11 run)

Settings: settings_sync_report (11/12 09:45 ET re-run) = 0 MISMATCH (1 known), live CBC v10.87. Data: tv-webhook-dashboard alerts, 3m setups matched to "Setup Ended" results. Room line present on 67 setups; rebuild matched it on 66. Note: this run fired at 09:45 ET (not after the close), so 11/12 is partial. Fresh data pull at 09:46 gave results identical to the 09:45 run.

## Verdicts
- **MES 3m: candidate, waiting for out-of-sample (2 blocked, -7.6).** Gate "room x TP1 < 0.2": 35 blocked, -52.6 (avg -1.50); halves -19.0 / -33.7; thirds -16.1 / -23.0 / -13.5; kept avg +0.50 vs -0.16 all. Rules (a)-(c) pass (also at 0.15 / 0.25 / 0.5); (d) needs 8+ out-of-sample blocked -- still only 4 MES 3m setups since 11/06 12:00 ET (2 blocked at 0.2).
- **MGC 3m: keep off.** At 0.2: 31 blocked, +1.0 (halves +0.7 / +0.3, thirds +0.6 / -14.3 / +14.8); kept avg -0.47 < all -0.26. Out-of-sample: 3 blocked, +4.3. No threshold passes.
- Gate live? Can't tell -- too few MES 3m setups (11/08 2 with 2 below 0.2, i.e. not live then; 11/12 1 with 0). Not 3+ setups/day on any recent day.
- **MES 3m data gap:** the MES 3m chart sent no alerts at all on 11/10 and 11/11 (MGC 3m sent 300+ per day); 11/09 had 1 setup, 11/12 so far 1. Only one new MES 3m setup with a result since the last run (11/12 09:30, -18.7), which moved MES 3m net from +1.8 to -16.9. Out-of-sample will stay thin until MES 3m alerts flow normally -- check the MES 3m TradingView alert if this wasn't intentional.
- Baseline unchanged vs 11/09 for the pre-11/09 setups (same 35 blocked / -52.6), so no effect from the 11/08 script sync here.

## MES 3m -- 106 setups (10/19 05:54 -> 11/12 09:30), win 46 %, net -16.9, avg -0.16; Room line on 36
Halves: 53 -34.1 / 53 +17.2; thirds: 35 -39.7 / 35 -27.0 / 36 +49.8

| room pts | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.5 | 19 | 42 | -19.0 | -1.00 |
| 0.5-1 | 9 | 33 | -28.2 | -3.13 |
| 1-2 | 28 | 64 | +52.9 | +1.89 |
| 2-3 | 14 | 29 | -28.5 | -2.04 |
| 3-5 | 22 | 45 | -8.4 | -0.38 |
| 5-8 | 7 | 14 | -44.3 | -6.32 |
| 8-+ | 7 | 71 | +58.6 | +8.37 |

| room x TP1 | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.1 | 23 | 43 | -20.2 | -0.88 |
| 0.1-0.2 | 12 | 33 | -32.5 | -2.70 |
| 0.2-0.3 | 15 | 67 | +31.3 | +2.09 |
| 0.3-0.5 | 21 | 33 | -40.7 | -1.94 |
| 0.5-1 | 26 | 50 | +13.2 | +0.51 |
| 1-+ | 9 | 56 | +31.9 | +3.54 |

**MES 3m all setups** (106 setups, net -16.9, avg -0.16)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 23 | -20.2 | -0.88 | -7.1 / -13.1 | -10.0 / -17.2 / +7.1 | +0.04 |
| room x TP1 < 0.15 | 31 | -43.4 | -1.40 | -18.2 / -25.2 | -15.3 / -23.0 / -5.0 | +0.35 |
| room x TP1 < 0.2 | 35 | -52.6 | -1.50 | -19.0 / -33.7 | -16.1 / -23.0 / -13.5 | +0.50 |
| room x TP1 < 0.25 | 40 | -28.4 | -0.71 | -1.2 / -27.2 | -2.7 / -16.9 / -8.8 | +0.17 |
| room x TP1 < 0.3 | 50 | -21.3 | -0.43 | -2.8 / -18.4 | -11.0 / -13.1 / +2.8 | +0.08 |
| room x TP1 < 0.5 | 71 | -62.0 | -0.87 | -35.2 / -26.8 | -37.3 / -20.4 / -4.3 | +1.29 |
| room < 0.5 pts | 19 | -19.0 | -1.00 | -7.1 / -11.9 | -10.0 / -18.1 / +9.1 | +0.02 |
| room < 1 pts | 28 | -47.2 | -1.68 | -15.0 / -32.2 | -12.1 / -23.0 / -12.0 | +0.39 |
| room < 2 pts | 56 | +5.7 | +0.10 | -0.8 / +6.5 | -12.6 / -2.7 / +21.0 | -0.45 |

**MES 3m bot set** (31 setups, net +25.7, avg +0.83)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 9 | +8.2 | +0.91 | -3.5 / +11.7 | -3.5 / +1.7 / +10.1 | +0.80 |
| room x TP1 < 0.15 | 11 | -16.3 | -1.48 | -3.5 / -12.8 | -3.5 / +1.7 / -14.4 | +2.10 |
| room x TP1 < 0.2 | 11 | -16.3 | -1.48 | -3.5 / -12.8 | -3.5 / +1.7 / -14.4 | +2.10 |
| room x TP1 < 0.25 | 14 | -5.4 | -0.39 | +0.9 / -6.3 | -3.5 / +7.8 / -9.7 | +1.83 |
| room x TP1 < 0.3 | 17 | -12.8 | -0.75 | -3.3 / -9.5 | -3.5 / -4.4 / -4.9 | +2.75 |
| room x TP1 < 0.5 | 22 | -3.8 | -0.17 | -4.0 / +0.2 | -7.9 / -0.7 / +4.8 | +3.28 |
| room < 0.5 pts | 8 | +2.9 | +0.36 | -3.5 / +6.5 | -3.5 / +1.7 / +4.8 | +0.99 |
| room < 1 pts | 9 | -7.3 | -0.81 | -3.5 / -3.8 | -3.5 / +1.7 / -5.4 | +1.50 |
| room < 2 pts | 18 | +11.5 | +0.64 | +6.8 / +4.8 | +2.8 / -0.7 / +9.4 | +1.09 |

**MES 3m out-of-sample (from 11/06 12:00 ET)** (4 setups, net -29.8, avg -7.45)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 0 | +0.0 | +0.00 | +0.0 / +0.0 | +0.0 / +0.0 / +0.0 | -7.45 |
| room x TP1 < 0.15 | 2 | -7.6 | -3.80 | +11.4 / -19.0 | +0.0 / +11.4 / -19.0 | -11.10 |
| room x TP1 < 0.2 | 2 | -7.6 | -3.80 | +11.4 / -19.0 | +0.0 / +11.4 / -19.0 | -11.10 |
| room x TP1 < 0.25 | 2 | -7.6 | -3.80 | +11.4 / -19.0 | +0.0 / +11.4 / -19.0 | -11.10 |
| room x TP1 < 0.3 | 2 | -7.6 | -3.80 | +11.4 / -19.0 | +0.0 / +11.4 / -19.0 | -11.10 |
| room x TP1 < 0.5 | 3 | -11.1 | -3.70 | +7.9 / -19.0 | -3.5 / +11.4 / -19.0 | -18.70 |
| room < 0.5 pts | 0 | +0.0 | +0.00 | +0.0 / +0.0 | +0.0 / +0.0 / +0.0 | -7.45 |
| room < 1 pts | 0 | +0.0 | +0.00 | +0.0 / +0.0 | +0.0 / +0.0 / +0.0 | -7.45 |
| room < 2 pts | 2 | -7.6 | -3.80 | +11.4 / -19.0 | +0.0 / +11.4 / -19.0 | -11.10 |

Per day (setups / room x TP1 < 0.2 by Room line), last 6: 11/03 8/4, 11/04 2/2, 11/05 5/3, 11/06 3/0, 11/08 2/2, 11/12 1/0

## MGC 3m -- 75 setups (10/19 03:42 -> 11/11 06:15), win 44 %, net -19.5, avg -0.26; Room line on 31
Halves: 37 -14.8 / 38 -4.6; thirds: 25 +4.6 / 25 -47.5 / 25 +23.5

| room pts | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.5 | 16 | 38 | -15.0 | -0.94 |
| 0.5-1 | 15 | 47 | +11.9 | +0.80 |
| 1-2 | 16 | 31 | -23.4 | -1.46 |
| 2-3 | 9 | 56 | +8.2 | +0.92 |
| 3-5 | 9 | 44 | -10.3 | -1.14 |
| 5-8 | 8 | 50 | -2.8 | -0.35 |
| 8-+ | 2 | 100 | +11.8 | +5.89 |

| room x TP1 | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.1 | 17 | 35 | -5.4 | -0.32 |
| 0.1-0.2 | 14 | 50 | +6.4 | +0.46 |
| 0.2-0.3 | 11 | 36 | -14.7 | -1.33 |
| 0.3-0.5 | 14 | 43 | -4.6 | -0.33 |
| 0.5-1 | 9 | 56 | +2.7 | +0.30 |
| 1-+ | 10 | 50 | -4.0 | -0.40 |

**MGC 3m all setups** (75 setups, net -19.5, avg -0.26)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 17 | -5.4 | -0.32 | +3.6 / -9.1 | +6.6 / -15.8 / +3.7 | -0.24 |
| room x TP1 < 0.15 | 27 | -3.0 | -0.11 | -2.4 / -0.6 | +0.6 / -17.4 / +13.8 | -0.34 |
| room x TP1 < 0.2 | 31 | +1.0 | +0.03 | +0.7 / +0.3 | +0.6 / -14.3 / +14.8 | -0.47 |
| room x TP1 < 0.25 | 35 | +4.1 | +0.12 | -5.0 / +9.1 | +0.6 / -15.1 / +18.7 | -0.59 |
| room x TP1 < 0.3 | 42 | -13.6 | -0.32 | -4.6 / -9.0 | +0.9 / -28.7 / +14.2 | -0.18 |
| room x TP1 < 0.5 | 56 | -18.2 | -0.32 | -0.6 / -17.6 | +4.9 / -37.2 / +14.2 | -0.07 |
| room < 0.5 pts | 16 | -15.0 | -0.94 | +4.8 / -19.8 | +6.6 / -14.6 / -7.0 | -0.08 |
| room < 1 pts | 31 | -3.0 | -0.10 | -1.4 / -1.7 | +0.6 / -16.4 / +12.8 | -0.37 |
| room < 2 pts | 47 | -26.4 | -0.56 | -14.3 / -12.2 | -8.8 / -28.7 / +11.0 | +0.25 |

**MGC 3m bot set** (24 setups, net -16.5, avg -0.69)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 7 | -19.2 | -2.74 | -1.1 / -18.1 | +0.9 / -8.4 / -11.7 | +0.16 |
| room x TP1 < 0.15 | 9 | -12.0 | -1.33 | +1.4 / -13.4 | +3.4 / -3.7 / -11.7 | -0.30 |
| room x TP1 < 0.2 | 13 | -7.9 | -0.61 | +4.6 / -12.5 | +3.4 / -0.6 / -10.8 | -0.78 |
| room x TP1 < 0.25 | 14 | -11.6 | -0.83 | +0.9 / -12.5 | +3.4 / -4.2 / -10.8 | -0.49 |
| room x TP1 < 0.3 | 16 | -17.7 | -1.10 | -5.2 / -12.5 | -2.7 / -4.2 / -10.8 | +0.14 |
| room x TP1 < 0.5 | 19 | -13.9 | -0.73 | -5.2 / -8.7 | -2.7 / -7.7 / -3.5 | -0.53 |
| room < 0.5 pts | 8 | -14.5 | -1.82 | -1.1 / -13.4 | +0.9 / -3.7 / -11.7 | -0.12 |
| room < 1 pts | 11 | -13.8 | -1.26 | +4.6 / -18.4 | +3.4 / -0.6 / -16.7 | -0.21 |
| room < 2 pts | 16 | -17.7 | -1.10 | -5.2 / -12.5 | -2.7 / -4.2 / -10.8 | +0.14 |

**MGC 3m out-of-sample (from 11/06 12:00 ET)** (10 setups, net +14.5, avg +1.45)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 2 | +9.3 | +4.63 | +9.3 / +0.0 | +0.0 / +9.3 / +0.0 | +0.65 |
| room x TP1 < 0.15 | 2 | +9.3 | +4.63 | +9.3 / +0.0 | +0.0 / +9.3 / +0.0 | +0.65 |
| room x TP1 < 0.2 | 3 | +4.3 | +1.42 | +9.3 / -5.0 | +0.0 / +9.3 / -5.0 | +1.46 |
| room x TP1 < 0.25 | 4 | +8.2 | +2.05 | +9.3 / -1.1 | +0.0 / +9.3 / -1.1 | +1.05 |
| room x TP1 < 0.3 | 4 | +8.2 | +2.05 | +9.3 / -1.1 | +0.0 / +9.3 / -1.1 | +1.05 |
| room x TP1 < 0.5 | 7 | +9.9 | +1.42 | +9.0 / +0.9 | -0.3 / +11.3 / -1.1 | +1.52 |
| room < 0.5 pts | 1 | -6.2 | -6.18 | -6.2 / +0.0 | +0.0 / -6.2 / +0.0 | +2.30 |
| room < 1 pts | 4 | +8.2 | +2.05 | +9.3 / -1.1 | +0.0 / +9.3 / -1.1 | +1.05 |
| room < 2 pts | 5 | +11.7 | +2.34 | +12.8 / -1.1 | +3.5 / +9.3 / -1.1 | +0.55 |

Per day (setups / room x TP1 < 0.2 by Room line), last 6: 11/05 4/2, 11/06 6/2, 11/08 3/2, 11/09 2/0, 11/10 1/0, 11/11 2/1

## History
| run | MES 3m blocked / net at 0.2 x TP1 | out-of-sample blocked / net | verdict |
|---|---|---|---|
| 2026-11-12 09:46 ET (re-run of failed 11/11) | 35 / -52.6 | 2 / -7.6 | MES 3m candidate, waiting for OOS (MES 3m alerts silent 11/10-11/11); MGC 3m keep off |
| 2026-11-09 17:48 ET | 35 / -52.6 | 2 / -7.6 | MES 3m candidate, waiting for OOS; MGC 3m keep off |
| 2026-11-06 (baseline study) | 32 / -53.1 | -- | MES 3m candidate; MGC 3m keep off |
