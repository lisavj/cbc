# HTF EMA length study -- 2026-11-12 09:58 ET (run 7)

## Since last run (11/09, run 6)

Settings sync (11/12 09:45 ET): no mismatches (v10.87), study settings current. No 11/11 HTF run was written, so this is run 7 and compares with run 6 (11/09). Replay window Jan 5 → latest archived bar (~1,200 more 3m / ~730 more 5m candles since run 6, all in the last third Jul–Nov).

- **MES 3m:** standard +2 (was +21). Nothing robust. Promising: both pierces off +198 (z 1.6, +42 / +56 / +100; was +176, z 1.4); HTF EMA9 Pierce off +154 (z 1.6, +25 / +55 / +73; was +137, z 1.5); HTF 7 / 16 +152 (z 1.1, +39 / +44 / +69; was +148, z 1.1); HTF 12 / 20 +123 (z 1.3, +28 / +49 / +45; was +106, z 1.1); HTF 7 / 20 +102 (z 1.1, +43 / +26 / +33; was +96, z 1.0); HTF 9 / 26 newly promising +99 (z 1.0, +29 / +35 / +36; was noise +86). Consecutive robust runs: 0 for all. Replay HTF EMA9 Pierce setups 289 · −150 (was 284 · −129).
- **MGC 3m:** standard +312 (was +287). Nothing robust or promising. Faster HTF still clearly worse (8 / 18 −305, z −2.8; 7 / 16 −263, z −1.9).
- **MES 5m:** standard +37 (was +6). With chart 9 / 20 / 200 every HTF change is worse or noise; pierce-off references all worse. Robust rows are all chart-EMA 16 / 34 / 120 combos: A+ (HTF 9 / 20) +490 (z 3.1, +200 / +136 / +154; was +496, z 3.2), H+ 9 / 34 +425 (z 2.4, +181 / +83 / +162; was +436, z 2.5), G+ 9 / 26 +415 (z 2.4, +123 / +74 / +218; was +440, z 2.5), C+ 8 / 18 +377 (z 2.1, +75 / +148 / +155; was +375, z 2.1) — each robust **7 runs in a row** (11/01–11/12, 11 days); I+ 7 / 20 +335 (z 2.0, +88 / +131 / +115) robust **3 runs in a row** (11/07–11/12, 5 days). J+ 12 / 20 still promising (+335, z 1.9). HTF 9 / 20 remains the best + row, so this is a chart-EMA signal (5m chart EMAs 16 / 34 / 120, separate chart-EMA study), not an HTF-length one.
- **MGC 5m:** standard −111 (was −121). Nothing robust or promising. Best still HTF 14 / 30 +299 (z 2.0 now, but Apr–Jun −6 → noise; was +276, z 1.9); HTF EMA9 Pierce off +114 (z 1.3, Apr–Jun −9, noise).

**Live HTF pierce setups** (alert store through 11/12 15:00 UTC, 44,319 alerts, matched to the first Setup Ended after each setup):

| Chart | Trigger | Setups | Ended | Win % | Net | Avg | vs 11/09 |
|---|---|---|---|---|---|---|---|
| MES 3m | HTF EMA9 Pierce | 15 | 14 | 43% | +4.8 | +0.34 | unchanged |
| MES 3m | HTF EMA20 Pierce | 10 | 8 | 38% | −5.1 | −0.63 | unchanged |
| MGC 3m | HTF EMA9 Pierce | 16 | 14 | 57% | +11.0 | +0.79 | +3 ended, net −0.8 → +11.0 |
| MGC 3m | HTF EMA20 Pierce | 14 | 13 | 38% | −20.9 | −1.61 | +3 ended, net −5.9 → −20.9 |
| MES 5m | HTF EMA9 Pierce | 4 | 2 | 0% | −13.5 | −6.75 | +1 setup (not ended) |
| MES 5m | HTF EMA20 Pierce | 9 | 8 | 62% | +4.9 | +0.61 | +1 setup (not ended) |
| MGC 5m | HTF EMA9 Pierce | 13 | 11 | 73% | +32.7 | +2.97 | +3 ended, net +9.7 → +32.7 |
| MGC 5m | HTF EMA20 Pierce | 9 | 8 | 50% | +2.1 | +0.26 | +4 ended, net +3.3 → +2.1 |

