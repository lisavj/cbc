# ①②③ full input sweep -- 5m charts on v1.11 settings -- 11/14/2026

Replay Jan 5 -> Nov 13, one change at a time, net after costs. Completes the ①②③ coverage on 5m (3m was already complete: ats_inputs, trig_inputs, time_blocks, all_report). Neighbour checks at the end.

## Verdict

Plateau candidates (neighbours agree):

- MNQ 5m: VWAP stretch gate 7 ATR (MNQ has none today) -> +606, z +2.2, thirds +59 / +227 / +319, last 4 wk +4, max DD 777 vs 891 (robust). 6 and 8 ATR also better in all thirds.
- MGC 5m: Max SL1 cap 7 -> 10 -> +160, z +1.9, thirds +109 / +11 / +40, last 4 wk +1, max DD 94 vs 118. Caps 12/15/20/OFF all +154 to +191 (plateau); 10 has the lowest DD.

Isolated peaks, not recommended: MES ATR 10 (8 and 12 mixed thirds), MGC stretch 6 (5 worse, 7 noise), skip non-flip from 12 on MGC/MNQ (10 and 15 noise), MNQ VWAP reclaim block 8 (6/12 noise), M2K HTF pierce ER 0 / TP1 0 % / ADX 15 (neighbours noise). MES No new setups 16:00-19:00 promising again (+27, z 1.7) -- same open item as 3m.

Flip side gate OFF (errored in the first pass) rerun: noise on all four charts.

## MES 5m (v1.11)

