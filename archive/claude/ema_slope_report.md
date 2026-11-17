# EMA direction gate study — MGC 3m / MES 3m (weekly check, 11/13 week) -- 2026-11-14 11:24 ET

**STUDY SETTINGS STALE:** claude/settings_sync_report.md (11/13) lists MISMATCH for chop_sim.py `EXIT[('MES',3)]` (part 'tod' = 80 %/100 % by time of day vs live v10.95+ 100 % at TP1 all day) and `EXIT[('MGC',3)]` (50 % at TP1 + trail 3.5 vs live v10.96 FLIP 0 %, no trail). This run used the unchanged script (method not changed), so the exits below are one step behind live on both cases.

**Existing CBC rule:** ① Auto Trade Setup → "Skip setups when HTF EMA slope is against the trade / min slope (pts)": Off (default) / HTF EMA9 / HTF EMA20 / Both EMA9 + EMA20, plus a min slope in pts. Slope = live 15m EMA now − one HTF candle (5 × 3m) ago. No chart-EMA20 direction gate exists.

## Since last week (11/06 rerun → 11/13)

**Baseline jump comes from the 11/08 replay-script sync, not the market:** chop_sim's MES 3m / MGC 3m exits were switched to the then-live exits (MES SL1 3 ATR / TP1 1.75 / 80-100 % by time; MGC 50 % + trail 3.5). New current baseline: MGC 3m 1148 setups, +547 (thirds +282 / +8 / +256), SD 8.5 (was 1183, +296, SD 6.8); MES 3m 1738, +47 (+171 / −382 / +258), SD 7.2 (was 1726, −102, SD 4.8). Moves in the table below are mostly that exit change plus one new week.

| Item (all triggers) | 11/06 (repaired) | 11/13 | Move |
|---|---|---|---|
| MGC 3m gate EMA9 min 0 | −40 (z −0.4), −21 / +2 / −21 | −72 (z −0.6), −31 / −25 / −16 | worse in every third now |
| MGC 3m gate EMA20 min 0 | −179 (z −2.5), −69 / −59 / −51 | −175 (z −1.9), −62 / −68 / −45 | ≈ same — worse in every third |
| MGC 3m gate Both min 0 | −120 (z −1.2), −55 / −34 / −32 | −175 (z −1.4), −80 / −60 / −35 | worse |
| MES 3m gate EMA9 min 0 | −26 (z −0.3), −33 / +24 / −17 | −53 (z −0.5), −72 / +50 / −31 | worse |
| MES 3m gate EMA20 min 0 | −66 (z −1.2), −30 / +13 / −49 | −146 (z −1.8), −48 / +13 / −111 | clearly worse |
| MES 3m gate Both min 0 | −23 (z −0.3), −32 / +36 / −27 | −92 (z −0.7), −67 / +55 / −80 | worse |
| **MES 3m Both EMA9 + EMA20, min 0.5** | +194, z +1.3, +0 / +129 / +65 — promising | **+51, z +0.2, −135 / +173 / +13 — noise** | dropped out of "promising" (Jan–Mar now −135 with the new exits) |
| **MES 3m chart EMA20 slope with trade** (not in CBC) | +102, z +1.5, +16 / +27 / +59 — promising | **+88, z +1.0 (just under 1), +8 / +28 / +51 — noise** | slightly down; still better in all thirds, z now just below the promising line |
| MES 3m HTF EMA9 min 0.5 | +132, z +1.0, +1 / +94 / +37 | +77, z +0.4, −118 / +125 / +69 | down — noise |
| Against-the-trade setups (HTF EMA20 against, all triggers) | MGC 100 +164 · MES 114 +81 | MGC 96 +184 · MES 110 +193 | more profitable → gate still removes winners |
| LTF EMA20 pierces with HTF EMA20 against | MGC 46 +99 · MES 44 +58 | MGC 45 +97 · MES 45 +132 | still positive |

Robust-week streak (verdict rule needs 3 consecutive): **0** for every variant (10/27, 10/30, 11/06, 11/13: none robust; no variant is even "promising" this week). The 10/27 conclusion (min-0 gate hurts) is **not reversed**: no case has Δ ≥ 0 in all thirds for a min-0 gate (MES EMA20 min 0 is now z −1.8, MGC EMA20 min 0 z −1.9).

## Live setups (real Trade Setup → Setup Ended results; slopes from BarFeed bars, chop_sim live 15m EMAs, last 5 candles, trade direction)

Alerts de-duplicated per claude/DATA_NOTES.md (stored duplicates still not cleaned); MGC 3m live results 11/09–11/12 are partly on the old exits (80 % / trail 1.7) where only the old-alert result existed, and MGC 3m since 11/13 runs FLIP 0 % (v10.96).

