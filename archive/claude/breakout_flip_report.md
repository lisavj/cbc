# Breakout exception + flip-ER variant study — Thu 10/29/2026 21:29

Simulator: chop_sim.py (approximates CBC v10.36: about 50 % of real setups matched exactly, so compare variants, not absolute numbers). z = change / (per-trade SD × √setups changed); "robust" = z ≥ 2 and better in all three thirds, "promising" = z ≥ 1 and all thirds better. About 100 settings have now been tried across the studies, so expect a few z ≈ 2 results by chance.

## MGC 3m — 01/05 to 10/29, current rule 1148 setups, net +194 pts (thirds +224 / -49 / +20), per-trade SD 6.7

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 985 | -34 | -229 | -2.3 | -192 / +16 / -53 | worse |
| 1 · breakout window 2 bars | 1096 | +89 | -105 | -1.7 | -118 / +16 / -3 | worse |
| 1 · breakout window 5 bars | 1215 | +290 | +96 | +1.3 | +57 / -0 / +39 | noise |
| 1 · breakout window 8 bars | 1271 | +216 | +22 | +0.2 | -10 / +14 / +19 | noise |
| 2 · clean break (>= 0.25 ATR beyond) | 1094 | +3 | -192 | -3.0 | -142 / -2 / -48 | worse |
| 2 · breakout candle volume >= 1.2x avg | 964 | +127 | -68 | -0.6 | -75 / +4 / +3 | worse |
| 3 · levels + prior-day H/L | 1164 | +279 | +85 | +2.6 | +28 / +7 / +49 | robust |
| 3 · levels + PP/R1/S1 | 1160 | +171 | -24 | -0.8 | -15 / -0 / -8 | worse |
| 3 · swings only | 1086 | +225 | +31 | +0.5 | -42 / +64 / +10 | noise |
| 3 · opening ranges only | 1000 | +43 | -151 | -1.5 | -73 / -46 / -33 | worse |
| 6 · flip ER min 0.15 | 1173 | +96 | -98 | -1.7 | -42 / -36 / -20 | worse |
| 6 · flip ER min 0.20 | 1157 | +153 | -41 | -1.1 | -19 / -5 / -17 | worse |
| 6 · flip ER min 0.26 | 1140 | +234 | +40 | +1.2 | +19 / +22 / -1 | noise |
| 6 · flip ER min 0.30 | 1126 | +201 | +6 | +0.1 | -7 / +25 / -12 | noise |
| 6 · flip ER min 0.35 | 1109 | +209 | +14 | +0.2 | -13 / +56 / -29 | noise |
| 6 · flip ER min 0.40 | 1094 | +247 | +52 | +0.6 | -6 / +68 / -9 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 1109 | +180 | -15 | -0.1 | +13 / +27 / -54 | worse |
| 7 · flip: + 15m ER >= 0.30 | 1083 | +211 | +17 | +0.2 | +32 / +19 / -34 | noise |
| 7 · flip: + 15m ER >= 0.40 | 1067 | +226 | +32 | +0.3 | +42 / +15 / -26 | noise |
| 8 · flip: + ER rising | 1137 | +184 | -10 | -0.2 | -21 / +43 / -31 | worse |

