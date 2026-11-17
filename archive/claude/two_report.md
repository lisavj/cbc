# 2m charts -- CBC EMA Slope studies (battery + full ①②③ sweep) -- 11/14/2026

Replay Jun 1 -> Nov 13 (the 2m bar feed starts Jun 1: ~5.5 months, thirds ~7 weeks), HTF 10m, net after costs (MES 0.50, MGC 0.22, MNQ 0.87, M2K 0.35). Baseline = LIVE v1.12 2m settings: MES 2m MTF (60m) gate, flips >= 4 in 8 HTF, skip all new setups from 9 HTF candles after the flip, slow EMA 14; MGC 2m range gate 5. Not modelled: MGC 2m flip-flop skip, VWAP Bounce. MNQ / M2K 2m have no 2m entries (= v10.97). In-sample, short sample.

Engine: two_live.py (live 2m), two_livef.py (live + final sets). Scripts: twol_study.py (battery: slope grid, ideas, greedy set, hour blocks, sessions), all2l_study.py (full ①②③ sweep + slope neighbours + existing 2m entries).

## Result -> v1.13

| Chart | Live 2m (v1.12) | v1.13 set | v1.13 | thirds | last 4 wk | max DD |
|---|---|---|---|---|---|---|
| MES 2m | 1322 / -490 | slope 0.75 + strict away + no SL1 cap + MTF gate OFF | 483 / +310 | +138 / +41 / +131 | +40 | 512 -> 41 |
| MGC 2m | 1789 / -74 | slope 0.42 | 863 / +329 | +170 / +126 / +33 | -24 | 238 -> 93 |
| MNQ 2m | 2179 / -2259 | slope 0.55 + FLIP 0 % exit | 732 / +3566 | +1397 / +487 / +1681 | +733 | 3140 -> 844 |
| M2K 2m | 1756 / -606 | slope 1.0 + LTF pierce min ER 0.2 | 198 / +33 | -6 / +5 / +33 | +20 | 606 -> 23 (thin: chart only) |

Plateaus: MES slope 0.65-1.0 all robust vs live (0.7 / 0.8 with MTF off also); MGC 0.2-0.55 all robust vs live; MNQ 0.42-0.8 robust (0.55 / 0.6 best with FLIP 0 %); M2K 0.55-1.0 robust.
MES 2m existing entries: MTF gate OFF robust on top of the slope set (+77, z 2.6); flips >= 4 and skip-from-9 still help (keep).

Candidates not implemented (single values / no per-chart input): MNQ 2m HTF pierce min ER 0 (+974, z 1.7; no per-chart HTF ER list), MGC 2m 0 % at TP1 (+114, z 1.2, DD up), MES 2m time stop 10, MES 2m block 06:00-07:00 (+44, z 2.3, last 4 wk -4), M2K 2m ER 0.18-0.20 (+9).

Note: a first pass on a v10.97-style 2m baseline (no existing 2m entries modelled; two_<sym>_report / all2_<sym> local only) picked MES slope 1.0 + flip OFF + ER 0.15 and MGC slope 0.42 -- superseded by the live-baseline runs below.

# MES 2m battery
## 0. Live 2m baseline (v1.12)

Trades 1322, net -490, avg -0.37, win 51 %, thirds -160 / -127 / -203, last 4 wk -223, max DD 512

By trigger: flip 411 / -257 · ltf20 656 / -176 · h9 171 / -89 · h20 84 / +32

By session: Asia 499 / -275 · London 400 / -264 · NY AM 144 / +49 · NY PM 279 / +1

## 1. HTF EMA20 slope filter (vs live 2m)

Base: 1322 trades, net -490, avg -0.37, thirds -160 / -127 / -203, last 4 wk -223, max DD 512

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.20 | 1144 | -293 | +196 | +2.2 | +155 / +10 / +32 | -20 | 336 | robust except last 4 wk |
| slope 0.30 | 1016 | -243 | +247 | +2.3 | +141 / -9 / +114 | +46 | 267 | noise |
| slope 0.42 | 866 | -116 | +374 | +3.0 | +225 / +55 / +94 | +30 | 222 | robust |
| slope 0.48 | 807 | -124 | +366 | +2.8 | +212 / +59 / +95 | +39 | 202 | robust |
| slope 0.55 | 707 | +11 | +501 | +3.6 | +215 / +108 / +178 | +106 | 116 | robust |
| slope 0.60 | 644 | +104 | +594 | +4.2 | +249 / +92 / +252 | +167 | 74 | robust |
| slope 0.65 | 582 | +152 | +642 | +4.4 | +261 / +117 / +264 | +172 | 67 | robust |
| slope 0.70 | 528 | +170 | +660 | +4.4 | +274 / +137 / +249 | +177 | 64 | robust |
| slope 0.75 | 480 | +171 | +661 | +4.3 | +271 / +144 / +246 | +185 | 49 | robust |
| slope 0.80 | 427 | +171 | +661 | +4.2 | +275 / +126 / +260 | +195 | 52 | robust |
| slope 0.90 | 327 | +128 | +618 | +3.8 | +275 / +114 / +228 | +175 | 59 | robust |
| slope 1.00 | 251 | +113 | +603 | +3.7 | +249 / +130 / +224 | +191 | 55 | robust |

## 2. Ideas on top of slope 0.75

Base: 480 trades, net +171, avg +0.36, thirds +111 / +18 / +43, last 4 wk -38, max DD 49

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back | 480 | +149 | -23 | -0.8 | -35 / -16 / +28 | +10 | 49 | worse |
| FLIP 0 % exit (0 % at TP1, BE, HTF flip) | 455 | +144 | -27 | -0.3 | -111 / +57 / +27 | +26 | 69 | worse |
| 100 % at TP1 | 527 | +100 | -71 | -0.9 | -20 / -23 / -27 | -14 | 55 | worse |
| 50 % at TP1 | 480 | +208 | +37 | +0.5 | -8 / +35 / +10 | +6 | 50 | noise |
| Range gate 5 ATR | 423 | +155 | -17 | -0.3 | +16 / +11 / -43 | -15 | 54 | worse |
| VWAP stretch 4 ATR | 136 | +103 | -68 | -0.8 | -58 / +20 / -30 | +14 | 29 | worse |
| LTF pierce min ER 0.12 | 469 | +185 | +14 | +0.7 | +13 / +6 / -5 | -1 | 49 | noise |
| LTF pierce min ER 0.15 | 450 | +179 | +8 | +0.3 | +4 / +17 / -13 | +2 | 49 | noise |
| LTF pierce min ER 0.20 | 422 | +195 | +24 | +0.6 | -8 / +38 / -6 | -4 | 45 | noise |
| LTF pierce min ER 0.23 | 397 | +175 | +4 | +0.1 | +4 / +40 / -40 | -14 | 52 | noise |
| Strict away flips (late-away OFF) | 454 | +202 | +31 | +1.3 | +4 / +5 / +21 | +24 | 44 | promising |
| Trigger HTF CBC Flip OFF | 454 | +196 | +24 | +0.5 | -20 / +28 / +16 | +31 | 33 | noise |
| Trigger LTF EMA20 Pierce OFF | 138 | +72 | -99 | -1.1 | -69 / -3 / -27 | -5 | 43 | worse |
| Trigger HTF EMA9 Pierce OFF | 440 | +120 | -51 | -1.6 | -9 / -17 / -25 | +0 | 55 | worse |
| Trigger HTF EMA20 Pierce OFF | 476 | +157 | -15 | -1.6 | -1 / -14 / +0 | +0 | 49 | worse |
| End setups at 16:00 OFF | 480 | +177 | +6 | +0.8 | +0 / +6 / -0 | -0 | 49 | noise |
| SL1 1.5 ATR | 480 | +175 | +4 | +0.1 | +6 / +2 / -5 | -8 | 47 | noise |
| SL1 2.5 ATR | 479 | +165 | -6 | -0.2 | -11 / +3 / +1 | -8 | 50 | worse |
| SL1 3.0 ATR | 477 | +189 | +18 | +0.5 | +2 / +15 / +1 | -6 | 49 | noise |
| TP1 1.5 ATR | 482 | +141 | -31 | -0.4 | +1 / -28 / -4 | -3 | 50 | worse |
| TP1 2.0 ATR | 479 | +146 | -25 | -0.4 | -9 / +8 / -24 | -7 | 55 | worse |
| TP1 2.5 ATR | 476 | +109 | -62 | -1.0 | -54 / +10 / -18 | +2 | 61 | worse |
| Max SL1 cap OFF | 480 | +194 | +23 | +1.3 | +4 / +5 / +14 | +14 | 64 | promising |
| Max TP1 cap OFF | 479 | +76 | -95 | -2.2 | -39 / -19 / -37 | +10 | 71 | robustly worse |
| Trail 3.5 ATR | 457 | +164 | -7 | -0.1 | -25 / +12 / +6 | +2 | 50 | worse |
| Breakeven OFF | 480 | +159 | -13 | -0.3 | -1 / -4 / -8 | -3 | 49 | worse |
| CHOP > 58 block | 432 | +132 | -40 | -0.9 | -2 / -15 / -23 | -7 | 59 | worse |
| ADX < 20 block | 406 | +196 | +24 | +0.5 | +33 / -8 / -1 | +16 | 41 | noise |
| Crosses >= 4 block | 447 | +169 | -2 | -0.1 | -28 / +10 / +16 | +13 | 44 | worse |
| HTF flips >= 3 in 8 block | 436 | +149 | -22 | -0.6 | -13 / -6 / -2 | +8 | 49 | worse |
| Environment EMA200 vs VWAP | 303 | +107 | -64 | -1.0 | -51 / -1 / -12 | +34 | 45 | worse |
| ER 0.18 | 501 | +133 | -39 | -1.7 | -12 / -2 / -25 | -16 | 57 | worse |
| ER 0.30 | 456 | +159 | -12 | -0.4 | -14 / +4 / -2 | +2 | 63 | worse |

## 3. Final set vs live 2m: slope 0.75 + Strict away flips (late-away OFF) + Max SL1 cap OFF

Base: 1322 trades, net -490, avg -0.37, thirds -160 / -127 / -203, last 4 wk -223, max DD 512

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| final | 454 | +234 | +724 | +4.7 | +284 / +154 / +286 | +227 | 49 | robust |
| slope only | 480 | +171 | +661 | +4.3 | +271 / +144 / +246 | +185 | 49 | robust |

## 4. One-hour blocks on top of the final set

Base: 454 trades, net +234, avg +0.52, thirds +124 / +27 / +83, last 4 wk +4, max DD 49

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| block 18:00-19:00 | 451 | +243 | +9 | +0.5 | +5 / -0 / +5 | +3 | 45 | noise |
| block 19:00-20:00 | 431 | +237 | +4 | +0.2 | -1 / -3 / +8 | +12 | 43 | noise |
| block 20:00-21:00 | 448 | +238 | +4 | +0.3 | +15 / +0 / -11 | -4 | 55 | noise |
| block 21:00-22:00 | 438 | +212 | -22 | -1.1 | -8 / +6 / -20 | -17 | 51 | worse |
| block 22:00-23:00 | 440 | +221 | -13 | -0.6 | -5 / +5 / -13 | +6 | 47 | worse |
| block 23:00-00:00 | 432 | +256 | +22 | +0.8 | +11 / +4 / +8 | +3 | 49 | noise |
| block 00:00-01:00 | 424 | +210 | -24 | -0.8 | -33 / +5 / +4 | +3 | 51 | worse |
| block 01:00-02:00 | 431 | +225 | -9 | -0.4 | -14 / -0 / +5 | +0 | 49 | worse |
| block 02:00-03:00 | 435 | +195 | -39 | -1.9 | -7 / -11 / -22 | -13 | 49 | worse |
| block 03:00-04:00 | 445 | +237 | +3 | +0.2 | -7 / +0 / +9 | +4 | 46 | noise |
| block 04:00-05:00 | 435 | +231 | -3 | -0.1 | +17 / +9 / -29 | -11 | 49 | worse |
| block 05:00-06:00 | 432 | +242 | +9 | +0.3 | +3 / -4 / +9 | -2 | 49 | noise |
| block 06:00-07:00 | 439 | +278 | +44 | +2.3 | +25 / +18 / +0 | -4 | 49 | robust except last 4 wk |
| block 07:00-08:00 | 432 | +271 | +37 | +1.7 | +23 / -1 / +16 | +16 | 44 | noise |
| block 08:00-09:00 | 434 | +208 | -26 | -1.1 | -11 / -27 / +12 | +13 | 53 | worse |
| block 09:00-10:00 | 441 | +224 | -10 | -0.6 | -4 / -11 / +6 | +2 | 49 | worse |
| block 10:00-11:00 | 437 | +154 | -80 | -4.0 | -19 / -37 / -25 | -4 | 49 | robustly worse |
| block 11:00-12:00 | 427 | +203 | -31 | -1.2 | -34 / +15 / -12 | +1 | 44 | worse |
| block 12:00-13:00 | 438 | +198 | -36 | -1.5 | -19 / -11 / -5 | +1 | 49 | worse |
| block 13:00-14:00 | 432 | +189 | -45 | -1.9 | -17 / +3 / -31 | -24 | 49 | worse |
| block 14:00-15:00 | 429 | +195 | -39 | -1.4 | -1 / -24 / -14 | -7 | 49 | worse |
| block 15:00-16:00 | 431 | +236 | +2 | +0.1 | -20 / +25 / -3 | -6 | 54 | noise |