| Case | Setups matched (period) | 15m EMA9 with / against | 15m EMA20 with / against | Both ≥ 0.5 pt / < 0.5 | Chart EMA20 with / against |
|---|---|---|---|---|---|
| MGC 3m | 79, net +10.9 (10/19–11/13; 0 unmatched to bars, 11 without a result) | 65 −7.2 / 14 +18.1 | 67 +11.8 / 12 −1.0 | 25 +16.2 / 54 −5.4 | 72 −6.4 / 7 +17.2 |
| MES 3m | 108, net −28.0 (10/19–11/13; 0 unmatched to bars, 13 without a result) | 93 −29.7 / 15 +1.7 | 100 −29.7 / 8 +1.7 | 53 −5.9 / 55 −22.1 | 101 −34.2 / 7 +6.2 |

Since 11/06: MGC +12 setups (+45.1), MES +5 setups (−37.4). "Against" groups are still below 20 (7–15 per case), so live data cannot test a min-0 gate; where they exist they are again the better group (against-the-trade setups did not lose). Both ≥ 0.5 vs < 0.5 (both groups ≥ 20): **MES** ≥ 0.5 still better (53 −5.9 vs 55 −22.1), live still agrees with the old watch item even though the simulator dropped it; **MGC** ≥ 0.5 now better too (25 +16.2 vs 54 −5.4; last week it was worse per trade), which the simulator does not support (MGC Both min 0.5: −88, worse in 2 of 3 thirds).

**Verdict:** keep the HTF EMA slope gate **Off** on MGC 3m and MES 3m (no variant robust; streak 0; no promising candidates this week). Watch items: MES 3m chart-EMA20 slope (z +1.0, better in all thirds, not a CBC input) and MES 3m "Both min 0.5" (simulator now noise, live still favourable). Next run should use chop_sim exits synced to v10.96 (MES 100 % at TP1; MGC FLIP 0 %) — fixes listed in settings_sync_report §C items 2–3 (not applied here). Simulator ≈ 50 % exact setup match: compare variants, not absolute numbers.

Script: claude/ema_slope_study.py (needs claude/chop_sim.py next to it and MES.json / MGC.json from /bars?sym=<KEY>&days=400&from=2026-01-05). Script ran unchanged (title line set to run time). Live check: same matching as cbc_daily_stats.py load_setups + dedupe.

---

# EMA direction gate study (MGC 3m, MES 3m) — 2026-11-14 11:24 ET (bars to 11/13 close)

EMA direction (slope) gate study -- MGC 3m and MES 3m.

Question: should a setup be skipped when the HTF EMA9 and/or HTF EMA20 (and/or the chart EMA20) is not sloping in the
trade direction?  CBC already has this input (v9.73-v9.76, default Off): "Skip setups when HTF EMA slope is against
the trade / min slope (pts)" with Off / HTF EMA9 / HTF EMA20 / Both EMA9 + EMA20. Slope = live 15m EMA now minus its
value one HTF candle (5 chart candles) ago; long needs slope >= min, short <= -min; applies to every trigger.

Simulator: chop_sim.py (CBC v10.35-style setup engine incl. current ER/breakout rule, R5/X4 gates and v10.31 exits;
~50 % exact match with real setups, so compare variants rather than absolute numbers). Bars: BarFeed archive 01/05 ->
today (MES.json / MGC.json in the cwd). Each variant changes ONE thing vs current (gate Off).
z = change / (per-trade SD x sqrt(setups changed)); "robust" = z >= 2 and better in all three thirds; "promising" =
z >= 1 and better in all three thirds.

## MGC 3m — 01/05 to 11/13 · current: 1148 setups, net +547 (thirds +282 / +8 / +256), SD 8.5

**Current setups split by EMA direction at entry (slope over the last 5 candles)**

| Trigger | N | HTF EMA9 with / against (net) | HTF EMA20 with / against (net) | Chart EMA20 with / against (net) | Both HTF with / not (net) |
|---|---|---|---|---|---|
| All | 1148 | 984 +457 / 164 +89 | 1052 +363 / 96 +184 | 1028 +585 / 120 -38 | 961 +376 / 187 +171 |
| HTF CBC Flip | 214 | 211 +168 / 3 -2 | 214 +166 / 0 +0 | 202 +196 / 12 -29 | 211 +168 / 3 -2 |
| LTF EMA20 Pierce | 586 | 530 +252 / 56 +31 | 541 +186 / 45 +97 | 581 +282 / 5 +1 | 514 +182 / 72 +101 |
| HTF EMA9 Pierce | 176 | 139 -27 / 37 +24 | 160 -51 / 16 +47 | 130 +34 / 46 -37 | 134 -35 / 42 +31 |
| HTF EMA20 Pierce | 172 | 104 +65 / 68 +37 | 137 +62 / 35 +39 | 115 +74 / 57 +27 | 102 +61 / 70 +40 |

