# EMA direction gate study — MGC 3m / MES 3m (weekly check 10/28/2026)

**Existing CBC rule:** ① Auto Trade Setup → "Skip setups when HTF EMA slope is against the trade / min slope (pts)": Off (default) / HTF EMA9 / HTF EMA20 / Both EMA9 + EMA20, plus a min slope in pts. Slope = live 15m EMA now − one HTF candle (5 × 3m) ago. No chart-EMA20 direction gate exists.

## Since last week (10/27 → 10/28; bars now end 10/28, only ~1 extra session)

| Item (all triggers) | 10/27 | 10/28 | Move |
|---|---|---|---|
| MGC 3m gate EMA9 min 0 | −21 (z −0.2) | −26 (z −0.3), thirds −21 / +2 / −6 | still worse |
| MGC 3m gate EMA20 min 0 | −163 (z −2.3) | −168 (z −2.3), thirds −69 / −59 / −40 | still worse in every third |
| MGC 3m gate Both min 0 | −98 (z −1.0) | −103 (z −1.0), thirds −55 / −34 / −14 | still worse in every third |
| MES 3m gate EMA9 min 0 | −25 (z −0.3) | −33 (z −0.4), thirds −33 / +24 / −24 | still worse |
| MES 3m gate EMA20 min 0 | −69 (z −1.3) | −77 (z −1.4), thirds −30 / +13 / −59 | still worse |
| MES 3m gate Both min 0 | −37 (z −0.4) | −45 (z −0.5), thirds −32 / +36 / −48 | still worse |
| **MES 3m Both EMA9 + EMA20, min 0.5** | +200, z +1.4, +0 / +129 / +71 | **+198, z +1.3, +0 / +129 / +69** | flat — promising, not robust (Jan–Mar still ≈ 0) |
| **MES 3m chart EMA20 slope with trade** (not in CBC) | +105, z +1.6, +16 / +27 / +61 | **+94, z +1.5, +16 / +27 / +51** | slightly weaker — promising |
| MES 3m EMA9 min 0.5 | +135, z +1.0 (promising) | +122, z +0.9 | dropped to noise |
| Against-the-trade setups (HTF EMA20 against, all triggers) | MGC 98 +148 · MES 110 +71 | MGC 99 +153 · MES 113 +79 | still profitable → gate still removes winners |
| LTF EMA20 pierces with HTF EMA20 against | MGC 46 +101 · MES 42 +56 | MGC 46 +101 · MES 43 +52 | unchanged |

Robust-week streak (verdict rule needs 3 consecutive): **0** for every variant. The 10/27 conclusion (min-0 gate hurts) is **not reversed** — no case has Δ ≥ 0 in all thirds.

## Live setups (real Trade Setup → Setup Ended results; slopes from bars, live 15m EMAs, last 5 candles, trade direction)

| Case | Setups matched (period) | 15m EMA9 with / against | 15m EMA20 with / against | Both ≥ 0.5 pt / < 0.5 | Chart EMA20 with / against |
|---|---|---|---|---|---|
| MGC 3m | 36, net -7.9 (10/19–10/28; 0 unmatched to bars) | 32 -11.6 / 4 +3.7 | 32 -2.3 / 4 -5.7 | 14 +15.2 / 22 -23.1 | 33 -16.3 / 3 +8.4 |
| MES 3m | 63, net -58.4 (10/19–10/28; 0 unmatched to bars) | 53 -60.7 / 10 +2.3 | 58 -48.5 / 5 -9.9 | 29 -37.1 / 34 -21.4 | 57 -65.6 / 6 +7.2 |

Live groups are far below 20 on the "against" side (MGC 3–4, MES 5–10), so live data cannot confirm anything yet. Both ≥ 0.5 vs < 0.5: MGC favours ≥ 0.5 (+15.2 vs −23.1), MES does not (−37.1 vs −21.4, 29 vs 34 setups) — opposite to the simulator's MES watch item.

**Verdict:** keep the HTF EMA slope gate **Off** on MGC 3m and MES 3m. Watch items: MES 3m "Both EMA9 + EMA20, min 0.5 pt" (z +1.3, first third flat) and MES 3m chart-EMA20 slope (z +1.5, not a CBC input). Simulator ≈ 50 % exact setup match — compare variants, not absolute numbers.