## 5. Sessions (final vs live 2m)

| Session | live trades / net | final trades / net |
|---|---|---|
| Asia | 499 / -275 | 180 / +49 |
| London | 400 / -264 | 130 / -49 |
| NY AM | 144 / +49 | 46 / +122 |
| NY PM | 279 / +1 | 98 / +112 |

FINAL_SET MES {'slope': 0.75, 'P': {'tw': None}, 'q': {'cap': 1000000000.0}}

# MGC 2m battery
## 0. Live 2m baseline (v1.12)

Trades 1789, net -74, avg -0.04, win 50 %, thirds +43 / +46 / -163, last 4 wk -65, max DD 238

By trigger: flip 312 / -45 · ltf20 937 / +221 · h9 304 / -95 · h20 236 / -156

By session: Asia 677 / -133 · London 579 / +56 · NY AM 199 / -25 · NY PM 333 / +29

## 1. HTF EMA20 slope filter (vs live 2m)

Base: 1789 trades, net -74, avg -0.04, thirds +43 / +46 / -163, last 4 wk -65, max DD 238

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.20 | 1289 | +313 | +388 | +3.1 | +85 / +120 / +183 | +56 | 111 | robust |
| slope 0.30 | 1059 | +291 | +366 | +2.5 | +139 / +48 / +179 | +44 | 81 | robust |
| slope 0.42 | 863 | +329 | +403 | +2.5 | +126 / +80 / +196 | +42 | 93 | robust |
| slope 0.48 | 755 | +340 | +414 | +2.5 | +127 / +81 / +206 | +40 | 91 | robust |
| slope 0.55 | 645 | +285 | +360 | +2.1 | +83 / +87 / +189 | +30 | 87 | robust |
| slope 0.60 | 580 | +241 | +315 | +1.8 | +101 / +34 / +180 | +39 | 71 | promising |
| slope 0.65 | 508 | +254 | +329 | +1.8 | +106 / +13 / +209 | +49 | 53 | promising |
| slope 0.70 | 462 | +293 | +368 | +2.0 | +116 / +5 / +247 | +58 | 41 | robust |
| slope 0.75 | 402 | +264 | +339 | +1.8 | +109 / -18 / +248 | +61 | 53 | noise |
| slope 0.80 | 355 | +209 | +283 | +1.5 | +67 / -28 / +244 | +70 | 58 | noise |
| slope 0.90 | 270 | +89 | +163 | +0.9 | +32 / -65 / +197 | +44 | 61 | noise |
| slope 1.00 | 193 | +96 | +171 | +0.9 | +36 / -51 / +186 | +52 | 42 | noise |

## 2. Ideas on top of slope 0.42

Base: 863 trades, net +329, avg +0.38, thirds +170 / +126 / +33, last 4 wk -24, max DD 93

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back | 863 | +357 | +28 | +0.8 | -12 / -25 / +65 | +24 | 92 | noise |
| FLIP 0 % exit (0 % at TP1, BE, HTF flip) | 797 | +464 | +135 | +1.3 | -36 / +194 / -23 | -37 | 125 | noise |
| 100 % at TP1 | 916 | +255 | -74 | -0.7 | -13 / -32 / -28 | -6 | 106 | worse |
| 50 % at TP1 | 863 | +371 | +43 | +0.4 | +10 / +22 / +10 | -12 | 101 | noise |
| Range gate 5 ATR | 863 | +329 | +0 | +0.0 | +0 / +0 / +0 | +0 | 93 | noise |
| VWAP stretch 4 ATR | 392 | +211 | -118 | -1.1 | -92 / -16 / -10 | +25 | 57 | worse |
| LTF pierce min ER 0.12 | 796 | +224 | -104 | -2.2 | -47 / -43 / -15 | +5 | 83 | robustly worse |
| LTF pierce min ER 0.15 | 744 | +207 | -122 | -1.9 | -80 / -32 / -10 | +14 | 63 | worse |
| LTF pierce min ER 0.20 | 652 | +184 | -145 | -1.8 | -91 / -36 / -18 | -9 | 74 | worse |
| LTF pierce min ER 0.23 | 607 | +158 | -171 | -1.9 | -137 / -34 / -1 | -10 | 72 | worse |
| Strict away flips (late-away OFF) | 727 | +286 | -42 | -0.8 | +4 / -22 / -24 | -14 | 116 | worse |
| Trigger HTF CBC Flip OFF | 801 | +292 | -36 | -0.7 | +11 / -35 / -12 | -12 | 108 | worse |
| Trigger LTF EMA20 Pierce OFF | 379 | +155 | -174 | -1.5 | -103 / -35 / -36 | +2 | 56 | worse |
| Trigger HTF EMA9 Pierce OFF | 734 | +334 | +5 | +0.1 | -59 / +20 / +44 | +20 | 60 | noise |
| Trigger HTF EMA20 Pierce OFF | 848 | +294 | -34 | -1.7 | -7 / -23 / -4 | +0 | 93 | worse |
| End setups at 16:00 OFF | 863 | +323 | -6 | -0.3 | +1 / +1 / -8 | -3 | 97 | worse |
| SL1 1.5 ATR | 866 | +298 | -31 | -0.7 | -1 / -8 / -22 | -11 | 112 | worse |
| SL1 2.5 ATR | 855 | +364 | +35 | +0.7 | -11 / +29 / +18 | +19 | 78 | noise |
| SL1 3.0 ATR | 854 | +378 | +49 | +0.9 | -18 / +25 / +42 | +35 | 67 | noise |
| TP1 1.5 ATR | 868 | +250 | -79 | -0.9 | -24 / -31 / -23 | -13 | 98 | worse |
| TP1 2.0 ATR | 858 | +283 | -46 | -0.6 | +3 / -22 / -26 | -22 | 102 | worse |
| TP1 2.5 ATR | 854 | +324 | -5 | -0.1 | +37 / -24 / -17 | -47 | 121 | worse |
| Max SL1 cap OFF | 862 | +325 | -4 | -0.1 | -8 / +9 / -4 | +3 | 100 | worse |
| Max TP1 cap OFF | 859 | +300 | -29 | -0.5 | -40 / +4 / +8 | +1 | 86 | worse |
| Trail 3.5 ATR | 801 | +312 | -17 | -0.2 | -5 / +17 / -29 | -3 | 97 | worse |
| Breakeven OFF | 859 | +315 | -13 | -0.3 | +1 / -6 / -8 | -9 | 96 | worse |
| CHOP > 58 block | 725 | +298 | -31 | -0.5 | -81 / +19 / +31 | +18 | 75 | worse |
| ADX < 20 block | 683 | +200 | -129 | -1.9 | -109 / -32 / +12 | +17 | 91 | worse |
| Crosses >= 4 block | 791 | +210 | -119 | -2.4 | -60 / -68 / +9 | -8 | 95 | worse |
| HTF flips >= 3 in 8 block | 759 | +285 | -44 | -0.8 | -5 / -45 / +5 | -8 | 85 | worse |
| Environment EMA200 vs VWAP | 543 | +193 | -136 | -1.6 | -86 / -29 / -21 | -17 | 73 | worse |
| ER 0.18 | 930 | +308 | -21 | -0.4 | -10 / -8 / -3 | -0 | 96 | worse |
| ER 0.30 | 789 | +374 | +45 | +0.9 | +11 / +38 / -4 | -3 | 91 | noise |

## 3. Final set vs live 2m: slope 0.42

Base: 1789 trades, net -74, avg -0.04, thirds +43 / +46 / -163, last 4 wk -65, max DD 238

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| final | 863 | +329 | +403 | +2.5 | +126 / +80 / +196 | +42 | 93 | robust |
| slope only | 863 | +329 | +403 | +2.5 | +126 / +80 / +196 | +42 | 93 | robust |

## 4. One-hour blocks on top of the final set

Base: 863 trades, net +329, avg +0.38, thirds +170 / +126 / +33, last 4 wk -24, max DD 93

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| block 18:00-19:00 | 855 | +343 | +15 | +1.1 | +8 / -2 / +8 | +3 | 85 | noise |
| block 19:00-20:00 | 824 | +352 | +24 | +0.8 | +10 / +8 / +5 | -2 | 87 | noise |
| block 20:00-21:00 | 848 | +300 | -29 | -1.3 | -19 / -10 / +1 | +0 | 93 | worse |
| block 21:00-22:00 | 811 | +280 | -48 | -1.2 | -39 / -32 / +23 | +4 | 77 | worse |
| block 22:00-23:00 | 820 | +342 | +13 | +0.4 | +19 / +8 / -15 | +4 | 94 | noise |
| block 23:00-00:00 | 824 | +353 | +24 | +0.7 | +12 / +11 / +1 | +21 | 81 | noise |
| block 00:00-01:00 | 825 | +329 | +0 | +0.0 | +1 / -3 / +2 | +3 | 81 | noise |
| block 01:00-02:00 | 827 | +281 | -48 | -1.6 | -9 / -18 / -21 | -4 | 92 | worse |
| block 02:00-03:00 | 829 | +352 | +23 | +0.8 | +7 / +9 / +8 | +2 | 99 | noise |
| block 03:00-04:00 | 836 | +293 | -36 | -1.3 | -12 / -7 / -17 | -7 | 100 | worse |
| block 04:00-05:00 | 818 | +306 | -23 | -0.7 | -16 / -10 / +3 | +2 | 98 | worse |
| block 05:00-06:00 | 832 | +329 | +1 | +0.0 | -1 / +2 / -0 | -5 | 93 | noise |
| block 06:00-07:00 | 830 | +321 | -7 | -0.3 | -13 / +9 / -3 | +11 | 85 | worse |
| block 07:00-08:00 | 817 | +213 | -115 | -3.3 | -63 / -55 / +2 | +4 | 86 | worse |
| block 08:00-09:00 | 822 | +292 | -37 | -1.1 | -30 / -14 / +7 | +12 | 76 | worse |
| block 09:00-10:00 | 841 | +324 | -5 | -0.2 | -22 / -6 / +23 | +9 | 77 | worse |
| block 10:00-11:00 | 810 | +325 | -4 | -0.1 | -4 / +20 / -20 | -8 | 94 | worse |
| block 11:00-12:00 | 827 | +235 | -94 | -2.9 | -43 / -31 / -20 | -6 | 103 | robustly worse |
| block 12:00-13:00 | 828 | +353 | +24 | +0.8 | +25 / +6 / -6 | -0 | 94 | noise |
| block 13:00-14:00 | 834 | +293 | -36 | -1.2 | -1 / -10 / -25 | -14 | 109 | worse |
| block 14:00-15:00 | 822 | +295 | -34 | -1.0 | -33 / -20 / +19 | +2 | 82 | worse |
| block 15:00-16:00 | 818 | +284 | -45 | -1.4 | -10 / -13 / -21 | -12 | 105 | worse |

## 5. Sessions (final vs live 2m)

| Session | live trades / net | final trades / net |
|---|---|---|
| Asia | 677 / -133 | 335 / -13 |
| London | 579 / +56 | 267 / +183 |
| NY AM | 199 / -25 | 98 / +76 |
| NY PM | 333 / +29 | 162 / +85 |

FINAL_SET MGC {'slope': 0.42}

# MNQ 2m battery
## 0. Live 2m baseline (v1.12)

Trades 2179, net -2259, avg -1.04, win 45 %, thirds -114 / -1353 / -792, last 4 wk -656, max DD 3140

By trigger: flip 607 / -418 · ltf20 958 / -1019 · h9 372 / -286 · h20 242 / -537

By session: Asia 807 / -773 · London 723 / -970 · NY AM 227 / -585 · NY PM 421 / +81

## 1. HTF EMA20 slope filter (vs live 2m)

Base: 2179 trades, net -2259, avg -1.04, thirds -114 / -1353 / -792, last 4 wk -656, max DD 3140

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.20 | 1595 | +339 | +2598 | +3.1 | +881 / +1162 / +554 | +33 | 919 | robust |
| slope 0.30 | 1302 | +1464 | +3723 | +4.0 | +980 / +1670 / +1072 | +448 | 616 | robust |
| slope 0.42 | 1045 | +1728 | +3987 | +3.9 | +1116 / +1083 / +1788 | +905 | 771 | robust |
| slope 0.48 | 921 | +1490 | +3749 | +3.5 | +949 / +1241 / +1559 | +712 | 581 | robust |
| slope 0.55 | 810 | +1572 | +3831 | +3.4 | +944 / +1424 / +1463 | +534 | 417 | robust |
| slope 0.60 | 713 | +1771 | +4029 | +3.6 | +1092 / +1481 / +1456 | +650 | 410 | robust |
| slope 0.65 | 642 | +1150 | +3409 | +3.0 | +816 / +1256 / +1337 | +470 | 421 | robust |
| slope 0.70 | 569 | +685 | +2944 | +2.5 | +691 / +1106 / +1147 | +453 | 449 | robust |
| slope 0.75 | 505 | +1265 | +3524 | +3.0 | +803 / +1312 / +1409 | +631 | 238 | robust |
| slope 0.80 | 445 | +1316 | +3575 | +3.0 | +859 / +1499 / +1217 | +626 | 253 | robust |
| slope 0.90 | 337 | +917 | +3176 | +2.6 | +577 / +1283 / +1316 | +663 | 297 | robust |
| slope 1.00 | 250 | +819 | +3078 | +2.5 | +442 / +1424 / +1212 | +588 | 205 | robust |

