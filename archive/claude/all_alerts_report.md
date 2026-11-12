# All CBC alerts re-checked -- 2026-11-07 09:52 ET (weekly run 2, rerun after data repair)

**Rerun after data repair — replaces the 11/06 20:43 run as weekly run 2** (run 1 = 11/01). The BarFeed bars were repaired on 11/07 (MGC 3m had 5m candles mixed in; MES 2m/5m and MNQ had gaps), so the 11/06 numbers are superseded; consecutive-run counts below use these figures for run 2. Alert Feed unchanged (34,777 alerts, 10/19–11/06); replay Jan–11/06 (2m Jun–11/06). A Saturday 09:46 ET run on the repaired data gave identical output and is folded into this one. "HTF" below = HTF CBC Flip / Agreement. Alert-type scores use generic exits (a) flip/17:00/2 h and (b) 1.3 / 2.0 ATR.

## Since last week (run 1, 11/01 → run 2, repaired)

**Verdict: no change yet.** Nothing has 3 consecutive weekly runs. Do not change any setting.

### Session gaps (replay; net by third Jan–Mar / Apr–Jun / Jul–now, 2m Jun–Jul / Aug / Sep–now)

| Chart | Gap | 11/06 before repair (superseded) | Run 2 (repaired) | Avg gap vs inside | Setups | Positive in all thirds, consecutive weekly runs |
|---|---|---|---|---|---|---|
| MES 3m | 22:30–03:00 | +71 (+14/+19/+38) | +71 (+14/+19/+38) | +0.19 vs +0.01 | 374 | **2** (run 3 = 11/13) → candidate: ⑤ Alerts → Asian end 22:30 → 03:00 |
| MES 3m | 07:45–09:30 | −72 (+2/−34/−40) | −71 (+2/−34/−40) | −0.39 vs +0.01 | 182 | 0 |
| MGC 3m | 22:30–03:00 | +147 (+120/+35/−8) | +159 (+120/+35/+4) | +0.64 vs +0.24 | 248 | **1** (run 1 last third was −10; run 2 +4) |
| MGC 3m | 07:45–09:30 | −96 (−14/−95/+13) | −77 (−14/−95/+32) | −0.63 vs +0.24 | 121 | 0 |
| MES 2m | 22:30–03:00 | −6 (+50/−2/−54) | −6 (+50/−2/−54) | −0.02 vs −0.24 | 278 | 0 |
| MES 2m | 07:45–09:30 | +7 (−19/+39/−13) | +8 (−19/+39/−13) | +0.07 vs −0.24 | 116 | 0 |
| MGC 2m | 22:30–03:00 | +86 (−36/+27/+95) | +85 (−36/+27/+94) | +0.27 vs +0.16 | 314 | 0 (first third −) |
| MGC 2m | 07:45–09:30 | +89 (+7/+11/+71) | +92 (+7/+11/+74) | +0.58 vs +0.16 | 158 | **2** → candidate: ⑤ Alerts → New York start 09:30 → 07:45 (or London end 07:45 → 09:30) |
| MES 5m | 22:30–03:00 | −56 (+10/−19/−47) | −56 (same) | −0.24 vs +0.20 | 233 | 0 |
| MES 5m | 07:45–09:30 | −119 (−31/−35/−53) | −119 (same) | −0.94 vs +0.20 | 127 | negative in all thirds 2 weekly runs — current setting right |
| MGC 5m | 22:30–03:00 | −49 (−30/+22/−41) | −49 (same) | −0.21 vs −0.23 | 237 | 0 |
| MGC 5m | 07:45–09:30 | +120 (+48/+36/+36) | +120 (same) | +0.90 vs −0.23 | 133 | **2** → candidate: ⑤ Alerts → New York start 09:30 → 07:45 (or London end 07:45 → 09:30) |

### Alert types (same alerts as the 11/06 run; differences vs the pre-repair 11/06 numbers come from the repaired bars)

- MES 3m, MES 2m, MGC 2m, MES 5m, MGC 5m: no sign or ✱ changes.
- MGC 3m: HTF CBC Flip (b) now + (+2.8) on repaired bars → not both-negative this run, streak 0; A+ Setup (b) turned − (−1.1, (a) +0.5 still +); Trade Setup gained ✱; ORB Pass + lost ✱.
- MNQ 3m: HTF EMA20 Pierce (a) turned − (−211 / +24); VWAP Bounce (a) turned + (10 alerts).
- Both-negative ≥ 30 alerts, at 2 weekly runs (runs 1 and 2) (3 needed): HTF EMA20 Touch – Pullback Entry (MES 3m, MGC 3m, MNQ 3m, MES 2m, MGC 2m, MES 5m; MGC 5m at 1); Price Enters HTF EMA9/20 Zone (MES 3m, MNQ 3m, MES 2m, MGC 2m, MES 5m, MGC 5m); LTF EMA20 Touch – Pullback Entry (MES 3m, MNQ 3m, MES 2m, MES 5m; MGC 5m at 1); A+ Setup (MES 2m; MGC 5m at 1).
- Stable good: Key Level Alert and Outside HTF ORB ✱ on all 7 charts.

---

# Every CBC alert type, scored — Sat 11/07/2026 09:52 ET

Every CBC alert type, scored -- 11/01/2026.

