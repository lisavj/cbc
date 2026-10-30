# CBC order-block setup study -- 2026-10-29 17:08 ET

Question: do CBC Trade Setups whose entry candle sits inside an order block do better? Alerts stored: 19566 (since 2026-10-19).
OB definitions: **A** = OB v1.08 defaults (internal, length 5, Leg swings, Lowest in leg, mitigation Close, Keep newest, last 5/5); **B** = CBC ⑨ Lux-style (ESLib2: length 5, Close, chart TF, last 5, block appears the bar after the break, Hide Overlap removes the older block). OB state = after the bar before the setup candle (no look-ahead). Buckets: ALIGNED (long traded into an active OB+ and closed at/above its bottom; short mirrored), OPPOSING (long into an OB- and closed at/below its top), NEAR (within 0.5 ATR of an aligned OB), NONE. ✱ = net positive in both chronological halves (half nets shown last). MFE/MAE = Best / Worst from the Setup Ended alert in ATR(14).

**Since last run:** vs 2026-10-28 17:08 ET: setups (ALIGNED+NONE+OPPOSING, OB v1.08) MES 3m 59->66, MGC 3m 35->41, MNQ 3m 59->70, MES 2m 69->72, MGC 2m 63->74, MNQ 2m 74->92, MES 5m 32->36, MGC 5m 20->20, MNQ 5m 22->28.

## MES 3m

Setups with results: 70 (skipped 0 without bars) · net -66.7 pts · halves split at 10/23 06:45 · A/B bucket agreement 65/70 (93%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 7 | 43% | -1.16 | -8.1 | 0.63 | 1.40 / -1.27 | +0.5 / -8.6 |
| NEAR | 4 | 25% | -1.61 | -6.4 | 0.49 | 1.27 / -1.92 | -4.1 / -2.3 |
| NONE | 42 | 38% | -1.33 | -56.0 | 0.57 | 1.29 / -1.13 | -26.7 / -29.4 |
| OPPOSING | 17 | 47% | +0.23 | +3.9 | 1.09 | 2.07 / -1.12 | -9.4 / +13.3 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 6 | 33% | -2.20 | -13.2 | 0.39 | 1.22 / -1.42 | -4.6 / -8.6 |
| NEAR | 5 | 20% | -2.11 | -10.5 | 0.37 | 1.27 / -1.82 | -4.1 / -6.4 |
| NONE | 46 | 41% | -0.93 | -42.6 | 0.68 | 1.41 / -1.09 | -18.1 / -24.5 |
| OPPOSING | 13 | 46% | -0.02 | -0.3 | 0.99 | 1.97 / -1.15 | -12.9 / +12.6 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (11) | 0 | 7 · 43% · -1.01 | 0 | 8 · 50% · -0.28 |
| LTF EMA20 Pierce/Touch (41) | 4 · 25% · -3.03 | 24 · 38% · -1.40 | 3 · 0% · -5.73 | 27 · 41% · -0.93 |
| HTF EMA pierce (17) | 3 · 67% · +1.33 | 10 · 40% · -0.97 | 3 · 67% · +1.33 | 10 · 40% · -0.97 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 70 setups, 10 say In OB): replay A agrees 65 (93%), replay B 69 (99%).
OB v1.08 indicator alerts for MES1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 7 vs 42, Δavg +0.17 · CBC 6 vs 46, Δavg -1.27)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 17 vs 53, Δavg +1.56 · CBC 13 vs 57, Δavg +1.14)

## MGC 3m

