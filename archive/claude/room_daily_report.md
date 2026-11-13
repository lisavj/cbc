# CBC room-to-first-level check -- 2026-11-12 17:48 ET

Settings: settings_sync_report (11/12 16:47 ET) = 0 MISMATCH (1 known); newest Pine v10.93 (v10.88-v10.93 are ▶ Bot changes only -- chart setups and their "Setup Ended" results unaffected). Data: tv-webhook-dashboard alerts (45,409 stored, not yet de-duplicated), 3m setups matched to "Setup Ended" results; duplicate setups collapsed by (time, direction, entry). Room line present on 68 setups; rebuild matched it on 67.

## Verdicts
- **MES 3m: candidate, waiting for out-of-sample (3 blocked, -2.4).** Gate "room x TP1 < 0.2": 36 blocked, -47.4 (avg -1.32); halves -19.0 / -28.4; thirds -16.1 / -23.0 / -8.2; kept avg +0.50 vs -0.11 all. Rules (a)-(c) pass at 0.2 and 0.25 (0.15 now fails: last third +0.2). (d) needs 8+ out-of-sample blocked -- only 5 MES 3m setups since 11/06 12:00 ET.
- **MGC 3m: keep off.** At 0.2: 31 blocked, +13.5 (halves +0.7 / +12.8, thirds +0.6 / -14.3 / +27.2); kept avg -0.49 < all -0.11. Out-of-sample: 3 blocked, +16.7. No threshold passes.
- Gate live? No -- 11/12 MES 3m had 2 setups, 1 with room x TP1 < 0.2 (11/12 10:03, room < 0.1, +5.2); 11/08 2/2. Never 3+ setups/day recently.
- **MES 3m still thin:** only 2 MES 3m setups with a result on 11/12 and none on 11/09-11/11 (see the 11/12 09:46 note about the MES 3m chart being silent 11/10-11/11). One new setup since the morning run (+5.2, blocked at 0.2), which moved MES 3m blocked net from -52.6 to -47.4.
- **MGC 3m numbers changed vs the morning run, not the market:** 3 MGC 3m setups (11/09-11/11) had two different "Setup Ended" results from the duplicate old-exit alert (data note 2); this run uses the 0.5×(TP1) result as the data notes say, which moved MGC 3m net -19.5 -> -7.9 and the 0.2 gate +1.0 -> +13.5. MGC 3m live results 11/09-11/12 are partly on the old exits. No MGC 3m setups with a result on 11/12.

## MES 3m -- 107 setups (10/19 05:54 -> 11/12 10:03), win 46 %, net -11.6, avg -0.11; Room line on 37; multi-result 0
Halves: 53 -34.1 / 54 +22.5; thirds: 35 -39.7 / 36 -18.0 / 36 +46.0

| room pts | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.5 | 20 | 45 | -13.7 | -0.69 |
| 0.5-1 | 9 | 33 | -28.2 | -3.13 |
| 1-2 | 28 | 64 | +52.9 | +1.89 |
| 2-3 | 14 | 28 | -28.5 | -2.04 |
| 3-5 | 22 | 45 | -8.4 | -0.38 |
| 5-8 | 7 | 14 | -44.3 | -6.32 |
| 8-+ | 7 | 71 | +58.6 | +8.37 |

| room x TP1 | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.1 | 24 | 45 | -14.9 | -0.62 |
| 0.1-0.2 | 12 | 33 | -32.5 | -2.70 |
| 0.2-0.3 | 15 | 66 | +31.3 | +2.09 |
| 0.3-0.5 | 21 | 33 | -40.7 | -1.94 |
| 0.5-1 | 26 | 50 | +13.2 | +0.51 |
| 1-+ | 9 | 55 | +31.9 | +3.54 |

