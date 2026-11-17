# HTF EMA length study -- 2026-11-15 19:13 ET (run 9)

## Since last run (11/13 19:13 ET, run 8)

**STUDY SETTINGS STALE:** settings sync (11/13 16:47 ET, CBC v10.96) still lists 3 MISMATCHes — mes3_ema_grid `LIVE` part 'tod' (MES 3m now 100 % at TP1 all day, v10.95), chop_sim `EXIT[('MES',3)]` part 'tod', chop_sim `EXIT[('MGC',3)]` 50 % / trail 3.5 (MGC 3m now FLIP 0 %, v10.96). Ran anyway. This study replays with ema5_study's BASE exits (`ss.QB`, 80 % / trail 1.7), not chop_sim `EXIT`, so the mismatches do not change these numbers; totals were never live exits (compare rows, not totals). Only ~26 more 3m / ~16 more 5m candles than run 8 (Friday close → weekend), so every row is unchanged or within 1 setup.

- **MES 3m:** standard +0 (unchanged). Nothing robust. Promising (all thirds +), all unchanged vs run 8: both pierces off +198 (z 1.6, +42 / +56 / +100); HTF EMA9 Pierce off +154 (z 1.6, +25 / +55 / +73); HTF 7 / 16 +158 (z 1.2, +39 / +44 / +75); HTF 12 / 20 +123 (z 1.2, +28 / +49 / +45); HTF 9 / 26 +104 (z 1.1, +29 / +35 / +41); HTF 7 / 20 +103 (z 1.1, +43 / +26 / +33). Consecutive robust runs: 0 for all. Replay HTF EMA9 Pierce setups 290 · −158 (unchanged).
- **MGC 3m:** standard +320 (unchanged). Nothing robust or promising. Faster HTF still clearly worse (8 / 18 −309, z −2.8; 7 / 16 −259, z −1.8). Best: HTF 12 / 26 +45 (z 0.3, Jul–Oct −1, noise).
- **MES 5m:** standard +20 (unchanged). With chart 9 / 20 / 200 every HTF change is worse or noise; pierce-off references all worse. Robust rows are all chart-EMA 16 / 34 / 120 combos, unchanged vs run 8: A+ (HTF 9 / 20) +504 (z 3.2, +200 / +136 / +168), H+ 9 / 34 +440 (z 2.5, +181 / +83 / +176), G+ 9 / 26 +430 (z 2.4, +123 / +74 / +232), C+ 8 / 18 +392 (z 2.2, +75 / +148 / +169) — each robust **9 runs in a row** (11/01–11/15, 14 days); I+ 7 / 20 +349 (z 2.1, +88 / +131 / +130) robust **5 runs in a row** (11/07–11/15, 8 days). J+ 12 / 20 promising (+342, z 1.9); B+, E+, F+ promising. HTF 9 / 20 is still the best + row → a chart-EMA signal (5m chart EMAs 16 / 34 / 120, separate chart-EMA study), not an HTF-length one.
- **MGC 5m:** standard −102 (unchanged). Nothing robust or promising. Best still HTF 14 / 30 +304 (z 2.1, but Apr–Jun −6 → noise); HTF EMA9 Pierce off +119 (z 1.3, Apr–Jun −9, noise).

**Live HTF pierce setups** (alert store through 11/16 00:16 UTC, 48,061 alerts; store still not cleaned (`lastDedupe` null), so near-copies — same chart, Time line and alert names within 60 s — were merged, longest kept; where one MGC 3m setup had two results the "0.5×(TP1)" one was used). Matched to the first Setup Ended after each setup. No new HTF pierce setups since run 8:

| Chart | Trigger | Setups | Ended | Win % | Net | Avg | vs 11/13 |
|---|---|---|---|---|---|---|---|
| MES 3m | HTF EMA9 Pierce | 15 | 14 | 43% | +4.8 | +0.34 | unchanged |
| MES 3m | HTF EMA20 Pierce | 10 | 8 | 38% | −5.1 | −0.63 | unchanged |
| MGC 3m | HTF EMA9 Pierce | 15 | 13 | 54% | +5.9 | +0.46 | unchanged |
| MGC 3m | HTF EMA20 Pierce | 12 | 11 | 45% | −7.7 | −0.70 | unchanged |
| MES 5m | HTF EMA9 Pierce | 5 | 3 | 33% | −8.7 | −2.90 | unchanged |
| MES 5m | HTF EMA20 Pierce | 9 | 8 | 62% | +4.9 | +0.61 | unchanged |
| MGC 5m | HTF EMA9 Pierce | 12 | 11 | 64% | +18.3 | +1.67 | unchanged |
| MGC 5m | HTF EMA20 Pierce | 7 | 6 | 50% | +2.7 | +0.45 | unchanged |