For each chart (MES / MGC / MNQ 3m, MES / MGC 2m, MES / MGC 5m) every directional alert section ("• <type>: LONG / SHORT /
Bullish / Bearish / Above / Below / Pass + / Pass - ...") stored in the Alert Feed is scored from the BarFeed bars with the
same two outcome rules as claude/alert_param_sweep.py:
  (a) entry = close of the alert candle, exit at the close of the first candle with an opposite HTF CBC flip, the candle
      ending 17:00 ET, or after 2 h;   (b) 1.3 ATR(14) stop / 2.0 ATR target (both in one candle = stop), else 17:00 ET.
Points per contract-point, before costs. ✱ = positive in both halves (by date) under both rules. Non-directional alerts
(Approaching / Crossing / Setup Ended / TP1 Partial / Shadow ...) are counted only.
Alert candle = the bar that closes at the alert's "Time:" (CBC alerts fire at the candle close).
Also: Trade Setups the setup engine would draw OUTSIDE CBC's alert sessions (Asia 18:00-22:30, London 03:00-07:45,
NY 09:30-17:00 ET) never reach the feed -- replay counts / results for 3m and 5m (chop_sim, live gates, base exits).
Usage: python3 all_alerts_study.py

Alert Feed: 34777 alerts, 2026-10-19 to 2026-11-06.

## MES 3m — 10/19 to 11/06 (17 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Outside HTF ORB | 186 | 10.9 | 185 | 51 | +5.36 | +992.5 | 59 | +2.81 | +520.3 | ✱ |
| Key Level Alert | 111 | 6.5 | 100 | 61 | +7.77 | +776.8 | 67 | +4.91 | +491.0 | ✱ |
| HTF EMA9 Pierce | 202 | 11.9 | 198 | 43 | +1.79 | +353.5 | 48 | +1.05 | +207.8 | ✱ |
| High Confluence Setup | 216 | 12.7 | 216 | 44 | +0.96 | +206.8 | 50 | +1.47 | +317.5 |  |
| ORB Pass - | 74 | 4.4 | 74 | 43 | +5.20 | +385.0 | 54 | +1.78 | +131.9 |  |
| VWAP Bounce - High R | 72 | 4.2 | 69 | 45 | +2.99 | +206.0 | 65 | +3.71 | +255.8 | ✱ |
| LTF EMA20 Pierce | 209 | 12.3 | 207 | 43 | +0.66 | +137.5 | 50 | +1.47 | +303.4 | ✱ |
| ORB Pass + | 90 | 5.3 | 89 | 51 | +3.81 | +339.5 | 46 | +0.70 | +62.5 |  |
| Trade Setup | 116 | 6.8 | 116 | 41 | +2.15 | +249.5 | 44 | +0.96 | +111.5 |  |
| HTF EMA20 Pierce | 123 | 7.2 | 121 | 44 | +1.62 | +196.5 | 46 | +0.36 | +44.0 |  |
| HTF | 176 | 10.4 | 175 | 39 | -0.61 | -106.5 | 45 | +0.74 | +129.7 |  |
| HTF Pullback Entry - Structure Confirmed | 3 | 0.2 | 3 | 0 | -13.33 | -40.0 | 0 | -8.12 | -24.4 |  |
| A+ Setup | 172 | 10.1 | 172 | 40 | +0.32 | +54.2 | 35 | -0.71 | -122.2 |  |
| LTF EMA20 Touch - Pullback Entry | 51 | 3.0 | 51 | 35 | -1.29 | -65.8 | 20 | -3.04 | -155.0 |  |
| Price Enters HTF EMA9/20 Zone | 94 | 5.5 | 93 | 17 | -4.65 | -432.0 | 19 | -3.00 | -278.9 |  |
| HTF EMA20 Touch - Pullback Entry | 141 | 8.3 | 139 | 23 | -3.76 | -522.8 | 11 | -4.21 | -584.7 |  |
| Setup Ended | 117 | 6.9 | 0 | | | | | | | |
| EMA 20 Crossing | 76 | 4.5 | 0 | | | | | | | |
| Setup Confirmed | 35 | 2.1 | 0 | | | | | | | |
| EMA 20 Approaching | 375 | 22.1 | 0 | | | | | | | |
| VWAP Approaching | 132 | 7.8 | 0 | | | | | | | |
| EMA 200 Approaching | 34 | 2.0 | 0 | | | | | | | |
| TP1 Partial | 53 | 3.1 | 0 | | | | | | | |
| Bill Breaker 7400 Crossing | 4 | 0.2 | 0 | | | | | | | |
| EMA 200 Crossing | 30 | 1.8 | 0 | | | | | | | |
| ORB High Crossing | 31 | 1.8 | 0 | | | | | | | |
| Bill Breaker 7400 Approaching | 14 | 0.8 | 0 | | | | | | | |
| YDL Crossing | 11 | 0.6 | 0 | | | | | | | |
| YDL Approaching | 18 | 1.1 | 0 | | | | | | | |
| Bill Breaker 7500 Approaching | 5 | 0.3 | 0 | | | | | | | |
| Bill Breaker 7600 Crossing | 4 | 0.2 | 0 | | | | | | | |
| Bill Breaker 7600 Approaching | 12 | 0.7 | 0 | | | | | | | |
| ORB High Approaching | 42 | 2.5 | 0 | | | | | | | |
| VWAP Crossing | 27 | 1.6 | 0 | | | | | | | |
| Bill Breaker 7700 Approaching | 13 | 0.8 | 0 | | | | | | | |
| YDH Approaching | 15 | 0.9 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 18 | 1.1 | 0 | | | | | | | |
| Bill Breaker 7500 Crossing | 1 | 0.1 | 0 | | | | | | | |
| ORB Low Crossing | 21 | 1.2 | 0 | | | | | | | |
| ORB Flip + | 10 | 0.6 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 8 | 0.5 | 0 | | | | | | | |
| ORB Low Approaching | 40 | 2.4 | 0 | | | | | | | |
| YDH Crossing | 7 | 0.4 | 0 | | | | | | | |
| ORB Flip - | 7 | 0.4 | 0 | | | | | | | |
| Bill Breaker 7700 Crossing | 4 | 0.2 | 0 | | | | | | | |
| Bill Breaker 7800 Approaching | 4 | 0.2 | 0 | | | | | | | |

