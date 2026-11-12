Maximum favourable price (MFE) with and without the recommended rules -- MES 3m and MGC 3m -- 11/08/2026.
For every trade: MFE in trade = the best price reached in the trade's direction between entry and exit (points, and as a share of
the TP1 distance); MAE = the worst price against; giveback = MFE minus the result (gross, before costs); MFE 60 = the best price in
the first 60 min after entry whatever the exit (what the setup offered); for trades a rule closes early: how far price went
afterwards, up to where the current exits would have closed the same trade.
Rule sets (same replay as all_combo.py; live 3m exits):
  MES 3m: current | TP1 -> 85 % after 18 min | balanced = shorts only below the 5-day EMA + stop after 2 losses / 2 flip-outs only
          when the previous 5 sessions lost + half SL1 if negative at 18 min | all four (balanced + the TP rule)
  MGC 3m: current | London stops after its first loss | London stop + skip against VWAP | all four (+ TP1 -> 65 % after 21 min +
          close if under 25 % of TP1 at 18 min)

## MES 3m

**Whole** (points; TP1 = share of the TP1 distance)

| Rule set | Trades | Avg MFE in trade | Median MFE | Avg MFE / TP1 | Reached 50 % of TP1 | Reached TP1 | Reached 1.5 x TP1 | Avg MAE | Avg result (gross) | Giveback (MFE − result) | Captured % of MFE | MFE first 60 min | Net after costs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Current exits | 1700 | 6.64 | 4.00 | 1.05 | 63 % | 45 % | 20 % | 4.97 | +0.01 | 6.63 | 0 % | 8.46 | -831 |
| TP1 -> 85 % after 18 min | 1770 | 5.67 | 3.75 | 0.91 | 63 % | 35 % | 12 % | 4.83 | +0.13 | 5.54 | 2 % | 8.49 | -652 |
| Balanced (filter + losing-stretch stop + SL rule) | 992 | 6.51 | 3.75 | 1.02 | 61 % | 46 % | 19 % | 4.41 | +0.52 | 5.99 | 8 % | 8.41 | +11 |
| All four | 1037 | 5.51 | 3.50 | 0.88 | 61 % | 35 % | 12 % | 4.34 | +0.52 | 4.98 | 10 % | 8.49 | +15 |

**Third 3** (points; TP1 = share of the TP1 distance)

| Rule set | Trades | Avg MFE in trade | Median MFE | Avg MFE / TP1 | Reached 50 % of TP1 | Reached TP1 | Reached 1.5 x TP1 | Avg MAE | Avg result (gross) | Giveback (MFE − result) | Captured % of MFE | MFE first 60 min | Net after costs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Current exits | 620 | 6.32 | 4.00 | 1.13 | 67 % | 49 % | 21 % | 4.47 | +0.35 | 5.98 | 5 % | 7.73 | -94 |
| TP1 -> 85 % after 18 min | 649 | 5.29 | 3.50 | 0.96 | 66 % | 38 % | 12 % | 4.37 | +0.39 | 4.90 | 7 % | 7.81 | -70 |
| Balanced (filter + losing-stretch stop + SL rule) | 370 | 6.14 | 3.75 | 1.05 | 62 % | 48 % | 19 % | 4.16 | +0.61 | 5.52 | 10 % | 7.70 | +37 |
| All four | 386 | 5.02 | 3.25 | 0.89 | 61 % | 37 % | 10 % | 4.11 | +0.51 | 4.52 | 10 % | 7.75 | -2 |

**Last 4 wk** (points; TP1 = share of the TP1 distance)

