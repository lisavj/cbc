# 5m chart EMA length check — weekly (run 3, Friday run: 2026-11-13 18:47 ET)

## Since last run (compared with the 11/12 manual Thursday run, which this Friday run replaces as weekly run 3)

**STUDY SETTINGS STALE:** settings sync 11/13 16:47 ET lists 3 MISMATCHes from v10.95–v10.96 — MES 3m now 100 % at TP1 all day (mes3_ema_grid `LIVE` and chop_sim `EXIT[('MES',3)]` still use the 80 / 100 % time-of-day rule) and MGC 3m now FLIP 0 % / no trail (chop_sim `EXIT[('MGC',3)]` still 50 % / trail 3.5). This study replays every chart with BASE exits (stretch_study `QB`) and does not read those constants, so its numbers are not affected; run anyway as instructed.

Bars now run to 11/13 (the "Jul–Oct" third includes November). Live numbers: the alert store still holds the 11/08–11/12 duplicate MGC 5m alerts (`/health` lastDedupe = null). A de-duplicated recount (same chart + Time + alert names within 60 s = one) changes only MGC 5m; it is shown next to the script's raw figure.

**MES 5m — standard 9 / 20 / 200: net +18 (11/12: +36)**
- N 16 / 34 / 120: +504, z 3.2, +200 / +136 / +168. Robust (11/12: +490, z 3.1). **Robust 3 consecutive weekly runs (10/31, 11/06, 11/13).** Still the best combo.
- I 16 / 34 / 200: +466, z 3.1, +199 / +116 / +151. Robust (11/12: +452, z 3.0). 3 runs.
- H 14 / 30 / 200: +378, z 2.6, +276 / +27 / +75. Robust (+372, z 2.6). 3 runs.
- L 20 / 40 / 200: +334, z 2.2, +183 / +108 / +43. Robust (+332, z 2.2). 3 runs.
- K 12 / 26 / 120: +306, z 2.2, +212 / +20 / +74. Robust (+292, z 2.1). 3 runs.
- F 12 / 26 / 200: +276, z 2.1, +208 / +6 / +62. Robust again (11/12: promising at z 2.0). Because this run replaces the 11/12 run, F is **robust 3 consecutive runs** (10/31, 11/06, 11/13).
- J 12 / 26 / 150: +277, z 2.1, robust (11/12: promising). Robust on 11/06 and 11/13 → 2 runs.
- M 24 / 50 / 200: +252, z 1.6, promising. D 9 / 20 / 120: +45, z 1.1, promising. G 10 / 24: +210, z 1.7, noise (Apr–Jun −1).
- Cooldown 6 bars: +100, z 2.0, +4 / +72 / +24. Robust (11/12: robust, same numbers). It was promising on 11/06, so its streak is **1 consecutive run** (11/13). Still −51 on MGC 5m.
- Live MES 5m LTF EMA20 Pierce (9 / 20): 49 setups (44 ended), −19.8, 48 % win (11/12: 47 / 42 ended, −34.9). The 2 new ended setups netted +15.1; the total is still net negative over ≥ 20 ended.

**MGC 5m — standard: net −107 (11/12: −105).** Nothing robust or promising. J +122 (z 0.8), K +96, F +93 — all negative in Jul–Nov. Live MGC 5m LTF EMA20 Pierce: raw 45 setups (39 ended) −55.2; de-duplicated 38 (34 ended) −60.0, 32 % win (11/12 raw: 43 / 37 ended, −42.3).

**MES 3m — standard: net +7 (11/12: +13)**
- Q3 7 / 16 / 200: +152, z 0.9, −61 / +154 / +59. Noise (11/12: +157, z 0.9). Robust 0 runs.
- R3 6 / 14 / 200: +54, z 0.3. Noise (+52). Robust 0 runs. P3 8 / 18: −12. S3 5 / 12: −71.
- Last 4 weeks: Q3 −36.5 (11/12: −21.1), R3 −35.7 (−17.7), P3 −57.5, S3 −40.7. Faster lengths are getting worse in the recent window.
- Live MES 3m LTF EMA20 Pierce: 76 setups (69 ended), −36.8 (11/12: 75 / 68 ended, −20.4).

