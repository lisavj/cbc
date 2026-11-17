## Week of 11/14/2026 summary

- STUDY SETTINGS STALE: the 11/13 settings sync (v10.96) lists 3 non-known MISMATCHes, NOT yet fixed in the project scripts, and they touch the 3m studies -- mes3_ema_grid LIVE still closes MES 3m 80/100 % by time of day (live since v10.95: 100 % at TP1 all day), and MGC 3m live is now FLIP 0 % (v10.96: nothing closed at TP1, BE, no trail, exit on HTF flip) while these replays use 80 % / trail 1.7 (MGCX) or 50 % / 3.5. Bot replay (H) is unaffected (part 1.0). Also new: the 11/14 X4 fix in mes3_ema_grid.py makes the MGC 3m VWAP-stretch gate actually block setups (MGC 3m 1193 setups vs 1707 last week), so MGC 3m numbers are not like-for-like with 11/09.
- Current exits after costs (to 11/13): MES -822 (11/09 -847) / MGC +55 (11/09 -129; stretch gate now applied) / MNQ -2075 (-1627) / M2K -598 (-604).
- Walk-forward last third: MES -144 / MGC +9 (with TP rule; SL-only pick -19) / MNQ -92 / M2K -60 (11/09: -85 / -14 / -92 / -84).
- MGC watch "cut if wrong side of HTF EMA9 at 18 min": **+63 after costs, z 1.25, thirds +26 / +6 / +31, last 4 wk +17, neighbours 15 / 21 min +14 / +45 -> T4R, promising** (11/09 +87 T4R z 1.6). Third week promising in a row (11/07, 11/09, 11/14), BUT the walk-forward pick is a different rule (SL-only last third -19) and the replay runs MGC 3m on 80 % / 1.7 exits, not the live FLIP 0 % -> NOT recommended yet; rerun on FLIP 0 % exits first.
- Best per chart: MES half SL1 if wrong side of HTF EMA9 at 18 min + TP rule +180 (z 1.0, third 3 -1, no flags); MGC same rule +92 (z 1.1, third 2 -12); MNQ BE if never reached 25 % at 18 min +162 (third 1 -33); M2K +8 -- none robust.
- Verdict per chart: keep current exits on all four.

---

# Early-exit lab — 3m charts — 11/14/2026 23:37

## Summary

- MES 3m: best half SL1 if wrong side of HTF EMA9 at 18 min + TP rule → +180 after costs (z +1.0, no flags); walk-forward last third **-144**
- MGC 3m: best half SL1 if wrong side of HTF EMA9 at 18 min + TP rule → +92 after costs (z +1.1, 4); walk-forward last third **+9**
- MNQ 3m: best SL1 to BE if never reached 25 % at 18 min → +162 after costs (z +0.6, 4); walk-forward last third **-92**
- M2K 3m: best half SL1 if wrong side of HTF EMA9 at 1st 15m close → +8 after costs (z +0.2, 4); walk-forward last third **-60**


Early-exit lab -- 3m charts MES, MGC, MNQ, M2K -- 11/07/2026.
Follow-up to the time-stop and TP+SL combo studies. One replay that tests, together:
 1. CHECK TIME: fixed X min after entry (12/15/18/21/24) vs the HTF (15m) candle close -- H1 = first 15m close after entry,
    H1+ = first 15m close at least 12 min after entry, H2 = second 15m close.
 2. COSTS: every result is shown gross and after costs. Cost per trade = round-trip commission (~$1.24 / micro) + 1 tick entry
    slippage; a rule exit at the candle close (market order) pays 1 more tick. MES 0.25+0.25 / MGC 0.12+0.10 / MNQ 0.62+0.25 /
    M2K 0.25+0.10 pts per trade; tick MES .25 / MGC .1 / MNQ .25 / M2K .1. Extra trades (re-entries after a cut) pay too.
 3. WALK-FORWARD: the best rule is chosen on the first two thirds of the period only (after costs), then scored on the last third.
 4. CONDITION at the check (before TP1 only): neg = close at / beyond Entry against; <25 % / <50 % = close less than that share
    of the way to TP1; h9 = close on the wrong side of the HTF EMA9; mfe25 / mfe50 = the best price so far never reached
    25 / 50 % of TP1 ("never got going").
    ACTION: CUT = close at that close; HALF = SL1 to half its distance; BE = SL1 to Entry (close now if already past it).
 5. SPLIT: Δ by session (NY 09:30-16:00 vs rest) and by trigger (HTF flip vs others) for the top rules.
 6. RE-ENTRY: trades that start within 30 min after a cut in the same direction -- count, net, avg vs all trades.
 7. BOT GUARDS (post-hoc on the trade list, after costs): stop for the rest of the session (18:00-18:00 ET) after K losses in
    a row or after the session is down L points (L = 1 / 2 / 3 x the average full SL1 loss).
MES 3m and MGC 3m are also run with the best TP-reduction rule on top (MES TP1 -> 85 % after 18 min, MGC -> 65 % after 21 min).
Replay = chop_sim rules (late window 1, NY OR block 30) on live exits: MES 3m SL1 3 ATR min 5, TP1 1.75 ATR, 80/100 % by time
of day; MGC 3m MGCX; MNQ / M2K 3m CBC defaults. Jan 5 -> now. Flags: T = better in all three thirds, 4 = better in the last
4 weeks, R = T and both time neighbours (±3 min) better (fixed-time rows only). z = Δ / (SD x sqrt(setups changed)).

