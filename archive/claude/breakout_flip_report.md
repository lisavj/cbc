# Breakout exception + flip-ER variant study -- 2026-11-12 17:28 ET

Settings check: claude/settings_sync_report.md (11/12 16:47 ET) -- newest Pine v10.93 (v10.88-v10.93 are all ▶ Bot changes: trigger set + flip-only bot exits 09:30-16:00), 0 MISMATCH, 1 known (late_study MGCX runner base; not used here). chop_sim EXIT / GATE all MATCH. The new bot rules do not touch the chart setups this study replays. Study settings current.

Run note: third run in the week of 11/09 (after 11/09 17:29 and 11/12 09:57 ET). Same scripts and settings as the 11/12 morning run; differences come only from the rest of the 11/12 session's bars. Does not add a new weekly check to any streak.

Simulator: chop_sim.py (approximates CBC v10.36: about 50 % of real setups matched exactly, so compare variants, not absolute numbers). z = change / (per-trade SD × √setups changed); "robust" = z ≥ 2 and better in all three thirds, "promising" = z ≥ 1 and all thirds better. About 100 settings have now been tried across the studies, so expect a few z ≈ 2 results by chance.

## MGC 3m — 01/05 to 11/12, current rule 1142 setups, net +539 pts (thirds +282 / +8 / +249), per-trade SD 8.5

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 989 | +405 | -135 | -1.0 | -84 / +33 / -83 | worse |
| 1 · breakout window 2 bars | 1091 | +492 | -48 | -0.6 | -55 / -4 / +11 | worse |
| 1 · breakout window 5 bars | 1201 | +650 | +111 | +1.2 | +77 / +0 / +33 | promising |
| 1 · breakout window 8 bars | 1254 | +543 | +4 | +0.0 | +26 / -8 / -14 | noise |
| 2 · clean break (>= 0.25 ATR beyond) | 1090 | +407 | -133 | -1.6 | -127 / +7 / -14 | worse |
| 2 · breakout candle volume >= 1.2x avg | 961 | +395 | -144 | -1.0 | -39 / -14 / -91 | worse |
| 3 · levels + prior-day H/L | 1158 | +520 | -20 | -0.5 | -10 / -6 / -3 | worse |
| 3 · levels + PP/R1/S1 | 1155 | +516 | -23 | -0.6 | -16 / +0 / -7 | worse |
| 3 · swings only | 1083 | +599 | +59 | +0.7 | +26 / +43 / -10 | noise |
| 3 · opening ranges only | 1000 | +410 | -129 | -1.0 | -29 / -55 / -46 | worse |
| 6 · flip ER min 0.15 | 1169 | +464 | -76 | -1.0 | -53 / -19 / -3 | worse |
| 6 · flip ER min 0.20 | 1153 | +524 | -15 | -0.3 | -6 / +3 / -11 | worse |
| 6 · flip ER min 0.26 | 1133 | +570 | +31 | +0.7 | +19 / +9 / +3 | noise |
| 6 · flip ER min 0.30 | 1121 | +561 | +21 | +0.3 | +2 / +23 / -4 | noise |
| 6 · flip ER min 0.35 | 1104 | +572 | +33 | +0.3 | +16 / +19 / -3 | noise |
| 6 · flip ER min 0.40 | 1086 | +649 | +109 | +0.9 | +63 / +40 / +6 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 1099 | +597 | +57 | +0.4 | +54 / +50 / -46 | noise |
| 7 · flip: + 15m ER >= 0.30 | 1072 | +625 | +85 | +0.7 | +88 / +22 / -25 | noise |
| 7 · flip: + 15m ER >= 0.40 | 1055 | +589 | +50 | +0.4 | +106 / +17 / -73 | noise |
| 8 · flip: + ER rising | 1132 | +554 | +15 | +0.3 | -9 / +33 / -9 | noise |

