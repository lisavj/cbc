# 5m chart EMA length check — weekly (run 3, manual Thursday run: 2026-11-12 11:37 ET)

## Since last run (run 2: 11/06, rerun on repaired data 11/07 09:57 ET)

This is a manual Thursday run (11/12), requested one day before the regular Friday run. It counts as weekly run 3. Bars 11/09–11/12 are new data since run 2. The Friday 11/13 run will **replace** this run as run 3; it will not add a run 4. Bars now run to 11/12, so the "Jul–Oct" third includes November. Settings sync (11/12 09:45 ET): no mismatches, so the study settings are current.

**MES 5m — standard 9 / 20 / 200: net +36 (run 2: −9)**
- N 16 / 34 / 120: +490, z 3.1, +200 / +136 / +154. Robust (run 2: +499, z 3.2). **Robust 3 consecutive weekly runs (10/31, 11/06, 11/12).** Still the best combo.
- I 16 / 34 / 200: +452, z 3.0, +199 / +116 / +136. Robust (run 2: +461, z 3.1). 3 runs.
- H 14 / 30 / 200: +372, z 2.6, +276 / +27 / +68. Robust (run 2: +389, z 2.7). 3 runs.
- L 20 / 40 / 200: +332, z 2.2, +183 / +108 / +42. Robust (run 2: +341, z 2.2). 3 runs.
- K 12 / 26 / 120: +292, z 2.1, +212 / +20 / +60. Robust (run 2: +296, z 2.2). 3 runs.
- F 12 / 26 / 200: +261, z 2.0 (just under 2), +208 / +6 / +47. Now **promising**, so its streak ended at 2. J 12 / 26 / 150: +263, z 2.0, promising (run 2: robust).
- M 24 / 50 / 200: +238, z 1.5, promising. D 9 / 20 / 120: +45, z 1.1, promising.
- Cooldown 6 bars: +100, z 2.0, +4 / +72 / +24. **Robust** again (run 2: promising, +91 / z 1.8), so it has 1 consecutive run. It is still −51 on MGC 5m.
- Live MES 5m LTF EMA20 Pierce (9 / 20): 47 setups (42 ended), −34.9, 45 % win. Last week it was 36 (33 ended), −34.5. The 9 new ended setups netted about −0.4, and the total is still net negative.

**MGC 5m — standard: net −105 (run 2: −117).** Nothing is robust or promising. J +128 (z 0.8), K +102 and F +100 are all negative in Jul–Nov. Live MGC 5m LTF EMA20 Pierce: 43 setups (37 ended), −42.3. Last week it was 26 (24 ended), −54.3.

**MES 3m — standard: net +13 (run 2: +26)**
- Q3 7 / 16 / 200: +157, z 0.9, −61 / +154 / +64. Noise (run 2: +203, z 1.2). Robust 0 runs.
- R3 6 / 14 / 200: +52, z 0.3. Noise (run 2: +119). Robust 0 runs. P3 8 / 18: +4. S3 5 / 12: −67.
- Last 4 weeks: Q3 −21.1 (run 2: +30.9), R3 −17.7 (+59.8), P3 −23.2, S3 −21.4. All faster lengths are now negative over the recent 4 weeks.
- Live MES 3m LTF EMA20 Pierce: 75 setups (68 ended), −20.4. Last week it was 72 (65 ended), −18.1.

**MES 2m — standard: net −202 (run 2: −186; LTF EMA20 Pierce 550 setups, −142)**
- U2 9 / 16 / 200: +220, z 1.9, +71 / −9 / +158. Still noise because Aug is −9 (run 2: +227, z 2.1). Robust 0 runs.
- W2 slow 28: +114, z 1.0. T2 slow 12: +93. V2 slow 24: +35. All are noise.
- Last 4 weeks: U2 +66.7 (run 2: +69.7), T2 +74.6, W2 +68.3, V2 −16.7.
- Live MES 2m LTF EMA20 Pierce: 87 setups (80 ended), −59.4, 42 % win. Last week it was 69 (65 ended), −71.0. The 15 new ended setups netted +11.6.

