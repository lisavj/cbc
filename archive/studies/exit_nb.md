# Exit ideas beyond the time-based TP cut — Fri 11/06/2026 10:43

Exit ideas beyond the plain time-based TP cut -- 11/06/2026, MES 3m + MGC 3m (live settings, replay Jan 5 -> now).
 1 VOL: time-based TP cut (after X min TP1 -> Y %) ONLY while ATR / ATR(100) >= r (high-volatility regime) -- X 21 / Y 70 %
 2 LOCK: before TP1, once the best move (MFE) reaches a x TP1, raise the stop to Entry + b x TP1 (profit lock)
 3 STALL: before TP1, after MFE >= 50 % of TP1, exit at the close when no new best price for N candles
 4 LOSER: before TP1, exit at the close after X min when the trade is still against Entry by >= k x ATR
All other exits unchanged. z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds.

## MES 3m — current exits net -8 (1670 setups)

| Idea | Variant | Net | Δ | z | Δ by third | Last 4 wk Δ | Setups changed | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 VOL | MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.5 | +123 | +131 | +2.1 | +101 / +2 / +27 | +11.7 | 72 | robust |
| 1 VOL | MES: cut to 70 % after 18 min while ATR/ATR100 >= 1.5 | +150 | +157 | +2.3 | +115 / +2 / +40 | +10.3 | 83 | robust |
| 1 VOL | MES: cut to 70 % after 24 min while ATR/ATR100 >= 1.5 | +122 | +130 | +2.1 | +106 / -3 / +27 | +11.7 | 68 | noise |
| 1 VOL | MES: cut to 65 % after 21 min while ATR/ATR100 >= 1.5 | +117 | +125 | +1.9 | +104 / -8 / +29 | +6.6 | 76 | noise |
| 1 VOL | MES: cut to 75 % after 21 min while ATR/ATR100 >= 1.5 | +108 | +116 | +1.9 | +114 / -23 / +25 | +16.8 | 69 | noise |
| 1 VOL | MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.4 | +136 | +144 | +1.9 | +103 / +14 / +27 | +11.7 | 100 | promising |
| 1 VOL | MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.6 | +113 | +120 | +2.2 | +98 / +16 / +7 | +8.9 | 52 | robust |
| 1 VOL | MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.8 | +60 | +68 | +1.6 | +19 / +40 / +9 | +5.8 | 30 | promising |
| 1 VOL | MES: cut to 70 % after 30 min while ATR/ATR100 >= 1.5 | +53 | +60 | +1.1 | +84 / -35 / +11 | +14.6 | 56 | noise |
| 1 VOL | MES: cut to 70 % after 15 min while ATR/ATR100 >= 1.5 | +152 | +160 | +2.2 | +111 / +14 / +35 | +5.2 | 93 | robust |
| 2 LOCK | MGC: MFE >= 75 % -> stop Entry + 50 % | +99 | +107 | +0.6 | -7 / +122 / -9 | -43.7 | 581 | noise |
| 2 LOCK | MGC: MFE >= 70 % -> stop Entry + 50 % | +158 | +166 | +0.8 | -10 / +195 / -19 | -70.1 | 680 | noise |
| 2 LOCK | MGC: MFE >= 80 % -> stop Entry + 50 % | -43 | -35 | -0.2 | +15 / +37 / -87 | -59.0 | 479 | worse |
| 2 LOCK | MGC: MFE >= 75 % -> stop Entry + 45 % | +74 | +82 | +0.5 | -19 / +112 / -11 | -48.3 | 541 | noise |
| 2 LOCK | MGC: MFE >= 75 % -> stop Entry + 55 % | +158 | +166 | +0.9 | -2 / +163 / +5 | -47.4 | 612 | noise |
| 2 LOCK | MGC: MFE >= 70 % -> stop Entry + 45 % | +86 | +94 | +0.5 | -33 / +172 / -45 | -75.3 | 641 | noise |
| 2 LOCK | MGC: MFE >= 80 % -> stop Entry + 55 % | +15 | +22 | +0.1 | +24 / +70 / -72 | -64.4 | 494 | noise |
| 2 LOCK | MGC: MFE >= 65 % -> stop Entry + 40 % | +159 | +167 | +0.8 | -21 / +221 / -33 | -67.0 | 705 | noise |
| 2 LOCK | MGC: MFE >= 85 % -> stop Entry + 60 % | +80 | +88 | +0.6 | +40 / +71 / -23 | -36.9 | 389 | noise |

## MGC 3m — current exits net +240 (1704 setups)

