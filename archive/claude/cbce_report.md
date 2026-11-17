Four "CBC Engine [MMT]" ideas tested on CBC -- MES 3m and MGC 3m -- 11/14/2026. Replay Jan 5 -> now, CBC engine setups, live gates.
Live exits: MES 3m SL1 3 ATR (min 5, no cap), TP1 1.75 ATR, 100 % at TP1. MGC 3m SL1 1.7 ATR (min 5, cap 7), TP1 1.7 ATR (cap 6),
0 % at TP1 + breakeven, then closed by the HTF CBC flip ("FLIP 0 %", CBC v10.96). Every setup also ends at 16:00 or the next setup.
1. CLOSE STOP: the stop only counts when a candle CLOSES beyond it (exit at that close) instead of a touch. (a) SL1 only, (b) SL1 + BE.
2. LAST-N STOP: SL1 = lowest low (long) / highest high (short) of the last N candles incl. the entry candle, N = 2 / 3 / 5;
   raw, and clamped to the symbol's min / cap. TP1 unchanged.
3. STRONG FLIP: keep a setup only if its candle swept the previous candle's low (long) then closed above the previous high
   (mirrored short). (a) the 3m entry candle, (b) the 15m candle of the HTF flip (flip setups only; others kept), (c) both.
4. ENVIRONMENT: longs only when slow EMA > VWAP, shorts only when slow EMA < VWAP; slow EMA = 3m EMA20 / 15m EMA20 / EMA200.
Ideas 3-4 are entry gates (a skipped setup can change later setups); 1-2 are exits on the same setups.
Net after costs (MES 0.50, MGC 0.22). z = Δ / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds.

## MES 3m -- current: 1799 setups, net -801, thirds -2 / -712 / -87, last 4 wk +99, win 48 %

| Variant | Setups | Net | Δ | z | Δ by third | Δ last 4 wk | Win % | Avg stop pts | Worst trade | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **Current (live)** | 1799 | -801 | +0 | +0.0 | +0 / +0 / +0 | +0 | 48 % | 11.1 | -37.6 | noise |
| 1a. Close stop: SL1 on a close (BE still a touch) | 1799 | -754 | +47 | +0.5 | +20 / +48 / -21 | -22 | 49 % | 11.1 | -34.8 | noise |
| 1b. Close stop: SL1 and BE on a close | 1799 | -754 | +47 | +0.5 | +20 / +48 / -21 | -22 | 49 % | 11.1 | -34.8 | noise |
| 2. Last-2-candle stop, raw | 1799 | -1100 | -299 | -1.2 | -143 / +73 / -229 | -103 | 25 % | 2.7 | -19.5 | worse |
| 2. Last-2-candle stop, min 5 | 1799 | -985 | -185 | -1.1 | -32 / +22 / -175 | -152 | 42 % | 5.5 | -19.5 | worse |
| 2. Last-3-candle stop, raw | 1799 | -1071 | -270 | -1.1 | -155 / +96 / -211 | -109 | 26 % | 3.0 | -19.5 | worse |
| 2. Last-3-candle stop, min 5 | 1799 | -972 | -171 | -1.0 | -49 / +44 / -166 | -135 | 42 % | 5.6 | -19.5 | worse |
| 2. Last-5-candle stop, raw | 1799 | -1044 | -244 | -1.0 | -94 / +68 / -217 | -136 | 31 % | 3.9 | -34.5 | worse |
| 2. Last-5-candle stop, min 5 | 1799 | -897 | -97 | -0.6 | +9 / +32 / -138 | -117 | 44 % | 6.1 | -34.5 | worse |
| 3a. Strong flip: 3m entry candle | 91 | -44 | +756 | +2.5 | -53 / +683 / +126 | -93 | 57 % | 12.7 | -28.6 | noise |
| 3b. Strong flip: 15m flip candle (flip setups) | 1651 | -643 | +157 | +1.1 | +105 / +111 / -58 | -34 | 47 % | 11.1 | -37.6 | noise |
| 3c. Strong flip: both | 89 | -40 | +761 | +2.5 | -44 / +683 / +122 | -93 | 57 % | 12.8 | -28.6 | noise |
| 4. Environment: 3m EMA20 vs VWAP | 1521 | -621 | +180 | +1.4 | +27 / +139 / +14 | -43 | 48 % | 11.2 | -37.6 | promising |
| 4. Environment: 15m EMA20 vs VWAP | 1237 | -601 | +200 | +1.1 | +31 / +220 / -52 | -112 | 48 % | 11.0 | -37.6 | noise |
| 4. Environment: EMA200 vs VWAP | 856 | -241 | +560 | +2.5 | +88 / +440 / +31 | -20 | 47 % | 10.6 | -27.9 | robust |

