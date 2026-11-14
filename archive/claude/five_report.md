# 5m charts (MES / MGC / MNQ / M2K) -- CBC EMA Slope branch studies -- 11/14/2026

## Verdict
- MES 5m: v10.97 1544 / -873 -> slope 0.70 + VWAP stretch 4: 228 / +248, z 5.1 vs v10.97, thirds +407 / +293 / +421 (change), max DD 46 vs 877. Plateau: slope 0.60-0.80 with stretch 4 all +239 to +249.
- MGC 5m: v10.97 1576 / -238 -> slope 0.48: 628 / +512, z 3.6, max DD 118 vs 298 (plateau 0.42-0.60). Candidate on top: Max SL1 cap 7 -> 12 (+155; cap off +191 robust except last 4 wk).
- MNQ 5m: v10.97 already +1428. Slope filter = noise at every value (middle third negative); FLIP 0 % = worse on v10.97. Keep v10.97 settings.
- M2K 5m: v10.97 1459 / -364 -> slope 1.00 + 50 % at TP1: 216 / +86, z 3.6; plateau slope 0.90-1.20. Thin edge (+0.4 pts / trade): chart only, not the bot.
- Not combined here: open ledger items C-011 (MES 5m chart EMAs 16/34/120) and C-012 (MES 5m ER 0.18), both from v10.97-era studies.

# MES 5m -- CBC EMA Slope branch studies -- 11/14/2026

Replay Jan 5 -> Nov 13, MES 5m (HTF = 25m), net after 0.50 pts cost. v10.97 / v1.10 5m settings (no 5m entries in any per-chart list): ER 0.23 + breakout 3, no range gate / stretch / slope, toward late-away 1 pt, flip distance max(2 ATR, 8 pts), SL1 1.7 ATR min 5 cap 8, TP1 1.7 ATR cap 6, 80 % at TP1 + BE + trail 1.7, no setups 16:00-18:45 + OR forming blocks, end at 16:00. In-sample.

## 0. v10.97 baseline

Trades 1544, net -873, avg -0.57, win 50 %, thirds -353 / -194 / -325, last 4 wk -92, max DD 877

By trigger: flip 343 / -194 · ltf20 765 / -467 · h9 251 / -153 · h20 185 / -58

By session: Asia 543 / -167 · London 508 / -377 · NY AM 194 / -188 · NY PM 296 / -130

## 1. HTF EMA20 slope filter (vs v10.97)

Base: 1544 trades, net -873, avg -0.57, thirds -353 / -194 / -325, last 4 wk -92, max DD 877

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.20 | 1142 | -280 | +592 | +4.1 | +291 / +108 / +193 | +32 | 324 | robust |
| slope 0.30 | 943 | -249 | +624 | +3.7 | +226 / +180 / +218 | +42 | 302 | robust |
| slope 0.42 | 775 | -162 | +711 | +3.9 | +242 / +140 / +329 | +62 | 276 | robust |
| slope 0.48 | 677 | -71 | +801 | +4.2 | +279 / +169 / +353 | +69 | 208 | robust |
| slope 0.55 | 593 | -30 | +842 | +4.3 | +311 / +176 / +355 | +57 | 166 | robust |
| slope 0.60 | 523 | +43 | +915 | +4.5 | +311 / +228 / +376 | +75 | 118 | robust |
| slope 0.65 | 467 | +28 | +901 | +4.4 | +295 / +254 / +352 | +79 | 119 | robust |
| slope 0.70 | 400 | +66 | +939 | +4.5 | +319 / +270 / +350 | +90 | 118 | robust |
| slope 0.75 | 354 | +64 | +936 | +4.4 | +334 / +257 / +345 | +94 | 109 | robust |
| slope 0.80 | 300 | +63 | +935 | +4.3 | +338 / +245 / +352 | +97 | 97 | robust |
| slope 0.90 | 230 | +20 | +892 | +4.1 | +345 / +184 / +363 | +72 | 76 | robust |
| slope 1.00 | 173 | -9 | +864 | +3.9 | +316 / +184 / +363 | +93 | 68 | robust |

## 2. Ideas on top of slope 0.75

Base: 354 trades, net +64, avg +0.18, thirds -19 / +63 / +20, last 4 wk +2, max DD 109

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back | 354 | +49 | -15 | -0.4 | +3 / -30 / +12 | -4 | 140 | worse |
| FLIP 0 % exit (0 % at TP1, BE, HTF flip) | 338 | +238 | +174 | +2.2 | +147 / -82 / +109 | +117 | 119 | noise |
| 100 % at TP1 | 377 | +13 | -51 | -0.6 | -57 / -19 / +24 | +7 | 117 | worse |
| 50 % at TP1 | 354 | +130 | +66 | +0.9 | +58 / +18 / -10 | -6 | 112 | noise |
| Range gate 5 ATR | 293 | +22 | -42 | -0.8 | +15 / -34 / -23 | -21 | 91 | worse |
| VWAP stretch 4 ATR | 188 | +239 | +175 | +2.3 | +92 / +31 / +53 | +10 | 53 | robust |
| LTF pierce min ER 0.12 | 312 | +47 | -17 | -0.4 | +14 / -22 / -9 | -5 | 86 | worse |
| LTF pierce min ER 0.15 | 290 | +42 | -21 | -0.4 | +17 / -26 / -12 | -1 | 91 | worse |
| LTF pierce min ER 0.20 | 260 | +36 | -28 | -0.5 | +18 / -26 / -20 | -4 | 93 | worse |
| LTF pierce min ER 0.23 | 247 | +31 | -33 | -0.5 | +17 / -34 / -16 | -12 | 93 | worse |
| Strict away flips (late-away OFF) | 317 | +55 | -9 | -0.3 | -6 / +4 / -7 | -4 | 89 | worse |
| Trigger HTF CBC Flip OFF | 311 | -24 | -87 | -1.8 | -44 / -20 / -24 | -11 | 97 | worse |
| Trigger LTF EMA20 Pierce OFF | 144 | +93 | +29 | +0.3 | +50 / -30 / +8 | -15 | 46 | noise |
| Trigger HTF EMA9 Pierce OFF | 307 | +27 | -37 | -0.8 | +15 / -40 / -12 | +10 | 103 | worse |
| Trigger HTF EMA20 Pierce OFF | 354 | +64 | +0 | +0.0 | +0 / +0 / +0 | +0 | 109 | noise |
| End setups at 16:00 OFF | 354 | +50 | -14 | -0.8 | -2 / -8 / -4 | +0 | 111 | worse |
| SL1 1.5 ATR | 355 | +30 | -34 | -0.9 | +4 / -33 / -4 | +5 | 108 | worse |
| SL1 2.5 ATR | 353 | +66 | +2 | +0.1 | +4 / -8 / +7 | -9 | 114 | noise |
| SL1 3.0 ATR | 353 | +72 | +8 | +0.2 | +16 / -10 / +2 | -12 | 102 | noise |
| TP1 1.5 ATR | 354 | +105 | +41 | +0.8 | +22 / +5 / +14 | +1 | 97 | noise |
| TP1 2.0 ATR | 353 | +77 | +13 | +0.3 | -5 / +6 / +12 | +1 | 115 | noise |
| TP1 2.5 ATR | 351 | +97 | +33 | +0.7 | +8 / +12 / +14 | +1 | 107 | noise |
| Max SL1 cap OFF | 354 | +132 | +68 | +1.9 | +65 / +16 / -13 | -5 | 75 | noise |
| Max TP1 cap OFF | 346 | +84 | +20 | +0.3 | +12 / -11 / +19 | +7 | 111 | noise |
| Trail 3.5 ATR | 339 | +69 | +6 | +0.1 | +1 / -21 / +26 | +20 | 111 | noise |
| Breakeven OFF | 349 | +72 | +8 | +0.2 | +6 / +2 / +0 | +3 | 110 | noise |
| CHOP > 58 block | 275 | +42 | -22 | -0.4 | +24 / -1 / -46 | -26 | 66 | worse |
| ADX < 20 block | 280 | +48 | -16 | -0.3 | -24 / +7 / +1 | +1 | 106 | worse |
| Crosses >= 4 block | 322 | -5 | -69 | -1.7 | -25 / -35 / -8 | +1 | 94 | worse |
| HTF flips >= 3 in 8 block | 327 | +16 | -48 | -1.4 | -15 / -10 / -24 | -12 | 109 | worse |
| Environment EMA200 vs VWAP | 74 | -37 | -100 | -1.1 | -24 / -19 / -57 | -3 | 62 | worse |
| ER 0.18 | 374 | +77 | +13 | +0.4 | +23 / -21 / +11 | -3 | 107 | noise |
| ER 0.30 | 327 | +47 | -17 | -0.5 | +6 / -19 / -4 | -0 | 98 | worse |

