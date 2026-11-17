Per-trigger results, current filters vs + "Block in chop: HTF EMA20 slope below 0.3 ATR" -- MES 3m and MGC 3m -- 11/14/2026.
Replay Jan 5 -> now, CBC engine setups, current filters (ER 0.23 + breakout 3, range gate 5 ATR, MGC VWAP stretch 4 ATR applied correctly),
live exits (MES 3m SL1 3 ATR min 5, TP1 1.75, 100 % at TP1; MGC 3m SL1 1.7 ATR min 5 cap 7, TP1 1.7 cap 6, FLIP 0 %). Net after costs
(MES 0.50, MGC 0.22). Trigger = the setup's first trigger. "Blocked" = setups in the current run that are absent with the slope filter
(the filter also lets some new setups in, because one setup at a time / cooldown). Thirds by date.

## MES 3m

| Trigger | Current: n / net / avg / win | Current thirds | Current last 4 wk | Slope 0.3: n / net / avg / win | Slope thirds | Slope last 4 wk | Δ net | Blocked by slope: n / net / avg |
|---|---|---|---|---|---|---|---|---|
| HTF CBC Flip | 320 / -378 / -1.18 / 54 % | -135 / -244 / +1 | -21 | 170 / -125 / -0.73 / 54 % | -21 / -142 / +39 | +9 | +253 | 150 / -253 / -1.69 |
| LTF EMA20 Pierce | 997 / -232 / -0.23 / 48 % | +103 / -350 / +15 | +89 | 811 / -51 / -0.06 / 50 % | +143 / -234 / +41 | +87 | +182 | 228 / -220 / -0.97 |
| HTF EMA9 Pierce | 312 / -178 / -0.57 / 42 % | +28 / -100 / -106 | +9 | 212 / -24 / -0.11 / 44 % | +58 / -84 / +2 | +2 | +154 | 120 / -137 / -1.14 |
| HTF EMA20 Pierce | 170 / -12 / -0.07 / 48 % | +3 / -17 / +3 | +21 | 49 / +93 / +1.89 / 63 % | +60 / +30 / +3 | +17 | +104 | 125 / -94 / -0.75 |
| **ALL** | 1799 / -801 / -0.45 / 48 % | -2 / -712 / -87 | +99 | 1242 / -107 / -0.09 / 50 % | +240 / -431 / +84 | +114 | +694 | 623 / -704 / -1.13 |

## MGC 3m

| Trigger | Current: n / net / avg / win | Current thirds | Current last 4 wk | Slope 0.3: n / net / avg / win | Slope thirds | Slope last 4 wk | Δ net | Blocked by slope: n / net / avg |
|---|---|---|---|---|---|---|---|---|
| HTF CBC Flip | 203 / +104 / +0.51 / 17 % | -7 / +1 / +110 | -13 | 62 / +7 / +0.12 / 15 % | -63 / -10 / +80 | -10 | -97 | 141 / +97 / +0.69 |
| LTF EMA20 Pierce | 559 / +406 / +0.73 / 17 % | +314 / -8 / +100 | +202 | 402 / +784 / +1.95 / 20 % | +539 / +64 / +181 | +167 | +378 | 211 / -149 / -0.70 |
| HTF EMA9 Pierce | 203 / +60 / +0.29 / 17 % | -22 / +67 / +15 | +27 | 127 / +163 / +1.29 / 26 % | +25 / +16 / +123 | +68 | +104 | 103 / -67 / -0.65 |
| HTF EMA20 Pierce | 171 / +45 / +0.26 / 26 % | +44 / -70 / +71 | +47 | 43 / +181 / +4.21 / 47 % | +45 / +8 / +128 | +53 | +136 | 135 / -73 / -0.54 |
| **ALL** | 1136 / +615 / +0.54 / 18 % | +329 / -10 / +297 | +262 | 634 / +1135 / +1.79 / 22 % | +545 / +78 / +512 | +279 | +520 | 590 / -191 / -0.32 |
## Check: slope filter with HTF CBC Flip setups exempt (MGC's blocked flips were +97)

| Chart | Variant | Setups | Net | Avg | Thirds | Last 4 wk | Max DD |
|---|---|---|---|---|---|---|---|
| MGC 3m | current | 1136 | +615 | +0.54 | +329 / -10 / +297 | +262 | 245 |
| MGC 3m | slope 0.3 all triggers | 634 | +1135 | +1.79 | +545 / +78 / +512 | +279 | 121 |
| MGC 3m | slope 0.3, flips exempt | 739 | +993 | +1.34 | +459 / +50 / +483 | +250 | 140 |
| MES 3m | current | 1799 | -801 | -0.45 | -2 / -712 / -87 | +99 | 1069 |
| MES 3m | slope 0.3 all triggers | 1242 | -107 | -0.09 | +240 / -431 / +84 | +114 | 624 |
| MES 3m | slope 0.3, flips exempt | 1357 | -308 | -0.23 | +139 / -508 / +61 | +100 | 712 |

Exempting flips is worse on both charts: the extra flip trades occupy the one-setup slot and push out better pierce setups. Keep the filter on all triggers.