| Rule set | Trades | Avg MFE in trade | Median MFE | Avg MFE / TP1 | Reached 50 % of TP1 | Reached TP1 | Reached 1.5 x TP1 | Avg MAE | Avg result (gross) | Giveback (MFE − result) | Captured % of MFE | MFE first 60 min | Net after costs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Current exits | 149 | 9.02 | 5.25 | 1.17 | 64 % | 56 % | 23 % | 5.79 | +1.68 | 7.34 | 19 % | 10.15 | +176 |
| TP1 -> 85 % after 18 min | 159 | 7.10 | 4.50 | 0.96 | 64 % | 45 % | 12 % | 5.64 | +1.45 | 5.65 | 20 % | 10.07 | +150 |
| Balanced (filter + losing-stretch stop + SL rule) | 118 | 9.00 | 4.88 | 1.12 | 61 % | 53 % | 23 % | 5.50 | +1.41 | 7.59 | 16 % | 10.09 | +106 |
| All four | 126 | 6.94 | 4.38 | 0.91 | 60 % | 42 % | 12 % | 5.41 | +1.01 | 5.93 | 15 % | 10.06 | +63 |

**After an early rule exit — TP1 -> 85 % after 18 min** (the same trade under current exits)

| Exit | Trades | Avg result with rule | Avg result current exits | Avg MFE until rule exit | Avg MFE under current exits | Later reached TP1 under current exits | Current exits ended at the full SL1 |
|---|---|---|---|---|---|---|---|
| reduced TP filled | 416 | +5.29 | +4.83 | 6.58 | 10.63 | 89 % | 2 % |

**After an early rule exit — Balanced (filter + losing-stretch stop + SL rule)** (the same trade under current exits)

| Exit | Trades | Avg result with rule | Avg result current exits | Avg MFE until rule exit | Avg MFE under current exits | Later reached TP1 under current exits | Current exits ended at the full SL1 |
|---|---|---|---|---|---|---|---|
| cut / tightened stop | 36 | -5.69 | -6.19 | 1.39 | 2.08 | 8 % | 33 % |

**After an early rule exit — All four** (the same trade under current exits)

| Exit | Trades | Avg result with rule | Avg result current exits | Avg MFE until rule exit | Avg MFE under current exits | Later reached TP1 under current exits | Current exits ended at the full SL1 |
|---|---|---|---|---|---|---|---|
| cut / tightened stop | 36 | -5.69 | -6.19 | 1.39 | 2.08 | 8 % | 33 % |
| reduced TP filled | 234 | +5.46 | +5.30 | 6.65 | 11.16 | 90 % | 1 % |

**Trades the TP1 -> 85 % after 18 min rule set skips** vs the trades it keeps (current exits): skipped 7, avg MFE 6.43 (43 % reached TP1), avg result +0.66 gross; kept 1693, avg MFE 6.64 (45 % reached TP1), avg result +0.01 gross.

**Trades the Balanced (filter + losing-stretch stop + SL rule) rule set skips** vs the trades it keeps (current exits): skipped 723, avg MFE 6.56 (42 % reached TP1), avg result -0.63 gross; kept 977, avg MFE 6.70 (47 % reached TP1), avg result +0.48 gross.

**Trades the All four rule set skips** vs the trades it keeps (current exits): skipped 725, avg MFE 6.52 (42 % reached TP1), avg result -0.60 gross; kept 975, avg MFE 6.74 (47 % reached TP1), avg result +0.47 gross.

## MGC 3m

**Whole** (points; TP1 = share of the TP1 distance)

| Rule set | Trades | Avg MFE in trade | Median MFE | Avg MFE / TP1 | Reached 50 % of TP1 | Reached TP1 | Reached 1.5 x TP1 | Avg MAE | Avg result (gross) | Giveback (MFE − result) | Captured % of MFE | MFE first 60 min | Net after costs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Current exits | 1705 | 8.24 | 4.80 | 1.47 | 65 % | 47 % | 31 % | 4.85 | +0.14 | 8.10 | 2 % | 11.84 | -138 |
| London stop after 1st loss | 1438 | 8.38 | 4.90 | 1.50 | 66 % | 48 % | 31 % | 4.79 | +0.28 | 8.09 | 3 % | 11.72 | +89 |
| London stop + VWAP filter | 1296 | 8.53 | 5.25 | 1.52 | 66 % | 49 % | 32 % | 4.76 | +0.37 | 8.16 | 4 % | 12.07 | +193 |
| All four | 1331 | 7.69 | 4.20 | 1.37 | 63 % | 41 % | 26 % | 4.33 | +0.44 | 7.25 | 6 % | 11.91 | +266 |

