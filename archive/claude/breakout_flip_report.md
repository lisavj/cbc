# Breakout exception + flip-ER variant study -- 2026-11-12 09:57 ET

Settings check: claude/settings_sync_report.md (11/12 09:45 ET) -- live CBC v10.87, 0 MISMATCH, 1 known (late_study MGCX runner base; not used here). Study settings current. Exits/gates = the 11/08-synced chop_sim (same as the 11/09 run), so changes vs 11/09 are new bars only (11/10-11/12).

Run note: this run started 11/12 09:57 ET (Thursday morning, not the usual ~5:30 PM slot; the 11/11 run appears to have failed -- the settings sync was also re-run manually for 11/11 this morning). It is the second run of the week of 11/09, so it does not add a new weekly check to any streak.

Simulator: chop_sim.py (approximates CBC v10.36: about 50 % of real setups matched exactly, so compare variants, not absolute numbers). z = change / (per-trade SD × √setups changed); "robust" = z ≥ 2 and better in all three thirds, "promising" = z ≥ 1 and all thirds better. About 100 settings have now been tried across the studies, so expect a few z ≈ 2 results by chance.

## MGC 3m — 01/05 to 11/12, current rule 1141 setups, net +543 pts (thirds +282 / +8 / +252), per-trade SD 8.5

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 988 | +408 | -135 | -1.0 | -84 / +33 / -83 | worse |
| 1 · breakout window 2 bars | 1090 | +495 | -48 | -0.6 | -55 / -4 / +11 | worse |
| 1 · breakout window 5 bars | 1200 | +654 | +111 | +1.2 | +77 / +0 / +33 | promising |
| 1 · breakout window 8 bars | 1253 | +546 | +4 | +0.0 | +26 / -8 / -14 | noise |
| 2 · clean break (>= 0.25 ATR beyond) | 1089 | +410 | -133 | -1.6 | -127 / +7 / -14 | worse |
| 2 · breakout candle volume >= 1.2x avg | 960 | +399 | -144 | -1.0 | -39 / -14 / -91 | worse |
| 3 · levels + prior-day H/L | 1157 | +523 | -20 | -0.5 | -10 / -6 / -3 | worse |
| 3 · levels + PP/R1/S1 | 1154 | +519 | -23 | -0.6 | -16 / +0 / -7 | worse |
| 3 · swings only | 1082 | +602 | +59 | +0.7 | +26 / +43 / -10 | noise |
| 3 · opening ranges only | 999 | +414 | -129 | -1.0 | -29 / -55 / -46 | worse |
| 6 · flip ER min 0.15 | 1168 | +467 | -76 | -1.0 | -53 / -19 / -3 | worse |
| 6 · flip ER min 0.20 | 1152 | +528 | -15 | -0.3 | -6 / +3 / -11 | worse |
| 6 · flip ER min 0.26 | 1132 | +573 | +31 | +0.7 | +19 / +9 / +3 | noise |
| 6 · flip ER min 0.30 | 1120 | +564 | +21 | +0.3 | +2 / +23 / -4 | noise |
| 6 · flip ER min 0.35 | 1103 | +575 | +33 | +0.3 | +16 / +19 / -3 | noise |
| 6 · flip ER min 0.40 | 1085 | +652 | +109 | +0.9 | +63 / +40 / +6 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 1098 | +600 | +57 | +0.4 | +54 / +50 / -46 | noise |
| 7 · flip: + 15m ER >= 0.30 | 1071 | +628 | +85 | +0.7 | +88 / +22 / -25 | noise |
| 7 · flip: + 15m ER >= 0.40 | 1054 | +593 | +50 | +0.4 | +106 / +17 / -73 | noise |
| 8 · flip: + ER rising | 1131 | +557 | +15 | +0.3 | -9 / +33 / -9 | noise |