Script: claude/ema_slope_study.py (needs claude/chop_sim.py next to it and MES.json / MGC.json from /bars?sym=<KEY>&days=400&from=2026-01-05). Script ran unchanged.

---

# EMA direction gate study (MGC 3m, MES 3m) — Wed 10/28/2026 22:21

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

## MGC 3m — 01/05 to 10/28 · current: 1140 setups, net +200 (thirds +224 / -49 / +25), SD 6.7

**Current setups split by EMA direction at entry (slope over the last 5 candles)**

| Trigger | N | HTF EMA9 with / against (net) | HTF EMA20 with / against (net) | Chart EMA20 with / against (net) | Both HTF with / not (net) |
|---|---|---|---|---|---|
| All | 1140 | 970 +170 / 170 +30 | 1041 +47 / 99 +153 | 1008 +236 / 132 -36 | 943 +111 / 197 +89 |
| HTF CBC Flip | 202 | 199 +91 / 3 -0 | 202 +90 / 0 +0 | 191 +116 / 11 -26 | 199 +91 / 3 -0 |
| LTF EMA20 Pierce | 578 | 524 +155 / 54 +6 | 532 +61 / 46 +101 | 574 +165 / 4 -3 | 506 +94 / 72 +68 |
| HTF EMA9 Pierce | 192 | 149 -88 / 43 -25 | 176 -121 / 16 +8 | 135 -82 / 57 -31 | 143 -89 / 49 -24 |
| HTF EMA20 Pierce | 168 | 98 +11 / 70 +50 | 131 +17 / 37 +45 | 108 +38 / 60 +23 | 95 +15 / 73 +46 |

**Gate applied to all triggers**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 999 | +174 | -26 | -0.3 | -21 / +2 / -6 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 911 | +244 | +44 | +0.4 | -2 / +32 / +15 | noise |
| HTF EMA9 slope with trade, min 0.5 pt | 774 | +245 | +45 | +0.3 | -71 / +89 / +26 | noise |
| HTF EMA9 slope with trade, min 1.0 pt | 512 | +183 | -17 | -0.1 | -106 / +99 / -9 | worse |
| HTF EMA20 slope with trade, min 0 pt | 1056 | +31 | -168 | -2.3 | -69 / -59 / -40 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 864 | +246 | +47 | +0.4 | -85 / +91 / +40 | noise |
| HTF EMA20 slope with trade, min 0.5 pt | 657 | +269 | +69 | +0.4 | -59 / +93 / +35 | noise |
| HTF EMA20 slope with trade, min 1.0 pt | 317 | +149 | -51 | -0.3 | -119 / +119 / -51 | worse |
| Both HTF EMA9 + EMA20, min 0 pt | 977 | +97 | -103 | -1.0 | -55 / -34 / -14 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 796 | +295 | +95 | +0.7 | -33 / +85 / +43 | noise |
| Both HTF EMA9 + EMA20, min 0.5 pt | 595 | +256 | +56 | +0.3 | -67 / +102 / +20 | noise |
| Both HTF EMA9 + EMA20, min 1.0 pt | 288 | +108 | -92 | -0.5 | -168 / +119 / -43 | worse |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1078 | +109 | -91 | -1.5 | -35 / -23 / -32 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1025 | +226 | +26 | +0.3 | +19 / +23 / -15 | noise |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 923 | +91 | -109 | -1.0 | -65 / -37 / -6 | worse |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 899 | +186 | -14 | -0.1 | -38 / +32 / -8 | worse |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 841 | +168 | -32 | -0.2 | -87 / +45 / +10 | worse |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 765 | +295 | +95 | +0.6 | -4 / +73 / +26 | noise |

