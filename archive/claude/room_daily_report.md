# CBC room-to-first-level check -- 2026-11-13 17:48 ET

**STUDY SETTINGS STALE:** settings_sync_report (11/13 16:47 ET) lists 3 MISMATCH -- mes3_ema_grid `LIVE` part 'tod' and chop_sim `EXIT` MES 3m part 'tod' vs live 100 % at TP1 all day (v10.95), chop_sim `EXIT` MGC 3m 50 % / trail 3.5 vs live FLIP 0 % / no trail (v10.96). This check reads CBC's own "Setup Ended" results, not the replay scripts, so the mismatches do not change its numbers; but the 11/13 setups ran on the new exits (MES 3m 100 % at TP1, MGC 3m FLIP 0 %), adding one more exit version to the mix. Newest Pine v10.96.

Data: tv-webhook-dashboard alerts (47,887 stored, store still not de-duplicated; setups collapsed by (time, direction, entry), duplicate results -> the 0.5×(TP1) one per data note 2 -- 3 MGC 3m setups). Room line on 74 setups; rebuild matched it on 73.

## Verdicts
- **MES 3m: candidate, waiting for out-of-sample (3 blocked, -2.4).** Gate "room x TP1 < 0.2": 36 blocked, -47.4 (avg -1.32); halves -19.0 / -28.4; thirds -16.1 / -23.0 / -8.2; kept avg +0.27 vs -0.26 all. (a)-(c) pass at 0.2, 0.25 and 0.5; (d) needs 8+ out-of-sample blocked -- only 6 MES 3m setups since 11/06 12:00 ET.
- **MGC 3m: keep off.** At 0.2: 33 blocked, +13.8 (halves +0.7 / +13.1, thirds -0.2 / -8.8 / +22.8); kept avg -0.19 < all +0.06. Out-of-sample 5 blocked, +17.0. No threshold passes.
- Gate live? No -- 11/13 MES 3m had 1 setup (08:33 long, room 0.79 x TP1, -16.3, not blocked); MES 3m still never has 3+ setups/day lately.
- Only one new MES 3m setup since the last run (11/13 08:33, kept by the gate, -16.3): the blocked numbers are unchanged and the all-setups avg dropped -0.11 -> -0.26. MGC 3m added 3 setups on 11/13 (2 with room x TP1 < 0.2: +2.1, -1.8) and 2 on 11/12 evening.
- Bot set here = first trigger HTF CBC Flip or LTF EMA20 Pierce beyond EMA9 (as defined in this check; the live MES 3m bot also takes "not beyond EMA9" since 11/12). MES 3m bot set at 0.2: 11 blocked, -16.3 (halves -8.5 / -7.8, thirds -3.5 / +1.7 / -14.4).

## MES 3m -- 108 setups (10/19 05:54 -> 11/13 08:33), win 46 %, net -28.0, avg -0.26; Room line on 38
Halves: 54 -31.1 / 54 +3.2; thirds: 36 -34.8 / 36 -17.9 / 36 +24.7

| room pts | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.5 | 20 | 45 | -13.7 | -0.69 |
| 0.5-1 | 9 | 33 | -28.2 | -3.13 |
| 1-2 | 28 | 64 | +52.9 | +1.89 |
| 2-3 | 14 | 28 | -28.5 | -2.04 |
| 3-5 | 22 | 45 | -8.4 | -0.38 |
| 5-8 | 8 | 12 | -60.6 | -7.57 |
| 8-+ | 7 | 71 | +58.6 | +8.37 |

| room x TP1 | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.1 | 24 | 45 | -14.9 | -0.62 |
| 0.1-0.2 | 12 | 33 | -32.5 | -2.70 |
| 0.2-0.3 | 15 | 66 | +31.3 | +2.09 |
| 0.3-0.5 | 21 | 33 | -40.7 | -1.94 |
| 0.5-1 | 27 | 48 | -3.1 | -0.12 |
| 1-+ | 9 | 55 | +31.9 | +3.54 |

