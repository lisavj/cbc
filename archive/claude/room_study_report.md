# Room-to-resistance study — weekly check 4, rerun after data repair (replaces the 11/06 run) — 2026-11-07 09:52 ET

## Since last week (vs check 3, 10/30) and vs the pre-repair 11/06 run

Manual rerun of the 11/06 check after the BarFeed bar repair (MGC 3m had 5m candles mixed in; MES 2m and others had gaps); it replaces the 11/06 run, so this is still check 4 for the consecutive-check count (0 robust variants either way). Same data window: 34,777 alerts (10/19 → 11/06 5:01 PM ET, was 21,407 to 10/30), bars to 11/06. The live splits come from the alerts, so they are unchanged by the repair (check-3 values are in the 11/06 report history: MES 3m L5 was -0.89 vs +1.07, MGC 3m OB -1.63 vs -0.39, MGC 2m FL -1.19 vs +0.56, MGC 3m CL -1.95 vs -0.19). The sim moved with the repaired bars, mostly in Jul–now; "was" below = pre-repair 11/06 run (MGC 3m current +278, was +186; MES 3m +16, was -22; MGC 2m +340, was +365; MES 2m -194, was -203). Live = real alerts 10/19–11/06 (mixed exit versions), avg/setup with flag vs without; halves = net of the flagged group in the first / second half of that case's setups. Sim = Jan–Nov 6 (2m: Jun–Nov 6), base exits, **no order blocks in the sim pool**.

| Case (setups, net) | L5 (room < 0.5x TP1) | OB before TP1 | Flip-flop warning | 15m cloud against | Best sim variant (Δ, z, thirds) |
|---|---|---|---|---|---|
| MGC 3m (67, -34.2; unchanged) | 51: -0.56 vs -0.36 (h -5.8 / -22.6) — no edge | 24: **-1.00** vs -0.24 (h -18.8 / -5.3) — unchanged, both halves neg. | 39: -0.39 vs -0.68 — no | 26: **-1.32** vs +0.00 (h -11.8 / -22.5) — unchanged | TP1 before level min 1.0 ATR: -6, z -0.5 (+6/-17/+5) — all variants worse (was -3) |
| MES 3m (103, +9.4; unchanged) | 69: **-0.79** vs **+1.88** (h -46.0 / -8.4) — unchanged | 36: +0.55 vs -0.15 — no | 65: +0.66 vs -0.88 — no | 25: +0.70 vs -0.10 — no | TP1 before level min 1.0 ATR: +30, z +2.1, thirds -8/+33/+5 → noise (same); Skip < 0.25x +91, z +0.7, noise (was +94) |
| MGC 2m (144, -63.8; unchanged) | 107: -0.43 vs -0.48 — no | 67: -0.29 vs -0.57 — no | 65: **-1.27** vs +0.24 (h -27.0 / -55.3) — unchanged | 42: -0.48 vs -0.43 — no | TP1 before level min 0.5 ATR: -3, z -0.1 (was -8); room gates clearly worse (-181 to -291) |
| MES 2m (116, -83.1; unchanged) | 71: -0.61 vs -0.89 — no | 40: -0.23 vs -0.97 — no | 46: **-1.79** vs -0.01 (h -57.0 / -25.4) — unchanged | 13: -2.42 vs -0.50 — < 20 | Skip < 0.25x + TP1 before: +52, z +0.5, thirds +3/-2/+52 → noise (was +58) |

**Logged CBC v10.47 Room line** (unchanged by the repair; Room line logged since 10/29–10/30; N / net):

| Case | With Room line | < 0.25 | 0.25–0.5 | 0.5–1 | ≥ 1 / none |
|---|---|---|---|---|---|
| MGC 3m | 23 | 10 / -3.9 | 9 / -13.2 | 0 | 4 / +3.8 |
| MES 3m | 33 | 13 / -1.2 | 8 / +4.5 | 8 / +45.5 | 4 / +27.3 |
| MGC 2m | 63 | 28 / +9.0 | 17 / -20.4 | 6 / -1.5 | 12 / -15.2 |
| MES 2m | 39 | 11 / +27.0 | 9 / +11.7 | 9 / +1.3 | 10 / +3.5 |

