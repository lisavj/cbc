# Exit ideas beyond the time-based TP cut — Fri 11/06/2026 10:42

Exit ideas beyond the plain time-based TP cut -- 11/06/2026, MES 3m + MGC 3m (live settings, replay Jan 5 -> now).
 1 VOL: time-based TP cut (after X min TP1 -> Y %) ONLY while ATR / ATR(100) >= r (high-volatility regime) -- X 21 / Y 70 %
 2 LOCK: before TP1, once the best move (MFE) reaches a x TP1, raise the stop to Entry + b x TP1 (profit lock)
 3 STALL: before TP1, after MFE >= 50 % of TP1, exit at the close when no new best price for N candles
 4 LOSER: before TP1, exit at the close after X min when the trade is still against Entry by >= k x ATR
All other exits unchanged. z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds.

## MES 3m — current exits net -8 (1670 setups)

| Idea | Variant | Net | Δ | z | Δ by third | Last 4 wk Δ | Setups changed | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 VOL | cut to 70 % after 21 min while ATR/ATR100 >= 0.0 | +205 | +213 | +1.2 | +102 / +111 / -0 | -53.2 | 571 | noise |
| 1 VOL | cut to 70 % after 21 min while ATR/ATR100 >= 1.0 | +128 | +135 | +1.1 | +121 / +42 / -28 | -45.8 | 279 | noise |
| 1 VOL | cut to 70 % after 21 min while ATR/ATR100 >= 1.2 | +92 | +100 | +1.0 | +101 / +10 / -11 | -19.7 | 165 | noise |
| 1 VOL | cut to 70 % after 21 min while ATR/ATR100 >= 1.5 | +123 | +131 | +2.1 | +101 / +2 / +27 | +11.7 | 72 | robust |
| 1 VOL | cut to 70 % after 24 min while ATR/ATR100 >= 1.2 | +105 | +113 | +1.2 | +109 / +11 / -6 | -19.7 | 155 | noise |
| 2 LOCK | MFE >= 50 % of TP1 -> stop to Entry + 0 % | -62 | -54 | -0.3 | -77 / +124 / -101 | -59.4 | 619 | worse |
| 2 LOCK | MFE >= 50 % of TP1 -> stop to Entry + 25 % | +122 | +130 | +0.6 | -46 / +232 / -56 | -115.1 | 822 | noise |
| 2 LOCK | MFE >= 75 % of TP1 -> stop to Entry + 0 % | -7 | +1 | +0.0 | -10 / +71 / -60 | -41.5 | 288 | noise |
| 2 LOCK | MFE >= 75 % of TP1 -> stop to Entry + 25 % | -20 | -12 | -0.1 | -31 / +70 / -51 | -53.4 | 418 | worse |
| 2 LOCK | MFE >= 75 % of TP1 -> stop to Entry + 50 % | +99 | +107 | +0.6 | -7 / +122 / -9 | -43.7 | 581 | noise |
| 2 LOCK | MFE >= 90 % of TP1 -> stop to Entry + 50 % | -5 | +3 | +0.0 | +16 / +12 / -25 | -2.6 | 242 | noise |
| 3 STALL | MFE >= 50 % TP1, no new best for 3 candles -> exit | -7 | +1 | +0.0 | +22 / -13 / -8 | -51.4 | 601 | noise |
| 3 STALL | MFE >= 50 % TP1, no new best for 5 candles -> exit | -69 | -61 | -0.4 | -17 / +28 / -73 | -70.7 | 464 | worse |
| 3 STALL | MFE >= 50 % TP1, no new best for 8 candles -> exit | -55 | -47 | -0.4 | -27 / +4 / -24 | -24.6 | 272 | worse |
| 3 STALL | MFE >= 50 % TP1, no new best for 12 candles -> exit | -46 | -38 | -0.4 | -41 / -7 / +10 | +1.0 | 145 | worse |
| 4 LOSER | after 15 min, still >= 0.5 ATR against -> exit | +34 | +42 | +0.2 | +72 / +42 / -72 | -130.6 | 676 | noise |
| 4 LOSER | after 30 min, still >= 0.0 ATR against -> exit | -83 | -75 | -0.4 | -2 / +23 / -96 | -101.3 | 494 | worse |
| 4 LOSER | after 30 min, still >= 0.5 ATR against -> exit | -38 | -30 | -0.2 | +35 / +22 / -87 | -87.5 | 360 | worse |
| 4 LOSER | after 45 min, still >= 0.0 ATR against -> exit | -98 | -90 | -0.8 | -15 / -2 / -73 | -50.3 | 257 | worse |
| 4 LOSER | after 45 min, still >= 0.5 ATR against -> exit | +3 | +11 | +0.1 | +25 / +36 / -50 | -60.0 | 194 | noise |
| 4 LOSER | after 60 min, still >= 0.5 ATR against -> exit | -20 | -12 | -0.2 | +14 / +4 / -29 | -17.3 | 99 | worse |

