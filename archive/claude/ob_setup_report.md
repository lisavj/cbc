# CBC order-block setup study -- 2026-11-12 09:59 ET

Question: do CBC Trade Setups whose entry candle sits inside an order block do better? Alerts stored: 44310 (since 2026-10-19).
OB definitions: **A** = OB v1.08 defaults (internal, length 5, Leg swings, Lowest in leg, mitigation Close, Keep newest, last 5/5); **B** = CBC ⑨ Lux-style (ESLib2: length 5, Close, chart TF, last 5, block appears the bar after the break, Hide Overlap removes the older block). OB state = after the bar before the setup candle (no look-ahead). Buckets: ALIGNED (long traded into an active OB+ and closed at/above its bottom; short mirrored), OPPOSING (long into an OB- and closed at/below its top), NEAR (within 0.5 ATR of an aligned OB), NONE. ✱ = net positive in both chronological halves (half nets shown last). MFE/MAE = Best / Worst from the Setup Ended alert in ATR(14).

**Since last run:** vs 2026-11-09 17:06 ET: setups (ALIGNED+NONE+OPPOSING, OB v1.08) MES 3m 101->102, MGC 3m 66->70, MNQ 3m 106->106, MES 2m 113->130, MGC 2m 142->176, MNQ 2m 145->172, MES 5m 55->63, MGC 5m 48->58, MNQ 5m 54->60. MNQ 2m "block OPPOSING" still clears the bar (v1.08 OPPOSING 51 · 33% · -5.55 vs rest 136, Δavg -4.98; CBC 41 vs 146, Δavg -4.91 -- gap narrower than 11/09's -6.33 / -8.40). MES 2m "block OPPOSING" back to "consistent but points the other way" (OPPOSING does slightly better than the rest). MNQ 3m: no new ended setups since 11/09. This run is a catch-up for the failed 11/10-11/11 runs (usage limit); from now on the study runs weekly (Fridays 17:05 ET). Settings sync: no mismatches (v10.87). Note: "Setup Ended" results mix exit versions (MES 3m v10.67-v10.82, MGC 3m 50 % + trail 3.5 v10.84, gates v10.77/v10.81/v10.86-87). No OB v1.08 indicator alerts in the feed for any ticker, so that cross-check is still not possible; replay B matches CBC's own "In OB" line 99-100 %, replay A 91-98 %.

## MES 3m

Setups with results: 106 (skipped 0 without bars) · net -16.9 pts · halves split at 10/27 18:48 · A/B bucket agreement 97/106 (92%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 13 | 38% | -1.80 | -23.4 | 0.57 | 1.83 / -1.50 | -9.2 / -14.1 |
| NEAR | 4 | 25% | -1.61 | -6.4 | 0.49 | 1.27 / -1.92 | -1.4 / -5.0 |
| NONE | 67 | 48% | +0.36 | +24.0 | 1.11 | 2.02 / -1.13 | -28.5 / +52.5 |
| OPPOSING | 22 | 50% | -0.50 | -11.1 | 0.85 | 1.87 / -1.20 | +5.1 / -16.1 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 11 | 27% | -3.47 | -38.2 | 0.30 | 1.34 / -1.71 | -14.3 / -23.9 |
| NEAR | 5 | 20% | -2.11 | -10.5 | 0.37 | 1.27 / -1.82 | -5.5 / -5.0 |
| NONE | 75 | 51% | +0.62 | +46.4 | 1.20 | 2.06 / -1.11 | -15.1 / +61.5 |
| OPPOSING | 15 | 47% | -0.97 | -14.6 | 0.74 | 1.98 / -1.20 | +0.8 / -15.4 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (16) | 1 · 0% · -10.21 | 11 · 55% · +1.99 | 1 · 0% · -10.21 | 12 · 58% · +2.23 |
| LTF EMA20 Pierce/Touch (66) | 8 · 38% · -2.02 | 40 · 50% · +0.26 | 6 · 17% · -5.16 | 47 · 53% · +0.59 |
| HTF EMA pierce (22) | 4 · 50% · +0.75 | 14 · 43% · +0.07 | 4 · 50% · +0.75 | 14 · 43% · +0.07 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 106 setups, 13 say In OB): replay A agrees 96 (91%), replay B 105 (99%).
OB v1.08 indicator alerts for MES1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 13 vs 67, Δavg -2.16 · CBC 11 vs 75, Δavg -4.09)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 22 vs 84, Δavg -0.43 · CBC 15 vs 91, Δavg -0.95)

