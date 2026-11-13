# CBC alert parameter sweep -- 2026-11-12 17:07 ET

Alert Feed: 45409 alerts (10/19 to 11/12). Bars: BarFeed, last 60 days. Validation window = days with stored alerts.
Outcome (a) = exit at first opposite HTF CBC flip / 17:00 ET / 2 h. (b) = 1.3 ATR stop / 2.0 ATR target (both in one candle = stop). Points per contract-point, before costs. ✱ = positive in both halves of the data under both rules. Validation: recall = stored alerts the replay reproduces (±1 bar), precision = replayed alerts that were stored. Unreliable = recall or precision < 70 %.

Notes: "Option 2: Reverse" pierces are scored in the reversed direction (as the alert says). LTF cooldown 0 and 1 are identical (a pierce needs the previous candle not touching the line). HTF EMA pierces use the setup-engine direction (flip counts on the HTF candle close) and the away / toward-late (1 pt) gate. 2m charts use their own 10m HTF fields from the BarFeed. Pullback-Structure replay rebuilds HTF swing pivots from the chart candles and does not reproduce the live alerts well (few stored alerts). In FVG alerts: none stored in the Alert Feed so far. Verdict rule: "worth considering" needs 30+ alerts, better than current in both halves under both rules, neighbouring values also better, and a reliable replay.

Settings: live CBC v10.93 (pine/CBC_v10_93.pine); claude/settings_sync_report.md (11/12 16:47 ET) shows 0 MISMATCH (1 known, unrelated). v10.88-v10.93 changed only ▶ Bot inputs; the ⑤ Alerts defaults are unchanged (checked in v10.93: ltf_ema20_pierce_cooldown 3, htf_pullback_recent_bars 4, fvg_alert_min_gap_bars 2 / fvg_alert_max_bars_after_flip 20, vwap_bounce_min_dist_override 0 = auto MES/MGC 6, MNQ 60, vb_tw_sym "MGC 3m 0300-1700 0.01, MGC 2m 0000-2400 0.01, MES 3m 0000-2400 4, MES 2m 0000-2400 4"). claude/CBC_SETTINGS.md lists only ats_/bot_/xr_/ema_ inputs, so these came from the Pine file. Data notes: stored alerts are not yet de-duplicated server-side (lastDedupe null); the replay keys stored alerts by chart + candle time, so the 11/08-11/12 double MGC alerts count once. MGC 3m BarFeed gaps 11/08 22:12-11/09 06:21 and 11/09 13:06-11/10 01:33 have no candles to replay.

Since last run (vs 11/12 09:58 ET): Alert Feed 44310 -> 45409 alerts. MES 3m / MNQ 3m alerts reached the feed again on 11/12 (59 / 76; still 0 on 11/10-11/11). MES 3m LTF EMA20 cooldown 8 still **worth considering** (4th run) and stronger: (a) +99.2 vs -272.5 at 3, (b) +188.5 vs -4.6. MGC 2m LTF EMA20 cooldown 5 still flagged (8th run): (a) -271.8 vs -450.5, (b) +68.1 vs -3.7 -- still negative under (a), i.e. "less bad" rather than good. MES 3m VWAP Bounce now validates on 5 stored alerts since 11/08 (recall 80 %, precision 100 %, small sample); current 4 is (a) -12.0 / (b) +22.5, 0 tops the sum but not in both halves. Still unreliable: MES 2m LTF EMA20 (66/68 %), MNQ 3m HTF EMA9 (77/65 %), Pullback-Structure everywhere; still no In FVG alerts in the Alert Feed.

## MES 3m (HTF 15m) -- 20578 bars 09/11 to 11/12

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 214, replayed 225, recall 81 %, precision 77 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 786 | 17.5 | 41 | -0.25 | -199.2 | 0.94 | 40 | +0.05 | +39.2 | 1.02 |  |
| 1 | 786 | 17.5 | 41 | -0.25 | -199.2 | 0.94 | 40 | +0.05 | +39.2 | 1.02 |  |
| 2 | 727 | 16.2 | 41 | -0.28 | -202.5 | 0.93 | 40 | +0.06 | +41.0 | 1.02 |  |
| 3 (current) | 683 | 15.2 | 40 | -0.40 | -272.5 | 0.91 | 40 | -0.01 | -4.6 | 1.00 |  |
| 5 | 606 | 13.5 | 40 | -0.29 | -174.0 | 0.93 | 39 | -0.15 | -88.9 | 0.95 |  |
| 8 | 518 | 11.5 | 42 | +0.19 | +99.2 | 1.05 | 42 | +0.36 | +188.5 | 1.12 |  |