**Verdict**
- **MES 5m: UPDATE WARRANTED.** Set CBC v10.50 "Chart EMA fast / slow / 200" = **16 / 34 / 120** on the MES 5m chart only. This is an input change, not a Pine change. Afterwards, recreate the MES 5m TradingView alert.
  - (a) N 16 / 34 / 120 is robust on 3 consecutive weekly runs.
  - (b) Its neighbours I 16 / 34 / 200 (same fast / slow, other third EMA), H 14 / 30 and L 20 / 40 are also robust this run.
  - (c) Live MES 5m LTF EMA20 Pierce is net negative: −34.9 over 42 ended setups.
- **MGC 5m: keep 9 / 20 / 200.** There are no candidates.
- **MES 3m: keep 9 / 20 / 200.** Q3 and R3 weakened, and their last-4-weeks Δ turned negative.
- **MES 2m: keep 9 / 20 / 200.** U2 still needs Aug to turn positive. The weekly Setup Triggers check (untick LTF EMA20 Pierce on MES 2m) is the other path. Whichever qualifies first is preferred.
- **5m bar gates: no change.** Cooldown 6 is robust on only 1 consecutive run and is worse on MGC 5m.

---

# 5m chart EMA length + bar-gate study — 2026-11-12 11:37 ET (run 3, manual Thursday run)

5m chart EMA length study (CBC v10.50 "Chart EMA fast / slow / 200") -- 10/31/2026 (weekly check; candidate 12 / 26 / 200).

Question: on MES / MGC 5m charts, do other chart EMA lengths (e.g. 5 / 12 / 120 = the 3m 9 / 20 / 200 time span) beat the
standard 9 / 20 / 200? And are CBC's bar-count gates (setup cooldown 10 bars, ER(12), range gate 24 bars) right on 5m candles,
where each bar is 5 minutes instead of 3?
Data: server archive MES_5 / MGC_5 (Databento rebuild + BarFeed), Jan 5 - Oct 30. Chart EMAs recomputed from the 5m closes
(fast / slow / 200 per combo); HTF = 25m (CBC default 5x) with BarFeed's 25m CBC and EMA9/20, or 15m rebuilt from the 5m
candles (CBC rule: 15m close above the prior 15m high = long, below the prior low = short) with 15m EMA9/20.
Engine: chop_sim (triggers HTF CBC Flip, LTF EMA20 Pierce on the slow chart EMA, HTF EMA9 / EMA20 Pierce, 1-bar late confirm,
ER chop rule 0.23 with breakout exception, VWAP bounce block, opening-range windows). 5m live settings: range gate, VWAP stretch
and MTF gate OFF (per-symbol lists only cover 3m / 2m). BASE exits (SL1 1.7 ATR min 5, TP1 1.7 ATR capped 6, 80 % at TP1, BE,
trail 1.7 ATR; SL cap MGC 7 / MES 8). Not modelled: "price past both EMA clouds" gate, CBC's 5-bar LTF late window.
~50 % exact match with live setups on 3m: compare variants, not totals. z = change / (SD x sqrt(setups changed));
robust = z >= 2 and better in all three thirds (Jan-Mar / Apr-Jun / Jul-Oct); promising = z >= 1 and better in all three.
Usage: python3 ema5_study.py   (needs chop_sim.py + stretch_study.py next to it)

## MES 5m (61307 candles, 01/05 to 11/12)

