# CBC alert parameter sweep -- 2026-10-29 17:07 ET

Alert Feed: 19566 alerts (10/19 to 10/29). Bars: BarFeed, last 60 days. Validation window = days with stored alerts.
Outcome (a) = exit at first opposite HTF CBC flip / 17:00 ET / 2 h. (b) = 1.3 ATR stop / 2.0 ATR target (both in one candle = stop). Points per contract-point, before costs. ✱ = positive in both halves of the data under both rules. Validation: recall = stored alerts the replay reproduces (±1 bar), precision = replayed alerts that were stored. Unreliable = recall or precision < 70 %.

Notes: "Option 2: Reverse" pierces are scored in the reversed direction (as the alert says). LTF cooldown 0 and 1 are identical (a pierce needs the previous candle not touching the line). HTF EMA pierces use the setup-engine direction (flip counts on the HTF candle close) and the away / toward-late (1 pt) gate. 2m charts use their own 10m HTF fields from the BarFeed. Pullback-Structure replay rebuilds HTF swing pivots from the chart candles and does not reproduce the live alerts well (few stored alerts). In FVG alerts: none stored in the Alert Feed so far. Verdict rule: "worth considering" needs 30+ alerts, better than current in both halves under both rules, neighbouring values also better, and a reliable replay.

Since last run: vs 10/28 report (Alert Feed 16242 -> 19566 alerts, bar window shifted 1 day). Still flagged: MES 3m VWAP Bounce min distance 2 (4th run in a row; rule (a) now positive +13.0 vs -271.0 at auto 6, rule (b) +139.0 vs +23.2), MES 3m LTF EMA20 Pierce cooldown 8 (2nd run; still negative under both rules, -151.8 / -50.0 vs -284.0 / -143.6 -- 'fewer losing alerts', not an edge), MGC 2m VWAP Bounce 0 (3rd run; rule (b) flat at +3.5). Dropped: MGC 3m VWAP Bounce 0 (no longer better than auto 6 in both halves; rule (b) -77.8) and MES 2m VWAP Bounce 2 (no longer better in both halves; rule (b) +3.9 vs -1.5). Validation rates within a few % of last run (MES 3m LTF EMA20 recall 73 -> 75 %, precision 81 -> 83 %); Pullback-Structure still unreliable everywhere; still no FVG alerts stored; few new VWAP Bounce alerts stored today (MGC 3m 20 -> 21, others unchanged). Script unchanged.

## MES 3m (HTF 15m) -- 20497 bars 08/28 to 10/29

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 143, replayed 129, recall 75 %, precision 83 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 821 | 18.2 | 40 | -0.32 | -263.5 | 0.91 | 38 | -0.17 | -137.4 | 0.94 |  |
| 1 | 821 | 18.2 | 40 | -0.32 | -263.5 | 0.91 | 38 | -0.17 | -137.4 | 0.94 |  |
| 2 | 764 | 17.0 | 40 | -0.35 | -266.0 | 0.90 | 38 | -0.21 | -156.9 | 0.92 |  |
| 3 (current) | 709 | 15.8 | 39 | -0.40 | -284.0 | 0.88 | 38 | -0.20 | -143.6 | 0.92 |  |
| 5 | 630 | 14.0 | 39 | -0.37 | -230.5 | 0.89 | 37 | -0.28 | -179.3 | 0.89 |  |
| 8 | 537 | 11.9 | 40 | -0.28 | -151.8 | 0.92 | 39 | -0.09 | -50.0 | 0.96 |  |

Best value: 8 · **worth considering: 8**

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 146, replayed 135, recall 86 %, precision 93 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 722 | 16.0 | 40 | -0.07 | -53.8 | 0.98 | 40 | +0.12 | +87.0 | 1.05 |  |
| 3 (current) | 653 | 14.5 | 39 | -0.23 | -149.8 | 0.94 | 39 | +0.07 | +43.1 | 1.03 |  |
| 5 | 567 | 12.6 | 38 | -0.33 | -187.0 | 0.91 | 40 | +0.11 | +65.0 | 1.05 |  |