MGC 3m live results 11/09–11/12 are partly on the old exits (DATA_NOTES note 2); MGC 3m exit is FLIP 0 % since v10.96 (11/13). No trigger has the 20 ended live setups the verdict rule needs.

**Verdict:** keep HTF 9 / 20 on all four charts. No HTF-length or pierce-off variation is robust on any chart with the live chart EMAs. On MES 5m the 16 / 34 / 120 rows (A+, C+, G+, H+; now also I+ at 5 runs / 8 days) pass (a) and (b) but fail (c) — MES 5m live HTF pierce setups have only 3 / 8 ended and HTF EMA20 Pierce is net positive — and the best of them keeps HTF 9 / 20, so they point at a chart-EMA change (separate study), not an HTF change. A different HTF length would need a new CBC version with "HTF EMA fast / slow" inputs; turning a pierce trigger off is already a CBC input (② Setup Triggers). Watch on MES 3m: both pierces off and HTF EMA9 Pierce off (z 1.6), HTF 7 / 16 and 12 / 20 (z 1.2), HTF 9 / 26 and 7 / 20 (z 1.1) — all promising, none robust, all flat this run.

---

## MES 3m — HTF 15m EMAs (102771 candles, chart EMAs 9 / 20 / 200, range gate on)

Check: recomputed HTF EMA20 vs BarFeed value — median gap 0.00 typical candle moves (after the first 200 HTF candles: 0.00)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A HTF 9 / 20 (standard) | 1757 | 50% | +0 | +0.00 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 320 / +50 · LTF20 963 / +116 · HTF9 290 / -158 · HTF20 184 / -7
| B HTF 7 / 16 (faster) | 1841 | 51% | +159 | +0.09 | +158 | +1.2 | +39 / +44 / +75 | promising | Flip 316 / +51 · LTF20 1009 / +47 · HTF9 312 / -12 · HTF20 204 / +72
| C HTF 8 / 18 (slightly faster) | 1812 | 49% | -59 | -0.03 | -60 | -0.6 | +14 / -31 / -43 | worse | Flip 318 / +50 · LTF20 977 / +33 · HTF9 319 / -186 · HTF20 198 / +43
| D HTF 5 / 12 (much faster) | 1913 | 50% | -50 | -0.03 | -51 | -0.3 | -47 / -63 / +59 | worse | Flip 316 / +41 · LTF20 1032 / +117 · HTF9 343 / -109 · HTF20 222 / -100
| E HTF 12 / 26 (slower) | 1633 | 50% | +111 | +0.07 | +111 | +0.8 | -19 / +74 / +55 | noise | Flip 324 / +59 · LTF20 939 / +52 · HTF9 250 / -63 · HTF20 120 / +64
| F HTF 14 / 30 (slower) | 1572 | 51% | +98 | +0.06 | +98 | +0.7 | +26 / +101 / -29 | noise | Flip 327 / +65 · LTF20 917 / +8 · HTF9 243 / +32 · HTF20 85 / -7
| G HTF 9 / 26 (slow line slower) | 1656 | 51% | +105 | +0.06 | +104 | +1.1 | +29 / +35 / +41 | promising | Flip 324 / +59 · LTF20 935 / +62 · HTF9 272 / -126 · HTF20 125 / +110
| H HTF 9 / 34 (slow line much slower) | 1593 | 50% | -5 | -0.00 | -6 | -0.1 | -41 / +73 / -38 | worse | Flip 329 / +52 · LTF20 902 / +103 · HTF9 262 / -142 · HTF20 100 / -19
| I HTF 7 / 20 (fast line faster) | 1773 | 50% | +103 | +0.06 | +103 | +1.1 | +43 / +26 / +33 | promising | Flip 320 / +50 · LTF20 960 / +85 · HTF9 301 / -15 · HTF20 192 / -17
| J HTF 12 / 20 (fast line slower) | 1716 | 50% | +123 | +0.07 | +123 | +1.2 | +28 / +49 / +45 | promising | Flip 320 / +50 · LTF20 971 / +113 · HTF9 262 / -45 · HTF20 163 / +5
| Reference: HTF EMA9 Pierce trigger OFF | 1568 | 51% | +154 | +0.10 | +154 | +1.6 | +25 / +55 / +73 | promising | Flip 320 / +50 · LTF20 1013 / +132 · HTF9 0 / +0 · HTF20 235 / -28
| Reference: HTF EMA20 Pierce trigger OFF | 1621 | 50% | +6 | +0.00 | +6 | +0.1 | +13 / -10 / +3 | noise | Flip 320 / +50 · LTF20 1007 / +123 · HTF9 294 / -167 · HTF20 0 / +0
| Reference: both HTF EMA pierce triggers OFF | 1388 | 51% | +199 | +0.14 | +198 | +1.6 | +42 / +56 / +100 | promising | Flip 320 / +50 · LTF20 1068 / +149 · HTF9 0 / +0 · HTF20 0 / +0

