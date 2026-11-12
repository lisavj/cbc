## Week of 11/09/2026 summary

- STUDY SETTINGS STALE: the 11/08 settings sync report lists 1 non-known MISMATCH (chop_sim GATE MGC 2m range gate R5=0) + late_study MES 3m tp=2.0 -- both already fixed in the project scripts used for this run, and neither affects these 3m studies.
- Data Jan 5 -> 11/09 (11/07 run: -> 11/06). Same picture as 11/07; **no candidates** (Candidates: none) -> no change recommended.
- MES 3m: current exits net +6 (11/07 +19). Positive cells CUT 11 / HALF 11 / BE 10 of 36 (11/07 11 / 11 / 9). Best: HALF if negative at 18 min +115 T (z 0.4, thirds +43 / +71 / +1, last 4 wk -35); CUT < 50 % at 18 min +177 but third 3 -118, last 4 wk -151.
- MGC 3m: current net +247 (11/07 +237). Positive cells 23 / 15 / 18 of 36 (unchanged). The two bolded T4R cells of 11/07 lost their bold: CUT < 25 % at 15 min now +34 TR (last 4 wk not better), CUT < 50 % at 18 min now +109 '4' only (third 2 -0). 18 min still the best check time (+109 .. +124, z 0.5).
- MNQ 3m: current net +58 (11/07 +36); positive cells 1 / 2 / 1 -- early cuts lose. M2K 3m: net +78 (11/07 +85); positive cells 13 / 7 / 12; only bolded cell HALF if negative at 45 min +16 T4R (z 0.1, too small to matter).
- Verdict per chart: MES / MGC / MNQ / M2K -- keep current exits (nothing robust/promising with neighbours, 0 weeks toward the 3-week rule).

---

# Time-based stop / cut study — 3m charts — 11/09/2026 13:58

Time-based stop study, MES 3m and MGC 3m -- 11/07/2026 (companion to the 11/06 TP1-reduction study).
Question: once a setup has been open X minutes and is NOT working (still negative, or less than Y % of the way to TP1),
should it be cut at that candle's close, or should SL1 be tightened?
Rule (one check, at the close of the candle X minutes after entry, only if TP1 has not been reached yet):
  condition  Y = 'neg'  -> close is at or below Entry (long; short mirrored)
             Y = 25 / 50 -> close is less than 25 / 50 % of the way from Entry to TP1 (includes negative trades)
  action     CUT  -> close the whole trade at that candle close
             HALF -> SL1 moves to half its original distance from Entry (if the close is already past it: close now)
             BE   -> SL1 moves to Entry (if the close is below Entry: close now; with Y = 'neg' this equals CUT)
X = 12..45 min by 3 (same spread as the TP study). Everything else unchanged: stop, TP1 partial / BE / trail, HTF flip,
16:00 and new-setup exits.
Replay (chop_sim rules, late window 1, NY OR block 30) on live settings: MES 3m 9 / 20 + range gate, SL1 3 x ATR min 5,
TP1 1.75 x ATR (v10.82), close at TP1 by time of day; MGC 3m range gate + VWAP stretch 4, SL1 1.7 ATR min 5 cap 7,
TP1 1.7 ATR cap 6, 80 % + BE + trail 1.7; MNQ 3m / M2K 3m CBC defaults (SL1 1.7 ATR min 25 / 3 cap 30 / 5, TP1 1.7 ATR
cap 40 / 3, 80 % + BE + trail 1.7, no range gate). Jan 5 -> now, repaired bar data (11/07).
Cell = Δ net pts vs current exits. Flags: T = better in all three thirds, 4 = better in the last 4 weeks,
R = T and both X neighbours (±3 min) also better overall. z = Δ / (SD x sqrt(setups changed)).

## MES 3m — current exits: 1705 setups 01/05–11/09, net +6, win 49 %, full SL1 losses 169 (-1689)