**Third 3** (points; TP1 = share of the TP1 distance)

| Rule set | Trades | Avg MFE in trade | Median MFE | Avg MFE / TP1 | Reached 50 % of TP1 | Reached TP1 | Reached 1.5 x TP1 | Avg MAE | Avg result (gross) | Giveback (MFE − result) | Captured % of MFE | MFE first 60 min | Net after costs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Current exits | 558 | 6.99 | 4.05 | 1.34 | 61 % | 45 % | 30 % | 4.20 | +0.08 | 6.90 | 1 % | 9.19 | -77 |
| London stop after 1st loss | 475 | 6.98 | 4.10 | 1.35 | 61 % | 45 % | 30 % | 4.15 | +0.12 | 6.86 | 2 % | 8.82 | -46 |
| London stop + VWAP filter | 429 | 7.24 | 4.40 | 1.40 | 62 % | 47 % | 31 % | 4.07 | +0.31 | 6.94 | 4 % | 9.29 | +37 |
| All four | 445 | 6.28 | 3.40 | 1.22 | 59 % | 38 % | 24 % | 3.63 | +0.36 | 5.92 | 6 % | 9.25 | +55 |

**Last 4 wk** (points; TP1 = share of the TP1 distance)

| Rule set | Trades | Avg MFE in trade | Median MFE | Avg MFE / TP1 | Reached 50 % of TP1 | Reached TP1 | Reached 1.5 x TP1 | Avg MAE | Avg result (gross) | Giveback (MFE − result) | Captured % of MFE | MFE first 60 min | Net after costs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Current exits | 154 | 7.82 | 4.25 | 1.53 | 67 % | 45 % | 33 % | 4.14 | +0.42 | 7.41 | 5 % | 9.20 | +30 |
| London stop after 1st loss | 132 | 7.99 | 4.45 | 1.56 | 70 % | 47 % | 33 % | 4.12 | +0.63 | 7.36 | 8 % | 9.26 | +53 |
| London stop + VWAP filter | 117 | 8.02 | 4.90 | 1.58 | 69 % | 49 % | 35 % | 3.85 | +0.78 | 7.24 | 10 % | 9.37 | +66 |
| All four | 121 | 7.00 | 4.10 | 1.39 | 64 % | 40 % | 26 % | 3.42 | +0.90 | 6.10 | 13 % | 9.36 | +80 |

**After an early rule exit — All four** (the same trade under current exits)

| Exit | Trades | Avg result with rule | Avg result current exits | Avg MFE until rule exit | Avg MFE under current exits | Later reached TP1 under current exits | Current exits ended at the full SL1 |
|---|---|---|---|---|---|---|---|
| cut / tightened stop | 240 | -1.12 | -1.56 | 2.86 | 5.57 | 33 % | 40 % |
| reduced TP filled | 55 | +3.65 | +3.12 | 5.40 | 11.00 | 71 % | 7 % |

**Trades the London stop after 1st loss rule set skips** vs the trades it keeps (current exits): skipped 267, avg MFE 7.50 (42 % reached TP1), avg result -0.63 gross; kept 1438, avg MFE 8.38 (48 % reached TP1), avg result +0.28 gross.

**Trades the London stop + VWAP filter rule set skips** vs the trades it keeps (current exits): skipped 425, avg MFE 7.41 (42 % reached TP1), avg result -0.51 gross; kept 1280, avg MFE 8.51 (49 % reached TP1), avg result +0.35 gross.

**Trades the All four rule set skips** vs the trades it keeps (current exits): skipped 435, avg MFE 7.44 (42 % reached TP1), avg result -0.47 gross; kept 1270, avg MFE 8.51 (49 % reached TP1), avg result +0.35 gross.