Candidates: B HTF 7 / 16 → +158, z +1.2, +39 / +44 / +75 (promising); G HTF 9 / 26 → +104, z +1.1, +29 / +35 / +41 (promising); I HTF 7 / 20 → +103, z +1.1, +43 / +26 / +33 (promising); J HTF 12 / 20 → +123, z +1.2, +28 / +49 / +45 (promising); HTF EMA9 Pierce trigger OFF  → +154, z +1.6, +25 / +55 / +73 (promising); both HTF EMA pierce triggers OFF  → +198, z +1.6, +42 / +56 / +100 (promising)


## MGC 3m — HTF 15m EMAs (102551 candles, chart EMAs 9 / 20 / 200, range gate on), VWAP stretch 4 ATR

Check: recomputed HTF EMA20 vs BarFeed value — median gap 0.00 typical candle moves (after the first 200 HTF candles: 0.00)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A HTF 9 / 20 (standard) | 1200 | 51% | +320 | +0.27 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 214 / +125 · LTF20 615 / +175 · HTF9 196 / -84 · HTF20 175 / +105
| B HTF 7 / 16 (faster) | 1300 | 49% | +61 | +0.05 | -259 | -1.8 | -78 / -36 / -146 | worse | Flip 214 / +125 · LTF20 669 / +157 · HTF9 217 / -82 · HTF20 200 / -138
| C HTF 8 / 18 (slightly faster) | 1255 | 48% | +12 | +0.01 | -309 | -2.8 | -93 / -105 / -110 | worse | Flip 215 / +118 · LTF20 634 / +161 · HTF9 205 / -143 · HTF20 201 / -125
| D HTF 5 / 12 (much faster) | 1441 | 50% | +308 | +0.21 | -12 | -0.1 | +33 / -103 / +59 | worse | Flip 212 / +128 · LTF20 718 / +91 · HTF9 265 / -10 · HTF20 246 / +99
| E HTF 12 / 26 (slower) | 1172 | 51% | +365 | +0.31 | +45 | +0.3 | +37 / +8 / -1 | noise | Flip 221 / +141 · LTF20 594 / +147 · HTF9 212 / +38 · HTF20 145 / +39
| F HTF 14 / 30 (slower) | 1130 | 51% | +286 | +0.25 | -34 | -0.2 | +48 / -4 / -79 | worse | Flip 222 / +135 · LTF20 575 / +200 · HTF9 212 / +40 · HTF20 121 / -89
| G HTF 9 / 26 (slow line slower) | 1160 | 51% | +358 | +0.31 | +37 | +0.3 | +26 / +45 / -34 | noise | Flip 221 / +141 · LTF20 595 / +170 · HTF9 192 / -50 · HTF20 152 / +96
| H HTF 9 / 34 (slow line much slower) | 1068 | 51% | +288 | +0.27 | -33 | -0.3 | -27 / +38 / -44 | worse | Flip 223 / +140 · LTF20 540 / +170 · HTF9 176 / -32 · HTF20 129 / +10
| I HTF 7 / 20 (fast line faster) | 1197 | 50% | +299 | +0.25 | -21 | -0.2 | -18 / +17 / -20 | worse | Flip 214 / +125 · LTF20 613 / +171 · HTF9 189 / -47 · HTF20 181 / +51
| J HTF 12 / 20 (fast line slower) | 1202 | 50% | +311 | +0.26 | -9 | -0.1 | -4 / -26 / +21 | worse | Flip 214 / +125 · LTF20 617 / +155 · HTF9 223 / -21 · HTF20 148 / +52
| Reference: HTF EMA9 Pierce trigger OFF | 1074 | 51% | +351 | +0.33 | +31 | +0.4 | +58 / -19 / -8 | noise | Flip 214 / +125 · LTF20 643 / +140 · HTF9 0 / +0 · HTF20 217 / +87
| Reference: HTF EMA20 Pierce trigger OFF | 1063 | 51% | +231 | +0.22 | -89 | -1.1 | -75 / +15 / -30 | worse | Flip 214 / +125 · LTF20 641 / +170 · HTF9 208 / -64 · HTF20 0 / +0
| Reference: both HTF EMA pierce triggers OFF | 899 | 51% | +274 | +0.30 | -47 | -0.4 | -11 / -6 / -29 | worse | Flip 214 / +125 · LTF20 685 / +149 · HTF9 0 / +0 · HTF20 0 / +0

