MGC 3m stop-loss mechanisms, with and without the HTF EMA20 slope filter -- 11/14/2026.
Setups: CBC engine replay Jan 5 -> now, current MGC 3m filters (ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR, VWAP stretch 4 ATR --
applied correctly, see tsf_study), and the same + "Block in chop: HTF EMA20 slope below 0.3 ATR" (|15m EMA20 now - 12 bars ago| / ATR).
Exit = live FLIP 0 %: nothing closed at TP1 (1.7 ATR, cap 6); at TP1 the stop moves to breakeven; closed by the HTF CBC flip against,
16:00 or the next setup. Only the initial stop (SL1) changes. Same setups for every stop (rescored), net after 0.22 cost per trade.
Stops: (A) SL1 x ATR with min 5 and cap 7 (live 1.7); (B) no cap / cap 10; (C) close-based (stop counts only on a close beyond it);
(D) last-N-candle low/high, raw and clamped min 5 / cap 7; (E) last-N low/high + 0.5 ATR buffer, clamped.
z = Δ / (SD x sqrt(trades changed)); robust = z >= 2, better in all three thirds and last 4 wk >= 0; promising = z >= 1 and all thirds.

## Overview -- best stops per filter set (Δ vs live stop in the same set)

**Current filters** (1136 setups, live stop +615, max DD 245): B. 2.0 ATR, min 5, no cap +266 (z +1.0, +281 / +15 / -30, l4 -4, worst -44.8, noise); B. 1.5 ATR, min 5, no cap +252 (z +1.0, +189 / +40 / +23, l4 +4, worst -33.6, noise); B. 1.7 ATR, min 5, no cap +206 (z +1.0, +159 / +41 / +6, l4 +9, worst -38.1, promising); B. 1.7 ATR, min 5, cap 10 +57 (z +0.3, +12 / +43 / +2, l4 -1, worst -10.2, noise)

**Current + HTF EMA20 slope < 0.3 ATR block** (634 setups, live stop +1135, max DD 121): B. 2.0 ATR, min 5, no cap +320 (z +1.5, +334 / +6 / -20, l4 -2, worst -18.3, noise); B. 1.7 ATR, min 5, no cap +161 (z +1.0, +143 / +11 / +6, l4 +2, worst -33.3, noise); B. 1.5 ATR, min 5, no cap +130 (z +0.6, +167 / -1 / -36, l4 +5, worst -29.4, noise); C. Close stop: SL1 on a close (BE a touch) +81 (z +0.4, +45 / +9 / +27, l4 -2, worst -32.8, noise)

## MGC 3m -- Current filters: 1136 setups; live stop net +615, thirds +329 / -10 / +297, last 4 wk +262, win 18 %, worst -7.2, max DD 245