## MGC 3m -- current: 1602 setups, net +547, thirds +268 / -92 / +371, last 4 wk +312, win 18 %

| Variant | Setups | Net | Δ | z | Δ by third | Δ last 4 wk | Win % | Avg stop pts | Worst trade | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **Current (live)** | 1602 | +547 | +0 | +0.0 | +0 / +0 / +0 | +0 | 18 % | 6.3 | -7.2 | noise |
| 1a. Close stop: SL1 on a close (BE still a touch) | 1602 | +420 | -126 | -0.4 | -111 / -22 / +7 | +9 | 19 % | 6.3 | -34.3 | worse |
| 1b. Close stop: SL1 and BE on a close | 1602 | +238 | -309 | -0.7 | -270 / +118 / -156 | -5 | 25 % | 6.3 | -34.3 | worse |
| 2. Last-2-candle stop, raw | 1602 | +262 | -285 | -0.6 | +118 / -93 / -310 | -123 | 11 % | 3.3 | -24.7 | worse |
| 2. Last-2-candle stop, min 5 / cap 7 | 1602 | +416 | -131 | -0.4 | -82 / -14 / -36 | -17 | 17 % | 5.3 | -7.2 | worse |
| 2. Last-3-candle stop, raw | 1602 | +371 | -175 | -0.4 | +88 / +24 / -287 | -116 | 12 % | 3.8 | -27.2 | worse |
| 2. Last-3-candle stop, min 5 / cap 7 | 1602 | +432 | -115 | -0.4 | -99 / +10 / -25 | -21 | 17 % | 5.3 | -7.2 | worse |
| 2. Last-5-candle stop, raw | 1602 | +425 | -121 | -0.3 | +106 / -46 / -182 | -150 | 14 % | 5.3 | -33.7 | worse |
| 2. Last-5-candle stop, min 5 / cap 7 | 1602 | +494 | -53 | -0.2 | -28 / +5 / -29 | -25 | 18 % | 5.6 | -7.2 | worse |
| 3a. Strong flip: 3m entry candle | 116 | +227 | -319 | -0.6 | -274 / +133 / -178 | -235 | 20 % | 6.4 | -7.2 | worse |
| 3b. Strong flip: 15m flip candle (flip setups) | 1424 | +857 | +311 | +1.0 | +356 / -11 / -34 | +29 | 19 % | 6.3 | -7.2 | noise |
| 3c. Strong flip: both | 114 | +227 | -319 | -0.6 | -274 / +133 / -178 | -235 | 20 % | 6.4 | -7.2 | worse |
| 4. Environment: 3m EMA20 vs VWAP | 1327 | +605 | +58 | +0.2 | -50 / +63 / +45 | -59 | 19 % | 6.3 | -7.2 | noise |
| 4. Environment: 15m EMA20 vs VWAP | 1088 | +577 | +31 | +0.1 | -79 / +102 / +7 | -21 | 20 % | 6.3 | -7.2 | noise |
| 4. Environment: EMA200 vs VWAP | 910 | +169 | -377 | -1.0 | -181 / +63 / -259 | -252 | 19 % | 6.2 | -7.2 | worse |