Candidates: none


## MES 5m — HTF 25m EMAs (61663 candles, chart EMAs 9 / 20 / 200)

Check: recomputed HTF EMA20 vs BarFeed value — median gap 0.00 typical candle moves (after the first 200 HTF candles: 0.00)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A HTF 9 / 20 (standard) | 1208 | 51% | +20 | +0.02 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 317 / -34 · LTF20 590 / -81 · HTF9 192 / +69 · HTF20 109 / +66
| B HTF 7 / 16 (faster) | 1252 | 50% | -91 | -0.07 | -110 | -0.9 | -61 / -44 / -6 | worse | Flip 317 / -34 · LTF20 617 / -96 · HTF9 181 / -57 · HTF20 137 / +96
| C HTF 8 / 18 (slightly faster) | 1226 | 51% | -54 | -0.04 | -74 | -0.7 | -63 / -2 / -10 | worse | Flip 317 / -34 · LTF20 604 / -144 · HTF9 177 / +78 · HTF20 128 / +46
| D HTF 5 / 12 (much faster) | 1323 | 50% | -206 | -0.16 | -225 | -1.4 | +61 / -95 / -191 | worse | Flip 317 / -34 · LTF20 632 / -127 · HTF9 240 / +45 · HTF20 134 / -89
| E HTF 12 / 26 (slower) | 1148 | 51% | -49 | -0.04 | -69 | -0.5 | +5 / -61 / -13 | worse | Flip 320 / -29 · LTF20 576 / -79 · HTF9 162 / -43 · HTF20 90 / +103
| F HTF 14 / 30 (slower) | 1119 | 51% | -84 | -0.07 | -103 | -0.8 | -63 / -25 / -15 | worse | Flip 321 / -23 · LTF20 570 / -133 · HTF9 140 / -34 · HTF20 88 / +106
| G HTF 9 / 26 (slow line slower) | 1162 | 52% | +25 | +0.02 | +5 | +0.1 | -41 / -37 / +82 | noise | Flip 320 / -29 · LTF20 558 / -104 · HTF9 186 / +74 · HTF20 98 / +84
| H HTF 9 / 34 (slow line much slower) | 1133 | 52% | +57 | +0.05 | +37 | +0.3 | +27 / -20 / +31 | noise | Flip 322 / -31 · LTF20 539 / -112 · HTF9 182 / +134 · HTF20 90 / +66
| I HTF 7 / 20 (fast line faster) | 1194 | 51% | -32 | -0.03 | -51 | -0.6 | -23 / +15 / -43 | worse | Flip 317 / -34 · LTF20 591 / -56 · HTF9 167 / -64 · HTF20 119 / +122
| J HTF 12 / 20 (fast line slower) | 1188 | 51% | -32 | -0.03 | -52 | -0.5 | +69 / -25 / -96 | worse | Flip 317 / -34 · LTF20 603 / -46 · HTF9 178 / -45 · HTF20 90 / +93
| A+ HTF 9 / 20 (standard, chart 16/34/120) | 1003 | 56% | +524 | +0.52 | +504 | +3.2 | +200 / +136 / +168 | robust | Flip 313 / -3 · LTF20 390 / +294 · HTF9 178 / +152 · HTF20 122 / +81
| B+ HTF 7 / 16 (faster, chart 16/34/120) | 1055 | 54% | +296 | +0.28 | +276 | +1.5 | +25 / +107 / +144 | promising | Flip 312 / -8 · LTF20 387 / +311 · HTF9 215 / -19 · HTF20 141 / +13
| C+ HTF 8 / 18 (slightly faster, chart 16/34/120) | 1026 | 56% | +411 | +0.40 | +392 | +2.2 | +75 / +148 / +169 | robust | Flip 312 / -8 · LTF20 381 / +228 · HTF9 194 / +157 · HTF20 139 / +35
| D+ HTF 5 / 12 (much faster, chart 16/34/120) | 1240 | 52% | +53 | +0.04 | +33 | +0.2 | +35 / -49 / +47 | noise | Flip 311 / -13 · LTF20 388 / +237 · HTF9 418 / -122 · HTF20 123 / -49
| E+ HTF 12 / 26 (slower, chart 16/34/120) | 957 | 55% | +297 | +0.31 | +277 | +1.4 | +116 / +3 / +158 | promising | Flip 313 / -3 · LTF20 390 / +238 · HTF9 159 / -9 · HTF20 95 / +72
| F+ HTF 14 / 30 (slower, chart 16/34/120) | 936 | 54% | +222 | +0.24 | +203 | +1.0 | +73 / +10 / +120 | promising | Flip 306 / -17 · LTF20 399 / +191 · HTF9 146 / -34 · HTF20 85 / +81
| G+ HTF 9 / 26 (slow line slower, chart 16/34/120) | 958 | 56% | +450 | +0.47 | +430 | +2.4 | +123 / +74 / +232 | robust | Flip 313 / -3 · LTF20 374 / +249 · HTF9 168 / +145 · HTF20 103 / +58
| H+ HTF 9 / 34 (slow line much slower, chart 16/34/120) | 931 | 56% | +459 | +0.49 | +440 | +2.5 | +181 / +83 / +176 | robust | Flip 299 / -31 · LTF20 370 / +211 · HTF9 171 / +204 · HTF20 91 / +74
| I+ HTF 7 / 20 (fast line faster, chart 16/34/120) | 1016 | 55% | +369 | +0.36 | +349 | +2.1 | +88 / +131 / +130 | robust | Flip 313 / -3 · LTF20 377 / +288 · HTF9 201 / -34 · HTF20 125 / +118
| J+ HTF 12 / 20 (fast line slower, chart 16/34/120) | 996 | 55% | +361 | +0.36 | +342 | +1.9 | +188 / +57 / +97 | promising | Flip 313 / -3 · LTF20 404 / +283 · HTF9 179 / -13 · HTF20 100 / +94
| Reference: HTF EMA9 Pierce trigger OFF | 1086 | 51% | -68 | -0.06 | -88 | -1.0 | -28 / -9 / -51 | worse | Flip 317 / -34 · LTF20 629 / -94 · HTF9 0 / +0 · HTF20 140 / +60
| Reference: HTF EMA20 Pierce trigger OFF | 1124 | 51% | -22 | -0.02 | -42 | -0.6 | -43 / -10 / +11 | worse | Flip 317 / -34 · LTF20 605 / -73 · HTF9 202 / +85 · HTF20 0 / +0
| Reference: both HTF EMA pierce triggers OFF | 977 | 51% | -130 | -0.13 | -149 | -1.3 | -70 / -4 / -75 | worse | Flip 317 / -34 · LTF20 660 / -96 · HTF9 0 / +0 · HTF20 0 / +0