Best value: 1 · no change yet (best 1: not better in both halves, neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 92, replayed 86, recall 87 %, precision 93 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 450 | 10.0 | 37 | -1.00 | -451.2 | 0.75 | 34 | -0.58 | -260.2 | 0.79 |  |
| 3 (current) | 398 | 8.8 | 37 | -1.09 | -434.2 | 0.74 | 35 | -0.54 | -215.8 | 0.80 |  |
| 5 | 354 | 7.9 | 37 | -1.12 | -395.2 | 0.73 | 34 | -0.65 | -229.5 | 0.77 |  |

Best value: 5 · no change yet (best 5: not better in both halves, neighbours disagree)

### HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)

Validation at current: stored 2, replayed 13, recall 0 %, precision 0 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 26 | 0.6 | 46 | +0.52 | +13.5 | 1.19 | 46 | +0.47 | +12.3 | 1.22 |  |
| 2 | 43 | 1.0 | 37 | -0.55 | -23.8 | 0.80 | 40 | -0.51 | -22.1 | 0.82 |  |
| 3 | 61 | 1.4 | 31 | -2.39 | -145.5 | 0.42 | 34 | -1.17 | -71.6 | 0.63 |  |
| 4 (current) | 81 | 1.8 | 33 | -1.74 | -141.0 | 0.47 | 41 | -0.25 | -20.6 | 0.90 |  |
| 6 | 100 | 2.2 | 39 | -0.75 | -75.0 | 0.73 | 47 | +0.38 | +38.2 | 1.16 |  |
| 8 | 118 | 2.6 | 39 | -0.71 | -84.2 | 0.74 | 49 | +0.60 | +70.9 | 1.26 |  |

Best value: 1 · no change yet (best 1: 26 alerts, not better in both halves, replay unreliable)

### In FVG of HTF Flip Candle: (min gap bars, stop after N bars)

Validation: no stored alerts of this type for this chart -- replay unchecked.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (1, 10) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (1, 15) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (1, 20) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (1, 30) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (1, 40) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (2, 10) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (2, 15) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (2, 20) (current) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (2, 30) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (2, 40) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (3, 10) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (3, 15) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (3, 20) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (3, 30) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (3, 40) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (5, 10) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (5, 15) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (5, 20) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (5, 30) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (5, 40) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |

Best value: (1, 10) · no change yet (best (1, 10): 0 alerts, not better in both halves, neighbours disagree, replay unreliable)

### VWAP Bounce: min distance from major S/R (pts, 0 = no gate)

Validation at current: stored 47, replayed 43, recall 91 %, precision 100 %
Current = auto 6.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 715 | 15.9 | 43 | -0.21 | -153.5 | 0.94 | 39 | +0.09 | +67.3 | 1.05 |  |
| 2 | 444 | 9.9 | 44 | +0.03 | +13.0 | 1.01 | 42 | +0.31 | +139.0 | 1.15 |  |
| 4 | 273 | 6.1 | 41 | -0.24 | -65.0 | 0.93 | 41 | +0.35 | +96.8 | 1.18 |  |
| 6 (current) | 180 | 4.0 | 34 | -1.51 | -271.0 | 0.59 | 37 | +0.13 | +23.2 | 1.07 |  |
| 8 | 156 | 3.5 | 35 | -0.83 | -129.5 | 0.72 | 36 | +0.05 | +7.2 | 1.02 |  |
| 10 | 133 | 3.0 | 35 | -0.96 | -127.5 | 0.61 | 35 | -0.36 | -48.4 | 0.80 |  |

Best value: 2 · **worth considering: 2**

## MGC 3m (HTF 15m) -- 20529 bars 08/28 to 10/29

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 150, replayed 136, recall 79 %, precision 88 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 776 | 17.2 | 40 | -0.04 | -31.8 | 0.99 | 40 | -0.05 | -38.4 | 0.98 |  |
| 1 | 776 | 17.2 | 40 | -0.04 | -31.8 | 0.99 | 40 | -0.05 | -38.4 | 0.98 |  |
| 2 | 726 | 16.1 | 39 | -0.35 | -256.3 | 0.92 | 40 | -0.10 | -72.1 | 0.96 |  |
| 3 (current) | 676 | 15.0 | 40 | -0.20 | -134.8 | 0.95 | 41 | +0.04 | +23.8 | 1.01 |  |
| 5 | 599 | 13.3 | 40 | +0.10 | +59.5 | 1.02 | 41 | -0.03 | -17.9 | 0.99 |  |
| 8 | 509 | 11.3 | 40 | +0.07 | +35.3 | 1.02 | 41 | -0.01 | -5.1 | 1.00 |  |

Best value: 5 · no change yet (best 5: not better in both halves)

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 133, replayed 130, recall 89 %, precision 92 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 740 | 16.4 | 40 | +0.32 | +239.4 | 1.09 | 36 | -0.39 | -288.6 | 0.87 |  |
| 3 (current) | 658 | 14.6 | 40 | +0.50 | +328.0 | 1.14 | 35 | -0.45 | -299.0 | 0.85 |  |
| 5 | 574 | 12.8 | 40 | +0.55 | +318.4 | 1.16 | 34 | -0.54 | -308.2 | 0.82 |  |

Best value: 3 · no change yet (current value is best)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 87, replayed 80, recall 89 %, precision 96 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 465 | 10.3 | 42 | +0.36 | +165.9 | 1.09 | 39 | -0.04 | -20.0 | 0.98 |  |
| 3 (current) | 418 | 9.3 | 41 | +0.19 | +77.9 | 1.05 | 39 | -0.10 | -41.6 | 0.96 |  |
| 5 | 366 | 8.1 | 41 | +0.22 | +80.4 | 1.06 | 39 | -0.11 | -38.6 | 0.96 |  |

Best value: 1 · no change yet (best 1: not better in both halves, neighbours disagree)

### HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)

Validation at current: stored 7, replayed 13, recall 14 %, precision 8 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 26 | 0.6 | 31 | +1.25 | +32.4 | 1.61 | 42 | +0.54 | +14.1 | 1.21 |  |
| 2 | 53 | 1.2 | 36 | +0.75 | +39.7 | 1.51 | 40 | -0.10 | -5.5 | 0.96 |  |
| 3 | 65 | 1.4 | 34 | +0.26 | +17.2 | 1.16 | 37 | -0.52 | -33.9 | 0.81 |  |
| 4 (current) | 74 | 1.6 | 34 | +0.19 | +13.8 | 1.11 | 36 | -0.61 | -44.9 | 0.79 |  |
| 6 | 106 | 2.4 | 36 | +0.14 | +14.9 | 1.07 | 42 | +0.19 | +20.4 | 1.07 |  |
| 8 | 123 | 2.7 | 37 | -0.03 | -3.9 | 0.98 | 40 | -0.04 | -5.0 | 0.99 |  |

Best value: 1 · no change yet (best 1: 26 alerts, replay unreliable)

### In FVG of HTF Flip Candle: (min gap bars, stop after N bars)

Validation: no stored alerts of this type for this chart -- replay unchecked.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (1, 10) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (1, 15) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (1, 20) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (1, 30) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (1, 40) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (2, 10) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (2, 15) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (2, 20) (current) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (2, 30) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (2, 40) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (3, 10) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (3, 15) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (3, 20) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (3, 30) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (3, 40) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (5, 10) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (5, 15) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (5, 20) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (5, 30) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |
| (5, 40) | 1 | 0.0 | 0 | -1.40 | -1.4 | 0.00 | 0 | -1.92 | -1.9 | 0.00 |  |

Best value: (1, 10) · no change yet (best (1, 10): 1 alerts, not better in both halves, neighbours disagree, replay unreliable)

### VWAP Bounce: min distance from major S/R (pts, 0 = no gate)

Validation at current: stored 21, replayed 24, recall 95 %, precision 83 %
Current = auto 6.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 532 | 11.8 | 43 | +0.46 | +247.3 | 1.12 | 38 | -0.15 | -77.8 | 0.94 |  |
| 2 | 397 | 8.8 | 43 | +0.42 | +168.2 | 1.11 | 38 | -0.17 | -68.0 | 0.93 |  |
| 4 | 287 | 6.4 | 43 | +0.28 | +80.2 | 1.08 | 35 | -0.48 | -136.4 | 0.81 |  |
| 6 (current) | 204 | 4.5 | 40 | +0.10 | +20.9 | 1.03 | 35 | -0.51 | -104.2 | 0.79 |  |
| 8 | 146 | 3.2 | 38 | +0.16 | +23.9 | 1.05 | 36 | -0.42 | -61.9 | 0.80 |  |
| 10 | 113 | 2.5 | 39 | +0.12 | +13.1 | 1.04 | 36 | -0.34 | -38.4 | 0.82 |  |

Best value: 0 · no change yet (best 0: not better in both halves)

## MNQ 3m (HTF 15m) -- 20499 bars 08/28 to 10/29

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 113, replayed 124, recall 82 %, precision 75 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 758 | 16.8 | 36 | -6.04 | -4576.2 | 0.76 | 38 | -2.15 | -1628.8 | 0.87 |  |
| 1 | 758 | 16.8 | 36 | -6.04 | -4576.2 | 0.76 | 38 | -2.15 | -1628.8 | 0.87 |  |
| 2 | 704 | 15.6 | 36 | -6.03 | -4242.0 | 0.76 | 38 | -2.20 | -1546.3 | 0.87 |  |
| 3 (current) | 664 | 14.8 | 36 | -5.44 | -3614.8 | 0.78 | 38 | -1.93 | -1278.7 | 0.89 |  |
| 5 | 588 | 13.1 | 36 | -7.45 | -4379.2 | 0.70 | 38 | -1.92 | -1129.1 | 0.89 |  |
| 8 | 514 | 11.4 | 36 | -6.00 | -3082.5 | 0.75 | 38 | -1.82 | -933.7 | 0.89 |  |

Best value: 8 · no change yet (best 8: not better in both halves, neighbours disagree)

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 109, replayed 104, recall 79 %, precision 83 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 699 | 15.5 | 38 | -3.71 | -2595.8 | 0.85 | 38 | -1.84 | -1287.2 | 0.89 |  |
| 3 (current) | 629 | 14.0 | 37 | -4.68 | -2946.8 | 0.81 | 37 | -2.55 | -1602.1 | 0.85 |  |
| 5 | 562 | 12.5 | 37 | -3.55 | -1993.2 | 0.85 | 37 | -2.03 | -1141.5 | 0.88 |  |

Best value: 5 · no change yet (best 5: neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 67, replayed 70, recall 91 %, precision 87 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 400 | 8.9 | 41 | -0.89 | -354.2 | 0.96 | 41 | +2.25 | +901.6 | 1.15 |  |
| 3 (current) | 349 | 7.8 | 38 | -4.43 | -1546.5 | 0.82 | 40 | +1.99 | +693.0 | 1.13 |  |
| 5 | 316 | 7.0 | 38 | -3.75 | -1184.8 | 0.85 | 41 | +2.72 | +858.7 | 1.18 |  |

Best value: 1 · no change yet (best 1: not better in both halves, neighbours disagree)

### HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)

Validation at current: stored 6, replayed 9, recall 17 %, precision 11 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 17 | 0.4 | 65 | +34.16 | +580.8 | 7.56 | 53 | +3.91 | +66.6 | 1.24 |  |
| 2 | 36 | 0.8 | 61 | +18.47 | +665.0 | 4.30 | 47 | +2.02 | +72.9 | 1.12 | ✱ |
| 3 | 46 | 1.0 | 59 | +20.99 | +965.5 | 4.86 | 50 | +5.20 | +239.2 | 1.34 | ✱ |
| 4 (current) | 54 | 1.2 | 57 | +22.34 | +1206.5 | 5.61 | 50 | +6.37 | +344.0 | 1.45 | ✱ |
| 6 | 76 | 1.7 | 54 | +15.97 | +1213.5 | 2.70 | 53 | +9.11 | +692.2 | 1.67 | ✱ |
| 8 | 91 | 2.0 | 49 | +11.10 | +1009.8 | 2.03 | 48 | +4.85 | +441.7 | 1.30 | ✱ |

Best value: 6 · no change yet (best 6: not better in both halves, neighbours disagree, replay unreliable)

### In FVG of HTF Flip Candle: (min gap bars, stop after N bars)

Validation: no stored alerts of this type for this chart -- replay unchecked.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (1, 10) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (1, 15) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (1, 20) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (1, 30) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (1, 40) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (2, 10) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (2, 15) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (2, 20) (current) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (2, 30) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (2, 40) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (3, 10) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (3, 15) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (3, 20) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (3, 30) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (3, 40) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (5, 10) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (5, 15) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (5, 20) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (5, 30) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |
| (5, 40) | 2 | 0.0 | 50 | -5.75 | -11.5 | 0.02 | 0 | -16.89 | -33.8 | 0.00 |  |

Best value: (1, 10) · no change yet (best (1, 10): 2 alerts, not better in both halves, neighbours disagree, replay unreliable)

### VWAP Bounce: min distance from major S/R (pts, 0 = no gate)

Validation at current: stored 9, replayed 9, recall 100 %, precision 100 %
Current = auto 60.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 103 | 2.3 | 42 | -3.11 | -320.8 | 0.85 | 42 | +1.73 | +178.4 | 1.13 |  |
| 20 | 68 | 1.5 | 40 | -3.38 | -229.8 | 0.84 | 43 | +2.75 | +187.2 | 1.22 |  |
| 40 | 40 | 0.9 | 45 | -2.94 | -117.5 | 0.87 | 40 | +2.54 | +101.8 | 1.23 |  |
| 60 (current) | 28 | 0.6 | 43 | -5.96 | -166.8 | 0.78 | 39 | +5.49 | +153.8 | 1.51 |  |
| 80 | 27 | 0.6 | 44 | -2.83 | -76.5 | 0.88 | 37 | +1.36 | +36.6 | 1.12 |  |

Best value: 60 · no change yet (current value is best)

## MES 2m (HTF 10m) -- 30749 bars 08/28 to 10/29

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 188, replayed 190, recall 82 %, precision 81 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1199 | 26.6 | 36 | -0.39 | -471.2 | 0.87 | 36 | -0.12 | -138.4 | 0.95 |  |
| 1 | 1199 | 26.6 | 36 | -0.39 | -471.2 | 0.87 | 36 | -0.12 | -138.4 | 0.95 |  |
| 2 | 1112 | 24.7 | 37 | -0.33 | -365.0 | 0.89 | 36 | -0.09 | -94.9 | 0.96 |  |
| 3 (current) | 1017 | 22.6 | 37 | -0.38 | -389.8 | 0.87 | 36 | -0.10 | -97.5 | 0.96 |  |
| 5 | 906 | 20.1 | 37 | -0.27 | -240.8 | 0.91 | 37 | -0.07 | -65.5 | 0.97 |  |
| 8 | 785 | 17.4 | 36 | -0.51 | -399.5 | 0.84 | 36 | -0.17 | -130.7 | 0.92 |  |

Best value: 5 · no change yet (best 5: neighbours disagree)

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 197, replayed 208, recall 88 %, precision 83 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1129 | 25.1 | 38 | -0.42 | -474.8 | 0.86 | 38 | +0.01 | +16.3 | 1.01 |  |
| 3 (current) | 1005 | 22.3 | 38 | -0.46 | -460.0 | 0.85 | 39 | +0.02 | +21.3 | 1.01 |  |
| 5 | 893 | 19.8 | 38 | -0.38 | -338.5 | 0.87 | 38 | +0.01 | +4.5 | 1.00 |  |

Best value: 5 · no change yet (best 5: not better in both halves, neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 133, replayed 128, recall 84 %, precision 88 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 671 | 14.9 | 38 | -0.63 | -422.2 | 0.81 | 37 | -0.09 | -59.7 | 0.96 |  |
| 3 (current) | 601 | 13.4 | 37 | -0.77 | -463.8 | 0.77 | 37 | -0.09 | -51.9 | 0.96 |  |
| 5 | 540 | 12.0 | 38 | -0.85 | -460.0 | 0.75 | 38 | -0.02 | -8.7 | 0.99 |  |

Best value: 5 · no change yet (best 5: not better in both halves, neighbours disagree)

### HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)

Validation at current: stored 2, replayed 24, recall 0 %, precision 0 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 34 | 0.8 | 56 | +1.61 | +54.8 | 1.74 | 62 | +1.53 | +52.1 | 2.04 | ✱ |
| 2 | 57 | 1.3 | 49 | +1.24 | +70.5 | 1.72 | 58 | +1.20 | +68.3 | 1.78 | ✱ |
| 3 | 88 | 2.0 | 47 | +1.44 | +126.5 | 1.89 | 52 | +0.50 | +43.6 | 1.26 | ✱ |
| 4 (current) | 107 | 2.4 | 47 | +1.44 | +154.0 | 1.88 | 50 | +0.38 | +40.8 | 1.20 | ✱ |
| 6 | 146 | 3.2 | 47 | +1.36 | +199.2 | 1.80 | 50 | +0.37 | +53.6 | 1.20 | ✱ |
| 8 | 172 | 3.8 | 48 | +1.76 | +302.8 | 2.12 | 52 | +0.69 | +118.5 | 1.38 | ✱ |

Best value: 8 · no change yet (best 8: replay unreliable)

### In FVG of HTF Flip Candle: (min gap bars, stop after N bars)

Validation: no stored alerts of this type for this chart -- replay unchecked.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (1, 10) | 3 | 0.1 | 0 | -0.50 | -1.5 | 0.00 | 0 | -3.52 | -10.6 | 0.00 |  |
| (1, 15) | 3 | 0.1 | 0 | -0.50 | -1.5 | 0.00 | 0 | -3.52 | -10.6 | 0.00 |  |
| (1, 20) | 3 | 0.1 | 0 | -0.50 | -1.5 | 0.00 | 0 | -3.52 | -10.6 | 0.00 |  |
| (1, 30) | 3 | 0.1 | 0 | -0.50 | -1.5 | 0.00 | 0 | -3.52 | -10.6 | 0.00 |  |
| (1, 40) | 3 | 0.1 | 0 | -0.50 | -1.5 | 0.00 | 0 | -3.52 | -10.6 | 0.00 |  |
| (2, 10) | 2 | 0.0 | 0 | -0.75 | -1.5 | 0.00 | 0 | -3.52 | -7.0 | 0.00 |  |
| (2, 15) | 2 | 0.0 | 0 | -0.75 | -1.5 | 0.00 | 0 | -3.52 | -7.0 | 0.00 |  |
| (2, 20) (current) | 2 | 0.0 | 0 | -0.75 | -1.5 | 0.00 | 0 | -3.52 | -7.0 | 0.00 |  |
| (2, 30) | 2 | 0.0 | 0 | -0.75 | -1.5 | 0.00 | 0 | -3.52 | -7.0 | 0.00 |  |
| (2, 40) | 2 | 0.0 | 0 | -0.75 | -1.5 | 0.00 | 0 | -3.52 | -7.0 | 0.00 |  |
| (3, 10) | 1 | 0.0 | 0 | -1.50 | -1.5 | 0.00 | 0 | -3.50 | -3.5 | 0.00 |  |
| (3, 15) | 1 | 0.0 | 0 | -1.50 | -1.5 | 0.00 | 0 | -3.50 | -3.5 | 0.00 |  |
| (3, 20) | 1 | 0.0 | 0 | -1.50 | -1.5 | 0.00 | 0 | -3.50 | -3.5 | 0.00 |  |
| (3, 30) | 1 | 0.0 | 0 | -1.50 | -1.5 | 0.00 | 0 | -3.50 | -3.5 | 0.00 |  |
| (3, 40) | 1 | 0.0 | 0 | -1.50 | -1.5 | 0.00 | 0 | -3.50 | -3.5 | 0.00 |  |
| (5, 10) | 1 | 0.0 | 0 | -1.50 | -1.5 | 0.00 | 0 | -3.50 | -3.5 | 0.00 |  |
| (5, 15) | 1 | 0.0 | 0 | -1.50 | -1.5 | 0.00 | 0 | -3.50 | -3.5 | 0.00 |  |
| (5, 20) | 1 | 0.0 | 0 | -1.50 | -1.5 | 0.00 | 0 | -3.50 | -3.5 | 0.00 |  |
| (5, 30) | 1 | 0.0 | 0 | -1.50 | -1.5 | 0.00 | 0 | -3.50 | -3.5 | 0.00 |  |
| (5, 40) | 1 | 0.0 | 0 | -1.50 | -1.5 | 0.00 | 0 | -3.50 | -3.5 | 0.00 |  |

Best value: (3, 10) · no change yet (best (3, 10): 1 alerts, not better in both halves, neighbours disagree, replay unreliable)

### VWAP Bounce: min distance from major S/R (pts, 0 = no gate)

Validation at current: stored 66, replayed 62, recall 91 %, precision 97 %
Current = auto 6.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1031 | 22.9 | 42 | +0.10 | +103.2 | 1.04 | 38 | -0.10 | -106.7 | 0.94 |  |
| 2 | 616 | 13.7 | 45 | +0.55 | +340.0 | 1.21 | 40 | +0.01 | +3.9 | 1.00 |  |
| 4 | 374 | 8.3 | 46 | +0.62 | +232.0 | 1.24 | 39 | +0.06 | +21.8 | 1.03 |  |
| 6 (current) | 252 | 5.6 | 41 | +0.09 | +23.0 | 1.03 | 39 | -0.01 | -1.5 | 1.00 |  |
| 8 | 216 | 4.8 | 41 | -0.24 | -51.5 | 0.91 | 39 | -0.06 | -13.1 | 0.96 |  |
| 10 | 182 | 4.0 | 40 | -0.93 | -168.5 | 0.66 | 39 | -0.18 | -33.5 | 0.88 |  |

Best value: 2 · no change yet (best 2: not better in both halves, neighbours disagree)

## MGC 2m (HTF 10m) -- 30793 bars 08/28 to 10/29

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 168, replayed 175, recall 79 %, precision 76 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1155 | 25.7 | 37 | -0.22 | -254.6 | 0.93 | 41 | +0.08 | +94.8 | 1.04 |  |
| 1 | 1155 | 25.7 | 37 | -0.22 | -254.6 | 0.93 | 41 | +0.08 | +94.8 | 1.04 |  |
| 2 | 1084 | 24.1 | 37 | -0.14 | -148.2 | 0.96 | 41 | +0.14 | +150.4 | 1.06 |  |
| 3 (current) | 1010 | 22.4 | 38 | -0.05 | -51.1 | 0.98 | 41 | +0.13 | +131.9 | 1.06 |  |
| 5 | 905 | 20.1 | 39 | +0.14 | +128.3 | 1.05 | 42 | +0.16 | +146.8 | 1.07 |  |
| 8 | 765 | 17.0 | 38 | +0.06 | +45.3 | 1.02 | 41 | +0.12 | +91.2 | 1.05 |  |

Best value: 5 · no change yet (best 5: not better in both halves)

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 180, replayed 196, recall 88 %, precision 81 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1126 | 25.0 | 39 | +0.13 | +144.4 | 1.04 | 41 | +0.12 | +134.5 | 1.05 |  |
| 3 (current) | 997 | 22.2 | 39 | +0.19 | +190.1 | 1.06 | 41 | +0.13 | +128.1 | 1.06 |  |
| 5 | 876 | 19.5 | 41 | +0.49 | +430.8 | 1.16 | 42 | +0.27 | +238.6 | 1.13 | ✱ |

Best value: 5 · no change yet (best 5: neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 109, replayed 110, recall 88 %, precision 87 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 697 | 15.5 | 38 | +0.12 | +83.7 | 1.04 | 40 | +0.03 | +21.5 | 1.01 |  |
| 3 (current) | 619 | 13.8 | 38 | +0.26 | +159.9 | 1.08 | 39 | -0.02 | -12.4 | 0.99 |  |
| 5 | 553 | 12.3 | 39 | +0.39 | +217.3 | 1.13 | 39 | -0.07 | -40.4 | 0.97 |  |

Best value: 5 · no change yet (best 5: not better in both halves, neighbours disagree)

### HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)

Validation at current: stored 6, replayed 11, recall 17 %, precision 9 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 41 | 0.9 | 39 | +1.32 | +54.3 | 1.71 | 44 | +0.28 | +11.5 | 1.15 |  |
| 2 | 67 | 1.5 | 31 | +0.15 | +9.8 | 1.07 | 39 | -0.33 | -22.3 | 0.85 |  |
| 3 | 91 | 2.0 | 33 | -0.09 | -8.1 | 0.96 | 36 | -0.50 | -45.9 | 0.79 |  |
| 4 (current) | 114 | 2.5 | 33 | +0.17 | +19.9 | 1.09 | 38 | -0.28 | -31.5 | 0.88 |  |
| 6 | 143 | 3.2 | 34 | +0.22 | +30.8 | 1.11 | 38 | +0.05 | +6.7 | 1.02 |  |
| 8 | 165 | 3.7 | 35 | +0.16 | +25.9 | 1.08 | 39 | +0.07 | +12.1 | 1.03 |  |

Best value: 1 · no change yet (best 1: not better in both halves, neighbours disagree, replay unreliable)

### In FVG of HTF Flip Candle: (min gap bars, stop after N bars)

Validation: no stored alerts of this type for this chart -- replay unchecked.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (1, 10) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (1, 15) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (1, 20) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (1, 30) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (1, 40) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (2, 10) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (2, 15) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (2, 20) (current) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (2, 30) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (2, 40) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (3, 10) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (3, 15) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (3, 20) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (3, 30) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (3, 40) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (5, 10) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (5, 15) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (5, 20) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (5, 30) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |
| (5, 40) | 0 | 0.0 | 0 | +0.00 | +0.0 | 0.00 | 0 | +0.00 | +0.0 | 0.00 |  |

Best value: (1, 10) · no change yet (best (1, 10): 0 alerts, not better in both halves, neighbours disagree, replay unreliable)

### VWAP Bounce: min distance from major S/R (pts, 0 = no gate)

Validation at current: stored 37, replayed 45, recall 100 %, precision 82 %
Current = auto 6.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 790 | 17.6 | 41 | +0.28 | +221.1 | 1.08 | 40 | +0.00 | +3.5 | 1.00 |  |
| 2 | 618 | 13.7 | 40 | +0.30 | +186.3 | 1.09 | 39 | -0.11 | -69.3 | 0.94 |  |
| 4 | 431 | 9.6 | 39 | +0.08 | +36.2 | 1.03 | 37 | -0.26 | -113.6 | 0.87 |  |
| 6 (current) | 312 | 6.9 | 38 | +0.17 | +54.5 | 1.06 | 39 | -0.16 | -49.6 | 0.91 |  |
| 8 | 224 | 5.0 | 36 | -0.30 | -67.3 | 0.89 | 41 | -0.00 | -0.0 | 1.00 |  |
| 10 | 175 | 3.9 | 34 | -0.38 | -67.0 | 0.83 | 41 | -0.01 | -2.3 | 0.99 |  |

Best value: 0 · **worth considering: 0**


<!-- SUMMARY
MES 3m LTF EMA20 Pierce: **worth considering: 8** (n=709) | HTF EMA9 Pierce: no change yet (best 1: not better in both halves, neighbours disagree) (n=653) | HTF EMA20 Pierce: no change yet (best 5: not better in both halves, neighbours disagree) (n=398) | HTF Pullback Entry - Structure Confirmed: no change yet (best 1: 26 alerts, not better in both halves, replay unreliable) (n=81, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 0 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=0, unchecked/unreliable) | VWAP Bounce: **worth considering: 2** (n=180)
MGC 3m LTF EMA20 Pierce: no change yet (best 5: not better in both halves) (n=676) | HTF EMA9 Pierce: no change yet (current value is best) (n=658) | HTF EMA20 Pierce: no change yet (best 1: not better in both halves, neighbours disagree) (n=418) | HTF Pullback Entry - Structure Confirmed: no change yet (best 1: 26 alerts, replay unreliable) (n=74, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 1 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=1, unchecked/unreliable) | VWAP Bounce: no change yet (best 0: not better in both halves) (n=204)
MNQ 3m LTF EMA20 Pierce: no change yet (best 8: not better in both halves, neighbours disagree) (n=664) | HTF EMA9 Pierce: no change yet (best 5: neighbours disagree) (n=629) | HTF EMA20 Pierce: no change yet (best 1: not better in both halves, neighbours disagree) (n=349) | HTF Pullback Entry - Structure Confirmed: no change yet (best 6: not better in both halves, neighbours disagree, replay unreliable) (n=54, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 2 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=2, unchecked/unreliable) | VWAP Bounce: no change yet (current value is best) (n=28)
MES 2m LTF EMA20 Pierce: no change yet (best 5: neighbours disagree) (n=1017) | HTF EMA9 Pierce: no change yet (best 5: not better in both halves, neighbours disagree) (n=1005) | HTF EMA20 Pierce: no change yet (best 5: not better in both halves, neighbours disagree) (n=601) | HTF Pullback Entry - Structure Confirmed: no change yet (best 8: replay unreliable) (n=107, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (3, 10): 1 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=2, unchecked/unreliable) | VWAP Bounce: no change yet (best 2: not better in both halves, neighbours disagree) (n=252)
MGC 2m LTF EMA20 Pierce: no change yet (best 5: not better in both halves) (n=1010) | HTF EMA9 Pierce: no change yet (best 5: neighbours disagree) (n=997) | HTF EMA20 Pierce: no change yet (best 5: not better in both halves, neighbours disagree) (n=619) | HTF Pullback Entry - Structure Confirmed: no change yet (best 1: not better in both halves, neighbours disagree, replay unreliable) (n=114, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 0 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=0, unchecked/unreliable) | VWAP Bounce: **worth considering: 0** (n=312)
-->
