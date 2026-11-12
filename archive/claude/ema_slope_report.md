# EMA direction gate study — MGC 3m / MES 3m (weekly check, 11/06 run — rerun after data repair) -- 2026-11-07 09:48 ET

**This run REPLACES the 11/06 17:41 run** (BarFeed bars repaired on 11/07: MGC 3m had 5m candles mixed in; the MES 3m 11/02 indicator gap is filled). The 11/06 run's numbers, and the 11/07 09:45 pre-check that already ran on the repaired bars, are superseded; the weekly run history / consecutive-run counts treat this as the 11/06 entry. Bars end 11/06 16:57 ET (same sessions as the original 11/06 run).

**Existing CBC rule:** ① Auto Trade Setup → "Skip setups when HTF EMA slope is against the trade / min slope (pts)": Off (default) / HTF EMA9 / HTF EMA20 / Both EMA9 + EMA20, plus a min slope in pts. Slope = live 15m EMA now − one HTF candle (5 × 3m) ago. No chart-EMA20 direction gate exists.

## Since last week (10/30 → 11/06, repaired bars)

Note: the 10/30 run used the unrepaired archive, so part of each move (mainly MGC's Jul–now third) comes from the repair, not from the new week. Repaired current baseline: MGC 3m 1183 setups, +296 (thirds +224 / −49 / +122); MES 3m 1726, −102 (+180 / −292 / +11).

| Item (all triggers) | 10/30 | 11/06 (repaired) | Move |
|---|---|---|---|
| MGC 3m gate EMA9 min 0 | −26 (z −0.3), −21 / +2 / −6 | −40 (z −0.4), −21 / +2 / −21 | slightly worse — still worse |
| MGC 3m gate EMA20 min 0 | −168 (z −2.3), −69 / −59 / −40 | −179 (z −2.5), −69 / −59 / −51 | worse in every third |
| MGC 3m gate Both min 0 | −103 (z −1.0), −55 / −34 / −14 | −120 (z −1.2), −55 / −34 / −32 | worse in every third |
| MES 3m gate EMA9 min 0 | −30 (z −0.4), −33 / +24 / −21 | −26 (z −0.3), −33 / +24 / −17 | ≈ flat — worse |
| MES 3m gate EMA20 min 0 | −77 (z −1.4), −30 / +13 / −59 | −66 (z −1.2), −30 / +13 / −49 | slightly less bad — worse |
| MES 3m gate Both min 0 | −42 (z −0.5), −32 / +36 / −45 | −23 (z −0.3), −32 / +36 / −27 | less bad — worse |
| **MES 3m Both EMA9 + EMA20, min 0.5** | +202, z +1.4, +0 / +129 / +73 | **+194, z +1.3, +0 / +129 / +65** | ≈ flat — promising, not robust (Jan–Mar ≈ 0) |
| **MES 3m chart EMA20 slope with trade** (not in CBC) | +95, z +1.5, +16 / +27 / +52 | **+102, z +1.5, +16 / +27 / +59** | slightly up — promising |
| MES 3m HTF EMA9 min 0.5 | +115, z +0.9, +1 / +94 / +20 | +132, z +1.0 (0.97), +1 / +94 / +37 | up — still "noise" (z < 1) |
| Against-the-trade setups (HTF EMA20 against, all triggers) | MGC 102 +149 · MES 113 +79 | MGC 100 +164 · MES 114 +81 | still profitable → gate still removes winners |
| LTF EMA20 pierces with HTF EMA20 against | MGC 48 +91 · MES 43 +52 | MGC 46 +99 · MES 44 +58 | still positive |

Robust-week streak (verdict rule needs 3 consecutive): **0** for every variant (10/27, 10/30, 11/06-rerun: none robust). The 10/27 conclusion (min-0 gate hurts) is **not reversed**: no case has Δ ≥ 0 in all thirds, and MGC EMA20 min 0 is z −2.5.

## Live setups (real Trade Setup → Setup Ended results; slopes from repaired bars, live 15m EMAs, last 5 candles, trade direction)

| Case | Setups matched (period) | 15m EMA9 with / against | 15m EMA20 with / against | Both ≥ 0.5 pt / < 0.5 | Chart EMA20 with / against |
|---|---|---|---|---|---|
| MGC 3m | 67, net -34.2 (10/19–11/06; 0 unmatched to bars, 10 without a result) | 57 -38.6 / 10 +4.4 | 56 -30.9 / 11 -3.3 | 23 -19.1 / 44 -15.1 | 61 -49.4 / 6 +15.2 |
| MES 3m | 103, net +9.4 (10/19–11/06; 0 unmatched to bars, 13 without a result) | 88 +7.7 / 15 +1.7 | 95 +7.7 / 8 +1.7 | 50 +17.7 / 53 -8.3 | 96 +3.2 / 7 +6.2 |

"Against" groups are still below 20 (MGC 6–11, MES 7–15), so live data cannot confirm a min-0 gate. Both ≥ 0.5 vs < 0.5 (both groups ≥ 20): **MES** ≥ 0.5 better (50 +17.7 vs 53 −8.3), which agrees with the simulator watch item; **MGC** ≥ 0.5 worse per trade (23 −19.1 vs 44 −15.1), which matches the simulator (every MGC min-slope variant loses in Jan–Mar). With repaired bars, all MES live setups now match (the original 11/06 run had 6 unmatched).

**Verdict:** keep the HTF EMA slope gate **Off** on MGC 3m and MES 3m (no variant robust; streak 0). Watch items: MES 3m "Both EMA9 + EMA20, min 0.5 pt" (z +1.3, first third flat, live agrees) and MES 3m chart-EMA20 slope (z +1.5, not a CBC input). Simulator ≈ 50 % exact setup match: compare variants, not absolute numbers.

Script: claude/ema_slope_study.py (needs claude/chop_sim.py next to it and MES.json / MGC.json from /bars?sym=<KEY>&days=400&from=2026-01-05). Script ran unchanged (title line set to run time).

---

# EMA direction gate study (MGC 3m, MES 3m) — 2026-11-07 09:48 ET (rerun of 11/06 after data repair)

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

## MGC 3m — 01/05 to 11/06 · current: 1183 setups, net +296 (thirds +224 / -49 / +122), SD 6.8

**Current setups split by EMA direction at entry (slope over the last 5 candles)**

| Trigger | N | HTF EMA9 with / against (net) | HTF EMA20 with / against (net) | Chart EMA20 with / against (net) | Both HTF with / not (net) |
|---|---|---|---|---|---|
| All | 1183 | 1006 +252 / 177 +44 | 1083 +132 / 100 +164 | 1045 +326 / 138 -30 | 982 +184 / 201 +112 |
| HTF CBC Flip | 210 | 207 +107 / 3 -0 | 210 +106 / 0 +0 | 199 +132 / 11 -26 | 207 +107 / 3 -0 |
| LTF EMA20 Pierce | 602 | 546 +209 / 56 +13 | 556 +124 / 46 +99 | 596 +217 / 6 +5 | 529 +144 / 73 +79 |
| HTF EMA9 Pierce | 197 | 152 -80 / 45 -13 | 180 -114 / 17 +21 | 138 -61 / 59 -31 | 147 -82 / 50 -11 |
| HTF EMA20 Pierce | 174 | 101 +16 / 73 +44 | 137 +16 / 37 +45 | 112 +38 / 62 +22 | 99 +16 / 75 +45 |

**Gate applied to all triggers**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 1035 | +256 | -40 | -0.4 | -21 / +2 / -21 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 943 | +292 | -4 | -0.0 | -2 / +32 / -34 | worse |
| HTF EMA9 slope with trade, min 0.5 pt | 801 | +260 | -36 | -0.2 | -71 / +89 / -55 | worse |
| HTF EMA9 slope with trade, min 1.0 pt | 528 | +208 | -88 | -0.5 | -106 / +99 / -80 | worse |
| HTF EMA20 slope with trade, min 0 pt | 1098 | +117 | -179 | -2.5 | -69 / -59 / -51 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 898 | +312 | +16 | +0.1 | -85 / +91 / +9 | noise |
| HTF EMA20 slope with trade, min 0.5 pt | 682 | +277 | -19 | -0.1 | -59 / +93 / -54 | worse |
| HTF EMA20 slope with trade, min 1.0 pt | 329 | +155 | -141 | -0.7 | -119 / +119 / -140 | worse |
| Both HTF EMA9 + EMA20, min 0 pt | 1015 | +176 | -120 | -1.2 | -55 / -34 / -32 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 825 | +330 | +34 | +0.2 | -33 / +85 / -18 | noise |
| Both HTF EMA9 + EMA20, min 0.5 pt | 618 | +257 | -39 | -0.2 | -67 / +102 / -75 | worse |
| Both HTF EMA9 + EMA20, min 1.0 pt | 298 | +113 | -183 | -0.9 | -168 / +119 / -133 | worse |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1118 | +197 | -99 | -1.6 | -35 / -23 / -41 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1064 | +313 | +17 | +0.2 | +19 / +23 / -25 | noise |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 959 | +168 | -128 | -1.1 | -65 / -37 / -25 | worse |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 935 | +302 | +6 | +0.1 | -38 / +32 / +12 | noise |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 872 | +210 | -86 | -0.6 | -87 / +45 / -45 | worse |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 796 | +331 | +35 | +0.2 | -4 / +73 / -35 | noise |

**Gate applied to pierces only (LTF20/HTF9/HTF20)**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 1037 | +251 | -45 | -0.5 | -28 / +2 / -19 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 951 | +298 | +2 | +0.0 | -13 / +35 / -20 | noise |
| HTF EMA9 slope with trade, min 0.5 pt | 827 | +304 | +8 | +0.1 | -71 / +80 / -1 | noise |
| HTF EMA9 slope with trade, min 1.0 pt | 603 | +261 | -35 | -0.2 | -128 / +106 / -13 | worse |
| HTF EMA20 slope with trade, min 0 pt | 1098 | +117 | -179 | -2.5 | -69 / -59 / -51 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 916 | +304 | +8 | +0.1 | -102 / +72 / +37 | noise |
| HTF EMA20 slope with trade, min 0.5 pt | 737 | +341 | +45 | +0.3 | -83 / +85 / +43 | noise |
| HTF EMA20 slope with trade, min 1.0 pt | 462 | +314 | +18 | +0.1 | -108 / +133 / -7 | noise |
| Both HTF EMA9 + EMA20, min 0 pt | 1017 | +171 | -125 | -1.2 | -62 / -34 / -29 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 847 | +327 | +31 | +0.2 | -52 / +74 / +9 | noise |
| Both HTF EMA9 + EMA20, min 0.5 pt | 679 | +327 | +31 | +0.2 | -82 / +98 / +16 | noise |
| Both HTF EMA9 + EMA20, min 1.0 pt | 434 | +267 | -29 | -0.2 | -157 / +133 / -6 | worse |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1118 | +197 | -99 | -1.6 | -35 / -23 / -41 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1072 | +294 | -2 | -0.0 | +13 / +17 / -32 | worse |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 967 | +149 | -147 | -1.3 | -72 / -43 / -32 | worse |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 969 | +342 | +46 | +0.4 | -17 / +16 / +47 | noise |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 888 | +225 | -71 | -0.5 | -101 / +56 / -26 | worse |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 834 | +307 | +11 | +0.1 | -66 / +78 / -1 | noise |


## MES 3m — 01/05 to 11/06 · current: 1726 setups, net -102 (thirds +180 / -292 / +11), SD 4.8

**Current setups split by EMA direction at entry (slope over the last 5 candles)**

| Trigger | N | HTF EMA9 with / against (net) | HTF EMA20 with / against (net) | Chart EMA20 with / against (net) | Both HTF with / not (net) |
|---|---|---|---|---|---|
| All | 1726 | 1490 -133 / 236 +32 | 1612 -182 / 114 +81 | 1557 -22 / 169 -79 | 1460 -139 / 266 +37 |
| HTF CBC Flip | 313 | 305 -43 / 8 +3 | 313 -41 / 0 +0 | 300 -14 / 13 -26 | 305 -43 / 8 +3 |
| LTF EMA20 Pierce | 953 | 902 -14 / 51 +42 | 909 -30 / 44 +58 | 948 +44 / 5 -16 | 882 -36 / 71 +64 |
| HTF EMA9 Pierce | 280 | 198 -56 / 82 -58 | 260 -79 / 20 -35 | 205 -73 / 75 -42 | 190 -35 / 90 -80 |
| HTF EMA20 Pierce | 180 | 85 -20 / 95 +45 | 130 -33 / 50 +58 | 104 +21 / 76 +4 | 83 -25 / 97 +50 |

**Gate applied to all triggers**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 1525 | -127 | -26 | -0.3 | -33 / +24 / -17 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 1330 | -42 | +60 | +0.6 | -1 / +70 / -9 | noise |
| HTF EMA9 slope with trade, min 0.5 pt | 1093 | +31 | +132 | +1.0 | +1 / +94 / +37 | noise |
| HTF EMA9 slope with trade, min 1.0 pt | 661 | -43 | +58 | +0.4 | -67 / +136 / -10 | noise |
| HTF EMA20 slope with trade, min 0 pt | 1635 | -168 | -66 | -1.2 | -30 / +13 / -49 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 1343 | -76 | +26 | +0.2 | +31 / +22 / -27 | noise |
| HTF EMA20 slope with trade, min 0.5 pt | 976 | -34 | +68 | +0.5 | -44 / +101 / +11 | noise |
| HTF EMA20 slope with trade, min 1.0 pt | 475 | +41 | +142 | +0.8 | -91 / +231 / +2 | noise |
| Both HTF EMA9 + EMA20, min 0 pt | 1499 | -125 | -23 | -0.3 | -32 / +36 / -27 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 1211 | -21 | +81 | +0.6 | +33 / +52 / -5 | noise |
| Both HTF EMA9 + EMA20, min 0.5 pt | 872 | +92 | +194 | +1.3 | +0 / +129 / +65 | promising |
| Both HTF EMA9 + EMA20, min 1.0 pt | 416 | +3 | +105 | +0.6 | -108 / +219 / -6 | noise |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1661 | -171 | -69 | -1.4 | -31 / +1 / -39 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1575 | +1 | +102 | +1.5 | +16 / +27 / +59 | promising |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 1447 | -63 | +39 | +0.4 | +10 / +22 / +7 | noise |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 1505 | -40 | +62 | +0.8 | +32 / +53 / -24 | noise |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 1329 | -37 | +65 | +0.6 | +0 / +52 / +12 | noise |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 1302 | -110 | -8 | -0.1 | +15 / +30 / -53 | worse |

**Gate applied to pierces only (LTF20/HTF9/HTF20)**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 1531 | -134 | -32 | -0.4 | -38 / +24 / -18 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 1352 | -60 | +42 | +0.4 | -2 / +68 / -24 | noise |
| HTF EMA9 slope with trade, min 0.5 pt | 1146 | -19 | +83 | +0.7 | -10 / +90 / +3 | noise |
| HTF EMA9 slope with trade, min 1.0 pt | 789 | -85 | +17 | +0.1 | -75 / +122 / -31 | noise |
| HTF EMA20 slope with trade, min 0 pt | 1635 | -168 | -66 | -1.2 | -30 / +13 / -49 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 1367 | -89 | +13 | +0.1 | +26 / +27 / -40 | noise |
| HTF EMA20 slope with trade, min 0.5 pt | 1054 | -49 | +52 | +0.4 | -50 / +108 / -6 | noise |
| HTF EMA20 slope with trade, min 1.0 pt | 672 | -24 | +77 | +0.5 | -101 / +171 / +7 | noise |
| Both HTF EMA9 + EMA20, min 0 pt | 1505 | -131 | -29 | -0.4 | -37 / +35 / -28 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 1245 | -32 | +69 | +0.6 | +26 / +60 / -17 | noise |
| Both HTF EMA9 + EMA20, min 0.5 pt | 959 | +61 | +163 | +1.1 | -10 / +140 / +33 | noise |
| Both HTF EMA9 + EMA20, min 1.0 pt | 620 | -61 | +41 | +0.3 | -112 / +166 / -13 | noise |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1661 | -171 | -69 | -1.4 | -31 / +1 / -39 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1585 | -29 | +73 | +1.2 | -6 / +32 / +46 | noise |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 1461 | -95 | +7 | +0.1 | -17 / +28 / -5 | noise |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 1522 | -15 | +86 | +1.1 | +25 / +76 / -15 | noise |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 1354 | -75 | +26 | +0.2 | -3 / +37 / -8 | noise |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 1324 | -137 | -35 | -0.3 | -10 / +31 / -56 | worse |


## Candidates (robust / promising)

- MES 3m (all triggers): Both HTF EMA9 + EMA20, min 0.5 pt → +194 pts, z +1.3, thirds +0 / +129 / +65 (promising)
- MES 3m (all triggers): Chart EMA20 slope with trade (not in CBC) → +102 pts, z +1.5, thirds +16 / +27 / +59 (promising)