## MES 3m — 01/05 to 11/12, current rule 1733 setups, net +53 pts (thirds +171 / -382 / +264), per-trade SD 7.2

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 1475 | -73 | -127 | -0.9 | -72 / -54 / +0 | worse |
| 1 · breakout window 2 bars | 1646 | -37 | -90 | -1.0 | -40 / -42 / -7 | worse |
| 1 · breakout window 5 bars | 1826 | -95 | -148 | -1.6 | -56 / -61 / -31 | worse |
| 1 · breakout window 8 bars | 1900 | -173 | -227 | -1.8 | -157 / -78 / +8 | worse |
| 2 · clean break (>= 0.25 ATR beyond) | 1655 | +54 | +1 | +0.0 | +39 / +4 / -43 | noise |
| 2 · breakout candle volume >= 1.2x avg | 1449 | -42 | -96 | -0.6 | -62 / -28 / -6 | worse |
| 3 · levels + prior-day H/L | 1743 | +24 | -30 | -1.0 | +1 / -14 / -16 | worse |
| 3 · levels + PP/R1/S1 | 1746 | +47 | -6 | -0.2 | -6 / +27 / -28 | worse |
| 3 · swings only | 1659 | +6 | -47 | -0.6 | -28 / +1 / -21 | worse |
| 3 · opening ranges only | 1461 | -51 | -104 | -0.7 | -50 / -58 / +3 | worse |
| 6 · flip ER min 0.15 | 1765 | +86 | +33 | +0.4 | -7 / +58 / -18 | noise |
| 6 · flip ER min 0.20 | 1744 | +30 | -23 | -0.5 | -51 / +21 / +6 | worse |
| 6 · flip ER min 0.26 | 1714 | +45 | -9 | -0.2 | +22 / -13 / -18 | worse |
| 6 · flip ER min 0.30 | 1694 | +76 | +22 | +0.3 | +54 / +23 / -55 | noise |
| 6 · flip ER min 0.35 | 1668 | +128 | +74 | +0.7 | +99 / +71 / -96 | noise |
| 6 · flip ER min 0.40 | 1642 | +174 | +120 | +1.0 | +111 / +53 / -43 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 1684 | +139 | +86 | +0.6 | +16 / +88 / -18 | noise |
| 7 · flip: + 15m ER >= 0.30 | 1643 | +182 | +129 | +1.1 | +86 / +50 / -8 | noise |
| 7 · flip: + 15m ER >= 0.40 | 1617 | +221 | +168 | +1.2 | +117 / +97 / -46 | noise |
| 8 · flip: + ER rising | 1717 | +61 | +7 | +0.1 | +6 / -6 / +8 | noise |

## MGC 2m — 01/05 to 11/12, current rule 2594 setups, net +507 pts (thirds +87 / +176 / +243), per-trade SD 5.2

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 2253 | +219 | -287 | -2.3 | -40 / -173 / -74 | worse |
| 1 · breakout window 2 bars | 2452 | +359 | -148 | -1.8 | -39 / -79 / -31 | worse |
| 1 · breakout window 5 bars | 2754 | +568 | +61 | +0.7 | +52 / -9 / +18 | noise |
| 1 · breakout window 8 bars | 2883 | +556 | +49 | +0.4 | +148 / -69 / -30 | noise |
| 2 · clean break (>= 0.25 ATR beyond) | 2476 | +444 | -63 | -0.8 | -84 / -5 / +26 | worse |
| 2 · breakout candle volume >= 1.2x avg | 2146 | +257 | -249 | -1.8 | -108 / -136 / -4 | worse |
| 3 · levels + prior-day H/L | 2611 | +450 | -56 | -2.0 | +4 / -22 / -38 | worse |
| 3 · levels + PP/R1/S1 | 2613 | +504 | -3 | -0.1 | -6 / +9 / -5 | worse |
| 3 · swings only | 2502 | +499 | -8 | -0.1 | -53 / +1 / +44 | worse |
| 3 · opening ranges only | 2145 | +157 | -349 | -2.5 | -140 / -127 / -83 | worse |
| 6 · flip ER min 0.15 | 2658 | +569 | +63 | +0.8 | -35 / +52 / +45 | noise |
| 6 · flip ER min 0.20 | 2622 | +546 | +40 | +0.9 | -4 / +30 / +14 | noise |
| 6 · flip ER min 0.26 | 2557 | +554 | +47 | +0.9 | -6 / +36 / +17 | noise |
| 6 · flip ER min 0.30 | 2520 | +567 | +61 | +0.8 | +22 / +37 / +1 | noise |
| 6 · flip ER min 0.35 | 2486 | +560 | +53 | +0.5 | +17 / +63 / -26 | noise |
| 6 · flip ER min 0.40 | 2444 | +565 | +58 | +0.5 | +51 / +67 / -60 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 2536 | +514 | +8 | +0.1 | +49 / +13 / -54 | noise |
| 7 · flip: + 15m ER >= 0.30 | 2462 | +560 | +54 | +0.5 | +73 / +38 / -57 | noise |
| 7 · flip: + 15m ER >= 0.40 | 2422 | +527 | +20 | +0.2 | +81 / +2 / -63 | noise |
| 8 · flip: + ER rising | 2542 | +509 | +2 | +0.0 | +16 / +4 / -19 | noise |