Setups with results: 44 (skipped 0 without bars) · net -20.9 pts · halves split at 10/25 21:48 · A/B bucket agreement 40/44 (91%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 8 | 62% | +0.62 | +5.0 ✱ | 1.39 | 2.49 / -0.85 | +3.3 / +1.7 |
| NEAR | 3 | 33% | -1.73 | -5.2 | 0.44 | 0.58 / -1.00 | -3.6 / -1.6 |
| NONE | 19 | 42% | -0.18 | -3.4 | 0.92 | 1.43 / -1.09 | +15.0 / -18.3 |
| OPPOSING | 14 | 36% | -1.24 | -17.3 | 0.48 | 1.14 / -1.08 | -6.3 / -11.0 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 7 | 71% | +1.42 | +10.0 ✱ | 2.31 | 2.79 / -0.71 | +8.3 / +1.7 |
| NEAR | 3 | 33% | -1.73 | -5.2 | 0.44 | 0.58 / -1.00 | -3.6 / -1.6 |
| NONE | 22 | 45% | -0.16 | -3.6 | 0.93 | 1.42 / -1.03 | +15.6 / -19.2 |
| OPPOSING | 12 | 25% | -1.84 | -22.1 | 0.30 | 1.04 / -1.24 | -11.9 / -10.2 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (5) | 0 | 3 · 100% · +3.17 | 0 | 4 · 75% · +0.62 |
| LTF EMA20 Pierce/Touch (26) | 4 · 50% · +0.32 | 10 · 40% · +0.33 | 3 · 67% · +2.09 | 11 · 45% · +0.86 |
| HTF EMA pierce (12) | 4 · 75% · +0.92 | 5 · 20% · -1.85 | 4 · 75% · +0.92 | 6 · 33% · -1.44 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 44 setups, 7 say In OB): replay A agrees 41 (93%), replay B 43 (98%).
OB v1.08 indicator alerts for MGC1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 8 vs 19, Δavg +0.80 · CBC 7 vs 22, Δavg +1.59)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 14 vs 30, Δavg -1.12 · CBC 12 vs 32, Δavg -1.88)

## MNQ 3m

Setups with results: 71 (skipped 0 without bars) · net -662.5 pts · halves split at 10/26 10:03 · A/B bucket agreement 63/71 (89%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 5 | 20% | -15.60 | -78.0 | 0.29 | 0.81 / -1.46 | -30.0 / -48.0 |
| NEAR | 1 | 100% | +30.59 | +30.6 | ∞ | 2.60 / -0.11 | +30.6 / +0.0 |
| NONE | 41 | 24% | -12.70 | -520.5 | 0.41 | 1.06 / -1.24 | -240.5 / -280.0 |
| OPPOSING | 24 | 42% | -3.94 | -94.5 | 0.76 | 1.23 / -0.93 | +51.3 / -145.8 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 5 | 20% | -15.60 | -78.0 | 0.29 | 0.81 / -1.46 | -30.0 / -48.0 |
| NEAR | 4 | 50% | +0.65 | +2.6 | 1.04 | 1.55 / -0.78 | +62.6 / -60.0 |
| NONE | 46 | 24% | -13.12 | -603.5 | 0.39 | 1.01 / -1.25 | -295.5 / -308.0 |
| OPPOSING | 16 | 50% | +1.03 | +16.5 | 1.07 | 1.44 / -0.79 | +74.3 / -57.8 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (23) | 1 · 0% · -25.00 | 13 · 23% · -13.12 | 1 · 0% · -25.00 | 15 · 20% · -15.37 |
| LTF EMA20 Pierce/Touch (30) | 3 · 33% · -7.67 | 18 · 11% · -19.91 | 3 · 33% · -7.67 | 21 · 14% · -18.16 |
| HTF EMA pierce (18) | 1 · 0% · -30.00 | 10 · 50% · +0.85 | 1 · 0% · -30.00 | 10 · 50% · +0.85 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 71 setups, 11 say In OB): replay A agrees 65 (92%), replay B 71 (100%).
OB v1.08 indicator alerts for MNQ1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 5 vs 41, Δavg -2.90 · CBC 5 vs 46, Δavg -2.48)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 24 vs 47, Δavg +8.15 · CBC 16 vs 55, Δavg +13.37)

## MES 2m