Base: 228 trades, net +248, avg +1.09, thirds +54 / +99 / +96, last 4 wk +17, max DD 46

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ③ CHOP > 61.8 block | 207 | +173 | -76 | -2.7 | -33 / -16 / -27 | -15 | 42 | robustly worse |
| ③ CHOP > 58 block | 177 | +166 | -82 | -1.9 | -26 / -3 / -53 | -20 | 28 | worse |
| ③ ADX < 20 block | 161 | +211 | -37 | -0.8 | -22 / +3 / -18 | +1 | 34 | worse |
| ③ ADX < 15 block | 208 | +229 | -19 | -0.7 | -14 / +16 / -21 | +0 | 46 | worse |
| ③ EMA20/VWAP crosses >= 4 block | 198 | +209 | -39 | -1.1 | +2 / -33 / -9 | +1 | 53 | worse |
| ③ crosses >= 6 block | 222 | +233 | -16 | -1.2 | -17 / +7 / -5 | +0 | 47 | worse |
| ③ N-bar range < 2 ATR block | 224 | +244 | -5 | -0.4 | -5 / +4 / -3 | -5 | 46 | worse |
| ③ N-bar range < 3 ATR block | 129 | +61 | -187 | -3.4 | -69 / -32 / -86 | -33 | 34 | robustly worse |
| ③ HTF flips >= 2 in 8 block | 121 | +193 | -56 | -0.9 | -21 / -16 / -18 | -4 | 22 | worse |
| ③ HTF flips >= 3 in 8 block | 210 | +219 | -30 | -1.2 | -10 / +3 / -23 | -11 | 37 | worse |
| ③ HTF flips >= 4 in 8 block | 223 | +231 | -18 | -1.2 | -5 / -6 / -6 | -6 | 46 | worse |
| ③ Skip non-flip setups from 6 HTF candles after flip | 146 | +106 | -142 | -2.9 | +1 / -65 / -79 | -22 | 46 | worse |
| ③ ... from 9 | 184 | +156 | -92 | -2.6 | -37 / -22 / -34 | -17 | 48 | robustly worse |
| ③ ... from 12 | 202 | +200 | -49 | -1.8 | -27 / -2 / -20 | +2 | 47 | worse |
| ③ Block if VWAP -3 / +2 pts | 203 | +232 | -16 | -0.5 | +15 / -19 / -13 | +5 | 48 | worse |
| ③ Block if EMA200 -3 / +2 pts | 222 | +247 | -1 | -0.1 | +7 / -6 / -3 | +0 | 46 | worse |
| ③ Environment EMA200 vs VWAP | 29 | +43 | -205 | -2.7 | -65 / -59 / -81 | -13 | 16 | robustly worse |
| ③ Skip while ATR > 1.8 x ATR(100) | 214 | +211 | -37 | -1.8 | -9 / -12 / -17 | +0 | 55 | worse |
| ③ Skip if SL1 cap < 1.5 ATR | 157 | +143 | -106 | -2.3 | -43 / -32 / -31 | +1 | 30 | robustly worse |
| ③ ER 0.18 | 238 | +258 | +10 | +0.5 | +8 / +3 / -1 | -3 | 46 | noise |
| ③ ER 0.20 | 232 | +256 | +8 | +0.4 | +4 / +0 / +4 | +0 | 46 | noise |
| ③ ER 0.26 | 221 | +256 | +8 | +0.4 | +2 / +9 / -3 | +0 | 33 | noise |
| ③ ER 0.30 | 206 | +230 | -18 | -0.7 | -5 / -6 / -8 | +0 | 33 | worse |
| ③ ER filter OFF | 274 | +303 | +54 | +1.2 | +68 / +11 / -25 | -1 | 53 | noise |
| ③ ER breakout exception OFF | 142 | +90 | -159 | -3.0 | -33 / -58 / -68 | -23 | 46 | robustly worse |
| ③ Range gate 4 ATR | 213 | +260 | +12 | +0.5 | +10 / +5 / -3 | -5 | 37 | noise |
| ③ Range gate 6 ATR | 197 | +267 | +19 | +0.5 | +30 / -6 / -5 | -17 | 38 | noise |
| ③ Range gate zone 30 % | 176 | +195 | -54 | -1.2 | -6 / -24 / -23 | -2 | 35 | worse |
| ③ Range gate ON 5 ATR | 201 | +250 | +2 | +0.1 | +26 / -14 / -10 | -17 | 38 | noise |
| ③ VWAP stretch 3 ATR | 172 | +176 | -72 | -1.7 | -28 / -52 / +8 | +9 | 38 | worse |
| ③ VWAP stretch 6 ATR | 311 | +172 | -76 | -1.5 | -55 / +11 / -32 | -15 | 55 | worse |
| ③ VWAP stretch OFF | 400 | +66 | -182 | -2.5 | -89 / -23 / -71 | -19 | 118 | robustly worse |
| ① Flip min ER 0.15 | 230 | +237 | -12 | -1.1 | +0 / -12 / +0 | +0 | 49 | worse |
| ① Flip min ER 0.30 | 222 | +220 | -29 | -1.9 | -19 / -10 / +0 | +0 | 46 | worse |
| ① Toward late-away 1 pt (instead of strict) | 228 | +248 | +0 | +0.0 | +0 / +0 / +0 | +0 | 46 | noise |
| ① SL1 x 1.5 ATR | 228 | +215 | -33 | -1.4 | +2 / -35 / -1 | +2 | 59 | worse |
| ① SL1 x 2.0 | 228 | +253 | +5 | +0.2 | +10 / -1 / -4 | -1 | 47 | noise |
| ① SL1 x 2.5 | 228 | +258 | +10 | +0.4 | +12 / -0 / -2 | -3 | 50 | noise |
| ① SL1 x 3.0 | 226 | +257 | +8 | +0.3 | +14 / -1 / -5 | -5 | 50 | noise |
| ① SL1 x 3.5 | 226 | +255 | +6 | +0.2 | +12 / -1 / -6 | -5 | 50 | noise |
| ① TP1 x 1.25 ATR | 230 | +251 | +2 | +0.0 | -0 / -7 / +10 | -4 | 48 | noise |
| ① TP1 x 1.5 | 228 | +255 | +7 | +0.1 | +3 / -10 / +14 | +2 | 47 | noise |
| ① TP1 x 1.75 | 228 | +248 | -1 | -0.0 | +2 / -5 / +2 | +0 | 46 | worse |
| ① TP1 x 2.0 | 227 | +257 | +9 | +0.2 | +2 / +1 / +6 | +0 | 47 | noise |
| ① TP1 x 2.5 | 226 | +273 | +25 | +0.6 | +11 / -2 / +15 | +0 | 55 | noise |
| ① Close at TP1 0 % | 228 | +305 | +56 | +0.9 | +77 / +13 / -33 | +3 | 59 | noise |
| ① Close at TP1 50 % | 228 | +270 | +21 | +0.3 | +29 / +5 / -13 | +1 | 51 | noise |
| ① Close at TP1 80 % | 228 | +248 | +0 | +0.0 | +0 / +0 / +0 | +0 | 46 | noise |
| ① Close at TP1 100 % | 237 | +259 | +10 | +0.2 | -15 / +0 / +26 | -2 | 44 | noise |
| ① Breakeven at TP1 OFF | 225 | +243 | -6 | -0.1 | -0 / -4 / -1 | +3 | 47 | worse |
| ① Trail 1.3 ATR | 233 | +254 | +6 | +0.1 | -6 / +2 / +10 | -4 | 47 | noise |
| ① Trail 1.7 ATR | 228 | +248 | +0 | +0.0 | +0 / +0 / +0 | +0 | 46 | noise |
| ① Trail 2.5 ATR | 224 | +239 | -9 | -0.2 | -3 / -11 / +5 | +2 | 46 | worse |
| ① Trail 3.5 ATR | 224 | +229 | -19 | -0.4 | -8 / -17 / +6 | +5 | 47 | worse |
| ① No trail | 224 | +229 | -20 | -0.4 | -9 / -17 / +6 | +5 | 47 | worse |
| ① Min SL x 0.6 | 228 | +252 | +3 | +0.1 | +5 / +4 / -6 | +1 | 45 | noise |
| ① Min SL x 1.4 | 226 | +250 | +1 | +0.0 | +1 / +1 / -1 | -4 | 49 | noise |
| ① Max SL1 cap OFF | 228 | +285 | +37 | +1.5 | +13 / +39 / -15 | -8 | 36 | noise |
| ① Max TP1 cap OFF | 226 | +239 | -10 | -0.2 | -18 / +12 / -4 | -5 | 85 | worse |
| ① Time stop 10 candles (< 0.5 ATR progress) | 228 | +250 | +1 | +0.1 | +0 / +1 / +0 | +0 | 45 | noise |
| ① Time stop 20 candles | 228 | +248 | +0 | +0.0 | +0 / +0 / +0 | +0 | 46 | noise |
| ① Flip ride ON | 228 | +246 | -3 | -0.1 | -2 / -10 / +9 | +5 | 46 | worse |
| ② LTF pierce late window 0 | 202 | +186 | -62 | -2.2 | -15 / -15 / -32 | -14 | 44 | robustly worse |
| ② LTF pierce late window 2 | 233 | +227 | -22 | -1.5 | +0 / -30 / +8 | +5 | 59 | worse |
| ② HTF pierce late window 0 | 226 | +240 | -8 | -1.1 | +0 / +0 / -8 | +0 | 46 | worse |
| ② HTF pierce late window 2 | 229 | +240 | -8 | -1.6 | +0 / -8 / +0 | +0 | 46 | worse |
| ② HTF late trade-colour OFF | 228 | +248 | +0 | +0.0 | +0 / +0 / +0 | +0 | 46 | noise |
| ② HTF pierce replaces current setup | 228 | +248 | +0 | +0.0 | +0 / +0 / +0 | +0 | 46 | noise |
| ② HTF pierce requires close beyond LTF EMA9/20 | 228 | +248 | +0 | +0.0 | +0 / +0 / +0 | +0 | 46 | noise |
| ② Flip: require pullback first (wait 10) | 228 | +248 | +0 | +0.0 | +0 / +0 / +0 | +0 | 46 | noise |
| ② Trigger HTF CBC Flip OFF | 210 | +216 | -32 | -1.1 | -16 / -9 / -7 | -7 | 41 | worse |
| ② Trigger LTF EMA20 Pierce OFF | 93 | +97 | -152 | -2.3 | -20 / -87 / -44 | -15 | 30 | robustly worse |
| ② Trigger HTF EMA9 Pierce OFF | 188 | +218 | -31 | -0.8 | -7 / -12 / -11 | +4 | 48 | worse |
| ② Trigger HTF EMA20 Pierce OFF | 225 | +248 | -0 | -0.0 | +0 / +8 / -9 | +0 | 46 | worse |
| ① Flip distance 1.5 ATR | 225 | +245 | -3 | -0.3 | +4 / +0 / -7 | -7 | 46 | worse |
| ① Flip distance 3 ATR | 230 | +257 | +9 | +1.1 | +4 / +0 / +4 | +0 | 46 | noise |
| ① Flip side gate 2 pts | 228 | +248 | +0 | +0.0 | +0 / +0 / +0 | +0 | 46 | noise |
| ① Flip VWAP slope OFF | 228 | +248 | +0 | +0.0 | +0 / +0 / +0 | +0 | 46 | noise |
| ① HTF pierce min ER 0 | 273 | +285 | +36 | +0.9 | +23 / +9 / +4 | -2 | 43 | noise |
| ① HTF pierce min ER 0.23 | 218 | +256 | +8 | +0.3 | +6 / +14 / -12 | +0 | 46 | noise |
| ① LTF pierce min ER 0.12 | 208 | +162 | -86 | -3.3 | -32 / -40 / -13 | -1 | 55 | robustly worse |
| ① LTF pierce min ER 0.15 | 189 | +120 | -128 | -3.6 | -34 / -59 / -35 | -4 | 46 | robustly worse |
| ① LTF pierce min ER 0.23 | 159 | +102 | -147 | -3.1 | -30 / -69 / -47 | -23 | 47 | robustly worse |
| ① VWAP reclaim block OFF | 243 | +268 | +20 | +0.9 | +7 / +1 / +13 | +6 | 51 | noise |
| ① VWAP reclaim block 8 | 226 | +234 | -14 | -1.1 | -4 / -10 / +0 | +0 | 46 | worse |
| ① Min candles between setups 5 | 230 | +259 | +11 | +1.4 | +0 / +6 / +5 | +0 | 46 | noise |
| ① Min candles 15 | 224 | +239 | -10 | -0.9 | +6 / -11 / -4 | +0 | 51 | worse |
| ① ATR length 10 | 235 | +312 | +64 | +1.0 | +2 / +19 / +43 | +11 | 45 | promising |
| ① ATR length 20 | 232 | +247 | -1 | -0.0 | +6 / -15 / +8 | +9 | 45 | worse |
| ① No new setups 16:00-19:00 | 219 | +276 | +27 | +1.7 | +16 / +4 / +7 | +5 | 42 | promising |
| ① No-new-setup window OFF | 258 | +248 | -0 | -0.0 | +38 / -24 / -15 | -15 | 40 | worse |
| ① OR forming blocks all OFF | 250 | +255 | +6 | +0.2 | -15 / +1 / +20 | -2 | 48 | noise |
| ① End setups at 16:00 OFF | 228 | +243 | -5 | -1.0 | +0 / +0 / -5 | +0 | 46 | worse |

## MGC 5m (v1.11)