No trigger has the 20 ended live setups the verdict rule needs.

**Verdict:** keep HTF 9 / 20 on all four charts. No HTF-length or pierce-off variation is robust on any chart with the live chart EMAs. On MES 5m the 16 / 34 / 120 rows (A+, C+, G+, H+) pass (a) (7 runs, 11 days) and (b), but fail (c) — MES 5m live HTF pierce setups have only 2 / 8 ended and HTF EMA20 Pierce is net positive — and the best of them keeps HTF 9 / 20, so they point at a chart-EMA change (separate study), not an HTF change. A different HTF length would need a new CBC version with "HTF EMA fast / slow" inputs; turning a pierce trigger off is already a CBC input (② Setup Triggers). Watch on MES 3m: both pierces off and HTF EMA9 Pierce off (z 1.6 each, climbing), HTF 12 / 20 (z 1.3), HTF 7 / 16 and 7 / 20 (z 1.1), HTF 9 / 26 (z 1.0) — all promising, none robust. Watch on MGC 3m live: HTF EMA20 Pierce now −20.9 over 13 ended (the replay says turning it off is worse, z −1.1).

---

## MES 3m — HTF 15m EMAs (102145 candles, chart EMAs 9 / 20 / 200, range gate on)

Check: recomputed HTF EMA20 vs BarFeed value — median gap 0.00 typical candle moves (after the first 200 HTF candles: 0.00)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A HTF 9 / 20 (standard) | 1752 | 50% | +2 | +0.00 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 319 / +58 · LTF20 960 / +101 · HTF9 289 / -150 · HTF20 184 / -7
| B HTF 7 / 16 (faster) | 1831 | 51% | +154 | +0.08 | +152 | +1.1 | +39 / +44 / +69 | promising | Flip 315 / +59 · LTF20 1005 / +33 · HTF9 309 / -5 · HTF20 202 / +66
| C HTF 8 / 18 (slightly faster) | 1804 | 49% | -64 | -0.04 | -66 | -0.6 | +14 / -31 / -50 | worse | Flip 317 / +58 · LTF20 973 / +19 · HTF9 318 / -178 · HTF20 196 / +36
| D HTF 5 / 12 (much faster) | 1904 | 50% | -66 | -0.03 | -67 | -0.4 | -47 / -63 / +43 | worse | Flip 315 / +49 · LTF20 1027 / +98 · HTF9 341 / -105 · HTF20 221 / -108
| E HTF 12 / 26 (slower) | 1627 | 50% | +108 | +0.07 | +106 | +0.8 | -19 / +74 / +51 | noise | Flip 323 / +67 · LTF20 935 / +45 · HTF9 250 / -63 · HTF20 119 / +59
| F HTF 14 / 30 (slower) | 1566 | 51% | +103 | +0.07 | +101 | +0.7 | +26 / +101 / -26 | noise | Flip 326 / +73 · LTF20 913 / +2 · HTF9 242 / +35 · HTF20 85 / -7
| G HTF 9 / 26 (slow line slower) | 1650 | 51% | +101 | +0.06 | +99 | +1.0 | +29 / +35 / +36 | promising | Flip 323 / +67 · LTF20 932 / +48 · HTF9 271 / -118 · HTF20 124 / +105
| H HTF 9 / 34 (slow line much slower) | 1588 | 50% | -4 | -0.00 | -6 | -0.1 | -41 / +73 / -38 | worse | Flip 328 / +60 · LTF20 899 / +89 · HTF9 261 / -134 · HTF20 100 / -19
| I HTF 7 / 20 (fast line faster) | 1766 | 50% | +104 | +0.06 | +102 | +1.1 | +43 / +26 / +33 | promising | Flip 319 / +58 · LTF20 957 / +70 · HTF9 298 / -8 · HTF20 192 / -17
| J HTF 12 / 20 (fast line slower) | 1711 | 50% | +124 | +0.07 | +123 | +1.3 | +28 / +49 / +45 | promising | Flip 319 / +58 · LTF20 967 / +106 · HTF9 262 / -45 · HTF20 163 / +5
| Reference: HTF EMA9 Pierce trigger OFF | 1563 | 51% | +156 | +0.10 | +154 | +1.6 | +25 / +55 / +73 | promising | Flip 319 / +58 · LTF20 1009 / +126 · HTF9 0 / +0 · HTF20 235 / -28
| Reference: HTF EMA20 Pierce trigger OFF | 1616 | 50% | +7 | +0.00 | +6 | +0.1 | +13 / -10 / +3 | noise | Flip 319 / +58 · LTF20 1004 / +109 · HTF9 293 / -159 · HTF20 0 / +0
| Reference: both HTF EMA pierce triggers OFF | 1383 | 51% | +200 | +0.14 | +198 | +1.6 | +42 / +56 / +100 | promising | Flip 319 / +58 · LTF20 1064 / +142 · HTF9 0 / +0 · HTF20 0 / +0

