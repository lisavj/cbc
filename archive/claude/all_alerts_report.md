# All CBC alerts re-checked -- 2026-11-13 20:43 ET (weekly run 3)

**STUDY SETTINGS STALE:** settings_sync_report (11/13 16:47 ET, CBC v10.96) lists 3 MISMATCH: chop_sim `EXIT` MES 3m (part 'tod' vs 100 % at TP1 all day), chop_sim `EXIT` MGC 3m (50 % / trail 3.5 vs FLIP 0 %), mes3_ema_grid `LIVE` part 'tod'. This study's replay passes its own base exits (`ss.QB`), so those constants do not change its numbers. Two gaps that are not in the settings map: (1) this script replays MGC 2m with the range gate OFF (live has it ON since v10.77); a side run with it ON is shown below. (2) On **MES 3m** the alerts follow **⑤ Alerts → "Alert hours per symbol/timeframe"** (`MES 3m 1830-2100, 0430-1300, 1400-1430`, v10.75+). The Asian / London / New York boxes are ignored there, so this study's MES 3m session-gap rows do not match the live alert hours.

Weekly run 3 (run 1 = 11/01, run 2 = 11/07 repaired). Alert Feed 10/19–11/13: 47,887 alerts, 46,383 after merging 1,504 near-duplicate copies (DATA_NOTES note 1; the store is not cleaned yet). The script now merges them; this is a data fix, and the method is unchanged. Replay: Jan–11/13 (2m Jun–11/13). The first two thirds are the same history every week and only the last third grows, so consecutive runs overlap heavily.

## Since last week (run 2 → run 3)

### Verdict

**UPDATE WARRANTED (3-run rule met):**

- **MGC 2m: ⑤ Alerts → London window 0300-0745 → 0300-0930** (London end 07:45 → 09:30). Or set New York start 09:30 → 07:45; either covers the gap. Evidence: the 07:45–09:30 gap has 165 setups, net +79, thirds +7 / +11 / +61, avg +0.48 vs +0.16 inside. All thirds have been positive for 3 runs. With the live range gate ON it still holds: 146 setups, +65, thirds +3 / +35 / +27, avg +0.45 vs +0.23. After the change, recreate the MGC 2m TradingView alert.
- **MGC 5m: ⑤ Alerts → London window 0300-0745 → 0300-0930** (or New York start 09:30 → 07:45). Evidence: the 07:45–09:30 gap has 137 setups, net +141, thirds +48 / +36 / +57, avg +1.03 vs −0.25 inside. All thirds have been positive for 3 runs. After the change, recreate the MGC 5m TradingView alert.
- **Alert types:** untick these checkboxes. Each type below has been negative under both exits for 3 runs with ≥ 30 directional alerts. The checkboxes only change alert messages, not Trade Setups.
  - **"Price Enters HTF EMA9/20 Zone - Entry"** (⑤ Alerts) on MES 3m, MNQ 3m, MES 2m, MGC 2m, MES 5m and MGC 5m. Not on MGC 3m, which is at 1 run.
  - **"Alert: EMA20 Touch - Pullback Entry (LTF/HTF)"** (⑤ Alerts) on MES 3m, MNQ 3m, MES 2m and MES 5m. On these charts both the HTF and the LTF touch types meet the rule. One checkbox mutes both types. On MGC 3m and MGC 2m only the HTF touch meets the rule (LTF touch is at 0 / 1 run), and on MGC 5m both types are at 2 runs, so wait on those three charts.
  - **"A+ Setup (Long/Short)"** (⑤ Alerts) on MES 2m: 279 alerts, −187 / −117.

**Rule met on paper but no change:** on MES 3m, the 22:30–03:00 gap has been positive in all thirds for 3 runs: +56, thirds +14 / +19 / +24, avg +0.15 vs +0.01 inside, 386 setups. But MES 3m alerts use "Alert hours per symbol/timeframe", so changing the Asian end does nothing on that chart. A side check against the live MES 3m alert hours gives the 21:00–04:30 gap 593 setups, +46, thirds +25 / −31 / +52 (not all positive). The hours inside the live windows come out at −2. No MES 3m change.

**Current setting confirmed:** on MES 5m, the 07:45–09:30 gap has been negative in all thirds for 3 runs (−133, thirds −31 / −35 / −66).

### Session gaps (replay; net by third Jan–Mar / Apr–Jun / Jul–now, 2m Jun–Jul / Aug / Sep–now)

| Chart | Gap | Run 2 (11/07) | Run 3 (11/13) | Avg gap vs inside | Setups | All-thirds-positive, consecutive runs |
|---|---|---|---|---|---|---|
| MES 3m | 22:30–03:00 | +71 (+14/+19/+38) | +56 (+14/+19/+24) | +0.15 vs +0.01 | 386 | **3**, but n/a: MES 3m uses alert hours list (see above) |
| MES 3m | 07:45–09:30 | −71 (+2/−34/−40) | −70 (+2/−34/−38) | −0.38 vs +0.01 | 185 | 0 |
| MGC 3m | 22:30–03:00 | +159 (+120/+35/+4) | +165 (+120/+35/+10) | +0.64 vs +0.26 | 256 | 2 (run 4 = 11/20 could make 3) |
| MGC 3m | 07:45–09:30 | −77 (−14/−95/+32) | −61 (−14/−95/+48) | −0.49 vs +0.26 | 123 | 0 |
| MES 2m | 22:30–03:00 | −6 (+50/−2/−54) | −16 (+50/−2/−64) | −0.05 vs −0.25 | 287 | 0 |
| MES 2m | 07:45–09:30 | +8 (−19/+39/−13) | +4 (−19/+39/−17) | +0.03 vs −0.25 | 123 | 0 |
| MGC 2m | 22:30–03:00 | +85 (−36/+27/+94) | +110 (−36/+27/+119) | +0.33 vs +0.16 | 333 | 0 (first third −; range gate ON: +14/−7/+98) |
| MGC 2m | 07:45–09:30 | +92 (+7/+11/+74) | +79 (+7/+11/+61) | +0.48 vs +0.16 | 165 | **3 → change** |
| MES 5m | 22:30–03:00 | −56 (+10/−19/−47) | −46 (+10/−19/−37) | −0.19 vs +0.24 | 239 | 0 |
| MES 5m | 07:45–09:30 | −119 (−31/−35/−53) | −133 (−31/−35/−66) | −1.00 vs +0.24 | 132 | negative in all thirds 3 runs: current setting right |
| MGC 5m | 22:30–03:00 | −49 (−30/+22/−41) | −43 (−30/+22/−35) | −0.18 vs −0.25 | 243 | 0 |
| MGC 5m | 07:45–09:30 | +120 (+48/+36/+36) | +141 (+48/+36/+57) | +1.03 vs −0.25 | 137 | **3 → change** |