## MGC 3m — 10/19 to 11/06 (17 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| LTF EMA20 Pierce | 244 | 14.4 | 244 | 51 | +2.43 | +592.8 | 54 | +1.89 | +461.2 | ✱ |
| Outside HTF ORB | 186 | 10.9 | 186 | 51 | +2.04 | +380.3 | 67 | +3.58 | +666.8 | ✱ |
| Key Level Alert | 266 | 15.6 | 260 | 53 | +1.34 | +348.6 | 61 | +2.30 | +598.7 | ✱ |
| High Confluence Setup | 270 | 15.9 | 270 | 43 | +1.59 | +429.0 | 51 | +1.66 | +449.4 |  |
| HTF EMA9 Pierce | 217 | 12.8 | 217 | 44 | +0.90 | +195.1 | 51 | +1.23 | +267.4 | ✱ |
| HTF EMA20 Pierce | 135 | 7.9 | 132 | 46 | +1.52 | +200.0 | 52 | +1.74 | +230.3 | ✱ |
| ORB Pass - | 99 | 5.8 | 99 | 46 | +1.77 | +175.3 | 57 | +1.89 | +187.0 | ✱ |
| VWAP Bounce - High R | 72 | 4.2 | 71 | 51 | +1.39 | +98.9 | 65 | +2.45 | +173.6 | ✱ |
| ORB Pass + | 53 | 3.1 | 53 | 51 | +0.54 | +28.6 | 60 | +2.57 | +136.4 |  |
| Trade Setup | 79 | 4.6 | 79 | 37 | +0.77 | +61.2 | 41 | +0.34 | +26.9 | ✱ |
| A+ Setup | 161 | 9.5 | 160 | 41 | +0.00 | +0.5 | 36 | -0.01 | -1.1 |  |
| Setup Blocked | 7 | 0.4 | 7 | 43 | -2.41 | -16.9 | 43 | +1.36 | +9.5 |  |
| LTF EMA20 Touch - Pullback Entry | 51 | 3.0 | 51 | 27 | +0.05 | +2.8 | 25 | -0.90 | -45.9 |  |
| HTF | 170 | 10.0 | 166 | 36 | -0.35 | -58.7 | 40 | +0.02 | +2.8 |  |
| Price Enters HTF EMA9/20 Zone | 134 | 7.9 | 132 | 32 | +0.20 | +26.7 | 30 | -0.70 | -91.8 |  |
| HTF Pullback Entry - Structure Confirmed | 10 | 0.6 | 10 | 10 | -5.15 | -51.5 | 10 | -3.33 | -33.3 |  |
| HTF EMA20 Touch - Pullback Entry | 148 | 8.7 | 146 | 25 | -2.40 | -350.1 | 18 | -2.14 | -312.2 |  |
| EMA 20 Approaching | 369 | 21.7 | 0 | | | | | | | |
| EMA 20 Crossing | 80 | 4.7 | 0 | | | | | | | |
| VWAP Approaching | 94 | 5.5 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 30 | 1.8 | 0 | | | | | | | |
| Setup Ended | 75 | 4.4 | 0 | | | | | | | |
| TP1 Partial | 26 | 1.5 | 0 | | | | | | | |
| Setup Confirmed | 37 | 2.2 | 0 | | | | | | | |
| VWAP Crossing | 30 | 1.8 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 25 | 1.5 | 0 | | | | | | | |
| ORB High Approaching | 38 | 2.2 | 0 | | | | | | | |
| ORB High Crossing | 21 | 1.2 | 0 | | | | | | | |
| EMA 200 Crossing | 30 | 1.8 | 0 | | | | | | | |
| YDL Approaching | 29 | 1.7 | 0 | | | | | | | |
| YDL Crossing | 21 | 1.2 | 0 | | | | | | | |
| EMA 200 Approaching | 39 | 2.3 | 0 | | | | | | | |
| ORB Low Approaching | 47 | 2.8 | 0 | | | | | | | |
| ORB Low Crossing | 42 | 2.5 | 0 | | | | | | | |
| Bill Breaker 4100 Approaching | 8 | 0.5 | 0 | | | | | | | |
| Bill Breaker 4100 Crossing | 3 | 0.2 | 0 | | | | | | | |
| Shadow Ended | 8 | 0.5 | 0 | | | | | | | |
| YDH Approaching | 8 | 0.5 | 0 | | | | | | | |
| YDH Crossing | 3 | 0.2 | 0 | | | | | | | |
| ORB Flip - | 10 | 0.6 | 0 | | | | | | | |
| Bill Breaker 3900 Approaching | 6 | 0.4 | 0 | | | | | | | |
| ORB Flip + | 8 | 0.5 | 0 | | | | | | | |
| Bill Breaker 4000 Crossing | 6 | 0.4 | 0 | | | | | | | |
| Bill Breaker 4000 Approaching | 4 | 0.2 | 0 | | | | | | | |