**Verdict: keep both room settings OFF on all four charts** ("Skip setup if the first opposing level / OB is within x × TP1" empty, "TP1 just before the first opposing level" off). No sim variant has been robust on any case in any of the 4 checks, so rule (a) fails everywhere.

**Live holds while the sim disagrees (unchanged):** MES 3m L5 meets rule (b) on its own (69 vs 34, -0.79 vs +1.88, both halves negative) but the sim says "Skip if room < 0.5 x TP1" on MES 3m is worse (-103, z -0.6); MGC 3m OB (24 vs 43, -1.00 vs -0.24, both halves) cannot be tested in the sim. Suggested next step (not done): add OB levels from claude/ob_sim.py to the sim's level pool and rerun MES 3m and MGC 3m. Strongest non-room live splits still: MGC 2m and MES 2m flip-flop warning, MGC 3m 15m cloud against.

---

# Room-to-resistance study — 2026-11-07 09:52 ET (rerun after data repair)

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

## MGC 3m — 01/05 to 11/06 · current (base exits, no room rule): 1180 setups, net +278 (thirds +161 / +2 / +114), SD 5.7

**Current setups by room to the first opposing level (x TP1)**

| Room | N | Win % | Net | Avg |
|---|---|---|---|---|
| < 0.25 | 409 | 51% | +137 | +0.33 |
| 0.25–0.5 | 269 | 46% | -19 | -0.07 |
| 0.5–0.75 | 152 | 53% | +83 | +0.55 |
| 0.75–1 | 115 | 46% | -57 | -0.49 |
| >= 1 / none | 233 | 56% | +147 | +0.63 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| Skip if room < 0.25 x TP1 | 847 | +191 | -86 | -0.7 | -65 / +72 / -94 | worse |
| Skip if room < 0.5 x TP1 | 576 | +235 | -43 | -0.3 | -81 / +135 / -97 | worse |
| Skip if room < 0.75 x TP1 | 399 | +82 | -195 | -1.2 | -126 / +93 / -162 | worse |
| Skip if room < 1.0 x TP1 | 273 | +146 | -132 | -0.7 | -101 / +95 / -126 | worse |
| TP1 just before the level (min 0.5 ATR) | 1190 | +237 | -40 | -2.2 | -16 / +21 / -46 | worse |
| TP1 just before the level (min 1.0 ATR) | 1185 | +272 | -6 | -0.5 | +6 / -17 / +5 | worse |
| Skip if room < 0.25 x TP1 + TP1 before the level (min 0.5 ATR) | 853 | +109 | -168 | -1.3 | -86 / +72 / -154 | worse |

## MES 3m — 01/05 to 11/06 · current (base exits, no room rule): 1719 setups, net +16 (thirds +123 / -214 / +107), SD 5.1

**Current setups by room to the first opposing level (x TP1)**

| Room | N | Win % | Net | Avg |
|---|---|---|---|---|
| < 0.25 | 482 | 48% | -53 | -0.11 |
| 0.25–0.5 | 399 | 51% | +121 | +0.30 |
| 0.5–0.75 | 293 | 49% | +9 | +0.03 |
| 0.75–1 | 167 | 51% | +42 | +0.25 |
| >= 1 / none | 365 | 51% | -90 | -0.25 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| Skip if room < 0.25 x TP1 | 1347 | +107 | +91 | +0.7 | -11 / +45 / +57 | noise |
| Skip if room < 0.5 x TP1 | 949 | -87 | -103 | -0.6 | -112 / +47 / -39 | worse |
| Skip if room < 0.75 x TP1 | 625 | -17 | -33 | -0.2 | -111 / +101 / -23 | worse |
| Skip if room < 1.0 x TP1 | 435 | -6 | -21 | -0.1 | -136 / +191 / -76 | worse |
| TP1 just before the level (min 0.5 ATR) | 1760 | -65 | -81 | -2.3 | -43 / +11 / -49 | worse |
| TP1 just before the level (min 1.0 ATR) | 1727 | +46 | +30 | +2.1 | -8 / +33 / +5 | noise |
| Skip if room < 0.25 x TP1 + TP1 before the level (min 0.5 ATR) | 1377 | -29 | -44 | -0.3 | -61 / +49 / -33 | worse |