Side runs (same method, other windows or gates):
- MGC 2m with live range gate ON: inside 933 setups +215 (+0.23); 07:45–09:30 146 / +65 / +3 / +35 / +27; 22:30–03:00 274 / +104 / +14 / −7 / +98.
- MES 3m by live alert hours: inside 934 setups −2 (+85 / −137 / +50); 21:00–04:30 593 / +46 (+25 / −31 / +52); 13:00–14:00 + 14:30–17:00 + 18:00–18:30 229 / −47 (+14 / −47 / −14).

### Alert types: sign / ✱ changes vs run 2

- **MES 3m:** ORB Pass − gained ✱. LTF EMA20 Pierce lost ✱. New type "Exit Rule" (1 alert).
- **MGC 3m:** Trade Setup lost ✱. A+ Setup is now + under both exits (+82 / +18). Setup Blocked is now + under both. HTF (b) turned − (both − now, 214 alerts, streak 1). Price Enters HTF EMA9/20 Zone (a) turned − (both − now, streak 1). New "Exit Rule" (15).
- **MNQ 3m:** ORB Pass + gained ✱. No sign changes.
- **MES 2m:** HTF EMA20 Pierce gained ✱. HTF EMA9 Pierce (a) turned + (both +). HTF flipped: (a) + / (b) −.
- **MGC 2m:** High Confluence Setup lost ✱ (still + both). ORB Pass + and ORB Pass − gained ✱. A+ Setup (b) turned + (both +). LTF EMA20 Touch (a) turned − (both −, streak 1). HTF flipped: (a) + / (b) −.
- **MES 5m:** LTF EMA20 Pierce and HTF EMA9 Pierce gained ✱. HTF EMA20 Pierce lost ✱. Trade Setup (b) and High Confluence (b) turned +.
- **MGC 5m:** ORB Pass − and VWAP Bounce gained ✱. High Confluence (a), VWAP Bounce (a), HTF (both) turned +. A+ Setup (a) turned + (no longer both −).
- **Both-negative streaks (≥ 30 alerts):**
  - HTF EMA20 Touch – Pullback Entry: 3 runs on MES 3m, MGC 3m, MNQ 3m, MES 2m, MGC 2m and MES 5m; 2 on MGC 5m.
  - Price Enters HTF EMA9/20 Zone: 3 runs on MES 3m, MNQ 3m, MES 2m, MGC 2m, MES 5m and MGC 5m; 1 on MGC 3m.
  - LTF EMA20 Touch – Pullback Entry: 3 runs on MES 3m, MNQ 3m, MES 2m and MES 5m; 2 on MGC 5m; 1 on MGC 2m.
  - A+ Setup: 3 runs on MES 2m.
  - Trade Setup: 2 runs on MNQ 3m, MES 2m and MGC 2m (run 1 was not listed).
  - HTF: 1 run on MGC 3m.
- Stable good: Key Level Alert and Outside HTF ORB are ✱ on all 7 charts for the 3rd run.

---

# Every CBC alert type, scored — Fri 11/13/2026 20:45 ET

Every CBC alert type, scored -- 11/01/2026.

For each chart (MES / MGC / MNQ 3m, MES / MGC 2m, MES / MGC 5m) every directional alert section ("• <type>: LONG / SHORT /
Bullish / Bearish / Above / Below / Pass + / Pass - ...") stored in the Alert Feed is scored from the BarFeed bars with the
same two outcome rules as claude/alert_param_sweep.py:
  (a) entry = close of the alert candle, exit at the close of the first candle with an opposite HTF CBC flip, the candle
      ending 17:00 ET, or after 2 h;   (b) 1.3 ATR(14) stop / 2.0 ATR target (both in one candle = stop), else 17:00 ET.
Points per contract-point, before costs. ✱ = positive in both halves (by date) under both rules. Non-directional alerts
(Approaching / Crossing / Setup Ended / TP1 Partial / Shadow ...) are counted only.
Alert candle = the bar that closes at the alert's "Time:" (CBC alerts fire at the candle close).
Duplicate alerts (DATA_NOTES note 1, 11/13): same "Chart:" line + same "Time:" line + same set of "•" names received within
60 s count as ONE alert (longest text kept).
Also: Trade Setups the setup engine would draw OUTSIDE CBC's alert sessions (Asia 18:00-22:30, London 03:00-07:45,
NY 09:30-17:00 ET) never reach the feed -- replay counts / results for 3m and 5m (chop_sim, live gates, base exits).
Usage: python3 all_alerts_study.py

Alert Feed: 46383 alerts (47887 before removing 1504 near-duplicate copies), 2026-10-19 to 2026-11-13.