## 2. Ideas on top of slope 0.55

Base: 810 trades, net +1572, avg +1.94, thirds +830 / +71 / +671, last 4 wk -122, max DD 417

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back | 810 | +2783 | +1211 | +5.5 | +707 / -88 / +591 | +814 | 525 | noise |
| FLIP 0 % exit (0 % at TP1, BE, HTF flip) | 732 | +3566 | +1994 | +3.6 | +567 / +416 / +1011 | +855 | 844 | robust |
| 100 % at TP1 | 868 | +1506 | -66 | -0.1 | +127 / +59 / -252 | -148 | 473 | worse |
| 50 % at TP1 | 810 | +1796 | +224 | +0.4 | +6 / -49 / +266 | +202 | 442 | noise |
| Range gate 5 ATR | 712 | +1588 | +16 | +0.0 | -274 / +161 / +129 | +152 | 348 | noise |
| VWAP stretch 4 ATR | 314 | +885 | -687 | -1.1 | -536 / +205 / -356 | +136 | 312 | worse |
| LTF pierce min ER 0.12 | 736 | +1602 | +30 | +0.1 | -85 / +109 / +5 | +106 | 351 | noise |
| LTF pierce min ER 0.15 | 694 | +1564 | -8 | -0.0 | -241 / +125 / +107 | +191 | 337 | worse |
| LTF pierce min ER 0.20 | 634 | +1429 | -144 | -0.3 | -393 / +177 / +73 | +196 | 297 | worse |
| LTF pierce min ER 0.23 | 599 | +1496 | -76 | -0.2 | -414 / +173 / +166 | +321 | 308 | worse |
| Strict away flips (late-away OFF) | 707 | +843 | -730 | -2.7 | -95 / -199 / -435 | -238 | 480 | robustly worse |
| Trigger HTF CBC Flip OFF | 727 | +1076 | -496 | -1.4 | -466 / -38 / +8 | +72 | 387 | worse |
| Trigger LTF EMA20 Pierce OFF | 361 | +1632 | +60 | +0.1 | -286 / +135 / +211 | +389 | 222 | noise |
| Trigger HTF EMA9 Pierce OFF | 698 | +1285 | -288 | -0.9 | -221 / -27 / -40 | +77 | 411 | worse |
| Trigger HTF EMA20 Pierce OFF | 806 | +1468 | -104 | -1.6 | +0 / -30 / -74 | -41 | 452 | worse |
| End setups at 16:00 OFF | 810 | +1542 | -30 | -0.4 | -12 / -5 / -12 | -12 | 420 | worse |
| SL1 1.5 ATR | 811 | +1447 | -125 | -0.6 | -76 / -27 / -22 | +17 | 418 | worse |
| SL1 2.5 ATR | 807 | +1537 | -35 | -0.1 | +33 / +4 / -71 | -52 | 454 | worse |
| SL1 3.0 ATR | 807 | +1546 | -26 | -0.1 | +25 / -28 / -24 | -57 | 459 | worse |
| TP1 1.5 ATR | 817 | +1701 | +129 | +0.3 | -33 / +215 / -53 | +44 | 410 | noise |
| TP1 2.0 ATR | 803 | +1746 | +174 | +0.4 | +84 / +35 / +55 | +25 | 423 | noise |
| TP1 2.5 ATR | 798 | +1777 | +205 | +0.4 | +122 / +14 / +69 | +62 | 424 | noise |
| Max SL1 cap OFF | 802 | +1313 | -259 | -0.8 | -338 / -8 / +87 | -4 | 474 | worse |
| Max TP1 cap OFF | 808 | +1563 | -9 | -0.0 | +139 / -116 / -32 | +9 | 370 | worse |
| Trail 3.5 ATR | 739 | +2175 | +603 | +1.3 | +95 / +245 / +263 | +272 | 389 | promising |
| Breakeven OFF | 807 | +1598 | +26 | +0.1 | +35 / -25 / +15 | -1 | 412 | noise |
| CHOP > 58 block | 664 | +914 | -659 | -1.7 | -220 / -249 / -190 | +113 | 465 | worse |
| ADX < 20 block | 656 | +807 | -765 | -2.1 | -201 / +48 / -612 | -468 | 719 | worse |
| Crosses >= 4 block | 746 | +1196 | -376 | -1.5 | -147 / -44 / -185 | -34 | 436 | worse |
| HTF flips >= 3 in 8 block | 725 | +1077 | -496 | -1.8 | -120 / -184 / -192 | -51 | 435 | worse |
| Environment EMA200 vs VWAP | 517 | +1431 | -141 | -0.3 | -332 / +151 / +40 | +93 | 396 | worse |
| ER 0.18 | 845 | +1618 | +46 | +0.2 | +118 / -13 / -59 | -41 | 459 | noise |
| ER 0.30 | 757 | +1142 | -430 | -1.7 | -211 / -92 / -127 | -1 | 424 | worse |

## 3. Final set vs live 2m: slope 0.55 + FLIP 0 % exit (0 % at TP1, BE, HTF flip)

Base: 2179 trades, net -2259, avg -1.04, thirds -114 / -1353 / -792, last 4 wk -656, max DD 3140

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| final | 732 | +3566 | +5825 | +4.8 | +1511 / +1840 / +2473 | +1389 | 844 | robust |
| slope only | 810 | +1572 | +3831 | +3.4 | +944 / +1424 / +1463 | +534 | 417 | robust |

## 4. One-hour blocks on top of the final set

Base: 732 trades, net +3566, avg +4.87, thirds +1397 / +487 / +1681, last 4 wk +733, max DD 844

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| block 18:00-19:00 | 720 | +3547 | -19 | -0.1 | +18 / +21 / -59 | +11 | 831 | worse |
| block 19:00-20:00 | 683 | +4024 | +458 | +1.2 | +130 / +74 / +253 | +219 | 772 | promising |
| block 20:00-21:00 | 718 | +3733 | +167 | +0.6 | -10 / -19 / +195 | +146 | 874 | noise |
| block 21:00-22:00 | 702 | +3601 | +35 | +0.1 | +36 / +2 / -3 | +31 | 794 | noise |
| block 22:00-23:00 | 705 | +3099 | -467 | -1.3 | -112 / +73 / -428 | -80 | 835 | worse |
| block 23:00-00:00 | 703 | +3722 | +156 | +0.5 | +44 / +29 / +83 | +73 | 810 | noise |
| block 00:00-01:00 | 700 | +3136 | -430 | -1.1 | -275 / -76 / -78 | -104 | 697 | worse |
| block 01:00-02:00 | 707 | +3353 | -213 | -0.6 | -80 / -220 / +86 | +55 | 936 | worse |
| block 02:00-03:00 | 696 | +3339 | -227 | -0.7 | -244 / +86 / -68 | +1 | 760 | worse |
| block 03:00-04:00 | 720 | +3539 | -27 | -0.1 | +26 / +21 / -74 | -69 | 826 | worse |
| block 04:00-05:00 | 698 | +3204 | -362 | -1.0 | +51 / -30 / -383 | -253 | 838 | worse |
| block 05:00-06:00 | 699 | +3666 | +100 | +0.3 | +219 / -173 / +54 | -9 | 826 | noise |
| block 06:00-07:00 | 713 | +2641 | -925 | -2.5 | -204 / -650 / -71 | +20 | 1280 | robustly worse |
| block 07:00-08:00 | 707 | +3532 | -34 | -0.1 | +58 / -158 / +66 | +21 | 834 | worse |
| block 08:00-09:00 | 700 | +3750 | +185 | +0.6 | -5 / +117 / +73 | +40 | 833 | noise |
| block 09:00-10:00 | 712 | +3308 | -258 | -1.0 | +94 / +149 / -501 | -556 | 753 | worse |
| block 10:00-11:00 | 693 | +3569 | +3 | +0.0 | +36 / -92 / +58 | -27 | 812 | noise |
| block 11:00-12:00 | 702 | +2990 | -576 | -1.5 | -555 / +167 / -189 | -82 | 765 | worse |
| block 12:00-13:00 | 700 | +3676 | +110 | +0.3 | +46 / +114 / -50 | +208 | 807 | noise |
| block 13:00-14:00 | 704 | +3308 | -258 | -0.7 | +88 / +53 / -399 | -321 | 822 | worse |
| block 14:00-15:00 | 705 | +3141 | -424 | -1.2 | -440 / -56 / +71 | +37 | 840 | worse |
| block 15:00-16:00 | 707 | +3168 | -398 | -1.5 | -287 / -109 / -2 | -18 | 916 | worse |

## 5. Sessions (final vs live 2m)

| Session | live trades / net | final trades / net |
|---|---|---|
| Asia | 807 / -773 | 301 / +700 |
| London | 723 / -970 | 214 / +1052 |
| NY AM | 227 / -585 | 81 / +601 |
| NY PM | 421 / +81 | 136 / +1212 |

FINAL_SET MNQ {'slope': 0.55, 'q': {'part': 0.0, 'tr': 0}}

# M2K 2m battery
## 0. Live 2m baseline (v1.12)

Trades 1756, net -606, avg -0.34, win 51 %, thirds -230 / -131 / -244, last 4 wk -136, max DD 606

By trigger: flip 376 / -165 · ltf20 908 / -296 · h9 290 / -75 · h20 182 / -70

By session: Asia 622 / -278 · London 572 / -260 · NY AM 172 / +47 · NY PM 390 / -114

## 1. HTF EMA20 slope filter (vs live 2m)

Base: 1756 trades, net -606, avg -0.34, thirds -230 / -131 / -244, last 4 wk -136, max DD 606

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.20 | 1374 | -397 | +208 | +3.6 | +103 / +20 / +86 | +39 | 397 | robust |
| slope 0.30 | 1192 | -290 | +315 | +4.8 | +161 / +48 / +107 | +51 | 292 | robust |
| slope 0.42 | 1002 | -212 | +394 | +5.4 | +162 / +71 / +161 | +87 | 228 | robust |
| slope 0.48 | 900 | -182 | +424 | +5.4 | +174 / +85 / +165 | +73 | 188 | robust |
| slope 0.55 | 802 | -141 | +465 | +5.7 | +185 / +94 / +187 | +84 | 142 | robust |
| slope 0.60 | 718 | -87 | +519 | +6.1 | +196 / +122 / +201 | +96 | 95 | robust |
| slope 0.65 | 653 | -35 | +571 | +6.5 | +209 / +128 / +234 | +112 | 53 | robust |
| slope 0.70 | 586 | -23 | +583 | +6.6 | +210 / +134 / +239 | +128 | 47 | robust |
| slope 0.75 | 531 | -17 | +588 | +6.5 | +206 / +127 / +256 | +137 | 59 | robust |
| slope 0.80 | 488 | -11 | +594 | +6.5 | +214 / +126 / +254 | +130 | 50 | robust |
| slope 0.90 | 380 | +5 | +611 | +6.5 | +212 / +118 / +281 | +138 | 47 | robust |
| slope 1.00 | 298 | -4 | +602 | +6.3 | +211 / +125 / +266 | +139 | 45 | robust |

## 2. Ideas on top of slope 1.00