**MES 2m — standard: net −217 (11/12: −202; replay LTF EMA20 Pierce 552 setups, −155)**
- U2 9 / 16 / 200: +221, z 1.9, +71 / −9 / +159. Still noise because Aug is −9 (11/12: +220, z 1.9). Robust 0 runs.
- W2 slow 28: +125, z 1.1. T2 slow 12: +87. V2 slow 24: +51. All noise.
- Last 4 weeks: U2 +68.6 (11/12: +66.7), T2 +70.6, W2 +85.4, V2 +9.6.
- Live MES 2m LTF EMA20 Pierce: 93 setups (86 ended), −76.5, 42 % win (11/12: 87 / 80 ended, −59.4). The 6 new ended setups netted −17.1.

**Verdict**
- **MES 5m: UPDATE WARRANTED (confirmed by the Friday run).** Set CBC v10.50 "Chart EMA fast / slow / 200" = **16 / 34 / 120** on the MES 5m chart only. This is an input change, not a Pine change. Afterwards, recreate the MES 5m TradingView alert. (If you already made this change after the 11/12 run, nothing more to do; future live MES 5m LTF numbers will then be on 16 / 34.)
  - (a) N 16 / 34 / 120 is robust on 3 consecutive weekly runs (10/31, 11/06, 11/13).
  - (b) Neighbours I 16 / 34 / 200 (same fast / slow, other third EMA), H 14 / 30 and L 20 / 40 are also robust this run.
  - (c) Live MES 5m LTF EMA20 Pierce (9 / 20) is net negative: −19.8 over 44 ended setups.
- **MGC 5m: keep 9 / 20 / 200.** No candidates.
- **MES 3m: keep 9 / 20 / 200.** Q3 / R3 stay noise and their last-4-weeks Δ fell further below zero.
- **MES 2m: keep 9 / 20 / 200.** U2 still needs Aug to turn positive (z 1.9). The weekly Setup Triggers check (untick LTF EMA20 Pierce on MES 2m) is the other path — live MES 2m LTF EMA20 Pierce keeps losing (−76.5 over 86 ended); whichever qualifies first is preferred.
- **5m bar gates: no change.** Cooldown 6 is robust on only 1 consecutive run and is worse on MGC 5m (a cooldown change for 5m would need a CBC Pine change).

---

# 5m chart EMA length + bar-gate study — 2026-11-13 18:47 ET (run 3, Friday run)

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

## MES 5m (61647 candles, 01/05 to 11/13)

**A. Chart EMA lengths (25m HTF = CBC default on 5m)**

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A 9 / 20 / 200 (standard) | 1208 | 51% | +18 | +0.02 | +0 | +0.0 | +0 / +0 / +0 | baseline |
| B 5 / 12 / 120 (3m time span) | 1481 | 53% | +48 | +0.03 | +29 | +0.2 | +81 / +22 / -74 | noise |
| C 5 / 12 / 200 (fast/slow only) | 1476 | 52% | +11 | +0.01 | -8 | -0.0 | +60 / +12 / -79 | worse |
| D 9 / 20 / 120 (200 only) | 1221 | 52% | +63 | +0.05 | +45 | +1.1 | +6 / +16 / +23 | promising |
| E 7 / 15 / 150 (midway) | 1370 | 52% | +39 | +0.03 | +20 | +0.1 | +122 / -52 / -50 | noise |
| F 12 / 26 / 200 (slower) | 1076 | 53% | +294 | +0.27 | +276 | +2.1 | +208 / +6 / +62 | robust |
| G 10 / 24 / 200 (around F) | 1114 | 53% | +228 | +0.20 | +210 | +1.7 | +174 / -1 / +37 | noise |
| H 14 / 30 / 200 (around F) | 1026 | 54% | +397 | +0.39 | +378 | +2.6 | +276 / +27 / +75 | robust |
| I 16 / 34 / 200 (around F) | 985 | 56% | +484 | +0.49 | +466 | +3.1 | +199 / +116 / +151 | robust |
| J 12 / 26 / 150 (F + EMA 150) | 1084 | 53% | +295 | +0.27 | +277 | +2.1 | +209 / +12 / +55 | robust |
| K 12 / 26 / 120 (F + EMA 120) | 1091 | 53% | +325 | +0.30 | +306 | +2.2 | +212 / +20 / +74 | robust |
| L 20 / 40 / 200 (beyond I) | 934 | 55% | +352 | +0.38 | +334 | +2.2 | +183 / +108 / +43 | robust |
| M 24 / 50 / 200 (beyond I) | 890 | 54% | +270 | +0.30 | +252 | +1.6 | +172 / +60 / +20 | promising |
| N 16 / 34 / 120 (I + EMA 120) | 1003 | 56% | +522 | +0.52 | +504 | +3.2 | +200 / +136 / +168 | robust |
| Reference: standard EMAs, LTF EMA20 Pierce trigger OFF | 837 | 53% | +156 | +0.19 | +137 | +1.0 | +126 / +14 / -3 | noise |