Base: 628 trades, net +512, avg +0.82, thirds +90 / +224 / +199, last 4 wk +11, max DD 118

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ③ CHOP > 61.8 block | 564 | +496 | -16 | -0.3 | -26 / -19 / +29 | +1 | 124 | worse |
| ③ CHOP > 58 block | 507 | +460 | -53 | -0.6 | -13 / -30 / -10 | +18 | 108 | worse |
| ③ ADX < 20 block | 478 | +355 | -157 | -1.8 | -38 / -10 / -109 | -23 | 123 | worse |
| ③ ADX < 15 block | 587 | +429 | -83 | -1.7 | -65 / +22 / -40 | -17 | 111 | worse |
| ③ EMA20/VWAP crosses >= 4 block | 557 | +448 | -64 | -1.0 | -75 / +13 / -2 | +25 | 99 | worse |
| ③ crosses >= 6 block | 617 | +501 | -12 | -0.4 | -14 / -9 / +12 | +14 | 118 | worse |
| ③ N-bar range < 2 ATR block | 611 | +483 | -29 | -0.9 | -37 / -3 / +11 | -5 | 118 | worse |
| ③ N-bar range < 3 ATR block | 416 | +273 | -240 | -2.2 | -118 / -50 / -72 | +4 | 112 | robustly worse |
| ③ HTF flips >= 2 in 8 block | 303 | +86 | -426 | -3.5 | -104 / -116 / -206 | +2 | 83 | robustly worse |
| ③ HTF flips >= 3 in 8 block | 552 | +316 | -196 | -3.1 | -77 / -17 / -102 | +0 | 116 | robustly worse |
| ③ HTF flips >= 4 in 8 block | 607 | +509 | -3 | -0.1 | +9 / +3 / -16 | +6 | 115 | worse |
| ③ Skip non-flip setups from 6 HTF candles after flip | 410 | +373 | -139 | -1.5 | -58 / -103 / +22 | -27 | 93 | worse |
| ③ ... from 9 | 499 | +523 | +11 | +0.2 | +39 / -60 / +32 | +3 | 72 | noise |
| ③ ... from 12 | 560 | +595 | +82 | +1.6 | +47 / +6 / +29 | +1 | 89 | promising |
| ③ Block if VWAP -3 / +2 pts | 600 | +455 | -57 | -1.6 | -22 / -11 / -25 | -3 | 110 | worse |
| ③ Block if EMA200 -3 / +2 pts | 622 | +479 | -33 | -1.5 | +0 / -7 / -26 | -3 | 118 | worse |
| ③ Environment EMA200 vs VWAP | 236 | +186 | -326 | -2.6 | -23 / -160 / -143 | -50 | 58 | robustly worse |
| ③ Skip while ATR > 1.8 x ATR(100) | 609 | +493 | -20 | -0.6 | +4 / -5 / -19 | +7 | 118 | worse |
| ③ Skip if SL1 cap < 1.5 ATR | 240 | +282 | -230 | -1.8 | -69 / -87 / -74 | -31 | 58 | worse |
| ③ ER 0.18 | 663 | +540 | +28 | +0.7 | +16 / +20 / -7 | -15 | 112 | noise |
| ③ ER 0.20 | 646 | +505 | -7 | -0.2 | -11 / +10 / -6 | -7 | 119 | worse |
| ③ ER 0.26 | 608 | +539 | +26 | +0.8 | +6 / +25 / -5 | +0 | 90 | noise |
| ③ ER 0.30 | 587 | +443 | -69 | -1.3 | -27 / -2 / -40 | -24 | 96 | worse |
| ③ ER filter OFF | 757 | +564 | +52 | +0.6 | -2 / +14 / +40 | +22 | 141 | noise |
| ③ ER breakout exception OFF | 398 | +265 | -247 | -2.3 | -56 / -130 / -61 | +1 | 119 | robustly worse |
| ③ Range gate 4 ATR | 600 | +497 | -15 | -0.3 | -31 / +19 / -3 | +3 | 118 | worse |
| ③ Range gate 6 ATR | 537 | +384 | -129 | -1.7 | -61 / -28 / -40 | +7 | 109 | worse |
| ③ Range gate zone 30 % | 504 | +414 | -98 | -1.1 | -24 / -51 / -22 | +33 | 88 | worse |
| ③ Range gate ON 5 ATR | 556 | +454 | -58 | -0.9 | -43 / +7 / -23 | +18 | 108 | worse |
| ③ VWAP stretch 3 ATR | 270 | +457 | -56 | -0.4 | -3 / -77 / +24 | +37 | 70 | worse |
| ③ VWAP stretch 6 ATR | 525 | +612 | +100 | +1.5 | +16 / +75 / +9 | +9 | 112 | promising |
| ③ VWAP stretch ON 4 ATR | 387 | +392 | -121 | -1.2 | -26 / -72 / -23 | +3 | 93 | worse |
| ① Flip min ER 0.15 | 642 | +514 | +2 | +0.1 | -24 / +15 / +11 | +7 | 113 | noise |
| ① Flip min ER 0.30 | 614 | +503 | -9 | -0.2 | -11 / +4 / -2 | -21 | 110 | worse |
| ① Toward late-away 1 pt (instead of strict) | 628 | +512 | +0 | +0.0 | +0 / +0 / +0 | +0 | 118 | noise |
| ① SL1 x 1.5 ATR | 628 | +497 | -16 | -0.3 | -8 / -17 / +9 | +1 | 117 | worse |
| ① SL1 x 2.0 | 627 | +505 | -7 | -0.2 | -2 / +3 / -9 | +0 | 118 | worse |
| ① SL1 x 2.5 | 627 | +496 | -16 | -0.4 | -3 / -0 / -12 | -0 | 118 | worse |
| ① SL1 x 3.0 | 627 | +496 | -17 | -0.4 | -4 / -0 / -12 | -0 | 118 | worse |
| ① SL1 x 3.5 | 627 | +496 | -17 | -0.4 | -4 / -0 / -12 | -0 | 118 | worse |
| ① TP1 x 1.25 ATR | 630 | +434 | -78 | -1.0 | -10 / -43 / -25 | +5 | 118 | worse |
| ① TP1 x 1.5 | 628 | +494 | -19 | -0.4 | -2 / -9 / -8 | -4 | 118 | worse |
| ① TP1 x 1.75 | 628 | +516 | +4 | +0.1 | +0 / +1 / +2 | +1 | 118 | noise |
| ① TP1 x 2.0 | 628 | +503 | -9 | -0.3 | +0 / +5 / -14 | -15 | 118 | worse |
| ① TP1 x 2.5 | 628 | +499 | -14 | -0.4 | +0 / +6 / -20 | -24 | 118 | worse |
| ① Close at TP1 0 % | 628 | +789 | +277 | +2.3 | +199 / -45 / +124 | +37 | 111 | noise |
| ① Close at TP1 50 % | 628 | +616 | +104 | +0.9 | +74 / -17 / +46 | +14 | 98 | noise |
| ① Close at TP1 80 % | 628 | +512 | +0 | +0.0 | +0 / +0 / +0 | +0 | 118 | noise |
| ① Close at TP1 100 % | 664 | +405 | -108 | -0.9 | -66 / -13 / -29 | -27 | 134 | worse |
| ① Breakeven at TP1 OFF | 618 | +460 | -52 | -0.6 | -13 / -35 / -4 | -3 | 126 | worse |
| ① Trail 1.3 ATR | 645 | +486 | -26 | -0.3 | -8 / -14 / -5 | -7 | 129 | worse |
| ① Trail 1.7 ATR | 628 | +512 | +0 | +0.0 | +0 / +0 / +0 | +0 | 118 | noise |
| ① Trail 2.5 ATR | 609 | +549 | +36 | +0.4 | -26 / +11 / +51 | +1 | 115 | noise |
| ① Trail 3.5 ATR | 598 | +536 | +24 | +0.3 | -47 / +23 / +48 | +6 | 121 | noise |
| ① No trail | 595 | +556 | +43 | +0.5 | -37 / +25 / +55 | +6 | 120 | noise |
| ① Min SL x 0.6 | 628 | +516 | +3 | +0.2 | +1 / +0 / +2 | +2 | 118 | noise |
| ① Min SL x 1.4 | 627 | +496 | -17 | -0.4 | -4 / -0 / -12 | -0 | 118 | worse |
| ① Max SL1 cap OFF | 623 | +704 | +191 | +2.3 | +136 / +14 / +41 | -4 | 142 | robust except last 4 wk |
| ① Max TP1 cap OFF | 614 | +586 | +73 | +0.6 | +63 / -34 / +45 | +7 | 150 | noise |
| ① Time stop 10 candles (< 0.5 ATR progress) | 630 | +509 | -4 | -0.2 | +6 / -0 / -9 | +0 | 118 | worse |
| ① Time stop 20 candles | 628 | +512 | +0 | +0.0 | +0 / +0 / +0 | +0 | 118 | noise |
| ① Flip ride ON | 628 | +554 | +42 | +0.8 | -9 / +1 / +49 | -27 | 153 | noise |
| ① Flip distance floor 8 pts | 623 | +518 | +6 | +0.3 | +0 / -2 / +7 | +7 | 118 | noise |
| ② LTF pierce late window 0 | 578 | +584 | +72 | +1.3 | +18 / +21 / +33 | +30 | 115 | promising |
| ② LTF pierce late window 2 | 643 | +533 | +21 | +0.7 | -18 / +29 / +9 | +1 | 131 | noise |
| ② HTF pierce late window 0 | 618 | +485 | -28 | -1.3 | +0 / -23 / -5 | +0 | 118 | worse |
| ② HTF pierce late window 2 | 629 | +505 | -7 | -0.7 | -7 / +0 / +0 | +0 | 118 | worse |
| ② HTF late trade-colour OFF | 628 | +512 | +0 | +0.0 | +0 / +0 / +0 | +0 | 118 | noise |
| ② HTF pierce replaces current setup | 648 | +583 | +71 | +2.3 | -6 / +42 / +34 | +6 | 119 | noise |
| ② HTF pierce requires close beyond LTF EMA9/20 | 628 | +512 | +0 | +0.0 | +0 / +0 / +0 | +0 | 118 | noise |
| ② Flip: require pullback first (wait 10) | 628 | +512 | +0 | +0.0 | +0 / +0 / +0 | +0 | 118 | noise |
| ② Trigger HTF CBC Flip OFF | 562 | +414 | -98 | -1.3 | -75 / -11 / -13 | -0 | 108 | worse |
| ② Trigger LTF EMA20 Pierce OFF | 277 | +272 | -240 | -1.8 | -47 / -128 / -65 | +6 | 71 | worse |
| ② Trigger HTF EMA9 Pierce OFF | 557 | +485 | -27 | -0.4 | +40 / -47 / -21 | +2 | 90 | worse |
| ② Trigger HTF EMA20 Pierce OFF | 624 | +500 | -12 | -0.8 | -8 / +1 / -5 | +0 | 118 | worse |
| ① Flip distance 1.5 ATR | 618 | +486 | -26 | -0.9 | -11 / -19 / +4 | +0 | 111 | worse |
| ① Flip distance 3 ATR | 636 | +488 | -24 | -1.0 | -7 / -6 / -11 | -4 | 118 | worse |
| ① Flip side gate 2 pts | 628 | +512 | +0 | +0.0 | +0 / +0 / +0 | +0 | 118 | noise |
| ① Flip VWAP slope OFF | 628 | +512 | +0 | +0.0 | +0 / +0 / +0 | +0 | 118 | noise |
| ① HTF pierce min ER 0 | 719 | +605 | +93 | +1.3 | +22 / +73 / -2 | -21 | 107 | noise |
| ① HTF pierce min ER 0.23 | 598 | +498 | -14 | -0.3 | +7 / +5 / -27 | +7 | 110 | worse |
| ① LTF pierce min ER 0.12 | 583 | +423 | -90 | -1.8 | -64 / +14 / -40 | -11 | 120 | worse |
| ① LTF pierce min ER 0.15 | 543 | +434 | -78 | -1.1 | -72 / +6 / -12 | +4 | 120 | worse |
| ① LTF pierce min ER 0.23 | 455 | +309 | -203 | -2.1 | -52 / -125 / -26 | -6 | 108 | robustly worse |
| ① VWAP reclaim block OFF | 645 | +507 | -6 | -0.2 | +11 / -27 / +11 | +4 | 118 | worse |
| ① VWAP reclaim block 8 | 625 | +542 | +29 | +2.1 | +19 / +10 / +0 | +0 | 106 | noise |
| ① Min candles between setups 5 | 660 | +486 | -26 | -0.6 | -53 / +30 / -3 | -2 | 135 | worse |
| ① Min candles 15 | 605 | +494 | -18 | -0.5 | +3 / -14 / -7 | +7 | 113 | worse |
| ① ATR length 10 | 626 | +525 | +12 | +0.1 | -11 / -1 / +25 | -8 | 111 | noise |
| ① ATR length 20 | 623 | +511 | -1 | -0.0 | -13 / +28 / -16 | -20 | 125 | worse |
| ① No new setups 16:00-19:00 | 623 | +503 | -9 | -0.5 | +0 / -3 / -7 | +4 | 118 | worse |
| ① No-new-setup window OFF | 677 | +490 | -22 | -0.5 | +18 / +2 / -43 | -11 | 131 | worse |
| ① OR forming blocks all OFF | 688 | +534 | +22 | +0.4 | -5 / +39 / -12 | -31 | 101 | noise |
| ① End setups at 16:00 OFF | 628 | +506 | -6 | -0.2 | +17 / -10 / -13 | -2 | 122 | worse |