## MES 3m — 01/05 to 11/12, current rule 1736 setups, net +77 pts (thirds +171 / -382 / +288), per-trade SD 7.2

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 1477 | -57 | -134 | -0.9 | -72 / -54 / -8 | worse |
| 1 · breakout window 2 bars | 1648 | -20 | -98 | -1.1 | -40 / -42 / -15 | worse |
| 1 · breakout window 5 bars | 1830 | -58 | -135 | -1.5 | -56 / -61 / -18 | worse |
| 1 · breakout window 8 bars | 1904 | -136 | -214 | -1.7 | -157 / -78 / +21 | worse |
| 2 · clean break (>= 0.25 ATR beyond) | 1658 | +78 | +1 | +0.0 | +39 / +4 / -43 | noise |
| 2 · breakout candle volume >= 1.2x avg | 1452 | -18 | -96 | -0.6 | -62 / -28 / -6 | worse |
| 3 · levels + prior-day H/L | 1746 | +48 | -30 | -1.0 | +1 / -14 / -16 | worse |
| 3 · levels + PP/R1/S1 | 1749 | +71 | -6 | -0.2 | -6 / +27 / -28 | worse |
| 3 · swings only | 1662 | +30 | -47 | -0.6 | -28 / +1 / -21 | worse |
| 3 · opening ranges only | 1463 | -35 | -112 | -0.8 | -50 / -58 / -5 | worse |
| 6 · flip ER min 0.15 | 1768 | +110 | +33 | +0.4 | -7 / +58 / -18 | noise |
| 6 · flip ER min 0.20 | 1747 | +54 | -23 | -0.5 | -51 / +21 / +6 | worse |
| 6 · flip ER min 0.26 | 1717 | +69 | -9 | -0.2 | +22 / -13 / -18 | worse |
| 6 · flip ER min 0.30 | 1697 | +100 | +22 | +0.3 | +54 / +23 / -55 | noise |
| 6 · flip ER min 0.35 | 1671 | +152 | +74 | +0.7 | +99 / +71 / -96 | noise |
| 6 · flip ER min 0.40 | 1645 | +198 | +120 | +1.0 | +111 / +53 / -43 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 1687 | +163 | +86 | +0.6 | +16 / +88 / -18 | noise |
| 7 · flip: + 15m ER >= 0.30 | 1646 | +206 | +129 | +1.1 | +86 / +50 / -8 | noise |
| 7 · flip: + 15m ER >= 0.40 | 1620 | +245 | +168 | +1.2 | +117 / +97 / -46 | noise |
| 8 · flip: + ER rising | 1720 | +85 | +7 | +0.1 | +6 / -6 / +8 | noise |

## MGC 2m — 01/05 to 11/12, current rule 2595 setups, net +511 pts (thirds +87 / +176 / +247), per-trade SD 5.2

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 2254 | +223 | -287 | -2.3 | -40 / -173 / -74 | worse |
| 1 · breakout window 2 bars | 2453 | +363 | -148 | -1.8 | -39 / -79 / -31 | worse |
| 1 · breakout window 5 bars | 2755 | +572 | +61 | +0.7 | +52 / -9 / +18 | noise |
| 1 · breakout window 8 bars | 2884 | +560 | +49 | +0.4 | +148 / -69 / -30 | noise |
| 2 · clean break (>= 0.25 ATR beyond) | 2477 | +448 | -63 | -0.8 | -84 / -5 / +26 | worse |
| 2 · breakout candle volume >= 1.2x avg | 2147 | +262 | -249 | -1.8 | -108 / -136 / -4 | worse |
| 3 · levels + prior-day H/L | 2612 | +454 | -56 | -2.0 | +4 / -22 / -38 | worse |
| 3 · levels + PP/R1/S1 | 2614 | +508 | -3 | -0.1 | -6 / +9 / -5 | worse |
| 3 · swings only | 2503 | +503 | -8 | -0.1 | -53 / +1 / +44 | worse |
| 3 · opening ranges only | 2146 | +162 | -349 | -2.5 | -140 / -127 / -83 | worse |
| 6 · flip ER min 0.15 | 2659 | +573 | +63 | +0.8 | -35 / +52 / +45 | noise |
| 6 · flip ER min 0.20 | 2623 | +551 | +40 | +0.9 | -4 / +30 / +14 | noise |
| 6 · flip ER min 0.26 | 2558 | +558 | +47 | +0.9 | -6 / +36 / +17 | noise |
| 6 · flip ER min 0.30 | 2520 | +567 | +57 | +0.7 | +22 / +37 / -3 | noise |
| 6 · flip ER min 0.35 | 2486 | +560 | +49 | +0.5 | +17 / +63 / -30 | noise |
| 6 · flip ER min 0.40 | 2444 | +565 | +54 | +0.5 | +51 / +67 / -64 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 2536 | +514 | +4 | +0.0 | +49 / +13 / -58 | noise |
| 7 · flip: + 15m ER >= 0.30 | 2462 | +560 | +50 | +0.4 | +73 / +38 / -61 | noise |
| 7 · flip: + 15m ER >= 0.40 | 2422 | +527 | +16 | +0.1 | +81 / +2 / -67 | noise |
| 8 · flip: + ER rising | 2543 | +513 | +2 | +0.0 | +16 / +4 / -19 | noise |

