# Volume Strong Flip + EMA200-vs-VWAP watch -- 2026-11-14 09:01 ET

Volume Strong Flip (CBC Engine idea 5) + EMA200-vs-VWAP watch -- MES 3m and MGC 3m. Weekly, Sundays 2 pm ET.
Replay Jan 5 -> now, CBC engine setups, live gates and live exits (MES 3m SL1 3 ATR min 5, TP1 1.75 ATR, 100 % at TP1;
MGC 3m SL1 1.7 ATR min 5 cap 7, TP1 1.7 ATR cap 6, 0 % at TP1 + BE, closed by the HTF flip = "FLIP 0 %").
VOLUME STRONG FLIP: keep a setup only when volume > the average volume of the previous N candles (N = 20 / 50 / 100; 50 = CBC Engine default).
  (a) the 3m setup candle, (b) the 15m candle of the HTF flip (flip setups only; other setups kept), (c) 3m setup candle OR any of the
  last 3 candles, (d) volume AND the sweep-and-close strong-flip candle, (e) volume gate + EMA200 vs VWAP.
ENVIRONMENT WATCH: longs only when EMA200 > VWAP, shorts only when EMA200 < VWAP (and 3m EMA20 vs VWAP) -- tracked weekly toward 3 runs.
Gates are entry filters: a skipped setup can change later setups (one setup at a time, cooldown). Net after costs (MES 0.50, MGC 0.22).
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds AND last 4 wk not negative; promising = z >= 1 and all thirds.

## Overview

| Chart | Variant | Setups | Δ | z | Δ thirds | Δ last 4 wk | Verdict |
|---|---|---|---|---|---|---|---|
| MES 3m | 5a. Volume > avg 20: 3m setup candle | 1003 | +328 | +1.4 | +159 / +158 / +11 | -82 | promising |
| MES 3m | 5a. Volume > avg 50: 3m setup candle | 971 | +243 | +1.1 | +12 / +315 / -85 | -141 | noise |
| MES 3m | 5a. Volume > avg 100: 3m setup candle | 868 | +285 | +1.2 | -9 / +351 / -56 | -134 | noise |
| MES 3m | 5b. Volume > avg 20: 15m flip candle (flip setups) | 1721 | +63 | +0.6 | +45 / +80 / -61 | -40 | noise |
| MES 3m | 5b. Volume > avg 50: 15m flip candle (flip setups) | 1705 | +54 | +0.5 | +56 / +48 / -49 | -36 | noise |
| MES 3m | 5b. Volume > avg 100: 15m flip candle (flip setups) | 1689 | +99 | +0.8 | +53 / +74 / -28 | -36 | noise |
| MES 3m | 5c. Volume > avg 50: setup candle or one of last 3 | 1324 | +13 | +0.1 | -90 / +92 / +11 | -71 | noise |
| MES 3m | 5d. Volume > avg 50 AND sweep-close strong candle | 57 | +671 | +2.2 | -78 / +668 / +81 | -103 | noise |
| MES 3m | 5e. Volume > avg 50 (3m) + EMA200 vs VWAP | 478 | +685 | +2.5 | +28 / +637 / +20 | -57 | robust except last 4 wk |
| MES 3m | W1. Watch: EMA200 vs VWAP | 856 | +560 | +2.5 | +88 / +440 / +31 | -20 | robust except last 4 wk |
| MES 3m | W2. Watch: 3m EMA20 vs VWAP | 1521 | +180 | +1.4 | +27 / +139 / +14 | -43 | promising |
| MGC 3m | 5a. Volume > avg 20: 3m setup candle | 857 | -26 | -0.1 | +283 / +149 / -459 | -308 | worse |
| MGC 3m | 5a. Volume > avg 50: 3m setup candle | 824 | +169 | +0.4 | +390 / +125 / -347 | -311 | noise |
| MGC 3m | 5a. Volume > avg 100: 3m setup candle | 774 | -152 | -0.3 | +147 / +31 / -331 | -308 | worse |
| MGC 3m | 5b. Volume > avg 20: 15m flip candle (flip setups) | 1485 | +164 | +0.7 | +212 / -6 / -42 | +36 | noise |
| MGC 3m | 5b. Volume > avg 50: 15m flip candle (flip setups) | 1490 | +200 | +0.8 | +238 / +38 / -76 | +36 | noise |
| MGC 3m | 5b. Volume > avg 100: 15m flip candle (flip setups) | 1485 | +159 | +0.6 | +227 / +28 / -96 | +36 | noise |
| MGC 3m | 5c. Volume > avg 50: setup candle or one of last 3 | 1125 | -121 | -0.4 | +146 / +18 / -285 | -319 | worse |
| MGC 3m | 5d. Volume > avg 50 AND sweep-close strong candle | 59 | -448 | -0.8 | -266 / +95 / -276 | -325 | worse |
| MGC 3m | 5e. Volume > avg 50 (3m) + EMA200 vs VWAP | 438 | -302 | -0.6 | -84 / +92 / -309 | -298 | worse |
| MGC 3m | W1. Watch: EMA200 vs VWAP | 910 | -377 | -1.0 | -181 / +63 / -259 | -252 | worse |
| MGC 3m | W2. Watch: 3m EMA20 vs VWAP | 1327 | +58 | +0.2 | -50 / +63 / +45 | -59 | noise |

