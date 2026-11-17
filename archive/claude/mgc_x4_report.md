MGC 3m after the replay-engine stretch-gate fix (11/14/2026): (1) check, (2) tp1flip exits rerun, (3) chart EMA 7 / 16 on the branch.
Engine fix: mes3_ema_grid MCase.gen set X4 = False for every main setup, so gates=dict(X4=1) only blocked late LTF setups; now
X4 = close more than 4 ATR beyond VWAP on the trade side (same as late_study / chop_sim / tsf_study's own check).
MGC 3m live settings: ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR, VWAP stretch 4 ATR; exits SL1 1.7 ATR min 5 cap 7,
TP1 1.7 ATR cap 6. Branch adds HTF EMA20 slope >= 0.3 ATR (MGC 3m; flip ride is MES 3m only). Replay Jan 5 -> now, net after 0.22 cost.
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, all three thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds.

Data: 102525 candles, 01/05 → 11/13. Thirds 01/05–04/19 / 04/19–08/01 / 08/01–11/13. Last 4 weeks from 10/16.

## 1. Check (TV EMA20, v10.97 MGC 3m settings, FLIP 0 % exits)

- Fixed engine, gates X4=1: 1136 setups, net +615.
- Stretch check inside the study (tsf_study way): 1136 setups, net +615 (tsf_report "current": 1136 setups).
- Old engine behaviour (main setups never stretch-blocked): 1628 setups, net +517 (tp1flip / cbce / volflip ran like this).

## 2a. tp1flip exits, gate applied (fixed) -- v10.97 settings -- 1136 setups; live = FLIP 0 % at TP1

| Exit | Close at TP1 | Net | Δ vs live | z | Thirds | Last 4 wk | Win % | Max DD |
|---|---|---|---|---|---|---|---|---|
| TRAIL | 0 % | +609 | -6 | -0.1 | +296 / +1 / +312 | +288 | 21 % | 254 |
| TRAIL | 25 % | +454 | -161 | -0.5 | +206 / +5 / +243 | +227 | 50 % | 220 |
| TRAIL | 50 % | +298 | -317 | -1.0 | +115 / +10 / +173 | +166 | 50 % | 187 |
| TRAIL | 75 % | +143 | -472 | -1.4 | +25 / +14 / +104 | +105 | 50 % | 158 |
| TRAIL | 100 % | -12 | -627 | -1.9 | -65 / +19 / +35 | +44 | 50 % | 176 |
| **FLIP (live)** | 0 % | +615 | +0 | +0.0 | +329 / -10 / +297 | +262 | 18 % | 245 |
| FLIP | 25 % | +458 | -157 | -0.5 | +230 / -3 / +231 | +208 | 50 % | 214 |
| FLIP | 50 % | +302 | -313 | -0.9 | +132 / +4 / +166 | +153 | 50 % | 183 |
| FLIP | 75 % | +145 | -470 | -1.4 | +33 / +11 / +100 | +99 | 50 % | 157 |
| FLIP-noBE | 0 % | +396 | -219 | -0.8 | +185 / +69 / +142 | +221 | 28 % | 356 |
| FLIP-noBE | 25 % | +294 | -321 | -1.0 | +122 / +57 / +115 | +177 | 32 % | 279 |
| FLIP-noBE | 50 % | +192 | -423 | -1.3 | +60 / +44 / +88 | +133 | 37 % | 214 |
| FLIP-noBE | 75 % | +90 | -525 | -1.6 | -3 / +31 / +62 | +89 | 50 % | 167 |
| FLIP+SL | - | +396 | -219 | -0.8 | +185 / +69 / +142 | +221 | 28 % | 356 |

Largest: FLIP 0 % = +615. Better than live in all three thirds: none

## 2b. Same, branch settings (+ slope 0.3) -- 634 setups; live = FLIP 0 % at TP1

| Exit | Close at TP1 | Net | Δ vs live | z | Thirds | Last 4 wk | Win % | Max DD |
|---|---|---|---|---|---|---|---|---|
| TRAIL | 0 % | +1112 | -24 | -0.2 | +519 / +87 / +506 | +297 | 24 % | 104 |
| TRAIL | 25 % | +922 | -214 | -0.7 | +416 / +90 / +416 | +246 | 54 % | 81 |
| TRAIL | 50 % | +732 | -404 | -1.3 | +313 / +93 / +326 | +195 | 54 % | 75 |
| TRAIL | 75 % | +541 | -594 | -2.0 | +210 / +96 / +235 | +144 | 54 % | 71 |
| TRAIL | 100 % | +351 | -784 | -2.6 | +106 / +100 / +145 | +94 | 54 % | 67 |
| **FLIP (live)** | 0 % | +1135 | +0 | +0.0 | +545 / +78 / +512 | +279 | 22 % | 121 |
| FLIP | 25 % | +939 | -196 | -0.7 | +436 / +84 / +420 | +232 | 54 % | 94 |
| FLIP | 50 % | +743 | -392 | -1.3 | +326 / +89 / +328 | +186 | 54 % | 70 |
| FLIP | 75 % | +547 | -588 | -2.0 | +216 / +94 / +237 | +140 | 54 % | 66 |
| FLIP-noBE | 0 % | +1038 | -97 | -0.4 | +480 / +137 / +422 | +258 | 32 % | 154 |
| FLIP-noBE | 25 % | +867 | -269 | -0.9 | +387 / +127 / +352 | +217 | 37 % | 101 |
| FLIP-noBE | 50 % | +695 | -441 | -1.5 | +293 / +118 / +283 | +176 | 41 % | 79 |
| FLIP-noBE | 75 % | +523 | -612 | -2.0 | +200 / +109 / +214 | +135 | 54 % | 73 |
| FLIP+SL | - | +1038 | -97 | -0.4 | +480 / +137 / +422 | +258 | 32 % | 154 |

Largest: FLIP 0 % = +1135. Better than live in all three thirds: none

## 2c. For reference: old engine (no gate on main setups) -- what the 11/13 tp1flip used -- 1628 setups; live = FLIP 0 % at TP1

| Exit | Close at TP1 | Net | Δ vs live | z | Thirds | Last 4 wk | Win % | Max DD |
|---|---|---|---|---|---|---|---|---|
| TRAIL | 0 % | +517 | -0 | -0.0 | +229 / -109 / +397 | +334 | 20 % | 304 |
| TRAIL | 25 % | +348 | -169 | -0.5 | +140 / -76 / +283 | +256 | 49 % | 251 |
| TRAIL | 50 % | +179 | -338 | -0.9 | +52 / -42 / +170 | +179 | 49 % | 222 |
| TRAIL | 75 % | +10 | -507 | -1.4 | -37 / -9 / +56 | +101 | 49 % | 205 |
| TRAIL | 100 % | -159 | -676 | -1.8 | -126 / +24 / -57 | +23 | 49 % | 205 |
| **FLIP (live)** | 0 % | +517 | +0 | +0.0 | +231 / -94 / +380 | +311 | 18 % | 291 |
| FLIP | 25 % | +348 | -169 | -0.5 | +142 / -64 / +271 | +239 | 49 % | 237 |
| FLIP | 50 % | +179 | -338 | -0.9 | +53 / -35 / +161 | +167 | 49 % | 204 |
| FLIP | 75 % | +10 | -507 | -1.4 | -37 / -5 / +52 | +95 | 49 % | 196 |
| FLIP-noBE | 0 % | +248 | -269 | -0.9 | +48 / -24 / +223 | +325 | 28 % | 451 |
| FLIP-noBE | 25 % | +146 | -371 | -1.0 | +5 / -12 / +153 | +250 | 32 % | 356 |
| FLIP-noBE | 50 % | +44 | -473 | -1.3 | -39 / +0 / +83 | +174 | 36 % | 264 |
| FLIP-noBE | 75 % | -57 | -574 | -1.5 | -82 / +12 / +13 | +99 | 49 % | 222 |
| FLIP+SL | - | +248 | -269 | -0.9 | +48 / -24 / +223 | +325 | 28 % | 451 |

Largest: FLIP 0 % = +517. Better than live in all three thirds: none

## 3a. Chart EMA, branch settings (stretch 4 + slope 0.3, FLIP 0 %)

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 9/20 | z | Δ by third | Δ last 4 wk | Max DD | Verdict | By trigger (n / net) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20, TV EMA20 (project baseline) | 634 | 22 % | +1135 | +1.79 | -4 | -0.2 | +0 / +0 / -4 | +0 | 121 | worse | Flip 62 / +7 · LTF20 402 / +784 · HTF9 127 / +163 · HTF20 43 / +181 |
| 9 / 20 recomputed (comparison base) | 633 | 22 % | +1140 | +1.80 | +0 | +0.0 | +0 / +0 / +0 | +279 | 121 | baseline | Flip 62 / +7 · LTF20 401 / +788 · HTF9 127 / +163 · HTF20 43 / +181 |
| 7 / 16 | 732 | 19 % | +1131 | +1.55 | -8 | -0.0 | -62 / +173 / -120 | -144 | 143 | worse | Flip 69 / -4 · LTF20 491 / +751 · HTF9 135 / +229 · HTF20 37 / +155 |
| 7 / 14 | 784 | 19 % | +1019 | +1.30 | -120 | -0.3 | -119 / +50 / -52 | -88 | 230 | worse | Flip 70 / -11 · LTF20 534 / +584 · HTF9 142 / +310 · HTF20 38 / +136 |

(Recomputed 9 / 20 row: "Δ last 4 wk" = its own last-4-week net.)

## 3b. Chart EMA, v10.97 settings (no slope filter)

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 9/20 | z | Δ by third | Δ last 4 wk | Max DD | Verdict | By trigger (n / net) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20, TV EMA20 (project baseline) | 1136 | 18 % | +615 | +0.54 | -4 | -0.3 | +0 / +0 / -4 | +0 | 245 | worse | Flip 203 / +104 · LTF20 559 / +406 · HTF9 203 / +60 · HTF20 171 / +45 |
| 9 / 20 recomputed (comparison base) | 1135 | 19 % | +619 | +0.55 | +0 | +0.0 | +0 / +0 / +0 | +262 | 245 | baseline | Flip 203 / +104 · LTF20 558 / +410 · HTF9 203 / +60 · HTF20 171 / +45 |
| 7 / 16 | 1232 | 17 % | +632 | +0.51 | +13 | +0.0 | +6 / +92 / -85 | -126 | 341 | noise | Flip 214 / +72 · LTF20 649 / +339 · HTF9 216 / +181 · HTF20 153 / +41 |
| 7 / 14 | 1297 | 17 % | +590 | +0.45 | -29 | -0.1 | +8 / -8 / -29 | -89 | 412 | worse | Flip 219 / +54 · LTF20 704 / +321 · HTF9 224 / +226 · HTF20 150 / -11 |

(Recomputed 9 / 20 row: "Δ last 4 wk" = its own last-4-week net.)