Setups with results: 77 (skipped 0 without bars) · net -126.6 pts · halves split at 10/21 14:38 · A/B bucket agreement 69/77 (90%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 7 | 43% | +0.25 | +1.8 | 1.19 | 1.43 / -0.75 | +2.8 / -1.0 |
| NEAR | 5 | 40% | -1.44 | -7.2 | 0.39 | 1.44 / -1.61 | -2.2 / -5.0 |
| NONE | 40 | 32% | -2.18 | -87.3 | 0.40 | 1.66 / -1.56 | -41.9 / -45.4 |
| OPPOSING | 25 | 36% | -1.35 | -33.9 | 0.54 | 1.28 / -1.70 | -8.8 / -25.0 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 7 | 43% | +0.25 | +1.8 | 1.19 | 1.43 / -0.75 | +2.8 / -1.0 |
| NEAR | 5 | 60% | +0.03 | +0.2 | 1.02 | 2.02 / -0.98 | -2.2 / +2.4 |
| NONE | 47 | 30% | -2.23 | -104.8 | 0.38 | 1.55 / -1.59 | -47.8 / -57.0 |
| OPPOSING | 18 | 39% | -1.32 | -23.8 | 0.58 | 1.26 / -1.85 | -3.0 / -20.8 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (21) | 0 | 8 · 50% · -0.41 | 0 | 11 · 36% · -1.66 |
| LTF EMA20 Pierce/Touch (38) | 5 · 40% · +0.05 | 22 · 27% · -3.35 | 5 · 40% · +0.05 | 25 · 28% · -2.81 |
| HTF EMA pierce (17) | 2 · 50% · +0.75 | 9 · 33% · -0.26 | 2 · 50% · +0.75 | 10 · 30% · -0.82 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 77 setups, 10 say In OB): replay A agrees 71 (92%), replay B 77 (100%).
OB v1.08 indicator alerts for MES1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 7 vs 40, Δavg +2.44 · CBC 7 vs 47, Δavg +2.48)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 25 vs 52, Δavg +0.43 · CBC 18 vs 59, Δavg +0.42)

## MGC 2m

Setups with results: 81 (skipped 0 without bars) · net -35.7 pts · halves split at 10/26 07:26 · A/B bucket agreement 77/81 (95%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 7 | 14% | -3.52 | -24.6 | 0.11 | 0.94 / -1.80 | -13.7 / -11.0 |
| NEAR | 7 | 43% | +0.08 | +0.6 | 1.04 | 2.44 / -1.91 | +6.2 / -5.6 |
| NONE | 44 | 50% | -0.15 | -6.7 | 0.93 | 1.82 / -1.45 | -24.5 / +17.8 |
| OPPOSING | 23 | 57% | -0.22 | -5.0 | 0.90 | 2.36 / -1.36 | +15.4 / -20.3 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 7 | 14% | -3.52 | -24.6 | 0.11 | 0.94 / -1.80 | -13.7 / -11.0 |
| NEAR | 4 | 75% | +2.47 | +9.9 | 2.98 | 3.41 / -1.91 | +11.2 / -1.3 |
| NONE | 48 | 48% | -0.24 | -11.7 | 0.88 | 1.83 / -1.48 | -29.5 / +17.8 |
| OPPOSING | 22 | 55% | -0.42 | -9.2 | 0.81 | 2.27 / -1.35 | +15.4 / -24.6 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (22) | 2 · 0% · -5.26 | 9 · 67% · -0.03 | 2 · 0% · -5.26 | 12 · 58% · -0.03 |
| LTF EMA20 Pierce/Touch (47) | 2 · 0% · -3.30 | 31 · 45% · -0.34 | 2 · 0% · -3.30 | 32 · 44% · -0.49 |
| HTF EMA pierce (12) | 3 · 33% · -2.50 | 4 · 50% · +1.07 | 3 · 33% · -2.50 | 4 · 50% · +1.07 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 81 setups, 18 say In OB): replay A agrees 79 (98%), replay B 81 (100%).
OB v1.08 indicator alerts for MGC1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 7 vs 44, Δavg -3.37 · CBC 7 vs 48, Δavg -3.27)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 23 vs 58, Δavg +0.31 · CBC 22 vs 59, Δavg +0.03)

