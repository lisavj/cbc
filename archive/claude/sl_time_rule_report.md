## Week of 11/14/2026 summary

- STUDY SETTINGS STALE: the 11/13 settings sync (v10.96) lists 3 non-known MISMATCHes, NOT yet fixed in the project scripts, and they touch the 3m studies -- mes3_ema_grid LIVE still closes MES 3m 80/100 % by time of day (live since v10.95: 100 % at TP1 all day), and MGC 3m live is now FLIP 0 % (v10.96: nothing closed at TP1, BE, no trail, exit on HTF flip) while these replays use 80 % / trail 1.7 (MGCX) or 50 % / 3.5. Bot replay (H) is unaffected (part 1.0). Also new: the 11/14 X4 fix in mes3_ema_grid.py makes the MGC 3m VWAP-stretch gate actually block setups (MGC 3m 1193 setups vs 1707 last week), so MGC 3m numbers are not like-for-like with 11/09.
- Data Jan 5 -> 11/13. **Candidates: none** -> no change recommended on any chart.
- MES 3m: current exits net +47 (11/09 +6). Positive cells CUT 10 / HALF 7 / BE 7 of 36 (11/09 11 / 11 / 10). Best CUT < 50 % at 15 min +117 but third 3 -186, last 4 wk -198; HALF if negative at 18 min fell to +66 (third 3 -59) -- no longer T.
- MGC 3m (stretch gate now applied): current net +317, 1193 setups. Positive cells 23 / 16 / 21. The 18-min "negative" cells are bolded T4R again: CUT / BE if negative at 18 min +102 (z 0.5, thirds +44 / +17 / +42, last 4 wk +25), HALF +79 T4R. z only 0.5 -> not promising; 18 min is still the clear best check time.
- MNQ 3m: net -362 (11/09 +58); positive cells 1 / 2 / 1 -- early cuts lose. M2K 3m: net +92; positive cells 8 / 5 / 6; no bolded cell (last week's HALF at 45 min lost its T).
- Verdict per chart: MES / MGC / MNQ / M2K -- keep current exits (0 weeks toward the 3-week rule).

---

# Time-based stop / cut study — 3m charts — 11/14/2026 23:35

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

## MES 3m — current exits: 1738 setups 01/05–11/13, net +47, win 49 %, full SL1 losses 174 (-1753)

**CUT at the candle close** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -4 | -39 | +86 |
| 15 | -62 | +32 | +117 |
| 18 | +42 | +60 | +107 |
| 21 | -67 | -165 | +18 |
| 24 | -124 | -197 | -152 |
| 27 | -165 | -133 | -141 |
| 30 | -34 | -85 | -33 |
| 33 | -46 | -20 | -66 |
| 36 | +11 | -47 | -43 |
| 39 | +9 | +38 | -39 |
| 42 | -25 | -73 | -46 |
| 45 | -11 | -69 | -57 |

Positive cells 10 of 36. Best: X 15 / < 50 % of TP1 +117 (z +0.4, thirds +73 / +229 / -186, last 4 wk -198.4); X 18 / < 50 % of TP1 +107 (z +0.4, thirds +83 / +207 / -182, last 4 wk -176.1); X 12 / < 50 % of TP1 +86 (z +0.3, thirds -23 / +277 / -168, last 4 wk -213.9).

**Tighten SL1 to half its distance** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -18 | -51 | -53 |
| 15 | -42 | -31 | -9 |
| 18 | +66 | +54 | +28 |
| 21 | +5 | -49 | -14 |
| 24 | -122 | -94 | -83 |
| 27 | -65 | -56 | -70 |
| 30 | -58 | -41 | -15 |
| 33 | -1 | -12 | -5 |
| 36 | -21 | -46 | -49 |
| 39 | -9 | +13 | -39 |
| 42 | -14 | -21 | -28 |
| 45 | +8 | +3 | -24 |

Positive cells 7 of 36. Best: X 18 / negative +66 (z +0.2, thirds +43 / +83 / -59, last 4 wk -63.8); X 18 / < 25 % of TP1 +54 (z +0.2, thirds +78 / +61 / -86, last 4 wk -88.5); X 18 / < 50 % of TP1 +28 (z +0.1, thirds +105 / +45 / -122, last 4 wk -120.3).

**SL1 to breakeven** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -4 | -112 | -94 |
| 15 | -62 | -27 | +16 |
| 18 | +42 | +29 | +37 |
| 21 | -67 | -164 | -72 |
| 24 | -124 | -221 | -181 |
| 27 | -165 | -133 | -163 |
| 30 | -34 | -81 | -55 |
| 33 | -46 | -49 | -84 |
| 36 | +11 | -64 | -52 |
| 39 | +9 | +2 | -65 |
| 42 | -25 | -59 | -62 |
| 45 | -11 | -68 | -97 |

Positive cells 7 of 36. Best: X 18 / negative +42 (z +0.1, thirds +6 / +185 / -148, last 4 wk -107.0); X 18 / < 50 % of TP1 +37 (z +0.1, thirds +72 / +140 / -174, last 4 wk -141.6); X 18 / < 25 % of TP1 +29 (z +0.1, thirds +26 / +166 / -162, last 4 wk -117.1).

## MGC 3m — current exits: 1193 setups 01/05–11/13, net +317, win 51 %, full SL1 losses 380 (-2413)

**CUT at the candle close** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -15 | -29 | +38 |
| 15 | +43 T | +32 | +23 |
| 18 | **+102 T4R** | +88 4 | +74 4 |
| 21 | +22 | -10 | +9 |
| 24 | +27 TR | +26 | +23 |
| 27 | +54 T4 | +34 | +14 |
| 30 | -16 | -19 | +13 |
| 33 | +30 T | +43 | +64 |
| 36 | -9 | +35 | +63 |
| 39 | -22 | +9 | +40 T |
| 42 | -25 | -8 | -10 |
| 45 | -39 | -9 | -1 |

Positive cells 23 of 36. Best: X 18 / negative +102 (z +0.5, thirds +44 / +17 / +42, last 4 wk +24.6); X 18 / < 25 % of TP1 +88 (z +0.5, thirds +65 / -5 / +29, last 4 wk +12.1); X 18 / < 50 % of TP1 +74 (z +0.4, thirds +76 / -8 / +6, last 4 wk +2.4).

**Tighten SL1 to half its distance** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | +30 TR | +16 | +12 |
| 15 | +43 TR | +4 | +25 |
| 18 | **+79 T4R** | +48 | +59 |
| 21 | +21 | +32 | +21 |
| 24 | +29 | +20 | +3 |
| 27 | +14 | -13 | -32 |
| 30 | -23 | -35 | -27 |
| 33 | -24 | -28 | -33 |
| 36 | -49 | -27 | -30 |
| 39 | -36 | -28 | -25 |
| 42 | -32 | -35 | -32 |
| 45 | -27 | -28 | -23 |

Positive cells 16 of 36. Best: X 18 / negative +79 (z +0.4, thirds +25 / +2 / +51, last 4 wk +14.6); X 18 / < 50 % of TP1 +59 (z +0.3, thirds +44 / -10 / +25, last 4 wk -13.0); X 18 / < 25 % of TP1 +48 (z +0.3, thirds +35 / -10 / +23, last 4 wk -13.0).

**SL1 to breakeven** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -15 | -68 | -60 |
| 15 | +43 T | +37 | +42 |
| 18 | **+102 T4R** | +80 4 | +70 4 |
| 21 | +22 | +7 | +7 |
| 24 | +27 TR | +19 | +1 |
| 27 | +54 T4 | +42 T4 | +0 |
| 30 | -16 | -16 | -3 |
| 33 | +30 T | +43 T | +62 T |
| 36 | -9 | +30 | +43 |
| 39 | -22 | -2 | +11 |
| 42 | -25 | -12 | -7 |
| 45 | -39 | -29 | -19 |

Positive cells 21 of 36. Best: X 18 / negative +102 (z +0.5, thirds +44 / +17 / +42, last 4 wk +24.6); X 18 / < 25 % of TP1 +80 (z +0.4, thirds +60 / -4 / +24, last 4 wk +7.9); X 18 / < 50 % of TP1 +70 (z +0.4, thirds +77 / +4 / -10, last 4 wk +1.7).

## MNQ 3m — current exits: 1969 setups 01/05–11/13, net -362, win 45 %, full SL1 losses 768 (-22079)

**CUT at the candle close** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -586 4 | -519 4 | -886 4 |
| 15 | -536 4 | -682 4 | -433 4 |
| 18 | -275 4 | -274 4 | -307 4 |
| 21 | -426 4 | -494 4 | -322 4 |
| 24 | -190 4 | -130 4 | -47 4 |
| 27 | -375 4 | -166 4 | +38 4 |
| 30 | -362 4 | -299 4 | -310 4 |
| 33 | -487 | -310 4 | -672 |
| 36 | -308 | -81 4 | -204 4 |
| 39 | -150 4 | -135 | -160 |
| 42 | -343 4 | -253 | -196 |
| 45 | -210 | -238 | -52 4 |

Positive cells 1 of 36. Best: X 27 / < 50 % of TP1 +38 (z +0.0, thirds +108 / -239 / +168, last 4 wk +142.2); X 24 / < 50 % of TP1 -47 (z -0.0, thirds -111 / -141 / +205, last 4 wk +170.5); X 45 / < 50 % of TP1 -52 (z -0.0, thirds -35 / -54 / +38, last 4 wk +2.9).

**Tighten SL1 to half its distance** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -339 4 | -620 4 | -629 4 |
| 15 | +27 4 | -297 4 | -385 4 |
| 18 | -199 4 | -178 4 | -481 4 |
| 21 | -235 4 | -504 4 | -597 4 |
| 24 | -320 4 | -531 4 | -769 4 |
| 27 | -414 4 | -491 4 | -532 4 |
| 30 | +37 4 | -154 4 | -296 4 |
| 33 | -203 4 | -307 4 | -361 |
| 36 | -244 4 | -303 4 | -267 |
| 39 | -71 4 | -214 | -182 |
| 42 | -69 4 | -164 | -174 |
| 45 | -139 | -174 | -156 |

Positive cells 2 of 36. Best: X 30 / negative +37 (z +0.0, thirds +35 / -20 / +21, last 4 wk +40.2); X 15 / negative +27 (z +0.0, thirds -67 / +127 / -33, last 4 wk +159.2); X 42 / negative -69 (z -0.1, thirds +11 / -69 / -12, last 4 wk +7.2).

**SL1 to breakeven** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -586 4 | -551 4 | -1143 4 |
| 15 | -536 4 | -638 4 | -371 4 |
| 18 | -275 4 | -212 4 | -294 4 |
| 21 | -426 4 | -464 4 | -532 4 |
| 24 | -190 4 | -331 4 | -379 4 |
| 27 | -375 4 | -254 4 | -130 4 |
| 30 | -362 4 | -408 4 | -321 4 |
| 33 | -487 | -275 4 | -323 |
| 36 | -308 | -77 4 | +20 |
| 39 | -150 4 | -139 | -92 |
| 42 | -343 4 | -272 | -253 |
| 45 | -210 | -305 | -297 |

Positive cells 1 of 36. Best: X 36 / < 50 % of TP1 +20 (z +0.0, thirds +74 / -14 / -40, last 4 wk -10.1); X 36 / < 25 % of TP1 -77 (z -0.1, thirds +79 / -128 / -27, last 4 wk +30.0); X 39 / < 50 % of TP1 -92 (z -0.1, thirds +132 / -47 / -176, last 4 wk -2.3).

## M2K 3m — current exits: 1970 setups 01/05–11/13, net +92, win 54 %, full SL1 losses 488 (-1789)

**CUT at the candle close** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -28 | -70 | -69 |
| 15 | +16 | +1 | +23 |
| 18 | +27 | -12 | +0 |
| 21 | -25 | -12 | -3 |
| 24 | -5 | -3 | +26 |
| 27 | -25 | -2 | +5 |
| 30 | -27 | -18 | +3 |
| 33 | -22 | -9 | -5 |
| 36 | -18 | -23 | -17 |
| 39 | -21 | -15 | -7 |
| 42 | -9 | -19 | -20 |
| 45 | -7 | -8 | -17 |

Positive cells 8 of 36. Best: X 18 / negative +27 (z +0.2, thirds +15 / +44 / -32, last 4 wk -10.5); X 24 / < 50 % of TP1 +26 (z +0.2, thirds +14 / +35 / -24, last 4 wk -11.3); X 15 / < 50 % of TP1 +23 (z +0.2, thirds -1 / +70 / -46, last 4 wk -22.8).

**Tighten SL1 to half its distance** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -27 | -58 | -57 |
| 15 | -11 | -31 | -21 |
| 18 | -21 | -41 | -43 |
| 21 | -21 | -31 | -32 |
| 24 | -33 | -33 | -23 |
| 27 | -46 | -36 | -33 |
| 30 | -39 | -36 | -34 |
| 33 | -9 | -3 | -6 |
| 36 | -17 | -20 | -20 |
| 39 | -7 | +2 | -1 |
| 42 | +1 | -8 | -3 |
| 45 | +14 | +2 | +2 |

Positive cells 5 of 36. Best: X 45 / negative +14 (z +0.1, thirds +5 / +10 / -1, last 4 wk -0.9); X 39 / < 25 % of TP1 +2 (z +0.0, thirds +2 / +6 / -6, last 4 wk -1.2); X 45 / < 50 % of TP1 +2 (z +0.0, thirds -5 / +14 / -7, last 4 wk -4.2).

**SL1 to breakeven** — Δ net vs current

| X min | negative | < 25 % of TP1 | < 50 % of TP1 |
|---|---|---|---|
| 12 | -28 | -44 | -40 |
| 15 | +16 | +10 | +35 |
| 18 | +27 | -2 | -4 |
| 21 | -25 | -14 | -24 |
| 24 | -5 | +7 | +26 |
| 27 | -25 | -1 | -1 |
| 30 | -27 | -18 | -5 |
| 33 | -22 | -17 | -9 |
| 36 | -18 | -32 | -33 |
| 39 | -21 | -23 | -19 |
| 42 | -9 | -21 | -22 |
| 45 | -7 | -11 | -13 |

Positive cells 6 of 36. Best: X 15 / < 50 % of TP1 +35 (z +0.3, thirds -3 / +58 / -21, last 4 wk -15.3); X 18 / negative +27 (z +0.2, thirds +15 / +44 / -32, last 4 wk -10.5); X 24 / < 50 % of TP1 +26 (z +0.2, thirds +18 / +42 / -34, last 4 wk -17.2).

## Candidates (robust / promising AND both X neighbours better)

- none