Base: 298 trades, net -4, avg -0.01, thirds -20 / -6 / +23, last 4 wk +3, max DD 45

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back | 298 | -8 | -4 | -0.5 | -1 / -3 / +0 | +8 | 50 | worse |
| FLIP 0 % exit (0 % at TP1, BE, HTF flip) | 282 | -6 | -3 | -0.1 | +4 / -24 / +17 | +16 | 80 | worse |
| 100 % at TP1 | 306 | -11 | -7 | -0.2 | +7 / -1 / -13 | -10 | 41 | worse |
| 50 % at TP1 | 298 | +7 | +11 | +0.4 | +0 / -4 / +15 | +11 | 47 | noise |
| Range gate 5 ATR | 276 | -9 | -5 | -0.4 | +0 / +2 / -8 | -6 | 38 | worse |
| VWAP stretch 4 ATR | 75 | +9 | +12 | +0.4 | +6 / +14 / -7 | +7 | 19 | noise |
| LTF pierce min ER 0.12 | 268 | +8 | +12 | +0.8 | -6 / +6 / +11 | +14 | 42 | noise |
| LTF pierce min ER 0.15 | 237 | +22 | +26 | +1.4 | -3 / +12 / +17 | +17 | 38 | noise |
| LTF pierce min ER 0.20 | 198 | +33 | +36 | +1.6 | +14 / +12 / +11 | +17 | 23 | promising |
| LTF pierce min ER 0.23 | 177 | +21 | +25 | +1.0 | +11 / +9 / +4 | +11 | 26 | noise |
| Strict away flips (late-away OFF) | 264 | -5 | -1 | -0.1 | +11 / +2 / -14 | -3 | 32 | worse |
| Trigger HTF CBC Flip OFF | 283 | +5 | +8 | +0.6 | -1 / +16 / -6 | -8 | 37 | noise |
| Trigger LTF EMA20 Pierce OFF | 70 | +20 | +24 | +0.7 | +19 / +5 / -0 | +10 | 16 | noise |
| Trigger HTF EMA9 Pierce OFF | 273 | -32 | -29 | -2.3 | -7 / -5 / -17 | -5 | 53 | robustly worse |
| Trigger HTF EMA20 Pierce OFF | 297 | -4 | -0 | -0.2 | +0 / -0 / +0 | +0 | 46 | worse |
| End setups at 16:00 OFF | 298 | -4 | -0 | -0.0 | -1 / +0 / +1 | +0 | 46 | worse |
| SL1 1.5 ATR | 298 | -17 | -13 | -1.2 | -3 / -1 / -9 | +2 | 49 | worse |
| SL1 2.5 ATR | 296 | -3 | +1 | +0.1 | +2 / -1 / +0 | +4 | 42 | noise |
| SL1 3.0 ATR | 296 | +7 | +11 | +0.8 | +3 / +4 / +4 | +6 | 39 | noise |
| TP1 1.5 ATR | 299 | -7 | -4 | -0.1 | -1 / -0 / -3 | -1 | 43 | worse |
| TP1 2.0 ATR | 296 | +8 | +12 | +0.4 | +5 / +1 / +6 | +7 | 45 | noise |
| TP1 2.5 ATR | 293 | +26 | +30 | +1.2 | +14 / +8 / +8 | +8 | 33 | promising |
| Max SL1 cap OFF | 298 | -4 | +0 | +0.0 | +0 / +0 / +0 | +0 | 45 | noise |
| Max TP1 cap OFF | 298 | +15 | +19 | +1.3 | +6 / +5 / +7 | +6 | 42 | promising |
| Trail 3.5 ATR | 283 | -7 | -3 | -0.1 | +1 / -2 / -3 | -2 | 45 | worse |
| Breakeven OFF | 295 | +1 | +5 | +0.4 | +1 / +3 / +0 | +0 | 41 | noise |
| CHOP > 58 block | 259 | +4 | +8 | +0.5 | +18 / -1 / -9 | -5 | 31 | noise |
| ADX < 20 block | 233 | -17 | -14 | -0.7 | -7 / +10 / -16 | -6 | 39 | worse |
| Crosses >= 4 block | 273 | -18 | -15 | -1.2 | -6 / -5 / -4 | -8 | 50 | worse |
| HTF flips >= 3 in 8 block | 273 | +7 | +11 | +0.8 | +1 / +7 / +3 | +0 | 41 | noise |
| Environment EMA200 vs VWAP | 188 | +4 | +7 | +0.3 | +15 / +3 / -11 | +2 | 28 | noise |
| ER 0.18 | 319 | -7 | -4 | -0.4 | -5 / +6 / -4 | -5 | 45 | worse |
| ER 0.30 | 271 | -6 | -3 | -0.2 | +10 / +2 / -15 | -12 | 35 | worse |

## 3. Final set vs live 2m: slope 1.00 + LTF pierce min ER 0.20

Base: 1756 trades, net -606, avg -0.34, thirds -230 / -131 / -244, last 4 wk -136, max DD 606

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| final | 198 | +33 | +638 | +6.5 | +225 / +137 / +277 | +156 | 23 | robust |
| slope only | 298 | -4 | +602 | +6.3 | +211 / +125 / +266 | +139 | 45 | robust |

## 4. One-hour blocks on top of the final set

Base: 198 trades, net +33, avg +0.17, thirds -6 / +5 / +33, last 4 wk +20, max DD 23

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| block 18:00-19:00 | 195 | +33 | +1 | +0.2 | +0 / +0 / +1 | -1 | 23 | noise |
| block 19:00-20:00 | 182 | +28 | -4 | -0.5 | -5 / +1 / -1 | +2 | 27 | worse |
| block 20:00-21:00 | 195 | +32 | -1 | -0.2 | +1 / -0 / -2 | -2 | 22 | worse |
| block 21:00-22:00 | 191 | +39 | +7 | +1.2 | +5 / +1 / +1 | -0 | 20 | promising |
| block 22:00-23:00 | 188 | +38 | +5 | +0.7 | +5 / -2 / +2 | -0 | 20 | noise |
| block 23:00-00:00 | 188 | +34 | +1 | +0.2 | -0 / +1 / +0 | -0 | 22 | noise |
| block 00:00-01:00 | 190 | +38 | +5 | +0.8 | +4 / -0 / +1 | +0 | 19 | noise |
| block 01:00-02:00 | 182 | +32 | -1 | -0.1 | -3 / -3 / +5 | -0 | 28 | worse |
| block 02:00-03:00 | 187 | +23 | -9 | -1.3 | -8 / +2 / -4 | -6 | 28 | worse |
| block 03:00-04:00 | 194 | +31 | -2 | -0.4 | -0 / -2 / +0 | +0 | 23 | worse |
| block 04:00-05:00 | 191 | +25 | -8 | -1.4 | -2 / -3 / -4 | -1 | 24 | worse |
| block 05:00-06:00 | 189 | +43 | +10 | +1.6 | +11 / -1 / +0 | +0 | 20 | noise |
| block 06:00-07:00 | 186 | +34 | +1 | +0.1 | +2 / +1 / -1 | +0 | 20 | noise |
| block 07:00-08:00 | 188 | +38 | +5 | +0.7 | +1 / -2 / +6 | +3 | 23 | noise |
| block 08:00-09:00 | 191 | +20 | -12 | -2.1 | -4 / -5 / -3 | -1 | 27 | robustly worse |
| block 09:00-10:00 | 190 | +40 | +8 | +1.2 | -2 / +9 / -0 | +2 | 24 | noise |
| block 10:00-11:00 | 192 | +17 | -16 | -2.9 | -6 / +0 / -9 | -2 | 27 | worse |
| block 11:00-12:00 | 192 | +14 | -19 | -3.0 | +0 / -5 / -14 | -11 | 26 | worse |
| block 12:00-13:00 | 188 | +28 | -5 | -0.6 | -2 / -0 / -2 | +1 | 22 | worse |
| block 13:00-14:00 | 185 | +29 | -4 | -0.4 | +4 / +1 / -8 | -2 | 24 | worse |
| block 14:00-15:00 | 188 | +25 | -8 | -1.1 | -5 / -5 / +2 | +5 | 25 | worse |
| block 15:00-16:00 | 190 | +37 | +4 | +0.6 | +9 / +2 / -6 | -6 | 15 | noise |

## 5. Sessions (final vs live 2m)

| Session | live trades / net | final trades / net |
|---|---|---|
| Asia | 622 / -278 | 85 / -4 |
| London | 572 / -260 | 57 / -4 |
| NY AM | 172 / +47 | 13 / +30 |
| NY PM | 390 / -114 | 43 / +12 |

FINAL_SET M2K {'slope': 1.0, 'erl': 0.2}

## MES 2m: full ①②③ sweep on live + v1.13 set