## MNQ 3m — 10/20 to 11/06 (16 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Key Level Alert | 136 | 8.5 | 125 | 58 | +44.26 | +5533.0 | 67 | +31.38 | +3922.0 | ✱ |
| Outside HTF ORB | 149 | 9.3 | 149 | 48 | +22.84 | +3403.0 | 58 | +24.44 | +3640.9 | ✱ |
| High Confluence Setup | 231 | 14.4 | 231 | 40 | +11.85 | +2736.8 | 48 | +10.92 | +2523.5 | ✱ |
| ORB Pass - | 50 | 3.1 | 49 | 37 | +33.92 | +1662.2 | 65 | +29.01 | +1421.5 |  |
| LTF EMA20 Pierce | 208 | 13.0 | 205 | 41 | +4.84 | +993.0 | 42 | +5.85 | +1198.5 |  |
| A+ Setup | 142 | 8.9 | 142 | 36 | +5.35 | +759.2 | 43 | +7.27 | +1032.0 |  |
| ORB Pass + | 81 | 5.1 | 81 | 49 | +0.14 | +11.2 | 54 | +16.93 | +1371.4 |  |
| VWAP Bounce - High R | 10 | 0.6 | 10 | 50 | +1.32 | +13.2 | 80 | +43.61 | +436.1 |  |
| HTF EMA20 Pierce | 107 | 6.7 | 105 | 36 | -2.01 | -211.0 | 42 | +0.22 | +23.6 |  |
| HTF Pullback Entry - Structure Confirmed | 11 | 0.7 | 11 | 18 | -71.61 | -787.8 | 18 | -25.99 | -285.9 |  |
| HTF | 176 | 11.0 | 175 | 34 | -8.52 | -1490.5 | 41 | +0.55 | +96.0 |  |
| HTF EMA9 Pierce | 170 | 10.6 | 167 | 32 | -10.33 | -1725.2 | 43 | +0.15 | +24.7 |  |
| LTF EMA20 Touch - Pullback Entry | 52 | 3.2 | 51 | 24 | -31.72 | -1617.5 | 20 | -17.90 | -912.9 |  |
| Trade Setup | 114 | 7.1 | 114 | 22 | -17.16 | -1956.0 | 25 | -11.89 | -1355.2 |  |
| Price Enters HTF EMA9/20 Zone | 102 | 6.4 | 100 | 20 | -27.76 | -2776.2 | 19 | -22.46 | -2245.6 |  |
| HTF EMA20 Touch - Pullback Entry | 137 | 8.6 | 135 | 18 | -28.33 | -3824.5 | 16 | -25.25 | -3409.3 |  |
| EMA 20 Approaching | 235 | 14.7 | 0 | | | | | | | |
| Bill Breaker 27100 Crossing | 6 | 0.4 | 0 | | | | | | | |
| VWAP Approaching | 73 | 4.6 | 0 | | | | | | | |
| Bill Breaker 27100 Approaching | 14 | 0.9 | 0 | | | | | | | |
| EMA 200 Crossing | 16 | 1.0 | 0 | | | | | | | |
| Bill Breaker 27200 Crossing | 3 | 0.2 | 0 | | | | | | | |
| ORB Low Crossing | 8 | 0.5 | 0 | | | | | | | |
| Setup Ended | 111 | 6.9 | 0 | | | | | | | |
| Bill Breaker 27200 Approaching | 12 | 0.8 | 0 | | | | | | | |
| TP1 Partial | 34 | 2.1 | 0 | | | | | | | |
| Bill Breaker 27300 Approaching | 5 | 0.3 | 0 | | | | | | | |
| EMA 200 Approaching | 56 | 3.5 | 0 | | | | | | | |
| Setup Confirmed | 31 | 1.9 | 0 | | | | | | | |
| ORB High Crossing | 13 | 0.8 | 0 | | | | | | | |
| ORB High Approaching | 49 | 3.1 | 0 | | | | | | | |
| Bill Breaker 27000 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27000 Approaching | 4 | 0.2 | 0 | | | | | | | |
| Bill Breaker 26900 Approaching | 7 | 0.4 | 0 | | | | | | | |
| Bill Breaker 26900 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 26700 Approaching | 3 | 0.2 | 0 | | | | | | | |
| Bill Breaker 26600 Crossing | 1 | 0.1 | 0 | | | | | | | |
| YDL Approaching | 11 | 0.7 | 0 | | | | | | | |
| EMA 20 Crossing | 43 | 2.7 | 0 | | | | | | | |
| Bill Breaker 26800 Approaching | 1 | 0.1 | 0 | | | | | | | |
| ORB Low Approaching | 42 | 2.6 | 0 | | | | | | | |
| Bill Breaker 27700 Approaching | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28000 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28000 Approaching | 1 | 0.1 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 26 | 1.6 | 0 | | | | | | | |
| Bill Breaker 28400 Approaching | 12 | 0.8 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 2 | 0.1 | 0 | | | | | | | |
| VWAP Crossing | 12 | 0.8 | 0 | | | | | | | |
| Bill Breaker 28300 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28300 Approaching | 10 | 0.6 | 0 | | | | | | | |
| YDL Crossing | 4 | 0.2 | 0 | | | | | | | |
| Bill Breaker 28400 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28200 Approaching | 9 | 0.6 | 0 | | | | | | | |
| Bill Breaker 28500 Approaching | 3 | 0.2 | 0 | | | | | | | |
| Bill Breaker 28600 Crossing | 3 | 0.2 | 0 | | | | | | | |
| Bill Breaker 28600 Approaching | 3 | 0.2 | 0 | | | | | | | |
| Bill Breaker 28700 Approaching | 12 | 0.8 | 0 | | | | | | | |
| Bill Breaker 28800 Approaching | 3 | 0.2 | 0 | | | | | | | |
| Bill Breaker 28800 Crossing | 2 | 0.1 | 0 | | | | | | | |
| YDH Approaching | 16 | 1.0 | 0 | | | | | | | |
| Bill Breaker 28500 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27900 Approaching | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27800 Approaching | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27900 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28100 Approaching | 1 | 0.1 | 0 | | | | | | | |
| ORB Flip + | 4 | 0.2 | 0 | | | | | | | |
| Bill Breaker 28700 Crossing | 1 | 0.1 | 0 | | | | | | | |
| YDH Crossing | 7 | 0.4 | 0 | | | | | | | |
| Bill Breaker 28900 Approaching | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29000 Approaching | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29100 Crossing | 3 | 0.2 | 0 | | | | | | | |
| Bill Breaker 29100 Approaching | 24 | 1.5 | 0 | | | | | | | |
| Bill Breaker 29200 Approaching | 12 | 0.8 | 0 | | | | | | | |
| Bill Breaker 29300 Approaching | 7 | 0.4 | 0 | | | | | | | |
| Bill Breaker 29500 Approaching | 25 | 1.6 | 0 | | | | | | | |
| Bill Breaker 29500 Crossing | 4 | 0.2 | 0 | | | | | | | |
| Bill Breaker 29600 Crossing | 3 | 0.2 | 0 | | | | | | | |
| Bill Breaker 29600 Approaching | 5 | 0.3 | 0 | | | | | | | |
| Bill Breaker 29700 Approaching | 13 | 0.8 | 0 | | | | | | | |
| Bill Breaker 29800 Approaching | 11 | 0.7 | 0 | | | | | | | |
| Bill Breaker 29900 Approaching | 14 | 0.9 | 0 | | | | | | | |
| Bill Breaker 29900 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29800 Crossing | 6 | 0.4 | 0 | | | | | | | |
| Bill Breaker 29300 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29400 Approaching | 3 | 0.2 | 0 | | | | | | | |
| Bill Breaker 29200 Crossing | 4 | 0.2 | 0 | | | | | | | |
| ORB Flip - | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 30000 Approaching | 5 | 0.3 | 0 | | | | | | | |
| Bill Breaker 30100 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 30100 Approaching | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29700 Crossing | 1 | 0.1 | 0 | | | | | | | |