By trigger (setups / net): A: Flip 317 / -34 · LTF20 591 / -83 · HTF9 191 / +70 · HTF20 109 / +66; B: Flip 381 / -60 · LTF20 816 / -55 · HTF9 187 / +84 · HTF20 97 / +78; C: Flip 347 / -71 · LTF20 837 / -85 · HTF9 191 / +103 · HTF20 101 / +64; D: Flip 349 / -9 · LTF20 577 / -64 · HTF9 187 / +69 · HTF20 108 / +68; E: Flip 350 / -45 · LTF20 736 / -45 · HTF9 178 / +102 · HTF20 106 / +26; F: Flip 298 / -28 · LTF20 465 / +138 · HTF9 194 / +98 · HTF20 119 / +86; G: Flip 305 / -35 · LTF20 501 / +73 · HTF9 191 / +106 · HTF20 117 / +84; H: Flip 288 / -37 · LTF20 438 / +311 · HTF9 176 / +61 · HTF20 124 / +62; I: Flip 281 / -27 · LTF20 400 / +288 · HTF9 179 / +151 · HTF20 125 / +72; J: Flip 318 / -20 · LTF20 457 / +135 · HTF9 191 / +92 · HTF20 118 / +88; K: Flip 330 / -3 · LTF20 455 / +136 · HTF9 190 / +98 · HTF20 116 / +94; L: Flip 267 / +2 · LTF20 375 / +113 · HTF9 168 / +161 · HTF20 124 / +77; M: Flip 244 / -30 · LTF20 305 / +116 · HTF9 221 / +125 · HTF20 120 / +60; N: Flip 313 / -3 · LTF20 391 / +292 · HTF9 177 / +153 · HTF20 122 / +81

**B. 15m HTF instead of 25m (⑪ HTF Timeframe = 15)** — compared with A (standard, 25m HTF)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 15m HTF + A 9 / 20 / 200 | 1225 | 48% | +31 | +0.03 | +13 | +0.1 | +241 / -115 / -113 | noise |
| 15m HTF + B 5 / 12 / 120 | 1627 | 49% | -41 | -0.03 | -60 | -0.2 | +227 / -175 / -112 | worse |

By trigger: 15m A: Flip 325 / +212 · LTF20 638 / -24 · HTF9 150 / -161 · HTF20 112 / +3; 15m B: Flip 382 / +198 · LTF20 961 / -132 · HTF9 185 / -115 · HTF20 99 / +7