| Idea | Variant | Net | Δ | z | Δ by third | Last 4 wk Δ | Setups changed | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 VOL | MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.5 | +245 | +5 | +0.2 | +3 / -4 / +6 | +6.9 | 15 | noise |
| 1 VOL | MES: cut to 70 % after 18 min while ATR/ATR100 >= 1.5 | +245 | +5 | +0.2 | +3 / -4 / +6 | +6.8 | 15 | noise |
| 1 VOL | MES: cut to 70 % after 24 min while ATR/ATR100 >= 1.5 | +246 | +6 | +0.3 | +4 / -4 / +5 | +7.2 | 10 | noise |
| 1 VOL | MES: cut to 65 % after 21 min while ATR/ATR100 >= 1.5 | +247 | +7 | +0.3 | +7 / -4 / +5 | +6.9 | 17 | noise |
| 1 VOL | MES: cut to 75 % after 21 min while ATR/ATR100 >= 1.5 | +244 | +4 | +0.2 | -1 / -3 / +8 | +7.1 | 13 | noise |
| 1 VOL | MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.4 | +242 | +2 | +0.1 | +3 / -7 / +6 | +6.9 | 20 | noise |
| 1 VOL | MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.6 | +232 | -8 | -0.6 | +0 / -3 / -5 | +0.0 | 6 | worse |
| 1 VOL | MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.8 | +240 | +0 | +0.0 | +0 / +0 / +0 | +0.0 | 1 | noise |
| 1 VOL | MES: cut to 70 % after 30 min while ATR/ATR100 >= 1.5 | +242 | +2 | +0.2 | +0 / -3 / +5 | +0.0 | 4 | noise |
| 1 VOL | MES: cut to 70 % after 15 min while ATR/ATR100 >= 1.5 | +243 | +3 | +0.1 | +3 / +1 / -0 | +3.7 | 20 | noise |
| 2 LOCK | MGC: MFE >= 75 % -> stop Entry + 50 % | +385 | +145 | +1.2 | +94 / +39 / +13 | +9.7 | 493 | promising |
| 2 LOCK | MGC: MFE >= 70 % -> stop Entry + 50 % | +429 | +188 | +1.4 | +116 / +75 / -3 | +12.9 | 570 | noise |
| 2 LOCK | MGC: MFE >= 80 % -> stop Entry + 50 % | +331 | +91 | +0.8 | +73 / +39 / -21 | +0.1 | 402 | noise |
| 2 LOCK | MGC: MFE >= 75 % -> stop Entry + 45 % | +320 | +80 | +0.6 | +73 / +13 / -6 | +2.8 | 482 | noise |
| 2 LOCK | MGC: MFE >= 75 % -> stop Entry + 55 % | +449 | +209 | +1.6 | +119 / +62 / +28 | +18.1 | 507 | promising |
| 2 LOCK | MGC: MFE >= 70 % -> stop Entry + 45 % | +342 | +102 | +0.8 | +86 / +42 / -26 | +5.8 | 560 | noise |
| 2 LOCK | MGC: MFE >= 80 % -> stop Entry + 55 % | +387 | +147 | +1.3 | +90 / +62 / -5 | +12.5 | 410 | noise |
| 2 LOCK | MGC: MFE >= 65 % -> stop Entry + 40 % | +370 | +130 | +0.9 | +112 / +36 / -19 | -4.8 | 624 | noise |
| 2 LOCK | MGC: MFE >= 85 % -> stop Entry + 60 % | +385 | +145 | +1.5 | +65 / +80 / +0 | +11.4 | 299 | promising |

## Candidates (robust / promising)

- MES 3m MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.5: +131, z +2.1, thirds +101 / +2 / +27, last 4 wk +11.7 (robust)
- MES 3m MES: cut to 70 % after 18 min while ATR/ATR100 >= 1.5: +157, z +2.3, thirds +115 / +2 / +40, last 4 wk +10.3 (robust)
- MES 3m MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.4: +144, z +1.9, thirds +103 / +14 / +27, last 4 wk +11.7 (promising)
- MES 3m MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.6: +120, z +2.2, thirds +98 / +16 / +7, last 4 wk +8.9 (robust)
- MES 3m MES: cut to 70 % after 21 min while ATR/ATR100 >= 1.8: +68, z +1.6, thirds +19 / +40 / +9, last 4 wk +5.8 (promising)
- MES 3m MES: cut to 70 % after 15 min while ATR/ATR100 >= 1.5: +160, z +2.2, thirds +111 / +14 / +35, last 4 wk +5.2 (robust)
- MGC 3m MGC: MFE >= 75 % -> stop Entry + 50 %: +145, z +1.2, thirds +94 / +39 / +13, last 4 wk +9.7 (promising)
- MGC 3m MGC: MFE >= 75 % -> stop Entry + 55 %: +209, z +1.6, thirds +119 / +62 / +28, last 4 wk +18.1 (promising)
- MGC 3m MGC: MFE >= 85 % -> stop Entry + 60 %: +145, z +1.5, thirds +65 / +80 / +0, last 4 wk +11.4 (promising)