## MNQ 5m (v1.11)

Base: 1544 trades, net +1428, avg +0.92, thirds +556 / +686 / +186, last 4 wk +487, max DD 891

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ③ CHOP > 61.8 block | 1416 | +1235 | -192 | -0.4 | -116 / -278 / +202 | +141 | 932 | worse |
| ③ CHOP > 58 block | 1282 | +828 | -600 | -1.0 | -321 / -574 / +295 | +123 | 919 | worse |
| ③ ADX < 20 block | 1054 | -71 | -1498 | -2.0 | -108 / -1242 / -148 | -137 | 1595 | worse |
| ③ ADX < 15 block | 1404 | +785 | -643 | -1.5 | -20 / -523 / -100 | +14 | 1388 | worse |
| ③ EMA20/VWAP crosses >= 4 block | 1306 | +23 | -1404 | -2.3 | -466 / -569 / -369 | -24 | 1275 | robustly worse |
| ③ crosses >= 6 block | 1513 | +323 | -1105 | -4.1 | -198 / -576 / -331 | +24 | 1328 | robustly worse |
| ③ N-bar range < 2 ATR block | 1518 | +1313 | -115 | -0.5 | -114 / -162 / +161 | +11 | 886 | worse |
| ③ N-bar range < 3 ATR block | 1103 | +171 | -1257 | -1.7 | -516 / -959 / +219 | +123 | 1495 | worse |
| ③ HTF flips >= 2 in 8 block | 688 | +1160 | -268 | -0.3 | -175 / -184 / +90 | -405 | 411 | worse |
| ③ HTF flips >= 3 in 8 block | 1294 | +979 | -449 | -0.8 | +72 / -492 / -29 | -173 | 1070 | worse |
| ③ HTF flips >= 4 in 8 block | 1485 | +1197 | -230 | -0.8 | -156 / -340 / +266 | +31 | 1104 | worse |
| ③ Skip non-flip setups from 6 HTF candles after flip | 1224 | +1697 | +270 | +0.5 | -73 / +2 / +341 | -7 | 685 | noise |
| ③ ... from 9 | 1383 | +1415 | -12 | -0.0 | -165 / +105 / +48 | -146 | 835 | worse |
| ③ ... from 12 | 1460 | +1847 | +419 | +1.5 | +53 / +152 / +213 | +15 | 786 | promising |
| ③ Block if VWAP -3 / +2 pts | 1524 | +1465 | +38 | +0.2 | +35 / +7 / -4 | -0 | 907 | noise |
| ③ Block if EMA200 -3 / +2 pts | 1521 | +1327 | -101 | -0.5 | -198 / +0 / +96 | +114 | 954 | worse |
| ③ Environment EMA200 vs VWAP | 638 | -145 | -1572 | -1.6 | -492 / -265 / -816 | -749 | 779 | worse |
| ③ Skip while ATR > 1.8 x ATR(100) | 1452 | +1499 | +71 | +0.2 | -335 / +242 / +164 | +61 | 822 | noise |
| ③ Skip if SL1 cap < 1.5 ATR | 507 | +787 | -640 | -0.6 | -400 / -745 / +504 | -562 | 339 | worse |
| ③ ER 0.18 | 1610 | +1344 | -83 | -0.2 | +59 / -297 / +154 | +100 | 1046 | worse |
| ③ ER 0.20 | 1589 | +1477 | +49 | +0.2 | +103 / -148 / +94 | +62 | 961 | noise |
| ③ ER 0.26 | 1503 | +1278 | -149 | -0.6 | +22 / -120 / -51 | -80 | 950 | worse |
| ③ ER 0.30 | 1467 | +1309 | -119 | -0.3 | -31 / -118 / +30 | -19 | 886 | worse |
| ③ ER filter OFF | 1697 | +1758 | +330 | +0.6 | +46 / -88 / +372 | +131 | 907 | noise |
| ③ ER breakout exception OFF | 1123 | +545 | -883 | -1.1 | -371 / -321 / -190 | -376 | 795 | worse |
| ③ Range gate 4 ATR | 1423 | +1581 | +153 | +0.3 | +200 / -449 / +403 | +182 | 885 | noise |
| ③ Range gate 6 ATR | 1248 | +1326 | -101 | -0.1 | -127 / -349 / +375 | +12 | 625 | worse |
| ③ Range gate zone 30 % | 1160 | -174 | -1602 | -2.0 | -696 / -1087 / +181 | +141 | 1378 | worse |
| ③ Range gate ON 5 ATR | 1312 | +1151 | -276 | -0.4 | -113 / -601 / +438 | +121 | 926 | worse |
| ③ VWAP stretch 3 ATR | 1149 | +2027 | +599 | +0.9 | -372 / +37 / +934 | +143 | 626 | noise |
| ③ VWAP stretch 6 ATR | 1450 | +2025 | +598 | +1.7 | +124 / +256 / +218 | +26 | 810 | promising |
| ③ VWAP stretch ON 4 ATR | 1297 | +2152 | +724 | +1.4 | -438 / +363 / +800 | +214 | 734 | noise |
| ① Flip min ER 0.15 | 1587 | +1889 | +461 | +1.3 | +256 / -42 / +248 | -50 | 895 | noise |
| ① Flip min ER 0.30 | 1496 | +1067 | -360 | -1.1 | +66 / -461 / +35 | +127 | 1053 | worse |
| ① Toward late-away 1 pt (instead of strict) | 1544 | +1428 | +0 | +0.0 | +0 / +0 / +0 | +0 | 891 | noise |
| ① SL1 x 1.5 ATR | 1548 | +1329 | -99 | -0.3 | +7 / -9 / -96 | +12 | 944 | worse |
| ① SL1 x 2.0 | 1542 | +1444 | +17 | +0.1 | +15 / +29 / -27 | -2 | 876 | noise |
| ① SL1 x 2.5 | 1541 | +1560 | +133 | +0.4 | +148 / +8 / -23 | -2 | 879 | noise |
| ① SL1 x 3.0 | 1541 | +1545 | +118 | +0.4 | +142 / -2 / -23 | -2 | 879 | noise |
| ① SL1 x 3.5 | 1541 | +1537 | +110 | +0.4 | +140 / -7 / -23 | -2 | 879 | noise |
| ① TP1 x 1.25 ATR | 1566 | +634 | -794 | -1.1 | -298 / -137 / -359 | -214 | 928 | worse |
| ① TP1 x 1.5 | 1552 | +1449 | +21 | +0.0 | -25 / +82 / -36 | -74 | 947 | noise |
| ① TP1 x 1.75 | 1541 | +1245 | -183 | -0.3 | -10 / -221 / +48 | +7 | 922 | worse |
| ① TP1 x 2.0 | 1537 | +1193 | -234 | -0.4 | +82 / -433 / +117 | +27 | 1114 | worse |
| ① TP1 x 2.5 | 1529 | +1155 | -273 | -0.5 | +87 / -488 / +128 | +30 | 1208 | worse |
| ① Close at TP1 0 % | 1544 | +800 | -628 | -0.8 | -263 / -901 / +535 | +163 | 2095 | worse |
| ① Close at TP1 50 % | 1544 | +1192 | -235 | -0.3 | -98 / -338 / +201 | +61 | 1128 | worse |
| ① Close at TP1 80 % | 1544 | +1428 | +0 | +0.0 | +0 / +0 / +0 | +0 | 891 | noise |
| ① Close at TP1 100 % | 1628 | +1861 | +433 | +0.5 | +21 / +65 / +346 | +5 | 829 | noise |
| ① Breakeven at TP1 OFF | 1526 | +1685 | +257 | +0.5 | +41 / -58 / +275 | +247 | 919 | noise |
| ① Trail 1.3 ATR | 1583 | +1541 | +114 | +0.2 | +60 / +48 / +5 | -15 | 828 | noise |
| ① Trail 1.7 ATR | 1544 | +1428 | +0 | +0.0 | +0 / +0 / +0 | +0 | 891 | noise |
| ① Trail 2.5 ATR | 1466 | +1581 | +154 | +0.2 | +48 / -61 / +168 | +58 | 823 | noise |
| ① Trail 3.5 ATR | 1431 | +1430 | +2 | +0.0 | +30 / -223 / +195 | +46 | 762 | noise |
| ① No trail | 1417 | +1280 | -148 | -0.2 | -12 / -237 / +101 | +5 | 754 | worse |
| ① Min SL x 0.6 | 1547 | +1423 | -5 | -0.0 | -25 / +42 / -21 | +0 | 927 | worse |
| ① Min SL x 1.4 | 1531 | +2009 | +582 | +0.7 | +795 / -101 / -112 | -68 | 1081 | noise |
| ① Max SL1 cap OFF | 1517 | +2389 | +962 | +1.3 | +1099 / -500 / +362 | +57 | 1285 | noise |
| ① Max TP1 cap OFF | 1531 | +1648 | +220 | +0.4 | +8 / +180 / +32 | +297 | 1371 | noise |
| ① Time stop 10 candles (< 0.5 ATR progress) | 1549 | +1413 | -14 | -0.1 | +4 / +31 / -49 | +22 | 948 | worse |
| ① Time stop 20 candles | 1545 | +1435 | +8 | +0.1 | -13 / +0 / +21 | +21 | 891 | noise |
| ① Flip ride ON | 1544 | +1146 | -282 | -0.7 | +229 / -678 / +168 | -79 | 1747 | worse |
| ② LTF pierce late window 0 | 1462 | +1634 | +207 | +0.5 | -45 / -122 / +373 | +132 | 954 | noise |
| ② LTF pierce late window 2 | 1577 | +1110 | -317 | -1.3 | -374 / +26 / +31 | -143 | 812 | worse |
| ② HTF pierce late window 0 | 1510 | +1382 | -45 | -0.2 | +97 / -67 / -76 | -82 | 771 | worse |
| ② HTF pierce late window 2 | 1554 | +1395 | -32 | -0.2 | -90 / +29 / +29 | -31 | 891 | worse |
| ② HTF late trade-colour OFF | 1544 | +1428 | +0 | +0.0 | +0 / +0 / +0 | +0 | 891 | noise |
| ② HTF pierce replaces current setup | 1626 | +1435 | +7 | +0.0 | -238 / +4 / +241 | -131 | 793 | noise |
| ② HTF pierce requires close beyond LTF EMA9/20 | 1544 | +1428 | +0 | +0.0 | +0 / +0 / +0 | +0 | 891 | noise |
| ② Flip: require pullback first (wait 10) | 1544 | +1428 | +0 | +0.0 | +0 / +0 / +0 | +0 | 891 | noise |
| ② Trigger HTF CBC Flip OFF | 1369 | +764 | -663 | -1.0 | -397 / -484 / +218 | +84 | 957 | worse |
| ② Trigger LTF EMA20 Pierce OFF | 1054 | +1322 | -105 | -0.1 | -36 / -472 / +403 | -575 | 1248 | worse |
| ② Trigger HTF EMA9 Pierce OFF | 1379 | +986 | -442 | -0.8 | +90 / -358 / -174 | -125 | 874 | worse |
| ② Trigger HTF EMA20 Pierce OFF | 1412 | +479 | -948 | -1.9 | -260 / -481 / -207 | +78 | 984 | worse |
| ① Flip distance 1.5 ATR | 1524 | +1520 | +92 | +0.5 | -11 / -10 / +113 | -50 | 831 | noise |
| ① Flip distance 3 ATR | 1580 | +1405 | -22 | -0.1 | -151 / +157 / -28 | -85 | 922 | worse |
| ① Flip side gate 2 pts | 1543 | +1407 | -20 | -0.6 | +0 / +0 / -20 | +0 | 911 | worse |
| ① Flip VWAP slope OFF | 1544 | +1428 | +0 | +0.0 | +0 / +0 / +0 | +0 | 891 | noise |
| ① HTF pierce min ER 0 | 1730 | +1136 | -292 | -0.5 | -521 / +296 / -67 | -45 | 1042 | worse |
| ① HTF pierce min ER 0.23 | 1456 | +506 | -922 | -2.3 | -323 / -366 / -232 | -93 | 956 | robustly worse |
| ① LTF pierce min ER 0.12 | 1453 | +1738 | +311 | +0.8 | +92 / +44 / +175 | +7 | 735 | noise |
| ① LTF pierce min ER 0.15 | 1386 | +1268 | -160 | -0.3 | -131 / -188 / +159 | -70 | 1070 | worse |
| ① LTF pierce min ER 0.23 | 1278 | +1250 | -178 | -0.3 | -161 / -40 / +23 | -296 | 984 | worse |
| ① VWAP reclaim block OFF | 1688 | +1402 | -25 | -0.1 | +76 / -181 / +79 | +138 | 1005 | worse |
| ① VWAP reclaim block 8 | 1521 | +1844 | +417 | +1.9 | +133 / +259 / +25 | +0 | 829 | promising |
| ① Min candles between setups 5 | 1623 | +1573 | +145 | +0.4 | -149 / +97 / +197 | -19 | 857 | noise |
| ① Min candles 15 | 1460 | +1098 | -330 | -1.0 | +10 / -302 / -38 | -72 | 915 | worse |
| ① ATR length 10 | 1549 | +1257 | -170 | -0.2 | +34 / -136 / -68 | -99 | 897 | worse |
| ① ATR length 20 | 1536 | +2020 | +593 | +0.8 | +145 / +129 / +319 | +81 | 827 | noise |
| ① No new setups 16:00-19:00 | 1532 | +1370 | -57 | -0.4 | +69 / -62 / -64 | -24 | 891 | worse |
| ① No-new-setup window OFF | 1657 | +1646 | +218 | +0.6 | +197 / -31 / +53 | +81 | 807 | noise |
| ① OR forming blocks all OFF | 1680 | +1105 | -322 | -0.7 | +291 / -143 / -470 | -86 | 1119 | worse |
| ① End setups at 16:00 OFF | 1544 | +971 | -456 | -2.3 | -197 / -192 / -67 | -9 | 972 | robustly worse |