**A. Chart EMA lengths (25m HTF = CBC default on 5m)**

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A 9 / 20 / 200 (standard) | 1204 | 51% | +36 | +0.03 | +0 | +0.0 | +0 / +0 / +0 | baseline |
| B 5 / 12 / 120 (3m time span) | 1476 | 53% | +73 | +0.05 | +37 | +0.2 | +81 / +22 / -67 | noise |
| C 5 / 12 / 200 (fast/slow only) | 1471 | 52% | +36 | +0.02 | -0 | -0.0 | +60 / +12 / -72 | worse |
| D 9 / 20 / 120 (200 only) | 1217 | 52% | +81 | +0.07 | +45 | +1.1 | +6 / +16 / +23 | promising |
| E 7 / 15 / 150 (midway) | 1366 | 53% | +56 | +0.04 | +20 | +0.1 | +122 / -52 / -50 | noise |
| F 12 / 26 / 200 (slower) | 1074 | 53% | +297 | +0.28 | +261 | +2.0 | +208 / +6 / +47 | promising |
| G 10 / 24 / 200 (around F) | 1112 | 53% | +231 | +0.21 | +195 | +1.6 | +174 / -1 / +22 | noise |
| H 14 / 30 / 200 (around F) | 1023 | 54% | +408 | +0.40 | +372 | +2.6 | +276 / +27 / +68 | robust |
| I 16 / 34 / 200 (around F) | 983 | 56% | +488 | +0.50 | +452 | +3.0 | +199 / +116 / +136 | robust |
| J 12 / 26 / 150 (F + EMA 150) | 1082 | 53% | +299 | +0.28 | +263 | +2.0 | +209 / +12 / +41 | promising |
| K 12 / 26 / 120 (F + EMA 120) | 1089 | 54% | +328 | +0.30 | +292 | +2.1 | +212 / +20 / +60 | robust |
| L 20 / 40 / 200 (beyond I) | 932 | 55% | +368 | +0.40 | +332 | +2.2 | +183 / +108 / +42 | robust |
| M 24 / 50 / 200 (beyond I) | 888 | 54% | +274 | +0.31 | +238 | +1.5 | +172 / +60 / +6 | promising |
| N 16 / 34 / 120 (I + EMA 120) | 1001 | 56% | +526 | +0.53 | +490 | +3.1 | +200 / +136 / +154 | robust |
| Reference: standard EMAs, LTF EMA20 Pierce trigger OFF | 835 | 53% | +159 | +0.19 | +123 | +0.9 | +126 / +14 / -17 | noise |

By trigger (setups / net): A: Flip 317 / -34 · LTF20 588 / -61 · HTF9 190 / +65 · HTF20 109 / +66; B: Flip 380 / -52 · LTF20 813 / -33 · HTF9 186 / +80 · HTF20 97 / +78; C: Flip 346 / -63 · LTF20 834 / -64 · HTF9 190 / +99 · HTF20 101 / +64; D: Flip 349 / -9 · LTF20 574 / -42 · HTF9 186 / +64 · HTF20 108 / +68; E: Flip 349 / -37 · LTF20 734 / -31 · HTF9 177 / +97 · HTF20 106 / +26; F: Flip 298 / -28 · LTF20 463 / +141 · HTF9 194 / +98 · HTF20 119 / +86; G: Flip 305 / -35 · LTF20 500 / +81 · HTF9 190 / +101 · HTF20 117 / +84; H: Flip 288 / -37 · LTF20 435 / +322 · HTF9 176 / +61 · HTF20 124 / +62; I: Flip 281 / -27 · LTF20 398 / +291 · HTF9 179 / +151 · HTF20 125 / +72; J: Flip 318 / -20 · LTF20 455 / +138 · HTF9 191 / +92 · HTF20 118 / +88; K: Flip 330 / -3 · LTF20 453 / +139 · HTF9 190 / +98 · HTF20 116 / +94; L: Flip 267 / +2 · LTF20 373 / +129 · HTF9 168 / +161 · HTF20 124 / +77; M: Flip 244 / -30 · LTF20 304 / +124 · HTF9 220 / +120 · HTF20 120 / +60; N: Flip 313 / -3 · LTF20 389 / +295 · HTF9 177 / +153 · HTF20 122 / +81

**B. 15m HTF instead of 25m (⑪ HTF Timeframe = 15)** — compared with A (standard, 25m HTF)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 15m HTF + A 9 / 20 / 200 | 1222 | 48% | +48 | +0.04 | +12 | +0.1 | +241 / -115 / -113 | noise |
| 15m HTF + B 5 / 12 / 120 | 1624 | 49% | -13 | -0.01 | -49 | -0.2 | +227 / -175 / -101 | worse |

By trigger: 15m A: Flip 325 / +212 · LTF20 635 / -6 · HTF9 150 / -161 · HTF20 112 / +3; 15m B: Flip 382 / +198 · LTF20 958 / -103 · HTF9 185 / -115 · HTF20 99 / +7

