# Stop-out reversals — SL1 hit, then TP1 within 5 / 10 / 15 / 20 candles? — Wed 10/28/2026 18:26 ET

CBC stop-out reversal study: after a setup hits SL1, does price turn around within the next 5 / 10 / 15 / 20 candles and reach
the setup's TP1 -- i.e. would a slightly wider stop have turned the loss into a TP1 win?

For every setup that ended "SL1 hit": the stop candle = the candle that touched SL1. For N = 1..10 we check the N
candles AFTER the stop candle: did any of them reach TP1 (long: high >= TP1, short: low <= TP1)? For those that did,
"extra stop needed" = how far price went beyond SL1 (from the stop candle up to the TP1 candle), in points and ATR.
Then a what-if: the same setups with SL1 wider by 0.25 / 0.5 / 0.75 / 1.0 ATR, replayed with the chart's exits
(net change counts the setups the wider stop saves AND the extra loss on the ones that still stop out; setups that
never touched SL1 are not affected by a wider stop).
Cases: MGC 3m, MES 3m (HTF 15m), MGC 2m, MES 2m (HTF 10m), MGC 5m, MES 5m (HTF 25m).
Sources:
  LIVE  real setups that ended "SL1 hit" (Entry / SL1 / TP1 from the Trade Setup alert, stop time from the Setup
        Ended alert), checked against the BarFeed candles.
  SIM   chop_sim.py replay (CBC v10.42 exits per chart; ~50 % exact match with real setups) on the BarFeed archive:
        3m and 5m from 01/05, 2m from 06/01. Thirds = the case's sim SL1 setups split into three equal time blocks.
Usage: python3 sl_reversal_study.py > sl_reversal_report_new.md   (needs chop_sim.py and evening_study.py next to it)

## MGC 3m — sim 1140 setups, 470 hit SL1 (41%) · live 15 SL1 setups (15 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 5 | 64 of 470 (14%) | 17% / 17% / 6% | 2 of 15 (13%) |
| within 10 | 120 of 470 (26%) | 35% / 28% / 14% | 3 of 15 (20%) |
| within 15 | 158 of 470 (34%) | 42% / 36% / 23% | 4 of 15 (27%) |
| within 20 | 192 of 470 (41%) | 47% / 46% / 29% | 6 of 15 (40%) |

| Window | Extra beyond SL1 needed: median | 75 % | 90 % |
|---|---|---|---|
| within 5 | 0.28 ATR / 1.40 pts | 0.50 ATR / 3.40 pts | 0.78 ATR / 5.50 pts |
| within 10 | 0.40 ATR / 2.17 pts | 0.84 ATR / 4.50 pts | 1.55 ATR / 7.45 pts |
| within 15 | 0.49 ATR / 2.51 pts | 1.17 ATR / 5.50 pts | 1.96 ATR / 11.10 pts |
| within 20 | 0.55 ATR / 3.16 pts | 1.37 ATR / 6.10 pts | 2.12 ATR / 11.10 pts |
Live: 10/23 04:33 L LTF EMA20 Pierce +0.89 pts beyond SL1, TP1 4 candle(s) after the stop; 10/26 18:48 S LTF EMA20 Pierce +0.09 pts beyond SL1, TP1 16 candle(s) after the stop; 10/26 19:18 S LTF EMA20 Pierce +0.02 pts beyond SL1, TP1 6 candle(s) after the stop; 10/27 06:00 L LTF EMA20 Pierce +6.13 pts beyond SL1, TP1 11 candle(s) after the stop; 10/27 19:00 L LTF EMA20 Pierce +4.21 pts beyond SL1, TP1 20 candle(s) after the stop; 10/28 14:45 L HTF CBC Flip +3.30 pts beyond SL1, TP1 1 candle(s) after the stop

**By setup type (sim, reached TP1 within 5 / 20 candles)**