## M2K 5m (v1.11)

Base: 216 trades, net +86, avg +0.40, thirds +42 / +1 / +43, last 4 wk -7, max DD 36

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ③ CHOP > 61.8 block | 201 | +93 | +7 | +0.4 | +2 / +5 / +0 | +1 | 35 | noise |
| ③ CHOP > 58 block | 185 | +59 | -27 | -1.2 | -19 / +6 / -15 | +1 | 33 | worse |
| ③ ADX < 20 block | 171 | +59 | -28 | -1.0 | +4 / -5 / -27 | -6 | 41 | worse |
| ③ ADX < 15 block | 204 | +105 | +18 | +1.3 | +10 / +7 / +2 | +2 | 36 | promising |
| ③ EMA20/VWAP crosses >= 4 block | 194 | +85 | -1 | -0.1 | -4 / -6 / +9 | +0 | 38 | worse |
| ③ crosses >= 6 block | 211 | +74 | -13 | -1.0 | +0 / -8 / -5 | +0 | 38 | worse |
| ③ N-bar range < 2 ATR block | 213 | +77 | -10 | -1.4 | -7 / +0 / -2 | +0 | 38 | worse |
| ③ N-bar range < 3 ATR block | 138 | +63 | -23 | -0.7 | -9 / +10 / -25 | +12 | 38 | worse |
| ③ HTF flips >= 2 in 8 block | 116 | +31 | -56 | -1.4 | -24 / -14 / -18 | +9 | 32 | worse |
| ③ HTF flips >= 3 in 8 block | 196 | +65 | -21 | -1.1 | -2 / +7 / -25 | +5 | 41 | worse |
| ③ HTF flips >= 4 in 8 block | 209 | +65 | -21 | -2.1 | -2 / -1 / -17 | +1 | 36 | robustly worse |
| ③ Skip non-flip setups from 6 HTF candles after flip | 123 | +58 | -28 | -0.8 | -14 / +7 / -22 | -3 | 37 | worse |
| ③ ... from 9 | 154 | +45 | -41 | -1.4 | -27 / +4 / -18 | -1 | 37 | worse |
| ③ ... from 12 | 177 | +65 | -21 | -0.9 | -26 / +1 / +3 | +0 | 36 | worse |
| ③ Block if VWAP -3 / +2 pts | 190 | +87 | +0 | +0.0 | -6 / +1 / +5 | +2 | 31 | noise |
| ③ Block if EMA200 -3 / +2 pts | 214 | +80 | -6 | -1.1 | -2 / +0 / -4 | +0 | 40 | worse |
| ③ Environment EMA200 vs VWAP | 44 | +68 | -18 | -0.4 | -13 / +16 / -22 | +8 | 9 | worse |
| ③ Skip while ATR > 1.8 x ATR(100) | 208 | +60 | -26 | -2.0 | -1 / +3 / -28 | +0 | 32 | worse |
| ③ Skip if SL1 cap < 1.5 ATR | 207 | +78 | -8 | -0.7 | -12 / +11 / -7 | -7 | 24 | worse |
| ③ ER 0.18 | 234 | +90 | +4 | +0.2 | +2 / -4 / +7 | +1 | 41 | noise |
| ③ ER 0.20 | 226 | +73 | -13 | -1.0 | -7 / -4 / -2 | -2 | 41 | worse |
| ③ ER 0.26 | 207 | +73 | -13 | -1.0 | -16 / +2 / +0 | +0 | 37 | worse |
| ③ ER 0.30 | 198 | +64 | -22 | -1.1 | -15 / -5 / -2 | +0 | 44 | worse |
| ③ ER filter OFF | 270 | +81 | -6 | -0.2 | +7 / -30 / +18 | +1 | 57 | worse |
| ③ ER breakout exception OFF | 121 | +62 | -24 | -0.6 | -29 / +11 / -6 | +7 | 24 | worse |
| ③ Range gate 4 ATR | 204 | +105 | +18 | +1.0 | +3 / +7 / +9 | -6 | 35 | promising |
| ③ Range gate 6 ATR | 182 | +63 | -23 | -0.9 | -13 / +6 / -16 | -8 | 31 | worse |
| ③ Range gate zone 30 % | 176 | +24 | -63 | -2.1 | -39 / +14 / -37 | -7 | 26 | worse |
| ③ Range gate ON 5 ATR | 195 | +65 | -22 | -1.0 | -14 / +4 / -12 | -7 | 35 | worse |
| ③ VWAP stretch 3 ATR | 78 | +29 | -57 | -1.3 | -30 / -11 / -16 | +2 | 23 | worse |
| ③ VWAP stretch 6 ATR | 163 | +79 | -7 | -0.3 | +3 / -3 / -7 | +4 | 30 | worse |
| ③ VWAP stretch ON 4 ATR | 106 | +46 | -40 | -1.0 | -30 / -6 / -4 | +1 | 24 | worse |
| ① Flip min ER 0.15 | 220 | +50 | -36 | -2.4 | +3 / -3 / -36 | -13 | 37 | worse |
| ① Flip min ER 0.30 | 212 | +94 | +8 | +0.7 | -5 / +10 / +2 | +2 | 31 | noise |
| ① Toward late-away 1 pt (instead of strict) | 216 | +86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 36 | noise |
| ① SL1 x 1.5 ATR | 217 | +75 | -12 | -0.6 | +2 / -0 / -13 | +2 | 37 | worse |
| ① SL1 x 2.0 | 216 | +96 | +10 | +0.5 | +4 / +4 / +2 | -1 | 35 | noise |
| ① SL1 x 2.5 | 216 | +94 | +8 | +0.4 | -1 / +10 / -1 | -2 | 34 | noise |
| ① SL1 x 3.0 | 216 | +86 | +0 | +0.0 | -2 / +8 / -5 | -3 | 35 | noise |
| ① SL1 x 3.5 | 216 | +86 | -0 | -0.0 | -2 / +6 / -5 | -4 | 35 | worse |
| ① TP1 x 1.25 ATR | 218 | +89 | +3 | +0.1 | -4 / +6 / +1 | -1 | 34 | noise |
| ① TP1 x 1.5 | 218 | +91 | +5 | +0.2 | +2 / +2 / +1 | -1 | 34 | noise |
| ① TP1 x 1.75 | 216 | +85 | -1 | -0.0 | +0 / -2 / +1 | +0 | 36 | worse |
| ① TP1 x 2.0 | 216 | +84 | -3 | -0.1 | +3 / -3 / -3 | +1 | 38 | worse |
| ① TP1 x 2.5 | 215 | +75 | -11 | -0.4 | +1 / -5 / -7 | +2 | 42 | worse |
| ① Close at TP1 0 % | 216 | +145 | +58 | +1.4 | +25 / +1 / +32 | -7 | 39 | promising |
| ① Close at TP1 50 % | 216 | +86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 36 | noise |
| ① Close at TP1 80 % | 216 | +51 | -35 | -0.8 | -15 / -1 / -19 | +4 | 37 | worse |
| ① Close at TP1 100 % | 225 | +35 | -51 | -1.1 | -22 / +0 / -29 | +7 | 42 | worse |
| ① Breakeven at TP1 OFF | 215 | +67 | -20 | -0.7 | -8 / -8 / -3 | -6 | 40 | worse |
| ① Trail 1.3 ATR | 221 | +100 | +14 | +0.4 | +8 / +8 / -2 | -1 | 34 | noise |
| ① Trail 1.7 ATR | 216 | +86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 36 | noise |
| ① Trail 2.5 ATR | 208 | +87 | +0 | +0.0 | +25 / -9 / -15 | -2 | 40 | noise |
| ① Trail 3.5 ATR | 208 | +59 | -28 | -0.8 | +15 / -17 / -26 | -3 | 45 | worse |
| ① No trail | 206 | +65 | -21 | -0.6 | +23 / -16 / -28 | -3 | 54 | worse |
| ① Min SL x 0.6 | 217 | +77 | -9 | -0.5 | +0 / +1 / -11 | +1 | 44 | worse |
| ① Min SL x 1.4 | 216 | +79 | -8 | -0.4 | -1 / -2 / -5 | -2 | 40 | worse |
| ① Max SL1 cap OFF | 216 | +84 | -2 | -0.3 | -0 / -2 / +0 | +0 | 38 | worse |
| ① Max TP1 cap OFF | 214 | +29 | -57 | -1.7 | -23 / -33 / -1 | -17 | 46 | worse |
| ① Time stop 10 candles (< 0.5 ATR progress) | 217 | +85 | -1 | -0.2 | +0 / -0 / -1 | +0 | 37 | worse |
| ① Time stop 20 candles | 217 | +85 | -1 | -0.2 | +0 / -1 / +0 | +0 | 37 | worse |
| ① Flip ride ON | 216 | +72 | -14 | -1.0 | -6 / -13 / +4 | +7 | 42 | worse |
| ② LTF pierce late window 0 | 184 | +80 | -6 | -0.2 | -3 / +9 / -12 | -2 | 27 | worse |
| ② LTF pierce late window 2 | 229 | +81 | -5 | -0.3 | +2 / -12 / +5 | -2 | 36 | worse |
| ② HTF pierce late window 0 | 213 | +77 | -9 | -1.4 | +0 / -1 / -8 | +0 | 36 | worse |
| ② HTF pierce late window 2 | 217 | +85 | -1 | -0.2 | +0 / +0 / -1 | +0 | 36 | worse |
| ② HTF late trade-colour OFF | 216 | +86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 36 | noise |
| ② HTF pierce replaces current setup | 219 | +80 | -6 | -0.7 | -4 / -2 / +0 | +0 | 38 | worse |
| ② HTF pierce requires close beyond LTF EMA9/20 | 216 | +86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 36 | noise |
| ② Flip: require pullback first (wait 10) | 216 | +86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 36 | noise |
| ② Trigger HTF CBC Flip OFF | 206 | +97 | +11 | +0.5 | -6 / +7 / +10 | -0 | 33 | noise |
| ② Trigger LTF EMA20 Pierce OFF | 57 | +39 | -47 | -0.9 | -28 / -6 / -14 | +7 | 18 | worse |
| ② Trigger HTF EMA9 Pierce OFF | 198 | +55 | -32 | -1.7 | +1 / -8 / -25 | +0 | 42 | worse |
| ② Trigger HTF EMA20 Pierce OFF | 216 | +86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 36 | noise |
| ① Flip distance 1.5 ATR | 211 | +100 | +14 | +1.1 | +2 / +2 / +10 | +0 | 35 | promising |
| ① Flip distance 3 ATR | 223 | +58 | -28 | -2.1 | -22 / -2 / -4 | +0 | 34 | robustly worse |
| ① Flip side gate 2 pts | 215 | +88 | +2 | +0.6 | +0 / +0 / +2 | +2 | 36 | noise |
| ① Flip VWAP slope OFF | 216 | +86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 36 | noise |
| ① HTF pierce min ER 0 | 245 | +132 | +46 | +2.0 | +8 / +26 / +12 | -2 | 35 | robust except last 4 wk |
| ① HTF pierce min ER 0.23 | 213 | +85 | -1 | -0.2 | +1 / -2 / +0 | +0 | 36 | worse |
| ① LTF pierce min ER 0.12 | 188 | +74 | -12 | -0.5 | -28 / +12 / +4 | +6 | 28 | worse |
| ① LTF pierce min ER 0.15 | 174 | +80 | -6 | -0.2 | -23 / +13 / +5 | +5 | 28 | worse |
| ① LTF pierce min ER 0.23 | 129 | +49 | -37 | -1.0 | -37 / +10 / -10 | +7 | 26 | worse |
| ① VWAP reclaim block OFF | 230 | +91 | +5 | +0.3 | -2 / +3 / +5 | +3 | 36 | noise |
| ① VWAP reclaim block 8 | 214 | +79 | -7 | -0.9 | -4 / +0 / -3 | +0 | 36 | worse |
| ① Min candles between setups 5 | 220 | +84 | -2 | -0.2 | -1 / +0 / -1 | -1 | 36 | worse |
| ① Min candles 15 | 213 | +80 | -7 | -0.8 | -3 / -3 / -1 | -1 | 36 | worse |
| ① ATR length 10 | 224 | +64 | -22 | -0.5 | +5 / +4 / -31 | -4 | 37 | worse |
| ① ATR length 20 | 208 | +92 | +6 | +0.1 | +6 / -9 / +9 | +4 | 34 | noise |
| ① No new setups 16:00-19:00 | 213 | +91 | +5 | +0.7 | +3 / +2 / +0 | +0 | 32 | noise |
| ① No-new-setup window OFF | 245 | +92 | +5 | +0.3 | +21 / -7 / -9 | -1 | 44 | noise |
| ① OR forming blocks all OFF | 233 | +118 | +32 | +2.0 | +26 / +14 / -8 | +1 | 41 | noise |
| ① End setups at 16:00 OFF | 216 | +87 | +1 | +0.1 | +6 / -2 / -3 | +0 | 38 | noise |