**C. Bar-count gates on 5m candles** (standard EMAs, 25m HTF). On 3m: cooldown 10 bars = 30 min, ER(12) = 36 min, range gate 24 bars = 72 min. Time-matched on 5m: cooldown 6, ER(8) (40 min; ER(6) = 30 min), range 14 bars.

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| Cooldown 6 bars (30 min) | 1253 | 52% | +136 | +0.11 | +100 | +2.0 | +4 / +72 / +24 | robust |
| Cooldown 4 bars | 1269 | 52% | +134 | +0.11 | +98 | +1.8 | -24 / +69 / +54 | noise |
| Cooldown 15 bars | 1146 | 51% | +29 | +0.03 | -7 | -0.1 | +15 / -28 / +5 | worse |
| ER(8) (40 min) | 1423 | 53% | +156 | +0.11 | +120 | +0.6 | +86 / +28 / +5 | noise |
| ER(6) (30 min) | 1510 | 53% | +246 | +0.16 | +210 | +1.1 | +225 / -50 / +35 | noise |
| ER(16) (80 min) | 1071 | 52% | +60 | +0.06 | +24 | +0.1 | +150 / -101 / -25 | noise |
| Cooldown 6 + ER(8) (all time-matched) | 1494 | 52% | +167 | +0.11 | +131 | +0.7 | +53 / +92 / -14 | noise |
| Range gate ON, 24 bars / 5 ATR (as 3m, = 120 min) | 1018 | 50% | +46 | +0.04 | +10 | +0.1 | +56 / -38 / -8 | noise |
| Range gate ON, 14 bars / 5 ATR (72 min) | 952 | 50% | -42 | -0.04 | -78 | -0.6 | -48 / -79 / +49 | worse |
| Range gate ON, 14 bars / 4 ATR | 1026 | 50% | -29 | -0.03 | -65 | -0.6 | -17 / -55 / +7 | worse |

**D. Bar-count gates with 5 / 12 / 120** (compared with A standard)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| B 5 / 12 / 120, standard gates | 1476 | 53% | +73 | +0.05 | +37 | +0.2 | +81 / +22 / -67 | noise |
| ER(8) (40 min) | 1603 | 54% | +225 | +0.14 | +189 | +0.8 | +58 / +117 / +14 | noise |
| Cooldown 6 + ER(8) (all time-matched) | 1688 | 53% | +121 | +0.07 | +85 | +0.4 | +31 / +77 / -22 | noise |
| Range gate ON, 14 bars / 5 ATR (72 min) | 1192 | 52% | +26 | +0.02 | -10 | -0.0 | -35 / -16 / +41 | worse |

## MGC 5m (61175 candles, 01/05 to 11/12)

**A. Chart EMA lengths (25m HTF = CBC default on 5m)**

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A 9 / 20 / 200 (standard) | 1190 | 51% | -105 | -0.09 | +0 | +0.0 | +0 / +0 / +0 | baseline |
| B 5 / 12 / 120 (3m time span) | 1489 | 51% | -226 | -0.15 | -121 | -0.6 | -67 / -87 / +32 | worse |
| C 5 / 12 / 200 (fast/slow only) | 1477 | 51% | -218 | -0.15 | -114 | -0.6 | -41 / -94 / +21 | worse |
| D 9 / 20 / 120 (200 only) | 1203 | 51% | -84 | -0.07 | +21 | +0.5 | -12 / +22 / +11 | noise |
| E 7 / 15 / 150 (midway) | 1369 | 51% | -139 | -0.10 | -35 | -0.2 | -35 / -65 / +65 | worse |
| F 12 / 26 / 200 (slower) | 1064 | 51% | -5 | -0.00 | +100 | +0.7 | +40 / +105 / -46 | noise |
| G 10 / 24 / 200 (around F) | 1092 | 51% | -117 | -0.11 | -12 | -0.1 | -39 / +107 / -81 | worse |
| H 14 / 30 / 200 (around F) | 1003 | 50% | -83 | -0.08 | +22 | +0.1 | +58 / +35 / -72 | noise |
| I 16 / 34 / 200 (around F) | 945 | 50% | -54 | -0.06 | +50 | +0.3 | +136 / +19 / -104 | noise |
| J 12 / 26 / 150 (F + EMA 150) | 1074 | 51% | +23 | +0.02 | +128 | +0.8 | +52 / +118 / -43 | noise |
| K 12 / 26 / 120 (F + EMA 120) | 1080 | 51% | -3 | -0.00 | +102 | +0.7 | +28 / +137 / -63 | noise |
| L 20 / 40 / 200 (beyond I) | 887 | 50% | -101 | -0.11 | +4 | +0.0 | +84 / +31 / -111 | noise |
| M 24 / 50 / 200 (beyond I) | 860 | 50% | -158 | -0.18 | -54 | -0.3 | -41 / +62 / -75 | worse |
| N 16 / 34 / 120 (I + EMA 120) | 962 | 50% | -73 | -0.08 | +32 | +0.2 | +119 / +47 / -134 | noise |
| Reference: standard EMAs, LTF EMA20 Pierce trigger OFF | 823 | 51% | -28 | -0.03 | +76 | +0.5 | +44 / +90 / -57 | noise |

