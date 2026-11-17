① Auto Trade Setup inputs not studied before -- MES 3m and MGC 3m on the CBC EMA Slope branch (v1.05) -- 11/14/2026.
One change at a time on top of each chart's branch settings. Replay Jan 5 -> now (BarFeed / Databento bars, TV EMA20), net after costs
(MES 0.50, MGC 0.22). Entry filters are entry filters: a skipped setup can change later setups (cooldown, one-per-direction).
MES 3m base: ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR, HTF EMA20 slope >= 0.42 ATR; SL1 3 ATR min 5, TP1 1.75, 100 % at TP1;
  HTF CBC Flip setups ride to the HTF flip back / SL1 / 16:00 / next setup.
MGC 3m base: same filters with slope >= 0.30 + VWAP stretch 4 ATR; SL1 1.7 ATR min 5 cap 7, TP1 1.7 cap 6, 0 % at TP1 + BE, closed by the HTF flip.
Both: flip gates as live (close <= max(2 ATR, 8 pts) from the 3m EMA20 -- the replay engine has always used 8 pts for MGC too, live is 10;
  close beyond VWAP and EMA200 by 1 pt; VWAP slope agrees; flip ER >= 0.23); per-trigger ER mins LTF 0.08 / HTF 0.15; VWAP reclaim block 5 bars;
  min 10 candles between setups; skip a new setup while the same-direction one runs; ATR 14; setups end at 16:00.
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, better in all three thirds, last 4 wk >= 0; promising = z >= 1 and all thirds.
Not modelled: pivot reclaim block (R2/R3/S2/S3 not in the bar feed), TP/SL steps (pivot levels; ATR method is live), closed-15m-values mode,
act-on-flip-at-HTF-close, toward flips (studied 11/03), OR blocks (orb_all), min SL / SL / TP / trail / caps / time stop (other studies).

## Candidates (promising or better)

- MES 3m: Min ER LTF EMA20 Pierce 0.15 → +183, z +1.4, thirds +73 / +74 / +37, last 4 wk +10, max DD 252 vs 296 (promising)
- MES 3m: End setups at 16:00 Off → +52, z +1.3, thirds +18 / +13 / +21, last 4 wk +8, max DD 297 vs 296 (promising)

## MES 3m -- branch base: 1000 setups, win 49 %, net +350, avg +0.35, thirds +235 / -232 / +347, last 4 wk +164, max DD 296