Candidates: B HTF 7 / 16 → +152, z +1.1, +39 / +44 / +69 (promising); G HTF 9 / 26 → +99, z +1.0, +29 / +35 / +36 (promising); I HTF 7 / 20 → +102, z +1.1, +43 / +26 / +33 (promising); J HTF 12 / 20 → +123, z +1.3, +28 / +49 / +45 (promising); HTF EMA9 Pierce trigger OFF  → +154, z +1.6, +25 / +55 / +73 (promising); both HTF EMA pierce triggers OFF  → +198, z +1.6, +42 / +56 / +100 (promising)

## MGC 3m — HTF 15m EMAs (101926 candles, chart EMAs 9 / 20 / 200, range gate on), VWAP stretch 4 ATR

Check: recomputed HTF EMA20 vs BarFeed value — median gap 0.00 typical candle moves (after the first 200 HTF candles: 0.00)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A HTF 9 / 20 (standard) | 1192 | 51% | +312 | +0.26 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 213 / +121 · LTF20 609 / +168 · HTF9 196 / -84 · HTF20 174 / +107
| B HTF 7 / 16 (faster) | 1292 | 48% | +49 | +0.04 | -263 | -1.9 | -78 / -36 / -150 | worse | Flip 213 / +121 · LTF20 664 / +147 · HTF9 217 / -82 · HTF20 198 / -137
| C HTF 8 / 18 (slightly faster) | 1247 | 48% | +7 | +0.01 | -305 | -2.8 | -93 / -105 / -106 | worse | Flip 214 / +114 · LTF20 628 / +155 · HTF9 205 / -143 · HTF20 200 / -119
| D HTF 5 / 12 (much faster) | 1436 | 50% | +308 | +0.21 | -4 | -0.0 | +33 / -103 / +67 | worse | Flip 211 / +124 · LTF20 714 / +94 · HTF9 265 / -10 · HTF20 246 / +99
| E HTF 12 / 26 (slower) | 1163 | 51% | +342 | +0.29 | +30 | +0.2 | +37 / +8 / -15 | noise | Flip 220 / +137 · LTF20 589 / +136 · HTF9 211 / +34 · HTF20 143 / +35
| F HTF 14 / 30 (slower) | 1122 | 51% | +267 | +0.24 | -45 | -0.3 | +48 / -4 / -89 | worse | Flip 221 / +131 · LTF20 570 / +188 · HTF9 211 / +36 · HTF20 120 / -88
| G HTF 9 / 26 (slow line slower) | 1152 | 51% | +339 | +0.29 | +27 | +0.3 | +26 / +45 / -44 | noise | Flip 220 / +137 · LTF20 590 / +158 · HTF9 192 / -50 · HTF20 150 / +93
| H HTF 9 / 34 (slow line much slower) | 1060 | 51% | +268 | +0.25 | -44 | -0.4 | -27 / +38 / -55 | worse | Flip 222 / +136 · LTF20 535 / +159 · HTF9 176 / -32 · HTF20 127 / +5
| I HTF 7 / 20 (fast line faster) | 1189 | 50% | +291 | +0.24 | -21 | -0.2 | -18 / +17 / -20 | worse | Flip 213 / +121 · LTF20 607 / +164 · HTF9 189 / -47 · HTF20 180 / +53
| J HTF 12 / 20 (fast line slower) | 1193 | 50% | +298 | +0.25 | -13 | -0.1 | -4 / -26 / +17 | worse | Flip 213 / +121 · LTF20 611 / +148 · HTF9 222 / -25 · HTF20 147 / +54
| Reference: HTF EMA9 Pierce trigger OFF | 1066 | 51% | +343 | +0.32 | +31 | +0.4 | +58 / -19 / -8 | noise | Flip 213 / +121 · LTF20 637 / +133 · HTF9 0 / +0 · HTF20 216 / +88
| Reference: HTF EMA20 Pierce trigger OFF | 1056 | 50% | +221 | +0.21 | -91 | -1.1 | -75 / +15 / -31 | worse | Flip 213 / +121 · LTF20 635 / +163 · HTF9 208 / -64 · HTF20 0 / +0
| Reference: both HTF EMA pierce triggers OFF | 892 | 51% | +263 | +0.30 | -49 | -0.4 | -11 / -6 / -31 | worse | Flip 213 / +121 · LTF20 679 / +142 · HTF9 0 / +0 · HTF20 0 / +0