Base: 454 trades, net +234, avg +0.52, thirds +124 / +27 / +83, last 4 wk +4, max DD 49

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ③ CHOP > 61.8 block | 434 | +230 | -3 | -0.1 | -3 / +3 / -3 | -4 | 49 | worse |
| ③ CHOP > 58 block | 411 | +195 | -39 | -0.9 | +2 / -13 / -28 | -11 | 57 | worse |
| ③ ADX < 20 block | 380 | +269 | +35 | +0.8 | +38 / -8 / +5 | +22 | 41 | noise |
| ③ ADX < 15 block | 434 | +251 | +17 | +0.6 | +28 / -10 / -1 | +11 | 46 | noise |
| ③ EMA20/VWAP crosses >= 4 block | 421 | +236 | +2 | +0.1 | -23 / +10 / +16 | +13 | 44 | noise |
| ③ crosses >= 6 block | 451 | +230 | -4 | -0.3 | -1 / -9 / +6 | +6 | 43 | worse |
| ③ N-bar range < 2 ATR block | 452 | +230 | -4 | -0.4 | +0 / -1 / -3 | +0 | 49 | worse |
| ③ N-bar range < 3 ATR block | 341 | +177 | -57 | -1.0 | -17 / -23 / -18 | -9 | 47 | worse |
| ③ HTF flips >= 2 in 8 block | 173 | +32 | -201 | -2.4 | -93 / -50 / -59 | -17 | 43 | robustly worse |
| ③ HTF flips >= 3 in 8 block | 410 | +212 | -22 | -0.6 | -13 / -6 / -2 | +8 | 49 | worse |
| ③ HTF flips >= 4 in 8 block | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ③ Skip non-flip setups from 6 HTF candles after flip | 363 | +222 | -12 | -0.3 | -13 / +5 / -4 | +19 | 39 | worse |
| ③ ... from 9 | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ③ ... from 12 | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ③ Block if VWAP -3 / +2 pts | 441 | +212 | -22 | -1.2 | -6 / -1 / -15 | -14 | 64 | worse |
| ③ Block if EMA200 -3 / +2 pts | 453 | +231 | -3 | -0.7 | +0 / +0 / -3 | -3 | 49 | worse |
| ③ Environment EMA200 vs VWAP | 285 | +128 | -106 | -1.7 | -55 / +3 / -54 | -8 | 44 | worse |
| ③ Skip while ATR > 1.8 x ATR(100) | 444 | +198 | -36 | -2.2 | -13 / -16 / -7 | +1 | 48 | robustly worse |
| ③ Skip if SL1 cap < 1.5 ATR | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ③ ER 0.18 | 473 | +221 | -12 | -0.5 | +12 / -2 / -23 | -18 | 60 | worse |
| ③ ER 0.20 | 466 | +240 | +6 | +0.3 | +14 / -3 / -6 | -2 | 49 | noise |
| ③ ER 0.26 | 445 | +220 | -14 | -0.6 | -9 / -9 / +4 | +6 | 49 | worse |
| ③ ER 0.30 | 432 | +213 | -20 | -0.7 | -14 / +2 / -8 | -4 | 49 | worse |
| ③ ER filter OFF | 509 | +222 | -12 | -0.3 | +21 / -39 / +6 | -4 | 60 | worse |
| ③ ER breakout exception OFF | 365 | +212 | -22 | -0.4 | +5 / +18 / -45 | -14 | 41 | worse |
| ③ Range gate 4 ATR | 436 | +230 | -4 | -0.1 | +10 / -2 / -13 | -1 | 49 | worse |
| ③ Range gate 6 ATR | 365 | +156 | -78 | -1.3 | -39 / +11 / -50 | -12 | 35 | worse |
| ③ Range gate zone 30 % | 361 | +222 | -12 | -0.2 | -8 / +7 / -11 | +4 | 33 | worse |
| ③ Range gate ON 5 ATR | 397 | +217 | -17 | -0.3 | +16 / +11 / -43 | -16 | 42 | worse |
| ③ VWAP stretch 3 ATR | 71 | +51 | -182 | -2.0 | -91 / -22 / -70 | -9 | 19 | worse |
| ③ VWAP stretch 6 ATR | 236 | +188 | -46 | -0.7 | -68 / +36 / -13 | +3 | 41 | worse |
| ③ VWAP stretch ON 4 ATR | 120 | +115 | -119 | -1.4 | -80 / +13 / -53 | -6 | 24 | worse |
| ① Flip min ER 0.15 | 459 | +238 | +4 | +0.2 | +3 / -2 / +4 | -0 | 54 | noise |
| ① Flip min ER 0.30 | 451 | +243 | +9 | +0.4 | +3 / +0 / +6 | +0 | 49 | noise |
| ① Toward late-away 1 pt (instead of strict) | 480 | +194 | -40 | -1.7 | -8 / -5 / -26 | -29 | 64 | worse |
| ① SL1 x 1.5 ATR | 454 | +208 | -26 | -0.9 | -10 / -10 / -7 | -8 | 45 | worse |
| ① SL1 x 2.0 | 453 | +231 | -3 | -0.1 | -12 / -8 / +16 | +10 | 42 | worse |
| ① SL1 x 2.5 | 453 | +238 | +4 | +0.1 | -12 / -7 / +23 | +15 | 43 | noise |
| ① SL1 x 3.0 | 451 | +266 | +32 | +0.8 | -8 / +3 / +37 | +30 | 41 | noise |
| ① SL1 x 3.5 | 451 | +272 | +38 | +1.0 | -2 / +7 / +33 | +27 | 37 | noise |
| ① TP1 x 1.25 ATR | 463 | +150 | -84 | -1.1 | -13 / -27 / -44 | -16 | 51 | worse |
| ① TP1 x 1.5 | 456 | +196 | -38 | -0.6 | +2 / -27 / -13 | -2 | 49 | worse |
| ① TP1 x 1.75 | 454 | +238 | +4 | +0.1 | -0 / +5 / -1 | +2 | 49 | noise |
| ① TP1 x 2.0 | 453 | +205 | -28 | -0.5 | -11 / +8 / -25 | -7 | 53 | worse |
| ① TP1 x 2.5 | 450 | +169 | -65 | -1.1 | -52 / +8 / -21 | +1 | 53 | worse |
| ① Close at TP1 0 % | 454 | +333 | +99 | +1.3 | -12 / +94 / +17 | +7 | 74 | noise |
| ① Close at TP1 50 % | 454 | +271 | +37 | +0.5 | -5 / +35 / +6 | +3 | 50 | noise |
| ① Close at TP1 80 % | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ① Close at TP1 100 % | 499 | +173 | -61 | -0.7 | -15 / -24 / -23 | -15 | 51 | worse |
| ① Breakeven at TP1 OFF | 452 | +223 | -11 | -0.3 | +2 / -4 / -9 | -4 | 49 | worse |
| ① Trail 1.3 ATR | 467 | +201 | -33 | -0.5 | -12 / -21 / -1 | +11 | 45 | worse |
| ① Trail 1.7 ATR | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ① Trail 2.5 ATR | 436 | +238 | +4 | +0.1 | -10 / -1 / +15 | +12 | 45 | noise |
| ① Trail 3.5 ATR | 431 | +230 | -4 | -0.1 | -23 / +12 / +8 | +3 | 46 | worse |
| ① No trail | 429 | +208 | -25 | -0.4 | -29 / +8 / -4 | -3 | 48 | worse |
| ① Min SL x 0.6 | 456 | +251 | +18 | +0.5 | +7 / -3 / +13 | +12 | 45 | noise |
| ① Min SL x 1.4 | 453 | +261 | +27 | +0.8 | +9 / +20 / -3 | -9 | 50 | noise |
| ① Max SL1 cap OFF | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ① Max TP1 cap OFF | 450 | +177 | -57 | -1.3 | -14 / -18 / -26 | +17 | 74 | worse |
| ① Time stop 10 candles (< 0.5 ATR progress) | 455 | +254 | +20 | +1.2 | +14 / +1 / +5 | +2 | 49 | promising |
| ① Time stop 20 candles | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ① Flip ride ON | 454 | +224 | -10 | -0.4 | -35 / -16 / +41 | +23 | 49 | worse |
| ② LTF pierce late window 0 | 406 | +224 | -10 | -0.2 | -26 / +22 / -6 | -8 | 47 | worse |
| ② LTF pierce late window 2 | 464 | +216 | -18 | -0.8 | +4 / -0 / -22 | -9 | 49 | worse |
| ② HTF pierce late window 0 | 450 | +217 | -17 | -1.5 | +6 / -8 / -14 | +0 | 49 | worse |
| ② HTF pierce late window 2 | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ② HTF late trade-colour OFF | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ② HTF pierce replaces current setup | 458 | +229 | -4 | -0.5 | +4 / +6 / -15 | -15 | 50 | worse |
| ② HTF pierce requires close beyond LTF EMA9/20 | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ② Flip: require pullback first (wait 10) | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ② Trigger HTF CBC Flip OFF | 428 | +246 | +12 | +0.2 | -20 / +28 / +3 | +18 | 29 | noise |
| ② Trigger LTF EMA20 Pierce OFF | 137 | +111 | -123 | -1.4 | -56 / -13 / -55 | -35 | 31 | worse |
| ② Trigger HTF EMA9 Pierce OFF | 414 | +182 | -51 | -1.6 | -9 / -17 / -25 | +0 | 57 | worse |
| ② Trigger HTF EMA20 Pierce OFF | 450 | +219 | -15 | -1.6 | -1 / -14 / +0 | +0 | 49 | worse |
| ① Flip distance 1.5 ATR | 453 | +225 | -9 | -1.9 | +0 / +0 / -9 | -9 | 49 | worse |
| ① Flip distance 3 ATR | 456 | +244 | +10 | +1.6 | +10 / +0 / +0 | +0 | 49 | noise |
| ① Flip side gate OFF | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ① Flip side gate 2 pts | 454 | +226 | -8 | -1.2 | -8 / +0 / +0 | +0 | 49 | worse |
| ① Flip VWAP slope OFF | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ① HTF pierce min ER 0 | 480 | +245 | +12 | +0.4 | +6 / +7 / -2 | -2 | 49 | noise |
| ① HTF pierce min ER 0.23 | 440 | +220 | -14 | -0.7 | +1 / -6 / -9 | +6 | 49 | worse |
| ① LTF pierce min ER 0.12 | 445 | +249 | +16 | +0.9 | +15 / +6 / -5 | -1 | 49 | noise |
| ① LTF pierce min ER 0.15 | 427 | +257 | +23 | +0.8 | +10 / +17 / -3 | +2 | 49 | noise |
| ① LTF pierce min ER 0.23 | 380 | +221 | -13 | -0.3 | +4 / +24 / -41 | -20 | 41 | worse |
| ① VWAP reclaim block OFF | 458 | +236 | +2 | +0.2 | +3 / +2 / -3 | +0 | 49 | noise |
| ① VWAP reclaim block 8 | 454 | +234 | +0 | +0.0 | +0 / +0 / +0 | +0 | 49 | noise |
| ① Min candles between setups 5 | 461 | +249 | +15 | +1.1 | +19 / +6 / -10 | -10 | 50 | noise |
| ① Min candles 15 | 450 | +232 | -2 | -0.2 | +1 / +1 / -3 | -9 | 49 | worse |
| ① ATR length 10 | 455 | +169 | -65 | -0.8 | -11 / -36 / -18 | +4 | 48 | worse |
| ① ATR length 20 | 457 | +216 | -18 | -0.2 | -34 / -11 / +27 | +2 | 48 | worse |
| ① No new setups 16:00-19:00 | 450 | +247 | +14 | +0.7 | +9 / -0 / +5 | +3 | 45 | noise |
| ① No-new-setup window OFF | 485 | +190 | -44 | -1.5 | -13 / -27 / -4 | -8 | 53 | worse |
| ① OR forming blocks all OFF | 490 | +311 | +77 | +2.4 | +36 / -7 / +49 | +31 | 60 | noise |
| ① End setups at 16:00 OFF | 454 | +240 | +6 | +0.8 | +0 / +6 / -0 | -0 | 49 | noise |
| ③ Slope 0.0 | 1192 | -365 | -599 | -4.2 | -279 / -114 / -205 | -156 | 458 | robustly worse |
| ③ Slope 0.6 | 604 | +172 | -62 | -0.9 | -33 / -42 / +12 | -27 | 70 | worse |
| ③ Slope 0.65 | 548 | +209 | -25 | -0.4 | -28 / -24 / +27 | -21 | 65 | worse |
| ③ Slope 0.7 | 500 | +218 | -16 | -0.4 | -9 / -7 / +1 | -24 | 52 | worse |
| ③ Slope 0.8 | 406 | +219 | -15 | -0.4 | -11 / -22 / +18 | +10 | 49 | worse |
| ③ Slope 0.9 | 308 | +181 | -53 | -0.8 | -18 / -34 / -1 | -6 | 50 | worse |
| Existing: MTF gate OFF | 483 | +310 | +77 | +2.6 | +15 / +13 / +48 | +36 | 41 | robust |
| Existing: flips >= 4 OFF | 462 | +217 | -17 | -0.7 | -11 / +0 / -6 | -14 | 55 | worse |
| Existing: skip all from 9 HTF candles OFF | 559 | +125 | -109 | -2.3 | -5 / -55 / -48 | -12 | 69 | robustly worse |
| Existing: skip all from 7 | 397 | +205 | -29 | -0.8 | +0 / -28 / -1 | +7 | 49 | worse |
| Existing: skip all from 12 | 493 | +129 | -105 | -3.6 | +1 / -66 / -40 | -21 | 61 | worse |
| ① Toward late-away 1 pt (instead of strict) | 480 | +194 | -40 | -1.7 | -8 / -5 / -26 | -29 | 64 | worse |
| ① Max SL1 cap 8 (symbol list) | 454 | +202 | -32 | -2.1 | -8 / -5 / -19 | -19 | 44 | robustly worse |
| ① Max SL1 cap 12 | 454 | +207 | -27 | -2.3 | -16 / +6 / -16 | -16 | 49 | worse |

## MGC 2m: full ①②③ sweep on live + v1.13 set