## MES 3m — current exits: 1738 setups to 11/13, net +47 gross / -822 after costs (0.50 pts per trade)

**1. When to check — best rule per check time (after costs; no TP rule)**

| Check | Best rule | Δ after costs | Gross | Thirds | Last 4 wk | Positive rules |
|---|---|---|---|---|---|---|
| 12 min | half SL1 if wrong side of HTF EMA9 | -19  | +5 | +45 / +1 / -65 | -49.7 | 0 / 17 |
| 15 min | half SL1 if wrong side of HTF EMA9 | -26  | -4 | -2 / +1 / -25 | -25.2 | 0 / 17 |
| 18 min | half SL1 if wrong side of HTF EMA9 | +37 T4 | +54 | +16 / +18 / +3 | +7.5 | 3 / 17 |
| 21 min | half SL1 if wrong side of HTF EMA9 | -7  | +13 | +10 / +16 / -33 | -8.9 | 0 / 17 |
| 24 min | half SL1 if never reached 25 % | -30  | -22 | +16 / +14 / -59 | -55.8 | 0 / 17 |
| 1st 15m close | half SL1 if wrong side of HTF EMA9 | +10  | +35 | +22 / +16 / -28 | -27.3 | 1 / 17 |
| 1st 15m close >= 12 min | half SL1 if wrong side of HTF EMA9 | -33  | -5 | -14 / +10 / -29 | -31.6 | 0 / 17 |
| 2nd 15m close | half SL1 if never reached 25 % | -7  | +6 | +3 / +15 / -24 | -21.3 | 0 / 17 |

**4. Which condition — best per condition (any check time / action, no TP rule)**

| Condition | Best rule | Δ after costs | Gross | Positive rules |
|---|---|---|---|---|
| negative | half SL1 if negative at 18 min | +31  | +66 | 1 / 16 |
| < 25 % of TP1 | half SL1 if < 25 % of TP1 at 18 min | +18  | +54 | 1 / 24 |
| < 50 % of TP1 | half SL1 if < 50 % of TP1 at 18 min | -9  | +28 | 0 / 24 |
| wrong side of HTF EMA9 | half SL1 if wrong side of HTF EMA9 at 18 min | +37 T4 | +54 | 2 / 24 |
| never reached 25 % | half SL1 if never reached 25 % at 2nd 15m close | -7  | +6 | 0 / 24 |
| never reached 50 % | half SL1 if never reached 50 % at 18 min | -17  | +10 | 0 / 24 |

**2. Costs:** 22 of 136 rules are better gross, 4 after costs. Avg cost of the rules: -115 pts.

**Top 8 rules after costs** (incl. with the TP rule where run)

1. half SL1 if wrong side of HTF EMA9 at 18 min + TP rule: **+180** after costs (gross +234) (z +1.0, thirds +93 / +88 / -1, last 4 wk -57.3, 61 cuts, +78 trades)
2. half SL1 if wrong side of HTF EMA9 at 1st 15m close + TP rule: **+159** after costs (gross +220) (z +0.9, thirds +96 / +85 / -22, last 4 wk -72.6, 87 cuts, +78 trades)
3. half SL1 if negative at 18 min + TP rule: **+154** after costs (gross +226) (z +0.8, thirds +114 / +112 / -72, last 4 wk -113.1, 82 cuts, +103 trades)
4. half SL1 if < 25 % of TP1 at 18 min + TP rule: **+140** after costs (gross +213) (z +0.7, thirds +128 / +114 / -102, last 4 wk -134.1, 82 cuts, +104 trades)
5. half SL1 if wrong side of HTF EMA9 at 21 min + TP rule: **+138** after costs (gross +195) (z +0.8, thirds +89 / +82 / -32, last 4 wk -68.3, 72 cuts, +78 trades)
6. half SL1 if never reached 50 % at 18 min + TP rule: **+138** after costs (gross +202) (z +0.7, thirds +134 / +102 / -98, last 4 wk -131.9, 66 cuts, +95 trades)
7. half SL1 if wrong side of HTF EMA9 at 12 min + TP rule: **+132** after costs (gross +192) (z +0.7, thirds +126 / +55 / -49, last 4 wk -88.5, 84 cuts, +78 trades)
8. half SL1 if never reached 25 % at 18 min + TP rule: **+132** after costs (gross +183) (z +0.7, thirds +106 / +87 / -61, last 4 wk -93.2, 38 cuts, +83 trades)

TP rule alone (TP1 -> 85 % after 18 min): +160 after costs, thirds +75 / +76 / +10, last 4 wk -50.9.

**3. Walk-forward** (choose on the first two thirds, test on the last third, after costs)

- SL rules only: picked on thirds 1-2 = **half SL1 if < 50 % of TP1 at 18 min** (+129 in-sample) → last third **-138** (rank 66 of 136; median rule -143; current exits 0)
- with TP rule: picked on thirds 1-2 = **half SL1 if < 50 % of TP1 at 18 min** (+258 in-sample) → last third **-144** (rank 75 of 136; median rule -132; current exits 0)