**CUT at the candle close** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | +29 | -2 | +144 |
| 15 | -18 | +69 | +172 |
| 18 | +109 | +125 | +177 |
| 21 | -16 | -82 | +101 |
| 24 | -55 | -120 | -75 |
| 27 | -157 | -84 | -78 |
| 30 | -25 | -78 | -11 |
| 33 | -44 | -18 | -58 |
| 36 | +17 | -41 | -24 |
| 39 | +11 | +45 | -28 |
| 42 | -25 | -73 | -41 |
| 45 | -11 | -69 | -57 |

Positive cells 11 of 36. Best: X 18 / < 50 % of TP1 +177 (z +0.6, thirds +83 / +211 / -118, last 4 wk -150.8); X 15 / < 50 % of TP1 +172 (z +0.6, thirds +73 / +239 / -140, last 4 wk -182.6); X 12 / < 50 % of TP1 +144 (z +0.5, thirds -23 / +261 / -94, last 4 wk -187.5).

**Tighten SL1 to half its distance** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | +17 | -16 | -17 |
| 15 | -8 | +4 | +26 |
| 18 | +115 T | +102 | +77 |
| 21 | +54 | -0 | +34 |
| 24 | -79 | -51 | -39 |
| 27 | -68 | -25 | -39 |
| 30 | -62 | -44 | -18 |
| 33 | -5 | -16 | -9 |
| 36 | -23 | -48 | -51 |
| 39 | -9 | +13 | -39 |
| 42 | -14 | -21 | -28 |
| 45 | +8 | +3 | -24 |

Positive cells 11 of 36. Best: X 18 / negative +115 (z +0.4, thirds +43 / +71 / +1, last 4 wk -35.3); X 18 / < 25 % of TP1 +102 (z +0.4, thirds +78 / +50 / -26, last 4 wk -60.0); X 18 / < 50 % of TP1 +77 (z +0.3, thirds +105 / +33 / -62, last 4 wk -91.7).

**SL1 to breakeven** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | +29 | -75 | -27 |
| 15 | -18 | +14 | +81 |
| 18 | +109 | +96 | +104 |
| 21 | -16 | -90 | +2 |
| 24 | -55 | -152 | -112 |
| 27 | -157 | -83 | -113 |
| 30 | -25 | -70 | -44 |
| 33 | -44 | -46 | -72 |
| 36 | +17 | -59 | -44 |
| 39 | +11 | +4 | -61 |
| 42 | -25 | -58 | -61 |
| 45 | -11 | -67 | -96 |

Positive cells 10 of 36. Best: X 18 / negative +109 (z +0.4, thirds +6 / +174 / -71, last 4 wk -67.1); X 18 / < 50 % of TP1 +104 (z +0.4, thirds +72 / +142 / -110, last 4 wk -118.0); X 18 / < 25 % of TP1 +96 (z +0.3, thirds +26 / +169 / -98, last 4 wk -83.7).

## MGC 3m — current exits: 1707 setups 01/05–11/09, net +247, win 50 %, full SL1 losses 560 (-3533)

**CUT at the candle close** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | +30 | +61 | +68 |
| 15 | +36 | +34 TR | +47 |
| 18 | +112 T4 | +124 T4 | +109 4 |
| 21 | -4 | -34 | +2 |
| 24 | +13 | +6 | +3 |
| 27 | +42 4 | +8 4 | -36 |
| 30 | -26 | -53 | -28 |
| 33 | +25 T | +28 4 | +27 4 |
| 36 | +20 | +25 | +58 4 |
| 39 | -22 | +2 | +15 4 |
| 42 | -39 | -32 | -29 |
| 45 | -55 | -11 | -19 |

Positive cells 23 of 36. Best: X 18 / < 25 % of TP1 +124 (z +0.5, thirds +49 / +8 / +67, last 4 wk +13.7); X 18 / negative +112 (z +0.5, thirds +31 / +22 / +59, last 4 wk +34.0); X 18 / < 50 % of TP1 +109 (z +0.5, thirds +73 / -0 / +37, last 4 wk +3.6).

**Tighten SL1 to half its distance** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | +75 TR | +75 | +36 |
| 15 | +34 | +8 | +46 TR |
| 18 | +54 4 | +38 | +55 |
| 21 | -10 | +2 | +0 |
| 24 | +30 | +19 T | +12 |
| 27 | +12 4 | -25 | -40 |
| 30 | -31 | -40 | -33 |
| 33 | -47 | -46 | -50 |
| 36 | -49 | -32 | -33 |
| 39 | -39 | -34 | -31 |
| 42 | -37 | -40 | -34 |
| 45 | -31 | -24 | -20 |