**Gate applied to all triggers**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 1016 | +474 | -72 | -0.6 | -31 / -25 / -16 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 925 | +474 | -72 | -0.5 | -14 / +2 / -60 | worse |
| HTF EMA9 slope with trade, min 0.5 pt | 794 | +432 | -115 | -0.6 | -81 / +41 / -74 | worse |
| HTF EMA9 slope with trade, min 1.0 pt | 531 | +456 | -90 | -0.4 | -97 / +108 / -101 | worse |
| HTF EMA20 slope with trade, min 0 pt | 1070 | +371 | -175 | -1.9 | -62 / -68 / -45 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 881 | +508 | -39 | -0.2 | -114 / +65 / +10 | worse |
| HTF EMA20 slope with trade, min 0.5 pt | 679 | +477 | -69 | -0.3 | -96 / +71 / -44 | worse |
| HTF EMA20 slope with trade, min 1.0 pt | 326 | +339 | -208 | -0.8 | -95 / +63 / -175 | worse |
| Both HTF EMA9 + EMA20, min 0 pt | 1000 | +372 | -175 | -1.4 | -80 / -60 / -35 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 810 | +502 | -45 | -0.2 | -76 / +56 / -26 | worse |
| Both HTF EMA9 + EMA20, min 0.5 pt | 619 | +459 | -88 | -0.4 | -93 / +73 / -67 | worse |
| Both HTF EMA9 + EMA20, min 1.0 pt | 297 | +336 | -210 | -0.8 | -109 / +65 / -166 | worse |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1086 | +463 | -84 | -1.1 | -24 / -33 / -27 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1047 | +570 | +24 | +0.2 | +27 / +29 / -33 | noise |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 951 | +404 | -143 | -1.0 | -65 / -44 / -34 | worse |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 907 | +521 | -26 | -0.2 | -57 / -3 / +34 | worse |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 864 | +399 | -148 | -0.9 | -96 / +16 / -68 | worse |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 782 | +616 | +69 | +0.4 | +47 / +49 / -27 | noise |

**Gate applied to pierces only (LTF20/HTF9/HTF20)**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 1018 | +470 | -77 | -0.7 | -38 / -25 / -14 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 935 | +482 | -64 | -0.5 | -21 / +5 / -49 | worse |
| HTF EMA9 slope with trade, min 0.5 pt | 822 | +476 | -71 | -0.4 | -87 / +38 / -21 | worse |
| HTF EMA9 slope with trade, min 1.0 pt | 606 | +480 | -67 | -0.3 | -116 / +98 / -49 | worse |
| HTF EMA20 slope with trade, min 0 pt | 1070 | +371 | -175 | -1.9 | -62 / -68 / -45 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 900 | +501 | -46 | -0.3 | -121 / +48 / +28 | worse |
| HTF EMA20 slope with trade, min 0.5 pt | 733 | +542 | -5 | -0.0 | -107 / +62 / +40 | worse |
| HTF EMA20 slope with trade, min 1.0 pt | 462 | +431 | -116 | -0.5 | -89 / +52 / -78 | worse |
| Both HTF EMA9 + EMA20, min 0 pt | 1002 | +367 | -180 | -1.4 | -87 / -60 / -33 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 834 | +498 | -48 | -0.3 | -87 / +49 / -10 | worse |
| Both HTF EMA9 + EMA20, min 0.5 pt | 681 | +533 | -14 | -0.1 | -98 / +68 / +17 | worse |
| Both HTF EMA9 + EMA20, min 1.0 pt | 436 | +417 | -130 | -0.5 | -107 / +53 / -76 | worse |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1086 | +463 | -84 | -1.1 | -24 / -33 / -27 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1054 | +559 | +13 | +0.1 | +21 / +22 / -30 | noise |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 958 | +393 | -154 | -1.1 | -71 / -51 / -32 | worse |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 943 | +540 | -7 | -0.1 | -33 / -20 / +46 | worse |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 881 | +396 | -150 | -0.9 | -111 / +12 / -52 | worse |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 821 | +521 | -26 | -0.1 | -58 / +37 / -5 | worse |


## MES 3m — 01/05 to 11/13 · current: 1738 setups, net +47 (thirds +171 / -382 / +258), SD 7.2

**Current setups split by EMA direction at entry (slope over the last 5 candles)**