HTF EMA9 Pierce 73 SL → 8% / 34%, LTF EMA20 Pierce 247 SL → 14% / 43%, HTF CBC Flip 92 SL → 15% / 40%, HTF EMA20 Pierce 58 SL → 17% / 40%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 92 of 470 | -40.7 | -60 / +71 / -52 | 5 of 15 | +6.3 |
| 0.50 ATR | 173 of 470 | +137.0 | +10 / +168 / -41 | 8 of 15 | +22.5 |
| 0.75 ATR | 227 of 470 | +95.0 | -29 / +168 / -44 | 10 of 15 | +21.0 |
| 1.00 ATR | 279 of 470 | +150.4 | +22 / +174 / -46 | 12 of 15 | +20.3 |

## MES 3m — sim 1669 setups, 448 hit SL1 (27%) · live 32 SL1 setups (32 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 5 | 62 of 448 (14%) | 16% / 9% / 17% | 6 of 32 (19%) |
| within 10 | 99 of 448 (22%) | 26% / 16% / 24% | 10 of 32 (31%) |
| within 15 | 133 of 448 (30%) | 34% / 24% / 31% | 12 of 32 (38%) |
| within 20 | 164 of 448 (37%) | 42% / 31% / 37% | 13 of 32 (41%) |

| Window | Extra beyond SL1 needed: median | 75 % | 90 % |
|---|---|---|---|
| within 5 | 0.51 ATR / 2.50 pts | 0.96 ATR / 5.25 pts | 1.67 ATR / 7.25 pts |
| within 10 | 0.57 ATR / 2.50 pts | 1.00 ATR / 5.25 pts | 2.21 ATR / 7.75 pts |
| within 15 | 0.60 ATR / 2.75 pts | 1.11 ATR / 5.67 pts | 1.79 ATR / 7.75 pts |
| within 20 | 0.67 ATR / 3.00 pts | 1.35 ATR / 6.00 pts | 2.25 ATR / 9.50 pts |
Live: 10/19 19:30 S HTF CBC Flip +2.09 pts beyond SL1, TP1 11 candle(s) after the stop; 10/20 06:03 S HTF EMA9 Pierce +0.61 pts beyond SL1, TP1 7 candle(s) after the stop; 10/20 07:30 S LTF EMA20 Pierce +0.11 pts beyond SL1, TP1 3 candle(s) after the stop; 10/20 14:51 S HTF EMA20 Pierce +1.04 pts beyond SL1, TP1 9 candle(s) after the stop; 10/21 14:54 L HTF EMA20 Pierce +24.69 pts beyond SL1, TP1 19 candle(s) after the stop; 10/22 11:21 S HTF EMA9 Pierce +0.25 pts beyond SL1, TP1 1 candle(s) after the stop; 10/22 14:15 S LTF EMA20 Pierce +4.47 pts beyond SL1, TP1 4 candle(s) after the stop; 10/23 07:30 S HTF EMA9 Pierce +1.16 pts beyond SL1, TP1 8 candle(s) after the stop; 10/26 13:33 L LTF EMA20 Pierce +7.46 pts beyond SL1, TP1 5 candle(s) after the stop; 10/28 12:57 L LTF EMA20 Pierce +8.35 pts beyond SL1, TP1 14 candle(s) after the stop; 10/28 13:36 S HTF EMA20 Pierce +7.51 pts beyond SL1, TP1 2 candle(s) after the stop; 10/28 14:03 L LTF EMA20 Pierce +9.82 pts beyond SL1, TP1 9 candle(s) after the stop; 10/28 14:45 L HTF CBC Flip +5.25 pts beyond SL1, TP1 1 candle(s) after the stop

**By setup type (sim, reached TP1 within 5 / 20 candles)**

LTF EMA20 Pierce 230 SL → 17% / 37%, HTF EMA20 Pierce 38 SL → 11% / 24%, HTF EMA9 Pierce 72 SL → 12% / 43%, HTF CBC Flip 108 SL → 10% / 35%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 95 of 448 | -12.4 | +39 / -63 / +12 | 6 of 32 | +11.3 |
| 0.50 ATR | 156 of 448 | +18.1 | +28 / -69 / +59 | 11 of 32 | +16.3 |
| 0.75 ATR | 223 of 448 | +93.8 | +78 / -84 / +100 | 16 of 32 | +48.7 |
| 1.00 ATR | 276 of 448 | +165.1 | +53 / -6 / +118 | 16 of 32 | +34.9 |