## MES 2m — 10/19 to 11/06 (17 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Key Level Alert | 151 | 8.9 | 139 | 55 | +5.44 | +756.8 | 71 | +4.59 | +638.1 | ✱ |
| Outside HTF ORB | 203 | 11.9 | 202 | 45 | +2.14 | +431.5 | 65 | +3.05 | +615.4 | ✱ |
| ORB Pass - | 84 | 4.9 | 84 | 56 | +5.09 | +427.5 | 61 | +2.64 | +221.7 | ✱ |
| High Confluence Setup | 358 | 21.1 | 357 | 38 | +0.62 | +221.5 | 47 | +1.15 | +411.0 |  |
| LTF EMA20 Pierce | 318 | 18.7 | 318 | 42 | +1.44 | +457.8 | 44 | +0.39 | +124.7 |  |
| ORB Pass + | 114 | 6.7 | 113 | 50 | +2.91 | +328.5 | 54 | +1.97 | +222.1 | ✱ |
| VWAP Bounce - High R | 100 | 5.9 | 98 | 49 | +3.49 | +341.8 | 58 | +1.75 | +171.4 | ✱ |
| HTF EMA20 Pierce | 174 | 10.2 | 172 | 42 | +0.52 | +88.8 | 51 | +1.18 | +202.2 |  |
| HTF | 265 | 15.6 | 263 | 35 | -0.25 | -64.5 | 43 | +0.16 | +42.5 |  |
| HTF EMA9 Pierce | 289 | 17.0 | 286 | 38 | -0.35 | -100.8 | 42 | +0.21 | +60.2 |  |
| HTF Pullback Entry - Structure Confirmed | 3 | 0.2 | 3 | 0 | -8.58 | -25.8 | 0 | -9.22 | -27.6 |  |
| Trade Setup | 126 | 7.4 | 126 | 26 | -1.62 | -203.8 | 33 | -0.70 | -88.2 |  |
| LTF EMA20 Touch - Pullback Entry | 71 | 4.2 | 71 | 24 | -2.59 | -183.8 | 23 | -1.73 | -122.8 |  |
| A+ Setup | 214 | 12.6 | 214 | 29 | -1.24 | -266.0 | 33 | -0.95 | -203.8 |  |
| Price Enters HTF EMA9/20 Zone | 166 | 9.8 | 165 | 21 | -2.45 | -404.2 | 15 | -2.67 | -441.0 |  |
| HTF EMA20 Touch - Pullback Entry | 184 | 10.8 | 182 | 16 | -3.07 | -559.0 | 15 | -2.72 | -495.5 |  |
| Setup Ended | 125 | 7.4 | 0 | | | | | | | |
| Bill Breaker 7400 Crossing | 8 | 0.5 | 0 | | | | | | | |
| TP1 Partial | 53 | 3.1 | 0 | | | | | | | |
| VWAP Crossing | 42 | 2.5 | 0 | | | | | | | |
| VWAP Approaching | 162 | 9.5 | 0 | | | | | | | |
| EMA 20 Approaching | 482 | 28.4 | 0 | | | | | | | |
| EMA 200 Approaching | 55 | 3.2 | 0 | | | | | | | |
| EMA 20 Crossing | 102 | 6.0 | 0 | | | | | | | |
| Setup Confirmed | 47 | 2.8 | 0 | | | | | | | |
| Bill Breaker 7400 Approaching | 6 | 0.4 | 0 | | | | | | | |
| ORB High Crossing | 44 | 2.6 | 0 | | | | | | | |
| EMA 200 Crossing | 51 | 3.0 | 0 | | | | | | | |
| Bill Breaker 7500 Approaching | 4 | 0.2 | 0 | | | | | | | |
| ORB Low Approaching | 35 | 2.1 | 0 | | | | | | | |
| Bill Breaker 7600 Approaching | 9 | 0.5 | 0 | | | | | | | |
| ORB High Approaching | 42 | 2.5 | 0 | | | | | | | |
| Bill Breaker 7700 Approaching | 15 | 0.9 | 0 | | | | | | | |
| Bill Breaker 7700 Crossing | 11 | 0.6 | 0 | | | | | | | |
| ORB Low Crossing | 30 | 1.8 | 0 | | | | | | | |
| YDL Approaching | 18 | 1.1 | 0 | | | | | | | |
| ORB Flip + | 7 | 0.4 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 17 | 1.0 | 0 | | | | | | | |
| YDH Approaching | 21 | 1.2 | 0 | | | | | | | |
| Bill Breaker 7600 Crossing | 1 | 0.1 | 0 | | | | | | | |
| YDL Crossing | 6 | 0.4 | 0 | | | | | | | |
| ORB Flip - | 10 | 0.6 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 13 | 0.8 | 0 | | | | | | | |
| Bill Breaker 7800 Approaching | 5 | 0.3 | 0 | | | | | | | |
| YDH Crossing | 8 | 0.5 | 0 | | | | | | | |
| Bill Breaker 7800 Crossing | 3 | 0.2 | 0 | | | | | | | |