## Neighbour checks: MES 5m

Base: 228 trades, net +248, avg +1.09, thirds +54 / +99 / +96, last 4 wk +17, max DD 46

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ① Flip side gate OFF | 229 | +253 | +5 | +0.5 | +5 / +0 / +0 | +0 | 46 | noise |
| ① ATR length 8 | 234 | +290 | +41 | +0.6 | -9 / +3 / +47 | +11 | 40 | noise |
| ① ATR length 10 | 235 | +312 | +64 | +1.0 | +2 / +19 / +43 | +11 | 45 | promising |
| ① ATR length 12 | 231 | +273 | +25 | +0.4 | -16 / +24 / +16 | +5 | 49 | noise |
| ① ATR length 16 | 231 | +262 | +14 | +0.2 | +1 / +6 / +7 | +0 | 46 | noise |
| ① No new setups 16:00-19:00 + ATR 10 | 227 | +332 | +83 | +1.3 | +10 / +23 / +50 | +17 | 41 | promising |

## Neighbour checks: MGC 5m

Base: 628 trades, net +512, avg +0.82, thirds +90 / +224 / +199, last 4 wk +11, max DD 118

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ① Flip side gate OFF | 628 | +512 | +0 | +0.0 | +0 / +0 / +0 | +0 | 118 | noise |
| ① Max SL1 cap 10 | 624 | +672 | +160 | +1.9 | +109 / +11 / +40 | +1 | 94 | promising |
| ① Max SL1 cap 12 | 623 | +667 | +154 | +1.9 | +81 / +27 / +46 | -3 | 115 | promising |
| ① Max SL1 cap 15 | 623 | +670 | +157 | +1.9 | +100 / +16 / +41 | -4 | 125 | promising |
| ① Max SL1 cap 20 | 623 | +689 | +177 | +2.1 | +122 / +14 / +41 | -4 | 132 | robust except last 4 wk |
| ① Max SL1 cap 1000000000.0 | 623 | +704 | +191 | +2.3 | +136 / +14 / +41 | -4 | 142 | robust except last 4 wk |
| ③ VWAP stretch 5 ATR | 464 | +508 | -4 | -0.1 | -17 / +33 / -20 | -20 | 99 | worse |
| ③ VWAP stretch 6 ATR | 525 | +612 | +100 | +1.5 | +16 / +75 / +9 | +9 | 112 | promising |
| ③ VWAP stretch 7 ATR | 568 | +527 | +15 | +0.3 | +4 / +21 / -11 | +3 | 110 | noise |
| ③ VWAP stretch 8 ATR | 593 | +522 | +9 | +0.3 | +12 / -5 / +2 | -10 | 118 | noise |
| ③ Skip non-flip from 10 | 525 | +519 | +7 | +0.1 | +18 / -37 / +26 | -4 | 94 | noise |
| ③ Skip non-flip from 12 | 560 | +595 | +82 | +1.6 | +47 / +6 / +29 | +1 | 89 | promising |
| ③ Skip non-flip from 15 | 588 | +541 | +29 | +0.7 | +9 / +0 / +20 | +3 | 115 | noise |
| ③ Skip non-flip from 18 | 610 | +492 | -20 | -0.8 | -14 / -4 / -2 | -4 | 118 | worse |
| ② LTF pierce late window 0 | 578 | +584 | +72 | +1.3 | +18 / +21 / +33 | +30 | 115 | promising |