Base: 863 trades, net +329, avg +0.38, thirds +170 / +126 / +33, last 4 wk -24, max DD 93

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ③ CHOP > 61.8 block | 801 | +303 | -26 | -0.5 | -74 / +21 / +27 | +27 | 94 | worse |
| ③ CHOP > 58 block | 725 | +298 | -31 | -0.5 | -81 / +19 / +31 | +18 | 75 | worse |
| ③ ADX < 20 block | 683 | +200 | -129 | -1.9 | -109 / -32 / +12 | +17 | 91 | worse |
| ③ ADX < 15 block | 820 | +314 | -15 | -0.4 | -32 / +31 / -13 | -12 | 101 | worse |
| ③ EMA20/VWAP crosses >= 4 block | 791 | +210 | -119 | -2.4 | -60 / -68 / +9 | -8 | 95 | worse |
| ③ crosses >= 6 block | 859 | +321 | -8 | -0.7 | +1 / -5 / -4 | +0 | 93 | worse |
| ③ N-bar range < 2 ATR block | 855 | +311 | -18 | -0.9 | -15 / -7 / +4 | +9 | 84 | worse |
| ③ N-bar range < 3 ATR block | 607 | +343 | +15 | +0.2 | -94 / +70 / +38 | +27 | 55 | noise |
| ③ HTF flips >= 2 in 8 block | 442 | +52 | -276 | -2.7 | -127 / -117 / -32 | +3 | 80 | robustly worse |
| ③ HTF flips >= 3 in 8 block | 759 | +285 | -44 | -0.8 | -5 / -45 / +5 | -8 | 85 | worse |
| ③ HTF flips >= 4 in 8 block | 845 | +336 | +7 | +0.3 | +9 / +8 / -10 | -9 | 97 | noise |
| ③ Skip non-flip setups from 6 HTF candles after flip | 560 | +366 | +37 | +0.4 | +11 / +39 / -13 | +10 | 81 | noise |
| ③ ... from 9 | 690 | +346 | +17 | +0.3 | -26 / +47 / -4 | +16 | 80 | noise |
| ③ ... from 12 | 778 | +339 | +10 | +0.2 | +7 / +5 / -2 | +21 | 73 | noise |
| ③ Block if VWAP -3 / +2 pts | 822 | +302 | -27 | -0.8 | -14 / -12 / -1 | -14 | 89 | worse |
| ③ Block if EMA200 -3 / +2 pts | 806 | +277 | -52 | -1.4 | -15 / -11 / -26 | -9 | 95 | worse |
| ③ Environment EMA200 vs VWAP | 543 | +193 | -136 | -1.6 | -86 / -29 / -21 | -17 | 73 | worse |
| ③ Skip while ATR > 1.8 x ATR(100) | 840 | +362 | +33 | +1.5 | -29 / +22 / +41 | +22 | 69 | noise |
| ③ Skip if SL1 cap < 1.5 ATR | 755 | +342 | +14 | +0.3 | -47 / +45 / +16 | +12 | 83 | noise |
| ③ ER 0.18 | 930 | +308 | -21 | -0.4 | -10 / -8 / -3 | -0 | 96 | worse |
| ③ ER 0.20 | 905 | +305 | -23 | -0.6 | -17 / -7 / +1 | +10 | 86 | worse |
| ③ ER 0.26 | 821 | +363 | +34 | +1.0 | +21 / +22 / -9 | -1 | 96 | noise |
| ③ ER 0.30 | 789 | +374 | +45 | +0.9 | +11 / +38 / -4 | -3 | 91 | noise |
| ③ ER filter OFF | 1062 | +320 | -9 | -0.1 | -31 / +70 / -48 | -60 | 154 | worse |
| ③ ER breakout exception OFF | 533 | +127 | -202 | -2.1 | -155 / -61 / +15 | +10 | 52 | worse |
| ③ Range gate 4 ATR | 929 | +326 | -2 | -0.0 | -15 / +42 / -29 | -36 | 123 | worse |
| ③ Range gate 6 ATR | 819 | +257 | -71 | -1.9 | -23 / -5 / -42 | -23 | 116 | worse |
| ③ Range gate zone 30 % | 789 | +275 | -53 | -1.1 | -12 / -21 / -20 | +17 | 81 | worse |
| ③ Range gate OFF | 987 | +331 | +3 | +0.0 | -50 / +98 / -46 | -47 | 138 | noise |
| ③ VWAP stretch 3 ATR | 321 | +249 | -79 | -0.7 | -61 / +7 / -26 | +18 | 49 | worse |
| ③ VWAP stretch 6 ATR | 532 | +286 | -43 | -0.5 | -50 / +9 / -2 | +12 | 67 | worse |
| ③ VWAP stretch ON 4 ATR | 392 | +211 | -118 | -1.1 | -92 / -16 / -10 | +25 | 57 | worse |
| ① Flip min ER 0.15 | 871 | +339 | +10 | +0.4 | +7 / +1 / +2 | -1 | 96 | noise |
| ① Flip min ER 0.30 | 846 | +346 | +18 | +0.6 | +18 / -4 / +4 | -6 | 98 | noise |
| ① Toward late-away 1 pt (instead of strict) | 863 | +329 | +0 | +0.0 | +0 / +0 / +0 | +0 | 93 | noise |
| ① SL1 x 1.5 ATR | 866 | +298 | -31 | -0.7 | -1 / -8 / -22 | -11 | 112 | worse |
| ① SL1 x 2.0 | 862 | +332 | +4 | +0.1 | -15 / +9 / +9 | +15 | 82 | noise |
| ① SL1 x 2.5 | 855 | +364 | +35 | +0.7 | -11 / +29 / +18 | +19 | 78 | noise |
| ① SL1 x 3.0 | 854 | +378 | +49 | +0.9 | -18 / +25 / +42 | +35 | 67 | noise |
| ① SL1 x 3.5 | 853 | +377 | +48 | +0.9 | -20 / +25 / +43 | +39 | 67 | noise |
| ① TP1 x 1.25 ATR | 876 | +246 | -83 | -0.8 | -44 / -55 / +16 | -2 | 71 | worse |
| ① TP1 x 1.5 | 868 | +250 | -79 | -0.9 | -24 / -31 / -23 | -13 | 98 | worse |
| ① TP1 x 1.75 | 863 | +307 | -22 | -0.3 | -9 / -11 / -2 | -7 | 88 | worse |
| ① TP1 x 2.0 | 858 | +283 | -46 | -0.6 | +3 / -22 / -26 | -22 | 102 | worse |
| ① TP1 x 2.5 | 854 | +324 | -5 | -0.1 | +37 / -24 / -17 | -47 | 121 | worse |
| ① Close at TP1 0 % | 863 | +442 | +114 | +1.2 | +28 / +60 / +26 | -31 | 135 | promising |
| ① Close at TP1 50 % | 863 | +371 | +43 | +0.4 | +10 / +22 / +10 | -12 | 101 | noise |
| ① Close at TP1 80 % | 863 | +329 | +0 | +0.0 | +0 / +0 / +0 | +0 | 93 | noise |
| ① Close at TP1 100 % | 916 | +255 | -74 | -0.7 | -13 / -32 / -28 | -6 | 106 | worse |
| ① Breakeven at TP1 OFF | 859 | +315 | -13 | -0.3 | +1 / -6 / -8 | -9 | 96 | worse |
| ① Trail 1.3 ATR | 894 | +296 | -33 | -0.4 | +3 / -20 / -16 | -8 | 106 | worse |
| ① Trail 1.7 ATR | 863 | +329 | +0 | +0.0 | +0 / +0 / +0 | +0 | 93 | noise |
| ① Trail 2.5 ATR | 820 | +346 | +18 | +0.2 | +13 / +21 / -16 | -5 | 98 | noise |
| ① Trail 3.5 ATR | 801 | +312 | -17 | -0.2 | -5 / +17 / -29 | -3 | 97 | worse |
| ① No trail | 797 | +331 | +2 | +0.0 | +1 / +30 / -29 | -6 | 100 | noise |
| ① Min SL x 0.6 | 865 | +321 | -8 | -0.2 | -17 / +10 / -1 | -6 | 90 | worse |
| ① Min SL x 1.4 | 852 | +378 | +50 | +0.9 | -15 / +25 / +39 | +39 | 68 | noise |
| ① Max SL1 cap OFF | 862 | +325 | -4 | -0.1 | -8 / +9 / -4 | +3 | 100 | worse |
| ① Max TP1 cap OFF | 859 | +300 | -29 | -0.5 | -40 / +4 / +8 | +1 | 86 | worse |
| ① Time stop 10 candles (< 0.5 ATR progress) | 865 | +328 | -1 | -0.1 | -5 / -9 / +13 | +8 | 82 | worse |
| ① Time stop 20 candles | 864 | +326 | -3 | -0.4 | +0 / -3 / +0 | +0 | 93 | worse |
| ① Flip ride ON | 863 | +357 | +28 | +0.8 | -12 / -25 / +65 | +24 | 92 | noise |
| ① Flip distance floor 8 pts | 857 | +337 | +9 | +0.6 | +2 / +12 / -6 | +0 | 98 | noise |
| ② LTF pierce late window 0 | 797 | +304 | -24 | -0.5 | -19 / -2 / -4 | -14 | 97 | worse |
| ② LTF pierce late window 2 | 890 | +311 | -17 | -0.5 | +11 / -9 / -20 | -1 | 96 | worse |
| ② HTF pierce late window 0 | 851 | +340 | +12 | +0.7 | -7 / +7 / +12 | +8 | 85 | noise |
| ② HTF pierce late window 2 | 866 | +328 | -1 | -0.1 | -1 / -1 / +1 | +0 | 93 | worse |
| ② HTF late trade-colour OFF | 863 | +329 | +0 | +0.0 | +0 / +0 / +0 | +0 | 93 | noise |
| ② HTF pierce replaces current setup | 875 | +346 | +17 | +0.9 | -5 / +20 / +2 | -2 | 95 | noise |
| ② HTF pierce requires close beyond LTF EMA9/20 | 863 | +329 | +0 | +0.0 | +0 / +0 / +0 | +0 | 93 | noise |
| ② Flip: require pullback first (wait 10) | 863 | +329 | +0 | +0.0 | +0 / +0 / +0 | +0 | 93 | noise |
| ② Trigger HTF CBC Flip OFF | 801 | +292 | -36 | -0.7 | +11 / -35 / -12 | -12 | 108 | worse |
| ② Trigger LTF EMA20 Pierce OFF | 379 | +155 | -174 | -1.5 | -103 / -35 / -36 | +2 | 56 | worse |
| ② Trigger HTF EMA9 Pierce OFF | 734 | +334 | +5 | +0.1 | -59 / +20 / +44 | +20 | 60 | noise |
| ② Trigger HTF EMA20 Pierce OFF | 848 | +294 | -34 | -1.7 | -7 / -23 / -4 | +0 | 93 | worse |
| ① Flip distance 1.5 ATR | 862 | +336 | +7 | +1.5 | +0 / +0 / +7 | +7 | 87 | noise |
| ① Flip distance 3 ATR | 869 | +304 | -25 | -1.9 | -12 / -12 / +0 | +0 | 93 | worse |
| ① Flip side gate OFF | 863 | +329 | +0 | +0.0 | +0 / +0 / +0 | +0 | 93 | noise |
| ① Flip side gate 2 pts | 863 | +329 | +0 | +0.0 | +0 / +0 / +0 | +0 | 93 | noise |
| ① Flip VWAP slope OFF | 863 | +329 | +0 | +0.0 | +0 / +0 / +0 | +0 | 93 | noise |
| ① HTF pierce min ER 0 | 985 | +354 | +25 | +0.4 | +33 / +33 / -41 | -8 | 121 | noise |
| ① HTF pierce min ER 0.23 | 814 | +304 | -25 | -0.7 | -24 / -10 / +8 | +3 | 88 | worse |
| ① LTF pierce min ER 0.12 | 796 | +224 | -104 | -2.2 | -47 / -43 / -15 | +5 | 83 | robustly worse |
| ① LTF pierce min ER 0.15 | 744 | +207 | -122 | -1.9 | -80 / -32 / -10 | +14 | 63 | worse |
| ① LTF pierce min ER 0.23 | 607 | +158 | -171 | -1.9 | -137 / -34 / -1 | -10 | 72 | worse |
| ① VWAP reclaim block OFF | 888 | +357 | +28 | +1.1 | +10 / -4 / +23 | +15 | 80 | noise |
| ① VWAP reclaim block 8 | 861 | +318 | -10 | -1.1 | -1 / -5 / -4 | +0 | 97 | worse |
| ① Min candles between setups 5 | 884 | +321 | -8 | -0.3 | -29 / +21 / +1 | +2 | 90 | worse |
| ① Min candles 15 | 844 | +346 | +17 | +0.7 | -2 / -5 / +24 | +3 | 82 | noise |
| ① ATR length 10 | 864 | +306 | -22 | -0.2 | +4 / -18 / -9 | +2 | 93 | worse |
| ① ATR length 20 | 856 | +317 | -11 | -0.1 | -6 / +4 / -9 | -3 | 80 | worse |
| ① No new setups 16:00-19:00 | 855 | +343 | +15 | +1.1 | +8 / -2 / +8 | +3 | 85 | noise |
| ① No-new-setup window OFF | 930 | +312 | -16 | -0.4 | -1 / -11 / -4 | -6 | 96 | worse |
| ① OR forming blocks all OFF | 937 | +350 | +22 | +0.5 | +5 / +25 / -8 | +11 | 89 | noise |
| ① End setups at 16:00 OFF | 863 | +323 | -6 | -0.3 | +1 / +1 / -8 | -3 | 97 | worse |
| ③ Slope 0.0 | 1789 | -74 | -403 | -2.5 | -126 / -80 / -196 | -42 | 238 | robustly worse |
| ③ Slope 0.2 | 1289 | +313 | -15 | -0.1 | -42 / +40 / -14 | +15 | 111 | worse |
| ③ Slope 0.3 | 1059 | +291 | -38 | -0.5 | +12 / -33 / -17 | +2 | 81 | worse |
| ③ Slope 0.48 | 755 | +340 | +11 | +0.2 | +1 / +1 / +9 | -2 | 91 | noise |
| ③ Slope 0.55 | 645 | +285 | -44 | -0.5 | -43 / +7 / -7 | -12 | 87 | worse |
| Existing: range gate 5 OFF | 987 | +331 | +3 | +0.0 | -50 / +98 / -46 | -47 | 138 | noise |

## MNQ 2m: full ①②③ sweep on live + v1.13 set

