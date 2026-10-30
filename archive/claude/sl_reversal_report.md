# Stop-out reversal study — run Wed 10/28/2026 (look-ahead window changed to 1–10 candles)

## Since last week

The look-ahead window is now **1–10 candles** after the stop (was 1–5); the summary reports **within 1 / within 10**. The what-if (SL1 wider by x ATR) replays every setup to its end, so it does not change with the window. Weekly check 1 of 3 (same day as the first run).

| Chart | TP1 within 1 / 10 candles after the stop (sim) | Extra room needed (median, 10-candle window) | Best what-if (sim) | Better in all thirds? | Live stop-outs → reversed within 10 | Live net at best width |
|---|---|---|---|---|---|---|
| MGC 3m | 3 % / 26 % | 0.40 ATR / 2.2 pts | +1.0 ATR: +150 | No | 15 → 3 | +20.3 |
| MES 3m | 3 % / 22 % | 0.57 ATR / 2.5 pts | +1.0 ATR: +165 | No | 32 → 10 | +34.9 |
| MGC 2m | 1 % / 12 % | 0.51 ATR / 1.5 pts | +1.0 ATR: +115 | No | 20 → 4 | +14.2 |
| MES 2m | 1 % / 14 % | 0.64 ATR / 2.5 pts | none (⚠ worse in all thirds at +0.5) | — | 34 → 1 | −32 (at +0.5) |
| MGC 5m | 7 % / 33 % | 0.37 ATR / 3.1 pts | +1.0 ATR: +361 | ✓ every width | 7 → 1 | −6.0 |
| MES 5m | 5 % / 26 % | 0.42 ATR / 2.5 pts | +1.0 ATR: +276 | ✓ at 0.75 and 1.0 | 14 → 4 | −17.4 |

**Verdict: no change.** MGC 5m and MES 5m pass the sim test, but this is weekly check 1 of 3, live samples are 7 and 14 (need ≥ 20), and live is net negative at every width on both. The setting in question is the "Max ATR SL1 (pts) per symbol" cap (MGC 7 / MES 8); it is per symbol, so a 5m-only change would need a Pine change.

---

# Stop-out reversals — SL1 hit, then TP1 within 1–10 candles? — Wed 10/28/2026 18:24 ET