## MES 2m — 01/05 to 11/12, current rule 2345 setups, net -166 pts (thirds +65 / -61 / -170), per-trade SD 4.7

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 2095 | -172 | -6 | -0.1 | -87 / -15 / +95 | worse |
| 1 · breakout window 2 bars | 2254 | -189 | -23 | -0.4 | -41 / -19 / +37 | worse |
| 1 · breakout window 5 bars | 2447 | -127 | +39 | +0.6 | -36 / +50 / +25 | noise |
| 1 · breakout window 8 bars | 2531 | -207 | -41 | -0.4 | -89 / +31 / +17 | worse |
| 2 · clean break (>= 0.25 ATR beyond) | 2265 | -186 | -20 | -0.3 | +12 / -41 / +9 | worse |
| 2 · breakout candle volume >= 1.2x avg | 2020 | -372 | -206 | -1.9 | -148 / -78 / +21 | worse |
| 3 · levels + prior-day H/L | 2356 | -167 | -1 | -0.0 | -14 / +8 / +6 | worse |
| 3 · levels + PP/R1/S1 | 2356 | -154 | +12 | +0.5 | +4 / +12 / -4 | noise |
| 3 · swings only | 2282 | -125 | +41 | +0.8 | +23 / -30 / +48 | noise |
| 3 · opening ranges only | 2006 | -254 | -88 | -0.8 | -162 / +50 / +24 | worse |
| 6 · flip ER min 0.15 | 2419 | -175 | -9 | -0.1 | +9 / -7 / -12 | worse |
| 6 · flip ER min 0.20 | 2376 | -183 | -17 | -0.4 | -17 / -9 / +9 | worse |
| 6 · flip ER min 0.26 | 2301 | -196 | -30 | -0.5 | -7 / -32 / +9 | worse |
| 6 · flip ER min 0.30 | 2248 | -183 | -17 | -0.2 | -12 / -8 / +3 | worse |
| 6 · flip ER min 0.35 | 2185 | -123 | +43 | +0.4 | +8 / +15 / +20 | noise |
| 6 · flip ER min 0.40 | 2141 | -53 | +113 | +0.9 | -1 / +75 / +39 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 2239 | -32 | +134 | +0.9 | -25 / +51 / +109 | noise |
| 7 · flip: + 15m ER >= 0.30 | 2151 | -41 | +125 | +1.0 | -20 / +28 / +117 | noise |
| 7 · flip: + 15m ER >= 0.40 | 2097 | -16 | +150 | +1.1 | -45 / +74 / +121 | noise |
| 8 · flip: + ER rising | 2295 | -156 | +10 | +0.2 | +7 / +19 / -15 | noise |

## Candidates (robust / promising)

- MGC 3m: 1 · breakout window 5 bars (+111 pts, z +1.2, promising)


## Comparison with previous report and recommendation

Previous report: 11/09 17:29 ET (bars to 11/09, first run on the 11/08-synced scripts). This run: bars to 11/12, same scripts and settings -- differences come only from the 11/10-11/12 bars. Week of 11/09, run 2 (the task now runs Tue/Thu/Fri; streaks still count one check per week).

| Case | Current net 11/09 → 11/12 | Change | 3-week count | Robust / promising rows now | Movement vs 11/09 |
|---|---|---|---|---|---|
| MGC 3m | +511 → +543 | +6 % | continues (week of 11/09) | 1 · breakout window 5 bars: promising (+111, z +1.2, +77 / +0 / +33) | 5-bar window +103 z 1.1 → +111 z 1.2 (Apr–Jun still only +0); flip ER 0.40 +110 → +109 (z 0.9, noise); prior-day H/L -20 (unchanged, worse); 1-bar window -104 → -135, clean break -133 (still worse) |
| MES 3m | +41 → +53 | +12 pts (+29 %, under 30 %) | continues | none | flip ER 0.40 +94 → +120 (z 1.0, Jul–now -43, noise); "+15m ER ≥ 0.40" +168 z 1.2, Jul–now -46 (unchanged, noise); breakout windows all still worse |
| MGC 2m | +502 → +507 | +1 % | continues | none | flip ER 0.20 / 0.26 z 0.9 (Jan–Mar slightly negative, noise); OR-only z -2.5, 1-bar window z -2.3, prior-day H/L z -2.0 (still worse) |
| MES 2m | -152 → -166 | -9 % | continues | none | "+15m ER ≥ 0.40" +146 → +150, z 1.1, Jan–Mar -45 (noise, same pattern); flip ER 0.35 now better in all thirds but z 0.4 |

**Recommendation: no change yet.** No variant is robust (z ≥ 2 and all thirds better) in any case. Only promising row: MGC 3m "breakout window 5 bars" (+111, z +1.2) -- promising, not robust, and its Apr–Jun gain is +0, so it does not start a robust streak. All flip-ER variants stay below z 1.3.

Robust-streak tracker: none active. (MGC 3m · levels + prior-day H/L: weeks of 10/26 #1, 11/02 #2, failed 11/09 under the synced exits; still worse on 11/12 at -20.)
Promising watch: MGC 3m · breakout window 5 bars -- promising 11/09 (z 1.1) and 11/12 (z 1.2), both in the week of 11/09.