**Gate applied to pierces only (LTF20/HTF9/HTF20)**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 1001 | +170 | -30 | -0.3 | -28 / +2 / -4 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 919 | +250 | +51 | +0.5 | -13 / +35 / +28 | noise |
| HTF EMA9 slope with trade, min 0.5 pt | 798 | +280 | +80 | +0.6 | -71 / +80 / +70 | noise |
| HTF EMA9 slope with trade, min 1.0 pt | 585 | +224 | +25 | +0.1 | -128 / +106 / +47 | noise |
| HTF EMA20 slope with trade, min 0 pt | 1056 | +31 | -168 | -2.3 | -69 / -59 / -40 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 881 | +232 | +32 | +0.3 | -102 / +72 / +61 | noise |
| HTF EMA20 slope with trade, min 0.5 pt | 710 | +322 | +122 | +0.8 | -83 / +85 / +120 | noise |
| HTF EMA20 slope with trade, min 1.0 pt | 444 | +278 | +78 | +0.4 | -108 / +133 / +53 | noise |
| Both HTF EMA9 + EMA20, min 0 pt | 979 | +92 | -107 | -1.1 | -62 / -34 / -12 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 817 | +286 | +86 | +0.6 | -52 / +74 / +64 | noise |
| Both HTF EMA9 + EMA20, min 0.5 pt | 653 | +312 | +112 | +0.7 | -82 / +98 / +97 | noise |
| Both HTF EMA9 + EMA20, min 1.0 pt | 418 | +232 | +33 | +0.2 | -157 / +133 / +56 | noise |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1078 | +109 | -91 | -1.5 | -35 / -23 / -32 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1033 | +207 | +7 | +0.1 | +13 / +17 / -22 | noise |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 931 | +72 | -127 | -1.1 | -72 / -43 / -13 | worse |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 931 | +226 | +27 | +0.3 | -17 / +16 / +28 | noise |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 857 | +184 | -16 | -0.1 | -101 / +56 / +29 | worse |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 802 | +265 | +65 | +0.5 | -66 / +78 / +53 | noise |


## MES 3m — 01/05 to 10/28 · current: 1677 setups, net -108 (thirds +180 / -292 / +4), SD 4.7

**Current setups split by EMA direction at entry (slope over the last 5 candles)**

| Trigger | N | HTF EMA9 with / against (net) | HTF EMA20 with / against (net) | Chart EMA20 with / against (net) | Both HTF with / not (net) |
|---|---|---|---|---|---|
| All | 1677 | 1446 -151 / 231 +43 | 1564 -187 / 113 +79 | 1512 -34 / 165 -74 | 1417 -155 / 260 +47 |
| HTF CBC Flip | 306 | 298 -40 / 8 +3 | 306 -37 / 0 +0 | 293 -11 / 13 -26 | 298 -40 / 8 +3 |
| LTF EMA20 Pierce | 920 | 871 -46 / 49 +49 | 877 -49 / 43 +52 | 917 +18 / 3 -15 | 852 -62 / 68 +65 |
| HTF EMA9 Pierce | 273 | 193 -49 / 80 -57 | 253 -74 / 20 -32 | 199 -65 / 74 -41 | 185 -32 / 88 -74 |
| HTF EMA20 Pierce | 178 | 84 -16 / 94 +48 | 128 -26 / 50 +58 | 103 +25 / 75 +7 | 82 -21 / 96 +53 |

**Gate applied to all triggers**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 1480 | -142 | -33 | -0.4 | -33 / +24 / -24 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 1289 | -47 | +62 | +0.6 | -1 / +70 / -7 | noise |
| HTF EMA9 slope with trade, min 0.5 pt | 1057 | +13 | +122 | +0.9 | +1 / +94 / +27 | noise |
| HTF EMA9 slope with trade, min 1.0 pt | 632 | -34 | +75 | +0.5 | -67 / +136 / +6 | noise |
| HTF EMA20 slope with trade, min 0 pt | 1586 | -185 | -77 | -1.4 | -30 / +13 / -59 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 1299 | -92 | +17 | +0.2 | +31 / +22 / -36 | noise |
| HTF EMA20 slope with trade, min 0.5 pt | 938 | -26 | +82 | +0.6 | -44 / +101 / +25 | noise |
| HTF EMA20 slope with trade, min 1.0 pt | 453 | +19 | +127 | +0.8 | -91 / +231 / -13 | noise |
| Both HTF EMA9 + EMA20, min 0 pt | 1455 | -153 | -45 | -0.5 | -32 / +36 / -48 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 1171 | -43 | +65 | +0.5 | +33 / +52 / -20 | noise |
| Both HTF EMA9 + EMA20, min 0.5 pt | 838 | +90 | +198 | +1.3 | +0 / +129 / +69 | promising |
| Both HTF EMA9 + EMA20, min 1.0 pt | 396 | -3 | +106 | +0.6 | -108 / +219 / -5 | noise |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1611 | -173 | -65 | -1.4 | -31 / +1 / -35 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1529 | -14 | +94 | +1.5 | +16 / +27 / +51 | promising |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 1405 | -96 | +12 | +0.1 | +10 / +22 / -20 | noise |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 1460 | -53 | +56 | +0.7 | +32 / +53 / -30 | noise |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 1289 | -58 | +50 | +0.5 | +0 / +52 / -2 | noise |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 1262 | -107 | +1 | +0.0 | +15 / +30 / -44 | noise |