**5. Split by session / trigger** (Δ after costs)

| Rule | NY 09:30-16:00 | Other hours | HTF flip | Other triggers |
|---|---|---|---|---|
| half SL1 if wrong side of HTF EMA9 at 18 min | +63 | -27 | +26 | +10 |
| half SL1 if negative at 18 min | +120 | -90 | +75 | -45 |
| half SL1 if < 25 % of TP1 at 18 min | +113 | -95 | +99 | -81 |

**6. Re-entry after a cut** (next same-direction trade starting within 30 min after the cut)

- half SL1 if wrong side of HTF EMA9 at 18 min: 58 cuts → 3 re-entries, net -19, avg -6.21 vs all trades -0.45
- half SL1 if negative at 18 min: 79 cuts → 5 re-entries, net -18, avg -3.66 vs all trades -0.45
- half SL1 if < 25 % of TP1 at 18 min: 79 cuts → 5 re-entries, net -18, avg -3.66 vs all trades -0.45

**7. Session guards** (skip the rest of the session after K losses in a row or after −L pts; avg full SL1 loss 10.6 pts)

| Guard | on current exits | beyond random skipping* | on best rule (half SL1 if wrong side of HTF EMA9 at 18 min) |
|---|---|---|---|
| 2 losses in a row | +493  (thirds +49 / +450 / -6, last 4 wk -141.1, 696 skipped) | **+164** | +444 vs rule alone |
| 2 losses in a row + −3 x SL1 (32 pts) | +493  (thirds +49 / +450 / -6, last 4 wk -141.1, 696 skipped) | **+164** | +444 vs rule alone |
| −3 x SL1 (32 pts) | +161 T (thirds +50 / +83 / +28, last 4 wk +0.0, 41 skipped) | **+142** | +127 vs rule alone |
| 2 losses in a row + −2 x SL1 (21 pts) | +458  (thirds +22 / +442 / -6, last 4 wk -141.1, 704 skipped) | **+125** | +408 vs rule alone |
| 2 losses in a row + −1 x SL1 (11 pts) | +445  (thirds -5 / +454 / -4, last 4 wk -141.9, 739 skipped) | **+95** | +411 vs rule alone |
| 3 losses in a row + −3 x SL1 (32 pts) | +212  (thirds +21 / +259 / -68, last 4 wk -217.9, 330 skipped) | **+56** | +213 vs rule alone |
| 3 losses in a row | +200  (thirds +9 / +259 / -68, last 4 wk -217.9, 328 skipped) | **+45** | +201 vs rule alone |
| 4 losses in a row + −3 x SL1 (32 pts) | +30  (thirds -10 / +61 / -21, last 4 wk -90.3, 149 skipped) | **-40** | -24 vs rule alone |
| 3 losses in a row + −2 x SL1 (21 pts) | +115  (thirds -64 / +262 / -82, last 4 wk -212.9, 351 skipped) | **-51** | +117 vs rule alone |
| −2 x SL1 (21 pts) | -1  (thirds -22 / +75 / -55, last 4 wk -82.2, 139 skipped) | **-67** | -3 vs rule alone |
| 4 losses in a row | -22  (thirds -57 / +66 / -32, last 4 wk -90.3, 138 skipped) | **-87** | -63 vs rule alone |
| 3 losses in a row + −1 x SL1 (11 pts) | +132  (thirds -35 / +266 / -99, last 4 wk -219.3, 470 skipped) | **-90** | +162 vs rule alone |
| −1 x SL1 (11 pts) | +88  (thirds -7 / +206 / -111, last 4 wk -219.3, 400 skipped) | **-101** | +36 vs rule alone |
| 4 losses in a row + −1 x SL1 (11 pts) | +66  (thirds -15 / +181 / -101, last 4 wk -219.3, 411 skipped) | **-128** | +28 vs rule alone |
| 4 losses in a row + −2 x SL1 (21 pts) | -117  (thirds -87 / +83 / -113, last 4 wk -172.5, 210 skipped) | **-216** | -149 vs rule alone |

*Current exits lose 0.47 pts per trade after costs, so skipping ANY trades looks good. This column = guard result minus what skipping the same number of random trades would give; positive = the guard picks the bad trades.

## MGC 3m — current exits: 1193 setups to 11/13, net +317 gross / +55 after costs (0.22 pts per trade)

**1. When to check — best rule per check time (after costs; no TP rule)**

| Check | Best rule | Δ after costs | Gross | Thirds | Last 4 wk | Positive rules |
|---|---|---|---|---|---|---|
| 12 min | half SL1 if negative | +21 TR | +30 | +10 / +4 / +8 | -14.4 | 3 / 17 |
| 15 min | half SL1 if wrong side of HTF EMA9 | +41 T4 | +46 | +29 / +10 / +1 | +6.3 | 9 / 17 |
| 18 min | cut if negative | +81 T4R | +102 | +38 / +8 / +35 | +23.8 | 16 / 17 |
| 21 min | cut if wrong side of HTF EMA9 | +45 T4R | +52 | +7 / +2 / +37 | +12.3 | 11 / 17 |
| 24 min | half SL1 if negative | +25  | +29 | -4 / +21 / +9 | -24.5 | 13 / 17 |
| 1st 15m close | half SL1 if never reached 25 % | +37 T | +43 | +4 / +6 / +27 | -0.9 | 4 / 17 |
| 1st 15m close >= 12 min | half SL1 if never reached 25 % | +7 4 | +9 | -3 / -16 / +26 | +8.1 | 1 / 17 |
| 2nd 15m close | cut if never reached 25 % | +24  | +26 | -1 / +10 / +15 | -0.1 | 6 / 17 |