**C. Bar-count gates on 5m candles** (standard EMAs, 25m HTF). On 3m: cooldown 10 bars = 30 min, ER(12) = 36 min, range gate 24 bars = 72 min. Time-matched on 5m: cooldown 6, ER(8) (40 min; ER(6) = 30 min), range 14 bars.

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| Cooldown 6 bars (30 min) | 1257 | 52% | +119 | +0.09 | +100 | +2.0 | +4 / +72 / +24 | robust |
| Cooldown 4 bars | 1273 | 52% | +117 | +0.09 | +98 | +1.7 | -24 / +69 / +54 | noise |
| Cooldown 15 bars | 1149 | 51% | +19 | +0.02 | +1 | +0.0 | +15 / -28 / +13 | noise |
| ER(8) (40 min) | 1427 | 52% | +139 | +0.10 | +121 | +0.6 | +86 / +28 / +6 | noise |
| ER(6) (30 min) | 1516 | 53% | +252 | +0.17 | +233 | +1.2 | +225 / -50 / +59 | noise |
| ER(16) (80 min) | 1074 | 52% | +38 | +0.04 | +19 | +0.1 | +150 / -101 / -30 | noise |
| Cooldown 6 + ER(8) (all time-matched) | 1498 | 52% | +151 | +0.10 | +132 | +0.7 | +53 / +92 / -13 | noise |
| Range gate ON, 24 bars / 5 ATR (as 3m, = 120 min) | 1022 | 50% | +28 | +0.03 | +10 | +0.1 | +56 / -38 / -8 | noise |
| Range gate ON, 14 bars / 5 ATR (72 min) | 956 | 50% | -59 | -0.06 | -78 | -0.6 | -48 / -79 / +49 | worse |
| Range gate ON, 14 bars / 4 ATR | 1030 | 50% | -47 | -0.05 | -65 | -0.6 | -17 / -55 / +7 | worse |

**D. Bar-count gates with 5 / 12 / 120** (compared with A standard)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| B 5 / 12 / 120, standard gates | 1481 | 53% | +48 | +0.03 | +29 | +0.2 | +81 / +22 / -74 | noise |
| ER(8) (40 min) | 1607 | 54% | +195 | +0.12 | +177 | +0.8 | +58 / +117 / +3 | noise |
| Cooldown 6 + ER(8) (all time-matched) | 1693 | 53% | +98 | +0.06 | +79 | +0.3 | +31 / +77 / -28 | noise |
| Range gate ON, 14 bars / 5 ATR (72 min) | 1197 | 52% | +0 | +0.00 | -18 | -0.1 | -35 / -16 / +33 | worse |

## MGC 5m (61515 candles, 01/05 to 11/13)

**A. Chart EMA lengths (25m HTF = CBC default on 5m)**

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A 9 / 20 / 200 (standard) | 1194 | 51% | -107 | -0.09 | +0 | +0.0 | +0 / +0 / +0 | baseline |
| B 5 / 12 / 120 (3m time span) | 1496 | 51% | -238 | -0.16 | -130 | -0.6 | -67 / -87 / +23 | worse |
| C 5 / 12 / 200 (fast/slow only) | 1484 | 51% | -230 | -0.15 | -123 | -0.6 | -41 / -94 / +12 | worse |
| D 9 / 20 / 120 (200 only) | 1207 | 51% | -86 | -0.07 | +21 | +0.5 | -12 / +22 / +11 | noise |
| E 7 / 15 / 150 (midway) | 1375 | 51% | -156 | -0.11 | -49 | -0.3 | -35 / -65 / +51 | worse |
| F 12 / 26 / 200 (slower) | 1071 | 51% | -14 | -0.01 | +93 | +0.6 | +40 / +105 / -52 | noise |
| G 10 / 24 / 200 (around F) | 1098 | 51% | -119 | -0.11 | -12 | -0.1 | -39 / +107 / -80 | worse |
| H 14 / 30 / 200 (around F) | 1009 | 50% | -96 | -0.10 | +11 | +0.1 | +58 / +35 / -83 | noise |
| I 16 / 34 / 200 (around F) | 951 | 50% | -58 | -0.06 | +49 | +0.3 | +136 / +19 / -105 | noise |
| J 12 / 26 / 150 (F + EMA 150) | 1081 | 51% | +14 | +0.01 | +122 | +0.8 | +52 / +118 / -49 | noise |
| K 12 / 26 / 120 (F + EMA 120) | 1087 | 51% | -11 | -0.01 | +96 | +0.6 | +28 / +137 / -70 | noise |
| L 20 / 40 / 200 (beyond I) | 891 | 50% | -103 | -0.12 | +4 | +0.0 | +84 / +31 / -111 | noise |
| M 24 / 50 / 200 (beyond I) | 863 | 50% | -154 | -0.18 | -47 | -0.3 | -41 / +62 / -68 | worse |
| N 16 / 34 / 120 (I + EMA 120) | 968 | 50% | -76 | -0.08 | +31 | +0.2 | +119 / +47 / -135 | noise |
| Reference: standard EMAs, LTF EMA20 Pierce trigger OFF | 827 | 51% | -31 | -0.04 | +76 | +0.5 | +44 / +90 / -57 | noise |