## MGC 2m — sim 1409 setups, 400 hit SL1 (28%) · live 20 SL1 setups (20 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 5 | 22 of 400 (6%) | 5% / 5% / 6% | 2 of 20 (10%) |
| within 10 | 50 of 400 (12%) | 11% / 14% / 13% | 4 of 20 (20%) |
| within 15 | 78 of 400 (20%) | 17% / 22% / 19% | 4 of 20 (20%) |
| within 20 | 102 of 400 (26%) | 26% / 25% / 25% | 5 of 20 (25%) |

| Window | Extra beyond SL1 needed: median | 75 % | 90 % |
|---|---|---|---|
| within 5 | 0.44 ATR / 1.95 pts | 0.77 ATR / 2.90 pts | 1.17 ATR / 5.60 pts |
| within 10 | 0.51 ATR / 1.50 pts | 0.78 ATR / 3.30 pts | 1.37 ATR / 6.40 pts |
| within 15 | 0.51 ATR / 1.60 pts | 0.92 ATR / 3.30 pts | 1.62 ATR / 6.40 pts |
| within 20 | 0.56 ATR / 1.90 pts | 1.14 ATR / 3.82 pts | 2.24 ATR / 6.90 pts |
Live: 10/19 19:50 S HTF CBC Flip +2.30 pts beyond SL1, TP1 10 candle(s) after the stop; 10/22 04:40 S HTF CBC Flip +0.60 pts beyond SL1, TP1 7 candle(s) after the stop; 10/22 21:10 S LTF EMA20 Pierce +0.51 pts beyond SL1, TP1 5 candle(s) after the stop; 10/26 07:04 L LTF EMA20 Pierce +0.70 pts beyond SL1, TP1 20 candle(s) after the stop; 10/28 14:10 S HTF CBC Flip +9.68 pts beyond SL1, TP1 1 candle(s) after the stop

**By setup type (sim, reached TP1 within 5 / 20 candles)**

HTF CBC Flip 166 SL → 5% / 28%, LTF EMA20 Pierce 154 SL → 6% / 26%, HTF EMA9 Pierce 52 SL → 4% / 23%, HTF EMA20 Pierce 28 SL → 7% / 14%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 88 of 400 | +46.5 | -42 / +20 / +68 | 4 of 20 | +14.1 |
| 0.50 ATR | 141 of 400 | +18.9 | -78 / +29 / +67 | 7 of 20 | +7.9 |
| 0.75 ATR | 193 of 400 | +69.4 | -35 / +57 / +48 | 10 of 20 | +19.2 |
| 1.00 ATR | 236 of 400 | +114.5 | -14 / +65 / +63 | 11 of 20 | +14.2 |

## MES 2m — sim 1149 setups, 285 hit SL1 (25%) · live 34 SL1 setups (34 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 5 | 17 of 285 (6%) | 7% / 6% / 4% | 0 of 34 (0%) |
| within 10 | 41 of 285 (14%) | 19% / 9% / 15% | 1 of 34 (3%) |
| within 15 | 54 of 285 (19%) | 23% / 17% / 17% | 2 of 34 (6%) |
| within 20 | 75 of 285 (26%) | 29% / 25% / 24% | 6 of 34 (18%) |