## MGC 3m — current exits net +240 (1704 setups)

| Idea | Variant | Net | Δ | z | Δ by third | Last 4 wk Δ | Setups changed | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 VOL | cut to 70 % after 21 min while ATR/ATR100 >= 0.0 | +251 | +11 | +0.1 | +10 / +6 / -5 | +8.8 | 229 | noise |
| 1 VOL | cut to 70 % after 21 min while ATR/ATR100 >= 1.0 | +236 | -4 | -0.1 | -4 / +18 / -18 | -1.7 | 98 | worse |
| 1 VOL | cut to 70 % after 21 min while ATR/ATR100 >= 1.2 | +247 | +7 | +0.2 | +3 / +3 / +0 | +7.3 | 43 | noise |
| 1 VOL | cut to 70 % after 21 min while ATR/ATR100 >= 1.5 | +245 | +5 | +0.2 | +3 / -4 / +6 | +6.9 | 15 | noise |
| 1 VOL | cut to 70 % after 24 min while ATR/ATR100 >= 1.2 | +246 | +6 | +0.2 | +9 / -14 / +11 | +7.6 | 30 | noise |
| 2 LOCK | MFE >= 50 % of TP1 -> stop to Entry + 0 % | +188 | -52 | -0.4 | +27 / +5 / -83 | +5.0 | 586 | worse |
| 2 LOCK | MFE >= 50 % of TP1 -> stop to Entry + 25 % | +421 | +181 | +1.1 | +165 / +58 / -42 | +30.3 | 809 | noise |
| 2 LOCK | MFE >= 75 % of TP1 -> stop to Entry + 0 % | +216 | -24 | -0.3 | +31 / -29 / -26 | -30.2 | 237 | worse |
| 2 LOCK | MFE >= 75 % of TP1 -> stop to Entry + 25 % | +265 | +25 | +0.2 | +60 / -9 / -26 | -12.7 | 410 | noise |
| 2 LOCK | MFE >= 75 % of TP1 -> stop to Entry + 50 % | +385 | +145 | +1.2 | +94 / +39 / +13 | +9.7 | 493 | promising |
| 2 LOCK | MFE >= 90 % of TP1 -> stop to Entry + 50 % | +276 | +35 | +0.5 | +22 / +34 / -20 | +11.0 | 192 | noise |
| 3 STALL | MFE >= 50 % TP1, no new best for 3 candles -> exit | +297 | +57 | +0.5 | +79 / -6 / -15 | -1.9 | 344 | noise |
| 3 STALL | MFE >= 50 % TP1, no new best for 5 candles -> exit | +236 | -5 | -0.1 | +49 / -34 / -19 | -5.7 | 215 | worse |
| 3 STALL | MFE >= 50 % TP1, no new best for 8 candles -> exit | +278 | +38 | +0.7 | +27 / +17 / -6 | +16.5 | 101 | noise |
| 3 STALL | MFE >= 50 % TP1, no new best for 12 candles -> exit | +247 | +7 | +0.2 | +22 / +3 / -18 | +12.8 | 42 | noise |
| 4 LOSER | after 15 min, still >= 0.5 ATR against -> exit | +342 | +102 | +1.0 | +65 / +5 / +31 | +8.0 | 335 | noise |
| 4 LOSER | after 30 min, still >= 0.0 ATR against -> exit | +233 | -7 | -0.1 | +28 / -16 / -20 | -4.3 | 171 | worse |
| 4 LOSER | after 30 min, still >= 0.5 ATR against -> exit | +204 | -36 | -0.6 | -2 / -7 / -27 | +2.8 | 121 | worse |
| 4 LOSER | after 45 min, still >= 0.0 ATR against -> exit | +212 | -28 | -0.6 | +7 / -31 / -5 | +17.5 | 69 | worse |
| 4 LOSER | after 45 min, still >= 0.5 ATR against -> exit | +224 | -16 | -0.4 | -13 / -5 / +3 | +11.3 | 49 | worse |
| 4 LOSER | after 60 min, still >= 0.5 ATR against -> exit | +239 | -1 | -0.0 | +6 / +4 / -11 | +4.7 | 19 | worse |

## Candidates (robust / promising)

- MES 3m cut to 70 % after 21 min while ATR/ATR100 >= 1.5: +131, z +2.1, thirds +101 / +2 / +27, last 4 wk +11.7 (robust)
- MGC 3m MFE >= 75 % of TP1 -> stop to Entry + 50 %: +145, z +1.2, thirds +94 / +39 / +13, last 4 wk +9.7 (promising)