Positive cells 15 of 36. Best: X 12 / negative +75 (z +0.3, thirds +2 / +22 / +52, last 4 wk -15.4); X 12 / < 25 % of TP1 +75 (z +0.3, thirds -16 / +46 / +45, last 4 wk -12.5); X 18 / < 50 % of TP1 +55 (z +0.2, thirds +40 / -20 / +35, last 4 wk -5.8).

**SL1 to breakeven** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | +30 | -6 | -51 |
| 15 | +36 | +33 T | +52 |
| 18 | +112 T4 | +104 T4 | +94 T |
| 21 | -4 | -34 | -28 |
| 24 | +13 | +13 | -10 |
| 27 | +42 4 | +20 4 | -39 |
| 30 | -26 | -39 | -29 |
| 33 | +25 T | +32 | +43 4 |
| 36 | +20 | +32 | +53 |
| 39 | -22 | -6 | +4 4 |
| 42 | -39 | -30 | -21 |
| 45 | -55 | -28 | -24 |

Positive cells 18 of 36. Best: X 18 / negative +112 (z +0.5, thirds +31 / +22 / +59, last 4 wk +34.0); X 18 / < 25 % of TP1 +104 (z +0.5, thirds +39 / +12 / +53, last 4 wk +6.1); X 18 / < 50 % of TP1 +94 (z +0.4, thirds +68 / +22 / +4, last 4 wk -1.6).

## MNQ 3m — current exits: 1937 setups 01/05–11/09, net +58, win 46 %, full SL1 losses 745 (-21394)

**CUT at the candle close** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -590 4 | -594 4 | -961 4 |
| 15 | -545 4 | -724 4 | -428 4 |
| 18 | -260 4 | -292 4 | -325 4 |
| 21 | -426 4 | -494 4 | -322 4 |
| 24 | -190 4 | -130 4 | -47 4 |
| 27 | -375 4 | -166 4 | +38 4 |
| 30 | -362 4 | -299 4 | -310 4 |
| 33 | -487 | -310 4 | -672 |
| 36 | -308 | -81 4 | -204 4 |
| 39 | -150 | -135 | -160 |
| 42 | -343 | -253 | -196 |
| 45 | -210 | -238 | -52 |

Positive cells 1 of 36. Best: X 27 / < 50 % of TP1 +38 (z +0.0, thirds +108 / -209 / +138, last 4 wk +154.4); X 24 / < 50 % of TP1 -47 (z -0.0, thirds -111 / -98 / +162, last 4 wk +214.7); X 45 / < 50 % of TP1 -52 (z -0.0, thirds -35 / -54 / +38, last 4 wk -0.5).

**Tighten SL1 to half its distance** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -369 4 | -680 4 | -689 4 |
| 15 | +19 4 | -321 4 | -409 4 |
| 18 | -214 4 | -208 4 | -511 4 |
| 21 | -235 4 | -504 4 | -597 4 |
| 24 | -320 4 | -531 4 | -769 4 |
| 27 | -414 4 | -491 4 | -532 4 |
| 30 | +37 4 | -154 4 | -296 4 |
| 33 | -203 | -307 4 | -361 |
| 36 | -244 | -303 4 | -267 |
| 39 | -71 | -214 | -182 |
| 42 | -69 4 | -164 | -174 |
| 45 | -139 | -174 | -156 |

Positive cells 2 of 36. Best: X 30 / negative +37 (z +0.0, thirds +35 / -20 / +21, last 4 wk +40.2); X 15 / negative +19 (z +0.0, thirds -67 / +99 / -14, last 4 wk +134.4); X 42 / negative -69 (z -0.1, thirds +11 / -69 / -12, last 4 wk +7.2).