Candidates: A+ HTF 9 / 20 → +504, z +3.2, +200 / +136 / +168 (robust); B+ HTF 7 / 16 → +276, z +1.5, +25 / +107 / +144 (promising); C+ HTF 8 / 18 → +392, z +2.2, +75 / +148 / +169 (robust); E+ HTF 12 / 26 → +277, z +1.4, +116 / +3 / +158 (promising); F+ HTF 14 / 30 → +203, z +1.0, +73 / +10 / +120 (promising); G+ HTF 9 / 26 → +430, z +2.4, +123 / +74 / +232 (robust); H+ HTF 9 / 34 → +440, z +2.5, +181 / +83 / +176 (robust); I+ HTF 7 / 20 → +349, z +2.1, +88 / +131 / +130 (robust); J+ HTF 12 / 20 → +342, z +1.9, +188 / +57 / +97 (promising)


## MGC 5m — HTF 25m EMAs (61531 candles, chart EMAs 9 / 20 / 200)

Check: recomputed HTF EMA20 vs BarFeed value — median gap 0.00 typical candle moves (after the first 200 HTF candles: 0.00)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A HTF 9 / 20 (standard) | 1195 | 51% | -102 | -0.09 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 326 / +71 · LTF20 579 / -66 · HTF9 178 / -85 · HTF20 112 / -23
| B HTF 7 / 16 (faster) | 1265 | 51% | -73 | -0.06 | +29 | +0.2 | +113 / -67 / -17 | noise | Flip 326 / +71 · LTF20 608 / -116 · HTF9 208 / -54 · HTF20 123 / +26
| C HTF 8 / 18 (slightly faster) | 1223 | 51% | -104 | -0.09 | -2 | -0.0 | +112 / -49 / -66 | worse | Flip 326 / +71 · LTF20 588 / -101 · HTF9 189 / -76 · HTF20 120 / +1
| D HTF 5 / 12 (much faster) | 1377 | 51% | -52 | -0.04 | +50 | +0.3 | -31 / +12 / +69 | noise | Flip 331 / +62 · LTF20 643 / -51 · HTF9 245 / -44 · HTF20 158 / -18
| E HTF 12 / 26 (slower) | 1188 | 52% | +15 | +0.01 | +117 | +0.9 | +50 / +32 / +35 | noise | Flip 331 / +63 · LTF20 583 / -120 · HTF9 174 / +18 · HTF20 100 / +54
| F HTF 14 / 30 (slower) | 1150 | 53% | +201 | +0.18 | +304 | +2.1 | +139 / -6 / +170 | noise | Flip 333 / +61 · LTF20 561 / +41 · HTF9 169 / +90 · HTF20 87 / +10
| G HTF 9 / 26 (slow line slower) | 1192 | 51% | -24 | -0.02 | +78 | +0.8 | +77 / +4 / -4 | noise | Flip 331 / +63 · LTF20 568 / -73 · HTF9 189 / -73 · HTF20 104 / +59
| H HTF 9 / 34 (slow line much slower) | 1133 | 51% | -143 | -0.13 | -41 | -0.3 | -23 / -37 / +19 | worse | Flip 334 / +54 · LTF20 546 / -43 · HTF9 183 / -88 · HTF20 70 / -65
| I HTF 7 / 20 (fast line faster) | 1213 | 52% | -29 | -0.02 | +73 | +0.7 | +52 / -31 / +53 | noise | Flip 326 / +71 · LTF20 576 / -38 · HTF9 194 / -65 · HTF20 117 / +3
| J HTF 12 / 20 (fast line slower) | 1194 | 52% | -56 | -0.05 | +46 | +0.5 | -27 / +49 / +24 | noise | Flip 326 / +71 · LTF20 595 / -103 · HTF9 174 / -45 · HTF20 99 / +22
| Reference: HTF EMA9 Pierce trigger OFF | 1083 | 52% | +17 | +0.02 | +119 | +1.3 | +52 / -9 / +76 | noise | Flip 326 / +71 · LTF20 616 / -43 · HTF9 0 / +0 · HTF20 141 / -11
| Reference: HTF EMA20 Pierce trigger OFF | 1117 | 51% | -93 | -0.08 | +9 | +0.1 | +22 / -18 / +5 | noise | Flip 326 / +71 · LTF20 600 / -76 · HTF9 191 / -88 · HTF20 0 / +0
| Reference: both HTF EMA pierce triggers OFF | 974 | 52% | -16 | -0.02 | +86 | +0.7 | +75 / -63 / +73 | noise | Flip 326 / +71 · LTF20 648 / -87 · HTF9 0 / +0 · HTF20 0 / +0

Candidates: none

