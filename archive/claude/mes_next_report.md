MES 3m next ideas -- HTF CBC Flip and the April-July stretch -- 11/14/2026.
BASELINE = current MES 3m filters (ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR) + "Block in chop: HTF EMA20 slope below 0.3 ATR"
(|15m EMA20 now - 12 bars ago| / ATR). Replay Jan 5 -> now, CBC engine setups, live exits (SL1 3 ATR min 5, TP1 1.75 ATR, 100 % at TP1),
net after 0.50 cost. One change at a time on top of the baseline; entry filters can change later setups (one at a time, cooldown).
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, better in all three thirds and last 4 wk >= 0; promising = z >= 1 and all thirds.

## Baseline (current + slope 0.3): 1242 setups, net -107, avg -0.09, win 50 %, thirds +240 / -431 / +84, last 4 wk +114, flips 170 / -125, max DD 624

## Candidates

- 4a. Flip setups exit: flip + SL1 (no TP): +245 (net +138), z +3.7, thirds +9 / +22 / +213, last 4 wk +41, 1242 setups, max DD 476 (robust)

## All variants

| Change | Setups | Net | Avg | Δ | z | Δ by third | Δ last 4 wk | Flips n / net | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1. HTF CBC Flip trigger OFF | 1147 | -55 | -0.05 | +52 | +0.5 | +42 / +66 / -55 | -17 | 0 / +0 | 504 | noise |
| 2a. Flips: skip when the flip is a flop (EMA200 / VWAP, 70 %) | 1237 | -98 | -0.08 | +9 | +0.4 | -5 / +0 / +15 | +0 | 163 / -108 | 612 | noise |
| 2a. All setups: skip while the current flip is a flop | 893 | -25 | -0.03 | +82 | +0.6 | -45 / +82 / +45 | +5 | 163 / -108 | 492 | noise |
| 2b. Flips: EMA200 slope must agree (now vs 5 bars ago) | 1241 | -109 | -0.09 | -2 | -0.2 | +0 / +0 / -2 | +0 | 169 / -126 | 624 | worse |
| 2c. Flip min ER 0.30 | 1218 | -103 | -0.08 | +4 | +0.1 | +7 / +30 / -33 | -22 | 128 / -112 | 594 | noise |
| 2c. Flip min ER 0.35 | 1205 | -106 | -0.09 | +1 | +0.0 | +24 / +25 / -47 | -25 | 101 / -92 | 587 | noise |
| 2d. Flips: close beyond VWAP and EMA200 by 2 pts | 1240 | -100 | -0.08 | +7 | +0.7 | +0 / +0 / +7 | +0 | 168 / -118 | 615 | noise |
| 2d. Flips: close beyond VWAP and EMA200 by 3 pts | 1237 | -104 | -0.08 | +3 | +0.2 | -9 / -0 / +13 | +0 | 164 / -123 | 615 | noise |
| 3a. Only the first 1 signal after the HTF flip | 970 | -165 | -0.17 | -58 | -0.5 | -103 / +27 / +18 | -30 | 170 / -125 | 602 | worse |
| 3b. Only the first 2 signals after the HTF flip | 1110 | -134 | -0.12 | -27 | -0.3 | -65 / +13 / +25 | -9 | 170 / -125 | 598 | worse |
| 3c. Only the first 3 signals after the HTF flip | 1182 | -125 | -0.11 | -18 | -0.3 | -37 / -7 / +25 | -6 | 170 / -125 | 622 | worse |
| 3d. Skip the flip itself; first pierce after it only | 911 | -117 | -0.13 | -10 | -0.1 | -39 / +85 / -55 | -59 | 0 / +0 | 497 | worse |
| 4a. Flip setups exit: flip + SL1 (no TP) | 1242 | +138 | +0.11 | +245 | +3.7 | +9 / +22 / +213 | +41 | 170 / +120 | 476 | robust |
| 4b. Flip setups exit: TP1 2.5 ATR | 1242 | -42 | -0.03 | +65 | +1.0 | +5 / +4 / +57 | +12 | 170 / -59 | 615 | noise |
| 4c. Flip setups exit: TP1 3.5 ATR | 1242 | -61 | -0.05 | +46 | +0.7 | -5 / -6 / +57 | +5 | 170 / -78 | 612 | noise |
| 5a. Flips only when the 1H CBC agrees | 1228 | -92 | -0.07 | +15 | +0.4 | +19 / +9 / -14 | +1 | 145 / -111 | 607 | noise |
| 5b. All setups only when the 1H CBC agrees | 1070 | -247 | -0.23 | -140 | -1.5 | -12 / -7 / -121 | -42 | 145 / -111 | 618 | worse |
| 7a. Daily trend: long above / short below yesterday's 5-day EMA | 854 | +27 | +0.03 | +134 | +1.0 | -100 / +274 / -40 | -13 | 123 / -54 | 332 | noise |
| 7b. Daily trend: no shorts above the 5-day EMA (bot rule) | 1031 | +61 | +0.06 | +168 | +1.6 | -17 / +198 / -13 | -3 | 144 / -12 | 426 | noise |
| 7c. Long above / short below yesterday's close | 1068 | -118 | -0.11 | -10 | -0.1 | -89 / +116 / -37 | -15 | 157 / -80 | 463 | worse |
| 8a. Skip while ATR > 1.3 x its 20-day average | 959 | -101 | -0.11 | +6 | +0.1 | -61 / +216 / -149 | -130 | 133 / -87 | 345 | noise |
| 8b. Skip while ATR > 1.6 x its 20-day average | 1083 | -31 | -0.03 | +76 | +0.8 | -40 / +225 / -109 | -102 | 151 / -107 | 364 | noise |
| 10a. Longs only | 676 | +47 | +0.07 | +154 | +0.9 | -89 / +333 / -91 | -135 | 91 / +3 | 193 | noise |
| 10b. Shorts only | 566 | -154 | -0.27 | -47 | -0.3 | -151 / +98 / +6 | +21 | 79 / -128 | 489 | worse |
| 11. + Environment EMA200 vs VWAP (v10.97 checkbox) | 564 | +90 | +0.16 | +197 | +1.1 | -51 / +307 / -59 | -40 | 73 / +10 | 256 | noise |
| 1 + 11. Flip OFF + EMA200 vs VWAP | 522 | +84 | +0.16 | +191 | +1.0 | -54 / +317 / -72 | -50 | 0 / +0 | 240 | noise |