**MES 3m all setups** (107 setups, net -11.6, avg -0.11)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 24 | -14.9 | -0.62 | -7.1 / -7.8 | -10.0 / -17.2 / +12.4 | +0.04 |
| room x TP1 < 0.15 | 32 | -38.1 | -1.19 | -18.2 / -19.9 | -15.3 / -23.0 / +0.2 | +0.35 |
| room x TP1 < 0.2 | 36 | -47.4 | -1.32 | -19.0 / -28.4 | -16.1 / -23.0 / -8.2 | +0.50 |
| room x TP1 < 0.25 | 41 | -23.2 | -0.56 | -1.2 / -21.9 | -2.7 / -16.9 / -3.5 | +0.17 |
| room x TP1 < 0.3 | 51 | -16.0 | -0.31 | -2.8 / -13.2 | -11.0 / -13.1 / +8.0 | +0.08 |
| room x TP1 < 0.5 | 72 | -56.8 | -0.79 | -35.2 / -21.6 | -37.3 / -20.4 / +1.0 | +1.29 |
| room < 0.5 pts | 20 | -13.7 | -0.69 | -7.1 / -6.6 | -10.0 / -18.1 / +14.4 | +0.02 |
| room < 1 pts | 29 | -41.9 | -1.45 | -15.0 / -27.0 | -12.1 / -23.0 / -6.8 | +0.39 |
| room < 2 pts | 57 | +11.0 | +0.19 | -0.8 / +11.7 | -12.6 / -2.7 / +26.3 | -0.45 |

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

**MES 3m out-of-sample (from 11/06 12:00 ET)** (5 setups, net -24.6, avg -4.91)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 1 | +5.2 | +5.25 | +0.0 / +5.2 | +0.0 / +0.0 / +5.2 | -7.45 |
| room x TP1 < 0.15 | 3 | -2.4 | -0.79 | +11.4 / -13.8 | +0.0 / -7.6 / +5.2 | -11.10 |
| room x TP1 < 0.2 | 3 | -2.4 | -0.79 | +11.4 / -13.8 | +0.0 / -7.6 / +5.2 | -11.10 |
| room x TP1 < 0.25 | 3 | -2.4 | -0.79 | +11.4 / -13.8 | +0.0 / -7.6 / +5.2 | -11.10 |
| room x TP1 < 0.3 | 3 | -2.4 | -0.79 | +11.4 / -13.8 | +0.0 / -7.6 / +5.2 | -11.10 |
| room x TP1 < 0.5 | 4 | -5.9 | -1.46 | +7.9 / -13.8 | -3.5 / -7.6 / +5.2 | -18.70 |
| room < 0.5 pts | 1 | +5.2 | +5.25 | +0.0 / +5.2 | +0.0 / +0.0 / +5.2 | -7.45 |
| room < 1 pts | 1 | +5.2 | +5.25 | +0.0 / +5.2 | +0.0 / +0.0 / +5.2 | -7.45 |
| room < 2 pts | 3 | -2.4 | -0.79 | +11.4 / -13.8 | +0.0 / -7.6 / +5.2 | -11.10 |

Per day (setups with Room line / room x TP1 < 0.2), last 8: 11/1 1/1, 11/2 8/1, 11/3 8/4, 11/4 2/2, 11/5 5/3, 11/6 3/0, 11/8 2/2, 11/12 2/1
All setups per day, last 8: 11/1 1, 11/2 8, 11/3 8, 11/4 2, 11/5 5, 11/6 3, 11/8 2, 11/12 2

## MGC 3m -- 75 setups (10/19 03:42 -> 11/11 06:15), win 44 %, net -7.9, avg -0.11; Room line on 31; multi-result 3
Halves: 37 -14.8 / 38 +7.0; thirds: 25 +4.6 / 25 -47.5 / 25 +35.1

| room pts | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.5 | 16 | 37 | -15.0 | -0.94 |
| 0.5-1 | 15 | 46 | +22.7 | +1.51 |
| 1-2 | 16 | 31 | -23.4 | -1.46 |
| 2-3 | 9 | 55 | +8.2 | +0.92 |
| 3-5 | 9 | 44 | -9.4 | -1.05 |
| 5-8 | 8 | 50 | -2.8 | -0.35 |
| 8-+ | 2 | 100 | +11.8 | +5.89 |

| room x TP1 | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.1 | 17 | 35 | +7.0 | +0.41 |
| 0.1-0.2 | 14 | 50 | +6.4 | +0.46 |
| 0.2-0.3 | 11 | 36 | -16.4 | -1.49 |
| 0.3-0.5 | 14 | 42 | -4.6 | -0.33 |
| 0.5-1 | 9 | 55 | +3.6 | +0.40 |
| 1-+ | 10 | 50 | -4.0 | -0.40 |

