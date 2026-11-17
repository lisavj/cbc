③ Trade Setup Filters vs current -- MES 3m and MGC 3m, CBC v10.97 -- 11/14/2026.
One change at a time on top of each chart's live settings: ER chop 0.23 + breakout exception 3 bars ON; range gate 24 bars / 20 % / 5 ATR
(MES 3m, MGC 3m); VWAP stretch 4 ATR (MGC 3m); everything else OFF. Replay Jan 5 -> now, CBC engine setups (late_study / combo_study), live exits
(MES 3m SL1 3 ATR min 5, TP1 1.75, 100 % at TP1; MGC 3m SL1 1.7 ATR min 5 cap 7, TP1 1.7 cap 6, 0 % at TP1 + BE, closed by the HTF flip).
Chop measures use the 12-bar "Chop filters length": Choppiness Index(12), ADX(12), candles in the last 12 whose close crossed EMA20 or VWAP, |HTF EMA20 now - 12 bars ago| / ATR
(as the Pine tooltip), 12-bar high-low range / ATR. Net after costs (MES 0.50, MGC 0.22). Entry filters: a skipped setup can change later setups.
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, better in all three thirds and last 4 wk >= 0; promising = z >= 1 and all thirds.
Note: the combo_study engine never applied the MGC VWAP stretch gate to its main setups (X4 always False in mes3_ema_grid gen),
so earlier MGC 3m replays (cbce, volflip, tp1flip: 1602 setups) ran without it; here it is applied (current = 1136 setups).
Not modelled: mixed chart structure, skip-the-breakout-candle, room to the first opposing level / OB (see room_study), the 2m-only lists.

## Candidates (promising or better)

- MES 3m: ER threshold 0.30 → +137, z +1.2, thirds +23 / +92 / +21, last 4 wk +6, avg -0.40 vs -0.45 (promising)
- MES 3m: ADX < 20 block → +264, z +1.5, thirds +40 / +153 / +72, last 4 wk +28, avg -0.44 vs -0.45 (promising)
- MES 3m: EMA20 / VWAP crosses >= 6 block → +133, z +2.3, thirds +44 / +60 / +29, last 4 wk +0, avg -0.38 vs -0.45 (robust)
- MES 3m: HTF EMA20 slope < 0.2 ATR block → +498, z +3.2, thirds +148 / +211 / +140, last 4 wk +6, avg -0.21 vs -0.45 (robust)
- MES 3m: HTF EMA20 slope < 0.3 ATR block (default value) → +694, z +3.7, thirds +242 / +281 / +171, last 4 wk +16, avg -0.09 vs -0.45 (robust)
- MES 3m: HTF EMA20 slope < 0.5 ATR block → +818, z +3.5, thirds +121 / +500 / +197, last 4 wk -0, avg +0.02 vs -0.45 (robust except last 4 wk)
- MES 3m: HTF EMA20 slope < 0.8 ATR block → +779, z +2.9, thirds +69 / +599 / +111, last 4 wk -33, avg -0.05 vs -0.45 (robust except last 4 wk)
- MES 3m: Environment: EMA200 vs VWAP (v10.97) → +560, z +2.5, thirds +88 / +440 / +31, last 4 wk -20, avg -0.28 vs -0.45 (robust except last 4 wk)
- MGC 3m: HTF EMA20 slope < 0.2 ATR block → +393, z +1.2, thirds +219 / +29 / +145, last 4 wk +20, avg +1.27 vs +0.54 (promising)
- MGC 3m: HTF EMA20 slope < 0.3 ATR block (default value) → +520, z +1.4, thirds +217 / +89 / +215, last 4 wk +16, avg +1.79 vs +0.54 (promising)
- MGC 3m: HTF EMA20 slope < 0.5 ATR block → +474, z +1.1, thirds +261 / +84 / +128, last 4 wk -56, avg +3.12 vs +0.54 (promising)

## MES 3m -- current: 1799 setups, win 48 %, net -801, avg -0.45, thirds -2 / -712 / -87, last 4 wk +99