## 3. Final set vs v10.97: slope 0.75 + VWAP stretch 4 ATR

Base: 1544 trades, net -873, avg -0.57, thirds -353 / -194 / -325, last 4 wk -92, max DD 877

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| final | 188 | +239 | +1111 | +5.0 | +425 / +288 / +398 | +104 | 53 | robust |
| slope only | 354 | +64 | +936 | +4.4 | +334 / +257 / +345 | +94 | 109 | robust |

## 4. One-hour blocks on top of the final set

Base: 188 trades, net +239, avg +1.27, thirds +72 / +94 / +73, last 4 wk +12, max DD 53

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| block 18:00-19:00 | 181 | +258 | +19 | +1.3 | +16 / -2 / +6 | +5 | 49 | noise |
| block 19:00-20:00 | 171 | +258 | +19 | +0.8 | +11 / -1 / +9 | +6 | 55 | noise |
| block 20:00-21:00 | 178 | +221 | -17 | -0.8 | -3 / -4 / -10 | -11 | 50 | worse |
| block 21:00-22:00 | 169 | +213 | -26 | -0.9 | -7 / +6 / -25 | -13 | 46 | worse |
| block 22:00-23:00 | 178 | +233 | -6 | -0.3 | +1 / -3 / -3 | +0 | 49 | worse |
| block 23:00-00:00 | 176 | +225 | -13 | -0.7 | -12 / -1 / +0 | +0 | 48 | worse |
| block 00:00-01:00 | 179 | +215 | -24 | -1.5 | -2 / -19 / -3 | +0 | 54 | worse |
| block 01:00-02:00 | 180 | +209 | -30 | -1.8 | -10 / -12 / -8 | -8 | 53 | worse |
| block 02:00-03:00 | 179 | +240 | +1 | +0.0 | +0 / -3 / +3 | +0 | 49 | noise |
| block 03:00-04:00 | 186 | +238 | -1 | -0.1 | -4 / +4 / +0 | +0 | 53 | worse |
| block 04:00-05:00 | 184 | +233 | -6 | -0.5 | +4 / -5 / -5 | +0 | 53 | worse |
| block 05:00-06:00 | 183 | +215 | -24 | -1.7 | -9 / -15 / +0 | +0 | 48 | worse |
| block 06:00-07:00 | 185 | +243 | +4 | +0.5 | +10 / -6 / +0 | +0 | 53 | noise |
| block 07:00-08:00 | 179 | +218 | -21 | -1.3 | +1 / -25 / +2 | +7 | 53 | worse |
| block 08:00-09:00 | 185 | +260 | +21 | +1.4 | +6 / +9 / +7 | +0 | 44 | promising |
| block 09:00-10:00 | 181 | +232 | -7 | -0.5 | -15 / +8 / -1 | +0 | 58 | worse |
| block 10:00-11:00 | 180 | +186 | -53 | -3.4 | +0 / -28 / -25 | +0 | 53 | worse |
| block 11:00-12:00 | 178 | +230 | -9 | -0.5 | -17 / -9 / +16 | -3 | 53 | worse |
| block 12:00-13:00 | 181 | +221 | -17 | -1.2 | -9 / -0 / -9 | +0 | 44 | worse |
| block 13:00-14:00 | 178 | +241 | +2 | +0.1 | -11 / +13 / +1 | +4 | 44 | noise |
| block 14:00-15:00 | 181 | +208 | -31 | -2.1 | -13 / -9 / -9 | +0 | 53 | robustly worse |
| block 15:00-16:00 | 185 | +231 | -8 | -0.8 | -5 / +0 / -3 | -4 | 53 | worse |

## 5. Sessions (final vs v10.97)

| Session | v10.97 trades / net | final trades / net |
|---|---|---|
| Asia | 543 / -167 | 107 / +101 |
| London | 508 / -377 | 33 / -2 |
| NY AM | 194 / -188 | 21 / +87 |
| NY PM | 296 / -130 | 27 / +54 |


# MGC 5m -- CBC EMA Slope branch studies -- 11/14/2026

Replay Jan 5 -> Nov 13, MGC 5m (HTF = 25m), net after 0.22 pts cost. v10.97 / v1.10 5m settings (no 5m entries in any per-chart list): ER 0.23 + breakout 3, no range gate / stretch / slope, toward late-away 1 pt, flip distance max(2 ATR, 10 pts), SL1 1.7 ATR min 5 cap 7, TP1 1.7 ATR cap 6, 80 % at TP1 + BE + trail 1.7, no setups 16:00-18:45 + OR forming blocks, end at 16:00. In-sample.

## 0. v10.97 baseline

Trades 1576, net -238, avg -0.15, win 52 %, thirds -176 / +20 / -82, last 4 wk -59, max DD 298

By trigger: flip 362 / -17 · ltf20 758 / -72 · h9 252 / -156 · h20 204 / +6

By session: Asia 591 / -179 · London 529 / -52 · NY AM 164 / +171 · NY PM 292 / -178

## 1. HTF EMA20 slope filter (vs v10.97)