| Trigger | N | HTF EMA9 with / against (net) | HTF EMA20 with / against (net) | Chart EMA20 with / against (net) | Both HTF with / not (net) |
|---|---|---|---|---|---|
| All | 1738 | 1520 -45 / 218 +92 | 1628 -146 / 110 +193 | 1593 +132 / 145 -85 | 1487 -111 / 251 +158 |
| HTF CBC Flip | 320 | 312 -223 / 8 +9 | 320 -214 / 0 +0 | 307 -203 / 13 -11 | 312 -223 / 8 +9 |
| LTF EMA20 Pierce | 984 | 934 +128 / 50 +98 | 939 +95 / 45 +132 | 979 +266 / 5 -39 | 913 +83 / 71 +143 |
| HTF EMA9 Pierce | 270 | 192 -1 / 78 -56 | 252 -65 / 18 +9 | 206 -21 / 64 -35 | 183 -26 / 87 -30 |
| HTF EMA20 Pierce | 164 | 82 +51 / 82 +40 | 117 +39 / 47 +52 | 101 +91 / 63 +1 | 79 +56 / 85 +36 |

**Gate applied to all triggers**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 1553 | -6 | -53 | -0.5 | -72 / +50 / -31 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 1358 | +63 | +16 | +0.1 | -113 / +111 / +18 | noise |
| HTF EMA9 slope with trade, min 0.5 pt | 1125 | +124 | +77 | +0.4 | -118 / +125 / +69 | noise |
| HTF EMA9 slope with trade, min 1.0 pt | 682 | -3 | -50 | -0.2 | -210 / +163 / -3 | worse |
| HTF EMA20 slope with trade, min 0 pt | 1647 | -99 | -146 | -1.8 | -48 / +13 / -111 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 1367 | +28 | -19 | -0.1 | -46 / +64 / -37 | worse |
| HTF EMA20 slope with trade, min 0.5 pt | 1002 | -48 | -95 | -0.4 | -154 / +128 / -68 | worse |
| HTF EMA20 slope with trade, min 1.0 pt | 487 | +50 | +3 | +0.0 | -131 / +248 / -114 | noise |
| Both HTF EMA9 + EMA20, min 0 pt | 1522 | -44 | -92 | -0.7 | -67 / +55 / -80 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 1236 | +75 | +28 | +0.2 | -84 / +120 / -8 | noise |
| Both HTF EMA9 + EMA20, min 0.5 pt | 899 | +98 | +51 | +0.2 | -135 / +173 / +13 | noise |
| Both HTF EMA9 + EMA20, min 1.0 pt | 428 | -10 | -58 | -0.2 | -177 / +221 / -102 | worse |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1678 | -60 | -108 | -1.5 | -54 / +8 / -61 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1607 | +135 | +88 | +1.0 | +8 / +28 / +51 | noise |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 1477 | +27 | -20 | -0.2 | -26 / +50 / -44 | worse |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 1518 | -20 | -67 | -0.6 | -21 / +98 / -144 | worse |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 1361 | +79 | +31 | +0.2 | -91 / +92 / +30 | noise |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 1329 | +106 | +59 | +0.3 | -46 / +123 / -18 | noise |

**Gate applied to pierces only (LTF20/HTF9/HTF20)**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 1559 | -6 | -53 | -0.5 | -80 / +50 / -24 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 1380 | +35 | -13 | -0.1 | -117 / +106 / -2 | worse |
| HTF EMA9 slope with trade, min 0.5 pt | 1178 | +80 | +33 | +0.2 | -138 / +120 / +51 | noise |
| HTF EMA9 slope with trade, min 1.0 pt | 812 | -64 | -112 | -0.5 | -237 / +168 / -43 | worse |
| HTF EMA20 slope with trade, min 0 pt | 1647 | -99 | -146 | -1.8 | -48 / +13 / -111 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 1393 | +18 | -30 | -0.2 | -46 / +71 / -54 | worse |
| HTF EMA20 slope with trade, min 0.5 pt | 1079 | -43 | -90 | -0.4 | -129 / +118 / -79 | worse |
| HTF EMA20 slope with trade, min 1.0 pt | 686 | -93 | -141 | -0.6 | -219 / +231 / -153 | worse |
| Both HTF EMA9 + EMA20, min 0 pt | 1528 | -44 | -92 | -0.8 | -75 / +56 / -73 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 1271 | +46 | -1 | -0.0 | -95 / +116 / -22 | worse |
| Both HTF EMA9 + EMA20, min 0.5 pt | 985 | +75 | +28 | +0.1 | -135 / +168 / -5 | noise |
| Both HTF EMA9 + EMA20, min 1.0 pt | 634 | -143 | -190 | -0.8 | -254 / +212 / -149 | worse |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1678 | -60 | -108 | -1.5 | -54 / +8 / -61 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1617 | +115 | +68 | +0.8 | -18 / +37 / +49 | noise |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 1490 | +3 | -44 | -0.3 | -61 / +59 / -42 | worse |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 1537 | -23 | -70 | -0.6 | -7 / +98 / -161 | worse |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 1386 | -10 | -57 | -0.4 | -121 / +58 / +7 | worse |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 1354 | +21 | -26 | -0.2 | -89 / +109 / -46 | worse |


## Candidates (robust / promising)

- none