| Change (one at a time) | Setups | Win % | Net | Avg/setup | Δ vs current | z | Δ by third | Δ last 4 wk | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| ER filter OFF | 2231 | 49 % | -1075 | -0.48 | -274 | -1.3 | -179 / -63 / -32 | +45 | worse |
| ER threshold 0.18 | 1915 | 48 % | -900 | -0.47 | -100 | -0.9 | -70 / +18 / -47 | -4 | worse |
| ER threshold 0.20 | 1875 | 48 % | -887 | -0.47 | -86 | -1.0 | -69 / +20 / -37 | -3 | worse |
| ER threshold 0.26 | 1726 | 48 % | -750 | -0.43 | +50 | +0.6 | -6 / +25 / +31 | +37 | noise |
| ER threshold 0.30 | 1651 | 48 % | -664 | -0.40 | +137 | +1.2 | +23 / +92 / +21 | +6 | promising |
| ER breakout exception OFF | 1272 | 49 % | -771 | -0.61 | +30 | +0.2 | -126 / +76 / +80 | +6 | noise |
| Choppiness Index > 61.8 block | 1672 | 48 % | -742 | -0.44 | +58 | +0.6 | -47 / +56 / +50 | +47 | noise |
| Choppiness Index > 58 block | 1520 | 48 % | -737 | -0.48 | +64 | +0.5 | -14 / +61 / +17 | +30 | noise |
| ADX < 20 block | 1231 | 47 % | -537 | -0.44 | +264 | +1.5 | +40 / +153 / +72 | +28 | promising |
| ADX < 15 block | 1646 | 48 % | -789 | -0.48 | +12 | +0.1 | -5 / +31 / -14 | -1 | noise |
| EMA20 / VWAP crosses >= 4 block | 1561 | 48 % | -605 | -0.39 | +196 | +1.5 | +30 / +202 / -36 | -34 | noise |
| EMA20 / VWAP crosses >= 6 block | 1768 | 48 % | -668 | -0.38 | +133 | +2.3 | +44 / +60 / +29 | +0 | robust |
| HTF EMA20 slope < 0.2 ATR block | 1445 | 49 % | -302 | -0.21 | +498 | +3.2 | +148 / +211 / +140 | +6 | robust |
| HTF EMA20 slope < 0.3 ATR block (default value) | 1242 | 50 % | -107 | -0.09 | +694 | +3.7 | +242 / +281 / +171 | +16 | robust |
| HTF EMA20 slope < 0.5 ATR block | 876 | 51 % | +18 | +0.02 | +818 | +3.5 | +121 / +500 / +197 | -0 | robust except last 4 wk |
| HTF EMA20 slope < 0.8 ATR block | 435 | 50 % | -22 | -0.05 | +779 | +2.9 | +69 / +599 / +111 | -33 | robust except last 4 wk |
| N-bar range < 2 ATR block | 1776 | 48 % | -829 | -0.47 | -28 | -0.7 | -38 / +2 / +7 | +0 | worse |
| N-bar range < 3 ATR block | 1303 | 47 % | -796 | -0.61 | +5 | +0.0 | -92 / +105 / -9 | +24 | noise |
| VWAP stretch 3 ATR | 1094 | 47 % | -454 | -0.42 | +346 | +1.7 | -40 / +355 / +31 | +14 | noise |
| VWAP stretch 4 ATR | 1320 | 48 % | -663 | -0.50 | +137 | +0.8 | -83 / +174 / +45 | +1 | noise |
| VWAP stretch 6 ATR | 1564 | 48 % | -763 | -0.49 | +38 | +0.3 | -41 / +32 / +47 | -1 | noise |
| Range gate OFF | 2091 | 49 % | -911 | -0.44 | -110 | -0.6 | +59 / -75 / -94 | +40 | worse |
| Range gate 4 ATR | 1955 | 49 % | -958 | -0.49 | -157 | -1.2 | -27 / -95 / -36 | +45 | worse |
| Range gate 6 ATR | 1731 | 47 % | -734 | -0.42 | +67 | +0.8 | +30 / +70 / -33 | -14 | noise |
| Block after HTF flips >= 2 in 8 | 708 | 45 % | -416 | -0.59 | +385 | +1.6 | -59 / +468 / -24 | -55 | noise |
| Block after HTF flips >= 3 in 8 | 1485 | 48 % | -561 | -0.38 | +240 | +1.7 | +43 / +215 / -19 | -17 | noise |
| Block after HTF flips >= 4 in 8 | 1739 | 48 % | -833 | -0.48 | -32 | -0.5 | +18 / -29 / -21 | +1 | worse |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 1564 | 48 % | -679 | -0.43 | +122 | +1.0 | -101 / +100 / +123 | +26 | noise |
| Block if EMA200 -3 / +2 pts | 1577 | 48 % | -693 | -0.44 | +108 | +0.9 | -41 / +63 / +85 | -23 | noise |
| Environment: EMA200 vs VWAP (v10.97) | 856 | 47 % | -241 | -0.28 | +560 | +2.5 | +88 / +440 / +31 | -20 | robust except last 4 wk |
| Skip if Max ATR SL1 cap < 1.5 x ATR | — | | | | | | | | | n/a (no cap on MES 3m) |
| Skip while ATR > 1.8 x ATR(100) | 1734 | 48 % | -888 | -0.51 | -87 | -1.4 | -119 / +82 / -50 | -68 | worse |

## MGC 3m -- current: 1136 setups, win 18 %, net +615, avg +0.54, thirds +329 / -10 / +297, last 4 wk +262