Base: 1576 trades, net -238, avg -0.15, thirds -176 / +20 / -82, last 4 wk -59, max DD 298

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.20 | 1131 | +215 | +453 | +2.9 | +109 / +184 / +160 | +56 | 141 | robust |
| slope 0.30 | 932 | +250 | +488 | +2.7 | +121 / +215 / +152 | +34 | 168 | robust |
| slope 0.42 | 725 | +458 | +696 | +3.5 | +207 / +208 / +282 | +59 | 131 | robust |
| slope 0.48 | 628 | +512 | +750 | +3.6 | +265 / +203 / +281 | +70 | 118 | robust |
| slope 0.55 | 516 | +382 | +620 | +2.9 | +203 / +210 / +206 | +31 | 103 | robust |
| slope 0.60 | 468 | +408 | +646 | +2.9 | +232 / +211 / +202 | +37 | 94 | robust |
| slope 0.65 | 417 | +337 | +575 | +2.6 | +228 / +166 / +182 | +34 | 88 | robust |
| slope 0.70 | 371 | +303 | +541 | +2.4 | +281 / +129 / +132 | +41 | 81 | robust |
| slope 0.75 | 321 | +240 | +478 | +2.1 | +240 / +117 / +121 | +58 | 68 | robust |
| slope 0.80 | 275 | +224 | +462 | +2.0 | +228 / +113 / +121 | +71 | 73 | promising |
| slope 0.90 | 193 | +156 | +394 | +1.6 | +220 / +51 / +123 | +81 | 65 | promising |
| slope 1.00 | 155 | +109 | +347 | +1.4 | +176 / +27 / +144 | +81 | 64 | promising |

## 2. Ideas on top of slope 0.48

Base: 628 trades, net +512, avg +0.82, thirds +90 / +224 / +199, last 4 wk +11, max DD 118

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back | 628 | +554 | +42 | +0.8 | -9 / +1 / +49 | -27 | 153 | noise |
| FLIP 0 % exit (0 % at TP1, BE, HTF flip) | 595 | +681 | +169 | +1.4 | -73 / +13 / +229 | +31 | 137 | noise |
| 100 % at TP1 | 664 | +405 | -108 | -0.9 | -66 / -13 / -29 | -27 | 134 | worse |
| 50 % at TP1 | 628 | +616 | +104 | +0.9 | +74 / -17 / +46 | +14 | 98 | noise |
| Range gate 5 ATR | 556 | +454 | -58 | -0.9 | -43 / +7 / -23 | +18 | 108 | worse |
| VWAP stretch 4 ATR | 387 | +392 | -121 | -1.2 | -26 / -72 / -23 | +3 | 93 | worse |
| LTF pierce min ER 0.12 | 583 | +423 | -90 | -1.8 | -64 / +14 / -40 | -11 | 120 | worse |
| LTF pierce min ER 0.15 | 543 | +434 | -78 | -1.1 | -72 / +6 / -12 | +4 | 120 | worse |
| LTF pierce min ER 0.20 | 489 | +318 | -195 | -2.2 | -19 / -120 / -55 | -18 | 115 | robustly worse |
| LTF pierce min ER 0.23 | 455 | +309 | -203 | -2.1 | -52 / -125 / -26 | -6 | 108 | robustly worse |
| Strict away flips (late-away OFF) | 547 | +336 | -176 | -3.1 | -74 / -67 / -35 | -19 | 108 | robustly worse |
| Trigger HTF CBC Flip OFF | 562 | +414 | -98 | -1.3 | -75 / -11 / -13 | -0 | 108 | worse |
| Trigger LTF EMA20 Pierce OFF | 277 | +272 | -240 | -1.8 | -47 / -128 / -65 | +6 | 71 | worse |
| Trigger HTF EMA9 Pierce OFF | 557 | +485 | -27 | -0.4 | +40 / -47 / -21 | +2 | 90 | worse |
| Trigger HTF EMA20 Pierce OFF | 624 | +500 | -12 | -0.8 | -8 / +1 / -5 | +0 | 118 | worse |
| End setups at 16:00 OFF | 628 | +506 | -6 | -0.2 | +17 / -10 / -13 | -2 | 122 | worse |
| SL1 1.5 ATR | 628 | +497 | -16 | -0.3 | -8 / -17 / +9 | +1 | 117 | worse |
| SL1 2.5 ATR | 627 | +496 | -16 | -0.4 | -3 / -0 / -12 | -0 | 118 | worse |
| SL1 3.0 ATR | 627 | +496 | -17 | -0.4 | -4 / -0 / -12 | -0 | 118 | worse |
| TP1 1.5 ATR | 628 | +494 | -19 | -0.4 | -2 / -9 / -8 | -4 | 118 | worse |
| TP1 2.0 ATR | 628 | +503 | -9 | -0.3 | +0 / +5 / -14 | -15 | 118 | worse |
| TP1 2.5 ATR | 628 | +499 | -14 | -0.4 | +0 / +6 / -20 | -24 | 118 | worse |
| Max SL1 cap OFF | 623 | +704 | +191 | +2.3 | +136 / +14 / +41 | -4 | 142 | robust except last 4 wk |
| Max TP1 cap OFF | 614 | +586 | +73 | +0.6 | +63 / -34 / +45 | +7 | 150 | noise |
| Trail 3.5 ATR | 598 | +536 | +24 | +0.3 | -47 / +23 / +48 | +6 | 121 | noise |
| Breakeven OFF | 618 | +460 | -52 | -0.6 | -13 / -35 / -4 | -3 | 126 | worse |
| CHOP > 58 block | 507 | +460 | -53 | -0.6 | -13 / -30 / -10 | +18 | 108 | worse |
| ADX < 20 block | 478 | +355 | -157 | -1.8 | -38 / -10 / -109 | -23 | 123 | worse |
| Crosses >= 4 block | 557 | +448 | -64 | -1.0 | -75 / +13 / -2 | +25 | 99 | worse |
| HTF flips >= 3 in 8 block | 552 | +316 | -196 | -3.1 | -77 / -17 / -102 | +0 | 116 | robustly worse |
| Environment EMA200 vs VWAP | 236 | +186 | -326 | -2.6 | -23 / -160 / -143 | -50 | 58 | robustly worse |
| ER 0.18 | 663 | +540 | +28 | +0.7 | +16 / +20 / -7 | -15 | 112 | noise |
| ER 0.30 | 587 | +443 | -69 | -1.3 | -27 / -2 / -40 | -24 | 96 | worse |

## 3. Final set vs v10.97: slope 0.48

Base: 1576 trades, net -238, avg -0.15, thirds -176 / +20 / -82, last 4 wk -59, max DD 298

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| final | 628 | +512 | +750 | +3.6 | +265 / +203 / +281 | +70 | 118 | robust |
| slope only | 628 | +512 | +750 | +3.6 | +265 / +203 / +281 | +70 | 118 | robust |

## 4. One-hour blocks on top of the final set

