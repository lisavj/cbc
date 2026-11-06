# MES 3m chart EMA + SL/TP grid — Wed 11/04/2026 07:47

MES 3m chart (LTF) EMA + SL/TP grid study -- 11/04/2026.

Question: with chart EMAs 7 / 14, 7 / 16 or 6 / 14 instead of 9 / 20 (CBC v10.50 "Chart EMA fast / slow / 200"), how does
MES 3m do on the live exits (v10.54: SL1 3.0 ATR min 5, TP1 1.75 ATR, no caps; close at TP1 80 % 06:00-16:00 and
18:00-22:30 ET with BE + trail 1.7, else 100 %), and is SL 3 / TP1 1.75 still the best stop / target with each EMA set?
Engine: chop_sim (HTF CBC Flip with live flip gates, LTF EMA20 Pierce on the SLOW chart EMA, HTF EMA9 / EMA20 Pierce, 1-bar
late; ER 0.23 chop rule + breakout exception; VWAP bounce block; cooldown 10; opening-range windows; range gate 24 bars /
5 ATR ON; toward HTF flips off, late-away OFF on MES 3m (v10.60)). Only the SLOW chart EMA changes the replay -- the fast EMA
only feeds the cloud / "price past both EMA clouds" gate, which is not modelled -- so 7 / 14 and 6 / 14 replay the same.
Data: server archive MES 3m (Databento rebuild + BarFeed) Jan 5 -> now. ~50 % exact match with live setups: compare
variants, not totals. z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds
(Jan-Mar / Apr-Jun / Jul-now); promising = z >= 1 and all three better.
Usage: python3 mes3_ema_grid.py   (needs chop_sim.py next to it)

Data: 99360 candles, 01/04 → 11/04. Thirds: 01/05–04/16 / 04/16–07/26 / 07/26–11/04.

## A. Chart EMA, live MES 3m exits (SL 3 / TP1 1.75 / time-of-day 80-100 %)

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 9 / 20 | z | Δ by third | Verdict | By trigger (setups / net) |
|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (current) | 1684 | 49% | -124 | -0.07 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 309 / -255 · LTF20 953 / +110 · HTF9 262 / -43 · HTF20 160 / +64 |
| 7 / 14 and 6 / 14 | 1916 | 50% | +169 | +0.09 | +293 | +1.1 | -7 / +78 / +222 | noise | Flip 322 / -203 · LTF20 1189 / +341 · HTF9 254 / -30 · HTF20 151 / +61 |
| 7 / 16 | 1830 | 50% | +90 | +0.05 | +214 | +0.9 | -18 / +122 / +110 | noise | Flip 319 / -226 · LTF20 1090 / +294 · HTF9 265 / -37 · HTF20 156 / +60 |

## A. Chart EMA, base exits (SL 1.7 + min 5 cap 8 / TP1 1.7 cap 6 / 80 % + BE + trail)

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 9 / 20 | z | Δ by third | Verdict | By trigger (setups / net) |
|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (current) | 1703 | 50% | -3 | -0.00 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 309 / +61 · LTF20 935 / +49 · HTF9 282 / -115 · HTF20 177 / +1 |
| 7 / 14 and 6 / 14 | 1928 | 51% | +149 | +0.08 | +152 | +0.8 | -55 / +79 / +127 | noise | Flip 322 / +70 · LTF20 1147 / +211 · HTF9 288 / -140 · HTF20 171 / +7 |
| 7 / 16 | 1842 | 52% | +218 | +0.12 | +221 | +1.4 | -55 / +172 / +104 | noise | Flip 319 / +66 · LTF20 1051 / +237 · HTF9 297 / -106 · HTF20 175 / +21 |

## B. SL / TP1 grid — chart EMA 9 / 20 (current) (net pts; ✱ both halves +, T all three thirds +, R = T and every ±1-step stop / TP neighbour +)

**Close at TP1: live 80/100 % by time**

