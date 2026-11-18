MES 3m -- VWAP stretch gate, flop skip, flip-count gate -- 11/18/2026.
Base = current CBC EMA Slope MES 3m (v1.19 logic = v1.23): slope 0.42 / 12 bars, LTF ER 0.15, range gate 5, hour block 13-15,
no new setups 16:00-19:00, flip setups ride (closed by HTF flip back / SL1 / next setup); SL1 3 ATR min 5, TP1 1.75 ATR, 100 % at TP1.
Engine = claude/noflip_study.py TCase (Jan 5 -> now). Net after 0.50 cost. One gate at a time on top of the base.
Stretch = (close - VWAP) / ATR in the trade direction against you, i.e. short = (VWAP - close)/ATR (price far below VWAP).
Flop = the 15m candle holding the current HTF flip crossed EMA200 / VWAP with < 70 % of its range on the flip side (= ats_flg);
 '+ pivots' also counts any cross of PP / R1-R3 / S1-S3 (= the alert's "Flip flop: crossed ..." text).
Flip count = HTF flips in the last N 15m candles (5 x 3m bars each), incl. the current one.
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, all thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds.

Bars to 11/16 14:33 UTC. Base: 705 setups, net +815, thirds +372 / +1 / +442, last 4 wk +212.

| Gate | Setups | Net | Avg | Win % | vs base | Changed | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Base (current MES 3m) | 705 | +815 | +1.16 | 51 % | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 142 |  |
| Stretch: skip all setups > 3.0 ATR beyond VWAP on the trade side | 308 | +291 | +0.95 | 55 % | -524 | 431 | -2.6 | -214 / +8 / -319 | -159 | 96 | worse |
| Stretch: skip FLIP setups > 3.0 ATR beyond VWAP | 682 | +348 | +0.51 | 53 % | -467 | 148 | -4.0 | -43 / -82 / -343 | -102 | 215 | robustly worse |
| Stretch: skip all setups > 3.5 ATR beyond VWAP on the trade side | 365 | +383 | +1.05 | 54 % | -432 | 380 | -2.3 | -204 / +19 / -248 | -158 | 90 | worse |
| Stretch: skip FLIP setups > 3.5 ATR beyond VWAP | 685 | +386 | +0.56 | 53 % | -429 | 137 | -3.8 | -47 / -82 / -301 | -121 | 202 | robustly worse |
| Stretch: skip all setups > 4.0 ATR beyond VWAP on the trade side | 414 | +513 | +1.24 | 54 % | -302 | 333 | -1.7 | -82 / -22 / -199 | -99 | 124 | worse |
| Stretch: skip FLIP setups > 4.0 ATR beyond VWAP | 687 | +525 | +0.76 | 53 % | -291 | 125 | -2.7 | +43 / -82 / -252 | -78 | 202 | worse |
| Flop skip, flip setups (EMA200/VWAP, 70 %) = ats_flg | 704 | +822 | +1.17 | 51 % | +6 | 1 | +0.7 | +6 / +0 / +0 | +0 | 142 | noise |
| Flop skip, flip setups, + pivots | 691 | +571 | +0.83 | 51 % | -244 | 22 | -5.4 | -20 / +13 / -237 | -83 | 149 | worse |
| Flop skip, ALL setups (EMA200/VWAP) | 509 | +669 | +1.31 | 50 % | -147 | 196 | -1.1 | -61 / -49 / -37 | -8 | 120 | worse |
| Flop skip, ALL setups, + pivots | 408 | +467 | +1.14 | 51 % | -348 | 297 | -2.1 | -88 / +8 / -268 | -114 | 106 | worse |
| Flip count: skip when >= 2 HTF flips in last 4 15m candles | 562 | +326 | +0.58 | 51 % | -489 | 243 | -3.2 | -141 / -15 / -334 | -84 | 167 | robustly worse |
| Flip count: skip when >= 3 HTF flips in last 4 15m candles | 701 | +731 | +1.04 | 51 % | -85 | 8 | -3.1 | -68 / +0 / -16 | +0 | 142 | worse |
| Flip count: skip when >= 3 HTF flips in last 8 15m candles | 621 | +752 | +1.21 | 52 % | -64 | 128 | -0.6 | -55 / +39 / -48 | -28 | 108 | worse |
| Flip count: skip when >= 4 HTF flips in last 8 15m candles | 691 | +706 | +1.02 | 51 % | -109 | 26 | -2.2 | -58 / -21 / -29 | -17 | 142 | robustly worse |
| Flip count: skip when >= 4 HTF flips in last 16 15m candles | 457 | +517 | +1.13 | 51 % | -299 | 312 | -1.7 | -216 / -6 / -77 | -36 | 114 | worse |
| Flip count: skip when >= 5 HTF flips in last 16 15m candles | 642 | +830 | +1.29 | 51 % | +15 | 91 | +0.2 | +9 / +36 / -29 | -25 | 116 | noise |

## 11/17-11/18 setups in the replay (base)

| Close ET | Dir | Trigger | Entry | Stretch (ATR, trade side) | Net | Flop / flips last 8 / 16 |
|---|---|---|---|---|---|---|

## Which 11/17-11/18 setups each gate removes

- Stretch: skip all setups > 3.0 ATR beyond VWAP on the trade side: none
- Stretch: skip FLIP setups > 3.0 ATR beyond VWAP: none
- Stretch: skip all setups > 3.5 ATR beyond VWAP on the trade side: none
- Stretch: skip FLIP setups > 3.5 ATR beyond VWAP: none
- Stretch: skip all setups > 4.0 ATR beyond VWAP on the trade side: none
- Stretch: skip FLIP setups > 4.0 ATR beyond VWAP: none
- Flop skip, flip setups (EMA200/VWAP, 70 %) = ats_flg: none
- Flop skip, flip setups, + pivots: none
- Flop skip, ALL setups (EMA200/VWAP): none
- Flop skip, ALL setups, + pivots: none
- Flip count: skip when >= 2 HTF flips in last 4 15m candles: none
- Flip count: skip when >= 3 HTF flips in last 4 15m candles: none
- Flip count: skip when >= 3 HTF flips in last 8 15m candles: none
- Flip count: skip when >= 4 HTF flips in last 8 15m candles: none
- Flip count: skip when >= 4 HTF flips in last 16 15m candles: none
- Flip count: skip when >= 5 HTF flips in last 16 15m candles: none