**4. Which condition — best per condition (any check time / action, no TP rule)**

| Condition | Best rule | Δ after costs | Gross | Positive rules |
|---|---|---|---|---|
| negative | cut if negative at 18 min | +81 T4R | +102 | 11 / 16 |
| < 25 % of TP1 | cut if < 25 % of TP1 at 18 min | +58 4 | +88 | 9 / 24 |
| < 50 % of TP1 | half SL1 if < 50 % of TP1 at 18 min | +51  | +59 | 8 / 24 |
| wrong side of HTF EMA9 | cut if wrong side of HTF EMA9 at 18 min | +63 T4R | +71 | 13 / 24 |
| never reached 25 % | half SL1 if never reached 25 % at 1st 15m close | +37 T | +43 | 14 / 24 |
| never reached 50 % | half SL1 if never reached 50 % at 1st 15m close | +20  | +30 | 8 / 24 |

**2. Costs:** 78 of 136 rules are better gross, 63 after costs. Avg cost of the rules: -16 pts.

**Top 8 rules after costs** (incl. with the TP rule where run)

1. half SL1 if wrong side of HTF EMA9 at 18 min + TP rule: **+92** after costs (gross +101) 4 (z +1.1, thirds +57 / -12 / +47, last 4 wk +9.0, 26 cuts, +28 trades)
2. SL1 to BE if wrong side of HTF EMA9 at 18 min + TP rule: **+89** after costs (gross +103) 4 (z +1.0, thirds +54 / -11 / +46, last 4 wk +10.6, 71 cuts, +30 trades)
3. cut if wrong side of HTF EMA9 at 18 min + TP rule: **+85** after costs (gross +99) 4 (z +1.0, thirds +54 / -11 / +41, last 4 wk +6.9, 75 cuts, +30 trades)
4. half SL1 if wrong side of HTF EMA9 at 21 min + TP rule: **+84** after costs (gross +92) 4 (z +1.0, thirds +38 / -2 / +47, last 4 wk +9.0, 22 cuts, +28 trades)
5. cut if negative at 18 min: **+81** after costs (gross +102) T4R (z +1.0, thirds +38 / +8 / +35, last 4 wk +23.8, 173 cuts, +17 trades) — promising
6. cut if wrong side of HTF EMA9 at 21 min + TP rule: **+75** after costs (gross +88) 4 (z +0.9, thirds +40 / -12 / +47, last 4 wk +7.3, 65 cuts, +28 trades)
7. cut if wrong side of HTF EMA9 at 24 min + TP rule: **+75** after costs (gross +86) (z +0.9, thirds +46 / -3 / +33, last 4 wk -0.3, 45 cuts, +30 trades)
8. SL1 to BE if wrong side of HTF EMA9 at 24 min + TP rule: **+75** after costs (gross +86) (z +0.9, thirds +46 / -4 / +33, last 4 wk -0.3, 44 cuts, +30 trades)

TP rule alone (TP1 -> 65 % after 21 min): +53 after costs, thirds +35 / +0 / +18, last 4 wk +0.2.

**3. Walk-forward** (choose on the first two thirds, test on the last third, after costs)

- SL rules only: picked on thirds 1-2 = **SL1 to BE if < 50 % of TP1 at 18 min** (+64 in-sample) → last third **-19** (rank 111 of 136; median rule +7; current exits 0)
- with TP rule: picked on thirds 1-2 = **half SL1 if wrong side of HTF EMA9 at 15 min** (+65 in-sample) → last third **+9** (rank 96 of 136; median rule +21; current exits 0)

**5. Split by session / trigger** (Δ after costs)

| Rule | NY 09:30-16:00 | Other hours | HTF flip | Other triggers |
|---|---|---|---|---|
| cut if negative at 18 min | +30 | +51 | +44 | +37 |
| half SL1 if negative at 18 min | +12 | +61 | +31 | +41 |
| cut if wrong side of HTF EMA9 at 18 min | +15 | +48 | +5 | +58 |

**6. Re-entry after a cut** (next same-direction trade starting within 30 min after the cut)

- cut if negative at 18 min: 173 cuts → 16 re-entries, net +5, avg +0.31 vs all trades +0.11
- half SL1 if negative at 18 min: 41 cuts → 1 re-entries, net +5, avg +4.96 vs all trades +0.11
- cut if wrong side of HTF EMA9 at 18 min: 72 cuts → 6 re-entries, net -5, avg -0.91 vs all trades +0.10

**7. Session guards** (skip the rest of the session after K losses in a row or after −L pts; avg full SL1 loss 6.6 pts)