By trigger (setups / net): A: Flip 326 / +71 · LTF20 579 / -66 · HTF9 177 / -90 · HTF20 112 / -23; B: Flip 374 / +64 · LTF20 822 / -180 · HTF9 192 / -88 · HTF20 108 / -34; C: Flip 346 / +58 · LTF20 836 / -151 · HTF9 192 / -102 · HTF20 110 / -35; D: Flip 354 / +77 · LTF20 567 / -60 · HTF9 179 / -78 · HTF20 107 / -25; E: Flip 348 / +119 · LTF20 735 / -186 · HTF9 181 / -54 · HTF20 111 / -34; F: Flip 302 / +104 · LTF20 463 / -16 · HTF9 177 / -68 · HTF20 129 / -34; G: Flip 310 / +60 · LTF20 487 / -105 · HTF9 179 / -44 · HTF20 122 / -30; H: Flip 289 / +110 · LTF20 387 / -101 · HTF9 196 / -65 · HTF20 137 / -41; I: Flip 278 / +90 · LTF20 364 / +21 · HTF9 175 / -142 · HTF20 134 / -27; J: Flip 315 / +125 · LTF20 460 / -19 · HTF9 178 / -64 · HTF20 128 / -28; K: Flip 329 / +106 · LTF20 456 / -29 · HTF9 178 / -64 · HTF20 124 / -24; L: Flip 265 / +58 · LTF20 319 / -48 · HTF9 170 / -82 · HTF20 137 / -31; M: Flip 245 / +59 · LTF20 287 / -146 · HTF9 197 / -45 · HTF20 134 / -21; N: Flip 305 / +92 · LTF20 362 / +0 · HTF9 174 / -147 · HTF20 127 / -21

**B. 15m HTF instead of 25m (⑪ HTF Timeframe = 15)** — compared with A (standard, 25m HTF)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 15m HTF + A 9 / 20 / 200 | 1274 | 48% | -115 | -0.09 | -8 | -0.0 | +74 / -170 / +87 | worse |
| 15m HTF + B 5 / 12 / 120 | 1681 | 49% | +29 | +0.02 | +136 | +0.4 | +128 / -240 / +248 | noise |

By trigger: 15m A: Flip 357 / -20 · LTF20 608 / +20 · HTF9 181 / -72 · HTF20 128 / -43; 15m B: Flip 407 / -1 · LTF20 968 / +145 · HTF9 199 / -85 · HTF20 107 / -30

**C. Bar-count gates on 5m candles** (standard EMAs, 25m HTF). On 3m: cooldown 10 bars = 30 min, ER(12) = 36 min, range gate 24 bars = 72 min. Time-matched on 5m: cooldown 6, ER(8) (40 min; ER(6) = 30 min), range 14 bars.

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| Cooldown 6 bars (30 min) | 1264 | 51% | -158 | -0.13 | -51 | -0.8 | -114 / +63 / -0 | worse |
| Cooldown 4 bars | 1294 | 51% | -126 | -0.10 | -19 | -0.2 | -110 / +73 / +18 | worse |
| Cooldown 15 bars | 1132 | 51% | -91 | -0.08 | +16 | +0.3 | -25 / +21 / +21 | noise |
| ER(8) (40 min) | 1461 | 51% | -207 | -0.14 | -100 | -0.5 | -36 / -52 / -12 | worse |
| ER(6) (30 min) | 1578 | 51% | -119 | -0.08 | -11 | -0.1 | +14 / +26 / -51 | worse |
| ER(16) (80 min) | 1043 | 50% | -103 | -0.10 | +5 | +0.0 | +134 / +65 / -194 | noise |
| Cooldown 6 + ER(8) (all time-matched) | 1553 | 50% | -259 | -0.17 | -151 | -0.7 | -124 / +13 / -41 | worse |
| Range gate ON, 24 bars / 5 ATR (as 3m, = 120 min) | 1034 | 51% | -46 | -0.04 | +61 | +0.5 | -89 / +43 / +106 | noise |
| Range gate ON, 14 bars / 5 ATR (72 min) | 962 | 49% | -207 | -0.21 | -100 | -0.7 | -79 / -18 / -2 | worse |
| Range gate ON, 14 bars / 4 ATR | 1034 | 50% | -224 | -0.22 | -117 | -1.0 | -73 / -29 / -15 | worse |