## MNQ 2m

Setups with results: 99 (skipped 0 without bars) · net -440.9 pts · halves split at 10/26 19:30 · A/B bucket agreement 91/99 (92%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 9 | 11% | -18.25 | -164.2 | 0.01 | 0.36 / -1.17 | -5.5 / -158.8 |
| NEAR | 7 | 43% | +2.27 | +15.9 | 1.18 | 1.21 / -1.29 | +48.1 / -32.2 |
| NONE | 58 | 43% | -1.31 | -76.3 | 0.91 | 1.74 / -1.10 | +101.0 / -177.2 |
| OPPOSING | 25 | 32% | -8.65 | -216.2 | 0.52 | 1.36 / -1.53 | -71.8 / -144.5 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 8 | 12% | -16.78 | -134.2 | 0.02 | 0.28 / -1.14 | -5.5 / -128.8 |
| NEAR | 8 | 38% | -4.08 | -32.6 | 0.73 | 0.85 / -1.46 | -0.4 / -32.2 |
| NONE | 64 | 41% | -2.57 | -164.4 | 0.84 | 1.70 / -1.12 | +100.1 / -264.5 |
| OPPOSING | 19 | 37% | -5.76 | -109.5 | 0.66 | 1.51 / -1.53 | -22.4 / -87.2 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (32) | 0 | 16 · 62% · +11.84 | 0 | 20 · 55% · +8.06 |
| LTF EMA20 Pierce/Touch (34) | 4 · 0% · -30.00 | 22 · 36% · -3.98 | 3 · 0% · -30.00 | 24 · 33% · -6.15 |
| HTF EMA pierce (31) | 4 · 0% · -11.69 | 19 · 37% · -7.80 | 4 · 0% · -11.69 | 19 · 37% · -7.80 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 99 setups, 18 say In OB): replay A agrees 95 (96%), replay B 99 (100%).
OB v1.08 indicator alerts for MNQ1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 9 vs 58, Δavg -16.94 · CBC 8 vs 64, Δavg -14.21)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 25 vs 74, Δavg -5.61 · CBC 19 vs 80, Δavg -1.62)

## MES 5m

Setups with results: 37 (skipped 0 without bars) · net -42.5 pts · halves split at 10/26 04:50 · A/B bucket agreement 36/37 (97%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 2 | 50% | -1.47 | -2.9 | 0.63 | 1.34 / -1.04 | -2.9 / +0.0 |
| NEAR | 1 | 100% | +4.32 | +4.3 | ∞ | 2.20 / -1.47 | +0.0 / +4.3 |
| NONE | 24 | 42% | -1.46 | -35.1 | 0.60 | 1.34 / -1.20 | -5.7 / -29.4 |
| OPPOSING | 10 | 50% | -0.88 | -8.8 | 0.74 | 1.07 / -1.05 | +5.5 / -14.4 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 2 | 50% | -1.47 | -2.9 | 0.63 | 1.34 / -1.04 | -2.9 / +0.0 |
| NEAR | 1 | 100% | +4.32 | +4.3 | ∞ | 2.20 / -1.47 | +0.0 / +4.3 |
| NONE | 25 | 44% | -1.21 | -30.3 | 0.65 | 1.34 / -1.16 | -0.9 / -29.4 |
| OPPOSING | 9 | 44% | -1.51 | -13.6 | 0.59 | 1.03 / -1.14 | +0.8 / -14.4 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (10) | 0 | 6 · 50% · -1.39 | 0 | 6 · 50% · -1.39 |
| LTF EMA20 Pierce/Touch (20) | 2 · 50% · -1.47 | 15 · 40% · -1.25 | 2 · 50% · -1.47 | 15 · 40% · -1.25 |
| HTF EMA pierce (6) | 0 | 2 · 50% · -1.08 | 0 | 3 · 67% · +0.88 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 37 setups, 4 say In OB): replay A agrees 36 (97%), replay B 37 (100%).
OB v1.08 indicator alerts for MES1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 2 vs 24, Δavg -0.01 · CBC 2 vs 25, Δavg -0.26)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 10 vs 27, Δavg +0.37 · CBC 9 vs 28, Δavg -0.48)