## MES 3m — 10/19 to 11/13 (20 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Outside HTF ORB | 194 | 9.7 | 193 | 51 | +5.29 | +1021.5 | 58 | +2.78 | +536.3 | ✱ |
| Key Level Alert | 123 | 6.2 | 112 | 59 | +8.05 | +901.8 | 68 | +5.37 | +602.0 | ✱ |
| ORB Pass - | 75 | 3.8 | 75 | 44 | +5.72 | +429.0 | 55 | +2.02 | +151.6 | ✱ |
| VWAP Bounce - High R | 80 | 4.0 | 77 | 45 | +3.11 | +239.5 | 66 | +3.97 | +305.9 | ✱ |
| LTF EMA20 Pierce | 219 | 10.9 | 217 | 41 | +1.01 | +219.5 | 50 | +1.44 | +312.1 |  |
| HTF EMA9 Pierce | 208 | 10.4 | 204 | 43 | +1.38 | +280.8 | 48 | +1.06 | +217.0 | ✱ |
| High Confluence Setup | 227 | 11.3 | 227 | 43 | +0.61 | +138.2 | 50 | +1.46 | +331.1 |  |
| ORB Pass + | 95 | 4.8 | 94 | 52 | +3.97 | +373.0 | 48 | +1.01 | +94.6 |  |
| Trade Setup | 121 | 6.0 | 121 | 40 | +1.49 | +180.5 | 44 | +1.01 | +121.7 |  |
| HTF EMA20 Pierce | 129 | 6.5 | 127 | 43 | +1.60 | +203.2 | 47 | +0.76 | +96.1 |  |
| Exit Rule | 1 | 0.1 | 1 | 100 | +34.75 | +34.8 | 100 | +19.20 | +19.2 |  |
| HTF | 194 | 9.7 | 193 | 39 | -0.57 | -109.5 | 45 | +0.59 | +113.4 |  |
| A+ Setup | 186 | 9.3 | 186 | 40 | +0.46 | +85.2 | 36 | -0.46 | -85.8 |  |
| HTF Pullback Entry - Structure Confirmed | 3 | 0.1 | 3 | 0 | -13.33 | -40.0 | 0 | -8.12 | -24.4 |  |
| LTF EMA20 Touch - Pullback Entry | 52 | 2.6 | 52 | 33 | -1.71 | -89.0 | 19 | -3.03 | -157.7 |  |
| Price Enters HTF EMA9/20 Zone | 98 | 4.9 | 97 | 19 | -4.90 | -475.8 | 20 | -2.91 | -282.5 |  |
| HTF EMA20 Touch - Pullback Entry | 148 | 7.4 | 146 | 23 | -4.02 | -586.2 | 12 | -4.11 | -600.7 |  |
| ORB Low Crossing | 20 | 1.0 | 0 | | | | | | | |
| TP1 Partial | 54 | 2.7 | 0 | | | | | | | |
| ORB Low Approaching | 40 | 2.0 | 0 | | | | | | | |
| EMA 20 Approaching | 407 | 20.4 | 0 | | | | | | | |
| Setup Ended | 122 | 6.1 | 0 | | | | | | | |
| VWAP Approaching | 143 | 7.2 | 0 | | | | | | | |
| EMA 20 Crossing | 81 | 4.0 | 0 | | | | | | | |
| VWAP Crossing | 31 | 1.6 | 0 | | | | | | | |
| EMA 200 Approaching | 38 | 1.9 | 0 | | | | | | | |
| Setup Confirmed | 36 | 1.8 | 0 | | | | | | | |
| ORB High Approaching | 45 | 2.2 | 0 | | | | | | | |
| ORB High Crossing | 32 | 1.6 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 8 | 0.4 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 18 | 0.9 | 0 | | | | | | | |
| EMA 200 Crossing | 31 | 1.6 | 0 | | | | | | | |
| YDL Approaching | 18 | 0.9 | 0 | | | | | | | |
| YDL Crossing | 12 | 0.6 | 0 | | | | | | | |
| YDH Approaching | 17 | 0.8 | 0 | | | | | | | |
| ORB Flip - | 7 | 0.3 | 0 | | | | | | | |
| Bill Breaker 7800 Approaching | 4 | 0.2 | 0 | | | | | | | |
| ORB Flip + | 10 | 0.5 | 0 | | | | | | | |
| Bill Breaker 7700 Approaching | 13 | 0.7 | 0 | | | | | | | |
| Bill Breaker 7700 Crossing | 4 | 0.2 | 0 | | | | | | | |
| YDH Crossing | 7 | 0.3 | 0 | | | | | | | |
| Bill Breaker 7600 Approaching | 14 | 0.7 | 0 | | | | | | | |
| Bill Breaker 7600 Crossing | 4 | 0.2 | 0 | | | | | | | |
| Bill Breaker 7500 Approaching | 5 | 0.2 | 0 | | | | | | | |
| Bill Breaker 7500 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 7400 Approaching | 16 | 0.8 | 0 | | | | | | | |
| Bill Breaker 7400 Crossing | 5 | 0.2 | 0 | | | | | | | |

## MGC 3m — 10/19 to 11/13 (23 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Outside HTF ORB | 223 | 9.7 | 223 | 55 | +2.39 | +533.9 | 70 | +3.83 | +853.6 | ✱ |
| LTF EMA20 Pierce | 283 | 12.3 | 283 | 50 | +2.61 | +739.3 | 53 | +1.80 | +508.2 | ✱ |
| Key Level Alert | 292 | 12.7 | 283 | 53 | +1.97 | +556.2 | 61 | +2.35 | +665.6 | ✱ |
| High Confluence Setup | 310 | 13.5 | 310 | 43 | +1.58 | +488.3 | 49 | +1.35 | +418.0 |  |
| HTF EMA9 Pierce | 262 | 11.4 | 261 | 46 | +1.69 | +439.9 | 51 | +1.18 | +307.3 | ✱ |
| HTF EMA20 Pierce | 166 | 7.2 | 162 | 45 | +1.74 | +282.4 | 53 | +1.88 | +304.6 | ✱ |
| ORB Pass - | 122 | 5.3 | 122 | 49 | +1.92 | +234.4 | 61 | +2.43 | +296.5 | ✱ |
| VWAP Bounce - High R | 98 | 4.3 | 95 | 54 | +1.53 | +145.5 | 63 | +2.18 | +207.6 | ✱ |
| ORB Pass + | 66 | 2.9 | 66 | 56 | +1.39 | +92.0 | 59 | +2.38 | +156.9 |  |
| Trade Setup | 90 | 3.9 | 90 | 37 | +1.53 | +138.0 | 43 | +0.72 | +64.9 |  |
| A+ Setup | 182 | 7.9 | 181 | 41 | +0.45 | +82.2 | 37 | +0.10 | +17.8 |  |
| Setup Blocked | 18 | 0.8 | 18 | 56 | +1.48 | +26.6 | 56 | +1.87 | +33.7 |  |
| LTF EMA20 Touch - Pullback Entry | 67 | 2.9 | 66 | 30 | +0.32 | +21.4 | 30 | -0.47 | -30.9 |  |
| Exit Rule | 15 | 0.7 | 15 | 20 | -3.51 | -52.7 | 33 | +0.20 | +3.1 |  |
| HTF Pullback Entry - Structure Confirmed | 11 | 0.5 | 11 | 9 | -4.98 | -54.8 | 9 | -3.39 | -37.3 |  |
| HTF | 219 | 9.5 | 214 | 37 | -0.25 | -52.7 | 38 | -0.24 | -50.5 |  |
| Price Enters HTF EMA9/20 Zone | 158 | 6.9 | 156 | 27 | -1.03 | -161.4 | 24 | -1.40 | -218.4 |  |
| HTF EMA20 Touch - Pullback Entry | 173 | 7.5 | 170 | 24 | -2.22 | -377.9 | 18 | -2.08 | -354.0 |  |
| Setup Ended | 89 | 3.9 | 0 | | | | | | | |
| EMA 20 Approaching | 509 | 22.1 | 0 | | | | | | | |
| VWAP Approaching | 128 | 5.6 | 0 | | | | | | | |
| TP1 Partial | 34 | 1.5 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 25 | 1.1 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 29 | 1.3 | 0 | | | | | | | |
| EMA 20 Crossing | 99 | 4.3 | 0 | | | | | | | |
| Setup Confirmed | 40 | 1.7 | 0 | | | | | | | |
| YDL Approaching | 33 | 1.4 | 0 | | | | | | | |
| ORB Low Approaching | 68 | 3.0 | 0 | | | | | | | |
| ORB Low Crossing | 57 | 2.5 | 0 | | | | | | | |
| VWAP Crossing | 38 | 1.7 | 0 | | | | | | | |
| YDL Crossing | 23 | 1.0 | 0 | | | | | | | |
| EMA 200 Approaching | 49 | 2.1 | 0 | | | | | | | |
| EMA 200 Crossing | 36 | 1.6 | 0 | | | | | | | |
| ORB High Crossing | 23 | 1.0 | 0 | | | | | | | |
| ORB Flip - | 10 | 0.4 | 0 | | | | | | | |
| ORB High Approaching | 47 | 2.0 | 0 | | | | | | | |
| ORB Flip + | 10 | 0.4 | 0 | | | | | | | |
| YDH Approaching | 10 | 0.4 | 0 | | | | | | | |
| Bill Breaker 4100 Approaching | 15 | 0.7 | 0 | | | | | | | |
| Bill Breaker 4100 Crossing | 5 | 0.2 | 0 | | | | | | | |
| Bill Breaker 4000 Approaching | 6 | 0.3 | 0 | | | | | | | |
| Bill Breaker 4000 Crossing | 6 | 0.3 | 0 | | | | | | | |
| YDH Crossing | 8 | 0.3 | 0 | | | | | | | |
| Bill Breaker 3900 Approaching | 7 | 0.3 | 0 | | | | | | | |
| Shadow Ended | 19 | 0.8 | 0 | | | | | | | |
| Bill Breaker 3900 Crossing | 5 | 0.2 | 0 | | | | | | | |