| Guard | on current exits | beyond random skipping* | on best rule (cut if negative at 18 min) |
|---|---|---|---|
| 3 losses in a row + −3 x SL1 (20 pts) | +38  (thirds +68 / +20 / -50, last 4 wk -26.3, 160 skipped) | **+46** | +46 vs rule alone |
| 4 losses in a row | +30  (thirds +37 / -5 / -2, last 4 wk +5.2, 58 skipped) | **+32** | +23 vs rule alone |
| 3 losses in a row | +24  (thirds +61 / +20 / -57, last 4 wk -26.3, 158 skipped) | **+31** | +46 vs rule alone |
| 4 losses in a row + −3 x SL1 (20 pts) | -2  (thirds +21 / -5 / -18, last 4 wk +5.2, 86 skipped) | **+2** | -27 vs rule alone |
| 2 losses in a row + −1 x SL1 (7 pts) | -27  (thirds +83 / -79 / -31, last 4 wk -56.9, 494 skipped) | **-4** | -35 vs rule alone |
| −3 x SL1 (20 pts) | -8  (thirds +16 / -4 / -20, last 4 wk +0.0, 55 skipped) | **-6** | -37 vs rule alone |
| −1 x SL1 (7 pts) | -30  (thirds +51 / -49 / -32, last 4 wk -57.9, 418 skipped) | **-11** | -18 vs rule alone |
| 4 losses in a row + −1 x SL1 (7 pts) | -30  (thirds +51 / -49 / -32, last 4 wk -57.9, 418 skipped) | **-11** | -20 vs rule alone |
| 3 losses in a row + −1 x SL1 (7 pts) | -42  (thirds +48 / -42 / -48, last 4 wk -56.7, 432 skipped) | **-22** | -11 vs rule alone |
| 2 losses in a row + −2 x SL1 (13 pts) | -41  (thirds +48 / -87 / -2, last 4 wk -24.4, 403 skipped) | **-23** | -39 vs rule alone |
| 2 losses in a row | -46  (thirds +44 / -87 / -2, last 4 wk -24.4, 400 skipped) | **-27** | -43 vs rule alone |
| 2 losses in a row + −3 x SL1 (20 pts) | -46  (thirds +44 / -87 / -2, last 4 wk -24.4, 400 skipped) | **-27** | -43 vs rule alone |
| 3 losses in a row + −2 x SL1 (13 pts) | -80  (thirds -24 / -7 / -49, last 4 wk -26.3, 231 skipped) | **-69** | -35 vs rule alone |
| 4 losses in a row + −2 x SL1 (13 pts) | -90  (thirds -49 / -20 / -21, last 4 wk -9.5, 189 skipped) | **-82** | -69 vs rule alone |
| −2 x SL1 (13 pts) | -96  (thirds -55 / -20 / -21, last 4 wk -9.5, 183 skipped) | **-87** | -69 vs rule alone |

*Current exits lose -0.05 pts per trade after costs, so skipping ANY trades looks good. This column = guard result minus what skipping the same number of random trades would give; positive = the guard picks the bad trades.

## MNQ 3m — current exits: 1969 setups to 11/13, net -362 gross / -2075 after costs (0.87 pts per trade)

**1. When to check — best rule per check time (after costs; no TP rule)**

| Check | Best rule | Δ after costs | Gross | Thirds | Last 4 wk | Positive rules |
|---|---|---|---|---|---|---|
| 12 min | half SL1 if never reached 25 % | +130 4 | +155 | -69 / +174 / +25 | +36.0 | 1 / 17 |
| 15 min | half SL1 if never reached 25 % | +38 4 | +59 | -36 / +109 / -35 | +30.0 | 1 / 17 |
| 18 min | SL1 to BE if never reached 25 % | +162 4 | +195 | -33 / +164 / +32 | +28.8 | 8 / 17 |
| 21 min | cut if never reached 50 % | +38 4 | +122 | -56 / +125 / -31 | +146.2 | 1 / 17 |
| 24 min | cut if never reached 50 % | +160 4 | +226 | -24 / +253 / -69 | +78.3 | 5 / 17 |
| 1st 15m close | half SL1 if wrong side of HTF EMA9 | -100  | -78 | +13 / +103 / -216 | -45.9 | 0 / 17 |
| 1st 15m close >= 12 min | cut if wrong side of HTF EMA9 | +46  | +79 | -108 / +121 / +33 | -0.7 | 2 / 17 |
| 2nd 15m close | cut if never reached 50 % | +152 4 | +213 | +22 / +223 / -92 | +56.3 | 6 / 17 |

**4. Which condition — best per condition (any check time / action, no TP rule)**

| Condition | Best rule | Δ after costs | Gross | Positive rules |
|---|---|---|---|---|
| negative | half SL1 if negative at 15 min | -21 4 | +27 | 0 / 16 |
| < 25 % of TP1 | half SL1 if < 25 % of TP1 at 18 min | -230 4 | -178 | 0 / 24 |
| < 50 % of TP1 | cut if < 50 % of TP1 at 24 min | -228 4 | -47 | 0 / 24 |
| wrong side of HTF EMA9 | cut if wrong side of HTF EMA9 at 18 min | +79 4 | +111 | 7 / 24 |
| never reached 25 % | SL1 to BE if never reached 25 % at 18 min | +162 4 | +195 | 7 / 24 |
| never reached 50 % | cut if never reached 50 % at 24 min | +160 4 | +226 | 10 / 24 |