Base: 628 trades, net +512, avg +0.82, thirds +90 / +224 / +199, last 4 wk +11, max DD 118

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| block 18:00-19:00 | 623 | +503 | -9 | -0.5 | +0 / -3 / -7 | +4 | 118 | worse |
| block 19:00-20:00 | 596 | +486 | -26 | -0.7 | +5 / -13 / -18 | +2 | 93 | worse |
| block 20:00-21:00 | 610 | +523 | +11 | +0.3 | +13 / +5 / -8 | -5 | 103 | noise |
| block 21:00-22:00 | 602 | +480 | -32 | -0.9 | -18 / -8 / -6 | +6 | 103 | worse |
| block 22:00-23:00 | 611 | +446 | -66 | -2.2 | -40 / -17 / -10 | +2 | 122 | robustly worse |
| block 23:00-00:00 | 608 | +492 | -20 | -0.6 | -17 / -4 / +1 | -13 | 112 | worse |
| block 00:00-01:00 | 611 | +462 | -51 | -1.3 | -21 / -31 / +2 | -3 | 118 | worse |
| block 01:00-02:00 | 591 | +493 | -20 | -0.5 | +33 / -48 / -4 | +6 | 90 | worse |
| block 02:00-03:00 | 598 | +478 | -35 | -1.0 | -2 / -7 / -26 | -10 | 125 | worse |
| block 03:00-04:00 | 611 | +499 | -13 | -0.4 | +16 / -5 / -23 | +6 | 118 | worse |
| block 04:00-05:00 | 593 | +578 | +66 | +1.4 | +15 / +28 / +23 | +23 | 105 | promising |
| block 05:00-06:00 | 601 | +491 | -21 | -0.5 | -0 / -34 / +13 | +14 | 112 | worse |
| block 06:00-07:00 | 604 | +451 | -61 | -1.7 | -24 / -33 / -5 | +1 | 121 | worse |
| block 07:00-08:00 | 602 | +539 | +27 | +0.7 | -3 / -1 / +30 | -5 | 110 | noise |
| block 08:00-09:00 | 592 | +439 | -73 | -1.8 | -20 / +2 / -54 | -17 | 116 | worse |
| block 09:00-10:00 | 609 | +440 | -72 | -2.5 | -15 / -27 / -30 | -4 | 103 | robustly worse |
| block 10:00-11:00 | 598 | +456 | -56 | -1.3 | -39 / -18 / +1 | +0 | 146 | worse |
| block 11:00-12:00 | 605 | +406 | -106 | -2.9 | -15 / -27 / -64 | -17 | 110 | robustly worse |
| block 12:00-13:00 | 607 | +543 | +31 | +0.9 | +29 / +4 / -2 | -1 | 106 | noise |
| block 13:00-14:00 | 598 | +525 | +13 | +0.3 | -20 / +15 / +17 | +11 | 117 | noise |
| block 14:00-15:00 | 601 | +491 | -22 | -0.6 | -8 / -16 / +2 | -10 | 128 | worse |
| block 15:00-16:00 | 597 | +523 | +11 | +0.3 | -3 / +6 / +8 | +4 | 103 | noise |

## 5. Sessions (final vs v10.97)

| Session | v10.97 trades / net | final trades / net |
|---|---|---|
| Asia | 591 / -179 | 231 / +239 |
| London | 529 / -52 | 212 / +133 |
| NY AM | 164 / +171 | 63 / +144 |
| NY PM | 292 / -178 | 122 / -3 |


# MNQ 5m -- CBC EMA Slope branch studies -- 11/14/2026

Replay Jan 5 -> Nov 13, MNQ 5m (HTF = 25m), net after 0.87 pts cost. v10.97 / v1.10 5m settings (no 5m entries in any per-chart list): ER 0.23 + breakout 3, no range gate / stretch / slope, toward late-away 1 pt, flip distance max(2 ATR, 50 pts), SL1 1.7 ATR min 25 cap 30, TP1 1.7 ATR cap 40, 80 % at TP1 + BE + trail 1.7, no setups 16:00-18:45 + OR forming blocks, end at 16:00. In-sample.

## 0. v10.97 baseline

Trades 1544, net +1428, avg +0.92, win 47 %, thirds +556 / +686 / +186, last 4 wk +487, max DD 891

By trigger: flip 323 / +172 · ltf20 765 / -74 · h9 270 / +413 · h20 186 / +916

By session: Asia 529 / +1742 · London 537 / +126 · NY AM 178 / -63 · NY PM 300 / -377

## 1. HTF EMA20 slope filter (vs v10.97)

Base: 1544 trades, net +1428, avg +0.92, thirds +556 / +686 / +186, last 4 wk +487, max DD 891

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.20 | 1137 | +1883 | +455 | +0.6 | +175 / -44 / +325 | -160 | 805 | noise |
| slope 0.30 | 969 | +2181 | +753 | +0.9 | +339 / +15 / +399 | -221 | 618 | noise |
| slope 0.42 | 786 | +1921 | +493 | +0.5 | +687 / -232 / +39 | -299 | 465 | noise |
| slope 0.48 | 690 | +1845 | +417 | +0.4 | +749 / -285 / -47 | -366 | 499 | noise |
| slope 0.55 | 601 | +1753 | +326 | +0.3 | +523 / -127 / -70 | -337 | 441 | noise |
| slope 0.60 | 513 | +1510 | +83 | +0.1 | +340 / -303 / +46 | -319 | 485 | noise |
| slope 0.65 | 461 | +1646 | +218 | +0.2 | +499 / -473 / +192 | -317 | 384 | noise |
| slope 0.70 | 415 | +1399 | -29 | -0.0 | +307 / -477 / +141 | -366 | 384 | worse |
| slope 0.75 | 370 | +1130 | -298 | -0.3 | +192 / -461 / -29 | -336 | 353 | worse |
| slope 0.80 | 321 | +1249 | -178 | -0.2 | +83 / -472 / +211 | -266 | 292 | worse |
| slope 0.90 | 252 | +768 | -659 | -0.6 | -34 / -756 / +131 | -275 | 256 | worse |
| slope 1.00 | 196 | +590 | -838 | -0.7 | -8 / -757 / -73 | -294 | 246 | worse |

## 2. Ideas on top of slope 0.20