| Window | Extra beyond SL1 needed: median | 75 % | 90 % |
|---|---|---|---|
| within 5 | 0.51 ATR / 1.58 pts | 0.92 ATR / 3.50 pts | 1.41 ATR / 4.75 pts |
| within 10 | 0.64 ATR / 2.50 pts | 1.26 ATR / 4.00 pts | 1.87 ATR / 5.25 pts |
| within 15 | 0.57 ATR / 2.31 pts | 1.26 ATR / 4.00 pts | 1.87 ATR / 5.71 pts |
| within 20 | 0.76 ATR / 2.75 pts | 1.41 ATR / 4.25 pts | 1.91 ATR / 6.37 pts |
Live: 10/19 10:32 L LTF EMA20 Pierce +1.75 pts beyond SL1, TP1 14 candle(s) after the stop; 10/19 19:20 S HTF CBC Flip +0.00 pts beyond SL1, TP1 16 candle(s) after the stop; 10/20 19:54 L LTF EMA20 Pierce +0.75 pts beyond SL1, TP1 8 candle(s) after the stop; 10/21 12:40 L HTF EMA9 Pierce +3.42 pts beyond SL1, TP1 20 candle(s) after the stop; 10/27 06:00 L HTF CBC Flip +10.00 pts beyond SL1, TP1 19 candle(s) after the stop; 10/28 14:00 L HTF CBC Flip +11.50 pts beyond SL1, TP1 16 candle(s) after the stop

**By setup type (sim, reached TP1 within 5 / 20 candles)**

LTF EMA20 Pierce 114 SL → 5% / 27%, HTF CBC Flip 123 SL → 5% / 22%, HTF EMA20 Pierce 14 SL → 14% / 43%, HTF EMA9 Pierce 34 SL → 9% / 32%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 64 of 285 | -34.9 | -10 / -29 / +4 | 4 of 34 | -22.8 |
| 0.50 ATR | 106 of 285 | -50.6 ⚠ | -18 / -12 / -20 | 7 of 34 | -32.3 |
| 0.75 ATR | 148 of 285 | -14.6 | -8 / -9 / +3 | 10 of 34 | -47.6 |
| 1.00 ATR | 176 of 285 | -16.6 | -35 / +16 / +3 | 17 of 34 | -34.7 |

## MGC 5m — sim 1134 setups, 461 hit SL1 (41%) · live 7 SL1 setups (7 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 5 | 97 of 461 (21%) | 31% / 18% / 14% | 0 of 7 (0%) |
| within 10 | 150 of 461 (33%) | 48% / 25% / 24% | 1 of 7 (14%) |
| within 15 | 201 of 461 (44%) | 59% / 35% / 36% | 2 of 7 (29%) |
| within 20 | 230 of 461 (50%) | 65% / 42% / 42% | 2 of 7 (29%) |

| Window | Extra beyond SL1 needed: median | 75 % | 90 % |
|---|---|---|---|
| within 5 | 0.29 ATR / 2.50 pts | 0.56 ATR / 6.10 pts | 1.06 ATR / 11.10 pts |
| within 10 | 0.37 ATR / 3.10 pts | 0.93 ATR / 7.60 pts | 1.62 ATR / 15.10 pts |
| within 15 | 0.48 ATR / 3.60 pts | 1.11 ATR / 9.20 pts | 2.04 ATR / 15.10 pts |
| within 20 | 0.61 ATR / 4.40 pts | 1.31 ATR / 10.10 pts | 2.58 ATR / 15.90 pts |
Live: 10/22 05:20 S LTF EMA20 Pierce +1.80 pts beyond SL1, TP1 11 candle(s) after the stop; 10/27 19:05 L LTF EMA20 Pierce +0.70 pts beyond SL1, TP1 7 candle(s) after the stop

**By setup type (sim, reached TP1 within 5 / 20 candles)**

HTF CBC Flip 128 SL → 18% / 44%, LTF EMA20 Pierce 231 SL → 23% / 54%, HTF EMA20 Pierce 39 SL → 18% / 44%, HTF EMA9 Pierce 63 SL → 21% / 52%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 103 of 461 | +320.4 ✓ | +195 / +51 / +75 | 2 of 7 | -3.3 |
| 0.50 ATR | 167 of 461 | +299.7 ✓ | +133 / +31 / +135 | 4 of 7 | -3.2 |
| 0.75 ATR | 215 of 461 | +255.3 ✓ | +146 / +37 / +72 | 5 of 7 | -3.8 |
| 1.00 ATR | 269 of 461 | +361.0 ✓ | +159 / +90 / +112 | 5 of 7 | -6.0 |