## Diagnostics (baseline)

### Baseline by month

| Group | Setups | Net | Avg | Win % | Flip net | Longs net | Shorts net | Avg ATR |
|---|---|---|---|---|---|---|---|---|
| Jan | 89 | -19 | -0.21 | 47 % | -39 | +1 | -19 | 3.0 |
| Feb | 99 | +150 | +1.52 | 57 % | +42 | +97 | +54 | 4.0 |
| Mar | 121 | +49 | +0.41 | 51 % | -31 | +7 | +42 | 5.8 |
| Apr | 131 | +50 | +0.38 | 53 % | -5 | +68 | -18 | 3.4 |
| May | 124 | -108 | -0.87 | 44 % | -63 | -59 | -49 | 3.2 |
| Jun | 99 | -227 | -2.30 | 38 % | -26 | -103 | -124 | 4.3 |
| Jul | 124 | -86 | -0.69 | 47 % | -43 | +44 | -130 | 3.7 |
| Aug | 137 | -171 | -1.25 | 42 % | -66 | -42 | -129 | 2.6 |
| Sep | 135 | +80 | +0.59 | 58 % | +60 | +24 | +56 | 3.0 |
| Oct | 128 | +89 | +0.70 | 58 % | +19 | -8 | +97 | 3.2 |
| Nov | 55 | +86 | +1.56 | 55 % | +26 | +19 | +67 | 5.8 |

### Baseline by hour (ET, candle start)