By trigger (setups / net): A: Flip 324 / +73 · LTF20 578 / -70 · HTF9 176 / -85 · HTF20 112 / -23; B: Flip 372 / +66 · LTF20 818 / -176 · HTF9 191 / -83 · HTF20 108 / -34; C: Flip 344 / +60 · LTF20 832 / -146 · HTF9 191 / -97 · HTF20 110 / -35; D: Flip 352 / +79 · LTF20 566 / -65 · HTF9 178 / -73 · HTF20 107 / -25; E: Flip 346 / +121 · LTF20 732 / -177 · HTF9 180 / -49 · HTF20 111 / -34; F: Flip 300 / +106 · LTF20 459 / -14 · HTF9 176 / -63 · HTF20 129 / -34; G: Flip 308 / +62 · LTF20 484 / -110 · HTF9 178 / -39 · HTF20 122 / -30; H: Flip 287 / +112 · LTF20 384 / -94 · HTF9 195 / -60 · HTF20 137 / -41; I: Flip 276 / +92 · LTF20 360 / +22 · HTF9 175 / -142 · HTF20 134 / -27; J: Flip 313 / +127 · LTF20 456 / -18 · HTF9 177 / -59 · HTF20 128 / -28; K: Flip 327 / +108 · LTF20 452 / -27 · HTF9 177 / -59 · HTF20 124 / -24; L: Flip 263 / +60 · LTF20 317 / -48 · HTF9 170 / -82 · HTF20 137 / -31; M: Flip 244 / +54 · LTF20 287 / -146 · HTF9 195 / -45 · HTF20 134 / -21; N: Flip 303 / +94 · LTF20 358 / +1 · HTF9 174 / -147 · HTF20 127 / -21

**B. 15m HTF instead of 25m (⑪ HTF Timeframe = 15)** — compared with A (standard, 25m HTF)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 15m HTF + A 9 / 20 / 200 | 1267 | 48% | -120 | -0.09 | -15 | -0.1 | +74 / -170 / +80 | worse |
| 15m HTF + B 5 / 12 / 120 | 1672 | 49% | +14 | +0.01 | +119 | +0.4 | +128 / -240 / +231 | noise |

By trigger: 15m A: Flip 355 / -18 · LTF20 604 / +11 · HTF9 181 / -72 · HTF20 127 / -42; 15m B: Flip 405 / +1 · LTF20 963 / +133 · HTF9 198 / -91 · HTF20 106 / -29

**C. Bar-count gates on 5m candles** (standard EMAs, 25m HTF). On 3m: cooldown 10 bars = 30 min, ER(12) = 36 min, range gate 24 bars = 72 min. Time-matched on 5m: cooldown 6, ER(8) (40 min; ER(6) = 30 min), range 14 bars.

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| Cooldown 6 bars (30 min) | 1260 | 51% | -156 | -0.12 | -51 | -0.8 | -114 / +63 / -0 | worse |
| Cooldown 4 bars | 1290 | 51% | -123 | -0.10 | -19 | -0.2 | -110 / +73 / +18 | worse |
| Cooldown 15 bars | 1128 | 51% | -89 | -0.08 | +16 | +0.3 | -25 / +21 / +21 | noise |
| ER(8) (40 min) | 1455 | 51% | -215 | -0.15 | -110 | -0.5 | -36 / -52 / -21 | worse |
| ER(6) (30 min) | 1570 | 51% | -114 | -0.07 | -9 | -0.0 | +14 / +26 / -48 | worse |
| ER(16) (80 min) | 1040 | 50% | -107 | -0.10 | -2 | -0.0 | +134 / +65 / -201 | worse |
| Cooldown 6 + ER(8) (all time-matched) | 1547 | 50% | -266 | -0.17 | -161 | -0.8 | -124 / +13 / -50 | worse |
| Range gate ON, 24 bars / 5 ATR (as 3m, = 120 min) | 1032 | 51% | -46 | -0.04 | +58 | +0.5 | -89 / +43 / +104 | noise |
| Range gate ON, 14 bars / 5 ATR (72 min) | 960 | 49% | -207 | -0.22 | -102 | -0.7 | -79 / -18 / -4 | worse |
| Range gate ON, 14 bars / 4 ATR | 1031 | 50% | -217 | -0.21 | -112 | -0.9 | -73 / -29 / -10 | worse |