Candidates: none

## MES 5m — HTF 25m EMAs (61288 candles, chart EMAs 9 / 20 / 200)

Check: recomputed HTF EMA20 vs BarFeed value — median gap 0.00 typical candle moves (after the first 200 HTF candles: 0.00)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A HTF 9 / 20 (standard) | 1204 | 51% | +37 | +0.03 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 317 / -34 · LTF20 587 / -59 · HTF9 191 / +64 · HTF20 109 / +66
| B HTF 7 / 16 (faster) | 1247 | 50% | -74 | -0.06 | -111 | -0.9 | -61 / -44 / -7 | worse | Flip 317 / -34 · LTF20 614 / -74 · HTF9 180 / -61 · HTF20 136 / +95
| C HTF 8 / 18 (slightly faster) | 1222 | 51% | -24 | -0.02 | -61 | -0.6 | -63 / -2 / +3 | worse | Flip 317 / -34 · LTF20 601 / -122 · HTF9 176 / +86 · HTF20 128 / +46
| D HTF 5 / 12 (much faster) | 1316 | 50% | -181 | -0.14 | -218 | -1.4 | +61 / -95 / -184 | worse | Flip 317 / -34 · LTF20 629 / -105 · HTF9 239 / +40 · HTF20 131 / -82
| E HTF 12 / 26 (slower) | 1144 | 51% | -19 | -0.02 | -56 | -0.4 | +5 / -61 / -0 | worse | Flip 320 / -29 · LTF20 573 / -57 · HTF9 161 / -35 · HTF20 90 / +103
| F HTF 14 / 30 (slower) | 1116 | 51% | -61 | -0.05 | -98 | -0.7 | -63 / -25 / -11 | worse | Flip 321 / -23 · LTF20 567 / -111 · HTF9 140 / -34 · HTF20 88 / +106
| G HTF 9 / 26 (slow line slower) | 1158 | 52% | +42 | +0.04 | +5 | +0.1 | -41 / -37 / +82 | noise | Flip 320 / -29 · LTF20 555 / -81 · HTF9 185 / +69 · HTF20 98 / +84
| H HTF 9 / 34 (slow line much slower) | 1129 | 52% | +74 | +0.07 | +37 | +0.3 | +27 / -20 / +31 | noise | Flip 322 / -31 · LTF20 536 / -90 · HTF9 181 / +129 · HTF20 90 / +66
| I HTF 7 / 20 (fast line faster) | 1190 | 51% | -14 | -0.01 | -51 | -0.6 | -23 / +15 / -43 | worse | Flip 317 / -34 · LTF20 588 / -34 · HTF9 166 / -69 · HTF20 119 / +122
| J HTF 12 / 20 (fast line slower) | 1184 | 51% | -2 | -0.00 | -39 | -0.4 | +69 / -25 / -83 | worse | Flip 317 / -34 · LTF20 600 / -24 · HTF9 177 / -37 · HTF20 90 / +93
| A+ HTF 9 / 20 (standard, chart 16/34/120) | 1001 | 56% | +527 | +0.53 | +490 | +3.1 | +200 / +136 / +154 | robust | Flip 313 / -3 · LTF20 388 / +297 · HTF9 178 / +152 · HTF20 122 / +81
| B+ HTF 7 / 16 (faster, chart 16/34/120) | 1052 | 54% | +299 | +0.28 | +261 | +1.4 | +25 / +107 / +129 | promising | Flip 312 / -8 · LTF20 385 / +314 · HTF9 215 / -19 · HTF20 140 / +12
| C+ HTF 8 / 18 (slightly faster, chart 16/34/120) | 1024 | 56% | +415 | +0.40 | +377 | +2.1 | +75 / +148 / +155 | robust | Flip 312 / -8 · LTF20 379 / +232 · HTF9 194 / +157 · HTF20 139 / +35
| D+ HTF 5 / 12 (much faster, chart 16/34/120) | 1235 | 52% | +63 | +0.05 | +26 | +0.1 | +35 / -49 / +40 | noise | Flip 311 / -13 · LTF20 386 / +240 · HTF9 418 / -122 · HTF20 120 / -42
| E+ HTF 12 / 26 (slower, chart 16/34/120) | 954 | 55% | +308 | +0.32 | +271 | +1.4 | +116 / +3 / +152 | promising | Flip 313 / -3 · LTF20 388 / +241 · HTF9 158 / -1 · HTF20 95 / +72
| F+ HTF 14 / 30 (slower, chart 16/34/120) | 934 | 54% | +226 | +0.24 | +188 | +1.0 | +73 / +10 / +106 | noise | Flip 306 / -17 · LTF20 397 / +195 · HTF9 146 / -34 · HTF20 85 / +81
| G+ HTF 9 / 26 (slow line slower, chart 16/34/120) | 956 | 56% | +453 | +0.47 | +415 | +2.4 | +123 / +74 / +218 | robust | Flip 313 / -3 · LTF20 372 / +252 · HTF9 168 / +145 · HTF20 103 / +58
| H+ HTF 9 / 34 (slow line much slower, chart 16/34/120) | 929 | 56% | +463 | +0.50 | +425 | +2.4 | +181 / +83 / +162 | robust | Flip 299 / -31 · LTF20 368 / +214 · HTF9 171 / +204 · HTF20 91 / +74
| I+ HTF 7 / 20 (fast line faster, chart 16/34/120) | 1014 | 55% | +372 | +0.37 | +335 | +2.0 | +88 / +131 / +115 | robust | Flip 313 / -3 · LTF20 375 / +291 · HTF9 201 / -34 · HTF20 125 / +118
| J+ HTF 12 / 20 (fast line slower, chart 16/34/120) | 993 | 55% | +373 | +0.38 | +335 | +1.9 | +188 / +57 / +91 | promising | Flip 313 / -3 · LTF20 402 / +286 · HTF9 178 / -5 · HTF20 100 / +94
| Reference: HTF EMA9 Pierce trigger OFF | 1083 | 51% | -46 | -0.04 | -83 | -0.9 | -28 / -9 / -46 | worse | Flip 317 / -34 · LTF20 626 / -72 · HTF9 0 / +0 · HTF20 140 / +60
| Reference: HTF EMA20 Pierce trigger OFF | 1120 | 51% | -4 | -0.00 | -42 | -0.6 | -43 / -10 / +11 | worse | Flip 317 / -34 · LTF20 602 / -51 · HTF9 201 / +80 · HTF20 0 / +0
| Reference: both HTF EMA pierce triggers OFF | 974 | 51% | -107 | -0.11 | -144 | -1.3 | -70 / -4 / -71 | worse | Flip 317 / -34 · LTF20 657 / -73 · HTF9 0 / +0 · HTF20 0 / +0