| Group | Setups | Net | Avg | Win % | Flip net | Longs net | Shorts net | Avg ATR |
|---|---|---|---|---|---|---|---|---|
| 18:00 | 28 | -35 | -1.24 | 43 % | -47 | +22 | -57 | 3.4 |
| 19:00 | 57 | +49 | +0.85 | 60 % | +5 | +37 | +12 | 2.6 |
| 20:00 | 26 | -21 | -0.82 | 46 % | -6 | +0 | -22 | 3.1 |
| 21:00 | 57 | +43 | +0.75 | 51 % | -6 | +8 | +35 | 2.9 |
| 22:00 | 37 | -10 | -0.27 | 49 % | -12 | -4 | -6 | 2.4 |
| 23:00 | 61 | -3 | -0.05 | 52 % | -20 | -10 | +7 | 2.2 |
| 00:00 | 72 | +49 | +0.69 | 58 % | -8 | +0 | +49 | 2.2 |
| 01:00 | 65 | -16 | -0.25 | 52 % | -6 | -25 | +9 | 2.3 |
| 02:00 | 80 | -35 | -0.44 | 51 % | -10 | -40 | +5 | 2.4 |
| 03:00 | 36 | -25 | -0.70 | 53 % | -6 | -12 | -13 | 2.7 |
| 04:00 | 58 | +15 | +0.26 | 52 % | +2 | +29 | -14 | 3.1 |
| 05:00 | 47 | -25 | -0.53 | 36 % | -5 | -25 | -0 | 3.0 |
| 06:00 | 64 | -6 | -0.10 | 52 % | -16 | +8 | -15 | 3.1 |
| 07:00 | 47 | -30 | -0.63 | 47 % | -5 | -42 | +13 | 3.6 |
| 08:00 | 78 | -24 | -0.30 | 49 % | +20 | -16 | -7 | 3.7 |
| 09:00 | 40 | +37 | +0.92 | 60 % | -6 | +65 | -28 | 4.4 |
| 10:00 | 69 | +29 | +0.42 | 51 % | -5 | +140 | -111 | 7.2 |
| 11:00 | 66 | +77 | +1.16 | 55 % | +51 | -8 | +85 | 6.6 |
| 12:00 | 65 | -1 | -0.01 | 49 % | -24 | +10 | -11 | 5.1 |
| 13:00 | 64 | -181 | -2.82 | 33 % | -11 | -105 | -76 | 4.7 |
| 14:00 | 55 | -43 | -0.77 | 42 % | -6 | -9 | -33 | 4.2 |
| 15:00 | 70 | +49 | +0.70 | 53 % | -3 | +23 | +26 | 4.8 |

### Baseline by session

| Group | Setups | Net | Avg | Win % | Flip net | Longs net | Shorts net | Avg ATR |
|---|---|---|---|---|---|---|---|---|
| RTH 9:30-16:00 | 389 | -69 | -0.18 | 47 % | +1 | +51 | -120 | 5.5 |
| Overnight | 853 | -38 | -0.04 | 51 % | -126 | -4 | -34 | 2.9 |

### Baseline by trigger and direction

| Group | Setups | Net | Avg | Win % | Flip net | Longs net | Shorts net | Avg ATR |
|---|---|---|---|---|---|---|---|---|
| HTF CBC Flip long | 91 | +3 | +0.04 | 58 % | +3 | +3 | +0 | 2.9 |
| HTF CBC Flip short | 79 | -128 | -1.62 | 49 % | -128 | +0 | -128 | 4.2 |
| LTF EMA20 Pierce long | 437 | +25 | +0.06 | 49 % | +0 | +25 | +0 | 3.3 |
| LTF EMA20 Pierce short | 374 | -75 | -0.20 | 51 % | +0 | +0 | -75 | 4.2 |
| HTF EMA9 Pierce long | 126 | -6 | -0.05 | 44 % | +0 | -6 | +0 | 3.6 |
| HTF EMA9 Pierce short | 86 | -18 | -0.21 | 45 % | +0 | +0 | -18 | 3.9 |
| HTF EMA20 Pierce long | 22 | +25 | +1.12 | 64 % | +0 | +25 | +0 | 3.3 |
| HTF EMA20 Pierce short | 27 | +68 | +2.51 | 63 % | +0 | +0 | +68 | 3.9 |

### Market by month (daily candles)

| Month | Days | Avg daily range | Trend days (body > 60 % of range) | Month change |
|---|---|---|---|---|
| Jan | 20 | 71 | 15 % | +49 |
| Feb | 20 | 101 | 35 % | -64 |
| Mar | 23 | 136 | 30 % | -212 |
| Apr | 22 | 86 | 45 % | +631 |
| May | 21 | 75 | 43 % | +333 |
| Jun | 22 | 113 | 41 % | -78 |
| Jul | 22 | 90 | 36 % | -33 |
| Aug | 22 | 64 | 41 % | +98 |
| Sep | 22 | 75 | 41 % | +79 |
| Oct | 21 | 83 | 38 % | -110 |
| Nov | 10 | 172 | 30 % | -66 |