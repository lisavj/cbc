MES 3m chart EMA 7 / 16 vs 9 / 20 on the CBC EMA Slope branch (CBC-ES v1.04) -- 11/14/2026.
Branch baseline = mes_next_study baseline (ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR, HTF EMA20 slope >= 0.3 ATR
|15m EMA20 now - 12 bars ago| / ATR) + exits SL1 3 ATR min 5, TP1 1.75 ATR, 100 % at TP1, and HTF CBC Flip setups ride
to the HTF flip back / SL1 / 16:00 / next setup (no TP, branch item 2). Replay Jan 5 -> now, net after 0.50 cost.
Only the SLOW chart EMA changes the replay (LTF EMA20 Pierce line, flip distance); the fast EMA (7 vs 9) only feeds the
cloud / "closed beyond EMA9" text, which is not modelled. Slow EMA is recomputed from closes for every variant (20 too).
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, all three thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds.

Data: 102745 candles, 01/05 → 11/13. Thirds 01/05–04/19 / 04/19–08/01 / 08/01–11/13. Last 4 weeks from 10/16.

## A. Branch settings (slope 0.3 + flip ride), TP1 1.75

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 9/20 | z | Δ by third | Δ last 4 wk | RTH net | Max DD | Verdict | By trigger (n / net) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (current) | 1242 | 48 % | +63 | +0.05 | +0 | +0.0 | +0 / +0 / +0 | +127 | -129 | 476 | baseline | Flip 169 / +74 · LTF20 813 / -67 · HTF9 211 / -36 · HTF20 49 / +93 |
| 7 / 16 | 1453 | 49 % | +24 | +0.02 | -39 | -0.1 | -31 / -32 / +24 | -7 | -47 | 516 | worse | Flip 178 / +25 · LTF20 1026 / -50 · HTF9 200 / -72 · HTF20 49 / +121 |
| 7 / 14 | 1594 | 49 % | -81 | -0.05 | -144 | -0.4 | -99 / +43 / -88 | -72 | -10 | 512 | worse | Flip 180 / -15 · LTF20 1163 / -147 · HTF9 202 / -48 · HTF20 49 / +129 |

(9 / 20 row: "Δ last 4 wk" column = its own last-4-week net.)

## B. Branch settings, TP1 1.5

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 9/20 | z | Δ by third | Δ last 4 wk | RTH net | Max DD | Verdict | By trigger (n / net) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (current) | 1261 | 51 % | +93 | +0.07 | +0 | +0.0 | +0 / +0 / +0 | +120 | -106 | 406 | baseline | Flip 169 / +87 · LTF20 824 / -27 · HTF9 216 / -38 · HTF20 52 / +71 |
| 7 / 16 | 1475 | 53 % | +45 | +0.03 | -48 | -0.2 | +6 / -32 / -22 | -20 | +9 | 459 | worse | Flip 178 / +27 · LTF20 1039 / +2 · HTF9 205 / -75 · HTF20 53 / +90 |
| 7 / 14 | 1615 | 52 % | -136 | -0.08 | -229 | -0.7 | -57 / -3 / -169 | -94 | -11 | 473 | worse | Flip 180 / -3 · LTF20 1175 / -172 · HTF9 207 / -71 · HTF20 53 / +109 |

(9 / 20 row: "Δ last 4 wk" column = its own last-4-week net.)

## C. Without the branch changes (v10.97 settings: no slope filter, flip setups use TP1)

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 9/20 | z | Δ by third | Δ last 4 wk | RTH net | Max DD | Verdict | By trigger (n / net) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (current) | 1799 | 48 % | -839 | -0.47 | +0 | +0.0 | +0 / +0 / +0 | +70 | -378 | 1069 | baseline | Flip 319 / -388 · LTF20 999 / -249 · HTF9 311 / -190 · HTF20 170 / -12 |
| 7 / 16 | 1998 | 49 % | -798 | -0.40 | +41 | +0.2 | -53 / +19 / +75 | +17 | -305 | 1079 | noise | Flip 330 / -353 · LTF20 1197 / -254 · HTF9 304 / -191 · HTF20 167 / +0 |
| 7 / 14 | 2140 | 49 % | -881 | -0.41 | -41 | -0.1 | -90 / +17 / +32 | -49 | -317 | 1137 | worse | Flip 333 / -329 · LTF20 1352 / -395 · HTF9 296 / -153 · HTF20 159 / -4 |

(9 / 20 row: "Δ last 4 wk" column = its own last-4-week net.)

## 11/11 rally (10:00-14:30 ET), branch settings: setups per slow EMA

- slow 20: 14:03 L HTF9 -8.00
- slow 16: 11:09 L LTF20 +10.94, 13:03 L LTF20 +6.54, 13:54 L LTF20 -10.65
- slow 16 raw triggers in the window: 10:42 L Flip (ER 0.26, range blk, slope 0.11), 11:09 L LTF20 (ER 0.35, range ok, slope 0.63), 13:03 L LTF20 (ER 0.10, range ok, slope 1.97), 13:54 L LTF20 (ER 0.23, range ok, slope 1.80), 14:03 L HTF9 (ER 0.38, range ok, slope 1.85)

## Check: baseline with the TradingView EMA20 from the bar feed (= project numbers)

- Branch settings: +138 (mes_next 4a: +138). v10.97 settings: -801 (tsf / mes_next: -801).
- The recomputed EMA20 baseline is lower (+63 / -839), the gap is all in the last third (BarFeed period). Variants are compared to the recomputed 20 so all three use the same EMA method; against the TV-EMA20 baseline 7 / 16 is worse still.