Base: 1137 trades, net +1883, avg +1.66, thirds +731 / +642 / +511, last 4 wk +327, max DD 805

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back | 1137 | +1810 | -73 | -0.2 | +306 / -365 / -13 | -114 | 1183 | worse |
| FLIP 0 % exit (0 % at TP1, BE, HTF flip) | 1036 | +2876 | +993 | +1.3 | +727 / +11 / +255 | -323 | 996 | promising |
| 100 % at TP1 | 1202 | +2048 | +165 | +0.2 | -17 / +113 / +69 | -88 | 631 | noise |
| 50 % at TP1 | 1137 | +1889 | +6 | +0.0 | -37 / -118 / +161 | +133 | 864 | noise |
| Range gate 5 ATR | 970 | +1738 | -145 | -0.3 | +29 / -332 / +158 | +82 | 601 | worse |
| VWAP stretch 4 ATR | 890 | +2424 | +541 | +1.0 | -401 / +332 / +611 | +26 | 579 | noise |
| LTF pierce min ER 0.12 | 1056 | +1812 | -71 | -0.2 | +90 / -58 / -103 | -102 | 686 | worse |
| LTF pierce min ER 0.15 | 1001 | +1389 | -494 | -1.1 | -52 / -308 / -134 | -178 | 918 | worse |
| LTF pierce min ER 0.20 | 932 | +1077 | -806 | -1.4 | -137 / -226 / -443 | -391 | 992 | worse |
| LTF pierce min ER 0.23 | 897 | +1354 | -529 | -0.9 | -137 / -69 / -322 | -399 | 737 | worse |
| Strict away flips (late-away OFF) | 937 | +1696 | -186 | -0.4 | -19 / -123 / -45 | +48 | 730 | worse |
| Trigger HTF CBC Flip OFF | 1012 | +1426 | -457 | -0.8 | -211 / -201 / -45 | +18 | 720 | worse |
| Trigger LTF EMA20 Pierce OFF | 689 | +1404 | -479 | -0.6 | -26 / -318 / -134 | -504 | 852 | worse |
| Trigger HTF EMA9 Pierce OFF | 999 | +1387 | -496 | -1.1 | +116 / -409 / -204 | +14 | 727 | worse |
| Trigger HTF EMA20 Pierce OFF | 1075 | +1114 | -769 | -2.6 | -285 / -397 / -87 | -6 | 847 | robustly worse |
| End setups at 16:00 OFF | 1137 | +1653 | -230 | -1.5 | -75 / -123 / -32 | +0 | 814 | worse |
| SL1 1.5 ATR | 1140 | +1938 | +55 | +0.2 | +35 / +4 / +16 | +11 | 780 | noise |
| SL1 2.5 ATR | 1136 | +1885 | +2 | +0.0 | +1 / +16 / -15 | -2 | 788 | noise |
| SL1 3.0 ATR | 1136 | +1879 | -4 | -0.0 | +1 / +10 / -15 | -2 | 788 | worse |
| TP1 1.5 ATR | 1143 | +1949 | +66 | +0.1 | -102 / +102 / +66 | -26 | 812 | noise |
| TP1 2.0 ATR | 1131 | +1679 | -204 | -0.4 | +12 / -290 / +73 | +15 | 836 | worse |
| TP1 2.5 ATR | 1126 | +1621 | -262 | -0.5 | -31 / -371 / +140 | +18 | 830 | worse |
| Max SL1 cap OFF | 1121 | +3091 | +1208 | +1.9 | +681 / -66 / +593 | +127 | 691 | noise |
| Max TP1 cap OFF | 1129 | +2222 | +339 | +0.7 | +86 / -41 / +293 | +572 | 1195 | noise |
| Trail 3.5 ATR | 1042 | +1903 | +20 | +0.0 | +38 / -75 / +57 | -32 | 618 | noise |
| Breakeven OFF | 1124 | +1995 | +112 | +0.3 | +12 / -109 / +209 | +251 | 757 | noise |
| CHOP > 58 block | 931 | +1079 | -804 | -1.5 | -320 / -516 / +32 | +79 | 850 | worse |
| ADX < 20 block | 800 | +401 | -1482 | -2.3 | -166 / -1007 / -309 | -20 | 1248 | robustly worse |
| Crosses >= 4 block | 979 | +280 | -1602 | -3.2 | -535 / -334 / -733 | -162 | 1034 | robustly worse |
| HTF flips >= 3 in 8 block | 973 | +1065 | -818 | -1.7 | -173 / -471 / -174 | -171 | 801 | worse |
| Environment EMA200 vs VWAP | 408 | +538 | -1345 | -1.6 | -663 / +194 / -876 | -476 | 568 | worse |
| ER 0.18 | 1202 | +1750 | -133 | -0.4 | +106 / -312 / +72 | +73 | 887 | worse |
| ER 0.30 | 1073 | +1833 | -50 | -0.2 | +8 / -59 / +1 | -18 | 733 | worse |

## 3. Final set vs v10.97: slope 0.20

Base: 1544 trades, net +1428, avg +0.92, thirds +556 / +686 / +186, last 4 wk +487, max DD 891

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| final | 1137 | +1883 | +455 | +0.6 | +175 / -44 / +325 | -160 | 805 | noise |
| slope only | 1137 | +1883 | +455 | +0.6 | +175 / -44 / +325 | -160 | 805 | noise |

## 4. One-hour blocks on top of the final set

Base: 1137 trades, net +1883, avg +1.66, thirds +731 / +642 / +511, last 4 wk +327, max DD 805

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| block 18:00-19:00 | 1131 | +1888 | +5 | +0.0 | +35 / -10 / -20 | -24 | 805 | noise |
| block 19:00-20:00 | 1097 | +1722 | -161 | -0.7 | -29 / +119 / -251 | -116 | 886 | worse |
| block 20:00-21:00 | 1125 | +1778 | -105 | -0.6 | -109 / +6 / -2 | -12 | 805 | worse |
| block 21:00-22:00 | 1091 | +1552 | -331 | -1.1 | -45 / +7 / -293 | -13 | 919 | worse |
| block 22:00-23:00 | 1115 | +1881 | -2 | -0.0 | -96 / -34 / +128 | +8 | 684 | worse |
| block 23:00-00:00 | 1096 | +1528 | -355 | -1.3 | +15 / -71 / -300 | -32 | 809 | worse |
| block 00:00-01:00 | 1104 | +1583 | -300 | -1.3 | +41 / -242 / -98 | +30 | 859 | worse |
| block 01:00-02:00 | 1093 | +1882 | -1 | -0.0 | -237 / +245 / -9 | +21 | 801 | worse |
| block 02:00-03:00 | 1081 | +2022 | +140 | +0.6 | +5 / -18 / +153 | +60 | 849 | noise |
| block 03:00-04:00 | 1108 | +1794 | -89 | -0.4 | -64 / +68 / -93 | -36 | 781 | worse |
| block 04:00-05:00 | 1083 | +1868 | -15 | -0.1 | +29 / -169 / +124 | +14 | 723 | worse |
| block 05:00-06:00 | 1082 | +1834 | -48 | -0.2 | -9 / -84 / +44 | +25 | 702 | worse |
| block 06:00-07:00 | 1084 | +1694 | -189 | -0.6 | -8 / -147 / -34 | +82 | 724 | worse |
| block 07:00-08:00 | 1089 | +1701 | -182 | -0.6 | +58 / -210 / -30 | +29 | 850 | worse |
| block 08:00-09:00 | 1064 | +1760 | -123 | -0.4 | -126 / +154 / -151 | -129 | 747 | worse |
| block 09:00-10:00 | 1091 | +2129 | +246 | +1.1 | +259 / -100 / +87 | -69 | 680 | noise |
| block 10:00-11:00 | 1078 | +1339 | -544 | -2.0 | -358 / -117 / -69 | -44 | 743 | worse |
| block 11:00-12:00 | 1090 | +1831 | -52 | -0.2 | -14 / +138 / -176 | -173 | 723 | worse |
| block 12:00-13:00 | 1090 | +1926 | +43 | +0.2 | -19 / -106 / +167 | +51 | 703 | noise |
| block 13:00-14:00 | 1099 | +1701 | -182 | -0.7 | +80 / -237 / -25 | -49 | 710 | worse |
| block 14:00-15:00 | 1087 | +2126 | +243 | +0.9 | +84 / +43 / +116 | +57 | 666 | noise |
| block 15:00-16:00 | 1078 | +1895 | +12 | +0.0 | -102 / -9 / +122 | +5 | 709 | noise |

