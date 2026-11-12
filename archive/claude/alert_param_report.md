# CBC alert parameter sweep -- 2026-11-12 09:58 ET

Alert Feed: 44310 alerts (10/19 to 11/12). Bars: BarFeed, last 60 days. Validation window = days with stored alerts.
Outcome (a) = exit at first opposite HTF CBC flip / 17:00 ET / 2 h. (b) = 1.3 ATR stop / 2.0 ATR target (both in one candle = stop). Points per contract-point, before costs. ✱ = positive in both halves of the data under both rules. Validation: recall = stored alerts the replay reproduces (±1 bar), precision = replayed alerts that were stored. Unreliable = recall or precision < 70 %.

Notes: "Option 2: Reverse" pierces are scored in the reversed direction (as the alert says). LTF cooldown 0 and 1 are identical (a pierce needs the previous candle not touching the line). HTF EMA pierces use the setup-engine direction (flip counts on the HTF candle close) and the away / toward-late (1 pt) gate. 2m charts use their own 10m HTF fields from the BarFeed. Pullback-Structure replay rebuilds HTF swing pivots from the chart candles and does not reproduce the live alerts well (few stored alerts). In FVG alerts: none stored in the Alert Feed so far. Verdict rule: "worth considering" needs 30+ alerts, better than current in both halves under both rules, neighbouring values also better, and a reliable replay.

Settings: live CBC v10.87 (pine/CBC_v10_87.pine); claude/settings_sync_report.md (11/12 09:45 ET) shows no mismatch (1 known, unrelated). claude/CBC_SETTINGS.md lists only ats_/bot_/xr_/ema_ inputs, so the ⑤ Alerts current values come from the newest Pine defaults: LTF EMA20 cooldown 3, PB window 4, FVG gap 2 / max 20, VWAP Bounce vb_tw_sym "MGC 3m 0300-1700 0.01, MGC 2m 0000-2400 0.01, MES 3m 0000-2400 4, MES 2m 0000-2400 4" + auto (MES/MGC 6, MNQ 60) -- unchanged since v10.83 (current rows: MES 3m/2m 4, MGC 2m 0, MGC 3m tod, MNQ 3m 60). This run is a late re-run (09:58 ET 11/12); no report was written for 11/10 or 11/11.

Since last run (vs the 11/09 17:06 ET run): Alert Feed 37235 -> 44310 alerts (last 11/12); bars now 09/11-11/12. **Data gap: no MES 3m or MNQ 3m alerts reached the Alert Feed on 11/10 and 11/11** (0 each, vs 41 / 63 on 11/09; a few again on 11/12), while MES 2m / MGC 2m / MGC 3m / 5m charts posted normally -- check those two TradingView alerts. So MES 3m / MNQ 3m validation counts barely moved and MES 3m VWAP Bounce still has only 3 stored alerts since 11/08 (still flagged unreliable on that small sample). Still flagged: MES 3m LTF EMA20 cooldown 8 (3rd run; (a) +3.5 vs -360.8, (b) +143.8 vs -30.0 -- (a) now only just positive) and MGC 2m LTF EMA20 cooldown 5 (7th run; (a) -280.7 vs -459.4, (b) +74.5 vs +2.7, still negative under (a)). MES 3m VWAP 4 weakened ((a) +1.0, (b) +42.8; 0 now tops the sum but not in both halves). VWAP replays at the v10.83 defaults validate well: MGC 3m tod 54 stored 100/84 %, MES 2m 35 stored 100/97 %, MGC 2m 65 stored 100/100 %. Still unreliable: MES 2m LTF EMA20 (67/69 %), MNQ 3m HTF EMA9 (76/67 %), Pullback-Structure everywhere; still no In FVG alerts in the Alert Feed.