## MES 3m -- current: 1799 setups, net -801, thirds -2 / -712 / -87, last 4 wk +99, win 48 % (volume present on 96 % of candles)

| Variant | Setups | Net | Δ | z | Δ by third | Δ last 4 wk | Win % | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Current (live)** | 1799 | -801 | +0 | +0.0 | +0 / +0 / +0 | +0 | 48 % | noise |
| 5a. Volume > avg 20: 3m setup candle | 1003 | -473 | +328 | +1.4 | +159 / +158 / +11 | -82 | 48 % | promising |
| 5a. Volume > avg 50: 3m setup candle | 971 | -558 | +243 | +1.1 | +12 / +315 / -85 | -141 | 47 % | noise |
| 5a. Volume > avg 100: 3m setup candle | 868 | -516 | +285 | +1.2 | -9 / +351 / -56 | -134 | 48 % | noise |
| 5b. Volume > avg 20: 15m flip candle (flip setups) | 1721 | -738 | +63 | +0.6 | +45 / +80 / -61 | -40 | 48 % | noise |
| 5b. Volume > avg 50: 15m flip candle (flip setups) | 1705 | -746 | +54 | +0.5 | +56 / +48 / -49 | -36 | 47 % | noise |
| 5b. Volume > avg 100: 15m flip candle (flip setups) | 1689 | -702 | +99 | +0.8 | +53 / +74 / -28 | -36 | 47 % | noise |
| 5c. Volume > avg 50: setup candle or one of last 3 | 1324 | -787 | +13 | +0.1 | -90 / +92 / +11 | -71 | 48 % | noise |
| 5d. Volume > avg 50 AND sweep-close strong candle | 57 | -130 | +671 | +2.2 | -78 / +668 / +81 | -103 | 47 % | noise |
| 5e. Volume > avg 50 (3m) + EMA200 vs VWAP | 478 | -116 | +685 | +2.5 | +28 / +637 / +20 | -57 | 49 % | robust except last 4 wk |
| W1. Watch: EMA200 vs VWAP | 856 | -241 | +560 | +2.5 | +88 / +440 / +31 | -20 | 47 % | robust except last 4 wk |
| W2. Watch: 3m EMA20 vs VWAP | 1521 | -621 | +180 | +1.4 | +27 / +139 / +14 | -43 | 48 % | promising |

## MGC 3m -- current: 1602 setups, net +547, thirds +268 / -92 / +371, last 4 wk +312, win 18 % (volume present on 92 % of candles)

| Variant | Setups | Net | Δ | z | Δ by third | Δ last 4 wk | Win % | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Current (live)** | 1602 | +547 | +0 | +0.0 | +0 / +0 / +0 | +0 | 18 % | noise |
| 5a. Volume > avg 20: 3m setup candle | 857 | +520 | -26 | -0.1 | +283 / +149 / -459 | -308 | 19 % | worse |
| 5a. Volume > avg 50: 3m setup candle | 824 | +716 | +169 | +0.4 | +390 / +125 / -347 | -311 | 18 % | noise |
| 5a. Volume > avg 100: 3m setup candle | 774 | +394 | -152 | -0.3 | +147 / +31 / -331 | -308 | 19 % | worse |
| 5b. Volume > avg 20: 15m flip candle (flip setups) | 1485 | +710 | +164 | +0.7 | +212 / -6 / -42 | +36 | 18 % | noise |
| 5b. Volume > avg 50: 15m flip candle (flip setups) | 1490 | +746 | +200 | +0.8 | +238 / +38 / -76 | +36 | 19 % | noise |
| 5b. Volume > avg 100: 15m flip candle (flip setups) | 1485 | +706 | +159 | +0.6 | +227 / +28 / -96 | +36 | 18 % | noise |
| 5c. Volume > avg 50: setup candle or one of last 3 | 1125 | +425 | -121 | -0.4 | +146 / +18 / -285 | -319 | 18 % | worse |
| 5d. Volume > avg 50 AND sweep-close strong candle | 59 | +99 | -448 | -0.8 | -266 / +95 / -276 | -325 | 17 % | worse |
| 5e. Volume > avg 50 (3m) + EMA200 vs VWAP | 438 | +245 | -302 | -0.6 | -84 / +92 / -309 | -298 | 18 % | worse |
| W1. Watch: EMA200 vs VWAP | 910 | +169 | -377 | -1.0 | -181 / +63 / -259 | -252 | 19 % | worse |
| W2. Watch: 3m EMA20 vs VWAP | 1327 | +605 | +58 | +0.2 | -50 / +63 / +45 | -59 | 19 % | noise |