Candidates: A+ HTF 9 / 20 → +490, z +3.1, +200 / +136 / +154 (robust); B+ HTF 7 / 16 → +261, z +1.4, +25 / +107 / +129 (promising); C+ HTF 8 / 18 → +377, z +2.1, +75 / +148 / +155 (robust); E+ HTF 12 / 26 → +271, z +1.4, +116 / +3 / +152 (promising); G+ HTF 9 / 26 → +415, z +2.4, +123 / +74 / +218 (robust); H+ HTF 9 / 34 → +425, z +2.4, +181 / +83 / +162 (robust); I+ HTF 7 / 20 → +335, z +2.0, +88 / +131 / +115 (robust); J+ HTF 12 / 20 → +335, z +1.9, +188 / +57 / +91 (promising)

## MGC 5m — HTF 25m EMAs (61156 candles, chart EMAs 9 / 20 / 200)

Check: recomputed HTF EMA20 vs BarFeed value — median gap 0.00 typical candle moves (after the first 200 HTF candles: 0.00)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A HTF 9 / 20 (standard) | 1191 | 51% | -111 | -0.09 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 324 / +73 · LTF20 578 / -82 · HTF9 177 / -80 · HTF20 112 / -23
| B HTF 7 / 16 (faster) | 1260 | 51% | -86 | -0.07 | +25 | +0.2 | +113 / -67 / -21 | noise | Flip 324 / +73 · LTF20 606 / -126 · HTF9 207 / -59 · HTF20 123 / +26
| C HTF 8 / 18 (slightly faster) | 1218 | 51% | -107 | -0.09 | +5 | +0.0 | +112 / -49 / -59 | noise | Flip 324 / +73 · LTF20 587 / -117 · HTF9 187 / -64 · HTF20 120 / +1
| D HTF 5 / 12 (much faster) | 1369 | 51% | -57 | -0.04 | +55 | +0.3 | -31 / +12 / +74 | noise | Flip 329 / +64 · LTF20 640 / -55 · HTF9 242 / -47 · HTF20 158 / -18
| E HTF 12 / 26 (slower) | 1185 | 52% | +1 | +0.00 | +112 | +0.8 | +50 / +32 / +30 | noise | Flip 329 / +65 · LTF20 582 / -137 · HTF9 174 / +18 · HTF20 100 / +54
| F HTF 14 / 30 (slower) | 1147 | 53% | +187 | +0.16 | +299 | +2.0 | +139 / -6 / +165 | noise | Flip 331 / +63 · LTF20 560 / +25 · HTF9 169 / +90 · HTF20 87 / +10
| G HTF 9 / 26 (slow line slower) | 1188 | 51% | -34 | -0.03 | +78 | +0.8 | +77 / +4 / -4 | noise | Flip 329 / +65 · LTF20 567 / -90 · HTF9 188 / -68 · HTF20 104 / +59
| H HTF 9 / 34 (slow line much slower) | 1128 | 51% | -158 | -0.14 | -46 | -0.4 | -23 / -37 / +14 | worse | Flip 332 / +56 · LTF20 545 / -60 · HTF9 182 / -83 · HTF20 69 / -71
| I HTF 7 / 20 (fast line faster) | 1209 | 51% | -48 | -0.04 | +63 | +0.6 | +52 / -31 / +43 | noise | Flip 324 / +73 · LTF20 575 / -54 · HTF9 193 / -70 · HTF20 117 / +3
| J HTF 12 / 20 (fast line slower) | 1191 | 52% | -70 | -0.06 | +41 | +0.4 | -27 / +49 / +19 | noise | Flip 324 / +73 · LTF20 594 / -120 · HTF9 174 / -45 · HTF20 99 / +22
| Reference: HTF EMA9 Pierce trigger OFF | 1080 | 52% | +2 | +0.00 | +114 | +1.3 | +52 / -9 / +71 | noise | Flip 324 / +73 · LTF20 615 / -60 · HTF9 0 / +0 · HTF20 141 / -11
| Reference: HTF EMA20 Pierce trigger OFF | 1113 | 51% | -102 | -0.09 | +9 | +0.1 | +22 / -18 / +5 | noise | Flip 324 / +73 · LTF20 599 / -92 · HTF9 190 / -83 · HTF20 0 / +0
| Reference: both HTF EMA pierce triggers OFF | 971 | 52% | -30 | -0.03 | +81 | +0.7 | +75 / -63 / +68 | noise | Flip 324 / +73 · LTF20 647 / -103 · HTF9 0 / +0 · HTF20 0 / +0

Candidates: none