## Neighbour checks: MNQ 5m

Base: 1544 trades, net +1428, avg +0.92, thirds +556 / +686 / +186, last 4 wk +487, max DD 891

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ① Flip side gate OFF | 1587 | +1686 | +259 | +0.8 | -78 / +205 / +132 | -72 | 805 | noise |
| ③ VWAP stretch 4 ATR | 1297 | +2152 | +724 | +1.4 | -438 / +363 / +800 | +214 | 734 | noise |
| ③ VWAP stretch 5 ATR | 1384 | +2148 | +721 | +1.7 | -215 / +357 / +579 | +75 | 767 | noise |
| ③ VWAP stretch 6 ATR | 1450 | +2025 | +598 | +1.7 | +124 / +256 / +218 | +26 | 810 | promising |
| ③ VWAP stretch 7 ATR | 1484 | +2033 | +606 | +2.2 | +59 / +227 / +319 | +4 | 777 | robust |
| ③ VWAP stretch 8 ATR | 1513 | +1766 | +338 | +1.7 | +80 / +167 / +92 | -26 | 838 | promising |
| ③ Skip non-flip from 10 | 1409 | +1621 | +193 | +0.5 | -19 / +173 / +39 | -146 | 804 | noise |
| ③ Skip non-flip from 12 | 1460 | +1847 | +419 | +1.5 | +53 / +152 / +213 | +15 | 786 | promising |
| ③ Skip non-flip from 15 | 1497 | +1527 | +99 | +0.5 | -47 / +90 / +57 | +59 | 832 | noise |
| ③ Skip non-flip from 18 | 1517 | +1521 | +93 | +0.6 | -76 / +32 / +137 | +68 | 862 | noise |
| ① VWAP reclaim block 6 | 1534 | +1554 | +126 | +0.9 | +92 / +44 / -10 | +0 | 891 | noise |
| ① VWAP reclaim block 8 | 1521 | +1844 | +417 | +1.9 | +133 / +259 / +25 | +0 | 829 | promising |
| ① VWAP reclaim block 10 | 1505 | +1765 | +337 | +1.2 | +217 / +70 / +51 | +0 | 841 | promising |
| ① VWAP reclaim block 12 | 1479 | +1702 | +274 | +0.8 | +262 / -54 / +67 | +9 | 856 | noise |