Base: 732 trades, net +3566, avg +4.87, thirds +1397 / +487 / +1681, last 4 wk +733, max DD 844

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ③ CHOP > 61.8 block | 672 | +3467 | -99 | -0.2 | +423 / -345 / -178 | -85 | 946 | worse |
| ③ CHOP > 58 block | 605 | +3450 | -116 | -0.2 | +436 / -401 / -151 | -10 | 853 | worse |
| ③ ADX < 20 block | 607 | +1588 | -1978 | -2.6 | -635 / -1 / -1342 | -1311 | 642 | robustly worse |
| ③ ADX < 15 block | 702 | +2462 | -1104 | -2.6 | +43 / -78 / -1069 | -1039 | 805 | worse |
| ③ EMA20/VWAP crosses >= 4 block | 682 | +2524 | -1042 | -2.1 | -434 / -538 / -69 | +47 | 1098 | robustly worse |
| ③ crosses >= 6 block | 727 | +3504 | -62 | -0.4 | -101 / +60 / -21 | -47 | 813 | worse |
| ③ N-bar range < 2 ATR block | 719 | +3686 | +120 | +0.5 | +79 / -9 / +50 | +19 | 896 | noise |
| ③ N-bar range < 3 ATR block | 489 | +2741 | -825 | -0.8 | +102 / -358 / -570 | -51 | 662 | worse |
| ③ HTF flips >= 2 in 8 block | 395 | +66 | -3499 | -3.0 | -1403 / -838 / -1258 | -1037 | 1236 | robustly worse |
| ③ HTF flips >= 3 in 8 block | 662 | +1867 | -1699 | -2.9 | -256 / -711 / -731 | -713 | 1314 | robustly worse |
| ③ HTF flips >= 4 in 8 block | 713 | +3408 | -157 | -0.6 | -36 / -181 / +59 | +167 | 810 | worse |
| ③ Skip non-flip setups from 6 HTF candles after flip | 509 | +3013 | -553 | -0.7 | +17 / -143 / -427 | +41 | 598 | worse |
| ③ ... from 9 | 617 | +3462 | -104 | -0.2 | +74 / +123 / -301 | -71 | 601 | worse |
| ③ ... from 12 | 675 | +3369 | -197 | -0.5 | -33 / -22 / -141 | -15 | 753 | worse |
| ③ Block if VWAP -3 / +2 pts | 728 | +3407 | -159 | -1.2 | -11 / -148 / +0 | +0 | 836 | worse |
| ③ Block if EMA200 -3 / +2 pts | 730 | +3563 | -3 | -0.0 | +0 / -3 / +0 | +0 | 848 | worse |
| ③ Environment EMA200 vs VWAP | 468 | +3251 | -315 | -0.3 | -272 / -396 / +353 | +118 | 942 | worse |
| ③ Skip while ATR > 1.8 x ATR(100) | 716 | +3533 | -33 | -0.1 | -60 / -141 / +168 | +49 | 836 | worse |
| ③ Skip if SL1 cap < 1.5 ATR | 488 | +897 | -2669 | -3.0 | -912 / -303 / -1454 | -1082 | 762 | robustly worse |
| ③ ER 0.18 | 763 | +3669 | +103 | +0.2 | +160 / +66 / -122 | -113 | 759 | noise |
| ③ ER 0.20 | 753 | +3547 | -19 | -0.1 | +88 / -99 / -8 | +11 | 890 | worse |
| ③ ER 0.26 | 710 | +3491 | -75 | -0.2 | -76 / -50 / +51 | +7 | 851 | worse |
| ③ ER 0.30 | 688 | +3417 | -149 | -0.3 | -137 / +5 / -17 | +35 | 860 | worse |
| ③ ER filter OFF | 848 | +3580 | +14 | +0.0 | +284 / +187 / -457 | -427 | 737 | noise |
| ③ ER breakout exception OFF | 512 | +3372 | -194 | -0.2 | +149 / -5 / -338 | +159 | 619 | worse |
| ③ Range gate 4 ATR | 699 | +3280 | -286 | -0.6 | -235 / -66 / +14 | +43 | 802 | worse |
| ③ Range gate 6 ATR | 620 | +2442 | -1124 | -1.4 | -860 / -360 / +95 | +161 | 1076 | worse |
| ③ Range gate zone 30 % | 587 | +2386 | -1180 | -1.3 | -525 / +109 / -764 | -707 | 664 | worse |
| ③ Range gate ON 5 ATR | 644 | +2999 | -566 | -0.8 | -795 / +102 / +126 | -18 | 781 | worse |
| ③ VWAP stretch 3 ATR | 234 | +1082 | -2483 | -2.0 | -1157 / -128 / -1198 | -399 | 309 | robustly worse |
| ③ VWAP stretch 6 ATR | 432 | +1389 | -2177 | -2.3 | -1273 / +184 / -1088 | -627 | 538 | worse |
| ③ VWAP stretch ON 4 ATR | 302 | +457 | -3109 | -2.7 | -1330 / -232 / -1547 | -644 | 427 | robustly worse |
| ① Flip min ER 0.15 | 745 | +3514 | -52 | -0.2 | -75 / +4 / +19 | -3 | 894 | worse |
| ① Flip min ER 0.30 | 720 | +2462 | -1104 | -3.1 | -438 / -680 / +15 | +44 | 1150 | worse |
| ① Toward late-away 1 pt (instead of strict) | 732 | +3566 | +0 | +0.0 | +0 / +0 / +0 | +0 | 844 | noise |
| ① SL1 x 1.5 ATR | 733 | +3450 | -116 | -0.3 | -58 / -49 / -9 | +12 | 910 | worse |
| ① SL1 x 2.0 | 731 | +3543 | -23 | -0.1 | +3 / +45 / -71 | -30 | 841 | worse |
| ① SL1 x 2.5 | 730 | +3505 | -61 | -0.1 | +30 / +20 / -111 | -51 | 864 | worse |
| ① SL1 x 3.0 | 730 | +3473 | -93 | -0.2 | +23 / -8 / -108 | -54 | 886 | worse |
| ① SL1 x 3.5 | 730 | +3463 | -103 | -0.2 | +22 / -12 / -112 | -54 | 889 | worse |
| ① TP1 x 1.25 ATR | 754 | +3703 | +137 | +0.3 | +72 / +125 / -60 | +49 | 797 | noise |
| ① TP1 x 1.5 | 739 | +3604 | +38 | +0.1 | +85 / +82 / -129 | +15 | 848 | noise |
| ① TP1 x 1.75 | 731 | +3501 | -65 | -0.5 | -12 / +0 / -53 | +0 | 844 | worse |
| ① TP1 x 2.0 | 725 | +3585 | +19 | +0.1 | +50 / +3 / -35 | -0 | 801 | noise |
| ① TP1 x 2.5 | 719 | +3566 | -0 | -0.0 | +26 / -7 / -20 | +16 | 778 | worse |
| ① Close at TP1 0 % | 732 | +3566 | +0 | +0.0 | +0 / +0 / +0 | +0 | 844 | noise |
| ① Close at TP1 50 % | 732 | +2659 | -907 | -0.9 | -297 / -115 / -495 | -377 | 465 | worse |
| ① Close at TP1 80 % | 732 | +2114 | -1452 | -1.4 | -475 / -185 / -792 | -604 | 385 | worse |
| ① Close at TP1 100 % | 868 | +1506 | -2060 | -1.7 | -440 / -357 / -1263 | -1003 | 473 | worse |
| ① Breakeven at TP1 OFF | 698 | +3187 | -379 | -0.5 | +95 / -381 / -92 | -60 | 1068 | worse |
| ① Trail 1.3 ATR | 844 | +1941 | -1625 | -1.5 | -668 / -504 / -453 | -216 | 703 | worse |
| ① Trail 1.7 ATR | 810 | +2168 | -1397 | -1.4 | -551 / -546 / -300 | -316 | 804 | worse |
| ① Trail 2.5 ATR | 763 | +3560 | -6 | -0.0 | +125 / -181 / +50 | +110 | 770 | worse |
| ① Trail 3.5 ATR | 739 | +3688 | +123 | +0.3 | +129 / +61 / -67 | -8 | 789 | noise |
| ① No trail | 732 | +3566 | +0 | +0.0 | +0 / +0 / +0 | +0 | 844 | noise |
| ① Min SL x 0.6 | 736 | +3648 | +82 | +0.2 | +54 / +28 / +0 | +20 | 841 | noise |
| ① Min SL x 1.4 | 724 | +3605 | +39 | +0.0 | +183 / -120 / -24 | -124 | 917 | noise |
| ① Max SL1 cap OFF | 724 | +3054 | -512 | -0.8 | -369 / -123 / -20 | -49 | 950 | worse |
| ① Max TP1 cap OFF | 729 | +3343 | -223 | -0.9 | -74 / -89 / -60 | -11 | 904 | worse |
| ① Time stop 10 candles (< 0.5 ATR progress) | 740 | +3573 | +7 | +0.0 | +37 / +38 / -68 | +6 | 803 | noise |
| ① Time stop 20 candles | 733 | +3561 | -5 | -0.1 | +0 / -5 / +0 | +0 | 850 | worse |
| ① Flip ride ON | 732 | +3285 | -281 | -0.8 | -49 / -163 / -68 | +29 | 972 | worse |
| ② LTF pierce late window 0 | 687 | +3999 | +433 | +0.9 | +164 / -27 / +296 | +80 | 769 | noise |
| ② LTF pierce late window 2 | 745 | +3523 | -43 | -0.1 | -296 / +58 / +195 | +176 | 773 | worse |
| ② HTF pierce late window 0 | 725 | +3281 | -285 | -1.6 | -1 / -46 / -238 | +0 | 890 | worse |
| ② HTF pierce late window 2 | 736 | +3537 | -28 | -0.3 | -2 / -22 / -4 | -4 | 867 | worse |
| ② HTF late trade-colour OFF | 732 | +3566 | +0 | +0.0 | +0 / +0 / +0 | +0 | 844 | noise |
| ② HTF pierce replaces current setup | 739 | +3807 | +241 | +1.2 | -62 / +72 / +231 | +231 | 806 | noise |
| ② HTF pierce requires close beyond LTF EMA9/20 | 732 | +3566 | +0 | +0.0 | +0 / +0 / +0 | +0 | 844 | noise |
| ② Flip: require pullback first (wait 10) | 732 | +3566 | +0 | +0.0 | +0 / +0 / +0 | +0 | 844 | noise |
| ② Trigger HTF CBC Flip OFF | 664 | +945 | -2620 | -3.5 | -1254 / -635 / -731 | -714 | 1119 | robustly worse |
| ② Trigger LTF EMA20 Pierce OFF | 345 | +3782 | +216 | +0.2 | -115 / +184 / +147 | +102 | 333 | noise |
| ② Trigger HTF EMA9 Pierce OFF | 644 | +3172 | -394 | -0.6 | -314 / -184 / +104 | +113 | 835 | worse |
| ② Trigger HTF EMA20 Pierce OFF | 728 | +3448 | -118 | -0.9 | +0 / +2 / -120 | -76 | 842 | worse |
| ① Flip distance 1.5 ATR | 729 | +3381 | -185 | -1.5 | -186 / +0 / +1 | +0 | 844 | worse |
| ① Flip distance 3 ATR | 739 | +3390 | -176 | -1.1 | -33 / -32 / -111 | -80 | 844 | worse |
| ① Flip side gate OFF | 733 | +3540 | -26 | -0.5 | +0 / -26 / +0 | +0 | 844 | worse |
| ① Flip side gate 2 pts | 732 | +3566 | +0 | +0.0 | +0 / +0 / +0 | +0 | 844 | noise |
| ① Flip VWAP slope OFF | 732 | +3566 | +0 | +0.0 | +0 / +0 / +0 | +0 | 844 | noise |
| ① HTF pierce min ER 0 | 801 | +4540 | +974 | +1.7 | +356 / +332 / +287 | +274 | 615 | promising |
| ① HTF pierce min ER 0.23 | 707 | +3350 | -216 | -0.7 | +126 / -140 / -202 | -8 | 908 | worse |
| ① LTF pierce min ER 0.12 | 671 | +3629 | +63 | +0.1 | -140 / +71 / +132 | +134 | 755 | noise |
| ① LTF pierce min ER 0.15 | 635 | +3756 | +190 | +0.3 | -124 / +142 / +172 | +218 | 700 | noise |
| ① LTF pierce min ER 0.23 | 554 | +3735 | +169 | +0.2 | -43 / +129 / +84 | +241 | 580 | noise |
| ① VWAP reclaim block OFF | 748 | +3832 | +266 | +1.0 | +226 / -29 / +68 | -16 | 841 | noise |
| ① VWAP reclaim block 8 | 730 | +3569 | +3 | +0.0 | +0 / +31 / -28 | +0 | 813 | noise |
| ① Min candles between setups 5 | 743 | +3766 | +200 | +0.8 | -65 / +25 / +240 | +231 | 853 | noise |
| ① Min candles 15 | 720 | +3609 | +43 | +0.2 | -104 / +64 / +83 | +31 | 837 | noise |
| ① ATR length 10 | 737 | +3497 | -69 | -0.1 | +95 / -149 / -16 | +175 | 918 | worse |
| ① ATR length 20 | 725 | +3397 | -169 | -0.3 | +59 / +42 / -269 | -8 | 794 | worse |
| ① No new setups 16:00-19:00 | 720 | +3661 | +95 | +0.4 | +133 / +21 / -59 | +11 | 831 | noise |
| ① No-new-setup window OFF | 772 | +3551 | -15 | -0.0 | -101 / -121 / +206 | +61 | 948 | worse |
| ① OR forming blocks all OFF | 798 | +3737 | +171 | +0.3 | -137 / +261 / +47 | +140 | 642 | noise |
| ① End setups at 16:00 OFF | 732 | +3502 | -64 | -0.4 | +38 / -30 / -73 | -73 | 890 | worse |
| ③ Slope 0.0 | 1951 | +501 | -3065 | -1.4 | -977 / -919 / -1169 | -423 | 3224 | worse |
| ③ Slope 0.48 | 831 | +3579 | +13 | +0.0 | -132 / -259 / +404 | +441 | 1148 | noise |
| ③ Slope 0.6 | 646 | +3701 | +135 | +0.2 | +183 / +66 / -115 | +180 | 786 | noise |
| ③ Slope 0.65 | 580 | +2678 | -888 | -1.1 | +35 / -175 / -748 | -553 | 681 | worse |

## M2K 2m: full ①②③ sweep on live + v1.13 set