**2. Costs:** 30 of 136 rules are better gross, 24 after costs. Avg cost of the rules: -91 pts.

**Top 8 rules after costs** (incl. with the TP rule where run)

1. SL1 to BE if never reached 25 % at 18 min: **+162** after costs (gross +195) 4 (z +0.6, thirds -33 / +164 / +32, last 4 wk +28.8, 68 cuts, +18 trades)
2. cut if never reached 50 % at 24 min: **+160** after costs (gross +226) 4 (z +0.4, thirds -24 / +253 / -69, last 4 wk +78.3, 148 cuts, +33 trades)
3. cut if never reached 25 % at 18 min: **+153** after costs (gross +189) 4 (z +0.5, thirds -21 / +171 / +4, last 4 wk +28.8, 81 cuts, +18 trades)
4. cut if never reached 50 % at 2nd 15m close: **+152** after costs (gross +213) 4 (z +0.4, thirds +22 / +223 / -92, last 4 wk +56.3, 143 cuts, +29 trades)
5. half SL1 if never reached 25 % at 12 min: **+130** after costs (gross +155) 4 (z +0.4, thirds -69 / +174 / +25, last 4 wk +36.0, 44 cuts, +16 trades)
6. half SL1 if never reached 50 % at 2nd 15m close: **+114** after costs (gross +133) T4 (z +0.4, thirds +22 / +75 / +16, last 4 wk +47.8, 33 cuts, +13 trades)
7. cut if never reached 50 % at 18 min: **+111** after costs (gross +223) 4 (z +0.2, thirds -46 / +127 / +30, last 4 wk +166.7, 263 cuts, +54 trades)
8. half SL1 if never reached 50 % at 18 min: **+99** after costs (gross +136) 4 (z +0.2, thirds +13 / +106 / -19, last 4 wk +113.8, 56 cuts, +27 trades)

**3. Walk-forward** (choose on the first two thirds, test on the last third, after costs)

- SL rules only: picked on thirds 1-2 = **cut if never reached 50 % at 2nd 15m close** (+244 in-sample) → last third **-92** (rank 64 of 136; median rule -106; current exits 0)

**5. Split by session / trigger** (Δ after costs)

| Rule | NY 09:30-16:00 | Other hours | HTF flip | Other triggers |
|---|---|---|---|---|
| SL1 to BE if never reached 25 % at 18 min | +27 | +135 | +42 | +119 |
| cut if never reached 50 % at 24 min | +126 | +34 | +147 | +13 |
| cut if never reached 25 % at 18 min | +4 | +150 | +23 | +130 |

**6. Re-entry after a cut** (next same-direction trade starting within 30 min after the cut)

- SL1 to BE if never reached 25 % at 18 min: 68 cuts → 13 re-entries, net -20, avg -1.53 vs all trades -0.96
- cut if never reached 50 % at 24 min: 148 cuts → 29 re-entries, net -174, avg -5.99 vs all trades -0.96
- cut if never reached 25 % at 18 min: 81 cuts → 17 re-entries, net -26, avg -1.55 vs all trades -0.97

**7. Session guards** (skip the rest of the session after K losses in a row or after −L pts; avg full SL1 loss 29.6 pts)

| Guard | on current exits | beyond random skipping* | on best rule (SL1 to BE if never reached 25 % at 18 min) |
|---|---|---|---|
| 2 losses in a row + −1 x SL1 (30 pts) | +1800 T (thirds +187 / +532 / +1081, last 4 wk +674.6, 1088 skipped) | **+653** | +1538 vs rule alone |
| 3 losses in a row + −1 x SL1 (30 pts) | +1607 T (thirds +161 / +390 / +1055, last 4 wk +663.6, 910 skipped) | **+647** | +1438 vs rule alone |
| −1 x SL1 (30 pts) | +1523 T (thirds +208 / +291 / +1024, last 4 wk +701.4, 869 skipped) | **+607** | +1306 vs rule alone |
| 3 losses in a row + −3 x SL1 (89 pts) | +1149 T (thirds +46 / +348 / +755, last 4 wk +456.9, 521 skipped) | **+600** | +1233 vs rule alone |
| 3 losses in a row | +1087 T (thirds +46 / +317 / +724, last 4 wk +426.1, 519 skipped) | **+540** | +1172 vs rule alone |
| 4 losses in a row + −1 x SL1 (30 pts) | +1461 T (thirds +94 / +291 / +1076, last 4 wk +701.4, 881 skipped) | **+533** | +1285 vs rule alone |
| 4 losses in a row + −3 x SL1 (89 pts) | +762  (thirds -174 / +483 / +454, last 4 wk +293.4, 284 skipped) | **+463** | +771 vs rule alone |
| −3 x SL1 (89 pts) | +602  (thirds -77 / +242 / +437, last 4 wk +316.2, 207 skipped) | **+384** | +466 vs rule alone |
| 4 losses in a row + −2 x SL1 (59 pts) | +758  (thirds +232 / -0 / +526, last 4 wk +432.5, 488 skipped) | **+243** | +1012 vs rule alone |
| 4 losses in a row | +463  (thirds -185 / +308 / +339, last 4 wk +174.9, 238 skipped) | **+212** | +503 vs rule alone |
| −2 x SL1 (59 pts) | +681  (thirds +382 / -144 / +443, last 4 wk +432.5, 460 skipped) | **+196** | +906 vs rule alone |
| 3 losses in a row + −2 x SL1 (59 pts) | +798  (thirds +129 / -8 / +677, last 4 wk +459.1, 612 skipped) | **+153** | +1209 vs rule alone |
| 2 losses in a row | +1150 T (thirds +280 / +54 / +816, last 4 wk +569.5, 991 skipped) | **+105** | +997 vs rule alone |
| 2 losses in a row + −2 x SL1 (59 pts) | +1150 T (thirds +280 / +54 / +816, last 4 wk +569.5, 991 skipped) | **+105** | +997 vs rule alone |
| 2 losses in a row + −3 x SL1 (89 pts) | +1150 T (thirds +280 / +54 / +816, last 4 wk +569.5, 991 skipped) | **+105** | +997 vs rule alone |