## 5. Sessions (final vs v10.97)

| Session | v10.97 trades / net | final trades / net |
|---|---|---|
| Asia | 529 / +1742 | 379 / +1335 |
| London | 537 / +126 | 413 / +422 |
| NY AM | 178 / -63 | 124 / +403 |
| NY PM | 300 / -377 | 221 / -277 |


# M2K 5m -- CBC EMA Slope branch studies -- 11/14/2026

Replay Jan 5 -> Nov 13, M2K 5m (HTF = 25m), net after 0.35 pts cost. v10.97 / v1.10 5m settings (no 5m entries in any per-chart list): ER 0.23 + breakout 3, no range gate / stretch / slope, toward late-away 1 pt, flip distance max(2 ATR, 0 pts), SL1 1.7 ATR min 3 cap 8, TP1 1.7 ATR cap 3, 80 % at TP1 + BE + trail 1.7, no setups 16:00-18:45 + OR forming blocks, end at 16:00. In-sample.

## 0. v10.97 baseline

Trades 1459, net -364, avg -0.25, win 56 %, thirds -76 / -131 / -158, last 4 wk -85, max DD 390

By trigger: flip 253 / +43 · ltf20 790 / -279 · h9 243 / -85 · h20 173 / -44

By session: Asia 487 / -151 · London 489 / -153 · NY AM 187 / +16 · NY PM 295 / -73

## 1. HTF EMA20 slope filter (vs v10.97)

Base: 1459 trades, net -364, avg -0.25, thirds -76 / -131 / -158, last 4 wk -85, max DD 390

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.20 | 1125 | -176 | +188 | +2.5 | +10 / +100 / +78 | +44 | 221 | robust |
| slope 0.30 | 963 | -57 | +307 | +3.5 | +39 / +164 / +104 | +51 | 124 | robust |
| slope 0.42 | 790 | +16 | +381 | +3.9 | +79 / +179 / +123 | +67 | 75 | robust |
| slope 0.48 | 695 | -16 | +349 | +3.4 | +73 / +163 / +112 | +64 | 88 | robust |
| slope 0.55 | 621 | -58 | +307 | +2.9 | +83 / +124 / +101 | +53 | 99 | robust |
| slope 0.60 | 558 | -12 | +352 | +3.3 | +93 / +137 / +123 | +60 | 81 | robust |
| slope 0.65 | 506 | +5 | +369 | +3.4 | +90 / +140 / +139 | +69 | 69 | robust |
| slope 0.70 | 457 | +11 | +375 | +3.3 | +81 / +139 / +155 | +66 | 54 | robust |
| slope 0.75 | 413 | +33 | +397 | +3.4 | +93 / +144 / +160 | +75 | 44 | robust |
| slope 0.80 | 358 | +20 | +384 | +3.3 | +93 / +135 / +157 | +74 | 34 | robust |
| slope 0.90 | 273 | +46 | +410 | +3.4 | +97 / +138 / +175 | +84 | 28 | robust |
| slope 1.00 | 216 | +51 | +416 | +3.4 | +104 / +131 / +181 | +83 | 37 | robust |

## 2. Ideas on top of slope 1.00

Base: 216 trades, net +51, avg +0.24, thirds +28 / +0 / +23, last 4 wk -2, max DD 37

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back | 216 | +31 | -20 | -1.9 | -7 / -15 / +2 | +5 | 49 | worse |
| FLIP 0 % exit (0 % at TP1, BE, HTF flip) | 206 | +108 | +57 | +1.6 | +86 / -28 / -2 | -20 | 65 | noise |
| 100 % at TP1 | 225 | +35 | -16 | -0.4 | -7 / +1 / -10 | +3 | 42 | worse |
| 50 % at TP1 | 216 | +86 | +35 | +1.0 | +15 / +1 / +19 | -4 | 36 | promising |
| Range gate 5 ATR | 195 | +40 | -11 | -0.6 | -8 / +1 / -4 | -7 | 35 | worse |
| VWAP stretch 4 ATR | 106 | +28 | -23 | -0.7 | -14 / -6 / -3 | -1 | 24 | worse |
| LTF pierce min ER 0.12 | 188 | +43 | -8 | -0.5 | -23 / +11 / +4 | +6 | 28 | worse |
| LTF pierce min ER 0.15 | 174 | +49 | -2 | -0.1 | -17 / +11 / +4 | +4 | 27 | worse |
| LTF pierce min ER 0.20 | 144 | +49 | -2 | -0.1 | -13 / +17 / -7 | +3 | 24 | worse |
| LTF pierce min ER 0.23 | 129 | +37 | -15 | -0.5 | -23 / +12 / -4 | +6 | 24 | worse |
| Strict away flips (late-away OFF) | 191 | +43 | -9 | -0.6 | -7 / +4 / -5 | +0 | 36 | worse |
| Trigger HTF CBC Flip OFF | 206 | +58 | +7 | +0.4 | -7 / +5 / +9 | -1 | 33 | noise |
| Trigger LTF EMA20 Pierce OFF | 57 | +31 | -21 | -0.5 | -13 / -3 / -5 | +4 | 17 | worse |
| Trigger HTF EMA9 Pierce OFF | 198 | +28 | -23 | -1.5 | -1 / -7 / -14 | +0 | 42 | worse |
| Trigger HTF EMA20 Pierce OFF | 216 | +51 | +0 | +0.0 | +0 / +0 / +0 | +0 | 37 | noise |
| End setups at 16:00 OFF | 216 | +54 | +3 | +0.4 | +5 / -1 / -1 | +0 | 38 | noise |
| SL1 1.5 ATR | 217 | +41 | -10 | -0.6 | +2 / -0 / -12 | +2 | 36 | worse |
| SL1 2.5 ATR | 216 | +62 | +11 | +0.6 | -0 / +10 / +0 | -2 | 33 | noise |
| SL1 3.0 ATR | 216 | +54 | +3 | +0.2 | -1 / +8 / -4 | -3 | 35 | noise |
| TP1 1.5 ATR | 218 | +55 | +4 | +0.2 | +1 / +3 / +0 | -1 | 34 | noise |
| TP1 2.0 ATR | 216 | +48 | -3 | -0.1 | +1 / -3 / -1 | +1 | 38 | worse |
| TP1 2.5 ATR | 215 | +39 | -12 | -0.5 | -1 / -5 / -6 | +2 | 43 | worse |
| Max SL1 cap OFF | 216 | +49 | -2 | -0.4 | -0 / -2 / +0 | +0 | 39 | worse |
| Max TP1 cap OFF | 214 | -6 | -57 | -2.2 | -24 / -37 / +3 | -17 | 57 | worse |
| Trail 3.5 ATR | 208 | +38 | -13 | -0.5 | +6 / -8 / -10 | -0 | 45 | worse |
| Breakeven OFF | 215 | +46 | -5 | -0.3 | -3 / -3 / +1 | -2 | 37 | worse |
| CHOP > 58 block | 185 | +32 | -19 | -1.1 | -13 / +5 / -11 | +1 | 35 | worse |
| ADX < 20 block | 171 | +22 | -29 | -1.3 | +3 / -5 / -26 | -6 | 44 | worse |
| Crosses >= 4 block | 194 | +54 | +3 | +0.2 | -4 / -6 / +13 | +0 | 37 | noise |
| HTF flips >= 3 in 8 block | 196 | +43 | -8 | -0.5 | -1 / +6 / -13 | +5 | 39 | worse |
| Environment EMA200 vs VWAP | 44 | +53 | +2 | +0.0 | -6 / +11 / -4 | +7 | 10 | noise |
| ER 0.18 | 234 | +51 | -0 | -0.0 | -2 / -3 / +5 | -1 | 39 | worse |
| ER 0.30 | 198 | +31 | -20 | -1.3 | -10 / -7 / -3 | +0 | 45 | worse |