Base: 198 trades, net +33, avg +0.17, thirds -6 / +5 / +33, last 4 wk +20, max DD 23

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ③ CHOP > 61.8 block | 190 | +29 | -4 | -0.7 | +0 / -4 / -1 | -1 | 22 | worse |
| ③ CHOP > 58 block | 175 | +33 | +1 | +0.1 | +9 / -5 / -4 | -1 | 19 | noise |
| ③ ADX < 20 block | 148 | +13 | -20 | -1.2 | -8 / +10 / -22 | -13 | 26 | worse |
| ③ ADX < 15 block | 175 | +23 | -10 | -0.9 | -2 / +4 / -12 | -5 | 24 | worse |
| ③ EMA20/VWAP crosses >= 4 block | 183 | +23 | -10 | -1.1 | -4 / -1 / -5 | -9 | 24 | worse |
| ③ crosses >= 6 block | 196 | +30 | -3 | -1.0 | -1 / -2 / +0 | +0 | 24 | worse |
| ③ N-bar range < 2 ATR block | 192 | +33 | +1 | +0.1 | +3 / -1 / -1 | -1 | 20 | noise |
| ③ N-bar range < 3 ATR block | 147 | +29 | -4 | -0.2 | +8 / -2 / -10 | -0 | 14 | worse |
| ③ HTF flips >= 2 in 8 block | 105 | +23 | -10 | -0.4 | +2 / +14 / -26 | -14 | 18 | worse |
| ③ HTF flips >= 3 in 8 block | 178 | +43 | +10 | +1.0 | +3 / +7 / +0 | -3 | 18 | noise |
| ③ HTF flips >= 4 in 8 block | 195 | +27 | -5 | -1.1 | -3 / +0 / -3 | -3 | 22 | worse |
| ③ Skip non-flip setups from 6 HTF candles after flip | 114 | +13 | -20 | -1.0 | +17 / -22 / -14 | -8 | 27 | worse |
| ③ ... from 9 | 149 | +29 | -4 | -0.2 | +12 / -7 / -9 | -4 | 16 | worse |
| ③ ... from 12 | 163 | +22 | -11 | -0.8 | +1 / -5 / -7 | -4 | 22 | worse |
| ③ Block if VWAP -3 / +2 pts | 169 | +29 | -3 | -0.3 | -4 / -2 / +3 | +3 | 29 | worse |
| ③ Block if EMA200 -3 / +2 pts | 188 | +26 | -7 | -1.0 | -3 / -4 / +0 | +0 | 28 | worse |
| ③ Environment EMA200 vs VWAP | 129 | +8 | -24 | -1.3 | -4 / -4 / -17 | -7 | 24 | worse |
| ③ Skip while ATR > 1.8 x ATR(100) | 192 | +28 | -5 | -0.8 | -6 / +1 / -0 | +1 | 24 | worse |
| ③ Skip if SL1 cap < 1.5 ATR | 197 | +24 | -8 | -3.8 | +0 / +0 / -8 | -8 | 23 | worse |
| ③ ER 0.18 | 212 | +41 | +9 | +1.1 | +1 / +6 / +1 | -3 | 21 | promising |
| ③ ER 0.20 | 209 | +42 | +9 | +1.2 | +2 / +6 / +1 | -3 | 20 | promising |
| ③ ER 0.26 | 188 | +33 | +0 | +0.1 | +0 / -1 / +1 | +1 | 20 | noise |
| ③ ER 0.30 | 169 | +31 | -2 | -0.2 | +10 / +3 / -15 | -12 | 16 | worse |
| ③ ER filter OFF | 213 | +43 | +10 | +1.2 | +1 / +6 / +2 | -2 | 21 | promising |
| ③ ER breakout exception OFF | 166 | +26 | -7 | -0.5 | +1 / -2 / -6 | -4 | 21 | worse |
| ③ Range gate 4 ATR | 190 | +21 | -12 | -1.7 | -3 / +0 / -9 | -7 | 25 | worse |
| ③ Range gate 6 ATR | 164 | +17 | -15 | -1.1 | -4 / -4 / -7 | -10 | 24 | worse |
| ③ Range gate zone 30 % | 161 | +24 | -8 | -0.6 | +2 / +4 / -14 | -10 | 19 | worse |
| ③ Range gate ON 5 ATR | 178 | +23 | -10 | -0.9 | -1 / -1 / -8 | -8 | 22 | worse |
| ③ VWAP stretch 3 ATR | 32 | +8 | -25 | -0.9 | +12 / -3 / -34 | -20 | 4 | worse |
| ③ VWAP stretch 6 ATR | 78 | +22 | -10 | -0.4 | +10 / +6 / -26 | -13 | 8 | worse |
| ③ VWAP stretch ON 4 ATR | 52 | +20 | -12 | -0.5 | +12 / +1 / -26 | -16 | 4 | worse |
| ① Flip min ER 0.15 | 202 | +29 | -4 | -0.7 | -2 / -3 / +2 | +2 | 28 | worse |
| ① Flip min ER 0.30 | 193 | +21 | -11 | -2.0 | -4 / +3 / -11 | -8 | 24 | worse |
| ① Toward late-away 1 pt (instead of strict) | 198 | +33 | +0 | +0.0 | +0 / +0 / +0 | +0 | 23 | noise |
| ① SL1 x 1.5 ATR | 198 | +20 | -13 | -1.7 | -4 / +1 / -10 | +1 | 22 | worse |
| ① SL1 x 2.0 | 198 | +28 | -4 | -0.5 | -2 / -2 / -1 | -1 | 26 | worse |
| ① SL1 x 2.5 | 197 | +32 | -1 | -0.1 | +2 / -0 / -3 | -2 | 19 | worse |
| ① SL1 x 3.0 | 197 | +42 | +9 | +0.9 | +3 / +6 / -1 | +1 | 17 | noise |
| ① SL1 x 3.5 | 197 | +43 | +11 | +1.0 | +2 / +9 / -0 | +1 | 18 | noise |
| ① TP1 x 1.25 ATR | 201 | +32 | -1 | -0.0 | +7 / -4 / -4 | -0 | 19 | worse |
| ① TP1 x 1.5 | 199 | +33 | -0 | -0.0 | +1 / -2 / +0 | -0 | 21 | worse |
| ① TP1 x 1.75 | 198 | +32 | -1 | -0.0 | +1 / -4 / +2 | +1 | 26 | worse |
| ① TP1 x 2.0 | 198 | +34 | +2 | +0.1 | +2 / -4 / +4 | +5 | 29 | noise |
| ① TP1 x 2.5 | 198 | +46 | +13 | +0.6 | +7 / +1 / +5 | +7 | 23 | noise |
| ① Close at TP1 0 % | 198 | +68 | +35 | +1.5 | -4 / -3 / +42 | +32 | 39 | noise |
| ① Close at TP1 50 % | 198 | +46 | +13 | +0.6 | -1 / -1 / +16 | +12 | 29 | noise |
| ① Close at TP1 80 % | 198 | +33 | +0 | +0.0 | +0 / +0 / +0 | +0 | 23 | noise |
| ① Close at TP1 100 % | 202 | +22 | -11 | -0.5 | +4 / -3 / -12 | -8 | 23 | worse |
| ① Breakeven at TP1 OFF | 198 | +35 | +3 | +0.2 | +1 / +0 / +1 | +1 | 23 | noise |
| ① Trail 1.3 ATR | 202 | +27 | -6 | -0.3 | +4 / -2 / -8 | -5 | 25 | worse |
| ① Trail 1.7 ATR | 198 | +33 | +0 | +0.0 | +0 / +0 / +0 | +0 | 23 | noise |
| ① Trail 2.5 ATR | 193 | +34 | +1 | +0.1 | +3 / -1 / -1 | -1 | 23 | noise |
| ① Trail 3.5 ATR | 193 | +30 | -3 | -0.1 | +1 / -1 / -3 | -4 | 27 | worse |
| ① No trail | 192 | +35 | +2 | +0.1 | +3 / -1 / +1 | +0 | 27 | noise |
| ① Min SL x 0.6 | 198 | +38 | +5 | +0.5 | +5 / +1 / -1 | -1 | 19 | noise |
| ① Min SL x 1.4 | 198 | +33 | +0 | +0.0 | -2 / +2 / +0 | +2 | 24 | noise |
| ① Max SL1 cap OFF | 198 | +33 | +0 | +0.0 | +0 / +0 / +0 | +0 | 23 | noise |
| ① Max TP1 cap OFF | 198 | +43 | +10 | +0.9 | +5 / +3 / +2 | +5 | 29 | noise |
| ① Time stop 10 candles (< 0.5 ATR progress) | 198 | +27 | -5 | -0.9 | -5 / -1 / +0 | +0 | 28 | worse |
| ① Time stop 20 candles | 198 | +30 | -2 | -1.1 | -2 / +0 / +0 | +0 | 25 | worse |
| ① Flip ride ON | 198 | +23 | -10 | -1.4 | -2 / -8 / +0 | +8 | 32 | worse |
| ② LTF pierce late window 0 | 175 | +27 | -6 | -0.5 | -6 / -1 / +1 | +1 | 24 | worse |
| ② LTF pierce late window 2 | 204 | +34 | +1 | +0.2 | +2 / -3 / +3 | +1 | 25 | noise |
| ② HTF pierce late window 0 | 194 | +26 | -7 | -1.5 | +1 / +0 / -8 | -4 | 22 | worse |
| ② HTF pierce late window 2 | 199 | +37 | +5 | +2.2 | +5 / +0 / +0 | +0 | 19 | noise |
| ② HTF late trade-colour OFF | 199 | +33 | +0 | +0.2 | +0 / +0 / +0 | +0 | 22 | noise |
| ② HTF pierce replaces current setup | 198 | +33 | +0 | +0.0 | +0 / +0 / +0 | +0 | 23 | noise |
| ② HTF pierce requires close beyond LTF EMA9/20 | 198 | +33 | +0 | +0.0 | +0 / +0 / +0 | +0 | 23 | noise |
| ② Flip: require pullback first (wait 10) | 198 | +33 | +0 | +0.0 | +0 / +0 / +0 | +0 | 23 | noise |
| ② Trigger HTF CBC Flip OFF | 180 | +45 | +12 | +1.0 | +5 / +14 / -7 | -9 | 20 | noise |
| ② Trigger LTF EMA20 Pierce OFF | 70 | +20 | -12 | -0.5 | +5 / -7 / -11 | -7 | 16 | worse |
| ② Trigger HTF EMA9 Pierce OFF | 169 | +8 | -24 | -1.9 | -3 / -5 / -16 | -6 | 24 | worse |
| ② Trigger HTF EMA20 Pierce OFF | 197 | +32 | -0 | -0.2 | +0 / -0 / +0 | +0 | 23 | worse |
| ① Flip distance 1.5 ATR | 189 | +27 | -6 | -0.8 | -1 / +4 / -9 | -10 | 22 | worse |
| ① Flip distance 3 ATR | 208 | +25 | -8 | -1.0 | -11 / +1 / +3 | +6 | 35 | worse |
| ① Flip side gate OFF | 198 | +33 | +0 | +0.0 | +0 / +0 / +0 | +0 | 23 | noise |
| ① Flip side gate 2 pts | 197 | +33 | +1 | +0.2 | +1 / +0 / +0 | +0 | 22 | noise |
| ① Flip VWAP slope OFF | 198 | +33 | +0 | +0.0 | +0 / +0 / +0 | +0 | 23 | noise |
| ① HTF pierce min ER 0 | 235 | +51 | +18 | +1.3 | +9 / -1 / +11 | +9 | 21 | noise |
| ① HTF pierce min ER 0.23 | 188 | +35 | +3 | +0.4 | +4 / +1 / -2 | -1 | 18 | noise |
| ① LTF pierce min ER 0.12 | 268 | +8 | -24 | -1.3 | -20 / -5 / +1 | -3 | 42 | worse |
| ① LTF pierce min ER 0.15 | 237 | +22 | -10 | -0.7 | -17 / +0 / +6 | +0 | 38 | worse |
| ① LTF pierce min ER 0.23 | 177 | +21 | -11 | -1.1 | -2 / -2 / -6 | -6 | 26 | worse |
| ① VWAP reclaim block OFF | 200 | +35 | +2 | +0.5 | +1 / +0 / +1 | +1 | 22 | noise |
| ① VWAP reclaim block 8 | 197 | +32 | -1 | -0.4 | -1 / +0 / +0 | +0 | 24 | worse |
| ① Min candles between setups 5 | 198 | +33 | +0 | +0.0 | +0 / +0 / +0 | +0 | 23 | noise |
| ① Min candles 15 | 195 | +31 | -2 | -0.5 | +0 / -2 / +0 | +0 | 23 | worse |
| ① ATR length 10 | 204 | +23 | -9 | -0.4 | -4 / -1 / -4 | +1 | 28 | worse |
| ① ATR length 20 | 191 | +55 | +22 | +0.9 | +3 / +14 / +6 | +2 | 21 | noise |
| ① No new setups 16:00-19:00 | 194 | +35 | +3 | +0.6 | +0 / +2 / +1 | -1 | 23 | noise |
| ① No-new-setup window OFF | 216 | +33 | +1 | +0.1 | -0 / -4 / +5 | +6 | 32 | noise |
| ① OR forming blocks all OFF | 213 | +45 | +13 | +1.4 | +11 / -5 / +7 | +2 | 19 | noise |
| ① End setups at 16:00 OFF | 198 | +33 | +0 | +0.0 | +0 / +0 / +0 | +0 | 23 | noise |
| ③ Slope 0.0 | 1469 | -501 | -534 | -6.6 | -213 / -122 / -199 | -92 | 508 | robustly worse |
| ③ Slope 0.8 | 341 | +15 | -17 | -0.6 | -6 / -6 / -5 | -2 | 40 | worse |
| ③ Slope 0.9 | 259 | +43 | +11 | +0.6 | +6 / -9 / +14 | -1 | 22 | noise |
| ③ Slope 1.1 | 151 | +24 | -9 | -0.6 | -4 / -3 / -2 | -5 | 27 | worse |
| ③ Slope 1.2 | 118 | +43 | +10 | +0.5 | +15 / -6 / +1 | -0 | 16 | noise |
