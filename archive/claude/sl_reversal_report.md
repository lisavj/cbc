# Stop-out reversal study — weekly check 3 (rerun after data repair) — 2026-11-07 09:51 ET

**Rerun after data repair.** This run **replaces the 11/06 18:08 ET run** as weekly check 3 (the user asked for a rerun on 11/07 after the BarFeed bars were repaired: MGC 3m had 5m candles mixed in, and the MES 2m / 5m charts had gaps, among other fixes). The original 11/06 run is no longer counted. An earlier 11/07 09:46 ET run gave identical results. Market closed since Fri 17:00, so the live alerts are the same as on 11/06.

## Since last week (vs Fri 10/30, check 2)

Look-ahead window 1–10 candles after the stop. Exits per CBC v10.45: all charts on the base exits (SL1 1.7 ATR + min 5, TP1 1.7 ATR, 80 %, BE at TP1, trail 1.7, no time stop), Max ATR SL1 cap MGC 7 / MES 8.

**Simulator caveat:** `chop_sim.py` still models the **old MGC 3m exits** (SL1 1.3 ATR, no minimum, TP1 2.0 ATR, 50 %, no BE, 10-bar time stop — v10.31); `evening_study.py` overrides only MES 3m and the 5m charts. The MGC 3m sim rows (and the MGC 3m live what-if replay) reflect the pre-10/29 exits. Method not changed. Sim matches ~50 % of real setups — compare, don't trust exact totals; a wider stop = more points at risk per contract.

| Chart | TP1 within 1 / 10 candles (sim) | vs 10/30 | Extra room needed (median) | Best what-if (sim) | ✓ all thirds? | Live stop-outs → reversed within 10 (vs 10/30) | Live net at best width |
|---|---|---|---|---|---|---|---|
| MGC 3m (old exits in sim) | 3 % / 26 % | same | 0.40 ATR / 2.2 pts | +1.0 ATR: +146 (+0.5: +145) | **No** — last third −23 … −39 at every width (original 11/06 run: ✓ at 0.5–1.0, on the bad MGC 3m data) | 26 → 4 (21 → 4) | +4.6 (+11.7 at 0.5) |
| MES 3m | 3 % / 23 % | was 3 / 22 | 0.53 ATR / 2.5 pts | +1.0 ATR: +186 | ✓ at 1.0 only (0.75: −76 mid third) | 40 → 12 (35 → 11) | +61.2 |
| MGC 2m | 1 % / 13 % | same | 0.49 ATR / 1.5 pts | +1.0 ATR: +104 | No (first third −7 … −72) | 46 → 8 (29 → 6) | −16.8 |
| MES 2m | 2 % / 15 % | was 1 / 15 | 0.64 ATR / 2.5 pts | +1.0 ATR: +5 | No (first two thirds negative at every width) | 47 → 3 (36 → 1) | −6.8 (negative at every width) |
| MGC 5m | 7 % / 32 % | same | 0.39 ATR / 3.1 pts | +1.0 ATR: +384 | ✓ at 0.25, 0.75, 1.0 (0.5: middle third −1) | 19 → 4 (9 → 2) | +6.1 (+20.1 at 0.5) |
| MES 5m | 5 % / 26 % | was 5 / 27 | 0.42 ATR / 2.5 pts | +1.0 ATR: +264 | ✓ at 0.5, 0.75, 1.0 | 25 → 9 (19 → 7) | −23.1 (negative at every width) |

