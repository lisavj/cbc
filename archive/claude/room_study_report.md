# Room-to-resistance study — first run 10/29/2026 (check 1)

Live check 10/29 (real alerts 10/19-10/29, mixed exit versions): MES 3m level/OB inside 0.5x TP1 48 setups -57.8 (h -37.3 / -20.4); MGC 3m opposing OB before TP1 18 setups -1.63/setup vs +0.33; MGC 2m flip flop warning 42 setups -1.13 vs +0.30; MGC 3m 15m cloud against 16 setups -1.40 vs +0.05. Sim (below, Jan-Oct, no order blocks in the pool) does NOT confirm the room gate on any case -- keep the CBC v10.47 room gate / TP1 option OFF; logging only.

Room-to-resistance study (CBC v10.47 "room" gate / TP1-before-level option) -- MGC 3m, MES 3m, MGC 2m, MES 2m.

Question: does a setup whose first opposing level sits close in front of TP1 do worse, and would CBC do better by
(a) skipping setups with the first opposing level within x * TP1 ("Skip setup if the first opposing level / OB is within
x x TP1"), or (b) moving TP1 to just before that level ("TP1 just before the first opposing level", min 0.5 / 1.0 ATR)?
Origin: 10/29 live check -- MES 3m setups with a level inside half the TP1 distance -1.77/setup vs +0.07; MGC 3m with an
opposing OB before TP1 -1.63 vs +0.33 (both halves).

Simulator: chop_sim.py (CBC-style setup engine, current ER/breakout rule, R5/X4/MTF gates), with the BASE exits on every
case (SL1 1.7 ATR + min 5, TP1 1.7 ATR capped at 6 pts, 80 % at TP1, breakeven, trail 1.7 ATR -- live on all charts since
CBC v10.45). Level pool per bar = classic PP/R1/S1, prior-day H/L, NY/London/Asia opening-range H/L, VWAP, EMA200, last LTF
swing H/L (N=2) and last HTF swing H/L (N=2 on the HTF candles). Lux order blocks are NOT in the sim pool (live alerts have
them) -- so the sim under-counts close levels a little. ~50 % exact match with real setups: compare variants, not totals.
z = change / (per-trade SD x sqrt(setups changed)); "robust" = z >= 2 and better in all three thirds; "promising" = z >= 1
and better in all three thirds. Usage: python3 room_study.py  (needs chop_sim.py next to it; downloads the bar archive).

## MGC 3m — 01/05 to 10/29 · current (base exits, no room rule): 1146 setups, net +222 (thirds +161 / +2 / +58), SD 5.7

**Current setups by room to the first opposing level (x TP1)**

| Room | N | Win % | Net | Avg |
|---|---|---|---|---|
| < 0.25 | 396 | 50% | +96 | +0.24 |
| 0.25–0.5 | 262 | 46% | -5 | -0.02 |
| 0.5–0.75 | 149 | 53% | +67 | +0.45 |
| 0.75–1 | 115 | 46% | -55 | -0.48 |
| >= 1 / none | 222 | 56% | +132 | +0.60 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| Skip if room < 0.25 x TP1 | 823 | +184 | -37 | -0.3 | -65 / +72 / -45 | worse |
| Skip if room < 0.5 x TP1 | 561 | +201 | -21 | -0.1 | -81 / +135 / -75 | worse |
| Skip if room < 0.75 x TP1 | 386 | +71 | -150 | -0.9 | -126 / +93 / -117 | worse |
| Skip if room < 1.0 x TP1 | 261 | +138 | -83 | -0.5 | -101 / +95 / -78 | worse |
| TP1 just before the level (min 0.5 ATR) | 1155 | +182 | -39 | -2.3 | -16 / +21 / -45 | worse |
| TP1 just before the level (min 1.0 ATR) | 1151 | +216 | -6 | -0.4 | +6 / -17 / +5 | worse |
| Skip if room < 0.25 x TP1 + TP1 before the level (min 0.5 ATR) | 829 | +109 | -112 | -0.9 | -86 / +72 / -99 | worse |

## MES 3m — 01/05 to 10/29 · current (base exits, no room rule): 1672 setups, net -10 (thirds +123 / -214 / +81), SD 5.0

**Current setups by room to the first opposing level (x TP1)**

| Room | N | Win % | Net | Avg |
|---|---|---|---|---|
| < 0.25 | 472 | 49% | -26 | -0.06 |
| 0.25–0.5 | 391 | 50% | +90 | +0.23 |
| 0.5–0.75 | 285 | 49% | +20 | +0.07 |
| 0.75–1 | 160 | 51% | +26 | +0.16 |
| >= 1 / none | 351 | 51% | -108 | -0.31 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| Skip if room < 0.25 x TP1 | 1306 | +69 | +79 | +0.7 | -11 / +45 / +45 | noise |
| Skip if room < 0.5 x TP1 | 918 | -120 | -110 | -0.7 | -112 / +47 / -45 | worse |
| Skip if room < 0.75 x TP1 | 601 | -68 | -57 | -0.3 | -111 / +101 / -47 | worse |
| Skip if room < 1.0 x TP1 | 416 | -33 | -23 | -0.1 | -136 / +191 / -78 | worse |
| TP1 just before the level (min 0.5 ATR) | 1713 | -76 | -66 | -1.9 | -43 / +11 / -34 | worse |
| TP1 just before the level (min 1.0 ATR) | 1680 | +21 | +31 | +2.2 | -8 / +33 / +6 | noise |
| Skip if room < 0.25 x TP1 + TP1 before the level (min 0.5 ATR) | 1336 | -52 | -41 | -0.3 | -61 / +49 / -30 | worse |

## MGC 2m — 06/01 to 10/29 · current (base exits, no room rule): 1421 setups, net +364 (thirds +83 / +130 / +151), SD 4.9

**Current setups by room to the first opposing level (x TP1)**

| Room | N | Win % | Net | Avg |
|---|---|---|---|---|
| < 0.25 | 431 | 55% | +258 | +0.60 |
| 0.25–0.5 | 297 | 53% | +55 | +0.18 |
| 0.5–0.75 | 177 | 50% | +2 | +0.01 |
| 0.75–1 | 155 | 49% | +19 | +0.12 |
| >= 1 / none | 336 | 50% | +17 | +0.05 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–now) | Verdict |
|---|---|---|---|---|---|---|
| Skip if room < 0.25 x TP1 | 1086 | +185 | -179 | -1.6 | -34 / -78 / -67 | worse |
| Skip if room < 0.5 x TP1 | 787 | +107 | -257 | -1.8 | +44 / -126 / -174 | worse |
| Skip if room < 0.75 x TP1 | 578 | +54 | -309 | -2.0 | -105 / -65 / -140 | worse |
| Skip if room < 1.0 x TP1 | 402 | +56 | -307 | -1.9 | -127 / -50 / -130 | worse |
| TP1 just before the level (min 0.5 ATR) | 1449 | +362 | -2 | -0.1 | -50 / +39 / +9 | worse |
| TP1 just before the level (min 1.0 ATR) | 1425 | +328 | -35 | -3.6 | -31 / -3 / -1 | worse |
| Skip if room < 0.25 x TP1 + TP1 before the level (min 0.5 ATR) | 1115 | +151 | -213 | -1.8 | -91 / -63 / -59 | worse |