## 3. Final set vs v10.97: slope 1.00

Base: 1459 trades, net -364, avg -0.25, thirds -76 / -131 / -158, last 4 wk -85, max DD 390

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| final | 216 | +51 | +416 | +3.4 | +104 / +131 / +181 | +83 | 37 | robust |
| slope only | 216 | +51 | +416 | +3.4 | +104 / +131 / +181 | +83 | 37 | robust |

## 4. One-hour blocks on top of the final set

Base: 216 trades, net +51, avg +0.24, thirds +28 / +0 / +23, last 4 wk -2, max DD 37

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| block 18:00-19:00 | 213 | +56 | +5 | +0.9 | +3 / +2 / +0 | +0 | 33 | noise |
| block 19:00-20:00 | 207 | +68 | +16 | +1.8 | -1 / +10 / +8 | +2 | 25 | noise |
| block 20:00-21:00 | 210 | +50 | -1 | -0.1 | -8 / +3 / +4 | +0 | 37 | worse |
| block 21:00-22:00 | 206 | +41 | -10 | -0.9 | -6 / -9 / +5 | +4 | 40 | worse |
| block 22:00-23:00 | 213 | +52 | +1 | +0.1 | -1 / -0 / +2 | +0 | 37 | noise |
| block 23:00-00:00 | 204 | +64 | +13 | +1.2 | +9 / +7 / -3 | +2 | 33 | noise |
| block 00:00-01:00 | 193 | +51 | +0 | +0.0 | +10 / -6 / -4 | +0 | 41 | noise |
| block 01:00-02:00 | 198 | +45 | -6 | -0.5 | -12 / +6 / +0 | -2 | 38 | worse |
| block 02:00-03:00 | 206 | +38 | -13 | -1.3 | -4 / -5 / -4 | -4 | 40 | worse |
| block 03:00-04:00 | 215 | +54 | +3 | +1.0 | +0 / +3 / +0 | +0 | 34 | noise |
| block 04:00-05:00 | 212 | +54 | +3 | +0.3 | +4 / +1 / -3 | +0 | 39 | noise |
| block 05:00-06:00 | 209 | +57 | +6 | +0.7 | +1 / -0 / +5 | +2 | 33 | noise |
| block 06:00-07:00 | 211 | +51 | -0 | -0.0 | -4 / +4 / +0 | +0 | 32 | worse |
| block 07:00-08:00 | 207 | +46 | -5 | -0.5 | -0 / +1 / -5 | +0 | 38 | worse |
| block 08:00-09:00 | 206 | +25 | -26 | -2.5 | -10 / -2 / -14 | -2 | 42 | robustly worse |
| block 09:00-10:00 | 207 | +32 | -20 | -1.7 | +3 / -11 / -12 | -2 | 42 | worse |
| block 10:00-11:00 | 212 | +48 | -4 | -0.6 | -2 / -2 / +1 | +0 | 38 | worse |
| block 11:00-12:00 | 210 | +40 | -11 | -1.1 | -8 / +2 / -6 | -2 | 35 | worse |
| block 12:00-13:00 | 213 | +51 | -0 | -0.1 | +5 / +0 / -5 | +0 | 41 | worse |
| block 13:00-14:00 | 204 | +65 | +14 | +1.2 | +3 / +7 / +4 | +2 | 36 | promising |
| block 14:00-15:00 | 197 | +48 | -3 | -0.2 | -2 / -8 / +7 | -2 | 38 | worse |
| block 15:00-16:00 | 202 | +45 | -6 | -0.6 | -2 / -3 / -1 | +4 | 39 | worse |

## 5. Sessions (final vs v10.97)

| Session | v10.97 trades / net | final trades / net |
|---|---|---|
| Asia | 487 / -151 | 101 / -9 |
| London | 489 / -153 | 46 / +38 |
| NY AM | 187 / +16 | 18 / +24 |
| NY PM | 295 / -73 | 51 / -1 |


## MNQ 5m: ideas on v10.97 (no slope filter)