## MES 3m (HTF 15m) -- 20438 bars 09/11 to 11/12

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 212, replayed 217, recall 81 %, precision 79 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 775 | 17.2 | 41 | -0.42 | -322.2 | 0.90 | 40 | +0.02 | +14.3 | 1.01 |  |
| 1 | 775 | 17.2 | 41 | -0.42 | -322.2 | 0.90 | 40 | +0.02 | +14.3 | 1.01 |  |
| 2 | 718 | 16.0 | 41 | -0.40 | -290.8 | 0.90 | 40 | +0.02 | +15.6 | 1.01 |  |
| 3 (current) | 674 | 15.0 | 40 | -0.54 | -360.8 | 0.87 | 40 | -0.04 | -30.0 | 0.99 |  |
| 5 | 597 | 13.3 | 39 | -0.44 | -262.2 | 0.89 | 38 | -0.19 | -114.3 | 0.94 |  |
| 8 | 509 | 11.3 | 42 | +0.01 | +3.5 | 1.00 | 41 | +0.28 | +143.8 | 1.10 |  |

Best value: 8 · **worth considering: 8**

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 206, replayed 225, recall 82 %, precision 75 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 692 | 15.4 | 42 | +0.87 | +600.2 | 1.24 | 43 | +0.57 | +391.4 | 1.20 | ✱ |
| 3 (current) | 621 | 13.8 | 42 | +0.87 | +542.8 | 1.24 | 43 | +0.55 | +342.8 | 1.20 | ✱ |
| 5 | 537 | 11.9 | 41 | +0.48 | +255.2 | 1.12 | 43 | +0.57 | +308.4 | 1.21 | ✱ |