## Neighbour checks: M2K 5m

Base: 216 trades, net +86, avg +0.40, thirds +42 / +1 / +43, last 4 wk -7, max DD 36

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ① Flip side gate OFF | 216 | +86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 36 | noise |
| ① HTF pierce min ER 0.0 | 245 | +132 | +46 | +2.0 | +8 / +26 / +12 | -2 | 35 | robust except last 4 wk |
| ① HTF pierce min ER 0.05 | 239 | +117 | +31 | +1.6 | -1 / +25 / +7 | -2 | 35 | noise |
| ① HTF pierce min ER 0.08 | 231 | +104 | +18 | +1.1 | -3 / +20 / +1 | -2 | 35 | noise |
| ① HTF pierce min ER 0.12 | 221 | +106 | +20 | +1.9 | +2 / +17 / +0 | +0 | 36 | noise |
| ① Close at TP1 0 % | 216 | +145 | +58 | +1.4 | +25 / +1 / +32 | -7 | 39 | promising |
| ① Close at TP1 25 % | 216 | +115 | +29 | +0.7 | +12 / +1 / +16 | -3 | 38 | noise |
| ③ ADX < 12 block | 210 | +90 | +3 | +0.4 | +2 / +0 / +1 | +0 | 36 | noise |
| ③ ADX < 15 block | 204 | +105 | +18 | +1.3 | +10 / +7 / +2 | +2 | 36 | promising |
| ③ ADX < 18 block | 183 | +75 | -12 | -0.5 | +7 / +1 / -20 | -5 | 40 | worse |