| Stop | Net | Δ vs live stop | z | Δ by third | Δ last 4 wk | Win % | Avg stop pts | Worst trade | Max DD |
|---|---|---|---|---|---|---|---|---|---|
| **Live: 1.7 ATR, min 5, cap 7** | +615 | +0 | +0.0 | +0 / +0 / +0 | +0 | 18 % | 6.3 | -7.2 | 245 |
| A. 1.3 ATR, min 5, cap 7 | +573 | -42 | -0.2 | +21 / -30 / -34 | -25 | 18 % | 5.8 | -7.2 | 241 |
| A. 1.5 ATR, min 5, cap 7 | +645 | +30 | +0.2 | +15 / +14 / +0 | -8 | 18 % | 6.0 | -7.2 | 216 |
| A. 2.0 ATR, min 5, cap 7 | +580 | -35 | -0.2 | -17 / -10 / -9 | -6 | 19 % | 6.6 | -7.2 | 267 |
| A. 2.5 ATR, min 5, cap 7 | +559 | -56 | -0.3 | -24 / -9 / -23 | -8 | 19 % | 6.8 | -7.2 | 277 |
| A. 1.7 ATR, min 4, cap 7 | +517 | -98 | -0.8 | +5 / +3 / -106 | +3 | 18 % | 6.2 | -7.2 | 265 |
| A. 1.7 ATR, min 6, cap 7 | +590 | -25 | -0.2 | -12 / -13 / -0 | -6 | 18 % | 6.6 | -7.2 | 260 |
| A. Fixed 7 pts | +557 | -58 | -0.3 | -27 / -15 / -15 | -10 | 19 % | 7.0 | -7.2 | 281 |
| A. Fixed 5 pts | +475 | -140 | -0.5 | -41 / -65 / -34 | -20 | 17 % | 5.0 | -5.2 | 327 |
| B. 1.5 ATR, min 5, no cap | +867 | +252 | +1.0 | +189 / +40 / +23 | +4 | 20 % | 7.6 | -33.6 | 225 |
| B. 1.7 ATR, min 5, no cap | +821 | +206 | +1.0 | +159 / +41 / +6 | +9 | 20 % | 8.4 | -38.1 | 257 |
| B. 2.0 ATR, min 5, no cap | +881 | +266 | +1.0 | +281 / +15 / -30 | -4 | 20 % | 9.8 | -44.8 | 228 |
| B. 1.7 ATR, min 5, cap 10 | +672 | +57 | +0.3 | +12 / +43 / +2 | -1 | 19 % | 7.3 | -10.2 | 246 |
| B. 2.0 ATR, min 5, cap 10 | +598 | -17 | -0.1 | -17 / +28 / -28 | -14 | 20 % | 8.0 | -10.2 | 266 |
| C. Close stop: SL1 on a close (BE a touch) | +593 | -22 | -0.1 | +3 / -27 / +3 | -2 | 20 % | 6.3 | -32.8 | 303 |
| C. Close stop: SL1 and BE on a close | +424 | -191 | -0.5 | -160 / +105 / -136 | -40 | 25 % | 6.3 | -32.8 | 438 |
| D. Last-2-candle low/high, raw | +480 | -135 | -0.3 | +132 / -159 / -109 | -86 | 12 % | 3.2 | -24.7 | 278 |
| D. Last-2-candle low/high, min 5 / cap 7 | +441 | -174 | -0.6 | -78 / -51 / -45 | -25 | 17 % | 5.2 | -7.2 | 334 |
| E. Last-2 low/high + 0.5 ATR, min 5 / cap 7 | +559 | -56 | -0.2 | +15 / -24 / -47 | -32 | 18 % | 5.6 | -7.2 | 252 |
| D. Last-3-candle low/high, raw | +537 | -78 | -0.2 | +75 / -52 / -101 | -77 | 13 % | 3.6 | -27.2 | 231 |
| D. Last-3-candle low/high, min 5 / cap 7 | +473 | -142 | -0.5 | -97 / -20 / -26 | -28 | 17 % | 5.3 | -7.2 | 291 |
| E. Last-3 low/high + 0.5 ATR, min 5 / cap 7 | +597 | -18 | -0.1 | +20 / +8 / -46 | -34 | 18 % | 5.7 | -7.2 | 214 |
| D. Last-5-candle low/high, raw | +460 | -155 | -0.4 | +69 / -71 / -153 | -92 | 15 % | 5.0 | -33.7 | 278 |
| D. Last-5-candle low/high, min 5 / cap 7 | +540 | -75 | -0.3 | -39 / -14 / -23 | -27 | 18 % | 5.5 | -7.2 | 249 |
| E. Last-5 low/high + 0.5 ATR, min 5 / cap 7 | +572 | -43 | -0.2 | -5 / -17 / -21 | -25 | 18 % | 5.9 | -7.2 | 248 |
| D. Last-8-candle low/high, raw | +610 | -5 | -0.0 | +84 / +32 / -121 | -102 | 17 % | 7.1 | -34.2 | 231 |
| D. Last-8-candle low/high, min 5 / cap 7 | +548 | -67 | -0.3 | -28 / -22 / -18 | -25 | 18 % | 5.9 | -7.2 | 269 |
| E. Last-8 low/high + 0.5 ATR, min 5 / cap 7 | +541 | -74 | -0.4 | -13 / -28 / -32 | -29 | 18 % | 6.2 | -7.2 | 274 |

## MGC 3m -- Current + HTF EMA20 slope < 0.3 ATR block: 634 setups; live stop net +1135, thirds +545 / +78 / +512, last 4 wk +279, win 22 %, worst -7.2, max DD 121