## MES 2m — 01/05 to 11/12, current rule 2347 setups, net -182 pts (thirds +65 / -61 / -185), per-trade SD 4.7

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| 1 · breakout window 1 bar | 2097 | -188 | -6 | -0.1 | -87 / -15 / +95 | worse |
| 1 · breakout window 2 bars | 2256 | -205 | -23 | -0.4 | -41 / -19 / +37 | worse |
| 1 · breakout window 5 bars | 2449 | -143 | +39 | +0.6 | -36 / +50 / +25 | noise |
| 1 · breakout window 8 bars | 2533 | -223 | -41 | -0.4 | -89 / +31 / +17 | worse |
| 2 · clean break (>= 0.25 ATR beyond) | 2267 | -201 | -20 | -0.3 | +12 / -41 / +9 | worse |
| 2 · breakout candle volume >= 1.2x avg | 2022 | -387 | -206 | -1.9 | -148 / -78 / +21 | worse |
| 3 · levels + prior-day H/L | 2358 | -182 | -1 | -0.0 | -14 / +8 / +6 | worse |
| 3 · levels + PP/R1/S1 | 2358 | -170 | +12 | +0.5 | +4 / +12 / -4 | noise |
| 3 · swings only | 2284 | -141 | +41 | +0.8 | +23 / -30 / +48 | noise |
| 3 · opening ranges only | 2008 | -270 | -88 | -0.8 | -162 / +50 / +24 | worse |
| 6 · flip ER min 0.15 | 2421 | -191 | -9 | -0.1 | +9 / -7 / -12 | worse |
| 6 · flip ER min 0.20 | 2378 | -199 | -17 | -0.4 | -17 / -9 / +9 | worse |
| 6 · flip ER min 0.26 | 2303 | -212 | -30 | -0.5 | -7 / -32 / +9 | worse |
| 6 · flip ER min 0.30 | 2250 | -198 | -17 | -0.2 | -12 / -8 / +3 | worse |
| 6 · flip ER min 0.35 | 2187 | -139 | +43 | +0.4 | +8 / +15 / +20 | noise |
| 6 · flip ER min 0.40 | 2143 | -69 | +113 | +0.9 | -1 / +75 / +39 | noise |
| 7 · flip: 15m ER >= 0.30 instead of ER12 | 2241 | -47 | +134 | +0.9 | -25 / +51 / +109 | noise |
| 7 · flip: + 15m ER >= 0.30 | 2153 | -57 | +125 | +1.0 | -20 / +28 / +117 | noise |
| 7 · flip: + 15m ER >= 0.40 | 2099 | -32 | +150 | +1.1 | -45 / +74 / +121 | noise |
| 8 · flip: + ER rising | 2297 | -172 | +10 | +0.2 | +7 / +19 / -15 | noise |

## Candidates (robust / promising)

- MGC 3m: 1 · breakout window 5 bars (+111 pts, z +1.2, promising)


## Comparison with previous report and recommendation

Previous report: 11/12 09:57 ET (bars to 11/12 morning). This run: bars to 11/12 ~17:25 ET, same scripts.

| Case | Current net 11/12 AM → 11/12 PM | Change | 3-week count | Robust / promising rows now | Movement vs 11/12 AM |
|---|---|---|---|---|---|
| MGC 3m | +543 → +539 | -1 % | continues | 1 · breakout window 5 bars: promising (+111, z +1.2, +77 / +0 / +33) | unchanged (+111, z 1.2, Apr–Jun still +0); flip ER 0.40 +109 (z 0.9, noise); prior-day H/L -20 (worse) |
| MES 3m | +53 → +77 | +24 pts (+45 % on a small base; one afternoon of bars, not a script/baseline change) | no streak active, nothing to restart | none | "+15m ER ≥ 0.40" +168 z 1.2, Jul–now -46 (noise, unchanged); flip ER 0.40 +120 z 1.0, Jul–now -43; breakout windows all still worse |
| MGC 2m | +507 → +511 | +1 % | continues | none | flip ER 0.20 / 0.26 z 0.9 (Jan–Mar slightly negative); flip ER 0.30 dropped to Jul–now -3; OR-only z -2.5, 1-bar window z -2.3, prior-day H/L z -2.0 (still worse) |
| MES 2m | -166 → -182 | -10 % | continues | none | "+15m ER ≥ 0.40" +150 z 1.1, Jan–Mar -45 (noise, same pattern); flip ER 0.35 better in all thirds but z 0.4 |

**Recommendation: no change yet.** No variant is robust (z ≥ 2 and all thirds better) in any case. Only promising row: MGC 3m "breakout window 5 bars" (+111, z +1.2), Apr–Jun gain +0, so not robust.

Robust-streak tracker: none active. (MGC 3m · levels + prior-day H/L: weeks of 10/26 #1, 11/02 #2, failed 11/09 under the synced exits; still worse at -20.)
Promising watch: MGC 3m · breakout window 5 bars -- promising 11/09 (z 1.1), 11/12 AM and PM (z 1.2), all in the week of 11/09.