## MGC 2m — 10/19 to 11/06 (16 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Outside HTF ORB | 189 | 11.8 | 189 | 54 | +3.20 | +605.2 | 65 | +2.41 | +455.2 | ✱ |
| High Confluence Setup | 408 | 25.5 | 406 | 38 | +1.30 | +529.0 | 48 | +0.97 | +393.5 | ✱ |
| Key Level Alert | 205 | 12.8 | 200 | 58 | +1.76 | +351.3 | 64 | +2.21 | +442.8 | ✱ |
| HTF EMA9 Pierce | 289 | 18.1 | 289 | 43 | +1.13 | +326.1 | 48 | +0.86 | +249.9 | ✱ |
| HTF EMA20 Pierce | 181 | 11.3 | 179 | 45 | +1.50 | +267.7 | 49 | +0.85 | +152.7 | ✱ |
| ORB Pass + | 56 | 3.5 | 56 | 57 | +2.34 | +131.0 | 68 | +3.02 | +169.3 |  |
| ORB Pass - | 106 | 6.6 | 106 | 46 | +1.76 | +186.5 | 53 | +0.95 | +101.0 |  |
| LTF EMA20 Pierce | 304 | 19.0 | 304 | 43 | +0.41 | +123.2 | 44 | +0.34 | +104.3 | ✱ |
| VWAP Bounce - High R | 59 | 3.7 | 57 | 40 | +0.38 | +21.4 | 67 | +2.16 | +123.0 |  |
| A+ Setup | 175 | 10.9 | 174 | 38 | +0.53 | +92.3 | 37 | -0.12 | -20.6 |  |
| LTF EMA20 Touch - Pullback Entry | 58 | 3.6 | 58 | 41 | +1.00 | +57.8 | 29 | -0.69 | -40.0 |  |
| HTF Pullback Entry - Structure Confirmed | 8 | 0.5 | 8 | 12 | -5.13 | -41.0 | 25 | -1.10 | -8.8 |  |
| HTF | 230 | 14.4 | 228 | 40 | -0.31 | -71.3 | 39 | +0.07 | +15.7 |  |
| Trade Setup | 157 | 9.8 | 157 | 29 | -1.05 | -164.1 | 38 | -0.21 | -33.0 |  |
| Price Enters HTF EMA9/20 Zone | 160 | 10.0 | 159 | 17 | -2.24 | -355.9 | 22 | -1.53 | -243.2 |  |
| HTF EMA20 Touch - Pullback Entry | 200 | 12.5 | 199 | 27 | -1.02 | -203.5 | 15 | -2.09 | -415.4 |  |
| EMA 20 Approaching | 439 | 27.4 | 0 | | | | | | | |
| YDL Approaching | 21 | 1.3 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 26 | 1.6 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 28 | 1.8 | 0 | | | | | | | |
| VWAP Approaching | 125 | 7.8 | 0 | | | | | | | |
| Setup Ended | 158 | 9.9 | 0 | | | | | | | |
| ORB High Approaching | 33 | 2.1 | 0 | | | | | | | |
| EMA 200 Approaching | 50 | 3.1 | 0 | | | | | | | |
| EMA 200 Crossing | 48 | 3.0 | 0 | | | | | | | |
| EMA 20 Crossing | 98 | 6.1 | 0 | | | | | | | |
| TP1 Partial | 76 | 4.8 | 0 | | | | | | | |
| Setup Confirmed | 87 | 5.4 | 0 | | | | | | | |
| ORB High Crossing | 27 | 1.7 | 0 | | | | | | | |
| VWAP Crossing | 37 | 2.3 | 0 | | | | | | | |
| ORB Low Crossing | 54 | 3.4 | 0 | | | | | | | |
| ORB Low Approaching | 45 | 2.8 | 0 | | | | | | | |
| Bill Breaker 4100 Approaching | 10 | 0.6 | 0 | | | | | | | |
| Bill Breaker 4100 Crossing | 6 | 0.4 | 0 | | | | | | | |
| YDH Approaching | 12 | 0.8 | 0 | | | | | | | |
| YDH Crossing | 6 | 0.4 | 0 | | | | | | | |
| YDL Crossing | 17 | 1.1 | 0 | | | | | | | |
| ORB Flip - | 10 | 0.6 | 0 | | | | | | | |
| Bill Breaker 3900 Approaching | 7 | 0.4 | 0 | | | | | | | |
| ORB Flip + | 7 | 0.4 | 0 | | | | | | | |
| Bill Breaker 4000 Crossing | 3 | 0.2 | 0 | | | | | | | |
| Bill Breaker 4000 Approaching | 3 | 0.2 | 0 | | | | | | | |