| Change (one at a time) | Setups | Win % | Net | Avg/setup | Δ vs current | z | Δ by third | Δ last 4 wk | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| ER filter OFF | 1386 | 18 % | +321 | +0.23 | -294 | -0.9 | -231 / +129 / -193 | -47 | worse |
| ER threshold 0.18 | 1221 | 18 % | +557 | +0.46 | -58 | -0.3 | -51 / +61 / -68 | -30 | worse |
| ER threshold 0.20 | 1195 | 18 % | +543 | +0.45 | -72 | -0.5 | -54 / +23 / -40 | -7 | worse |
| ER threshold 0.26 | 1107 | 19 % | +686 | +0.62 | +71 | +0.6 | +74 / +0 / -3 | +5 | noise |
| ER threshold 0.30 | 1065 | 19 % | +779 | +0.73 | +164 | +0.9 | +139 / +19 / +6 | -18 | noise |
| ER breakout exception OFF | 821 | 18 % | +301 | +0.37 | -314 | -1.0 | -139 / -94 / -81 | -91 | worse |
| Choppiness Index > 61.8 block | 1086 | 18 % | +531 | +0.49 | -84 | -0.6 | +21 / -5 / -100 | -70 | worse |
| Choppiness Index > 58 block | 1011 | 18 % | +439 | +0.43 | -176 | -0.9 | -60 / +38 / -154 | -76 | worse |
| ADX < 20 block | 773 | 17 % | +407 | +0.53 | -208 | -0.7 | -43 / -52 / -114 | -138 | worse |
| ADX < 15 block | 1065 | 19 % | +717 | +0.67 | +102 | +0.7 | -5 / +35 / +71 | +20 | noise |
| EMA20 / VWAP crosses >= 4 block | 974 | 20 % | +804 | +0.83 | +189 | +0.8 | +199 / -2 / -8 | -19 | noise |
| EMA20 / VWAP crosses >= 6 block | 1114 | 19 % | +630 | +0.57 | +15 | +0.1 | +15 / +9 / -9 | +8 | noise |
| HTF EMA20 slope < 0.2 ATR block | 795 | 20 % | +1008 | +1.27 | +393 | +1.2 | +219 / +29 / +145 | +20 | promising |
| HTF EMA20 slope < 0.3 ATR block (default value) | 634 | 22 % | +1135 | +1.79 | +520 | +1.4 | +217 / +89 / +215 | +16 | promising |
| HTF EMA20 slope < 0.5 ATR block | 349 | 25 % | +1089 | +3.12 | +474 | +1.1 | +261 / +84 / +128 | -56 | promising |
| HTF EMA20 slope < 0.8 ATR block | 135 | 24 % | +761 | +5.64 | +146 | +0.3 | +207 / +43 / -104 | -251 | noise |
| N-bar range < 2 ATR block | 1128 | 18 % | +558 | +0.49 | -57 | -1.3 | -14 / +5 / -48 | -48 | worse |
| N-bar range < 3 ATR block | 877 | 19 % | +441 | +0.50 | -174 | -0.7 | -84 / +46 / -136 | -87 | worse |
| VWAP stretch 3 ATR | 964 | 18 % | +709 | +0.73 | +94 | +0.4 | +108 / -81 / +67 | -0 | noise |
| VWAP stretch 6 ATR | 1376 | 18 % | +317 | +0.23 | -298 | -1.2 | -156 / -104 / -37 | +32 | worse |
| VWAP stretch OFF | 1628 | 18 % | +517 | +0.32 | -98 | -0.3 | -98 / -83 / +83 | +49 | worse |
| Range gate OFF | 1282 | 19 % | +606 | +0.47 | -9 | -0.0 | +121 / -54 / -76 | -83 | worse |
| Range gate 4 ATR | 1222 | 19 % | +729 | +0.60 | +114 | +0.6 | +129 / +65 / -80 | -107 | noise |
| Range gate 6 ATR | 1086 | 19 % | +604 | +0.56 | -11 | -0.1 | +48 / +4 / -62 | -45 | worse |
| Block after HTF flips >= 2 in 8 | 373 | 22 % | -14 | -0.04 | -629 | -1.5 | -421 / +56 / -265 | -260 | worse |
| Block after HTF flips >= 3 in 8 | 868 | 20 % | +329 | +0.38 | -286 | -1.0 | -149 / -43 / -94 | -135 | worse |
| Block after HTF flips >= 4 in 8 | 1082 | 19 % | +643 | +0.59 | +28 | +0.2 | +24 / -0 / +4 | -15 | noise |
| Block if VWAP -3 / +2 pts (unless candle 1 pt beyond) | 987 | 19 % | +772 | +0.78 | +157 | +0.7 | +91 / +31 / +36 | +11 | noise |
| Block if EMA200 -3 / +2 pts | 984 | 19 % | +709 | +0.72 | +94 | +0.4 | -40 / +62 / +72 | -6 | noise |
| Environment: EMA200 vs VWAP (v10.97) | 488 | 19 % | +197 | +0.40 | -418 | -1.1 | -213 / +66 / -271 | -257 | worse |
| Skip if Max ATR SL1 cap < 1.5 x ATR | 720 | 19 % | +300 | +0.42 | -314 | -1.0 | -162 / -71 / -82 | -145 | worse |
| Skip while ATR > 1.8 x ATR(100) | 1103 | 19 % | +657 | +0.60 | +42 | +0.5 | +31 / -15 / +27 | +6 | noise |