## MES 3m — 01/05 to 10/29, current rule 1680 setups, net -114 pts (thirds +180 / -292 / -2), per-trade SD 4.7

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 1427 | -98 | +16 | +0.2 | -1 / +6 / +11 | noise |
| 1 · breakout window 2 bars | 1594 | -104 | +11 | +0.2 | -21 / +3 / +29 | noise |
| 1 · breakout window 5 bars | 1770 | -190 | -76 | -1.2 | -19 / -12 / -44 | worse |
| 1 · breakout window 8 bars | 1844 | -189 | -75 | -0.9 | -42 / -24 / -9 | worse |
| 2 · clean break (>= 0.25 ATR beyond) | 1603 | -68 | +47 | +0.8 | +33 / +10 / +3 | noise |
| 2 · breakout candle volume >= 1.2x avg | 1410 | -108 | +7 | +0.1 | -29 / +21 / +14 | noise |
| 3 · levels + prior-day H/L | 1688 | -118 | -3 | -0.2 | +9 / -5 / -8 | worse |
| 3 · levels + PP/R1/S1 | 1692 | -100 | +15 | +0.6 | -8 / +30 / -8 | noise |
| 3 · swings only | 1604 | -115 | -1 | -0.0 | +4 / +8 / -13 | worse |
| 3 · opening ranges only | 1422 | -163 | -49 | -0.5 | -55 / -18 / +24 | worse |
| 6 · flip ER min 0.15 | 1715 | -109 | +5 | +0.1 | -12 / +15 / +1 | noise |
| 6 · flip ER min 0.20 | 1693 | -110 | +5 | +0.2 | -23 / +14 / +14 | noise |
| 6 · flip ER min 0.26 | 1660 | -90 | +25 | +0.7 | +19 / +29 / -24 | noise |
| 6 · flip ER min 0.30 | 1639 | -81 | +33 | +0.7 | +22 / +26 / -15 | noise |
| 6 · flip ER min 0.35 | 1610 | -63 | +52 | +0.7 | +34 / +63 / -46 | noise |
| 6 · flip ER min 0.40 | 1584 | -86 | +28 | +0.4 | +25 / +50 / -47 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 1630 | -128 | -13 | -0.1 | +11 / +56 / -80 | worse |
| 7 · flip: + 15m ER >= 0.30 | 1584 | -102 | +12 | +0.2 | +20 / +39 / -46 | noise |
| 7 · flip: + 15m ER >= 0.40 | 1557 | -100 | +14 | +0.2 | +28 / +61 / -75 | noise |
| 8 · flip: + ER rising | 1659 | -116 | -2 | -0.1 | -17 / +8 / +7 | worse |

## MGC 2m — 01/05 to 10/29, current rule 2865 setups, net +405 pts (thirds +3 / +135 / +267), per-trade SD 5.3

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 2595 | +230 | -175 | -1.5 | -20 / -113 / -42 | worse |
| 1 · breakout window 2 bars | 2752 | +370 | -35 | -0.5 | -2 / -31 / -2 | worse |
| 1 · breakout window 5 bars | 3001 | +462 | +57 | +0.6 | +50 / +4 / +3 | noise |
| 1 · breakout window 8 bars | 3116 | +456 | +51 | +0.4 | +148 / -49 / -48 | noise |
| 2 · clean break (>= 0.25 ATR beyond) | 2760 | +286 | -119 | -1.5 | -77 / -26 / -16 | worse |
| 2 · breakout candle volume >= 1.2x avg | 2496 | +202 | -203 | -1.5 | -70 / -99 / -35 | worse |
| 3 · levels + prior-day H/L | 2881 | +354 | -51 | -1.7 | +4 / -21 / -34 | worse |
| 3 · levels + PP/R1/S1 | 2884 | +389 | -16 | -0.5 | -11 / +5 / -9 | worse |
| 3 · swings only | 2788 | +354 | -51 | -0.8 | -63 / -4 / +16 | worse |
| 3 · opening ranges only | 2495 | +149 | -256 | -1.9 | -85 / -78 / -93 | worse |
| 6 · flip ER min 0.15 | 2961 | +434 | +29 | +0.3 | -75 / +64 / +40 | noise |
| 6 · flip ER min 0.20 | 2911 | +440 | +35 | +0.6 | -27 / +53 / +9 | noise |
| 6 · flip ER min 0.26 | 2814 | +419 | +14 | +0.2 | -3 / +11 / +6 | noise |
| 6 · flip ER min 0.30 | 2756 | +432 | +27 | +0.3 | +31 / -13 / +9 | noise |
| 6 · flip ER min 0.35 | 2685 | +455 | +50 | +0.4 | +28 / +47 / -25 | noise |
| 6 · flip ER min 0.40 | 2607 | +528 | +123 | +0.8 | +75 / +101 / -53 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 2743 | +370 | -35 | -0.2 | +29 / -9 / -54 | worse |
| 7 · flip: + 15m ER >= 0.30 | 2635 | +444 | +39 | +0.2 | +114 / -1 / -74 | noise |
| 7 · flip: + 15m ER >= 0.40 | 2559 | +391 | -14 | -0.1 | +79 / -9 / -84 | worse |
| 8 · flip: + ER rising | 2787 | +416 | +11 | +0.2 | -16 / +30 / -2 | noise |