| Stop \ TP1 | 1.25 ATR | 1.50 ATR | 1.75 ATR | 2.00 ATR | 2.50 ATR |
|---|---|---|---|---|---|
| 1.7 ATR | +0 | -5 | -128 | -52 | -46 |
| 2.0 ATR | +49 | +67 | -78 | -17 | -45 |
| 2.5 ATR | +43 ✱ | +40 | -113 | -80 | -68 |
| 3.0 ATR | +33 | +16 | -124 | -109 | -148 |
| 3.5 ATR | +147 ✱ | +116 ✱ | -9 | +21 | -3 |

**Close at TP1: 100 %**

| Stop \ TP1 | 1.25 ATR | 1.50 ATR | 1.75 ATR | 2.00 ATR | 2.50 ATR |
|---|---|---|---|---|---|
| 1.7 ATR | +23 | +33 | -60 | +6 | +43 |
| 2.0 ATR | +59 | +98 ✱ | -27 | +22 | +49 |
| 2.5 ATR | +55 ✱ | +87 ✱ | -48 | -33 | +32 |
| 3.0 ATR | +44 | +58 ✱ | -48 | -48 | -45 |
| 3.5 ATR | +151 ✱ | +152 ✱ | +66 | +75 ✱ | +93 |

**Close at TP1: 80 % + BE + trail**

| Stop \ TP1 | 1.25 ATR | 1.50 ATR | 1.75 ATR | 2.00 ATR | 2.50 ATR |
|---|---|---|---|---|---|
| 1.7 ATR | -79 | -72 | -197 | -103 | -86 |
| 2.0 ATR | -33 | -4 | -157 | -75 | -92 |
| 2.5 ATR | -35 | -24 | -187 | -135 | -112 |
| 3.0 ATR | -47 | -49 | -204 | -155 | -190 |
| 3.5 ATR | +61 ✱ | +44 ✱ | -100 | -40 | -48 |

Current live (3.0 / 1.75 / time of day): -124, 1684 setups, win 49%.
Top 5: SL 3.5 / TP1 1.50 / 100 % = +152 (win 54%); SL 3.5 / TP1 1.25 / 100 % = +151 (win 58%); SL 3.5 / TP1 1.25 / live 80/100 % by time = +147 (win 58%); SL 3.5 / TP1 1.50 / live 80/100 % by time = +116 (win 54%); SL 2.0 / TP1 1.50 / 100 % = +98 (win 51%)
Robust cells: 0 of 75.

## B. SL / TP1 grid — chart EMA 7 / 14 and 6 / 14 (net pts; ✱ both halves +, T all three thirds +, R = T and every ±1-step stop / TP neighbour +)

**Close at TP1: live 80/100 % by time**

| Stop \ TP1 | 1.25 ATR | 1.50 ATR | 1.75 ATR | 2.00 ATR | 2.50 ATR |
|---|---|---|---|---|---|
| 1.7 ATR | +78 ✱ | +227 ✱ | +189 ✱ | +181 ✱ | +126 |
| 2.0 ATR | +142 ✱ | +327 ✱ | +278 ✱ | +249 ✱ | +168 ✱ |
| 2.5 ATR | +187 | +298 | +237 ✱ | +181 | +160 |
| 3.0 ATR | +119 | +204 | +169 ✱ | +93 | +21 |
| 3.5 ATR | +196 | +264 | +244 ✱ | +176 ✱ | +117 ✱ |

**Close at TP1: 100 %**

| Stop \ TP1 | 1.25 ATR | 1.50 ATR | 1.75 ATR | 2.00 ATR | 2.50 ATR |
|---|---|---|---|---|---|
| 1.7 ATR | +137 ✱ | +260 ✱ | +184 ✱ | +170 ✱ | +214 |
| 2.0 ATR | +181 ✱ | +346 ✱ | +272 ✱ | +243 ✱ | +259 ✱ |
| 2.5 ATR | +190 | +319 ✱ | +236 ✱ | +166 | +235 ✱ |
| 3.0 ATR | +114 | +216 ✱ | +156 ✱ | +65 | +84 |
| 3.5 ATR | +191 ✱ | +279 ✱ | +232 | +143 | +165 |