**D. Bar-count gates with 5 / 12 / 120** (compared with A standard)

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| B 5 / 12 / 120, standard gates | 1496 | 51% | -238 | -0.16 | -130 | -0.6 | -67 / -87 / +23 | worse |
| ER(8) (40 min) | 1673 | 51% | -169 | -0.10 | -62 | -0.2 | -34 / -41 / +13 | worse |
| Cooldown 6 + ER(8) (all time-matched) | 1797 | 51% | -242 | -0.13 | -135 | -0.5 | -104 / -62 / +31 | worse |
| Range gate ON, 14 bars / 5 ATR (72 min) | 1221 | 50% | -156 | -0.13 | -49 | -0.2 | +8 / -65 / +8 | worse |

## MES 3m (102745 candles) — watch: slow EMA 16 / 14 (range gate on, base exits)

Only the SLOW length changes the replay (the fast EMA feeds only the cloud / "price past both EMA clouds" gate, not modelled).

| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|---|
| A3 9 / 20 / 200 (standard) | 1756 | 50% | +7 | +0.00 | +0 | +0.0 | +0 / +0 / +0 | baseline | Flip 319 / +41 · LTF20 964 / +129 · HTF9 291 / -163 · HTF20 182 / -0
| P3 8 / 18 / 200 | 1848 | 51% | -5 | -0.00 | -12 | -0.1 | -38 / +26 / +1 | worse | Flip 324 / +51 · LTF20 1048 / +141 · HTF9 294 / -210 · HTF20 182 / +13
| Q3 7 / 16 / 200 | 1901 | 51% | +159 | +0.08 | +152 | +0.9 | -61 / +154 / +59 | noise | Flip 330 / +51 · LTF20 1084 / +236 · HTF9 306 / -153 · HTF20 181 / +25
| R3 6 / 14 / 200 | 1996 | 51% | +61 | +0.03 | +54 | +0.3 | -69 / +70 / +53 | noise | Flip 333 / +55 · LTF20 1190 / +176 · HTF9 296 / -181 · HTF20 177 / +11
| S3 5 / 12 / 200 | 2092 | 51% | -64 | -0.03 | -71 | -0.3 | -115 / +37 / +7 | worse | Flip 336 / +49 · LTF20 1296 / +101 · HTF9 295 / -214 · HTF20 165 / -0

Last 4 weeks of the replay, Δ net vs standard (live-period check; the extra shallow pierces a faster slow EMA adds cannot be seen in the live alerts): P3 -57.5 · Q3 -36.5 · R3 -35.7 · S3 -40.7

## MES 2m (82259 candles, Jun–Oct) — watch: slow EMA 16 (1H MTF gate + HTF flips >= 4, base exits)

Only the SLOW length changes the replay. Thirds = Jun–Jul / Aug / Sep–Oct.

| Variant | Setups | Net | Δ vs standard | z | Δ by third | Verdict | LTF EMA20 Pierce setups / net |
|---|---|---|---|---|---|---|---|
| A2 9 / 20 / 200 (standard) | 1224 | -217 | +0 | +0.0 | +0 / +0 / +0 | baseline | 552 / -155 |
| T2 9 / 12 / 200 | 1391 | -130 | +87 | +0.6 | +37 / -2 / +52 | noise | 713 / -30 |
| U2 9 / 16 / 200 | 1315 | +4 | +221 | +1.9 | +71 / -9 / +159 | noise | 635 / +107 |
| V2 9 / 24 / 200 | 1145 | -166 | +51 | +0.5 | -13 / +23 / +42 | noise | 473 / -53 |
| W2 9 / 28 / 200 | 1062 | -92 | +125 | +1.1 | -36 / +19 / +143 | noise | 401 / +23 |