## MGC 3m

Setups with results: 75 (skipped 0 without bars) · net -19.5 pts · halves split at 10/28 21:42 · A/B bucket agreement 69/75 (92%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 9 | 67% | +0.94 | +8.5 ✱ | 1.67 | 2.41 / -0.77 | +8.5 / +0.0 |
| NEAR | 5 | 40% | -0.91 | -4.6 | 0.71 | 1.87 / -1.03 | -3.6 / -1.0 |
| NONE | 43 | 44% | +0.03 | +1.1 | 1.01 | 1.91 / -1.12 | +3.8 / -2.7 |
| OPPOSING | 18 | 33% | -1.36 | -24.5 | 0.44 | 1.09 / -1.05 | -23.5 / -1.0 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 8 | 75% | +1.69 | +13.5 ✱ | 2.77 | 2.67 / -0.64 | +13.5 / +0.0 |
| NEAR | 5 | 40% | -0.91 | -4.6 | 0.71 | 1.87 / -1.03 | -3.6 / -1.0 |
| NONE | 48 | 46% | +0.06 | +2.9 | 1.03 | 1.84 / -1.06 | -2.6 / +5.5 |
| OPPOSING | 14 | 21% | -2.23 | -31.3 | 0.23 | 0.98 / -1.27 | -22.1 / -9.2 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (9) | 0 | 5 · 80% · +1.30 | 0 | 7 · 71% · +0.36 |
| LTF EMA20 Pierce/Touch (43) | 4 · 50% · +0.32 | 24 · 46% · +0.75 | 3 · 67% · +2.09 | 26 · 46% · +0.90 |
| HTF EMA pierce (22) | 5 · 80% · +1.44 | 13 · 31% · -1.28 | 5 · 80% · +1.44 | 14 · 36% · -1.14 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 75 setups, 9 say In OB): replay A agrees 69 (92%), replay B 74 (99%).
OB v1.08 indicator alerts for MGC1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 9 vs 43, Δavg +0.92 · CBC 8 vs 48, Δavg +1.63)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 18 vs 57, Δavg -1.45 · CBC 14 vs 61, Δavg -2.43)

## MNQ 3m

Setups with results: 108 (skipped 0 without bars) · net -972.3 pts · halves split at 10/28 10:48 · A/B bucket agreement 96/108 (89%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 9 | 33% | -8.14 | -73.2 | 0.57 | 1.10 / -1.09 | -48.0 / -25.2 |
| NEAR | 2 | 100% | +38.98 | +78.0 ✱ | ∞ | 4.05 / -0.23 | +30.6 / +47.4 |
| NONE | 64 | 25% | -11.81 | -755.6 | 0.44 | 1.04 / -1.10 | -507.7 / -247.8 |
| OPPOSING | 33 | 36% | -6.71 | -221.4 | 0.63 | 1.18 / -0.99 | +11.5 / -232.9 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 8 | 38% | -5.41 | -43.2 | 0.69 | 1.12 / -1.05 | -48.0 / +4.8 |
| NEAR | 4 | 50% | +0.65 | +2.6 | 1.04 | 1.55 / -0.78 | +32.6 / -30.0 |
| NONE | 73 | 25% | -11.93 | -871.2 | 0.44 | 1.07 / -1.12 | -592.7 / -278.5 |
| OPPOSING | 23 | 43% | -2.63 | -60.4 | 0.84 | 1.33 / -0.87 | +94.5 / -154.9 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (30) | 1 · 0% · -25.00 | 18 · 33% · -6.94 | 1 · 0% · -25.00 | 20 · 30% · -9.24 |
| LTF EMA20 Pierce/Touch (54) | 5 · 40% · -4.20 | 35 · 14% · -17.41 | 4 · 50% · +2.25 | 41 · 15% · -17.37 |
| HTF EMA pierce (24) | 3 · 33% · -9.08 | 11 · 45% · -1.96 | 3 · 33% · -9.08 | 12 · 50% · +2.15 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 108 setups, 18 say In OB): replay A agrees 101 (94%), replay B 108 (100%).
OB v1.08 indicator alerts for MNQ1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 9 vs 64, Δavg +3.67 · CBC 8 vs 73, Δavg +6.53)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 33 vs 75, Δavg +3.30 · CBC 23 vs 85, Δavg +8.10)