**SL1 to breakeven** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -590 4 | -616 4 | -1207 4 |
| 15 | -545 4 | -677 4 | -378 4 |
| 18 | -260 4 | -226 4 | -309 4 |
| 21 | -426 4 | -464 4 | -532 4 |
| 24 | -190 4 | -331 4 | -379 4 |
| 27 | -375 4 | -254 4 | -130 4 |
| 30 | -362 4 | -408 4 | -321 4 |
| 33 | -487 | -275 4 | -323 |
| 36 | -308 | -77 4 | +20 |
| 39 | -150 | -139 | -92 |
| 42 | -343 | -272 | -253 |
| 45 | -210 | -305 | -297 |

Positive cells 1 of 36. Best: X 36 / < 50 % of TP1 +20 (z +0.0, thirds +74 / -14 / -40, last 4 wk -2.2); X 36 / < 25 % of TP1 -77 (z -0.1, thirds +79 / -128 / -27, last 4 wk +37.9); X 39 / < 50 % of TP1 -92 (z -0.1, thirds +132 / -47 / -176, last 4 wk -25.2).

## M2K 3m — current exits: 1948 setups 01/05–11/09, net +78, win 54 %, full SL1 losses 485 (-1776)

**CUT at the candle close** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -14 4 | -53 | -57 |
| 15 | +21 | +5 | +29 |
| 18 | +30 | -8 | +9 |
| 21 | -19 | -6 | +3 |
| 24 | -0 | +1 | +30 4 |
| 27 | -19 | +6 | +10 |
| 30 | -22 | -13 | +8 |
| 33 | -12 | +0 | +4 |
| 36 | -11 | -16 | -9 |
| 39 | -17 | -11 | -2 |
| 42 | -6 | -16 | -15 |
| 45 | -6 | -6 | -13 |

Positive cells 13 of 36. Best: X 24 / < 50 % of TP1 +30 (z +0.3, thirds +14 / +33 / -17, last 4 wk +1.3); X 18 / negative +30 (z +0.2, thirds +15 / +39 / -25, last 4 wk -9.5); X 15 / < 50 % of TP1 +29 (z +0.2, thirds -1 / +68 / -38, last 4 wk -19.3).

**Tighten SL1 to half its distance** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -17 4 | -48 4 | -48 4 |
| 15 | -8 | -28 | -18 |
| 18 | -18 | -38 | -40 |
| 21 | -16 | -27 | -27 |
| 24 | -29 | -29 | -19 4 |
| 27 | -41 | -31 | -28 |
| 30 | -34 4 | -31 4 | -29 4 |
| 33 | -3 | +2 | -0 |
| 36 | -12 4 | -15 4 | -15 |
| 39 | -5 4 | +4 4 | +0 4 |
| 42 | +3 | -6 | -2 |
| 45 | **+16 T4R** | +3 | +3 |

Positive cells 7 of 36. Best: X 45 / negative +16 (z +0.1, thirds +5 / +10 / +0, last 4 wk +3.2); X 39 / < 25 % of TP1 +4 (z +0.0, thirds +2 / +6 / -4, last 4 wk +1.1); X 45 / < 50 % of TP1 +3 (z +0.0, thirds -5 / +14 / -6, last 4 wk -0.0).

**SL1 to breakeven** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -14 4 | -31 | -31 |
| 15 | +21 | +15 | +40 |
| 18 | +30 | +3 | +4 |
| 21 | -19 | -8 | -18 |
| 24 | -0 | +12 | +30 |
| 27 | -19 | +7 | +5 |
| 30 | -22 | -11 | +1 |
| 33 | -12 | -8 | +1 |
| 36 | -11 | -25 | -27 |
| 39 | -17 | -18 | -15 |
| 42 | -6 | -17 | -18 |
| 45 | -6 | -8 | -11 |

Positive cells 12 of 36. Best: X 15 / < 50 % of TP1 +40 (z +0.3, thirds -3 / +57 / -14, last 4 wk -7.2); X 24 / < 50 % of TP1 +30 (z +0.3, thirds +18 / +38 / -26, last 4 wk -5.5); X 18 / negative +30 (z +0.2, thirds +15 / +39 / -25, last 4 wk -9.5).

## Candidates (robust / promising AND both X neighbours better)

- none