*Current exits lose 1.05 pts per trade after costs, so skipping ANY trades looks good. This column = guard result minus what skipping the same number of random trades would give; positive = the guard picks the bad trades.

## M2K 3m — current exits: 1970 setups to 11/13, net +92 gross / -598 after costs (0.35 pts per trade)

**1. When to check — best rule per check time (after costs; no TP rule)**

| Check | Best rule | Δ after costs | Gross | Thirds | Last 4 wk | Positive rules |
|---|---|---|---|---|---|---|
| 12 min | half SL1 if wrong side of HTF EMA9 | +3 4 | +11 | -7 / +6 / +3 | +9.2 | 3 / 17 |
| 15 min | cut if wrong side of HTF EMA9 | +7 4 | +26 | -2 / +16 / -7 | +5.4 | 3 / 17 |
| 18 min | cut if wrong side of HTF EMA9 | -37 4 | -17 | -14 / +10 / -33 | +0.8 | 0 / 17 |
| 21 min | half SL1 if never reached 25 % | -29  | -22 | +1 / -7 / -23 | -9.4 | 0 / 17 |
| 24 min | cut if wrong side of HTF EMA9 | -21  | -6 | +0 / +4 / -25 | -2.0 | 0 / 17 |
| 1st 15m close | half SL1 if wrong side of HTF EMA9 | +8 4 | +17 | +2 / +15 / -9 | +5.7 | 1 / 17 |
| 1st 15m close >= 12 min | half SL1 if wrong side of HTF EMA9 | -1 4 | +7 | -2 / +6 / -5 | +7.4 | 0 / 17 |
| 2nd 15m close | half SL1 if wrong side of HTF EMA9 | -19  | -13 | -5 / -0 / -14 | -2.9 | 0 / 17 |

**4. Which condition — best per condition (any check time / action, no TP rule)**

| Condition | Best rule | Δ after costs | Gross | Positive rules |
|---|---|---|---|---|
| negative | half SL1 if negative at 1st 15m close | -22 4 | +5 | 0 / 16 |
| < 25 % of TP1 | half SL1 if < 25 % of TP1 at 21 min | -54  | -31 | 0 / 24 |
| < 50 % of TP1 | SL1 to BE if < 50 % of TP1 at 24 min | -40  | +26 | 0 / 24 |
| wrong side of HTF EMA9 | half SL1 if wrong side of HTF EMA9 at 1st 15m close | +8 4 | +17 | 7 / 24 |
| never reached 25 % | SL1 to BE if never reached 25 % at 2nd 15m close | -24  | -9 | 0 / 24 |
| never reached 50 % | cut if never reached 50 % at 2nd 15m close | -44  | -6 | 0 / 24 |

**2. Costs:** 29 of 136 rules are better gross, 7 after costs. Avg cost of the rules: -45 pts.

**Top 8 rules after costs** (incl. with the TP rule where run)

1. half SL1 if wrong side of HTF EMA9 at 1st 15m close: **+8** after costs (gross +17) 4 (z +0.2, thirds +2 / +15 / -9, last 4 wk +5.7, 67 cuts, +7 trades)
2. cut if wrong side of HTF EMA9 at 15 min: **+7** after costs (gross +26) 4 (z +0.2, thirds -2 / +16 / -7, last 4 wk +5.4, 147 cuts, +14 trades)
3. SL1 to BE if wrong side of HTF EMA9 at 15 min: **+7** after costs (gross +25) 4 (z +0.2, thirds -2 / +16 / -7, last 4 wk +5.4, 141 cuts, +13 trades)
4. half SL1 if wrong side of HTF EMA9 at 12 min: **+3** after costs (gross +11) 4 (z +0.1, thirds -7 / +6 / +3, last 4 wk +9.2, 60 cuts, +8 trades)
5. cut if wrong side of HTF EMA9 at 12 min: **+2** after costs (gross +23) 4 (z +0.1, thirds -5 / +18 / -10, last 4 wk +0.8, 164 cuts, +14 trades)
6. SL1 to BE if wrong side of HTF EMA9 at 12 min: **+0** after costs (gross +21) 4 (z +0.0, thirds -7 / +18 / -10, last 4 wk +0.8, 160 cuts, +14 trades)
7. half SL1 if wrong side of HTF EMA9 at 15 min: **+0** after costs (gross +8) 4 (z +0.0, thirds +0 / +11 / -12, last 4 wk +4.0, 49 cuts, +8 trades)
8. half SL1 if wrong side of HTF EMA9 at 1st 15m close >= 12 min: **-1** after costs (gross +7) 4 (z -0.0, thirds -2 / +6 / -5, last 4 wk +7.4, 55 cuts, +7 trades)