## MNQ 3m — 10/20 to 11/13 (20 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Key Level Alert | 175 | 8.8 | 164 | 57 | +45.76 | +7504.8 | 65 | +30.68 | +5031.5 | ✱ |
| Outside HTF ORB | 169 | 8.4 | 167 | 51 | +26.75 | +4467.5 | 60 | +27.20 | +4541.9 | ✱ |
| High Confluence Setup | 261 | 13.1 | 261 | 41 | +9.88 | +2579.0 | 49 | +11.22 | +2929.3 | ✱ |
| ORB Pass - | 55 | 2.8 | 54 | 43 | +39.75 | +2146.2 | 69 | +34.33 | +1853.6 |  |
| LTF EMA20 Pierce | 231 | 11.6 | 228 | 42 | +6.86 | +1564.0 | 44 | +7.69 | +1753.7 |  |
| ORB Pass + | 94 | 4.7 | 94 | 53 | +6.80 | +639.2 | 55 | +18.13 | +1704.0 | ✱ |
| A+ Setup | 156 | 7.8 | 156 | 37 | +6.85 | +1069.0 | 42 | +5.74 | +895.7 |  |
| VWAP Bounce - High R | 10 | 0.5 | 10 | 50 | +1.32 | +13.2 | 80 | +43.61 | +436.1 |  |
| HTF | 203 | 10.2 | 200 | 37 | -2.23 | -446.2 | 43 | +1.94 | +388.8 |  |
| HTF EMA20 Pierce | 114 | 5.7 | 112 | 37 | -3.47 | -388.5 | 44 | +1.91 | +213.9 |  |
| HTF EMA9 Pierce | 182 | 9.1 | 179 | 34 | -5.09 | -911.5 | 44 | +3.25 | +581.9 |  |
| HTF Pullback Entry - Structure Confirmed | 12 | 0.6 | 12 | 25 | -61.96 | -743.5 | 17 | -26.32 | -315.8 |  |
| LTF EMA20 Touch - Pullback Entry | 57 | 2.9 | 56 | 29 | -22.02 | -1233.0 | 23 | -14.78 | -827.8 |  |
| Trade Setup | 123 | 6.2 | 123 | 22 | -15.67 | -1928.0 | 24 | -13.96 | -1717.6 |  |
| Price Enters HTF EMA9/20 Zone | 115 | 5.8 | 113 | 21 | -25.62 | -2894.5 | 19 | -23.91 | -2701.4 |  |
| HTF EMA20 Touch - Pullback Entry | 151 | 7.5 | 149 | 19 | -26.54 | -3954.0 | 15 | -25.74 | -3835.5 |  |
| Setup Ended | 120 | 6.0 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 29 | 1.4 | 0 | | | | | | | |
| EMA 20 Approaching | 261 | 13.1 | 0 | | | | | | | |
| EMA 20 Crossing | 49 | 2.5 | 0 | | | | | | | |
| Setup Confirmed | 31 | 1.6 | 0 | | | | | | | |
| TP1 Partial | 37 | 1.9 | 0 | | | | | | | |
| VWAP Approaching | 78 | 3.9 | 0 | | | | | | | |
| EMA 200 Crossing | 20 | 1.0 | 0 | | | | | | | |
| Bill Breaker 29700 Approaching | 13 | 0.7 | 0 | | | | | | | |
| Bill Breaker 29700 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29900 Approaching | 14 | 0.7 | 0 | | | | | | | |
| ORB High Approaching | 55 | 2.8 | 0 | | | | | | | |
| ORB Flip + | 4 | 0.2 | 0 | | | | | | | |
| ORB Low Approaching | 45 | 2.2 | 0 | | | | | | | |
| EMA 200 Approaching | 67 | 3.4 | 0 | | | | | | | |
| YDH Approaching | 16 | 0.8 | 0 | | | | | | | |
| Bill Breaker 29800 Approaching | 11 | 0.6 | 0 | | | | | | | |
| VWAP Crossing | 14 | 0.7 | 0 | | | | | | | |
| ORB High Crossing | 15 | 0.8 | 0 | | | | | | | |
| Bill Breaker 30000 Approaching | 5 | 0.2 | 0 | | | | | | | |
| Bill Breaker 30100 Approaching | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 30100 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29800 Crossing | 6 | 0.3 | 0 | | | | | | | |
| YDL Approaching | 14 | 0.7 | 0 | | | | | | | |
| YDL Crossing | 6 | 0.3 | 0 | | | | | | | |
| Bill Breaker 29500 Approaching | 25 | 1.2 | 0 | | | | | | | |
| ORB Low Crossing | 9 | 0.5 | 0 | | | | | | | |
| Bill Breaker 29300 Approaching | 7 | 0.3 | 0 | | | | | | | |
| Bill Breaker 29200 Approaching | 12 | 0.6 | 0 | | | | | | | |
| Bill Breaker 29100 Approaching | 24 | 1.2 | 0 | | | | | | | |
| Bill Breaker 29200 Crossing | 4 | 0.2 | 0 | | | | | | | |
| ORB Flip - | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29100 Crossing | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29400 Approaching | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29500 Crossing | 4 | 0.2 | 0 | | | | | | | |
| YDH Crossing | 7 | 0.3 | 0 | | | | | | | |
| Bill Breaker 29300 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29900 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29600 Approaching | 5 | 0.2 | 0 | | | | | | | |
| Bill Breaker 29600 Crossing | 3 | 0.1 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 29000 Approaching | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28900 Approaching | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28700 Approaching | 12 | 0.6 | 0 | | | | | | | |
| Bill Breaker 28800 Approaching | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28700 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28600 Approaching | 4 | 0.2 | 0 | | | | | | | |
| Bill Breaker 28400 Approaching | 14 | 0.7 | 0 | | | | | | | |
| Bill Breaker 28200 Approaching | 9 | 0.5 | 0 | | | | | | | |
| Bill Breaker 28100 Approaching | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28300 Approaching | 14 | 0.7 | 0 | | | | | | | |
| Bill Breaker 28400 Crossing | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27900 Approaching | 6 | 0.3 | 0 | | | | | | | |
| Bill Breaker 27900 Crossing | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27800 Approaching | 7 | 0.3 | 0 | | | | | | | |
| Bill Breaker 27700 Approaching | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28500 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28500 Approaching | 11 | 0.6 | 0 | | | | | | | |
| Bill Breaker 28800 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28600 Crossing | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28300 Crossing | 4 | 0.2 | 0 | | | | | | | |
| Bill Breaker 28000 Approaching | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28000 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27300 Approaching | 5 | 0.2 | 0 | | | | | | | |
| Bill Breaker 27200 Approaching | 12 | 0.6 | 0 | | | | | | | |
| Bill Breaker 27000 Approaching | 4 | 0.2 | 0 | | | | | | | |
| Bill Breaker 26800 Approaching | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27100 Approaching | 15 | 0.8 | 0 | | | | | | | |
| Bill Breaker 26900 Approaching | 8 | 0.4 | 0 | | | | | | | |
| Bill Breaker 26900 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27100 Crossing | 7 | 0.3 | 0 | | | | | | | |
| Bill Breaker 26700 Approaching | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 26600 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27000 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27200 Crossing | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27300 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 28200 Crossing | 1 | 0.1 | 0 | | | | | | | |
| Bill Breaker 27800 Crossing | 2 | 0.1 | 0 | | | | | | | |