**MGC 3m live, split by exit regime** (live what-if replays with the sim's old MGC 3m exits):
- Before 10/29 (old 1.3-ATR stop): 16 stop-outs, 3 reversed to TP1 within 10 (1 within 1); +0.25 / 0.5 / 0.75 / 1.0 ATR → +3.1 / +19.6 / +19.9 / +19.1.
- From 10/29 (1.7 ATR + min 5): 10 stop-outs, 1 reversed within 10 (10/29 21:21 S); +0.25 / 0.5 / 0.75 / 1.0 → −0.6 / −7.8 / −10.4 / −14.5. Negative at every width; too few to judge.

(5m live by period, for reference: MES 5m 15 before 10/29 → 4 reversed, net −1 to −16; 10 from 10/29 → 5 reversed, net −9 to +2. MGC 5m 7 before → 1, net −3 to −6; 12 from → 3, net +12 to +23.)

**Verdict streaks** (better in all thirds at a width AND a neighbouring width; checks 10/28, 10/30, 11/06 = this rerun):
- MES 5m: 0.75 ATR (neighbours 0.5 / 1.0 also ✓) — **3 of 3** checks. Sim side met. Live 25 stop-outs, **net negative at every width** (−1.7 / −17.1 / −23.1 at 0.5 / 0.75 / 1.0). Live condition fails → not ready.
- MGC 5m: 0.75 + 1.0 ✓ (also 0.25) → streak **1** (reset on 10/30).
- MGC 3m: no width ✓ on the repaired data → streak **0** (the original 11/06 run's ✓ came from the mixed-in 5m candles). Post-10/29 live is negative at every width.
- MES 3m: ✓ at 1.0 only, neighbour fails → 0. MGC 2m / MES 2m: 0.

**Verdict: no change.** Nothing meets the rule. Strongest candidate is still the per-symbol **"Max ATR SL1 (pts)" cap** (MES 8) for MES 5m — sim has held 3 checks, but real MES 5m stop-outs still lose more with a wider stop than they save. The cap is per symbol, so a 5m-only change would need a Pine change.

---

# Stop-out reversals — SL1 hit, then TP1 within 1–10 candles? (rerun after data repair) — 2026-11-07 09:51 ET

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

## MGC 3m — sim 1183 setups, 482 hit SL1 (41%) · live 26 SL1 setups (26 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 1 | 16 of 482 (3%) | 6% / 3% / 1% | 1 of 26 (4%) |
| within 2 | 28 of 482 (6%) | 9% / 5% / 3% | 1 of 26 (4%) |
| within 3 | 40 of 482 (8%) | 12% / 9% / 4% | 1 of 26 (4%) |
| within 4 | 55 of 482 (11%) | 15% / 14% / 6% | 2 of 26 (8%) |
| within 5 | 66 of 482 (14%) | 18% / 16% / 7% | 3 of 26 (12%) |
| within 6 | 77 of 482 (16%) | 21% / 17% / 10% | 4 of 26 (15%) |
| within 7 | 88 of 482 (18%) | 27% / 18% / 10% | 4 of 26 (15%) |
| within 8 | 101 of 482 (21%) | 31% / 22% / 11% | 4 of 26 (15%) |
| within 9 | 112 of 482 (23%) | 32% / 24% / 14% | 4 of 26 (15%) |
| within 10 | 124 of 482 (26%) | 35% / 26% / 16% | 4 of 26 (15%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.40 ATR / 2.17 pts, 75 % 0.84 ATR / 4.50 pts, 90 % 1.46 ATR / 7.24 pts.
Live: 10/23 04:33 L LTF EMA20 Pierce +0.89 pts beyond SL1, TP1 4 candle(s) after the stop; 10/26 19:18 S LTF EMA20 Pierce +0.02 pts beyond SL1, TP1 6 candle(s) after the stop; 10/28 14:45 L HTF CBC Flip +3.30 pts beyond SL1, TP1 1 candle(s) after the stop; 10/29 21:21 S LTF EMA20 Pierce +0.50 pts beyond SL1, TP1 5 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

HTF EMA9 Pierce 75 SL → 0% / 17%, LTF EMA20 Pierce 255 SL → 4% / 25%, HTF CBC Flip 94 SL → 3% / 31%, HTF EMA20 Pierce 58 SL → 7% / 29%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 94 of 482 | -32.3 | -35 / +42 / -39 | 6 of 26 | +2.5 |
| 0.50 ATR | 178 of 482 | +145.2 | +32 / +137 / -23 | 10 of 26 | +11.7 |
| 0.75 ATR | 232 of 482 | +96.1 | -9 / +133 / -28 | 15 of 26 | +9.5 |
| 1.00 ATR | 285 of 482 | +146.0 | +41 / +138 / -33 | 18 of 26 | +4.6 |

## MES 3m — sim 1719 setups, 466 hit SL1 (27%) · live 40 SL1 setups (40 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 1 | 14 of 466 (3%) | 3% / 2% / 4% | 2 of 40 (5%) |
| within 2 | 28 of 466 (6%) | 6% / 5% / 6% | 3 of 40 (8%) |
| within 3 | 46 of 466 (10%) | 12% / 8% / 10% | 4 of 40 (10%) |
| within 4 | 54 of 466 (12%) | 13% / 10% / 12% | 6 of 40 (15%) |
| within 5 | 66 of 466 (14%) | 15% / 12% / 15% | 7 of 40 (18%) |
| within 6 | 75 of 466 (16%) | 17% / 14% / 17% | 7 of 40 (18%) |
| within 7 | 84 of 466 (18%) | 19% / 15% / 19% | 8 of 40 (20%) |
| within 8 | 89 of 466 (19%) | 21% / 15% / 21% | 10 of 40 (25%) |
| within 9 | 99 of 466 (21%) | 24% / 17% / 23% | 12 of 40 (30%) |
| within 10 | 106 of 466 (23%) | 25% / 19% / 24% | 12 of 40 (30%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.53 ATR / 2.50 pts, 75 % 0.93 ATR / 5.25 pts, 90 % 2.19 ATR / 7.51 pts.
Live: 10/20 06:03 S HTF EMA9 Pierce +0.61 pts beyond SL1, TP1 7 candle(s) after the stop; 10/20 07:30 S LTF EMA20 Pierce +0.11 pts beyond SL1, TP1 3 candle(s) after the stop; 10/20 14:51 S HTF EMA20 Pierce +1.04 pts beyond SL1, TP1 9 candle(s) after the stop; 10/22 11:21 S HTF EMA9 Pierce +0.25 pts beyond SL1, TP1 1 candle(s) after the stop; 10/22 14:15 S LTF EMA20 Pierce +4.47 pts beyond SL1, TP1 4 candle(s) after the stop; 10/23 07:30 S HTF EMA9 Pierce +1.16 pts beyond SL1, TP1 8 candle(s) after the stop; 10/26 13:33 L LTF EMA20 Pierce +7.46 pts beyond SL1, TP1 5 candle(s) after the stop; 10/28 13:36 S HTF EMA20 Pierce +7.51 pts beyond SL1, TP1 2 candle(s) after the stop; 10/28 14:03 L LTF EMA20 Pierce +9.82 pts beyond SL1, TP1 9 candle(s) after the stop; 10/28 14:45 L HTF CBC Flip +5.25 pts beyond SL1, TP1 1 candle(s) after the stop; 10/29 04:36 L HTF EMA9 Pierce +7.02 pts beyond SL1, TP1 4 candle(s) after the stop; 11/02 15:03 S LTF EMA20 Pierce +6.75 pts beyond SL1, TP1 8 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

LTF EMA20 Pierce 240 SL → 4% / 25%, HTF EMA20 Pierce 38 SL → 3% / 18%, HTF EMA9 Pierce 76 SL → 1% / 22%, HTF CBC Flip 112 SL → 3% / 19%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 98 of 466 | -2.7 | +37 / -50 / +10 | 7 of 40 | +6.0 |
| 0.50 ATR | 162 of 466 | +41.3 | +23 / -49 / +67 | 12 of 40 | +2.8 |
| 0.75 ATR | 230 of 466 | +120.5 | +78 / -76 / +118 | 21 of 40 | +56.6 |
| 1.00 ATR | 285 of 466 | +185.9 ✓ | +52 / +25 / +109 | 22 of 40 | +61.2 |

## MGC 2m — sim 1499 setups, 430 hit SL1 (29%) · live 46 SL1 setups (46 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 1 | 5 of 430 (1%) | 1% / 1% / 1% | 2 of 46 (4%) |
| within 2 | 9 of 430 (2%) | 3% / 2% / 1% | 2 of 46 (4%) |
| within 3 | 11 of 430 (3%) | 3% / 3% / 1% | 2 of 46 (4%) |
| within 4 | 21 of 430 (5%) | 5% / 6% / 4% | 3 of 46 (7%) |
| within 5 | 25 of 430 (6%) | 6% / 6% / 6% | 4 of 46 (9%) |
| within 6 | 32 of 430 (7%) | 6% / 8% / 8% | 4 of 46 (9%) |
| within 7 | 39 of 430 (9%) | 7% / 10% / 10% | 6 of 46 (13%) |
| within 8 | 48 of 430 (11%) | 10% / 12% / 11% | 6 of 46 (13%) |
| within 9 | 52 of 430 (12%) | 11% / 13% / 12% | 7 of 46 (15%) |
| within 10 | 55 of 430 (13%) | 11% / 15% / 12% | 8 of 46 (17%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.49 ATR / 1.50 pts, 75 % 0.78 ATR / 3.30 pts, 90 % 1.33 ATR / 5.70 pts.
Live: 10/19 19:50 S HTF CBC Flip +2.30 pts beyond SL1, TP1 10 candle(s) after the stop; 10/22 04:40 S HTF CBC Flip +0.60 pts beyond SL1, TP1 7 candle(s) after the stop; 10/22 21:10 S LTF EMA20 Pierce +0.51 pts beyond SL1, TP1 5 candle(s) after the stop; 10/28 14:10 S HTF CBC Flip +9.68 pts beyond SL1, TP1 1 candle(s) after the stop; 10/28 19:40 S HTF EMA9 Pierce +1.00 pts beyond SL1, TP1 4 candle(s) after the stop; 10/29 21:22 S LTF EMA20 Pierce +2.30 pts beyond SL1, TP1 7 candle(s) after the stop; 11/01 19:56 L LTF EMA20 Pierce +3.50 pts beyond SL1, TP1 1 candle(s) after the stop; 11/05 10:02 S LTF EMA20 Pierce +5.20 pts beyond SL1, TP1 9 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

HTF CBC Flip 177 SL → 2% / 16%, LTF EMA20 Pierce 163 SL → 1% / 11%, HTF EMA9 Pierce 58 SL → 0% / 10%, HTF EMA20 Pierce 32 SL → 0% / 9%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 94 of 430 | +42.8 | -32 / +18 / +56 | 8 of 46 | +1.1 |
| 0.50 ATR | 155 of 430 | +32.0 | -72 / +38 / +66 | 15 of 46 | -15.8 |
| 0.75 ATR | 208 of 430 | +69.5 | -25 / +56 / +39 | 21 of 46 | -1.8 |
| 1.00 ATR | 253 of 430 | +104.2 | -7 / +63 / +48 | 23 of 46 | -16.8 |

## MES 2m — sim 1226 setups, 315 hit SL1 (26%) · live 47 SL1 setups (47 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 1 | 5 of 315 (2%) | 3% / 1% / 1% | 0 of 47 (0%) |
| within 2 | 9 of 315 (3%) | 4% / 3% / 2% | 0 of 47 (0%) |
| within 3 | 12 of 315 (4%) | 6% / 3% / 3% | 0 of 47 (0%) |
| within 4 | 14 of 315 (4%) | 7% / 4% / 3% | 1 of 47 (2%) |
| within 5 | 19 of 315 (6%) | 8% / 6% / 5% | 1 of 47 (2%) |
| within 6 | 23 of 315 (7%) | 10% / 6% / 6% | 1 of 47 (2%) |
| within 7 | 28 of 315 (9%) | 14% / 6% / 7% | 1 of 47 (2%) |
| within 8 | 34 of 315 (11%) | 16% / 8% / 9% | 3 of 47 (6%) |
| within 9 | 41 of 315 (13%) | 17% / 8% / 14% | 3 of 47 (6%) |
| within 10 | 47 of 315 (15%) | 18% / 10% / 16% | 3 of 47 (6%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.64 ATR / 2.50 pts, 75 % 1.13 ATR / 4.25 pts, 90 % 1.82 ATR / 6.25 pts.
Live: 10/20 19:54 L LTF EMA20 Pierce +0.75 pts beyond SL1, TP1 8 candle(s) after the stop; 11/03 20:50 S LTF EMA20 Pierce +6.25 pts beyond SL1, TP1 8 candle(s) after the stop; 11/04 03:52 L LTF EMA20 Pierce +1.23 pts beyond SL1, TP1 4 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

LTF EMA20 Pierce 128 SL → 2% / 16%, HTF CBC Flip 133 SL → 1% / 12%, HTF EMA20 Pierce 15 SL → 7% / 27%, HTF EMA9 Pierce 39 SL → 3% / 18%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 75 of 315 | -12.9 | -11 / -40 / +38 | 11 of 47 | -9.4 |
| 0.50 ATR | 123 of 315 | -26.4 | -19 / -22 / +15 | 15 of 47 | -0.5 |
| 0.75 ATR | 167 of 315 | +0.4 | -12 / -24 / +36 | 20 of 47 | -17.2 |
| 1.00 ATR | 198 of 315 | +5.2 | -27 / -17 / +49 | 27 of 47 | -6.8 |

## MGC 5m — sim 1173 setups, 480 hit SL1 (41%) · live 19 SL1 setups (19 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 1 | 35 of 480 (7%) | 16% / 3% / 3% | 1 of 19 (5%) |
| within 2 | 50 of 480 (10%) | 20% / 7% / 4% | 1 of 19 (5%) |
| within 3 | 72 of 480 (15%) | 28% / 8% / 9% | 3 of 19 (16%) |
| within 4 | 81 of 480 (17%) | 29% / 11% / 10% | 3 of 19 (16%) |
| within 5 | 100 of 480 (21%) | 32% / 16% / 14% | 3 of 19 (16%) |
| within 6 | 116 of 480 (24%) | 38% / 17% / 18% | 3 of 19 (16%) |
| within 7 | 126 of 480 (26%) | 42% / 19% / 18% | 4 of 19 (21%) |
| within 8 | 142 of 480 (30%) | 45% / 21% / 22% | 4 of 19 (21%) |
| within 9 | 147 of 480 (31%) | 46% / 22% / 24% | 4 of 19 (21%) |
| within 10 | 155 of 480 (32%) | 49% / 24% / 24% | 4 of 19 (21%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.39 ATR / 3.10 pts, 75 % 0.93 ATR / 7.50 pts, 90 % 1.62 ATR / 14.70 pts.
Live: 10/27 19:05 L LTF EMA20 Pierce +0.70 pts beyond SL1, TP1 7 candle(s) after the stop; 10/29 20:35 S LTF EMA20 Pierce +3.97 pts beyond SL1, TP1 3 candle(s) after the stop; 11/04 11:05 L HTF CBC Flip +2.40 pts beyond SL1, TP1 3 candle(s) after the stop; 11/05 10:15 S LTF EMA20 Pierce +0.90 pts beyond SL1, TP1 1 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

HTF CBC Flip 135 SL → 8% / 28%, LTF EMA20 Pierce 238 SL → 9% / 35%, HTF EMA20 Pierce 41 SL → 0% / 27%, HTF EMA9 Pierce 66 SL → 5% / 35%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 108 of 480 | +344.6 ✓ | +220 / +25 / +99 | 5 of 19 | +13.1 |
| 0.50 ATR | 174 of 480 | +340.7 | +167 / -1 / +174 | 8 of 19 | +20.1 |
| 0.75 ATR | 224 of 480 | +286.1 ✓ | +173 / +0 / +113 | 9 of 19 | +10.4 |
| 1.00 ATR | 279 of 480 | +383.5 ✓ | +185 / +65 / +133 | 10 of 19 | +6.1 |

## MES 5m — sim 1183 setups, 391 hit SL1 (33%) · live 25 SL1 setups (25 matched to bars)

| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |
|---|---|---|---|
| within 1 | 20 of 391 (5%) | 8% / 5% / 3% | 1 of 25 (4%) |
| within 2 | 25 of 391 (6%) | 10% / 6% / 3% | 1 of 25 (4%) |
| within 3 | 37 of 391 (9%) | 13% / 10% / 5% | 2 of 25 (8%) |
| within 4 | 56 of 391 (14%) | 22% / 15% / 7% | 3 of 25 (12%) |
| within 5 | 63 of 391 (16%) | 24% / 18% / 7% | 5 of 25 (20%) |
| within 6 | 75 of 391 (19%) | 27% / 20% / 11% | 6 of 25 (24%) |
| within 7 | 82 of 391 (21%) | 29% / 21% / 13% | 7 of 25 (28%) |
| within 8 | 88 of 391 (23%) | 32% / 22% / 15% | 8 of 25 (32%) |
| within 9 | 94 of 391 (24%) | 32% / 22% / 18% | 8 of 25 (32%) |
| within 10 | 102 of 391 (26%) | 34% / 25% / 20% | 9 of 25 (36%) |

Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median 0.42 ATR / 2.50 pts, 75 % 0.89 ATR / 4.50 pts, 90 % 1.58 ATR / 11.25 pts.
Live: 10/20 21:00 L other +0.75 pts beyond SL1, TP1 5 candle(s) after the stop; 10/22 13:05 S LTF EMA20 Pierce +5.75 pts beyond SL1, TP1 8 candle(s) after the stop; 10/26 19:00 L LTF EMA20 Pierce +9.50 pts beyond SL1, TP1 7 candle(s) after the stop; 10/28 03:40 L LTF EMA20 Pierce +0.75 pts beyond SL1, TP1 1 candle(s) after the stop; 10/29 10:40 L HTF CBC Flip +15.25 pts beyond SL1, TP1 10 candle(s) after the stop; 10/29 14:55 S LTF EMA20 Pierce +15.00 pts beyond SL1, TP1 6 candle(s) after the stop; 10/30 10:40 S LTF EMA20 Pierce +2.25 pts beyond SL1, TP1 4 candle(s) after the stop; 11/04 13:25 L LTF EMA20 Pierce +3.50 pts beyond SL1, TP1 5 candle(s) after the stop; 11/06 07:25 S LTF EMA20 Pierce +3.25 pts beyond SL1, TP1 3 candle(s) after the stop

**By setup type (sim, reached TP1 within 1 / 10 candles)**

HTF EMA9 Pierce 47 SL → 2% / 26%, HTF CBC Flip 124 SL → 3% / 19%, LTF EMA20 Pierce 194 SL → 6% / 30%, HTF EMA20 Pierce 26 SL → 12% / 31%

**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**

| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |
|---|---|---|---|---|---|
| 0.25 ATR | 72 of 391 | +120.9 | +119 / -3 / +5 | 5 of 25 | -4.7 |
| 0.50 ATR | 133 of 391 | +151.9 ✓ | +117 / +13 / +22 | 11 of 25 | -1.7 |
| 0.75 ATR | 177 of 391 | +146.6 ✓ | +116 / +29 / +2 | 13 of 25 | -17.1 |
| 1.00 ATR | 223 of 391 | +263.9 ✓ | +118 / +129 / +17 | 15 of 25 | -23.1 |

## Summary

- MGC 3m: 3% of sim SL1 setups reach TP1 within 1 candle, 26% within 10 (live 15% of 26); SL1 +0.5 ATR → sim +145 (thirds +32 / +137 / -23), live +11.7
- MES 3m: 3% of sim SL1 setups reach TP1 within 1 candle, 23% within 10 (live 30% of 40); SL1 +0.5 ATR → sim +41 (thirds +23 / -49 / +67), live +2.8
- MGC 2m: 1% of sim SL1 setups reach TP1 within 1 candle, 13% within 10 (live 17% of 46); SL1 +0.5 ATR → sim +32 (thirds -72 / +38 / +66), live -15.8
- MES 2m: 2% of sim SL1 setups reach TP1 within 1 candle, 15% within 10 (live 6% of 47); SL1 +0.5 ATR → sim -26 (thirds -19 / -22 / +15), live -0.5
- MGC 5m: 7% of sim SL1 setups reach TP1 within 1 candle, 32% within 10 (live 21% of 19); SL1 +0.5 ATR → sim +341 (thirds +167 / -1 / +174), live +20.1
- MES 5m: 5% of sim SL1 setups reach TP1 within 1 candle, 26% within 10 (live 36% of 25); SL1 +0.5 ATR → sim +152 (thirds +117 / +13 / +22), live -1.7

✓ = better in all three thirds, ⚠ = worse in all three thirds. Stop widths and minimums also change position size / risk per trade, which this does not account for.