## MES 5m — 10/20 to 11/06 (16 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Outside HTF ORB | 134 | 8.4 | 133 | 53 | +5.58 | +741.8 | 62 | +4.30 | +572.1 | ✱ |
| Key Level Alert | 83 | 5.2 | 70 | 59 | +7.31 | +512.0 | 70 | +6.73 | +471.2 | ✱ |
| LTF EMA20 Pierce | 115 | 7.2 | 113 | 49 | +2.52 | +285.2 | 51 | +1.84 | +207.7 |  |
| HTF EMA9 Pierce | 115 | 7.2 | 111 | 44 | +1.31 | +145.5 | 50 | +2.33 | +258.4 |  |
| ORB Pass - | 53 | 3.3 | 53 | 40 | +4.49 | +237.8 | 49 | +2.43 | +129.0 |  |
| HTF EMA20 Pierce | 82 | 5.1 | 80 | 48 | +1.26 | +101.0 | 55 | +2.65 | +212.2 | ✱ |
| ORB Pass + | 76 | 4.8 | 74 | 51 | +1.55 | +114.8 | 51 | +1.92 | +141.9 | ✱ |
| VWAP Bounce - High R | 33 | 2.1 | 30 | 50 | +2.73 | +82.0 | 73 | +5.03 | +150.8 | ✱ |
| A+ Setup | 95 | 5.9 | 95 | 37 | +1.21 | +114.5 | 38 | -0.28 | -26.9 |  |
| HTF Pullback Entry - Structure Confirmed | 3 | 0.2 | 3 | 33 | -3.00 | -9.0 | 33 | -1.51 | -4.5 |  |
| Trade Setup | 64 | 4.0 | 64 | 30 | -1.63 | -104.2 | 39 | -0.31 | -20.0 |  |
| HTF | 99 | 6.2 | 99 | 38 | -1.46 | -144.8 | 40 | +0.19 | +18.4 |  |
| LTF EMA20 Touch - Pullback Entry | 35 | 2.2 | 34 | 26 | -5.74 | -195.0 | 24 | -4.74 | -161.1 |  |
| High Confluence Setup | 131 | 8.2 | 129 | 34 | -3.09 | -399.0 | 43 | -0.35 | -45.2 |  |
| Price Enters HTF EMA9/20 Zone | 53 | 3.3 | 53 | 13 | -7.05 | -373.8 | 15 | -4.62 | -244.7 |  |
| HTF EMA20 Touch - Pullback Entry | 89 | 5.6 | 87 | 9 | -9.89 | -860.5 | 14 | -5.41 | -470.3 |  |
| EMA 20 Approaching | 196 | 12.2 | 0 | | | | | | | |
| Bill Breaker 7400 Approaching | 10 | 0.6 | 0 | | | | | | | |
| VWAP Approaching | 79 | 4.9 | 0 | | | | | | | |
| VWAP Crossing | 20 | 1.2 | 0 | | | | | | | |
| EMA 200 Crossing | 9 | 0.6 | 0 | | | | | | | |
| Setup Ended | 66 | 4.1 | 0 | | | | | | | |
| EMA 20 Crossing | 41 | 2.6 | 0 | | | | | | | |
| Setup Confirmed | 26 | 1.6 | 0 | | | | | | | |
| ORB High Crossing | 26 | 1.6 | 0 | | | | | | | |
| ORB High Approaching | 26 | 1.6 | 0 | | | | | | | |
| Bill Breaker 7400 Crossing | 2 | 0.1 | 0 | | | | | | | |
| TP1 Partial | 34 | 2.1 | 0 | | | | | | | |
| YDL Approaching | 14 | 0.9 | 0 | | | | | | | |
| Bill Breaker 7500 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 7500 Approaching | 3 | 0.2 | 0 | | | | | | | |
| Bill Breaker 7700 Approaching | 11 | 0.7 | 0 | | | | | | | |
| YDH Approaching | 12 | 0.8 | 0 | | | | | | | |
| Bill Breaker 7600 Approaching | 13 | 0.8 | 0 | | | | | | | |
| ORB Low Approaching | 43 | 2.7 | 0 | | | | | | | |
| ORB Flip + | 9 | 0.6 | 0 | | | | | | | |
| Bill Breaker 7600 Crossing | 2 | 0.1 | 0 | | | | | | | |
| YDL Crossing | 2 | 0.1 | 0 | | | | | | | |
| ORB Flip - | 8 | 0.5 | 0 | | | | | | | |
| ORB Low Crossing | 13 | 0.8 | 0 | | | | | | | |
| EMA 200 Approaching | 20 | 1.2 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 14 | 0.9 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 7700 Crossing | 3 | 0.2 | 0 | | | | | | | |
| YDH Crossing | 4 | 0.2 | 0 | | | | | | | |
| Bill Breaker 7800 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 7800 Approaching | 2 | 0.1 | 0 | | | | | | | |