## MES 2m — 10/19 to 11/13 (23 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Key Level Alert | 215 | 9.3 | 201 | 59 | +5.85 | +1176.2 | 72 | +4.84 | +972.1 | ✱ |
| Outside HTF ORB | 270 | 11.7 | 268 | 49 | +2.94 | +788.5 | 65 | +3.21 | +860.2 | ✱ |
| High Confluence Setup | 493 | 21.4 | 492 | 40 | +0.65 | +318.8 | 50 | +1.48 | +727.4 |  |
| ORB Pass + | 153 | 6.7 | 152 | 51 | +3.39 | +515.5 | 53 | +1.90 | +289.3 | ✱ |
| VWAP Bounce - High R | 147 | 6.4 | 143 | 50 | +3.16 | +451.5 | 61 | +2.15 | +306.7 | ✱ |
| ORB Pass - | 103 | 4.5 | 102 | 56 | +4.38 | +446.5 | 59 | +2.49 | +253.9 | ✱ |
| LTF EMA20 Pierce | 432 | 18.8 | 431 | 41 | +1.03 | +445.0 | 43 | +0.25 | +108.7 |  |
| HTF EMA20 Pierce | 245 | 10.7 | 241 | 43 | +1.00 | +240.0 | 49 | +1.06 | +254.3 | ✱ |
| HTF EMA9 Pierce | 391 | 17.0 | 388 | 41 | +0.45 | +175.0 | 44 | +0.57 | +222.4 |  |
| HTF | 367 | 16.0 | 363 | 37 | +0.07 | +25.5 | 40 | -0.10 | -36.5 |  |
| HTF Pullback Entry - Structure Confirmed | 7 | 0.3 | 7 | 14 | -6.18 | -43.2 | 29 | -3.08 | -21.6 |  |
| Trade Setup | 159 | 6.9 | 159 | 28 | -1.06 | -168.0 | 35 | -0.51 | -81.2 |  |
| A+ Setup | 279 | 12.1 | 279 | 32 | -0.67 | -187.2 | 36 | -0.42 | -116.7 |  |
| LTF EMA20 Touch - Pullback Entry | 96 | 4.2 | 96 | 27 | -2.40 | -230.0 | 21 | -2.06 | -197.6 |  |
| Price Enters HTF EMA9/20 Zone | 217 | 9.4 | 215 | 23 | -2.33 | -500.8 | 20 | -2.15 | -462.0 |  |
| HTF EMA20 Touch - Pullback Entry | 265 | 11.5 | 261 | 18 | -3.43 | -896.2 | 16 | -2.76 | -719.7 |  |
| TP1 Partial | 66 | 2.9 | 0 | | | | | | | |
| ORB Low Crossing | 33 | 1.4 | 0 | | | | | | | |
| VWAP Approaching | 226 | 9.8 | 0 | | | | | | | |
| EMA 20 Approaching | 695 | 30.2 | 0 | | | | | | | |
| VWAP Crossing | 54 | 2.3 | 0 | | | | | | | |
| Setup Ended | 156 | 6.8 | 0 | | | | | | | |
| EMA 20 Crossing | 149 | 6.5 | 0 | | | | | | | |
| Setup Confirmed | 62 | 2.7 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 24 | 1.0 | 0 | | | | | | | |
| ORB High Crossing | 52 | 2.3 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 23 | 1.0 | 0 | | | | | | | |
| EMA 200 Approaching | 74 | 3.2 | 0 | | | | | | | |
| EMA 200 Crossing | 69 | 3.0 | 0 | | | | | | | |
| ORB High Approaching | 60 | 2.6 | 0 | | | | | | | |
| ORB Low Approaching | 44 | 1.9 | 0 | | | | | | | |
| YDL Approaching | 22 | 1.0 | 0 | | | | | | | |
| YDL Crossing | 7 | 0.3 | 0 | | | | | | | |
| YDH Approaching | 24 | 1.0 | 0 | | | | | | | |
| ORB Flip - | 10 | 0.4 | 0 | | | | | | | |
| YDH Crossing | 10 | 0.4 | 0 | | | | | | | |
| Bill Breaker 7800 Approaching | 5 | 0.2 | 0 | | | | | | | |
| Bill Breaker 7800 Crossing | 3 | 0.1 | 0 | | | | | | | |
| ORB Flip + | 8 | 0.3 | 0 | | | | | | | |
| Bill Breaker 7700 Approaching | 15 | 0.7 | 0 | | | | | | | |
| Bill Breaker 7700 Crossing | 11 | 0.5 | 0 | | | | | | | |
| Bill Breaker 7600 Approaching | 21 | 0.9 | 0 | | | | | | | |
| Bill Breaker 7600 Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 7500 Approaching | 7 | 0.3 | 0 | | | | | | | |
| Bill Breaker 7400 Approaching | 7 | 0.3 | 0 | | | | | | | |
| Bill Breaker 7400 Crossing | 9 | 0.4 | 0 | | | | | | | |