Best value: 1 · no change yet (best 1: neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 127, replayed 138, recall 83 %, precision 77 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 401 | 8.9 | 41 | -0.91 | -366.2 | 0.80 | 39 | -0.23 | -94.0 | 0.92 |  |
| 3 (current) | 357 | 7.9 | 42 | -1.01 | -361.5 | 0.78 | 40 | -0.21 | -73.6 | 0.93 |  |
| 5 | 325 | 7.2 | 42 | -1.31 | -424.8 | 0.73 | 39 | -0.30 | -97.5 | 0.90 |  |

Best value: 3 · no change yet (current value is best)

### HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)

Validation at current: stored 3, replayed 19, recall 0 %, precision 0 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 24 | 0.5 | 42 | +0.23 | +5.5 | 1.08 | 46 | +0.58 | +13.9 | 1.26 |  |
| 2 | 40 | 0.9 | 40 | +0.44 | +17.8 | 1.18 | 45 | +0.53 | +21.1 | 1.20 |  |
| 3 | 55 | 1.2 | 35 | -2.05 | -112.5 | 0.54 | 38 | -0.66 | -36.1 | 0.80 |  |
| 4 (current) | 72 | 1.6 | 38 | -1.23 | -88.8 | 0.65 | 46 | +0.20 | +14.6 | 1.07 |  |
| 6 | 90 | 2.0 | 40 | -0.35 | -31.8 | 0.88 | 51 | +0.74 | +66.3 | 1.29 |  |
| 8 | 106 | 2.4 | 40 | -0.56 | -59.5 | 0.81 | 53 | +0.83 | +87.8 | 1.33 |  |

Best value: 2 · no change yet (best 2: not better in both halves, neighbours disagree, replay unreliable)

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

Validation at current: stored 3, replayed 2, recall 67 %, precision 100 % -- **unreliable**
Current = 4 (v10.83 default changed from auto 6; vb_tw_sym "MES 3m 0000-2400 4"). Validation uses stored alerts from 11/08 on.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 636 | 14.1 | 44 | +0.08 | +50.5 | 1.02 | 39 | +0.02 | +15.6 | 1.01 |  |
| 2 | 417 | 9.3 | 44 | +0.07 | +27.8 | 1.02 | 39 | +0.00 | +1.1 | 1.00 |  |
| 4 (current) | 273 | 6.1 | 41 | +0.00 | +1.0 | 1.00 | 38 | +0.16 | +42.8 | 1.06 |  |
| 6 | 186 | 4.1 | 38 | -0.45 | -84.0 | 0.90 | 35 | -0.06 | -10.9 | 0.98 |  |
| 8 | 155 | 3.4 | 37 | -0.16 | -25.0 | 0.96 | 34 | -0.19 | -29.1 | 0.93 |  |
| 10 | 126 | 2.8 | 37 | -0.19 | -24.2 | 0.94 | 33 | -0.39 | -49.6 | 0.84 |  |

Best value: 0 · no change yet (best 0: not better in both halves, neighbours disagree, replay unreliable)

## MGC 3m (HTF 15m) -- 20439 bars 09/11 to 11/12

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 267, replayed 301, recall 94 %, precision 83 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 787 | 17.5 | 40 | +0.49 | +385.7 | 1.13 | 41 | +0.21 | +163.6 | 1.08 | ✱ |
| 1 | 787 | 17.5 | 40 | +0.49 | +385.7 | 1.13 | 41 | +0.21 | +163.6 | 1.08 | ✱ |
| 2 | 740 | 16.4 | 40 | +0.35 | +259.1 | 1.09 | 42 | +0.25 | +182.1 | 1.09 | ✱ |
| 3 (current) | 693 | 15.4 | 40 | +0.44 | +308.1 | 1.12 | 42 | +0.28 | +191.0 | 1.10 | ✱ |
| 5 | 611 | 13.6 | 40 | +0.65 | +394.5 | 1.18 | 42 | +0.17 | +106.7 | 1.07 |  |
| 8 | 522 | 11.6 | 40 | +0.47 | +243.4 | 1.13 | 41 | +0.15 | +78.2 | 1.06 | ✱ |

Best value: 0 · no change yet (best 0: not better in both halves)

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 240, replayed 265, recall 82 %, precision 73 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 737 | 16.4 | 41 | +0.46 | +337.7 | 1.13 | 40 | +0.05 | +40.3 | 1.02 |  |
| 3 (current) | 657 | 14.6 | 41 | +0.39 | +256.6 | 1.11 | 39 | -0.06 | -39.8 | 0.98 |  |
| 5 | 572 | 12.7 | 40 | +0.50 | +287.5 | 1.14 | 38 | -0.15 | -87.5 | 0.94 |  |

Best value: 1 · no change yet (best 1: not better in both halves, neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 152, replayed 151, recall 80 %, precision 81 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 454 | 10.1 | 39 | -0.11 | -48.7 | 0.97 | 38 | -0.26 | -118.8 | 0.91 |  |
| 3 (current) | 406 | 9.0 | 37 | -0.55 | -224.5 | 0.86 | 36 | -0.45 | -182.8 | 0.85 |  |
| 5 | 357 | 7.9 | 38 | -0.48 | -172.2 | 0.87 | 38 | -0.38 | -136.5 | 0.87 |  |

Best value: 1 · no change yet (best 1: neighbours disagree)

### HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)

Validation at current: stored 11, replayed 25, recall 9 %, precision 4 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 33 | 0.7 | 33 | +1.35 | +44.7 | 1.65 | 42 | +0.14 | +4.5 | 1.05 |  |
| 2 | 53 | 1.2 | 36 | +0.81 | +42.7 | 1.48 | 40 | -0.31 | -16.2 | 0.88 |  |
| 3 | 68 | 1.5 | 35 | +1.14 | +77.4 | 1.70 | 38 | -0.48 | -32.9 | 0.81 |  |
| 4 (current) | 76 | 1.7 | 36 | +1.75 | +133.3 | 2.05 | 38 | -0.45 | -34.4 | 0.83 |  |
| 6 | 103 | 2.3 | 38 | +1.72 | +177.5 | 2.01 | 44 | +0.17 | +17.2 | 1.07 |  |
| 8 | 117 | 2.6 | 36 | +1.21 | +141.3 | 1.65 | 42 | -0.13 | -14.8 | 0.95 |  |

Best value: 6 · no change yet (best 6: replay unreliable)

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

Validation at current: stored 54, replayed 64, recall 100 %, precision 84 %
Current = tod: v10.75 time-of-day rule (no gate 03:00-17:00 ET, auto 6 in Asia); validated on stored alerts from 11/06 on (older alerts used auto 6 all day). Plain values apply all day.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 528 | 11.7 | 41 | +0.55 | +288.2 | 1.13 | 38 | -0.07 | -37.9 | 0.97 |  |
| 2 | 402 | 8.9 | 42 | +0.70 | +280.8 | 1.18 | 39 | -0.04 | -15.9 | 0.98 |  |
| 4 | 299 | 6.6 | 42 | +0.61 | +182.2 | 1.17 | 36 | -0.38 | -112.3 | 0.85 |  |
| 6 | 195 | 4.3 | 41 | +0.50 | +98.1 | 1.14 | 35 | -0.62 | -120.9 | 0.75 |  |
| 8 | 137 | 3.0 | 42 | +0.88 | +120.4 | 1.29 | 37 | -0.48 | -65.2 | 0.78 |  |
| 10 | 103 | 2.3 | 44 | +1.36 | +140.2 | 1.54 | 37 | -0.46 | -47.0 | 0.77 |  |
| tod (current) | 341 | 7.6 | 44 | +1.11 | +378.4 | 1.31 | 40 | +0.04 | +14.9 | 1.02 | ✱ |

Best value: tod · no change yet (current value is best)

## MNQ 3m (HTF 15m) -- 20440 bars 09/11 to 11/12

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 212, replayed 224, recall 89 %, precision 84 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 722 | 16.0 | 38 | -0.50 | -360.5 | 0.98 | 41 | +0.15 | +111.3 | 1.01 |  |
| 1 | 722 | 16.0 | 38 | -0.50 | -360.5 | 0.98 | 41 | +0.15 | +111.3 | 1.01 |  |
| 2 | 673 | 15.0 | 38 | -0.86 | -580.8 | 0.97 | 41 | -0.13 | -88.7 | 0.99 |  |
| 3 (current) | 636 | 14.1 | 38 | -0.52 | -327.8 | 0.98 | 41 | +0.17 | +108.7 | 1.01 |  |
| 5 | 564 | 12.5 | 37 | -2.32 | -1306.8 | 0.92 | 40 | -0.29 | -164.8 | 0.99 |  |
| 8 | 494 | 11.0 | 40 | +1.25 | +617.5 | 1.05 | 42 | +1.09 | +537.9 | 1.06 |  |

Best value: 8 · no change yet (best 8: not better in both halves, neighbours disagree)

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 173, replayed 196, recall 76 %, precision 67 % -- **unreliable**
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 656 | 14.6 | 39 | +3.09 | +2024.8 | 1.11 | 40 | -0.82 | -538.7 | 0.96 |  |
| 3 (current) | 595 | 13.2 | 40 | +4.02 | +2392.5 | 1.15 | 39 | -0.98 | -585.1 | 0.95 |  |
| 5 | 524 | 11.6 | 40 | +3.66 | +1916.0 | 1.14 | 40 | -0.42 | -221.0 | 0.98 |  |

Best value: 3 · no change yet (current value is best)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 110, replayed 127, recall 89 %, precision 77 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 366 | 8.1 | 41 | +1.79 | +654.2 | 1.07 | 43 | +3.58 | +1308.9 | 1.20 |  |
| 3 (current) | 318 | 7.1 | 39 | -1.33 | -421.8 | 0.95 | 42 | +2.71 | +862.2 | 1.15 |  |
| 5 | 288 | 6.4 | 39 | -1.70 | -489.5 | 0.94 | 43 | +4.00 | +1153.2 | 1.22 |  |

Best value: 1 · no change yet (best 1: neighbours disagree)

### HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)

Validation at current: stored 11, replayed 20, recall 9 %, precision 5 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 18 | 0.4 | 50 | +17.06 | +307.0 | 2.01 | 50 | -2.13 | -38.4 | 0.92 |  |
| 2 | 34 | 0.8 | 53 | +10.60 | +360.2 | 1.93 | 47 | +2.70 | +91.9 | 1.13 |  |
| 3 | 42 | 0.9 | 50 | +15.00 | +630.0 | 2.40 | 48 | +3.41 | +143.4 | 1.17 |  |
| 4 (current) | 52 | 1.2 | 48 | +15.21 | +791.0 | 2.46 | 46 | +3.07 | +159.6 | 1.16 |  |
| 6 | 75 | 1.7 | 45 | +5.74 | +430.5 | 1.31 | 51 | +4.45 | +333.7 | 1.23 | ✱ |
| 8 | 88 | 2.0 | 43 | +1.80 | +158.5 | 1.09 | 48 | +1.84 | +161.6 | 1.09 |  |

Best value: 4 · no change yet (current value is best)

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

Validation at current: stored 10, replayed 12, recall 100 %, precision 83 %
Current = auto 60.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 85 | 1.9 | 44 | +6.37 | +541.5 | 1.27 | 40 | +1.68 | +142.4 | 1.11 |  |
| 20 | 57 | 1.3 | 44 | +13.19 | +752.0 | 1.57 | 40 | +3.63 | +206.8 | 1.25 |  |
| 40 | 40 | 0.9 | 50 | +12.33 | +493.2 | 1.54 | 42 | +6.71 | +268.2 | 1.51 |  |
| 60 (current) | 30 | 0.7 | 43 | -2.56 | -76.8 | 0.90 | 43 | +11.92 | +357.7 | 1.99 |  |
| 80 | 27 | 0.6 | 44 | +0.19 | +5.0 | 1.01 | 37 | +2.06 | +55.7 | 1.15 |  |

Best value: 20 · no change yet (best 20: not better in both halves)

## MES 2m (HTF 10m) -- 30658 bars 09/11 to 11/12

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 405, replayed 392, recall 67 %, precision 69 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1173 | 26.1 | 37 | -0.47 | -550.0 | 0.86 | 38 | +0.01 | +10.7 | 1.00 |  |
| 1 | 1173 | 26.1 | 37 | -0.47 | -550.0 | 0.86 | 38 | +0.01 | +10.7 | 1.00 |  |
| 2 | 1096 | 24.4 | 38 | -0.40 | -438.8 | 0.88 | 38 | +0.04 | +42.2 | 1.02 |  |
| 3 (current) | 1004 | 22.3 | 37 | -0.44 | -441.2 | 0.87 | 38 | +0.05 | +47.0 | 1.02 |  |
| 5 | 898 | 20.0 | 37 | -0.30 | -265.8 | 0.91 | 39 | +0.09 | +78.5 | 1.04 |  |
| 8 | 779 | 17.3 | 37 | -0.38 | -299.8 | 0.89 | 38 | +0.01 | +9.7 | 1.01 |  |

Best value: 5 · no change yet (best 5: replay unreliable)

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 370, replayed 392, recall 82 %, precision 78 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1063 | 23.6 | 40 | +0.10 | +109.2 | 1.03 | 40 | +0.08 | +88.7 | 1.04 |  |
| 3 (current) | 945 | 21.0 | 40 | +0.20 | +187.0 | 1.06 | 41 | +0.13 | +126.0 | 1.06 | ✱ |
| 5 | 838 | 18.6 | 40 | +0.40 | +336.0 | 1.13 | 40 | +0.09 | +71.8 | 1.04 | ✱ |

Best value: 5 · no change yet (best 5: not better in both halves, neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 229, replayed 230, recall 84 %, precision 83 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 587 | 13.0 | 42 | -0.03 | -16.2 | 0.99 | 39 | -0.03 | -14.9 | 0.99 |  |
| 3 (current) | 531 | 11.8 | 41 | -0.14 | -73.5 | 0.96 | 39 | +0.04 | +19.8 | 1.02 |  |
| 5 | 485 | 10.8 | 42 | -0.10 | -47.2 | 0.97 | 40 | +0.18 | +87.2 | 1.08 |  |

Best value: 5 · no change yet (best 5: neighbours disagree)

### HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)

Validation at current: stored 6, replayed 54, recall 17 %, precision 2 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 39 | 0.9 | 56 | +1.61 | +62.8 | 1.67 | 56 | +1.40 | +54.7 | 1.73 |  |
| 2 | 63 | 1.4 | 48 | +1.01 | +63.8 | 1.53 | 51 | +0.60 | +37.6 | 1.27 |  |
| 3 | 94 | 2.1 | 43 | +0.51 | +47.8 | 1.28 | 48 | +0.50 | +47.2 | 1.22 |  |
| 4 (current) | 117 | 2.6 | 41 | +0.66 | +77.8 | 1.37 | 49 | +0.57 | +66.8 | 1.25 |  |
| 6 | 157 | 3.5 | 42 | +0.95 | +149.0 | 1.50 | 50 | +0.72 | +112.9 | 1.34 | ✱ |
| 8 | 185 | 4.1 | 43 | +1.09 | +202.5 | 1.62 | 50 | +0.78 | +143.5 | 1.37 | ✱ |

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

Validation at current: stored 35, replayed 36, recall 100 %, precision 97 %
Current = 4 (v10.83 default changed from auto 6; vb_tw_sym "MES 2m 0000-2400 4"). Validation uses stored alerts from 11/08 on.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 912 | 20.3 | 42 | +0.17 | +154.0 | 1.06 | 37 | -0.15 | -133.3 | 0.93 |  |
| 2 | 584 | 13.0 | 43 | +0.39 | +225.2 | 1.12 | 38 | -0.12 | -70.1 | 0.94 |  |
| 4 (current) | 381 | 8.5 | 44 | +0.76 | +290.5 | 1.25 | 39 | +0.11 | +42.3 | 1.05 |  |
| 6 | 262 | 5.8 | 40 | +0.42 | +110.8 | 1.12 | 38 | +0.04 | +11.1 | 1.02 |  |
| 8 | 219 | 4.9 | 39 | -0.07 | -15.8 | 0.98 | 37 | -0.08 | -16.7 | 0.96 |  |
| 10 | 179 | 4.0 | 38 | -0.60 | -107.8 | 0.82 | 36 | -0.35 | -62.3 | 0.83 |  |

Best value: 4 · no change yet (current value is best)

## MGC 2m (HTF 10m) -- 30656 bars 09/11 to 11/12

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 382, replayed 417, recall 82 %, precision 75 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1191 | 26.5 | 38 | -0.58 | -693.4 | 0.83 | 40 | -0.01 | -12.5 | 1.00 |  |
| 1 | 1191 | 26.5 | 38 | -0.58 | -693.4 | 0.83 | 40 | -0.01 | -12.5 | 1.00 |  |
| 2 | 1118 | 24.8 | 38 | -0.49 | -545.0 | 0.86 | 40 | +0.02 | +22.1 | 1.01 |  |
| 3 (current) | 1046 | 23.2 | 38 | -0.44 | -459.4 | 0.87 | 40 | +0.00 | +2.7 | 1.00 |  |
| 5 | 937 | 20.8 | 39 | -0.30 | -280.7 | 0.91 | 40 | +0.08 | +74.5 | 1.04 |  |
| 8 | 784 | 17.4 | 38 | -0.25 | -195.8 | 0.93 | 40 | -0.05 | -39.9 | 0.98 |  |

Best value: 5 · **worth considering: 5**

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 349, replayed 397, recall 86 %, precision 75 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1095 | 24.3 | 40 | +0.70 | +767.4 | 1.23 | 41 | +0.16 | +171.4 | 1.07 |  |
| 3 (current) | 976 | 21.7 | 40 | +0.54 | +531.7 | 1.17 | 41 | +0.17 | +165.4 | 1.08 |  |
| 5 | 858 | 19.1 | 41 | +0.54 | +461.4 | 1.17 | 42 | +0.27 | +232.2 | 1.13 |  |

Best value: 1 · no change yet (best 1: not better in both halves, neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 220, replayed 234, recall 87 %, precision 82 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 694 | 15.4 | 38 | +0.21 | +147.1 | 1.07 | 42 | +0.12 | +81.9 | 1.05 |  |
| 3 (current) | 606 | 13.5 | 38 | +0.22 | +135.0 | 1.07 | 41 | +0.08 | +50.3 | 1.04 |  |
| 5 | 541 | 12.0 | 39 | +0.48 | +260.7 | 1.15 | 41 | +0.10 | +56.0 | 1.05 |  |

Best value: 5 · no change yet (best 5: not better in both halves, neighbours disagree)

### HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)

Validation at current: stored 9, replayed 28, recall 11 %, precision 4 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 39 | 0.9 | 31 | +1.13 | +44.2 | 1.59 | 38 | -0.28 | -10.9 | 0.87 |  |
| 2 | 64 | 1.4 | 28 | +0.02 | +1.5 | 1.01 | 36 | -0.68 | -43.6 | 0.71 |  |
| 3 | 83 | 1.8 | 28 | -0.22 | -18.4 | 0.90 | 35 | -0.69 | -57.4 | 0.71 |  |
| 4 (current) | 107 | 2.4 | 29 | -0.17 | -18.6 | 0.92 | 36 | -0.45 | -47.6 | 0.80 |  |
| 6 | 137 | 3.0 | 31 | +0.12 | +16.9 | 1.06 | 36 | -0.49 | -66.9 | 0.78 |  |
| 8 | 157 | 3.5 | 31 | +0.48 | +75.5 | 1.24 | 36 | -0.51 | -80.0 | 0.78 |  |

Best value: 1 · no change yet (best 1: replay unreliable)

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

Validation at current: stored 65, replayed 66, recall 100 %, precision 100 %
Current = 0 (v10.83 default changed from auto 6; vb_tw_sym "MGC 2m 0000-2400 0.01"). Validation uses stored alerts from 11/08 on.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 (current) | 787 | 17.5 | 42 | +0.57 | +452.1 | 1.17 | 40 | +0.07 | +52.5 | 1.03 |  |
| 2 | 628 | 14.0 | 40 | +0.35 | +221.6 | 1.10 | 39 | -0.06 | -36.0 | 0.97 |  |
| 4 | 452 | 10.0 | 40 | +0.07 | +33.5 | 1.02 | 37 | -0.31 | -138.3 | 0.85 |  |
| 6 | 313 | 7.0 | 40 | +0.10 | +32.1 | 1.03 | 39 | -0.17 | -52.0 | 0.91 |  |
| 8 | 225 | 5.0 | 39 | -0.04 | -8.8 | 0.99 | 40 | -0.07 | -15.3 | 0.96 |  |
| 10 | 172 | 3.8 | 38 | +0.10 | +17.4 | 1.03 | 40 | -0.09 | -16.2 | 0.94 |  |

Best value: 0 · no change yet (current value is best)


<!-- SUMMARY
MES 3m LTF EMA20 Pierce: **worth considering: 8** (n=674) | HTF EMA9 Pierce: no change yet (best 1: neighbours disagree) (n=621) | HTF EMA20 Pierce: no change yet (current value is best) (n=357) | HTF Pullback Entry - Structure Confirmed: no change yet (best 2: not better in both halves, neighbours disagree, replay unreliable) (n=72, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 0 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=0, unchecked/unreliable) | VWAP Bounce: no change yet (best 0: not better in both halves, neighbours disagree, replay unreliable) (n=273, unchecked/unreliable)
MGC 3m LTF EMA20 Pierce: no change yet (best 0: not better in both halves) (n=693) | HTF EMA9 Pierce: no change yet (best 1: not better in both halves, neighbours disagree) (n=657) | HTF EMA20 Pierce: no change yet (best 1: neighbours disagree) (n=406) | HTF Pullback Entry - Structure Confirmed: no change yet (best 6: replay unreliable) (n=76, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 1 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=1, unchecked/unreliable) | VWAP Bounce: no change yet (current value is best) (n=341)
MNQ 3m LTF EMA20 Pierce: no change yet (best 8: not better in both halves, neighbours disagree) (n=636) | HTF EMA9 Pierce: no change yet (current value is best) (n=595, unchecked/unreliable) | HTF EMA20 Pierce: no change yet (best 1: neighbours disagree) (n=318) | HTF Pullback Entry - Structure Confirmed: no change yet (current value is best) (n=52, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 2 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=2, unchecked/unreliable) | VWAP Bounce: no change yet (best 20: not better in both halves) (n=30)
MES 2m LTF EMA20 Pierce: no change yet (best 5: replay unreliable) (n=1004, unchecked/unreliable) | HTF EMA9 Pierce: no change yet (best 5: not better in both halves, neighbours disagree) (n=945) | HTF EMA20 Pierce: no change yet (best 5: neighbours disagree) (n=531) | HTF Pullback Entry - Structure Confirmed: no change yet (best 8: replay unreliable) (n=117, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (3, 10): 1 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=2, unchecked/unreliable) | VWAP Bounce: no change yet (current value is best) (n=381)
MGC 2m LTF EMA20 Pierce: **worth considering: 5** (n=1046) | HTF EMA9 Pierce: no change yet (best 1: not better in both halves, neighbours disagree) (n=976) | HTF EMA20 Pierce: no change yet (best 5: not better in both halves, neighbours disagree) (n=606) | HTF Pullback Entry - Structure Confirmed: no change yet (best 1: replay unreliable) (n=107, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 0 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=0, unchecked/unreliable) | VWAP Bounce: no change yet (current value is best) (n=787)
-->