## MES 2m

Setups with results: 138 (skipped 0 without bars) · net -66.5 pts · halves split at 10/28 05:50 · A/B bucket agreement 121/138 (88%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 12 | 50% | +0.76 | +9.1 ✱ | 1.56 | 1.41 / -0.72 | +4.3 / +4.8 |
| NEAR | 8 | 50% | +0.54 | +4.3 | 1.30 | 2.15 / -1.14 | -2.2 / +6.5 |
| NONE | 74 | 43% | -0.96 | -71.2 | 0.69 | 1.67 / -1.31 | -82.2 / +11.0 |
| OPPOSING | 44 | 45% | -0.20 | -8.7 | 0.92 | 1.50 / -1.34 | -31.5 / +22.7 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 12 | 50% | +0.76 | +9.1 ✱ | 1.56 | 1.41 / -0.72 | +4.3 / +4.8 |
| NEAR | 8 | 50% | +0.05 | +0.4 ✱ | 1.02 | 2.09 / -0.99 | +0.2 / +0.2 |
| NONE | 89 | 40% | -1.05 | -93.8 | 0.66 | 1.56 / -1.31 | -94.6 / +0.9 |
| OPPOSING | 29 | 55% | +0.61 | +17.8 | 1.26 | 1.79 / -1.37 | -21.4 / +39.2 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (37) | 0 | 19 · 58% · +0.35 | 0 | 25 · 52% · -0.20 |
| LTF EMA20 Pierce/Touch (78) | 7 · 57% · +1.34 | 44 · 39% · -1.61 | 7 · 57% · +1.34 | 52 · 37% · -1.46 |
| HTF EMA pierce (21) | 4 · 25% · -1.28 | 10 · 40% · +0.12 | 4 · 25% · -1.28 | 11 · 36% · -0.42 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 138 setups, 20 say In OB): replay A agrees 127 (92%), replay B 138 (100%).
OB v1.08 indicator alerts for MES1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 12 vs 74, Δavg +1.72 · CBC 12 vs 89, Δavg +1.81)

Verdict: block OPPOSING (OPPOSING vs rest): **consistent but points the other way** (v1.08 44 vs 94, Δavg +0.42 · CBC 29 vs 109, Δavg +1.39)

## MGC 2m

Setups with results: 189 (skipped 0 without bars) · net -74.6 pts · halves split at 11/01 19:02 · A/B bucket agreement 179/189 (95%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 13 | 38% | -1.18 | -15.3 | 0.54 | 1.65 / -1.36 | -15.5 / +0.1 |
| NEAR | 13 | 46% | +0.54 | +7.0 | 1.30 | 3.20 / -1.55 | -0.6 / +7.7 |
| NONE | 117 | 44% | -0.53 | -62.0 | 0.76 | 1.56 / -1.36 | -6.9 / -55.1 |
| OPPOSING | 46 | 54% | -0.09 | -4.3 | 0.96 | 2.42 / -1.29 | -5.0 / +0.7 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 13 | 38% | -1.18 | -15.3 | 0.54 | 1.65 / -1.36 | -15.5 / +0.1 |
| NEAR | 11 | 55% | +0.85 | +9.3 ✱ | 1.44 | 3.47 / -1.40 | +8.7 / +0.6 |
| NONE | 126 | 43% | -0.58 | -72.8 | 0.74 | 1.55 / -1.38 | -11.9 / -60.9 |
| OPPOSING | 39 | 56% | +0.11 | +4.2 | 1.06 | 2.61 / -1.28 | -9.2 / +13.4 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (49) | 2 · 0% · -5.26 | 26 · 38% · -1.49 | 2 · 0% · -5.26 | 31 · 39% · -1.26 |
| LTF EMA20 Pierce/Touch (97) | 5 · 60% · +1.07 | 65 · 46% · -0.32 | 5 · 60% · +1.07 | 67 · 45% · -0.44 |
| HTF EMA pierce (42) | 6 · 33% · -1.69 | 25 · 44% · +0.11 | 6 · 33% · -1.69 | 27 · 44% · +0.02 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 189 setups, 30 say In OB): replay A agrees 180 (95%), replay B 189 (100%).
OB v1.08 indicator alerts for MGC1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 13 vs 117, Δavg -0.65 · CBC 13 vs 126, Δavg -0.60)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 46 vs 143, Δavg +0.40 · CBC 39 vs 150, Δavg +0.63)