Last 4 weeks of the replay, Δ net vs standard: T2 +70.6 · U2 +68.6 · V2 +9.6 · W2 +85.4

## Candidates (robust / promising)

- MES 5m: D 9 / 20 / 120 (200 only) → Δ +45, z +1.1, thirds +6 / +16 / +23 (promising)
- MES 5m: F 12 / 26 / 200 (slower) → Δ +276, z +2.1, thirds +208 / +6 / +62 (robust)
- MES 5m: H 14 / 30 / 200 (around F) → Δ +378, z +2.6, thirds +276 / +27 / +75 (robust)
- MES 5m: I 16 / 34 / 200 (around F) → Δ +466, z +3.1, thirds +199 / +116 / +151 (robust)
- MES 5m: J 12 / 26 / 150 (F + EMA 150) → Δ +277, z +2.1, thirds +209 / +12 / +55 (robust)
- MES 5m: K 12 / 26 / 120 (F + EMA 120) → Δ +306, z +2.2, thirds +212 / +20 / +74 (robust)
- MES 5m: L 20 / 40 / 200 (beyond I) → Δ +334, z +2.2, thirds +183 / +108 / +43 (robust)
- MES 5m: M 24 / 50 / 200 (beyond I) → Δ +252, z +1.6, thirds +172 / +60 / +20 (promising)
- MES 5m: N 16 / 34 / 120 (I + EMA 120) → Δ +504, z +3.2, thirds +200 / +136 / +168 (robust)
- MES 5m: Cooldown 6 bars (30 min) → Δ +100, z +2.0, thirds +4 / +72 / +24 (robust)
## Live setups (alert store, current CBC chart EMAs 9 / 20 / 200) by trigger: MES / MGC 5m and MES 3m

| Chart | Trigger | Setups | Ended | Win % | Net | Avg |
|---|---|---|---|---|---|---|
| MES 2m | HTF CBC Flip | 40 | 37 | 51% | -6.2 | -0.17 |
| MES 2m | HTF EMA20 Pierce | 13 | 12 | 33% | -8.5 | -0.71 |
| MES 2m | HTF EMA9 Pierce | 11 | 10 | 44% | -9.2 | -0.92 |
| MES 2m | HTF Pullback Structure | 2 | 2 | 50% | -3.2 | -1.60 |
| MES 2m | LTF EMA20 Pierce | 93 | 86 | 42% | -76.5 | -0.89 |
| MES 3m | HTF CBC Flip | 18 | 16 | 56% | +23.0 | +1.44 |
| MES 3m | HTF EMA20 Pierce | 10 | 8 | 38% | -5.1 | -0.63 |
| MES 3m | HTF EMA9 Pierce | 15 | 14 | 43% | +4.8 | +0.34 |
| MES 3m | HTF Pullback Structure | 2 | 2 | 0% | -9.1 | -4.54 |
| MES 3m | LTF EMA20 Pierce | 76 | 69 | 48% | -36.8 | -0.53 |
| MES 5m | HTF CBC Flip | 17 | 15 | 67% | +11.0 | +0.74 |
| MES 5m | HTF EMA20 Pierce | 9 | 8 | 62% | +4.9 | +0.61 |
| MES 5m | HTF EMA9 Pierce | 5 | 3 | 33% | -8.7 | -2.90 |
| MES 5m | HTF Pullback Structure | 1 | 1 | 0% | -5.8 | -5.75 |
| MES 5m | LTF EMA20 Pierce | 49 | 44 | 48% | -19.8 | -0.45 |
| MGC 5m | HTF CBC Flip | 18 | 18 | 56% | -1.2 | -0.07 |
| MGC 5m | HTF EMA20 Pierce | 9 | 8 | 50% | +2.1 | +0.26 |
| MGC 5m | HTF EMA9 Pierce | 14 | 12 | 67% | +27.5 | +2.29 |
| MGC 5m | HTF Pullback Structure | 1 | 1 | 0% | -2.7 | -2.70 |
| MGC 5m | LTF EMA20 Pierce | 45 | 39 | 36% | -55.2 | -1.42 |
| MGC 5m | LTF EMA20 Touch | 1 | 1 | 100% | +5.6 | +5.58 |