## MGC 5m

Setups with results: 21 (skipped 0 without bars) · net -2.9 pts · halves split at 10/26 03:35 · A/B bucket agreement 20/21 (95%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 1 | 0% | -7.00 | -7.0 | 0.00 | 0.33 / -1.38 | -7.0 / +0.0 |
| NEAR | 1 | 100% | +3.04 | +3.0 | ∞ | 1.88 / -0.54 | +0.0 / +3.0 |
| NONE | 16 | 44% | -0.17 | -2.7 | 0.93 | 1.43 / -1.09 | +7.7 / -10.3 |
| OPPOSING | 3 | 67% | +1.25 | +3.8 | 1.75 | 2.10 / -1.14 | +0.0 / +3.8 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 1 | 0% | -7.00 | -7.0 | 0.00 | 0.33 / -1.38 | -7.0 / +0.0 |
| NEAR | 0 | – | – | – | – | – | |
| NONE | 17 | 47% | +0.02 | +0.4 | 1.01 | 1.46 / -1.06 | +7.7 / -7.3 |
| OPPOSING | 3 | 67% | +1.25 | +3.8 | 1.75 | 2.10 / -1.14 | +0.0 / +3.8 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (6) | 0 | 4 · 50% · -0.31 | 0 | 5 · 60% · +0.36 |
| LTF EMA20 Pierce/Touch (10) | 1 · 0% · -7.00 | 7 · 14% · -2.39 | 1 · 0% · -7.00 | 7 · 14% · -2.39 |
| HTF EMA pierce (5) | 0 | 5 · 80% · +3.06 | 0 | 5 · 80% · +3.06 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 21 setups, 0 say In OB): replay A agrees 21 (100%), replay B 21 (100%).
OB v1.08 indicator alerts for MGC1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 1 vs 16, Δavg -6.83 · CBC 1 vs 17, Δavg -7.02)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 3 vs 18, Δavg +1.62 · CBC 3 vs 18, Δavg +1.62)

## MNQ 5m

Setups with results: 28 (skipped 0 without bars) · net +144.2 pts · halves split at 10/25 19:25 · A/B bucket agreement 26/28 (93%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 7 | 43% | -3.83 | -26.8 | 0.74 | 1.06 / -0.82 | +41.4 / -68.2 |
| NEAR | 0 | – | – | – | – | – | |
| NONE | 16 | 62% | +11.32 | +181.1 ✱ | 2.13 | 1.55 / -0.76 | +112.9 / +68.3 |
| OPPOSING | 5 | 40% | -2.02 | -10.1 | 0.86 | 1.13 / -0.77 | +17.2 / -27.4 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 7 | 43% | -3.83 | -26.8 | 0.74 | 1.06 / -0.82 | +41.4 / -68.2 |
| NEAR | 0 | – | – | – | – | – | |
| NONE | 18 | 56% | +7.58 | +136.4 ✱ | 1.67 | 1.49 / -0.79 | +98.1 / +38.3 |
| OPPOSING | 3 | 67% | +11.55 | +34.6 ✱ | 2.15 | 1.18 / -0.59 | +32.0 / +2.6 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| LTF EMA20 Pierce/Touch (12) | 2 · 100% · +35.72 | 9 · 44% · +0.47 | 2 · 100% · +35.72 | 10 · 40% · -1.05 |
| HTF EMA pierce (12) | 5 · 20% · -19.65 | 5 · 80% · +21.14 | 5 · 20% · -19.65 | 5 · 80% · +21.14 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 28 setups, 2 say In OB): replay A agrees 25 (89%), replay B 28 (100%).
OB v1.08 indicator alerts for MNQ1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 7 vs 16, Δavg -15.15 · CBC 7 vs 18, Δavg -11.41)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 5 vs 23, Δavg -8.73 · CBC 3 vs 25, Δavg +7.16)