## MES 2m — 06/01 to 10/29 · current (base exits, no room rule): 1159 setups, net -195 (thirds -103 / +80 / -172), SD 4.4

**Current setups by room to the first opposing level (x TP1)**

| Room | N | Win % | Net | Avg |
|---|---|---|---|---|
| < 0.25 | 306 | 45% | -109 | -0.36 |
| 0.25–0.5 | 278 | 54% | +41 | +0.15 |
| 0.5–0.75 | 174 | 49% | -15 | -0.09 |
| 0.75–1 | 129 | 49% | +16 | +0.12 |
| >= 1 / none | 258 | 47% | -149 | -0.58 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–now) | Verdict |
|---|---|---|---|---|---|---|
| Skip if room < 0.25 x TP1 | 945 | -169 | +26 | +0.3 | +13 / -21 / +34 | noise |
| Skip if room < 0.5 x TP1 | 701 | -188 | +7 | +0.1 | -18 / -54 / +79 | noise |
| Skip if room < 0.75 x TP1 | 497 | -176 | +20 | +0.1 | +1 / -52 / +70 | noise |
| Skip if room < 1.0 x TP1 | 331 | -123 | +73 | +0.5 | +4 / -57 / +126 | noise |
| TP1 just before the level (min 0.5 ATR) | 1190 | -164 | +31 | +1.1 | -11 / +15 / +26 | noise |
| TP1 just before the level (min 1.0 ATR) | 1167 | -189 | +7 | +0.5 | -5 / +9 / +3 | noise |
| Skip if room < 0.25 x TP1 + TP1 before the level (min 0.5 ATR) | 968 | -115 | +80 | +0.9 | +3 / -2 / +80 | noise |

## Candidates (robust / promising)

- none