| Change (one at a time) | Setups | Win % | Net | Avg | Δ vs base | z | Δ by third | Δ last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| Flip distance 1.5 ATR | 996 | 49 % | +315 | +0.32 | -35 | -1.4 | -20 / +18 / -33 | +13 | 280 | worse |
| Flip distance 2.5 ATR | 1006 | 48 % | +310 | +0.31 | -40 | -1.5 | -46 / +1 / +4 | +4 | 303 | worse |
| Flip distance 3 ATR | 1010 | 48 % | +310 | +0.31 | -40 | -1.2 | -40 / -4 / +4 | +4 | 308 | worse |
| Flip distance Off | 1020 | 48 % | +237 | +0.23 | -113 | -2.5 | -118 / -33 / +38 | -10 | 336 | worse |
| Flip side gate 0 pts | 1000 | 49 % | +350 | +0.35 | +0 | +0.0 | +0 / +0 / +0 | +0 | 296 | noise |
| Flip side gate 2 pts | 1000 | 49 % | +350 | +0.35 | +0 | +0.0 | +0 / +0 / +0 | +0 | 296 | noise |
| Flip side gate Off | 1001 | 49 % | +347 | +0.35 | -3 | -0.3 | -3 / +0 / +0 | +0 | 296 | worse |
| Flip VWAP slope must agree Off | 1000 | 49 % | +350 | +0.35 | +0 | +0.0 | +0 / +0 / +0 | +0 | 296 | noise |
| Flip EMA200 slope must agree On | 1000 | 49 % | +350 | +0.35 | +0 | +0.0 | +0 / +0 / +0 | +0 | 296 | noise |
| Flip min ER 0 (off) | 1044 | 48 % | +358 | +0.34 | +8 | +0.1 | -5 / +15 / -2 | -16 | 290 | noise |
| Flip min ER 0.15 | 1016 | 48 % | +327 | +0.32 | -23 | -0.4 | -33 / +36 / -27 | -17 | 265 | worse |
| Flip min ER 0.30 | 984 | 49 % | +232 | +0.24 | -118 | -2.2 | +2 / +30 / -151 | -46 | 306 | worse |
| Skip the flip setup when the flip is a flop | 999 | 49 % | +366 | +0.37 | +16 | +0.8 | +16 / +0 / +0 | +0 | 296 | noise |
| Also skip non-flip setups while the flip is a flop | 729 | 49 % | +401 | +0.55 | +51 | +0.3 | -5 / +35 / +20 | -6 | 273 | noise |
| Min ER LTF EMA20 Pierce 0 | 1179 | 49 % | +323 | +0.27 | -27 | -0.2 | +10 / +3 / -39 | -38 | 292 | worse |
| Min ER LTF EMA20 Pierce 0.15 | 836 | 49 % | +533 | +0.64 | +183 | +1.4 | +73 / +74 / +37 | +10 | 252 | promising |
| Min ER HTF EMA9/20 0 | 1161 | 48 % | +367 | +0.32 | +17 | +0.1 | +11 / +66 / -59 | -41 | 268 | noise |
| Min ER HTF EMA9/20 0.23 | 949 | 49 % | +304 | +0.32 | -46 | -0.6 | -49 / +9 / -6 | +2 | 288 | worse |
| Skip setups against the MTF (60m) CBC | 890 | 48 % | +147 | +0.17 | -203 | -2.2 | -38 / -26 / -139 | -77 | 317 | robustly worse |
| HTF EMA20 slope against the trade = skip (min 0) | 976 | 49 % | +346 | +0.35 | -4 | -0.1 | -17 / +16 / -3 | -8 | 276 | worse |
| VWAP reclaim block Off | 1029 | 49 % | +397 | +0.39 | +47 | +0.9 | +40 / -12 / +18 | +12 | 298 | noise |
| VWAP reclaim block 3 bars | 1001 | 49 % | +341 | +0.34 | -9 | -0.6 | +0 / -9 / +0 | +0 | 301 | worse |
| VWAP reclaim block 8 bars | 993 | 48 % | +318 | +0.32 | -32 | -1.4 | -20 / -4 / -8 | +0 | 296 | worse |
| Require price past both EMA clouds (chart 9/20) | 448 | 54 % | +548 | +1.22 | +198 | +0.9 | -53 / +173 / +78 | -34 | 141 | noise |
| ... + close beyond HTF EMA9 | 445 | 53 % | +548 | +1.23 | +198 | +0.9 | -45 / +173 / +70 | -34 | 141 | noise |
| ... + close beyond HTF EMA20 | 442 | 53 % | +543 | +1.23 | +193 | +0.9 | -45 / +181 / +57 | -45 | 133 | noise |
| Skip same-direction setup while running Off | 1050 | 48 % | +338 | +0.32 | -12 | -0.1 | +2 / -13 / -1 | +4 | 308 | worse |
| Min candles between setups 5 | 1022 | 49 % | +383 | +0.38 | +33 | +0.6 | -7 / -8 / +49 | +31 | 304 | noise |
| Min candles between setups 8 | 1012 | 49 % | +371 | +0.37 | +21 | +0.6 | -30 / +2 / +49 | +31 | 294 | noise |
| Min candles between setups 12 | 990 | 48 % | +345 | +0.35 | -5 | -0.1 | -22 / +15 / +2 | +0 | 287 | worse |
| Min candles between setups 15 | 960 | 48 % | +306 | +0.32 | -44 | -0.7 | -66 / +6 / +16 | -5 | 297 | worse |
| Min candles between setups 20 | 915 | 49 % | +344 | +0.38 | -6 | -0.1 | -68 / +54 / +8 | -21 | 273 | worse |
| ATR length 10 | 1015 | 49 % | +270 | +0.27 | -80 | -0.4 | -72 / +38 / -45 | -32 | 261 | worse |
| ATR length 15 (your chart) | 991 | 48 % | +273 | +0.28 | -77 | -0.4 | -9 / -10 / -58 | -11 | 302 | worse |
| ATR length 20 | 999 | 48 % | +290 | +0.29 | -60 | -0.3 | +49 / -50 / -59 | -11 | 345 | worse |
| End setups at 16:00 Off | 999 | 49 % | +402 | +0.40 | +52 | +1.3 | +18 / +13 / +21 | +8 | 297 | promising |