Best value: 8 · **worth considering: 8**

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 207, replayed 227, recall 82 %, precision 75 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 694 | 15.4 | 43 | +0.89 | +618.8 | 1.24 | 43 | +0.61 | +422.7 | 1.22 | ✱ |
| 3 (current) | 623 | 13.8 | 42 | +0.90 | +561.2 | 1.25 | 43 | +0.60 | +374.1 | 1.22 | ✱ |
| 5 | 539 | 12.0 | 41 | +0.51 | +273.8 | 1.13 | 43 | +0.63 | +339.7 | 1.23 | ✱ |

Best value: 1 · no change yet (best 1: neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 128, replayed 140, recall 84 %, precision 76 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 403 | 9.0 | 41 | -0.96 | -386.5 | 0.80 | 39 | -0.21 | -83.2 | 0.93 |  |
| 3 (current) | 359 | 8.0 | 42 | -1.06 | -381.8 | 0.77 | 40 | -0.17 | -62.8 | 0.94 |  |
| 5 | 327 | 7.3 | 42 | -1.36 | -445.0 | 0.72 | 39 | -0.26 | -86.7 | 0.92 |  |

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

Validation at current: stored 5, replayed 4, recall 80 %, precision 100 %
Current = 4 (v10.83 default changed from auto 6; vb_tw_sym "MES 3m 0000-2400 4"). Validation uses stored alerts from 11/08 on.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 640 | 14.2 | 44 | +0.06 | +37.2 | 1.02 | 39 | -0.01 | -5.0 | 1.00 |  |
| 2 | 421 | 9.4 | 44 | +0.03 | +14.5 | 1.01 | 39 | -0.05 | -19.5 | 0.98 |  |
| 4 (current) | 275 | 6.1 | 41 | -0.04 | -12.0 | 0.99 | 38 | +0.08 | +22.5 | 1.03 |  |
| 6 | 188 | 4.2 | 38 | -0.52 | -97.0 | 0.89 | 35 | -0.17 | -31.1 | 0.94 |  |
| 8 | 156 | 3.5 | 37 | -0.30 | -46.2 | 0.92 | 34 | -0.27 | -41.4 | 0.90 |  |
| 10 | 127 | 2.8 | 36 | -0.36 | -45.5 | 0.90 | 33 | -0.49 | -61.9 | 0.80 |  |

Best value: 0 · no change yet (best 0: not better in both halves, neighbours disagree)

## MGC 3m (HTF 15m) -- 20579 bars 09/11 to 11/12

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 268, replayed 311, recall 93 %, precision 80 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 795 | 17.7 | 40 | +0.48 | +378.8 | 1.13 | 41 | +0.18 | +144.4 | 1.07 | ✱ |
| 1 | 795 | 17.7 | 40 | +0.48 | +378.8 | 1.13 | 41 | +0.18 | +144.4 | 1.07 | ✱ |
| 2 | 747 | 16.6 | 40 | +0.34 | +256.7 | 1.09 | 41 | +0.22 | +166.6 | 1.08 | ✱ |
| 3 (current) | 699 | 15.5 | 40 | +0.44 | +310.1 | 1.12 | 42 | +0.26 | +178.8 | 1.10 | ✱ |
| 5 | 616 | 13.7 | 40 | +0.64 | +394.2 | 1.18 | 41 | +0.16 | +98.8 | 1.06 |  |
| 8 | 526 | 11.7 | 40 | +0.47 | +248.5 | 1.13 | 41 | +0.15 | +77.1 | 1.05 | ✱ |

Best value: 0 · no change yet (best 0: not better in both halves)

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 245, replayed 273, recall 82 %, precision 73 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 742 | 16.5 | 41 | +0.46 | +339.7 | 1.13 | 40 | +0.05 | +36.7 | 1.02 |  |
| 3 (current) | 662 | 14.7 | 41 | +0.39 | +258.6 | 1.11 | 39 | -0.07 | -43.4 | 0.98 |  |
| 5 | 575 | 12.8 | 40 | +0.51 | +291.8 | 1.15 | 38 | -0.16 | -92.4 | 0.94 |  |

Best value: 1 · no change yet (best 1: not better in both halves, neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 153, replayed 153, recall 80 %, precision 80 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 455 | 10.1 | 39 | -0.12 | -53.1 | 0.97 | 38 | -0.27 | -122.1 | 0.91 |  |
| 3 (current) | 407 | 9.0 | 37 | -0.56 | -228.9 | 0.86 | 36 | -0.46 | -186.1 | 0.84 |  |
| 5 | 358 | 8.0 | 38 | -0.49 | -176.6 | 0.87 | 37 | -0.39 | -139.8 | 0.86 |  |

Best value: 1 · no change yet (best 1: neighbours disagree)

### HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)

Validation at current: stored 11, replayed 30, recall 9 %, precision 3 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 34 | 0.8 | 32 | +1.20 | +40.8 | 1.56 | 41 | -0.06 | -2.1 | 0.98 |  |
| 2 | 54 | 1.2 | 35 | +0.72 | +38.8 | 1.42 | 39 | -0.42 | -22.8 | 0.84 |  |
| 3 | 69 | 1.5 | 35 | +1.07 | +73.5 | 1.64 | 38 | -0.57 | -39.5 | 0.78 |  |
| 4 (current) | 77 | 1.7 | 35 | +1.68 | +129.4 | 1.99 | 38 | -0.53 | -41.1 | 0.80 |  |
| 6 | 106 | 2.4 | 39 | +1.76 | +186.6 | 2.04 | 44 | +0.22 | +23.7 | 1.09 |  |
| 8 | 120 | 2.7 | 37 | +1.25 | +150.4 | 1.68 | 42 | -0.07 | -8.3 | 0.97 |  |

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

## MNQ 3m (HTF 15m) -- 20580 bars 09/11 to 11/12

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 215, replayed 230, recall 88 %, precision 82 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 723 | 16.1 | 38 | -0.56 | -402.8 | 0.98 | 41 | +0.08 | +60.7 | 1.00 |  |
| 1 | 723 | 16.1 | 38 | -0.56 | -402.8 | 0.98 | 41 | +0.08 | +60.7 | 1.00 |  |
| 2 | 674 | 15.0 | 38 | -0.92 | -623.0 | 0.97 | 41 | -0.21 | -139.2 | 0.99 |  |
| 3 (current) | 637 | 14.2 | 38 | -0.58 | -370.0 | 0.98 | 41 | +0.09 | +58.1 | 1.00 |  |
| 5 | 565 | 12.6 | 37 | -2.39 | -1349.0 | 0.91 | 40 | -0.38 | -215.3 | 0.98 |  |
| 8 | 495 | 11.0 | 40 | +1.16 | +575.2 | 1.04 | 42 | +0.98 | +487.4 | 1.05 |  |

Best value: 8 · no change yet (best 8: not better in both halves, neighbours disagree)

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 175, replayed 206, recall 77 %, precision 65 % -- **unreliable**
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 663 | 14.7 | 40 | +3.66 | +2428.8 | 1.14 | 40 | -0.43 | -283.4 | 0.98 |  |
| 3 (current) | 602 | 13.4 | 40 | +4.65 | +2796.5 | 1.18 | 40 | -0.55 | -329.8 | 0.97 |  |
| 5 | 531 | 11.8 | 40 | +4.37 | +2320.0 | 1.17 | 40 | +0.06 | +34.3 | 1.00 |  |

Best value: 3 · no change yet (current value is best)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 110, replayed 135, recall 89 %, precision 73 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 370 | 8.2 | 41 | +2.14 | +791.8 | 1.08 | 42 | +3.67 | +1358.3 | 1.20 |  |
| 3 (current) | 322 | 7.2 | 39 | -0.88 | -284.2 | 0.97 | 41 | +2.83 | +911.7 | 1.15 |  |
| 5 | 292 | 6.5 | 39 | -1.21 | -352.0 | 0.96 | 42 | +4.12 | +1202.7 | 1.23 |  |

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

## MES 2m (HTF 10m) -- 30869 bars 09/11 to 11/12

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 415, replayed 400, recall 66 %, precision 68 % -- **unreliable**

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1184 | 26.3 | 37 | -0.50 | -593.0 | 0.86 | 38 | +0.01 | +11.1 | 1.00 |  |
| 1 | 1184 | 26.3 | 37 | -0.50 | -593.0 | 0.86 | 38 | +0.01 | +11.1 | 1.00 |  |
| 2 | 1106 | 24.6 | 38 | -0.43 | -478.0 | 0.88 | 39 | +0.04 | +49.3 | 1.02 |  |
| 3 (current) | 1013 | 22.5 | 37 | -0.49 | -491.8 | 0.86 | 38 | +0.04 | +44.5 | 1.02 |  |
| 5 | 906 | 20.1 | 37 | -0.36 | -329.2 | 0.90 | 39 | +0.07 | +66.3 | 1.03 |  |
| 8 | 786 | 17.5 | 37 | -0.46 | -359.8 | 0.87 | 38 | +0.01 | +6.7 | 1.00 |  |

Best value: 5 · no change yet (best 5: not better in both halves, replay unreliable)

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 373, replayed 396, recall 83 %, precision 78 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1068 | 23.7 | 40 | +0.05 | +48.8 | 1.01 | 40 | +0.09 | +95.3 | 1.04 |  |
| 3 (current) | 950 | 21.1 | 40 | +0.13 | +126.5 | 1.04 | 41 | +0.14 | +132.6 | 1.06 | ✱ |
| 5 | 843 | 18.7 | 40 | +0.33 | +275.5 | 1.11 | 40 | +0.09 | +78.3 | 1.04 | ✱ |

Best value: 5 · no change yet (best 5: not better in both halves, neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 229, replayed 230, recall 84 %, precision 83 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 588 | 13.1 | 42 | -0.02 | -13.0 | 0.99 | 39 | -0.00 | -2.4 | 1.00 |  |
| 3 (current) | 532 | 11.8 | 41 | -0.13 | -70.2 | 0.96 | 39 | +0.06 | +32.2 | 1.03 |  |
| 5 | 486 | 10.8 | 42 | -0.09 | -44.0 | 0.97 | 41 | +0.21 | +99.6 | 1.09 |  |

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
| 0 | 916 | 20.4 | 42 | +0.17 | +153.8 | 1.06 | 37 | -0.14 | -130.6 | 0.93 |  |
| 2 | 588 | 13.1 | 43 | +0.38 | +225.0 | 1.12 | 38 | -0.11 | -67.4 | 0.95 |  |
| 4 (current) | 381 | 8.5 | 44 | +0.76 | +290.5 | 1.25 | 39 | +0.11 | +42.3 | 1.05 |  |
| 6 | 262 | 5.8 | 40 | +0.42 | +110.8 | 1.12 | 38 | +0.04 | +11.1 | 1.02 |  |
| 8 | 219 | 4.9 | 39 | -0.07 | -15.8 | 0.98 | 37 | -0.08 | -16.7 | 0.96 |  |
| 10 | 179 | 4.0 | 38 | -0.60 | -107.8 | 0.82 | 36 | -0.35 | -62.3 | 0.83 |  |

Best value: 4 · no change yet (current value is best)

## MGC 2m (HTF 10m) -- 30867 bars 09/11 to 11/12

### LTF EMA20 Pierce: cooldown bars

Validation at current: stored 386, replayed 420, recall 82 %, precision 75 %

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1195 | 26.6 | 38 | -0.57 | -675.9 | 0.84 | 40 | -0.01 | -13.9 | 0.99 |  |
| 1 | 1195 | 26.6 | 38 | -0.57 | -675.9 | 0.84 | 40 | -0.01 | -13.9 | 0.99 |  |
| 2 | 1122 | 24.9 | 38 | -0.47 | -527.5 | 0.86 | 40 | +0.02 | +20.7 | 1.01 |  |
| 3 (current) | 1049 | 23.3 | 38 | -0.43 | -450.5 | 0.88 | 40 | -0.00 | -3.7 | 1.00 |  |
| 5 | 940 | 20.9 | 39 | -0.29 | -271.8 | 0.91 | 40 | +0.07 | +68.1 | 1.03 |  |
| 8 | 787 | 17.5 | 38 | -0.24 | -186.9 | 0.93 | 40 | -0.06 | -46.3 | 0.97 |  |

Best value: 5 · **worth considering: 5**

### HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)

Validation at current: stored 357, replayed 406, recall 87 %, precision 76 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1105 | 24.6 | 41 | +0.71 | +780.2 | 1.23 | 41 | +0.15 | +161.7 | 1.07 |  |
| 3 (current) | 985 | 21.9 | 40 | +0.55 | +545.9 | 1.18 | 41 | +0.16 | +159.0 | 1.08 |  |
| 5 | 864 | 19.2 | 41 | +0.54 | +467.4 | 1.17 | 42 | +0.27 | +234.9 | 1.13 |  |

Best value: 1 · no change yet (best 1: not better in both halves, neighbours disagree)

### HTF EMA20 Pierce: spacing (bars)

Validation at current: stored 228, replayed 242, recall 87 %, precision 82 %
No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.

| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 703 | 15.6 | 39 | +0.25 | +172.8 | 1.08 | 42 | +0.14 | +100.8 | 1.07 |  |
| 3 (current) | 614 | 13.6 | 39 | +0.26 | +156.8 | 1.08 | 41 | +0.10 | +64.1 | 1.05 |  |
| 5 | 546 | 12.1 | 40 | +0.51 | +280.7 | 1.16 | 41 | +0.13 | +71.0 | 1.06 |  |

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
MES 3m LTF EMA20 Pierce: **worth considering: 8** (n=683) | HTF EMA9 Pierce: no change yet (best 1: neighbours disagree) (n=623) | HTF EMA20 Pierce: no change yet (current value is best) (n=359) | HTF Pullback Entry - Structure Confirmed: no change yet (best 2: not better in both halves, neighbours disagree, replay unreliable) (n=72, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 0 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=0, unchecked/unreliable) | VWAP Bounce: no change yet (best 0: not better in both halves, neighbours disagree) (n=275)
MGC 3m LTF EMA20 Pierce: no change yet (best 0: not better in both halves) (n=699) | HTF EMA9 Pierce: no change yet (best 1: not better in both halves, neighbours disagree) (n=662) | HTF EMA20 Pierce: no change yet (best 1: neighbours disagree) (n=407) | HTF Pullback Entry - Structure Confirmed: no change yet (best 6: replay unreliable) (n=77, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 1 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=1, unchecked/unreliable) | VWAP Bounce: no change yet (current value is best) (n=341)
MNQ 3m LTF EMA20 Pierce: no change yet (best 8: not better in both halves, neighbours disagree) (n=637) | HTF EMA9 Pierce: no change yet (current value is best) (n=602, unchecked/unreliable) | HTF EMA20 Pierce: no change yet (best 1: neighbours disagree) (n=322) | HTF Pullback Entry - Structure Confirmed: no change yet (current value is best) (n=52, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 2 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=2, unchecked/unreliable) | VWAP Bounce: no change yet (best 20: not better in both halves) (n=30)
MES 2m LTF EMA20 Pierce: no change yet (best 5: not better in both halves, replay unreliable) (n=1013, unchecked/unreliable) | HTF EMA9 Pierce: no change yet (best 5: not better in both halves, neighbours disagree) (n=950) | HTF EMA20 Pierce: no change yet (best 5: neighbours disagree) (n=532) | HTF Pullback Entry - Structure Confirmed: no change yet (best 8: replay unreliable) (n=117, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (3, 10): 1 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=2, unchecked/unreliable) | VWAP Bounce: no change yet (current value is best) (n=381)
MGC 2m LTF EMA20 Pierce: **worth considering: 5** (n=1049) | HTF EMA9 Pierce: no change yet (best 1: not better in both halves, neighbours disagree) (n=985) | HTF EMA20 Pierce: no change yet (best 5: not better in both halves, neighbours disagree) (n=614) | HTF Pullback Entry - Structure Confirmed: no change yet (best 1: replay unreliable) (n=107, unchecked/unreliable) | In FVG of HTF Flip Candle: no change yet (best (1, 10): 0 alerts, not better in both halves, neighbours disagree, replay unreliable) (n=0, unchecked/unreliable) | VWAP Bounce: no change yet (current value is best) (n=787)
-->