**D. Bar-count gates with 5 / 12 / 120** (compared with A standard)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| B 5 / 12 / 120, standard gates | 1489 | 51% | -226 | -0.15 | -121 | -0.6 | -67 / -87 / +32 | worse |
| ER(8) (40 min) | 1666 | 51% | -156 | -0.09 | -52 | -0.2 | -34 / -41 / +23 | worse |
| Cooldown 6 + ER(8) (all time-matched) | 1790 | 51% | -229 | -0.13 | -124 | -0.5 | -104 / -62 / +42 | worse |
| Range gate ON, 14 bars / 5 ATR (72 min) | 1216 | 50% | -159 | -0.13 | -54 | -0.2 | +8 / -65 / +4 | worse |

## MES 3m (102179 candles) — watch: slow EMA 16 / 14 (range gate on, base exits)

Only the SLOW length changes the replay (the fast EMA feeds only the cloud / "price past both EMA clouds" gate, not modelled).

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A3 9 / 20 / 200 (standard) | 1752 | 50% | +13 | +0.01 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 318 / +49 · LTF20 962 / +120 · HTF9 290 / -155 · HTF20 182 / -0
| P3 8 / 18 / 200 | 1843 | 51% | +18 | +0.01 | +4 | +0.0 | -38 / +26 / +17 | noise | Flip 323 / +59 · LTF20 1045 / +148 · HTF9 293 / -202 · HTF20 182 / +13
| Q3 7 / 16 / 200 | 1896 | 51% | +171 | +0.09 | +157 | +0.9 | -61 / +154 / +64 | noise | Flip 329 / +59 · LTF20 1081 / +232 · HTF9 305 / -145 · HTF20 181 / +25
| R3 6 / 14 / 200 | 1990 | 51% | +66 | +0.03 | +52 | +0.3 | -69 / +70 / +52 | noise | Flip 332 / +63 · LTF20 1186 / +165 · HTF9 295 / -173 · HTF20 177 / +11
| S3 5 / 12 / 200 | 2085 | 51% | -54 | -0.03 | -67 | -0.3 | -115 / +37 / +11 | worse | Flip 335 / +57 · LTF20 1291 / +95 · HTF9 294 / -206 · HTF20 165 / -0

Last 4 weeks of the replay, Δ net vs standard (live-period check; the extra shallow pierces a faster slow EMA adds cannot be seen in the live alerts): P3 -23.2 · Q3 -21.1 · R3 -17.7 · S3 -21.4

## MES 2m (81410 candles, Jun–Oct) — watch: slow EMA 16 (1H MTF gate + HTF flips >= 4, base exits)

Only the SLOW length changes the replay. Thirds = Jun–Jul / Aug / Sep–Oct.

| Variant | Setups | Net | Δ vs standard | z | Δ by third | Verdict | LTF EMA20 Pierce setups / net |
|---|---|---|---|---|---|---|---|
| A2 9 / 20 / 200 (standard) | 1218 | -202 | +0 | +0.0 | +0 / +0 / +0 | baseline | 550 / -142 |
| T2 9 / 12 / 200 | 1383 | -109 | +93 | +0.7 | +37 / -2 / +58 | noise | 708 / -17 |
| U2 9 / 16 / 200 | 1308 | +18 | +220 | +1.9 | +71 / -9 / +158 | noise | 632 / +119 |
| V2 9 / 24 / 200 | 1139 | -167 | +35 | +0.3 | -13 / +23 / +25 | noise | 472 / -53 |
| W2 9 / 28 / 200 | 1057 | -88 | +114 | +1.0 | -36 / +19 / +132 | noise | 401 / +29 |