CBC stop-out reversal study: after a setup hits SL1, does price turn around within the next 1-10 candles and reach
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
| within 1 | 15 of 470 (3%) | 6% / 3% / 1% | 1 of 15 (7%) |
| within 2 | 27 of 470 (6%) | 9% / 6% / 3% | 1 of 15 (7%) |
| within 3 | 39 of 470 (8%) | 12% / 10% / 4% | 1 of 15 (7%) |
| within 4 | 54 of 470 (11%) | 14% / 15% / 5% | 2 of 15 (13%) |
| within 5 | 64 of 470 (14%) | 17% / 17% / 6% | 2 of 15 (13%) |
| within 6 | 74 of 470 (16%) | 20% / 19% / 8% | 3 of 15 (20%) |
| within 7 | 85 of 470 (18%) | 26% / 20% / 8% | 3 of 15 (20%) |
| within 8 | 98 of 470 (21%) | 30% / 24% / 9% | 3 of 15 (20%) |
| within 9 | 108 of 470 (23%) | 31% / 26% / 11% | 3 of 15 (20%) |
| within 10 | 120 of 470 (26%) | 35% / 28% / 14% | 3 of 15 (20%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.40 ATR / 2.17 pts, 75 % 0.84 ATR / 4.50 pts, 90 % 1.55 ATR / 7.45 pts.
Live: 10/23 04:33 L LTF EMA20 Pierce +0.89 pts beyond SL1, TP1 4 candle(s) after the stop; 10/26 19:18 S LTF EMA20 Pierce +0.02 pts beyond SL1, TP1 6 candle(s) after the stop; 10/28 14:45 L HTF CBC Flip +3.30 pts beyond SL1, TP1 1 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

HTF EMA9 Pierce 73 SL → 0% / 18%, LTF EMA20 Pierce 247 SL → 4% / 26%, HTF CBC Flip 92 SL → 2% / 29%, HTF EMA20 Pierce 58 SL → 7% / 29%

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
| within 1 | 14 of 448 (3%) | 3% / 1% / 5% | 2 of 32 (6%) |
| within 2 | 27 of 448 (6%) | 7% / 4% / 7% | 3 of 32 (9%) |
| within 3 | 43 of 448 (10%) | 12% / 6% / 11% | 4 of 32 (12%) |
| within 4 | 50 of 448 (11%) | 13% / 7% / 13% | 5 of 32 (16%) |
| within 5 | 62 of 448 (14%) | 16% / 9% / 17% | 6 of 32 (19%) |
| within 6 | 70 of 448 (16%) | 18% / 11% / 18% | 6 of 32 (19%) |
| within 7 | 77 of 448 (17%) | 20% / 13% / 19% | 7 of 32 (22%) |
| within 8 | 82 of 448 (18%) | 22% / 13% / 20% | 8 of 32 (25%) |
| within 9 | 92 of 448 (21%) | 25% / 14% / 23% | 10 of 32 (31%) |
| within 10 | 99 of 448 (22%) | 26% / 16% / 24% | 10 of 32 (31%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.57 ATR / 2.50 pts, 75 % 1.00 ATR / 5.25 pts, 90 % 2.21 ATR / 7.75 pts.
Live: 10/20 06:03 S HTF EMA9 Pierce +0.61 pts beyond SL1, TP1 7 candle(s) after the stop; 10/20 07:30 S LTF EMA20 Pierce +0.11 pts beyond SL1, TP1 3 candle(s) after the stop; 10/20 14:51 S HTF EMA20 Pierce +1.04 pts beyond SL1, TP1 9 candle(s) after the stop; 10/22 11:21 S HTF EMA9 Pierce +0.25 pts beyond SL1, TP1 1 candle(s) after the stop; 10/22 14:15 S LTF EMA20 Pierce +4.47 pts beyond SL1, TP1 4 candle(s) after the stop; 10/23 07:30 S HTF EMA9 Pierce +1.16 pts beyond SL1, TP1 8 candle(s) after the stop; 10/26 13:33 L LTF EMA20 Pierce +7.46 pts beyond SL1, TP1 5 candle(s) after the stop; 10/28 13:36 S HTF EMA20 Pierce +7.51 pts beyond SL1, TP1 2 candle(s) after the stop; 10/28 14:03 L LTF EMA20 Pierce +9.82 pts beyond SL1, TP1 9 candle(s) after the stop; 10/28 14:45 L HTF CBC Flip +5.25 pts beyond SL1, TP1 1 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

LTF EMA20 Pierce 230 SL → 4% / 24%, HTF EMA20 Pierce 38 SL → 3% / 18%, HTF EMA9 Pierce 72 SL → 1% / 22%, HTF CBC Flip 108 SL → 3% / 19%

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
| within 1 | 4 of 400 (1%) | 0% / 2% / 1% | 1 of 20 (5%) |
| within 2 | 8 of 400 (2%) | 2% / 2% / 1% | 1 of 20 (5%) |
| within 3 | 10 of 400 (2%) | 3% / 3% / 1% | 1 of 20 (5%) |
| within 4 | 19 of 400 (5%) | 5% / 5% / 5% | 1 of 20 (5%) |
| within 5 | 22 of 400 (6%) | 5% / 5% / 6% | 2 of 20 (10%) |
| within 6 | 28 of 400 (7%) | 5% / 8% / 8% | 2 of 20 (10%) |
| within 7 | 35 of 400 (9%) | 6% / 9% / 11% | 3 of 20 (15%) |
| within 8 | 44 of 400 (11%) | 10% / 11% / 13% | 3 of 20 (15%) |
| within 9 | 47 of 400 (12%) | 11% / 12% / 13% | 3 of 20 (15%) |
| within 10 | 50 of 400 (12%) | 11% / 14% / 13% | 4 of 20 (20%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.51 ATR / 1.50 pts, 75 % 0.78 ATR / 3.30 pts, 90 % 1.37 ATR / 6.40 pts.
Live: 10/19 19:50 S HTF CBC Flip +2.30 pts beyond SL1, TP1 10 candle(s) after the stop; 10/22 04:40 S HTF CBC Flip +0.60 pts beyond SL1, TP1 7 candle(s) after the stop; 10/22 21:10 S LTF EMA20 Pierce +0.51 pts beyond SL1, TP1 5 candle(s) after the stop; 10/28 14:10 S HTF CBC Flip +9.68 pts beyond SL1, TP1 1 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

HTF CBC Flip 166 SL → 2% / 16%, LTF EMA20 Pierce 154 SL → 0% / 9%, HTF EMA9 Pierce 52 SL → 0% / 12%, HTF EMA20 Pierce 28 SL → 0% / 11%

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
| within 1 | 4 of 285 (1%) | 3% / 1% / 0% | 0 of 34 (0%) |
| within 2 | 7 of 285 (2%) | 4% / 3% / 0% | 0 of 34 (0%) |
| within 3 | 10 of 285 (4%) | 5% / 4% / 1% | 0 of 34 (0%) |
| within 4 | 12 of 285 (4%) | 6% / 5% / 1% | 0 of 34 (0%) |
| within 5 | 17 of 285 (6%) | 7% / 6% / 4% | 0 of 34 (0%) |
| within 6 | 21 of 285 (7%) | 11% / 6% / 5% | 0 of 34 (0%) |
| within 7 | 26 of 285 (9%) | 15% / 6% / 6% | 0 of 34 (0%) |
| within 8 | 31 of 285 (11%) | 17% / 7% / 8% | 1 of 34 (3%) |
| within 9 | 36 of 285 (13%) | 18% / 7% / 13% | 1 of 34 (3%) |
| within 10 | 41 of 285 (14%) | 19% / 9% / 15% | 1 of 34 (3%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.64 ATR / 2.50 pts, 75 % 1.26 ATR / 4.00 pts, 90 % 1.87 ATR / 5.25 pts.
Live: 10/20 19:54 L LTF EMA20 Pierce +0.75 pts beyond SL1, TP1 8 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

LTF EMA20 Pierce 114 SL → 2% / 15%, HTF CBC Flip 123 SL → 0% / 11%, HTF EMA20 Pierce 14 SL → 7% / 29%, HTF EMA9 Pierce 34 SL → 3% / 18%

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
| within 1 | 34 of 461 (7%) | 14% / 5% / 3% | 0 of 7 (0%) |
| within 2 | 48 of 461 (10%) | 18% / 10% / 3% | 0 of 7 (0%) |
| within 3 | 69 of 461 (15%) | 27% / 11% / 7% | 0 of 7 (0%) |
| within 4 | 78 of 461 (17%) | 28% / 13% / 10% | 0 of 7 (0%) |
| within 5 | 97 of 461 (21%) | 31% / 18% / 14% | 0 of 7 (0%) |
| within 6 | 113 of 461 (25%) | 37% / 19% / 18% | 0 of 7 (0%) |
| within 7 | 123 of 461 (27%) | 41% / 21% / 18% | 1 of 7 (14%) |
| within 8 | 139 of 461 (30%) | 44% / 23% / 23% | 1 of 7 (14%) |
| within 9 | 143 of 461 (31%) | 46% / 24% / 23% | 1 of 7 (14%) |
| within 10 | 150 of 461 (33%) | 48% / 25% / 24% | 1 of 7 (14%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.37 ATR / 3.10 pts, 75 % 0.93 ATR / 7.60 pts, 90 % 1.62 ATR / 15.10 pts.
Live: 10/27 19:05 L LTF EMA20 Pierce +0.70 pts beyond SL1, TP1 7 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

HTF CBC Flip 128 SL → 9% / 27%, LTF EMA20 Pierce 231 SL → 9% / 35%, HTF EMA20 Pierce 39 SL → 0% / 28%, HTF EMA9 Pierce 63 SL → 5% / 35%

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
| within 1 | 20 of 379 (5%) | 8% / 4% / 4% | 1 of 14 (7%) |
| within 2 | 25 of 379 (7%) | 10% / 5% / 5% | 1 of 14 (7%) |
| within 3 | 36 of 379 (9%) | 13% / 9% / 6% | 1 of 14 (7%) |
| within 4 | 55 of 379 (15%) | 22% / 13% / 8% | 1 of 14 (7%) |
| within 5 | 62 of 379 (16%) | 25% / 17% / 8% | 2 of 14 (14%) |
| within 6 | 73 of 379 (19%) | 28% / 18% / 12% | 2 of 14 (14%) |
| within 7 | 80 of 379 (21%) | 30% / 19% / 14% | 3 of 14 (21%) |
| within 8 | 86 of 379 (23%) | 33% / 20% / 16% | 4 of 14 (29%) |
| within 9 | 92 of 379 (24%) | 33% / 21% / 19% | 4 of 14 (29%) |
| within 10 | 99 of 379 (26%) | 35% / 22% / 21% | 4 of 14 (29%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.42 ATR / 2.50 pts, 75 % 0.88 ATR / 4.50 pts, 90 % 1.52 ATR / 9.59 pts.
Live: 10/20 21:00 L other +0.75 pts beyond SL1, TP1 5 candle(s) after the stop; 10/22 13:05 S LTF EMA20 Pierce +5.75 pts beyond SL1, TP1 8 candle(s) after the stop; 10/26 19:00 L LTF EMA20 Pierce +9.50 pts beyond SL1, TP1 7 candle(s) after the stop; 10/28 03:40 L LTF EMA20 Pierce +0.75 pts beyond SL1, TP1 1 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

HTF EMA9 Pierce 45 SL → 2% / 27%, HTF CBC Flip 119 SL → 3% / 19%, LTF EMA20 Pierce 189 SL → 6% / 30%, HTF EMA20 Pierce 26 SL → 12% / 31%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 70 of 379 | +121.5 | +122 / -7 / +6 | 3 of 14 | -2.6 |
| 0.50 ATR | 129 of 379 | +168.8 | +123 / -2 / +47 | 5 of 14 | -5.4 |
| 0.75 ATR | 172 of 379 | +157.4 ✓ | +126 / +11 / +21 | 7 of 14 | -9.3 |
| 1.00 ATR | 216 of 379 | +276.3 ✓ | +118 / +125 / +33 | 7 of 14 | -17.4 |

## Summary

- MGC 3m: 3% of sim SL1 setups reach TP1 within 1 candle, 26% within 10 (live 20% of 15); SL1 +0.5 ATR → sim +137 (thirds +10 / +168 / -41), live +22.5
- MES 3m: 3% of sim SL1 setups reach TP1 within 1 candle, 22% within 10 (live 31% of 32); SL1 +0.5 ATR → sim +18 (thirds +28 / -69 / +59), live +16.3
- MGC 2m: 1% of sim SL1 setups reach TP1 within 1 candle, 12% within 10 (live 20% of 20); SL1 +0.5 ATR → sim +19 (thirds -78 / +29 / +67), live +7.9
- MES 2m: 1% of sim SL1 setups reach TP1 within 1 candle, 14% within 10 (live 3% of 34); SL1 +0.5 ATR → sim -51 (thirds -18 / -12 / -20), live -32.3
- MGC 5m: 7% of sim SL1 setups reach TP1 within 1 candle, 33% within 10 (live 14% of 7); SL1 +0.5 ATR → sim +300 (thirds +133 / +31 / +135), live -3.2
- MES 5m: 5% of sim SL1 setups reach TP1 within 1 candle, 26% within 10 (live 29% of 14); SL1 +0.5 ATR → sim +169 (thirds +123 / -2 / +47), live -5.4

✓ = better in all three thirds, ⚠ = worse in all three thirds. Stop widths and minimums also change position size / risk per trade, which this does not account for.