**MES 3m all setups** (108 setups, net -28.0, avg -0.26)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 24 | -14.9 | -0.62 | -7.1 / -7.8 | -10.0 / -17.2 / +12.4 | -0.16 |
| room x TP1 < 0.15 | 32 | -38.1 | -1.19 | -18.2 / -19.9 | -15.3 / -23.0 / +0.2 | +0.13 |
| room x TP1 < 0.2 | 36 | -47.4 | -1.32 | -19.0 / -28.4 | -16.1 / -23.0 / -8.2 | +0.27 |
| room x TP1 < 0.25 | 41 | -23.2 | -0.56 | -1.2 / -21.9 | -2.7 / -16.9 / -3.5 | -0.07 |
| room x TP1 < 0.3 | 51 | -16.0 | -0.31 | -2.8 / -13.2 | -11.0 / -13.1 / +8.0 | -0.21 |
| room x TP1 < 0.5 | 72 | -56.8 | -0.79 | -32.3 / -24.5 | -37.3 / -15.5 / -4.0 | +0.80 |
| room < 0.5 pts | 20 | -13.7 | -0.69 | -7.1 / -6.6 | -10.0 / -18.1 / +14.4 | -0.16 |
| room < 1 pts | 29 | -41.9 | -1.45 | -15.0 / -27.0 | -12.1 / -23.0 / -6.8 | +0.18 |
| room < 2 pts | 57 | +11.0 | +0.19 | +2.2 / +8.8 | -12.6 / +2.3 / +21.3 | -0.76 |

**MES 3m bot set (Flip + LTF beyond EMA9)** (32 setups, net +9.4, avg +0.29)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 9 | +8.2 | +0.91 | -8.5 / +16.7 | -3.5 / +1.7 / +10.1 | +0.05 |
| room x TP1 < 0.15 | 11 | -16.3 | -1.48 | -8.5 / -7.8 | -3.5 / +1.7 / -14.4 | +1.22 |
| room x TP1 < 0.2 | 11 | -16.3 | -1.48 | -8.5 / -7.8 | -3.5 / +1.7 / -14.4 | +1.22 |
| room x TP1 < 0.25 | 14 | -5.4 | -0.39 | -4.1 / -1.3 | -3.5 / +7.8 / -9.7 | +0.82 |
| room x TP1 < 0.3 | 17 | -12.8 | -0.75 | -8.3 / -4.5 | -3.5 / -4.4 / -4.9 | +1.48 |
| room x TP1 < 0.5 | 22 | -3.8 | -0.17 | -9.0 / +5.2 | -7.9 / -0.7 / +4.8 | +1.32 |
| room < 0.5 pts | 8 | +2.9 | +0.36 | -8.5 / +11.4 | -3.5 / +1.7 / +4.8 | +0.27 |
| room < 1 pts | 9 | -7.3 | -0.81 | -8.5 / +1.2 | -3.5 / +1.7 / -5.4 | +0.73 |
| room < 2 pts | 18 | +11.5 | +0.64 | +1.8 / +9.8 | +2.8 / -0.7 / +9.4 | -0.15 |

**MES 3m out-of-sample (from 11/06 12:00 ET)** (6 setups, net -40.9, avg -6.81)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 1 | +5.2 | +5.25 | +0.0 / +5.2 | +0.0 / +0.0 / +5.2 | -9.23 |
| room x TP1 < 0.15 | 3 | -2.4 | -0.79 | -7.6 / +5.2 | +11.4 / -19.0 / +5.2 | -12.84 |
| room x TP1 < 0.2 | 3 | -2.4 | -0.79 | -7.6 / +5.2 | +11.4 / -19.0 / +5.2 | -12.84 |
| room x TP1 < 0.25 | 3 | -2.4 | -0.79 | -7.6 / +5.2 | +11.4 / -19.0 / +5.2 | -12.84 |
| room x TP1 < 0.3 | 3 | -2.4 | -0.79 | -7.6 / +5.2 | +11.4 / -19.0 / +5.2 | -12.84 |
| room x TP1 < 0.5 | 4 | -5.9 | -1.46 | -11.1 / +5.2 | +7.9 / -19.0 / +5.2 | -17.51 |
| room < 0.5 pts | 1 | +5.2 | +5.25 | +0.0 / +5.2 | +0.0 / +0.0 / +5.2 | -9.23 |
| room < 1 pts | 1 | +5.2 | +5.25 | +0.0 / +5.2 | +0.0 / +0.0 / +5.2 | -9.23 |
| room < 2 pts | 3 | -2.4 | -0.79 | -7.6 / +5.2 | +11.4 / -19.0 / +5.2 | -12.84 |

Per day (setups / with Room line / room x TP1 < 0.2 by Room line), last 8: 11/2 8/8/1, 11/3 8/8/4, 11/4 2/2/2, 11/5 5/5/3, 11/6 3/3/0, 11/8 2/2/2, 11/12 2/2/1, 11/13 1/1/0