## MES 2m — 01/05 to 10/29, current rule 2230 setups, net -146 pts (thirds +65 / -61 / -150), per-trade SD 4.6

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 1997 | -160 | -14 | -0.2 | -87 / -15 / +87 | worse |
| 1 · breakout window 2 bars | 2146 | -169 | -23 | -0.4 | -41 / -19 / +37 | worse |
| 1 · breakout window 5 bars | 2329 | -142 | +4 | +0.1 | -36 / +50 / -10 | noise |
| 1 · breakout window 8 bars | 2410 | -211 | -65 | -0.7 | -89 / +31 / -7 | worse |
| 2 · clean break (>= 0.25 ATR beyond) | 2156 | -139 | +7 | +0.1 | +12 / -41 / +36 | noise |
| 2 · breakout candle volume >= 1.2x avg | 1936 | -299 | -153 | -1.5 | -148 / -78 / +74 | worse |
| 3 · levels + prior-day H/L | 2240 | -150 | -4 | -0.2 | -14 / +8 / +2 | worse |
| 3 · levels + PP/R1/S1 | 2241 | -134 | +12 | +0.5 | +4 / +12 / -4 | noise |
| 3 · swings only | 2169 | -107 | +39 | +0.8 | +23 / -30 / +46 | noise |
| 3 · opening ranges only | 1916 | -203 | -57 | -0.5 | -162 / +50 / +55 | worse |
| 6 · flip ER min 0.15 | 2299 | -147 | -1 | -0.0 | +9 / -7 / -4 | worse |
| 6 · flip ER min 0.20 | 2259 | -165 | -19 | -0.4 | -17 / -9 / +7 | worse |
| 6 · flip ER min 0.26 | 2188 | -186 | -40 | -0.7 | -7 / -32 / -1 | worse |
| 6 · flip ER min 0.30 | 2137 | -164 | -18 | -0.2 | -12 / -8 / +1 | worse |
| 6 · flip ER min 0.35 | 2075 | -121 | +25 | +0.2 | +8 / +15 / +2 | noise |
| 6 · flip ER min 0.40 | 2033 | -43 | +103 | +0.9 | -1 / +75 / +29 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 2125 | -41 | +105 | +0.8 | -25 / +51 / +79 | noise |
| 7 · flip: + 15m ER >= 0.30 | 2043 | -55 | +91 | +0.8 | -20 / +28 / +83 | noise |
| 7 · flip: + 15m ER >= 0.40 | 1990 | -18 | +128 | +1.0 | -45 / +74 / +98 | noise |
| 8 · flip: + ER rising | 2181 | -138 | +8 | +0.1 | +7 / +19 / -18 | noise |

## Candidates (robust / promising)

- MGC 3m: 3 · levels + prior-day H/L (+85 pts, z +2.6, robust)


## Comparison with previous report (10/28) and recommendation

| Case | Current net 10/25 → 10/26 → 10/27 → 10/28 → 10/29 | Robust / promising rows | Movement |
|---|---|---|---|
| MGC 3m | +183 → +185 → +183 → +200 → +194 | 3 · levels + prior-day H/L: robust | +85, z +2.6 (thirds +28 / +7 / +49) — unchanged from 10/25–10/28 (10/29 added 8 setups, none changed by the variant) |
| MES 3m | -66 → -74 → -82 → -108 → -114 | none | still sliding (Jul–now third +4 → -2). Best noise rows: flip ER 0.35 +52 z +0.7; clean break +47 z +0.8 (was +52) |
| MGC 2m | +390 → n/a → +415 → +412 → +405 | none | prior-day H/L worse again (-51, z -1.7, was -41); flip ER 0.40 +123 z +0.8 (Jul–now -53) |
| MES 2m | -44 → n/a → -103 → -121 → -146 | none | Jul–now third keeps falling (-124 → -150). "+15m ER ≥ 0.40" +128, z +1.0 but Jan–Mar -45, so noise |

**Recommendation: no change yet.** MGC 3m "levels + prior-day H/L" is robust for the 5th daily run in a row (10/25–10/29), but these runs share almost all their data, so it is still weekly check #1 of 3. It still does not help MES 3m (-3), MGC 2m (-51) or MES 2m (-4). Shorter breakout windows (1–2 bars) and clean break remain clearly worse on MGC 3m (z -2.3 / -1.7 / -3.0); every flip-ER variant is still noise (|z| ≤ 1.2) in every case.

Robust-streak tracker: MGC 3m · levels + prior-day H/L — week of 10/26 robust (daily runs 10/25–10/29 all robust) = weekly check #1 of 3. Next counting check: first run in the week of 11/02; #3 in the week of 11/09.