## All cases pooled (info only -- decide per symbol + timeframe)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 53 | 34% | -5.76 | -305.0 | 0.34 | 1.21 / -1.14 | -19.1 / -285.9 |
| NEAR | 29 | 45% | +1.23 | +35.6 | 1.26 | 1.60 / -1.49 | +49.2 / -13.6 |
| NONE | 300 | 40% | -2.02 | -606.8 | 0.75 | 1.51 / -1.22 | +19.5 / -626.3 |
| OPPOSING | 146 | 42% | -2.59 | -378.1 | 0.68 | 1.53 / -1.27 | +2.6 / -380.7 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 50 | 34% | -5.50 | -275.1 | 0.36 | 1.20 / -1.14 | -19.2 / -255.9 |
| NEAR | 30 | 47% | -1.05 | -31.4 | 0.86 | 1.57 / -1.36 | +1.6 / -33.0 |
| NONE | 333 | 40% | -2.47 | -824.2 | 0.70 | 1.49 / -1.23 | -37.5 / -786.6 |
| OPPOSING | 115 | 44% | -1.08 | -123.7 | 0.84 | 1.58 / -1.30 | +107.3 / -231.0 |

A/B bucket agreement: 487/528 (92%). Points differ in size between symbols (MNQ >> MES > MGC), so pooled pts are dominated by MNQ.

## Summary (A buckets: n · win % · avg pts)

- MES 3m: ALIGNED 7 · 43% · -1.16 / NONE 42 · 38% · -1.33 / OPPOSING 17 · 47% · +0.23 (A; B ALIGNED 6 · 33% · -2.20, NONE 46 · 41% · -0.93) -> not enough evidence yet
- MGC 3m: ALIGNED 8 · 62% · +0.62 / NONE 19 · 42% · -0.18 / OPPOSING 14 · 36% · -1.24 (A; B ALIGNED 7 · 71% · +1.42, NONE 22 · 45% · -0.16) -> not enough evidence yet
- MNQ 3m: ALIGNED 5 · 20% · -15.60 / NONE 41 · 24% · -12.70 / OPPOSING 24 · 42% · -3.94 (A; B ALIGNED 5 · 20% · -15.60, NONE 46 · 24% · -13.12) -> not enough evidence yet
- MES 2m: ALIGNED 7 · 43% · +0.25 / NONE 40 · 32% · -2.18 / OPPOSING 25 · 36% · -1.35 (A; B ALIGNED 7 · 43% · +0.25, NONE 47 · 30% · -2.23) -> not enough evidence yet
- MGC 2m: ALIGNED 7 · 14% · -3.52 / NONE 44 · 50% · -0.15 / OPPOSING 23 · 57% · -0.22 (A; B ALIGNED 7 · 14% · -3.52, NONE 48 · 48% · -0.24) -> not enough evidence yet
- MNQ 2m: ALIGNED 9 · 11% · -18.25 / NONE 58 · 43% · -1.31 / OPPOSING 25 · 32% · -8.65 (A; B ALIGNED 8 · 12% · -16.78, NONE 64 · 41% · -2.57) -> not enough evidence yet
- MES 5m: ALIGNED 2 · 50% · -1.47 / NONE 24 · 42% · -1.46 / OPPOSING 10 · 50% · -0.88 (A; B ALIGNED 2 · 50% · -1.47, NONE 25 · 44% · -1.21) -> not enough evidence yet
- MGC 5m: ALIGNED 1 · 0% · -7.00 / NONE 16 · 44% · -0.17 / OPPOSING 3 · 67% · +1.25 (A; B ALIGNED 1 · 0% · -7.00, NONE 17 · 47% · +0.02) -> not enough evidence yet
- MNQ 5m: ALIGNED 7 · 43% · -3.83 / NONE 16 · 62% · +11.32 / OPPOSING 5 · 40% · -2.02 (A; B ALIGNED 7 · 43% · -3.83, NONE 18 · 56% · +7.58) -> not enough evidence yet