| Stop | Net | Δ vs live stop | z | Δ by third | Δ last 4 wk | Win % | Avg stop pts | Worst trade | Max DD |
|---|---|---|---|---|---|---|---|---|---|
| **Live: 1.7 ATR, min 5, cap 7** | +1135 | +0 | +0.0 | +0 / +0 / +0 | +0 | 22 % | 6.3 | -7.2 | 121 |
| A. 1.3 ATR, min 5, cap 7 | +1043 | -93 | -0.6 | +4 / -21 / -75 | +4 | 22 % | 5.8 | -7.2 | 117 |
| A. 1.5 ATR, min 5, cap 7 | +1088 | -47 | -0.3 | +5 / +0 / -52 | +1 | 22 % | 6.1 | -7.2 | 120 |
| A. 2.0 ATR, min 5, cap 7 | +1124 | -12 | -0.1 | -5 / -1 / -6 | -0 | 22 % | 6.6 | -7.2 | 125 |
| A. 2.5 ATR, min 5, cap 7 | +1117 | -19 | -0.1 | -12 / +4 / -10 | -3 | 22 % | 6.9 | -7.2 | 126 |
| A. 1.7 ATR, min 4, cap 7 | +1020 | -116 | -1.2 | +4 / -3 / -117 | +1 | 22 % | 6.2 | -7.2 | 121 |
| A. 1.7 ATR, min 6, cap 7 | +1124 | -12 | -0.1 | -6 / -7 / +1 | -0 | 22 % | 6.6 | -7.2 | 123 |
| A. Fixed 7 pts | +1121 | -14 | -0.1 | -16 / +1 / -0 | -4 | 22 % | 7.0 | -7.2 | 127 |
| A. Fixed 5 pts | +1041 | -94 | -0.4 | -4 / -14 / -77 | -2 | 21 % | 5.0 | -5.2 | 107 |
| B. 1.5 ATR, min 5, no cap | +1265 | +130 | +0.6 | +167 / -1 / -36 | +5 | 23 % | 7.8 | -29.4 | 101 |
| B. 1.7 ATR, min 5, no cap | +1296 | +161 | +1.0 | +143 / +11 / +6 | +2 | 24 % | 8.7 | -33.3 | 114 |
| B. 2.0 ATR, min 5, no cap | +1456 | +320 | +1.5 | +334 / +6 / -20 | -2 | 24 % | 10.1 | -18.3 | 102 |
| B. 1.7 ATR, min 5, cap 10 | +1141 | +5 | +0.0 | -18 / +14 / +9 | +2 | 23 % | 7.3 | -10.2 | 141 |
| B. 2.0 ATR, min 5, cap 10 | +1121 | -14 | -0.1 | -15 / +14 / -13 | -2 | 24 % | 8.0 | -10.2 | 140 |
| C. Close stop: SL1 on a close (BE a touch) | +1217 | +81 | +0.4 | +45 / +9 / +27 | -2 | 24 % | 6.3 | -32.8 | 96 |
| C. Close stop: SL1 and BE on a close | +1031 | -105 | -0.3 | -113 / +65 / -57 | -37 | 29 % | 6.3 | -32.8 | 202 |
| D. Last-2-candle low/high, raw | +855 | -281 | -0.8 | -42 / -53 / -186 | -82 | 15 % | 3.4 | -24.7 | 80 |
| D. Last-2-candle low/high, min 5 / cap 7 | +1069 | -66 | -0.3 | -31 / -15 / -20 | -4 | 21 % | 5.3 | -7.2 | 107 |
| E. Last-2 low/high + 0.5 ATR, min 5 / cap 7 | +1097 | -39 | -0.2 | -4 / -16 / -18 | +4 | 22 % | 5.7 | -7.2 | 112 |
| D. Last-3-candle low/high, raw | +812 | -324 | -1.0 | -64 / -70 / -189 | -74 | 16 % | 3.7 | -27.2 | 81 |
| D. Last-3-candle low/high, min 5 / cap 7 | +1070 | -65 | -0.3 | -35 / -16 / -13 | +6 | 21 % | 5.3 | -7.2 | 109 |
| E. Last-3 low/high + 0.5 ATR, min 5 / cap 7 | +1092 | -43 | -0.2 | -8 / -14 / -22 | +2 | 22 % | 5.7 | -7.2 | 114 |
| D. Last-5-candle low/high, raw | +759 | -377 | -1.2 | -87 / -85 / -205 | -75 | 17 % | 4.5 | -19.7 | 97 |
| D. Last-5-candle low/high, min 5 / cap 7 | +1060 | -75 | -0.4 | -48 / -29 / +2 | +5 | 21 % | 5.5 | -7.2 | 112 |
| E. Last-5 low/high + 0.5 ATR, min 5 / cap 7 | +1094 | -42 | -0.2 | -15 / -23 / -4 | +2 | 22 % | 5.8 | -7.2 | 117 |
| D. Last-8-candle low/high, raw | +1050 | -85 | -0.3 | +97 / -33 / -149 | -93 | 19 % | 6.1 | -31.5 | 81 |
| D. Last-8-candle low/high, min 5 / cap 7 | +1056 | -80 | -0.4 | -43 / -35 / -1 | +2 | 22 % | 5.7 | -7.2 | 118 |
| E. Last-8 low/high + 0.5 ATR, min 5 / cap 7 | +1108 | -27 | -0.2 | -2 / -30 / +4 | +3 | 22 % | 6.0 | -7.2 | 118 |