**Close at TP1: 80 % + BE + trail**

| Stop \ TP1 | 1.25 ATR | 1.50 ATR | 1.75 ATR | 2.00 ATR | 2.50 ATR |
|---|---|---|---|---|---|
| 1.7 ATR | +55 | +215 ✱ | +206 ✱ | +193 ✱ | +150 |
| 2.0 ATR | +111 | +308 ✱ | +286 ✱ | +255 ✱ | +208 ✱ |
| 2.5 ATR | +153 | +282 | +248 ✱ | +199 ✱ | +214 ✱ |
| 3.0 ATR | +62 | +171 | +163 ✱ | +122 ✱ | +85 |
| 3.5 ATR | +135 | +230 | +232 ✱ | +197 ✱ | +178 ✱ |

Current live (3.0 / 1.75 / time of day): +169, 1916 setups, win 50%.
Top 5: SL 2.0 / TP1 1.50 / 100 % = +346 (win 52%); SL 2.0 / TP1 1.50 / live 80/100 % by time = +327 (win 53%); SL 2.5 / TP1 1.50 / 100 % = +319 (win 54%); SL 2.0 / TP1 1.50 / 80 % + BE + trail = +308 (win 53%); SL 2.5 / TP1 1.50 / live 80/100 % by time = +298 (win 54%)
Robust cells: 0 of 75.

## B. SL / TP1 grid — chart EMA 7 / 16 (net pts; ✱ both halves +, T all three thirds +, R = T and every ±1-step stop / TP neighbour +)

**Close at TP1: live 80/100 % by time**

| Stop \ TP1 | 1.25 ATR | 1.50 ATR | 1.75 ATR | 2.00 ATR | 2.50 ATR |
|---|---|---|---|---|---|
| 1.7 ATR | +163 ✱ | +213 ✱ | +88 | +72 | +72 |
| 2.0 ATR | +263 ✱ | +349 ✱ | +198 ✱ | +192 ✱ | +155 ✱ |
| 2.5 ATR | +290 ✱ | +296 ✱ | +130 ✱ | +102 | +111 ✱ |
| 3.0 ATR | +254 ✱ | +234 ✱ | +90 ✱ | +61 ✱ | +25 |
| 3.5 ATR | +327 ✱ | +290 ✱ | +161 ✱ | +145 ✱ | +116 ✱ |

**Close at TP1: 100 %**

| Stop \ TP1 | 1.25 ATR | 1.50 ATR | 1.75 ATR | 2.00 ATR | 2.50 ATR |
|---|---|---|---|---|---|
| 1.7 ATR | +207 ✱ | +267 ✱ | +107 ✱ | +111 | +119 |
| 2.0 ATR | +314 ✱ | +419 ✱ | +224 ✱ | +248 ✱ | +213 ✱ |
| 2.5 ATR | +330 ✱ | +366 ✱ | +164 ✱ | +157 ✱ | +156 ✱ |
| 3.0 ATR | +273 ✱ | +285 ✱ | +102 ✱ | +95 | +45 |
| 3.5 ATR | +348 ✱ | +346 ✱ | +175 ✱ | +169 | +126 |

**Close at TP1: 80 % + BE + trail**

| Stop \ TP1 | 1.25 ATR | 1.50 ATR | 1.75 ATR | 2.00 ATR | 2.50 ATR |
|---|---|---|---|---|---|
| 1.7 ATR | +147 ✱ | +200 ✱ | +83 ✱ | +66 | +89 ✱ |
| 2.0 ATR | +242 ✱ | +332 ✱ | +184 ✱ | +174 ✱ | +176 ✱ |
| 2.5 ATR | +264 ✱ | +276 ✱ | +107 ✱ | +75 | +126 ✱ |
| 3.0 ATR | +233 ✱ | +225 | +73 ✱ | +62 ✱ | +61 |
| 3.5 ATR | +304 ✱ | +280 ✱ | +137 | +135 | +152 ✱ |