## MES 5m — sim 1154 setups, 379 hit SL1 (33%) · live 14 SL1 setups (14 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 5 | 62 of 379 (16%) | 25% / 17% / 8% | 2 of 14 (14%) |
| within 10 | 99 of 379 (26%) | 35% / 22% / 21% | 4 of 14 (29%) |
| within 15 | 136 of 379 (36%) | 40% / 35% / 33% | 5 of 14 (36%) |
| within 20 | 162 of 379 (43%) | 44% / 45% / 39% | 5 of 14 (36%) |

| Window | Extra beyond SL1 needed: median | 75 % | 90 % |
|---|---|---|---|
| within 5 | 0.28 ATR / 1.75 pts | 0.53 ATR / 3.50 pts | 1.00 ATR / 6.00 pts |
| within 10 | 0.42 ATR / 2.50 pts | 0.88 ATR / 4.50 pts | 1.52 ATR / 9.59 pts |
| within 15 | 0.53 ATR / 2.65 pts | 1.21 ATR / 5.75 pts | 2.72 ATR / 11.75 pts |
| within 20 | 0.58 ATR / 2.75 pts | 1.31 ATR / 6.00 pts | 2.58 ATR / 11.75 pts |
Live: 10/20 21:00 L other +0.75 pts beyond SL1, TP1 5 candle(s) after the stop; 10/21 05:50 L LTF EMA20 Pierce +5.41 pts beyond SL1, TP1 15 candle(s) after the stop; 10/22 13:05 S LTF EMA20 Pierce +5.75 pts beyond SL1, TP1 8 candle(s) after the stop; 10/26 19:00 L LTF EMA20 Pierce +9.50 pts beyond SL1, TP1 7 candle(s) after the stop; 10/28 03:40 L LTF EMA20 Pierce +0.75 pts beyond SL1, TP1 1 candle(s) after the stop

**By setup type (sim, reached TP1 within 5 / 20 candles)**

HTF EMA9 Pierce 45 SL → 16% / 33%, HTF CBC Flip 119 SL → 13% / 41%, LTF EMA20 Pierce 189 SL → 19% / 45%, HTF EMA20 Pierce 26 SL → 15% / 50%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 70 of 379 | +121.5 | +122 / -7 / +6 | 3 of 14 | -2.6 |
| 0.50 ATR | 129 of 379 | +168.8 | +123 / -2 / +47 | 5 of 14 | -5.4 |
| 0.75 ATR | 172 of 379 | +157.4 ✓ | +126 / +11 / +21 | 7 of 14 | -9.3 |
| 1.00 ATR | 216 of 379 | +276.3 ✓ | +118 / +125 / +33 | 7 of 14 | -17.4 |

## Summary

- MGC 3m: 3% of sim SL1 setups reach TP1 within 1 candle, 41% within 10 (live 40% of 15); SL1 +0.5 ATR → sim +137 (thirds +10 / +168 / -41), live +22.5
- MES 3m: 3% of sim SL1 setups reach TP1 within 1 candle, 37% within 10 (live 41% of 32); SL1 +0.5 ATR → sim +18 (thirds +28 / -69 / +59), live +16.3
- MGC 2m: 1% of sim SL1 setups reach TP1 within 1 candle, 26% within 10 (live 25% of 20); SL1 +0.5 ATR → sim +19 (thirds -78 / +29 / +67), live +7.9
- MES 2m: 1% of sim SL1 setups reach TP1 within 1 candle, 26% within 10 (live 18% of 34); SL1 +0.5 ATR → sim -51 (thirds -18 / -12 / -20), live -32.3
- MGC 5m: 7% of sim SL1 setups reach TP1 within 1 candle, 50% within 10 (live 29% of 7); SL1 +0.5 ATR → sim +300 (thirds +133 / +31 / +135), live -3.2
- MES 5m: 5% of sim SL1 setups reach TP1 within 1 candle, 43% within 10 (live 36% of 14); SL1 +0.5 ATR → sim +169 (thirds +123 / -2 / +47), live -5.4

✓ = better in all three thirds, ⚠ = worse in all three thirds. Stop widths and minimums also change position size / risk per trade, which this does not account for.