**Gate applied to pierces only (LTF20/HTF9/HTF20)**

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| HTF EMA9 slope with trade, min 0 pt | 1486 | -148 | -39 | -0.5 | -38 / +24 / -25 | worse |
| HTF EMA9 slope with trade, min 0.25 pt | 1311 | -65 | +44 | +0.4 | -2 / +68 / -22 | noise |
| HTF EMA9 slope with trade, min 0.5 pt | 1109 | -32 | +77 | +0.6 | -10 / +90 / -3 | noise |
| HTF EMA9 slope with trade, min 1.0 pt | 758 | -67 | +42 | +0.3 | -75 / +122 / -6 | noise |
| HTF EMA20 slope with trade, min 0 pt | 1586 | -185 | -77 | -1.4 | -30 / +13 / -59 | worse |
| HTF EMA20 slope with trade, min 0.25 pt | 1323 | -104 | +4 | +0.0 | +26 / +27 / -49 | noise |
| HTF EMA20 slope with trade, min 0.5 pt | 1016 | -31 | +77 | +0.6 | -50 / +108 / +19 | noise |
| HTF EMA20 slope with trade, min 1.0 pt | 647 | -32 | +76 | +0.5 | -101 / +171 / +6 | noise |
| Both HTF EMA9 + EMA20, min 0 pt | 1461 | -159 | -51 | -0.6 | -37 / +35 / -49 | worse |
| Both HTF EMA9 + EMA20, min 0.25 pt | 1205 | -55 | +54 | +0.5 | +26 / +60 / -33 | noise |
| Both HTF EMA9 + EMA20, min 0.5 pt | 924 | +74 | +182 | +1.3 | -10 / +140 / +52 | noise |
| Both HTF EMA9 + EMA20, min 1.0 pt | 597 | -53 | +55 | +0.3 | -112 / +166 / +1 | noise |
| Either HTF EMA9 or EMA20 with trade (not in CBC) | 1611 | -173 | -65 | -1.4 | -31 / +1 / -35 | worse |
| Chart EMA20 slope with trade (not in CBC) | 1539 | -44 | +65 | +1.1 | -6 / +32 / +38 | noise |
| Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC) | 1419 | -128 | -20 | -0.2 | -17 / +28 / -32 | worse |
| HTF cloud with trade: EMA9 beyond EMA20 (not in CBC) | 1477 | -28 | +80 | +1.1 | +25 / +76 / -21 | noise |
| HTF EMA9 slope >= 0.1 ATR (not in CBC) | 1314 | -96 | +12 | +0.1 | -3 / +37 / -22 | noise |
| HTF EMA20 slope >= 0.1 ATR (not in CBC) | 1284 | -134 | -26 | -0.2 | -10 / +31 / -47 | worse |


## Candidates (robust / promising)

- MES 3m (all triggers): Both HTF EMA9 + EMA20, min 0.5 pt → +198 pts, z +1.3, thirds +0 / +129 / +69 (promising)
- MES 3m (all triggers): Chart EMA20 slope with trade (not in CBC) → +94 pts, z +1.5, thirds +16 / +27 / +51 (promising)