## MGC 3m -- branch base: 634 setups, win 22 %, net +1135, avg +1.79, thirds +545 / +78 / +512, last 4 wk +279, max DD 121

| Change (one at a time) | Setups | Win % | Net | Avg | Δ vs base | z | Δ by third | Δ last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| Flip distance 1.5 ATR | 631 | 22 % | +1157 | +1.83 | +22 | +0.7 | +22 / +0 / +0 | +0 | 114 | noise |
| Flip distance 2.5 ATR | 640 | 22 % | +1116 | +1.74 | -20 | -0.3 | -15 / -4 / -1 | +0 | 122 | worse |
| Flip distance 3 ATR | 642 | 22 % | +834 | +1.30 | -301 | -3.8 | -282 / -11 / -8 | -7 | 122 | robustly worse |
| Flip distance Off | 646 | 22 % | +827 | +1.28 | -309 | -3.6 | -282 / -18 / -8 | -7 | 122 | robustly worse |
| Flip distance floor 10 pts (MGC live value) | 635 | 22 % | +1139 | +1.79 | +4 | +0.1 | +0 / +4 / +0 | +0 | 121 | noise |
| Flip side gate 0 pts | 635 | 22 % | +1131 | +1.78 | -5 | -0.3 | +0 / +0 / -5 | +0 | 121 | worse |
| Flip side gate 2 pts | 633 | 22 % | +1136 | +1.79 | +0 | +0.0 | +0 / +0 / +0 | +0 | 121 | noise |
| Flip side gate Off | 636 | 22 % | +1140 | +1.79 | +4 | +0.2 | +0 / +9 / -5 | +0 | 121 | noise |
| Flip VWAP slope must agree Off | 635 | 22 % | +1102 | +1.74 | -33 | -0.9 | -33 / +0 / +0 | +0 | 121 | worse |
| Flip EMA200 slope must agree On | 634 | 22 % | +1135 | +1.79 | +0 | +0.0 | +0 / +0 / +0 | +0 | 121 | noise |
| Flip min ER 0 (off) | 652 | 22 % | +1156 | +1.77 | +21 | +0.2 | +7 / +34 / -21 | -4 | 117 | noise |
| Flip min ER 0.15 | 640 | 22 % | +1157 | +1.81 | +21 | +0.3 | -0 / +32 / -10 | +1 | 117 | noise |
| Flip min ER 0.30 | 629 | 23 % | +1169 | +1.86 | +34 | +0.4 | +18 / +7 / +9 | +2 | 121 | noise |
| Skip the flip setup when the flip is a flop | 628 | 22 % | +1170 | +1.86 | +35 | +0.7 | +14 / +6 / +15 | +0 | 121 | noise |
| Also skip non-flip setups while the flip is a flop | 362 | 22 % | +265 | +0.73 | -871 | -3.1 | -577 / +7 / -301 | -206 | 129 | worse |
| Min ER LTF EMA20 Pierce 0 | 703 | 21 % | +1000 | +1.42 | -136 | -0.8 | -56 / -38 / -42 | -14 | 150 | worse |
| Min ER LTF EMA20 Pierce 0.15 | 561 | 23 % | +1046 | +1.86 | -89 | -0.5 | -39 / -66 / +15 | +7 | 139 | worse |
| Min ER HTF EMA9/20 0 | 755 | 23 % | +1239 | +1.64 | +103 | +0.4 | +55 / +22 / +27 | -4 | 165 | noise |
| Min ER HTF EMA9/20 0.23 | 592 | 21 % | +1061 | +1.79 | -74 | -0.5 | -0 / -13 / -61 | +0 | 114 | worse |
| Skip setups against the MTF (60m) CBC | 528 | 23 % | +967 | +1.83 | -168 | -0.9 | -10 / -36 / -122 | -35 | 109 | worse |
| HTF EMA20 slope against the trade = skip (min 0) | 607 | 21 % | +1063 | +1.75 | -73 | -0.7 | -10 / -42 / -21 | -1 | 137 | worse |
| VWAP reclaim block Off | 677 | 22 % | +1177 | +1.74 | +42 | +0.4 | +59 / +1 / -18 | -0 | 131 | noise |
| VWAP reclaim block 3 bars | 640 | 22 % | +1209 | +1.89 | +73 | +1.4 | +86 / -12 / -0 | +0 | 112 | noise |
| VWAP reclaim block 8 bars | 627 | 22 % | +1120 | +1.79 | -15 | -0.3 | -22 / +10 / -3 | +0 | 121 | worse |
| Require price past both EMA clouds (chart 9/20) | 273 | 21 % | +390 | +1.43 | -745 | -2.2 | -329 / -138 / -277 | -187 | 173 | robustly worse |
| ... + close beyond HTF EMA9 | 270 | 21 % | +406 | +1.50 | -729 | -2.1 | -329 / -128 / -272 | -187 | 163 | robustly worse |
| ... + close beyond HTF EMA20 | 266 | 22 % | +424 | +1.59 | -711 | -2.1 | -315 / -120 / -276 | -187 | 148 | robustly worse |
| Skip same-direction setup while running Off | 690 | 24 % | +1106 | +1.60 | -29 | -0.2 | -13 / -12 / -4 | -4 | 103 | worse |
| Min candles between setups 5 | 650 | 22 % | +1155 | +1.78 | +20 | +0.3 | -10 / +15 / +15 | +0 | 127 | noise |
| Min candles between setups 8 | 637 | 22 % | +1150 | +1.81 | +15 | +0.3 | -1 / +15 / +0 | +0 | 121 | noise |
| Min candles between setups 12 | 630 | 22 % | +1143 | +1.81 | +7 | +0.2 | +7 / +0 / -0 | +0 | 121 | noise |
| Min candles between setups 15 | 624 | 22 % | +1065 | +1.71 | -70 | -1.0 | -61 / +0 / -10 | +0 | 121 | worse |
| Min candles between setups 20 | 604 | 22 % | +1078 | +1.78 | -57 | -0.6 | -23 / -14 / -21 | +2 | 121 | worse |
| ATR length 10 | 621 | 22 % | +1101 | +1.77 | -34 | -0.2 | +15 / +23 / -72 | -67 | 118 | worse |
| ATR length 15 (your chart) | 633 | 22 % | +1137 | +1.80 | +1 | +0.0 | -0 / -8 / +10 | +13 | 122 | noise |
| ATR length 20 | 638 | 21 % | +1068 | +1.67 | -67 | -0.4 | -49 / -14 / -4 | +2 | 123 | worse |
| End setups at 16:00 Off | 634 | 22 % | +1120 | +1.77 | -15 | -0.3 | -7 / -8 / -0 | +0 | 121 | worse |