Base: 1544 trades, net +1428, avg +0.92, thirds +556 / +686 / +186, last 4 wk +487, max DD 891

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back | 1544 | +1146 | -282 | -0.7 | +229 / -678 / +168 | -79 | 1747 | worse |
| FLIP 0 % exit (0 % at TP1, BE, HTF flip) | 1417 | +1418 | -10 | -0.0 | +348 / -1244 / +886 | -183 | 1658 | worse |
| 100 % at TP1 | 1628 | +1861 | +433 | +0.5 | +21 / +65 / +346 | +5 | 829 | noise |
| 50 % at TP1 | 1544 | +1192 | -235 | -0.3 | -98 / -338 / +201 | +61 | 1128 | worse |
| Range gate 5 ATR | 1312 | +1151 | -276 | -0.4 | -113 / -601 / +438 | +121 | 926 | worse |
| VWAP stretch 4 ATR | 1297 | +2152 | +724 | +1.4 | -438 / +363 / +800 | +214 | 734 | noise |
| LTF pierce min ER 0.12 | 1453 | +1738 | +311 | +0.8 | +92 / +44 / +175 | +7 | 735 | noise |
| LTF pierce min ER 0.15 | 1386 | +1268 | -160 | -0.3 | -131 / -188 / +159 | -70 | 1070 | worse |
| LTF pierce min ER 0.20 | 1316 | +945 | -482 | -0.8 | -249 / -136 / -98 | -288 | 1234 | worse |
| LTF pierce min ER 0.23 | 1278 | +1250 | -178 | -0.3 | -161 / -40 / +23 | -296 | 984 | worse |
| Strict away flips (late-away OFF) | 1149 | +1066 | -361 | -0.6 | +32 / -122 / -272 | -160 | 930 | worse |
| Trigger HTF CBC Flip OFF | 1369 | +764 | -663 | -1.0 | -397 / -484 / +218 | +84 | 957 | worse |
| Trigger LTF EMA20 Pierce OFF | 1054 | +1322 | -105 | -0.1 | -36 / -472 / +403 | -575 | 1248 | worse |
| Trigger HTF EMA9 Pierce OFF | 1379 | +986 | -442 | -0.8 | +90 / -358 / -174 | -125 | 874 | worse |
| Trigger HTF EMA20 Pierce OFF | 1412 | +479 | -948 | -1.9 | -260 / -481 / -207 | +78 | 984 | worse |
| End setups at 16:00 OFF | 1544 | +971 | -456 | -2.3 | -197 / -192 / -67 | -9 | 972 | robustly worse |
| SL1 1.5 ATR | 1548 | +1329 | -99 | -0.3 | +7 / -9 / -96 | +12 | 944 | worse |
| SL1 2.5 ATR | 1541 | +1560 | +133 | +0.4 | +148 / +8 / -23 | -2 | 879 | noise |
| SL1 3.0 ATR | 1541 | +1545 | +118 | +0.4 | +142 / -2 / -23 | -2 | 879 | noise |
| TP1 1.5 ATR | 1552 | +1449 | +21 | +0.0 | -25 / +82 / -36 | -74 | 947 | noise |
| TP1 2.0 ATR | 1537 | +1193 | -234 | -0.4 | +82 / -433 / +117 | +27 | 1114 | worse |
| TP1 2.5 ATR | 1529 | +1155 | -273 | -0.5 | +87 / -488 / +128 | +30 | 1208 | worse |
| Max SL1 cap OFF | 1517 | +2389 | +962 | +1.3 | +1099 / -500 / +362 | +57 | 1285 | noise |
| Max TP1 cap OFF | 1531 | +1648 | +220 | +0.4 | +8 / +180 / +32 | +297 | 1371 | noise |
| Trail 3.5 ATR | 1431 | +1430 | +2 | +0.0 | +30 / -223 / +195 | +46 | 762 | noise |
| Breakeven OFF | 1526 | +1685 | +257 | +0.5 | +41 / -58 / +275 | +247 | 919 | noise |
| CHOP > 58 block | 1282 | +828 | -600 | -1.0 | -321 / -574 / +295 | +123 | 919 | worse |
| ADX < 20 block | 1054 | -71 | -1498 | -2.0 | -108 / -1242 / -148 | -137 | 1595 | worse |
| Crosses >= 4 block | 1306 | +23 | -1404 | -2.3 | -466 / -569 / -369 | -24 | 1275 | robustly worse |
| HTF flips >= 3 in 8 block | 1294 | +979 | -449 | -0.8 | +72 / -492 / -29 | -173 | 1070 | worse |
| Environment EMA200 vs VWAP | 638 | -145 | -1572 | -1.6 | -492 / -265 / -816 | -749 | 779 | worse |
| ER 0.18 | 1610 | +1344 | -83 | -0.2 | +59 / -297 / +154 | +100 | 1046 | worse |
| ER 0.30 | 1467 | +1309 | -119 | -0.3 | -31 / -118 / +30 | -19 | 886 | worse |

## MNQ 5m: FLIP 0 % combos

Base: 1544 trades, net +1428, avg +0.92, thirds +556 / +686 / +186, last 4 wk +487, max DD 891

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| FLIP 0 % + slope 0.30 | 879 | +2619 | +1191 | +1.1 | +669 / -101 / +623 | -522 | 1005 | noise |
| FLIP 0 % + cap OFF | 1383 | +753 | -674 | -0.6 | +688 / -2596 / +1234 | +396 | 2794 | worse |

## MES 5m: slope + stretch neighbours (vs v10.97)

Base: 1544 trades, net -873, avg -0.57, thirds -353 / -194 / -325, last 4 wk -92, max DD 877

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.60 + stretch 3 | 255 | +203 | +1076 | +4.9 | +408 / +234 / +433 | +111 | 40 | robust |
| slope 0.60 + stretch 4 | 330 | +247 | +1120 | +5.2 | +426 / +262 / +432 | +103 | 42 | robust |
| slope 0.60 + stretch 6 | 431 | +155 | +1027 | +4.9 | +343 / +262 / +423 | +87 | 63 | robust |
| slope 0.70 + stretch 3 | 172 | +176 | +1049 | +4.7 | +379 / +241 / +429 | +117 | 38 | robust |
| slope 0.70 + stretch 4 | 228 | +248 | +1121 | +5.1 | +407 / +293 / +421 | +108 | 46 | robust |
| slope 0.70 + stretch 6 | 311 | +172 | +1045 | +4.8 | +352 / +304 / +389 | +93 | 55 | robust |
| slope 0.75 + stretch 3 | 136 | +162 | +1035 | +4.6 | +395 / +234 / +406 | +113 | 31 | robust |
| slope 0.75 + stretch 4 | 188 | +239 | +1111 | +5.0 | +425 / +288 / +398 | +104 | 53 | robust |
| slope 0.75 + stretch 6 | 267 | +163 | +1036 | +4.7 | +361 / +293 / +381 | +97 | 50 | robust |
| slope 0.80 + stretch 3 | 106 | +172 | +1045 | +4.6 | +389 / +242 / +414 | +116 | 25 | robust |
| slope 0.80 + stretch 4 | 150 | +249 | +1122 | +5.0 | +408 / +292 / +422 | +124 | 42 | robust |
| slope 0.80 + stretch 6 | 218 | +161 | +1033 | +4.6 | +368 / +272 / +393 | +105 | 40 | robust |

## M2K 5m: slope extended + ideas (vs v10.97)

Base: 1459 trades, net -364, avg -0.25, thirds -76 / -131 / -158, last 4 wk -85, max DD 390

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.90 | 273 | +46 | +410 | +3.4 | +97 / +138 / +175 | +84 | 28 | robust |
| slope 1.00 | 216 | +51 | +416 | +3.4 | +104 / +131 / +181 | +83 | 37 | robust |
| slope 1.10 | 160 | +52 | +416 | +3.4 | +106 / +136 / +174 | +84 | 35 | robust |
| slope 1.20 | 129 | +46 | +410 | +3.3 | +101 / +151 / +158 | +78 | 19 | robust |
| slope 1.40 | 75 | +26 | +391 | +3.1 | +71 / +143 / +176 | +81 | 17 | robust |
| slope 1.00 + stretch 4 | 106 | +28 | +392 | +3.1 | +89 / +125 / +178 | +82 | 24 | robust |
| slope 1.00 + LTF ER 0.23 | 129 | +37 | +401 | +3.2 | +81 / +143 / +177 | +88 | 24 | robust |
| slope 1.00 + 50 % at TP1 | 216 | +86 | +451 | +3.6 | +118 / +132 / +201 | +79 | 36 | robust |
| slope 0.75 + stretch 4 + ER 0.23 | 151 | -6 | +358 | +2.9 | +67 / +147 / +144 | +72 | 30 | robust |

## MGC 5m: slope 0.48 + cap neighbours (vs v10.97)

Base: 1576 trades, net -238, avg -0.15, thirds -176 / +20 / -82, last 4 wk -59, max DD 298

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.48 + cap 7 | 628 | +512 | +750 | +3.6 | +265 / +203 / +281 | +70 | 118 | robust |
| slope 0.48 + cap 9 | 625 | +573 | +811 | +3.7 | +304 / +179 / +328 | +73 | 117 | robust |
| slope 0.48 + cap 12 | 623 | +667 | +905 | +4.1 | +346 / +231 / +327 | +67 | 115 | robust |
| slope 0.48 + cap 1000000000.0 | 623 | +704 | +942 | +4.3 | +402 / +217 / +323 | +66 | 142 | robust |