## MNQ 2m

Setups with results: 187 (skipped 0 without bars) · net -360.2 pts · halves split at 10/29 12:20 · A/B bucket agreement 171/187 (91%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 16 | 19% | -13.96 | -223.4 | 0.29 | 1.33 / -1.18 | -164.2 / -59.1 |
| NEAR | 15 | 47% | +3.93 | +59.0 ✱ | 1.33 | 1.55 / -1.02 | +15.9 / +43.1 |
| NONE | 105 | 46% | +0.83 | +87.1 | 1.06 | 1.74 / -0.99 | -71.2 / +158.3 |
| OPPOSING | 51 | 33% | -5.55 | -282.9 | 0.69 | 1.77 / -1.35 | -186.2 / -96.7 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 13 | 15% | -16.10 | -209.3 | 0.18 | 1.02 / -1.22 | -134.2 / -75.1 |
| NEAR | 16 | 38% | -2.58 | -41.2 | 0.82 | 1.31 / -1.21 | -32.6 / -8.6 |
| NONE | 117 | 45% | +1.08 | +126.5 | 1.07 | 1.81 / -0.99 | -159.4 / +285.9 |
| OPPOSING | 41 | 34% | -5.76 | -236.1 | 0.68 | 1.75 / -1.38 | -79.5 / -156.6 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (60) | 1 · 0% · -30.00 | 28 · 57% · +8.95 | 0 | 34 · 53% · +6.80 |
| LTF EMA20 Pierce/Touch (78) | 8 · 12% · -20.48 | 48 · 40% · -2.70 | 6 · 0% · -29.96 | 54 · 41% · -1.31 |
| HTF EMA pierce (46) | 5 · 20% · -0.41 | 28 · 46% · -0.14 | 5 · 20% · -0.41 | 28 · 46% · -0.14 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 187 setups, 38 say In OB): replay A agrees 179 (96%), replay B 186 (99%).
OB v1.08 indicator alerts for MNQ1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 16 vs 105, Δavg -14.79 · CBC 13 vs 117, Δavg -17.18)

Verdict: block OPPOSING (OPPOSING vs rest): **OB filter worth testing** (v1.08 51 vs 136, Δavg -4.98 · CBC 41 vs 146, Δavg -4.91)

## MES 5m

Setups with results: 67 (skipped 0 without bars) · net -30.2 pts · halves split at 10/28 20:55 · A/B bucket agreement 65/67 (97%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 6 | 67% | +1.37 | +8.2 | 1.63 | 1.90 / -0.84 | -2.9 / +11.1 |
| NEAR | 4 | 25% | -2.92 | -11.7 | 0.27 | 0.81 / -1.06 | +4.3 / -16.0 |
| NONE | 41 | 51% | -0.34 | -14.0 | 0.89 | 1.41 / -1.01 | -24.1 / +10.1 |
| OPPOSING | 16 | 50% | -0.80 | -12.7 | 0.78 | 1.33 / -1.02 | -0.8 / -11.9 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 6 | 67% | +1.37 | +8.2 | 1.63 | 1.90 / -0.84 | -2.9 / +11.1 |
| NEAR | 4 | 25% | -2.92 | -11.7 | 0.27 | 0.81 / -1.06 | +4.3 / -16.0 |
| NONE | 43 | 53% | -0.00 | -0.2 | 1.00 | 1.50 / -0.97 | -19.3 / +19.1 |
| OPPOSING | 14 | 43% | -1.90 | -26.6 | 0.53 | 1.03 / -1.12 | -5.6 / -21.0 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (15) | 0 | 9 · 67% · +0.74 | 0 | 9 · 67% · +0.74 |
| LTF EMA20 Pierce/Touch (41) | 5 · 60% · +0.26 | 28 · 50% · -0.17 | 5 · 60% · +0.26 | 29 · 52% · +0.15 |
| HTF EMA pierce (10) | 1 · 100% · +6.92 | 3 · 33% · -3.38 | 1 · 100% · +6.92 | 4 · 50% · -1.34 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 67 setups, 11 say In OB): replay A agrees 64 (96%), replay B 66 (99%).
OB v1.08 indicator alerts for MES1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 6 vs 41, Δavg +1.71 · CBC 6 vs 43, Δavg +1.37)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 16 vs 51, Δavg -0.45 · CBC 14 vs 53, Δavg -1.83)