# Neighbour check (python3 ats_inputs_study.py nb)

### MES 3m -- branch base: 1000 setups, win 49 %, net +350, avg +0.35, thirds +235 / -232 / +347, last 4 wk +164, max DD 296
| Min ER LTF EMA20 Pierce 0.10 | 944 | 49 % | +414 | +0.44 | +63 | +0.8 | +37 / -1 / +28 | -1 | 309 | noise |
| Min ER LTF EMA20 Pierce 0.12 | 906 | 49 % | +477 | +0.53 | +127 | +1.3 | +84 / +26 / +17 | -14 | 275 | promising |
| Min ER LTF EMA20 Pierce 0.14 | 859 | 49 % | +534 | +0.62 | +184 | +1.5 | +72 / +52 / +60 | +23 | 271 | promising |
| Min ER LTF EMA20 Pierce 0.15 | 836 | 49 % | +533 | +0.64 | +183 | +1.4 | +73 / +74 / +37 | +10 | 252 | promising |
| Min ER LTF EMA20 Pierce 0.16 | 825 | 49 % | +498 | +0.60 | +147 | +1.1 | +56 / +62 / +30 | +10 | 263 | promising |
| Min ER LTF EMA20 Pierce 0.18 | 793 | 49 % | +481 | +0.61 | +131 | +0.9 | +42 / +33 / +56 | +4 | 285 | noise |
| Min ER LTF EMA20 Pierce 0.20 | 766 | 50 % | +551 | +0.72 | +201 | +1.3 | +12 / +57 / +131 | +56 | 264 | promising |
| Min ER LTF EMA20 Pierce 0.23 | 729 | 50 % | +575 | +0.79 | +225 | +1.3 | +25 / +60 / +140 | +48 | 248 | promising |
| End 16:00 Off + Min ER LTF 0.15 | 836 | 50 % | +599 | +0.72 | +249 | +1.8 | +94 / +97 / +58 | +17 | 241 | promising |
| ATR 15 + Min ER LTF 0.15 | 827 | 49 % | +468 | +0.57 | +118 | +0.5 | +64 / +64 / -10 | +7 | 254 | noise |
| ATR 15 + End 16:00 Off | 990 | 48 % | +325 | +0.33 | -25 | -0.1 | +9 / +3 / -37 | -3 | 303 | worse |
### MGC 3m -- branch base: 634 setups, win 22 %, net +1135, avg +1.79, thirds +545 / +78 / +512, last 4 wk +279, max DD 121
| Min ER LTF EMA20 Pierce 0.10 | 616 | 22 % | +1067 | +1.73 | -68 | -0.8 | -55 / +8 / -21 | -12 | 117 | worse |
| Min ER LTF EMA20 Pierce 0.12 | 591 | 23 % | +1085 | +1.84 | -50 | -0.4 | -40 / -9 / -2 | -12 | 136 | worse |
| Min ER LTF EMA20 Pierce 0.14 | 570 | 24 % | +1088 | +1.91 | -47 | -0.3 | -31 / -34 / +18 | +2 | 139 | worse |
| Min ER LTF EMA20 Pierce 0.15 | 561 | 23 % | +1046 | +1.86 | -89 | -0.5 | -39 / -66 / +15 | +7 | 139 | worse |
| Min ER LTF EMA20 Pierce 0.16 | 547 | 23 % | +1032 | +1.89 | -104 | -0.6 | -56 / -78 / +30 | +7 | 148 | worse |
| Min ER LTF EMA20 Pierce 0.18 | 528 | 23 % | +860 | +1.63 | -276 | -1.3 | -122 / -81 / -73 | -75 | 173 | worse |
| Min ER LTF EMA20 Pierce 0.20 | 508 | 23 % | +859 | +1.69 | -277 | -1.2 | -119 / -99 / -59 | -76 | 182 | worse |
| Min ER LTF EMA20 Pierce 0.23 | 480 | 23 % | +727 | +1.51 | -408 | -1.6 | -251 / -86 / -71 | -82 | 180 | worse |
| End 16:00 Off + Min ER LTF 0.15 | 561 | 23 % | +1044 | +1.86 | -92 | -0.5 | -33 / -74 / +15 | +7 | 147 | worse |
| ATR 15 + Min ER LTF 0.15 | 562 | 23 % | +1055 | +1.88 | -81 | -0.4 | -39 / -60 / +18 | +13 | 137 | worse |
| ATR 15 + End 16:00 Off | 633 | 21 % | +1121 | +1.77 | -14 | -0.1 | -7 / -16 / +9 | +13 | 122 | worse |