Current live (3.0 / 1.75 / time of day): +90, 1830 setups, win 50%.
Top 5: SL 2.0 / TP1 1.50 / 100 % = +419 (win 53%); SL 2.5 / TP1 1.50 / 100 % = +366 (win 54%); SL 2.0 / TP1 1.50 / live 80/100 % by time = +349 (win 53%); SL 3.5 / TP1 1.25 / 100 % = +348 (win 60%); SL 3.5 / TP1 1.50 / 100 % = +346 (win 55%)
Robust cells: 0 of 75.

## Summary

- 7 / 14 and 6 / 14, live exits: Δ +293, z +1.1, thirds -7 / +78 / +222 (noise); last 4 weeks Δ +134.1
- 7 / 16, live exits: Δ +214, z +0.9, thirds -18 / +122 / +110 (noise); last 4 weeks Δ +79.1
- 7 / 14 and 6 / 14, base exits: Δ +152, z +0.8, thirds -55 / +79 / +127 (noise); last 4 weeks Δ +79.0
- 7 / 16, base exits: Δ +221, z +1.4, thirds -55 / +172 / +104 (noise); last 4 weeks Δ +39.3
- Grid best vs current live exits: 9 / 20 (current): best SL 3.5 / TP1 1.50 / 100 % +152 vs current -124; 7 / 14 and 6 / 14: best SL 2.0 / TP1 1.50 / 100 % +346 vs current +169; 7 / 16: best SL 2.0 / TP1 1.50 / 100 % +419 vs current +90

## Thirds and last 4 weeks for key cells (check run)

Thirds = Jan 5–Apr 15 / Apr 15–Jul 25 / Jul 25–Nov 3 (equal time). The middle third is negative for EVERY cell, so no cell can be "robust".

| Slow EMA | SL / TP1 / close | Setups | Net | Thirds | Last 4 wk |
|---|---|---|---|---|---|
| 20 | 3.0 / 1.75 / live (current) | 1684 | -124 | +230 / -473 / +119 | +114 |
| 20 | 3.0 / 1.50 / live | 1715 | +16 | +219 / -359 / +156 | +117 |
| 20 | 2.0 / 1.50 / 100 % | 1794 | +98 | +300 / -364 / +162 | +127 |
| 14 | 3.0 / 1.75 / live | 1916 | +169 | +223 / -395 / +341 | +248 |
| 14 | 2.0 / 1.50 / 100 % | 2131 | +346 | +311 / -227 / +262 | +165 |
| 16 | 3.0 / 1.75 / live | 1830 | +90 | +212 / -351 / +229 | +193 |
| 16 | 2.0 / 1.50 / 100 % | 1996 | +419 | +370 / -199 / +248 | +144 |

## Verdict (11/04/2026)

- Slow chart EMA 14 or 16 beats 20 on MES 3m with both exit sets (+150 to +290 pts over 10 months, last 4 weeks +40 to +134), almost all of it from more / better LTF EMA20 Pierce setups. Not robust: z 0.8–1.4 and Jan–Mar is slightly worse. 7 / 14 and 6 / 14 are the same replay (fast EMA not modelled). Watch, don't change yet. If it holds: "...slow EMA per symbol/timeframe" = "MES 2m 14, MES 3m 14" (input only).
- Exits: across all three EMA sets TP1 1.50 ATR beats 1.75 at almost every stop; SL 2.0 / TP1 1.50 / 100 % is the top cell with slow 14 and 16. The current 3.0 / 1.75 is mid-pack (and one of the weakest cells with 9 / 20 over 10 months), though it is positive in the last 4 weeks, matching the 10/19–11/02 live grid that chose it. No cell is robust (middle third negative everywhere), so no exit change on this evidence.