## MGC 5m

Setups with results: 63 (skipped 0 without bars) · net -14.9 pts · halves split at 11/02 21:30 · A/B bucket agreement 61/63 (97%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 5 | 20% | -4.04 | -20.2 | 0.18 | 1.35 / -0.96 | -9.4 / -10.8 |
| NEAR | 5 | 80% | +2.34 | +11.7 ✱ | 2.95 | 1.80 / -0.52 | +2.1 / +9.7 |
| NONE | 40 | 48% | +0.07 | +2.7 ✱ | 1.03 | 1.39 / -1.03 | +1.3 / +1.4 |
| OPPOSING | 13 | 46% | -0.69 | -9.0 | 0.78 | 1.59 / -1.04 | -1.7 / -7.4 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 5 | 20% | -4.04 | -20.2 | 0.18 | 1.35 / -0.96 | -9.4 / -10.8 |
| NEAR | 4 | 75% | +2.17 | +8.7 | 2.45 | 1.77 / -0.51 | -1.0 / +9.7 |
| NONE | 42 | 48% | +0.06 | +2.5 ✱ | 1.02 | 1.39 / -1.01 | +1.1 / +1.4 |
| OPPOSING | 12 | 50% | -0.49 | -5.8 | 0.85 | 1.65 / -1.05 | +1.5 / -7.4 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (15) | 0 | 9 · 67% · +1.37 | 0 | 10 · 70% · +1.53 |
| LTF EMA20 Pierce/Touch (32) | 4 · 0% · -6.20 | 21 · 29% · -1.60 | 4 · 0% · -6.20 | 21 · 29% · -1.60 |
| HTF EMA pierce (16) | 1 · 100% · +4.58 | 10 · 70% · +2.40 | 1 · 100% · +4.58 | 11 · 64% · +1.89 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 63 setups, 8 say In OB): replay A agrees 62 (98%), replay B 63 (100%).
OB v1.08 indicator alerts for MGC1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 5 vs 40, Δavg -4.11 · CBC 5 vs 42, Δavg -4.10)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 13 vs 50, Δavg -0.58 · CBC 12 vs 51, Δavg -0.31)

## MNQ 5m

Setups with results: 60 (skipped 0 without bars) · net +487.2 pts · halves split at 11/02 04:25 · A/B bucket agreement 57/60 (95%)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 10 | 50% | +8.93 | +89.3 ✱ | 1.68 | 1.71 / -0.72 | +87.3 / +2.0 |
| NEAR | 0 | – | – | – | – | – | |
| NONE | 37 | 57% | +10.99 | +406.7 ✱ | 1.92 | 1.90 / -0.68 | +218.0 / +188.8 |
| OPPOSING | 13 | 38% | -0.68 | -8.8 | 0.96 | 1.70 / -0.71 | -10.1 / +1.3 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 10 | 50% | +8.93 | +89.3 ✱ | 1.68 | 1.71 / -0.72 | +87.3 / +2.0 |
| NEAR | 0 | – | – | – | – | – | |
| NONE | 40 | 55% | +9.88 | +395.3 ✱ | 1.81 | 1.86 / -0.69 | +173.2 / +222.1 |
| OPPOSING | 10 | 40% | +0.26 | +2.6 | 1.01 | 1.77 / -0.68 | +34.6 / -32.1 |

By trigger (n · win % · avg pts):

| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |
|---|---|---|---|---|
| HTF CBC Flip (9) | 0 | 7 · 43% · -1.71 | 0 | 8 · 38% · -5.25 |
| LTF EMA20 Pierce/Touch (32) | 5 · 80% · +37.50 | 20 · 60% · +13.47 | 5 · 80% · +37.50 | 21 · 57% · +12.13 |
| HTF EMA pierce (18) | 5 · 20% · -19.65 | 10 · 60% · +14.92 | 5 · 20% · -19.65 | 11 · 64% · +16.60 |

Cross-check vs CBC alert "In OB±/OB: none" line (close inside, 60 setups, 4 say In OB): replay A agrees 56 (93%), replay B 60 (100%).
OB v1.08 indicator alerts for MNQ1! in the feed: 0 (none within 5 candles of a setup) -- cross-check not possible.

Verdict: require ALIGNED (ALIGNED vs NONE): **not enough evidence yet** (v1.08 10 vs 37, Δavg -2.07 · CBC 10 vs 40, Δavg -0.96)