# Verdict 11/14/2026

- MES 3m "Minimum ER: LTF EMA20 Pierce" 0.08 -> 0.15: promising (+183, z 1.4, thirds +73 / +74 / +37, last 4 wk +10, max DD 252 vs 296). Plateau: 0.12-0.23 all promising, 0.14 +184 (z 1.5), 0.23 +225 (z 1.3). It only acts on LTF pierces let through by the breakout exception (the per-trigger minimum is not lifted by it). MGC 3m: every value above 0.08 is worse -> MES 3m chart instance only (global input; per-symbol list would need a Pine change).
- MES 3m "End setups at 16:00" OFF: promising (+52, z 1.3, all thirds); with ER 0.15 together +249, z 1.8 (+94 / +97 / +58). Only the exit is modelled (no setups 16:00-18:30 either way); the bot flattens at 15:57 regardless. MGC 3m: worse (-15).
- ATR length: the user's chart shows 15, the code default and every replay use 14. MES 3m 15 = -77 (thirds -9 / -10 / -58, last 4 wk -11); MGC 3m 15 = +1 (noise). Suggest 14 on MES 3m.
- Everything else noise or worse. Robustly worse (confirms current): MES MTF 60m gate (-203); MGC flip distance 3 ATR / off (-301 / -309); MGC "price past both EMA clouds" (-745). Inert in the replay (no setup changed): flip side gate 0 / 2 pts, MES flip VWAP slope off, flip EMA200 slope on.