**3. Walk-forward** (choose on the first two thirds, test on the last third, after costs)

- SL rules only: picked on thirds 1-2 = **SL1 to BE if < 50 % of TP1 at 24 min** (+20 in-sample) → last third **-60** (rank 99 of 136; median rule -43; current exits 0)

**5. Split by session / trigger** (Δ after costs)

| Rule | NY 09:30-16:00 | Other hours | HTF flip | Other triggers |
|---|---|---|---|---|
| half SL1 if wrong side of HTF EMA9 at 1st 15m close | +14 | -6 | +6 | +1 |
| cut if wrong side of HTF EMA9 at 15 min | +3 | +3 | +5 | +2 |
| SL1 to BE if wrong side of HTF EMA9 at 15 min | +3 | +4 | +5 | +2 |

**6. Re-entry after a cut** (next same-direction trade starting within 30 min after the cut)

- half SL1 if wrong side of HTF EMA9 at 1st 15m close: 67 cuts → 7 re-entries, net +0, avg +0.07 vs all trades -0.30
- cut if wrong side of HTF EMA9 at 15 min: 147 cuts → 11 re-entries, net +2, avg +0.22 vs all trades -0.30
- SL1 to BE if wrong side of HTF EMA9 at 15 min: 141 cuts → 10 re-entries, net -0, avg -0.02 vs all trades -0.30

**7. Session guards** (skip the rest of the session after K losses in a row or after −L pts; avg full SL1 loss 4.0 pts)

| Guard | on current exits | beyond random skipping* | on best rule (half SL1 if wrong side of HTF EMA9 at 1st 15m close) |
|---|---|---|---|
| 4 losses in a row + −3 x SL1 (12 pts) | +118 T (thirds +36 / +72 / +10, last 4 wk +4.5, 171 skipped) | **+66** | +125 vs rule alone |
| 4 losses in a row | +94 T (thirds +38 / +50 / +6, last 4 wk +5.5, 129 skipped) | **+55** | +96 vs rule alone |
| −3 x SL1 (12 pts) | +78  (thirds +29 / +50 / -1, last 4 wk +0.4, 120 skipped) | **+41** | +81 vs rule alone |
| 3 losses in a row + −3 x SL1 (12 pts) | +114 T (thirds +33 / +78 / +3, last 4 wk +17.2, 364 skipped) | **+4** | +118 vs rule alone |
| 4 losses in a row + −2 x SL1 (8 pts) | +100  (thirds -6 / +69 / +37, last 4 wk +19.3, 317 skipped) | **+4** | +83 vs rule alone |
| 3 losses in a row | +104 T (thirds +28 / +73 / +3, last 4 wk +17.2, 360 skipped) | **-5** | +108 vs rule alone |
| −2 x SL1 (8 pts) | +83  (thirds -14 / +65 / +32, last 4 wk +19.3, 302 skipped) | **-9** | +58 vs rule alone |
| 3 losses in a row + −2 x SL1 (8 pts) | +114 T (thirds +7 / +86 / +21, last 4 wk +20.5, 425 skipped) | **-15** | +109 vs rule alone |
| 3 losses in a row + −1 x SL1 (4 pts) | +155 T (thirds +9 / +108 / +38, last 4 wk +45.0, 711 skipped) | **-60** | +188 vs rule alone |
| −1 x SL1 (4 pts) | +151 T (thirds +9 / +108 / +34, last 4 wk +45.0, 708 skipped) | **-64** | +186 vs rule alone |
| 4 losses in a row + −1 x SL1 (4 pts) | +151 T (thirds +9 / +108 / +34, last 4 wk +45.0, 708 skipped) | **-64** | +186 vs rule alone |
| 2 losses in a row | +204 T (thirds +70 / +116 / +18, last 4 wk +31.3, 928 skipped) | **-77** | +222 vs rule alone |
| 2 losses in a row + −2 x SL1 (8 pts) | +204 T (thirds +70 / +116 / +18, last 4 wk +31.3, 928 skipped) | **-77** | +222 vs rule alone |
| 2 losses in a row + −3 x SL1 (12 pts) | +204 T (thirds +70 / +116 / +18, last 4 wk +31.3, 928 skipped) | **-77** | +222 vs rule alone |
| 2 losses in a row + −1 x SL1 (4 pts) | +194 T (thirds +40 / +121 / +33, last 4 wk +38.5, 975 skipped) | **-102** | +231 vs rule alone |

*Current exits lose 0.30 pts per trade after costs, so skipping ANY trades looks good. This column = guard result minus what skipping the same number of random trades would give; positive = the guard picks the bad trades.