## MGC 2m — 10/19 to 11/13 (22 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| High Confluence Setup | 556 | 25.3 | 554 | 40 | +1.64 | +906.8 | 48 | +1.15 | +634.9 |  |
| Outside HTF ORB | 248 | 11.3 | 248 | 55 | +3.01 | +746.3 | 65 | +2.37 | +587.0 | ✱ |
| HTF EMA9 Pierce | 391 | 17.8 | 388 | 46 | +1.90 | +737.3 | 51 | +1.06 | +413.0 | ✱ |
| Key Level Alert | 242 | 11.0 | 234 | 59 | +2.46 | +575.0 | 65 | +2.43 | +568.4 | ✱ |
| HTF EMA20 Pierce | 247 | 11.2 | 244 | 46 | +2.00 | +487.8 | 52 | +1.04 | +252.7 | ✱ |
| LTF EMA20 Pierce | 417 | 19.0 | 415 | 45 | +0.67 | +278.8 | 47 | +0.63 | +260.9 | ✱ |
| ORB Pass - | 140 | 6.4 | 140 | 48 | +1.97 | +275.7 | 57 | +1.25 | +174.4 | ✱ |
| ORB Pass + | 70 | 3.2 | 70 | 56 | +1.93 | +134.9 | 64 | +2.64 | +184.7 | ✱ |
| VWAP Bounce - High R | 139 | 6.3 | 133 | 48 | +0.05 | +7.0 | 62 | +1.83 | +243.1 |  |
| A+ Setup | 230 | 10.5 | 229 | 38 | +0.88 | +202.1 | 39 | +0.02 | +4.2 |  |
| HTF | 342 | 15.5 | 340 | 38 | +0.01 | +2.0 | 38 | -0.03 | -10.2 |  |
| HTF Pullback Entry - Structure Confirmed | 11 | 0.5 | 11 | 9 | -4.91 | -54.0 | 18 | -1.70 | -18.7 |  |
| LTF EMA20 Touch - Pullback Entry | 80 | 3.6 | 79 | 35 | -0.16 | -12.9 | 28 | -0.86 | -68.3 |  |
| Trade Setup | 227 | 10.3 | 227 | 33 | -0.29 | -64.7 | 37 | -0.24 | -55.4 |  |
| HTF EMA20 Touch - Pullback Entry | 269 | 12.2 | 267 | 26 | -0.88 | -233.8 | 16 | -1.98 | -527.9 |  |
| Price Enters HTF EMA9/20 Zone | 221 | 10.0 | 219 | 19 | -2.25 | -492.4 | 21 | -1.52 | -333.1 |  |
| EMA 20 Approaching | 686 | 31.2 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 31 | 1.4 | 0 | | | | | | | |
| EMA 20 Crossing | 127 | 5.8 | 0 | | | | | | | |
| VWAP Approaching | 170 | 7.7 | 0 | | | | | | | |
| TP1 Partial | 103 | 4.7 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 28 | 1.3 | 0 | | | | | | | |
| Setup Ended | 228 | 10.4 | 0 | | | | | | | |
| EMA 200 Approaching | 67 | 3.0 | 0 | | | | | | | |
| EMA 200 Crossing | 66 | 3.0 | 0 | | | | | | | |
| Setup Confirmed | 114 | 5.2 | 0 | | | | | | | |
| YDL Approaching | 27 | 1.2 | 0 | | | | | | | |
| ORB Low Approaching | 70 | 3.2 | 0 | | | | | | | |
| ORB Low Crossing | 75 | 3.4 | 0 | | | | | | | |
| VWAP Crossing | 50 | 2.3 | 0 | | | | | | | |
| YDL Crossing | 25 | 1.1 | 0 | | | | | | | |
| ORB Flip - | 11 | 0.5 | 0 | | | | | | | |
| ORB High Crossing | 36 | 1.6 | 0 | | | | | | | |
| ORB High Approaching | 43 | 2.0 | 0 | | | | | | | |
| ORB Flip + | 8 | 0.4 | 0 | | | | | | | |
| YDH Approaching | 15 | 0.7 | 0 | | | | | | | |
| Bill Breaker 4100 Approaching | 21 | 1.0 | 0 | | | | | | | |
| Bill Breaker 4100 Crossing | 7 | 0.3 | 0 | | | | | | | |
| Bill Breaker 4000 Approaching | 8 | 0.4 | 0 | | | | | | | |
| Bill Breaker 4000 Crossing | 6 | 0.3 | 0 | | | | | | | |
| YDH Crossing | 17 | 0.8 | 0 | | | | | | | |
| Bill Breaker 3900 Approaching | 9 | 0.4 | 0 | | | | | | | |
| Bill Breaker 3900 Crossing | 5 | 0.2 | 0 | | | | | | | |