Last 4 weeks of the replay, Δ net vs standard: T2 +74.6 · U2 +66.7 · V2 -16.7 · W2 +68.3

## Candidates (robust / promising)

- MES 5m: D 9 / 20 / 120 (200 only) → Δ +45, z +1.1, thirds +6 / +16 / +23 (promising)
- MES 5m: F 12 / 26 / 200 (slower) → Δ +261, z +2.0, thirds +208 / +6 / +47 (promising)
- MES 5m: H 14 / 30 / 200 (around F) → Δ +372, z +2.6, thirds +276 / +27 / +68 (robust)
- MES 5m: I 16 / 34 / 200 (around F) → Δ +452, z +3.0, thirds +199 / +116 / +136 (robust)
- MES 5m: J 12 / 26 / 150 (F + EMA 150) → Δ +263, z +2.0, thirds +209 / +12 / +41 (promising)
- MES 5m: K 12 / 26 / 120 (F + EMA 120) → Δ +292, z +2.1, thirds +212 / +20 / +60 (robust)
- MES 5m: L 20 / 40 / 200 (beyond I) → Δ +332, z +2.2, thirds +183 / +108 / +42 (robust)
- MES 5m: M 24 / 50 / 200 (beyond I) → Δ +238, z +1.5, thirds +172 / +60 / +6 (promising)
- MES 5m: N 16 / 34 / 120 (I + EMA 120) → Δ +490, z +3.1, thirds +200 / +136 / +154 (robust)
- MES 5m: Cooldown 6 bars (30 min) → Δ +100, z +2.0, thirds +4 / +72 / +24 (robust)
## Live setups (alert store, current CBC chart EMAs 9 / 20 / 200) by trigger: MES / MGC 5m and MES 3m

| Chart | Trigger | Setups | Ended | Win % | Net | Avg |
|---|---|---|---|---|---|---|
| MES 2m | HTF CBC Flip | 40 | 37 | 51% | -6.2 | -0.17 |
| MES 2m | HTF EMA20 Pierce | 13 | 12 | 33% | -8.5 | -0.71 |
| MES 2m | HTF EMA9 Pierce | 10 | 9 | 50% | -1.2 | -0.14 |
| MES 2m | HTF Pullback Structure | 2 | 2 | 50% | -3.2 | -1.60 |
| MES 2m | LTF EMA20 Pierce | 87 | 80 | 42% | -59.4 | -0.74 |
| MES 3m | HTF CBC Flip | 18 | 16 | 56% | +23.0 | +1.44 |
| MES 3m | HTF EMA20 Pierce | 10 | 8 | 38% | -5.1 | -0.63 |
| MES 3m | HTF EMA9 Pierce | 15 | 14 | 43% | +4.8 | +0.34 |
| MES 3m | HTF Pullback Structure | 2 | 2 | 0% | -9.1 | -4.54 |
| MES 3m | LTF EMA20 Pierce | 75 | 68 | 49% | -20.4 | -0.30 |
| MES 5m | HTF CBC Flip | 17 | 15 | 67% | +11.0 | +0.74 |
| MES 5m | HTF EMA20 Pierce | 9 | 8 | 62% | +4.9 | +0.61 |
| MES 5m | HTF EMA9 Pierce | 4 | 2 | 0% | -13.5 | -6.75 |
| MES 5m | HTF Pullback Structure | 1 | 1 | 0% | -5.8 | -5.75 |
| MES 5m | LTF EMA20 Pierce | 47 | 42 | 45% | -34.9 | -0.83 |
| MGC 5m | HTF CBC Flip | 17 | 17 | 59% | +5.8 | +0.34 |
| MGC 5m | HTF EMA20 Pierce | 9 | 8 | 50% | +2.1 | +0.26 |
| MGC 5m | HTF EMA9 Pierce | 13 | 11 | 73% | +32.7 | +2.97 |
| MGC 5m | LTF EMA20 Pierce | 43 | 37 | 38% | -42.3 | -1.14 |