## MGC 5m — 10/20 to 11/06 (16 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Outside HTF ORB | 111 | 6.9 | 111 | 60 | +4.61 | +511.8 | 61 | +3.26 | +361.7 | ✱ |
| Key Level Alert | 139 | 8.7 | 133 | 54 | +2.05 | +272.1 | 66 | +3.42 | +454.7 | ✱ |
| HTF EMA9 Pierce | 116 | 7.2 | 115 | 43 | +2.01 | +230.8 | 54 | +2.15 | +247.6 | ✱ |
| LTF EMA20 Pierce | 116 | 7.2 | 116 | 49 | +0.81 | +94.4 | 53 | +2.12 | +245.4 | ✱ |
| ORB Pass + | 34 | 2.1 | 34 | 74 | +4.70 | +159.8 | 62 | +3.12 | +106.2 | ✱ |
| ORB Pass - | 56 | 3.5 | 56 | 43 | +2.86 | +160.2 | 46 | +1.25 | +69.9 |  |
| HTF EMA20 Pierce | 62 | 3.9 | 62 | 50 | +1.67 | +103.3 | 53 | +1.33 | +82.6 | ✱ |
| High Confluence Setup | 153 | 9.6 | 153 | 31 | -0.41 | -62.3 | 46 | +1.21 | +185.3 |  |
| VWAP Bounce - High R | 15 | 0.9 | 15 | 47 | -0.07 | -1.0 | 80 | +4.35 | +65.3 |  |
| Trade Setup | 52 | 3.2 | 52 | 33 | +0.10 | +5.3 | 44 | +0.85 | +44.4 |  |
| HTF Pullback Entry - Structure Confirmed | 1 | 0.1 | 1 | 0 | -12.50 | -12.5 | 0 | -8.15 | -8.2 |  |
| A+ Setup | 103 | 6.4 | 102 | 38 | -0.67 | -68.8 | 38 | -0.38 | -38.3 |  |
| Price Enters HTF EMA9/20 Zone | 68 | 4.2 | 68 | 28 | -0.42 | -28.6 | 32 | -1.18 | -80.4 |  |
| LTF EMA20 Touch - Pullback Entry | 36 | 2.2 | 36 | 31 | -1.66 | -59.6 | 25 | -1.52 | -54.8 |  |
| HTF | 97 | 6.1 | 97 | 41 | -0.93 | -90.5 | 39 | -0.63 | -61.6 |  |
| HTF EMA20 Touch - Pullback Entry | 68 | 4.2 | 67 | 28 | -1.41 | -94.2 | 24 | -2.60 | -174.3 |  |
| EMA 20 Approaching | 151 | 9.4 | 0 | | | | | | | |
| EMA 200 Crossing | 18 | 1.1 | 0 | | | | | | | |
| VWAP Approaching | 56 | 3.5 | 0 | | | | | | | |
| Setup Ended | 61 | 3.8 | 0 | | | | | | | |
| YDL Approaching | 16 | 1.0 | 0 | | | | | | | |
| TP1 Partial | 26 | 1.6 | 0 | | | | | | | |
| EMA 200 Approaching | 25 | 1.6 | 0 | | | | | | | |
| ORB High Approaching | 33 | 2.1 | 0 | | | | | | | |
| EMA 20 Crossing | 39 | 2.4 | 0 | | | | | | | |
| ORB High Crossing | 16 | 1.0 | 0 | | | | | | | |
| ORB Low Approaching | 28 | 1.8 | 0 | | | | | | | |
| ORB Low Crossing | 18 | 1.1 | 0 | | | | | | | |
| YDL Crossing | 3 | 0.2 | 0 | | | | | | | |
| Bill Breaker 4100 Approaching | 8 | 0.5 | 0 | | | | | | | |
| VWAP Crossing | 19 | 1.2 | 0 | | | | | | | |
| ORB Flip + | 5 | 0.3 | 0 | | | | | | | |
| Setup Confirmed | 26 | 1.6 | 0 | | | | | | | |
| YDH Approaching | 14 | 0.9 | 0 | | | | | | | |
| ORB Flip - | 7 | 0.4 | 0 | | | | | | | |
| Bill Breaker 3900 Approaching | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 4000 Crossing | 2 | 0.1 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 4000 Approaching | 7 | 0.4 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 2 | 0.1 | 0 | | | | | | | |

## Trade Setups drawn outside the alert sessions (replay, Jan–Oct, live gates, base exits)

CBC sends no alert outside Asia 18:00–22:30, London 03:00–07:45, NY 09:30–17:00 ET (⑤ Alerts session boxes). The chart still draws these setups.

| Chart | Window | Setups | Win % | Net | Avg | Net by third (3m/5m: Jan–Mar / Apr–Jun / Jul–Oct; 2m: Jun–Jul / Aug / Sep–Oct) |
|---|---|---|---|---|---|---|
| MES 3m | inside sessions | 1163 | 49% | +16 | +0.01 | +107 / -199 / +109 |
| MES 3m | 22:30–03:00 | 374 | 53% | +71 | +0.19 | +14 / +19 / +38 |
| MES 3m | 07:45–09:30 | 182 | 46% | -71 | -0.39 | +2 / -34 / -40 |
| MGC 3m | inside sessions | 811 | 50% | +195 | +0.24 | +56 / +62 / +77 |
| MGC 3m | 22:30–03:00 | 248 | 54% | +159 | +0.64 | +120 / +35 / +4 |
| MGC 3m | 07:45–09:30 | 121 | 45% | -77 | -0.63 | -14 / -95 / +32 |
| MES 2m | inside sessions | 832 | 47% | -196 | -0.24 | -135 / +43 / -103 |
| MES 2m | 22:30–03:00 | 278 | 53% | -6 | -0.02 | +50 / -2 / -54 |
| MES 2m | 07:45–09:30 | 116 | 51% | +8 | +0.07 | -19 / +39 / -13 |
| MGC 2m | inside sessions | 1027 | 51% | +164 | +0.16 | +112 / +92 / -40 |
| MGC 2m | 22:30–03:00 | 314 | 52% | +85 | +0.27 | -36 / +27 / +94 |
| MGC 2m | 07:45–09:30 | 158 | 53% | +92 | +0.58 | +7 / +11 / +74 |
| MES 5m | inside sessions | 823 | 53% | +166 | +0.20 | -125 / +149 / +142 |
| MES 5m | 22:30–03:00 | 233 | 45% | -56 | -0.24 | +10 / -19 / -47 |
| MES 5m | 07:45–09:30 | 127 | 45% | -119 | -0.94 | -31 / -35 / -53 |
| MGC 5m | inside sessions | 803 | 50% | -188 | -0.23 | -143 / +20 / -66 |
| MGC 5m | 22:30–03:00 | 237 | 50% | -49 | -0.21 | -30 / +22 / -41 |
| MGC 5m | 07:45–09:30 | 133 | 57% | +120 | +0.90 | +48 / +36 / +36 |