Verdict: block OPPOSING (OPPOSING vs rest): **not enough evidence yet** (v1.08 13 vs 47, Δavg -11.23 · CBC 10 vs 50, Δavg -9.44)

## All cases pooled (info only -- decide per symbol + timeframe)

**A · OB v1.08**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 93 | 41% | -2.59 | -240.6 | 0.69 | 1.62 / -1.06 | -215.0 / -25.5 |
| NEAR | 56 | 48% | +2.45 | +137.3 ✱ | 1.52 | 2.09 / -1.16 | +41.2 / +96.2 |
| NONE | 588 | 44% | -0.65 | -381.2 | 0.91 | 1.63 / -1.13 | -676.2 / +295.0 |
| OPPOSING | 256 | 43% | -2.28 | -583.5 | 0.73 | 1.69 / -1.19 | -323.1 / -260.4 |

**B · CBC Lux-style**

| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |
|---|---|---|---|---|---|---|---|
| ALIGNED | 86 | 41% | -2.40 | -206.2 | 0.70 | 1.53 / -1.07 | -185.1 / -21.2 |
| NEAR | 57 | 44% | -0.83 | -47.1 | 0.88 | 1.90 / -1.16 | -25.8 / -21.3 |
| NONE | 653 | 44% | -0.71 | -464.3 | 0.90 | 1.63 / -1.12 | -892.4 / +428.1 |
| OPPOSING | 197 | 45% | -1.78 | -350.2 | 0.79 | 1.78 / -1.20 | -69.8 / -280.4 |

A/B bucket agreement: 916/993 (92%). Points differ in size between symbols (MNQ >> MES > MGC), so pooled pts are dominated by MNQ.

## Summary (A buckets: n · win % · avg pts)

- MES 3m: ALIGNED 13 · 38% · -1.80 / NONE 67 · 48% · +0.36 / OPPOSING 22 · 50% · -0.50 (A; B ALIGNED 11 · 27% · -3.47, NONE 75 · 51% · +0.62) -> not enough evidence yet
- MGC 3m: ALIGNED 9 · 67% · +0.94 / NONE 43 · 44% · +0.03 / OPPOSING 18 · 33% · -1.36 (A; B ALIGNED 8 · 75% · +1.69, NONE 48 · 46% · +0.06) -> not enough evidence yet
- MNQ 3m: ALIGNED 9 · 33% · -8.14 / NONE 64 · 25% · -11.81 / OPPOSING 33 · 36% · -6.71 (A; B ALIGNED 8 · 38% · -5.41, NONE 73 · 25% · -11.93) -> not enough evidence yet
- MES 2m: ALIGNED 12 · 50% · +0.76 / NONE 74 · 43% · -0.96 / OPPOSING 44 · 45% · -0.20 (A; B ALIGNED 12 · 50% · +0.76, NONE 89 · 40% · -1.05) -> not enough evidence yet
- MGC 2m: ALIGNED 13 · 38% · -1.18 / NONE 117 · 44% · -0.53 / OPPOSING 46 · 54% · -0.09 (A; B ALIGNED 13 · 38% · -1.18, NONE 126 · 43% · -0.58) -> not enough evidence yet
- MNQ 2m: ALIGNED 16 · 19% · -13.96 / NONE 105 · 46% · +0.83 / OPPOSING 51 · 33% · -5.55 (A; B ALIGNED 13 · 15% · -16.10, NONE 117 · 45% · +1.08) -> worth testing
- MES 5m: ALIGNED 6 · 67% · +1.37 / NONE 41 · 51% · -0.34 / OPPOSING 16 · 50% · -0.80 (A; B ALIGNED 6 · 67% · +1.37, NONE 43 · 53% · -0.00) -> not enough evidence yet
- MGC 5m: ALIGNED 5 · 20% · -4.04 / NONE 40 · 48% · +0.07 / OPPOSING 13 · 46% · -0.69 (A; B ALIGNED 5 · 20% · -4.04, NONE 42 · 48% · +0.06) -> not enough evidence yet
- MNQ 5m: ALIGNED 10 · 50% · +8.93 / NONE 37 · 57% · +10.99 / OPPOSING 13 · 38% · -0.68 (A; B ALIGNED 10 · 50% · +8.93, NONE 40 · 55% · +9.88) -> not enough evidence yet