## MES 5m — 10/20 to 11/12 (21 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Outside HTF ORB | 174 | 8.3 | 173 | 55 | +5.10 | +882.2 | 62 | +4.60 | +796.1 | ✱ |
| Key Level Alert | 120 | 5.7 | 104 | 60 | +7.61 | +791.0 | 68 | +5.91 | +614.6 | ✱ |
| HTF EMA9 Pierce | 145 | 6.9 | 140 | 44 | +2.23 | +312.2 | 51 | +2.66 | +373.1 | ✱ |
| LTF EMA20 Pierce | 141 | 6.7 | 139 | 49 | +2.58 | +358.2 | 52 | +1.86 | +257.9 | ✱ |
| ORB Pass + | 99 | 4.7 | 97 | 55 | +2.44 | +237.0 | 54 | +2.50 | +242.8 | ✱ |
| VWAP Bounce - High R | 45 | 2.1 | 41 | 56 | +4.55 | +186.8 | 73 | +5.80 | +237.6 | ✱ |
| HTF EMA20 Pierce | 95 | 4.5 | 93 | 43 | +0.59 | +55.2 | 55 | +2.71 | +252.4 |  |
| ORB Pass - | 63 | 3.0 | 63 | 37 | +2.93 | +184.5 | 46 | +1.31 | +82.3 |  |
| A+ Setup | 124 | 5.9 | 124 | 38 | +2.04 | +252.5 | 37 | -0.47 | -57.9 |  |
| Trade Setup | 81 | 3.9 | 81 | 32 | -0.54 | -43.8 | 41 | +0.33 | +26.6 |  |
| HTF Pullback Entry - Structure Confirmed | 4 | 0.2 | 4 | 50 | -1.94 | -7.8 | 25 | -2.65 | -10.6 |  |
| HTF | 119 | 5.7 | 118 | 38 | -1.25 | -147.2 | 38 | +0.09 | +10.4 |  |
| High Confluence Setup | 153 | 7.3 | 151 | 38 | -2.29 | -345.2 | 44 | +0.24 | +35.5 |  |
| LTF EMA20 Touch - Pullback Entry | 49 | 2.3 | 48 | 29 | -4.59 | -220.2 | 27 | -3.97 | -190.6 |  |
| Price Enters HTF EMA9/20 Zone | 65 | 3.1 | 65 | 17 | -6.60 | -429.0 | 17 | -4.44 | -288.4 |  |
| HTF EMA20 Touch - Pullback Entry | 104 | 5.0 | 102 | 12 | -8.55 | -872.0 | 18 | -4.39 | -447.7 |  |
| EMA 20 Approaching | 247 | 11.8 | 0 | | | | | | | |
| Setup Confirmed | 31 | 1.5 | 0 | | | | | | | |
| VWAP Approaching | 106 | 5.0 | 0 | | | | | | | |
| TP1 Partial | 44 | 2.1 | 0 | | | | | | | |
| ORB High Crossing | 33 | 1.6 | 0 | | | | | | | |
| EMA 20 Crossing | 62 | 3.0 | 0 | | | | | | | |
| Setup Ended | 80 | 3.8 | 0 | | | | | | | |
| VWAP Crossing | 23 | 1.1 | 0 | | | | | | | |
| ORB High Approaching | 41 | 2.0 | 0 | | | | | | | |
| ORB Low Crossing | 16 | 0.8 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 4 | 0.2 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 15 | 0.7 | 0 | | | | | | | |
| ORB Flip - | 8 | 0.4 | 0 | | | | | | | |
| ORB Low Approaching | 51 | 2.4 | 0 | | | | | | | |
| YDH Approaching | 19 | 0.9 | 0 | | | | | | | |
| Bill Breaker 7800 Approaching | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 7800 Crossing | 2 | 0.1 | 0 | | | | | | | |
| ORB Flip + | 10 | 0.5 | 0 | | | | | | | |
| Bill Breaker 7700 Approaching | 11 | 0.5 | 0 | | | | | | | |
| Bill Breaker 7700 Crossing | 3 | 0.1 | 0 | | | | | | | |
| EMA 200 Approaching | 34 | 1.6 | 0 | | | | | | | |
| EMA 200 Crossing | 11 | 0.5 | 0 | | | | | | | |
| YDH Crossing | 4 | 0.2 | 0 | | | | | | | |
| YDL Approaching | 14 | 0.7 | 0 | | | | | | | |
| YDL Crossing | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 7600 Approaching | 20 | 1.0 | 0 | | | | | | | |
| Bill Breaker 7600 Crossing | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 7500 Approaching | 6 | 0.3 | 0 | | | | | | | |
| Bill Breaker 7500 Crossing | 1 | 0.0 | 0 | | | | | | | |
| Bill Breaker 7400 Approaching | 11 | 0.5 | 0 | | | | | | | |
| Bill Breaker 7400 Crossing | 3 | 0.1 | 0 | | | | | | | |

## MGC 5m — 10/20 to 11/13 (22 days with alerts)

| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |
|---|---|---|---|---|---|---|---|---|---|---|
| Outside HTF ORB | 157 | 7.1 | 157 | 61 | +6.47 | +1015.6 | 64 | +3.75 | +589.0 | ✱ |
| Key Level Alert | 168 | 7.6 | 159 | 57 | +2.80 | +445.0 | 65 | +3.42 | +543.3 | ✱ |
| HTF EMA9 Pierce | 157 | 7.1 | 155 | 43 | +2.39 | +370.2 | 52 | +1.90 | +293.8 | ✱ |
| LTF EMA20 Pierce | 158 | 7.2 | 157 | 54 | +2.02 | +317.8 | 52 | +2.07 | +324.8 | ✱ |
| ORB Pass - | 83 | 3.8 | 83 | 49 | +4.75 | +393.9 | 55 | +2.76 | +228.9 | ✱ |
| High Confluence Setup | 194 | 8.8 | 194 | 36 | +0.82 | +159.8 | 48 | +1.71 | +331.6 |  |
| HTF EMA20 Pierce | 92 | 4.2 | 91 | 47 | +2.45 | +223.3 | 51 | +1.33 | +120.7 | ✱ |
| ORB Pass + | 43 | 2.0 | 43 | 70 | +4.54 | +195.1 | 63 | +3.22 | +138.5 | ✱ |
| Trade Setup | 75 | 3.4 | 75 | 37 | +1.39 | +104.6 | 41 | +0.40 | +30.0 |  |
| A+ Setup | 133 | 6.0 | 132 | 39 | +1.22 | +161.0 | 38 | -0.24 | -31.3 |  |
| VWAP Bounce - High R | 23 | 1.0 | 23 | 48 | +1.65 | +37.9 | 65 | +3.10 | +71.3 | ✱ |
| HTF | 137 | 6.2 | 136 | 44 | +0.09 | +11.7 | 44 | +0.12 | +16.2 |  |
| HTF Pullback Entry - Structure Confirmed | 4 | 0.2 | 4 | 25 | +2.27 | +9.1 | 25 | -2.33 | -9.3 |  |
| LTF EMA20 Touch - Pullback Entry | 49 | 2.2 | 49 | 31 | -2.02 | -98.9 | 24 | -1.68 | -82.6 |  |
| Price Enters HTF EMA9/20 Zone | 95 | 4.3 | 95 | 28 | -1.30 | -123.1 | 29 | -1.56 | -147.9 |  |
| HTF EMA20 Touch - Pullback Entry | 103 | 4.7 | 101 | 31 | -1.29 | -130.5 | 21 | -2.78 | -280.7 |  |
| VWAP Crossing | 26 | 1.2 | 0 | | | | | | | |
| EMA 200 Approaching | 37 | 1.7 | 0 | | | | | | | |
| EMA 20 Approaching | 241 | 11.0 | 0 | | | | | | | |
| YDL Approaching | 29 | 1.3 | 0 | | | | | | | |
| ORB High Crossing | 19 | 0.9 | 0 | | | | | | | |
| ORB Low Approaching | 52 | 2.4 | 0 | | | | | | | |
| Setup Ended | 84 | 3.8 | 0 | | | | | | | |
| ORB Flip - | 8 | 0.4 | 0 | | | | | | | |
| VWAP Approaching | 80 | 3.6 | 0 | | | | | | | |
| EMA 200 Crossing | 26 | 1.2 | 0 | | | | | | | |
| EMA 20 Crossing | 52 | 2.4 | 0 | | | | | | | |
| ORB High Approaching | 46 | 2.1 | 0 | | | | | | | |
| HTF EMA 200 Approaching | 3 | 0.1 | 0 | | | | | | | |
| Setup Confirmed | 32 | 1.5 | 0 | | | | | | | |
| ORB Low Crossing | 29 | 1.3 | 0 | | | | | | | |
| TP1 Partial | 39 | 1.8 | 0 | | | | | | | |
| HTF EMA 200 Crossing | 2 | 0.1 | 0 | | | | | | | |
| ORB Flip + | 5 | 0.2 | 0 | | | | | | | |
| Bill Breaker 4100 Approaching | 10 | 0.5 | 0 | | | | | | | |
| Bill Breaker 4000 Approaching | 11 | 0.5 | 0 | | | | | | | |
| YDL Crossing | 4 | 0.2 | 0 | | | | | | | |
| YDH Approaching | 15 | 0.7 | 0 | | | | | | | |
| Bill Breaker 4000 Crossing | 3 | 0.1 | 0 | | | | | | | |
| Bill Breaker 3900 Approaching | 5 | 0.2 | 0 | | | | | | | |
| YDH Crossing | 2 | 0.1 | 0 | | | | | | | |
| Bill Breaker 3900 Crossing | 4 | 0.2 | 0 | | | | | | | |

## Trade Setups drawn outside the alert sessions (replay, Jan–Oct, live gates, base exits)

CBC sends no alert outside Asia 18:00–22:30, London 03:00–07:45, NY 09:30–17:00 ET (⑤ Alerts session boxes). The chart still draws these setups.

| Chart | Window | Setups | Win % | Net | Avg | Net by third (3m/5m: Jan–Mar / Apr–Jun / Jul–Oct; 2m: Jun–Jul / Aug / Sep–Oct) |
|---|---|---|---|---|---|---|
| MES 3m | inside sessions | 1185 | 50% | +10 | +0.01 | +107 / -199 / +103 |
| MES 3m | 22:30–03:00 | 386 | 52% | +56 | +0.15 | +14 / +19 / +24 |
| MES 3m | 07:45–09:30 | 185 | 46% | -70 | -0.38 | +2 / -34 / -38 |
| MGC 3m | inside sessions | 820 | 50% | +217 | +0.26 | +56 / +62 / +99 |
| MGC 3m | 22:30–03:00 | 256 | 54% | +165 | +0.64 | +120 / +35 / +10 |
| MGC 3m | 07:45–09:30 | 123 | 46% | -61 | -0.49 | -14 / -95 / +48 |
| MES 2m | inside sessions | 870 | 47% | -218 | -0.25 | -135 / +43 / -126 |
| MES 2m | 22:30–03:00 | 287 | 53% | -16 | -0.05 | +50 / -2 / -64 |
| MES 2m | 07:45–09:30 | 123 | 50% | +4 | +0.03 | -19 / +39 / -17 |
| MGC 2m | inside sessions | 1074 | 51% | +171 | +0.16 | +112 / +92 / -33 |
| MGC 2m | 22:30–03:00 | 333 | 53% | +110 | +0.33 | -36 / +27 / +119 |
| MGC 2m | 07:45–09:30 | 165 | 53% | +79 | +0.48 | +7 / +11 / +61 |
| MES 5m | inside sessions | 837 | 54% | +197 | +0.24 | -125 / +149 / +173 |
| MES 5m | 22:30–03:00 | 239 | 46% | -46 | -0.19 | +10 / -19 / -37 |
| MES 5m | 07:45–09:30 | 132 | 45% | -133 | -1.00 | -31 / -35 / -66 |
| MGC 5m | inside sessions | 814 | 50% | -205 | -0.25 | -143 / +20 / -83 |
| MGC 5m | 22:30–03:00 | 243 | 50% | -43 | -0.18 | -30 / +22 / -35 |
| MGC 5m | 07:45–09:30 | 137 | 58% | +141 | +1.03 | +48 / +36 / +57 |