Last 6 setups: 11/06 14:03 L HTF Pullback Structure rx 0.35 -3.5; 11/08 18:48 S LTF EMA20 Pierce (late rx 0.11 +11.4; 11/08 20:36 S LTF EMA20 Pierce (clos rx 0.13 -19.0; 11/12 09:30 S HTF CBC Flip rx 0.62 -18.7; 11/12 10:03 L LTF EMA20 Pierce (clos rx 0.01 +5.2; 11/13 08:33 L LTF EMA20 Pierce (clos rx 0.79 -16.3

Verdict checks (x: a b c d | OOS n/net): 0.1: YnYn 1/+5.2; 0.15: YnYn 3/-2.4; 0.2: YYYn 3/-2.4; 0.25: YYYn 3/-2.4; 0.3: YnYn 3/-2.4; 0.5: YYYn 4/-5.9

## MGC 3m -- 80 setups (10/19 03:42 -> 11/13 12:57), win 46 %, net +4.7, avg +0.06; Room line on 36
Halves: 40 -13.0 / 40 +17.6; thirds: 26 +3.8 / 27 -50.8 / 27 +51.7

| room pts | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.5 | 18 | 38 | -14.7 | -0.82 |
| 0.5-1 | 15 | 46 | +22.7 | +1.51 |
| 1-2 | 16 | 31 | -23.4 | -1.46 |
| 2-3 | 10 | 60 | +10.6 | +1.06 |
| 3-5 | 11 | 54 | +0.5 | +0.04 |
| 5-8 | 8 | 50 | -2.8 | -0.35 |
| 8-+ | 2 | 100 | +11.8 | +5.89 |

| room x TP1 | N | win % | net | avg |
|---|---|---|---|---|
| 0-0.1 | 19 | 36 | +7.3 | +0.39 |
| 0.1-0.2 | 14 | 50 | +6.4 | +0.46 |
| 0.2-0.3 | 11 | 36 | -16.4 | -1.49 |
| 0.3-0.5 | 14 | 42 | -4.6 | -0.33 |
| 0.5-1 | 12 | 66 | +15.9 | +1.32 |
| 1-+ | 10 | 50 | -4.0 | -0.40 |

**MGC 3m all setups** (80 setups, net +4.7, avg +0.06)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 19 | +7.3 | +0.39 | +3.6 / +3.7 | +5.8 / -15.0 / +16.5 | -0.04 |
| room x TP1 < 0.15 | 29 | +9.7 | +0.33 | -2.4 / +12.1 | -0.2 / -12.0 / +21.9 | -0.10 |
| room x TP1 < 0.2 | 33 | +13.8 | +0.42 | +0.7 / +13.1 | -0.2 / -8.8 / +22.8 | -0.19 |
| room x TP1 < 0.25 | 37 | +15.1 | +0.41 | -0.2 / +15.3 | -0.2 / -9.7 / +25.0 | -0.24 |
| room x TP1 < 0.3 | 44 | -2.6 | -0.06 | -6.7 / +4.1 | +0.1 / -23.2 / +20.5 | +0.20 |
| room x TP1 < 0.5 | 58 | -7.2 | -0.12 | -2.8 / -4.4 | +4.1 / -33.5 / +22.2 | +0.54 |
| room < 0.5 pts | 18 | -14.7 | -0.82 | +4.8 / -19.6 | +5.8 / -9.1 / -11.4 | +0.31 |
| room < 1 pts | 33 | +8.0 | +0.24 | -1.4 / +9.3 | -0.2 / -10.9 / +19.1 | -0.07 |
| room < 2 pts | 49 | -15.4 | -0.31 | -16.4 / +0.9 | -9.6 / -24.9 / +19.1 | +0.65 |

**MGC 3m bot set (Flip + LTF beyond EMA9)** (26 setups, net -7.0, avg -0.27)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 7 | -19.2 | -2.74 | -1.1 / -18.1 | +0.9 / -8.4 / -11.7 | +0.64 |
| room x TP1 < 0.15 | 9 | -12.0 | -1.33 | +1.4 / -13.4 | +3.4 / -3.7 / -11.7 | +0.29 |
| room x TP1 < 0.2 | 13 | -7.9 | -0.61 | +4.6 / -12.5 | +3.4 / -0.6 / -10.8 | +0.07 |
| room x TP1 < 0.25 | 14 | -11.6 | -0.83 | +0.9 / -12.5 | +3.4 / -4.2 / -10.8 | +0.38 |
| room x TP1 < 0.3 | 16 | -17.7 | -1.10 | -5.2 / -12.5 | -2.7 / -4.2 / -10.8 | +1.07 |
| room x TP1 < 0.5 | 19 | -13.9 | -0.73 | -8.7 / -5.2 | -2.7 / -2.5 / -8.8 | +0.98 |
| room < 0.5 pts | 8 | -14.5 | -1.82 | -1.1 / -13.4 | +0.9 / -3.7 / -11.7 | +0.42 |
| room < 1 pts | 11 | -13.8 | -1.26 | +4.6 / -18.4 | +3.4 / -0.6 / -16.7 | +0.45 |
| room < 2 pts | 16 | -17.7 | -1.10 | -5.2 / -12.5 | -2.7 / -4.2 / -10.8 | +1.07 |

**MGC 3m out-of-sample (from 11/06 12:00 ET)** (15 setups, net +38.6, avg +2.57)

| gate | blocked N | net | avg | halves | thirds | kept avg |
|---|---|---|---|---|---|---|
| room x TP1 < 0.1 | 4 | +22.0 | +5.50 | +21.7 / +0.3 | +21.7 / +0.0 / +0.3 | +1.51 |
| room x TP1 < 0.15 | 4 | +22.0 | +5.50 | +21.7 / +0.3 | +21.7 / +0.0 / +0.3 | +1.51 |
| room x TP1 < 0.2 | 5 | +17.0 | +3.40 | +21.7 / -4.7 | +21.7 / -5.0 / +0.3 | +2.16 |
| room x TP1 < 0.25 | 6 | +19.2 | +3.20 | +21.7 / -2.5 | +21.7 / -2.8 / +0.3 | +2.16 |
| room x TP1 < 0.3 | 6 | +19.2 | +3.20 | +21.7 / -2.5 | +21.7 / -2.8 / +0.3 | +2.16 |
| room x TP1 < 0.5 | 9 | +20.9 | +2.33 | +23.4 / -2.5 | +21.4 / -0.8 / +0.3 | +2.95 |
| room < 0.5 pts | 3 | -5.9 | -1.97 | -6.2 / +0.3 | -6.2 / +0.0 / +0.3 | +3.71 |
| room < 1 pts | 6 | +19.2 | +3.20 | +21.7 / -2.5 | +21.7 / -2.8 / +0.3 | +2.16 |
| room < 2 pts | 7 | +22.7 | +3.25 | +25.2 / -2.5 | +25.2 / -2.8 / +0.3 | +1.99 |

Per day (setups / with Room line / room x TP1 < 0.2 by Room line), last 8: 11/5 4/4/2, 11/6 6/6/2, 11/8 3/3/2, 11/9 2/2/0, 11/10 1/1/0, 11/11 2/2/1, 11/12 2/2/0, 11/13 3/3/2

Last 6 setups: 11/11 06:15 L HTF CBC Flip rx 0.18 -5.0; 11/12 19:03 L LTF EMA20 Pierce (clos rx 0.51 +2.4; 11/12 19:39 L HTF EMA9 Pierce (late) rx 0.79 +2.8; 11/13 06:18 S LTF EMA20 Pierce (clos rx 0.10 +2.1; 11/13 10:15 S LTF EMA20 Pierce (clos rx 0.68 +7.2; 11/13 12:57 L HTF EMA20 Pierce rx 0.04 -1.8

Verdict checks (x: a b c d | OOS n/net): 0.1: nnnn 4/+22.0; 0.15: Ynnn 4/+22.0; 0.2: Ynnn 5/+17.0; 0.25: Ynnn 6/+19.2; 0.3: YnYn 6/+19.2; 0.5: YnYn 9/+20.9


## History
| run | MES 3m blocked / net at 0.2 x TP1 | out-of-sample blocked / net | verdict |
|---|---|---|---|
| 2026-11-13 17:48 ET | 36 / -47.4 | 3 / -2.4 | MES 3m candidate, waiting for OOS (6 OOS setups); MGC 3m keep off; study settings stale (3 MISMATCH, replay scripts only) |
| 2026-11-12 17:48 ET | 36 / -47.4 | 3 / -2.4 | MES 3m candidate, waiting for OOS (5 OOS setups); MGC 3m keep off (now using 0.5×TP1 results for duplicated setups) |
| 2026-11-12 09:46 ET (re-run of failed 11/11) | 35 / -52.6 | 2 / -7.6 | MES 3m candidate, waiting for OOS (MES 3m alerts silent 11/10-11/11); MGC 3m keep off |
| 2026-11-09 17:48 ET | 35 / -52.6 | 2 / -7.6 | MES 3m candidate, waiting for OOS; MGC 3m keep off |
| 2026-11-06 (baseline study) | 32 / -53.1 | -- | MES 3m candidate; MGC 3m keep off |