## MGC 2m — 06/01 to 11/06 · current (base exits, no room rule): 1499 setups, net +340 (thirds +83 / +130 / +127), SD 4.9

**Current setups by room to the first opposing level (x TP1)**

| Room | N | Win % | Net | Avg |
|---|---|---|---|---|
| < 0.25 | 452 | 54% | +249 | +0.55 |
| 0.25–0.5 | 316 | 52% | +24 | +0.08 |
| 0.5–0.75 | 188 | 51% | +8 | +0.04 |
| 0.75–1 | 162 | 50% | +34 | +0.21 |
| >= 1 / none | 351 | 50% | +22 | +0.06 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–now) | Verdict |
|---|---|---|---|---|---|---|
| Skip if room < 0.25 x TP1 | 1150 | +159 | -181 | -1.6 | -34 / -78 / -69 | worse |
| Skip if room < 0.5 x TP1 | 833 | +105 | -235 | -1.6 | +44 / -126 / -153 | worse |
| Skip if room < 0.75 x TP1 | 611 | +56 | -285 | -1.8 | -105 / -65 / -115 | worse |
| Skip if room < 1.0 x TP1 | 426 | +49 | -291 | -1.7 | -127 / -50 / -114 | worse |
| TP1 just before the level (min 0.5 ATR) | 1528 | +337 | -3 | -0.1 | -50 / +39 / +8 | worse |
| TP1 just before the level (min 1.0 ATR) | 1503 | +299 | -41 | -4.2 | -31 / -3 / -7 | worse |
| Skip if room < 0.25 x TP1 + TP1 before the level (min 0.5 ATR) | 1179 | +117 | -223 | -1.9 | -91 / -63 / -69 | worse |

## MES 2m — 06/01 to 11/06 · current (base exits, no room rule): 1226 setups, net -194 (thirds -103 / +80 / -170), SD 4.5

**Current setups by room to the first opposing level (x TP1)**

| Room | N | Win % | Net | Avg |
|---|---|---|---|---|
| < 0.25 | 320 | 45% | -113 | -0.35 |
| 0.25–0.5 | 293 | 54% | +41 | +0.14 |
| 0.5–0.75 | 184 | 50% | +15 | +0.08 |
| 0.75–1 | 135 | 50% | +27 | +0.20 |
| >= 1 / none | 280 | 46% | -184 | -0.66 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–now) | Verdict |
|---|---|---|---|---|---|---|
| Skip if room < 0.25 x TP1 | 1003 | -166 | +28 | +0.3 | +13 / -21 / +36 | noise |
| Skip if room < 0.5 x TP1 | 744 | -193 | +1 | +0.0 | -18 / -54 / +73 | noise |
| Skip if room < 0.75 x TP1 | 527 | -210 | -16 | -0.1 | +1 / -52 / +35 | worse |
| Skip if room < 1.0 x TP1 | 355 | -158 | +36 | +0.3 | +4 / -57 / +90 | noise |
| TP1 just before the level (min 0.5 ATR) | 1257 | -188 | +5 | +0.2 | -11 / +15 / +1 | noise |
| TP1 just before the level (min 1.0 ATR) | 1234 | -190 | +3 | +0.3 | -5 / +9 / -0 | noise |
| Skip if room < 0.25 x TP1 + TP1 before the level (min 0.5 ATR) | 1026 | -141 | +52 | +0.5 | +3 / -2 / +52 | noise |

## Candidates (robust / promising)

- none