**MGC 3m all setups** (75 setups, net -7.9, avg -0.11)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 17 | +7.0 | +0.41 | +3.6 / +3.4 | +6.6 / -15.8 / +16.2 | -0.26 |
| room x TP1 < 0.15 | 27 | +9.4 | +0.35 | -2.4 / +11.9 | +0.6 / -17.4 / +26.3 | -0.36 |
| room x TP1 < 0.2 | 31 | +13.5 | +0.44 | +0.7 / +12.8 | +0.6 / -14.3 / +27.2 | -0.49 |
| room x TP1 < 0.25 | 35 | +14.8 | +0.42 | -5.0 / +19.9 | +0.6 / -15.1 / +29.4 | -0.57 |
| room x TP1 < 0.3 | 42 | -2.9 | -0.07 | -4.6 / +1.7 | +0.9 / -28.7 / +24.9 | -0.15 |
| room x TP1 < 0.5 | 56 | -7.5 | -0.13 | -0.6 / -6.8 | +4.9 / -37.2 / +24.9 | -0.02 |
| room < 0.5 pts | 16 | -15.0 | -0.94 | +4.8 / -19.8 | +6.6 / -14.6 / -7.0 | +0.12 |
| room < 1 pts | 31 | +7.7 | +0.25 | -1.4 / +9.1 | +0.6 / -16.4 / +23.5 | -0.35 |
| room < 2 pts | 47 | -15.7 | -0.33 | -14.3 / -1.5 | -8.8 / -28.7 / +21.7 | +0.28 |

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

**MGC 3m out-of-sample (from 11/06 12:00 ET)** (10 setups, net +26.1, avg +2.60)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 2 | +21.7 | +10.86 | +21.7 / +0.0 | +0.0 / +21.7 / +0.0 | +0.54 |
| room x TP1 < 0.15 | 2 | +21.7 | +10.86 | +21.7 / +0.0 | +0.0 / +21.7 / +0.0 | +0.54 |
| room x TP1 < 0.2 | 3 | +16.7 | +5.57 | +21.7 / -5.0 | +0.0 / +21.7 / -5.0 | +1.33 |
| room x TP1 < 0.25 | 4 | +18.9 | +4.73 | +21.7 / -2.8 | +0.0 / +21.7 / -2.8 | +1.19 |
| room x TP1 < 0.3 | 4 | +18.9 | +4.73 | +21.7 / -2.8 | +0.0 / +21.7 / -2.8 | +1.19 |
| room x TP1 < 0.5 | 7 | +20.6 | +2.95 | +21.4 / -0.8 | -0.3 / +23.7 / -2.8 | +1.80 |
| room < 0.5 pts | 1 | -6.2 | -6.18 | -6.2 / +0.0 | +0.0 / -6.2 / +0.0 | +3.58 |
| room < 1 pts | 4 | +18.9 | +4.73 | +21.7 / -2.8 | +0.0 / +21.7 / -2.8 | +1.19 |
| room < 2 pts | 5 | +22.4 | +4.49 | +25.2 / -2.8 | +3.5 / +21.7 / -2.8 | +0.72 |

Per day (setups with Room line / room x TP1 < 0.2), last 8: 11/3 6/3, 11/4 2/0, 11/5 4/2, 11/6 6/2, 11/8 3/2, 11/9 2/0, 11/10 1/0, 11/11 2/1
All setups per day, last 8: 11/3 6, 11/4 2, 11/5 4, 11/6 6, 11/8 3, 11/9 2, 11/10 1, 11/11 2

Room line on 68 setups; rebuild matched on 67.

## History
| run | MES 3m blocked / net at 0.2 x TP1 | out-of-sample blocked / net | verdict |
|---|---|---|---|
| 2026-11-12 17:48 ET | 36 / -47.4 | 3 / -2.4 | MES 3m candidate, waiting for OOS (5 OOS setups); MGC 3m keep off (now using 0.5×TP1 results for duplicated setups) |
| 2026-11-12 09:46 ET (re-run of failed 11/11) | 35 / -52.6 | 2 / -7.6 | MES 3m candidate, waiting for OOS (MES 3m alerts silent 11/10-11/11); MGC 3m keep off |
| 2026-11-09 17:48 ET | 35 / -52.6 | 2 / -7.6 | MES 3m candidate, waiting for OOS; MGC 3m keep off |
| 2026-11-06 (baseline study) | 32 / -53.1 | -- | MES 3m candidate; MGC 3m keep off |
