## Week of 11/09/2026 summary

- STUDY SETTINGS STALE: the 11/08 settings sync report lists 1 non-known MISMATCH (chop_sim GATE MGC 2m range gate R5=0) + late_study MES 3m tp=2.0 -- both already fixed in the project scripts used for this run, and neither affects these 3m studies.
- Current exits after costs: MES -847 / MGC -129 / MNQ -1627 / M2K -604 (11/07: -831 / -138 / -1646 / -595).
- Walk-forward last third: MES -85 / MGC -14 / MNQ -92 / M2K -84 (11/07: -79 / -19 / -92 / -85) -- still negative on every chart.
- MGC watch 'cut if wrong side of HTF EMA9 at 18 min': **+87 after costs, T4R, z 1.6** (thirds +25 / +18 / +44, last 4 wk +29) -- unchanged, promising for the 2nd week in a row (11/07, 11/09); not recommendable yet (needs 3 weeks and the walk-forward pick is still negative).
- MES: best 'half SL1 if negative at 18 min + TP rule' +206 (z 1.0, no flags); 'half SL1 if wrong side of HTF EMA9 at 18 min + TP rule' +202 TR z 1.1 (promising) but last 4 wk -48. MNQ best +162 (z 0.6); M2K best +8.
- Verdict: keep current exits on all four charts.

---

# Early-exit lab — 3m charts — 11/09/2026 13:58

## Summary

- MES 3m: best half SL1 if negative at 18 min + TP rule → +206 after costs (z +1.0, no flags); walk-forward last third **-85**
- MGC 3m: best cut if < 25 % of TP1 at 18 min + TP rule → +96 after costs (z +0.8, 4); walk-forward last third **-14**
- MNQ 3m: best SL1 to BE if never reached 25 % at 18 min → +162 after costs (z +0.6, 4); walk-forward last third **-92**
- M2K 3m: best half SL1 if wrong side of HTF EMA9 at 1st 15m close → +8 after costs (z +0.2, 4); walk-forward last third **-84**


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

## MES 3m — current exits: 1705 setups to 11/09, net +6 gross / -847 after costs (0.50 pts per trade)

**1. When to check — best rule per check time (after costs; no TP rule)**

| Check | Best rule | Δ after costs | Gross | Thirds | Last 4 wk | Positive rules |
|---|---|---|---|---|---|---|
| 12 min | half SL1 if wrong side of HTF EMA9 | -20  | +3 | +45 / +2 / -67 | -62.7 | 0 / 17 |
| 15 min | half SL1 if < 50 % of TP1 | -14  | +26 | +66 / -15 / -65 | -93.3 | 0 / 17 |
| 18 min | half SL1 if negative | +80  | +115 | +34 / +60 / -14 | -38.5 | 6 / 17 |
| 21 min | half SL1 if negative | +18  | +54 | +45 / +27 / -54 | -40.1 | 2 / 17 |
| 24 min | half SL1 if never reached 25 % | +17  | +26 | +16 / +14 / -12 | -20.4 | 1 / 17 |
| 1st 15m close | half SL1 if wrong side of HTF EMA9 | +11  | +35 | +22 / -1 / -10 | -26.5 | 1 / 17 |
| 1st 15m close >= 12 min | half SL1 if never reached 25 % | -22  | -4 | +3 / +19 / -43 | -36.9 | 0 / 17 |
| 2nd 15m close | half SL1 if never reached 25 % | +5  | +17 | +3 / +15 / -12 | -9.4 | 1 / 17 |

**4. Which condition — best per condition (any check time / action, no TP rule)**

| Condition | Best rule | Δ after costs | Gross | Positive rules |
|---|---|---|---|---|
| negative | half SL1 if negative at 18 min | +80  | +115 | 2 / 16 |
| < 25 % of TP1 | half SL1 if < 25 % of TP1 at 18 min | +68  | +102 | 1 / 24 |
| < 50 % of TP1 | half SL1 if < 50 % of TP1 at 18 min | +41  | +77 | 1 / 24 |
| wrong side of HTF EMA9 | half SL1 if wrong side of HTF EMA9 at 18 min | +38 T | +55 | 2 / 24 |
| never reached 25 % | half SL1 if never reached 25 % at 18 min | +43  | +57 | 4 / 24 |
| never reached 50 % | half SL1 if never reached 50 % at 18 min | +36  | +62 | 1 / 24 |

**2. Costs:** 46 of 136 rules are better gross, 11 after costs. Avg cost of the rules: -112 pts.

**Top 8 rules after costs** (incl. with the TP rule where run)

1. half SL1 if negative at 18 min + TP rule: **+206** after costs (gross +275) (z +1.0, thirds +114 / +105 / -13, last 4 wk -85.9, 78 cuts, +100 trades)
2. half SL1 if wrong side of HTF EMA9 at 18 min + TP rule: **+202** after costs (gross +255) TR (z +1.1, thirds +93 / +96 / +13, last 4 wk -47.9, 59 cuts, +76 trades) — promising
3. half SL1 if < 25 % of TP1 at 18 min + TP rule: **+193** after costs (gross +263) (z +1.0, thirds +128 / +107 / -43, last 4 wk -106.9, 78 cuts, +101 trades)
4. half SL1 if never reached 50 % at 18 min + TP rule: **+193** after costs (gross +255) (z +1.0, thirds +134 / +95 / -36, last 4 wk -102.1, 64 cuts, +92 trades)
5. half SL1 if never reached 25 % at 18 min + TP rule: **+185** after costs (gross +234) (z +1.1, thirds +106 / +91 / -11, last 4 wk -57.9, 36 cuts, +80 trades)
6. half SL1 if wrong side of HTF EMA9 at 1st 15m close + TP rule: **+180** after costs (gross +239) T (z +1.0, thirds +96 / +72 / +12, last 4 wk -46.2, 85 cuts, +76 trades)
7. half SL1 if never reached 25 % at 24 min + TP rule: **+170** after costs (gross +214) TR (z +1.0, thirds +92 / +74 / +5, last 4 wk -61.6, 19 cuts, +77 trades) — promising
8. half SL1 if < 50 % of TP1 at 18 min + TP rule: **+166** after costs (gross +236) (z +0.8, thirds +156 / +95 / -85, last 4 wk -143.0, 78 cuts, +102 trades)

TP rule alone (TP1 -> 85 % after 18 min): +180 after costs, thirds +75 / +80 / +25, last 4 wk -25.3.

**3. Walk-forward** (choose on the first two thirds, test on the last third, after costs)

- SL rules only: picked on thirds 1-2 = **cut if < 50 % of TP1 at 18 min** (+131 in-sample) → last third **-218** (rank 127 of 136; median rule -102; current exits 0)
- with TP rule: picked on thirds 1-2 = **half SL1 if < 50 % of TP1 at 18 min** (+251 in-sample) → last third **-85** (rank 72 of 136; median rule -80; current exits 0)

**5. Split by session / trigger** (Δ after costs)

| Rule | NY 09:30-16:00 | Other hours | HTF flip | Other triggers |
|---|---|---|---|---|
| half SL1 if negative at 18 min | +120 | -40 | +78 | +2 |
| half SL1 if < 25 % of TP1 at 18 min | +113 | -45 | +102 | -34 |
| half SL1 if never reached 25 % at 18 min | +40 | +4 | +59 | -15 |

**6. Re-entry after a cut** (next same-direction trade starting within 30 min after the cut)

- half SL1 if negative at 18 min: 75 cuts → 5 re-entries, net -18, avg -3.66 vs all trades -0.44
- half SL1 if < 25 % of TP1 at 18 min: 75 cuts → 5 re-entries, net -18, avg -3.66 vs all trades -0.45
- half SL1 if never reached 25 % at 18 min: 35 cuts → 4 re-entries, net -21, avg -5.28 vs all trades -0.47

**7. Session guards** (skip the rest of the session after K losses in a row or after −L pts; avg full SL1 loss 10.5 pts)

| Guard | on current exits | beyond random skipping* | on best rule (half SL1 if negative at 18 min) |
|---|---|---|---|
| 2 losses in a row | +568 T (thirds +49 / +460 / +58, last 4 wk -80.0, 676 skipped) | **+232** | +585 vs rule alone |
| 2 losses in a row + −3 x SL1 (31 pts) | +568 T (thirds +49 / +460 / +58, last 4 wk -80.0, 676 skipped) | **+232** | +585 vs rule alone |
| 2 losses in a row + −2 x SL1 (21 pts) | +532 T (thirds +22 / +452 / +58, last 4 wk -80.0, 684 skipped) | **+193** | +565 vs rule alone |
| 3 losses in a row + −3 x SL1 (31 pts) | +310 T (thirds +21 / +257 / +32, last 4 wk -120.3, 315 skipped) | **+153** | +335 vs rule alone |
| 2 losses in a row + −1 x SL1 (10 pts) | +504  (thirds -5 / +462 / +48, last 4 wk -95.2, 718 skipped) | **+148** | +552 vs rule alone |
| 3 losses in a row | +298 T (thirds +9 / +257 / +32, last 4 wk -120.3, 313 skipped) | **+142** | +331 vs rule alone |
| −3 x SL1 (31 pts) | +161 T (thirds +50 / +83 / +28, last 4 wk +0.0, 41 skipped) | **+141** | +40 vs rule alone |
| 3 losses in a row + −2 x SL1 (21 pts) | +213  (thirds -64 / +261 / +17, last 4 wk -115.3, 336 skipped) | **+46** | +308 vs rule alone |
| 4 losses in a row + −3 x SL1 (31 pts) | +75  (thirds -10 / +61 / +24, last 4 wk -45.0, 142 skipped) | **+5** | +8 vs rule alone |
| −2 x SL1 (21 pts) | +55  (thirds -22 / +73 / +3, last 4 wk -26.3, 132 skipped) | **-11** | +66 vs rule alone |
| 3 losses in a row + −1 x SL1 (10 pts) | +214  (thirds -53 / +320 / -53, last 4 wk -154.0, 456 skipped) | **-12** | +284 vs rule alone |
| 4 losses in a row | +23  (thirds -57 / +66 / +14, last 4 wk -45.0, 131 skipped) | **-42** | +24 vs rule alone |
| −1 x SL1 (10 pts) | +132  (thirds -54 / +260 / -74, last 4 wk -154.0, 393 skipped) | **-63** | +113 vs rule alone |
| 4 losses in a row + −1 x SL1 (10 pts) | +109  (thirds -62 / +236 / -64, last 4 wk -154.0, 404 skipped) | **-91** | +95 vs rule alone |
| 4 losses in a row + −2 x SL1 (21 pts) | -16  (thirds -87 / +82 / -10, last 4 wk -71.3, 196 skipped) | **-113** | -15 vs rule alone |

*Current exits lose 0.50 pts per trade after costs, so skipping ANY trades looks good. This column = guard result minus what skipping the same number of random trades would give; positive = the guard picks the bad trades.

## MGC 3m — current exits: 1707 setups to 11/09, net +247 gross / -129 after costs (0.22 pts per trade)

**1. When to check — best rule per check time (after costs; no TP rule)**

| Check | Best rule | Δ after costs | Gross | Thirds | Last 4 wk | Positive rules |
|---|---|---|---|---|---|---|
| 12 min | half SL1 if negative | +62  | +75 | -1 / +16 / +47 | -17.4 | 6 / 17 |
| 15 min | half SL1 if wrong side of HTF EMA9 | +75 T4R | +82 | +35 / +25 / +15 | +14.2 | 9 / 17 |
| 18 min | cut if wrong side of HTF EMA9 | +87 T4R | +98 | +25 / +18 / +44 | +29.1 | 16 / 17 |
| 21 min | cut if wrong side of HTF EMA9 | +53 T4R | +63 | +18 / +1 / +34 | +20.2 | 7 / 17 |
| 24 min | cut if wrong side of HTF EMA9 | +25 T4R | +31 | +18 / +1 / +6 | +0.2 | 11 / 17 |
| 1st 15m close | half SL1 if never reached 50 % | +71 T | +85 | +9 / +35 / +27 | -25.0 | 4 / 17 |
| 1st 15m close >= 12 min | half SL1 if never reached 50 % | +16  | +25 | -11 / -8 / +35 | -12.7 | 3 / 17 |
| 2nd 15m close | cut if never reached 50 % | +2  | +16 | -14 / -1 / +17 | -14.7 | 3 / 17 |

**4. Which condition — best per condition (any check time / action, no TP rule)**

| Condition | Best rule | Δ after costs | Gross | Positive rules |
|---|---|---|---|---|
| negative | cut if negative at 18 min | +82 T4 | +112 | 5 / 16 |
| < 25 % of TP1 | cut if < 25 % of TP1 at 18 min | +78 4 | +124 | 5 / 24 |
| < 50 % of TP1 | SL1 to BE if < 50 % of TP1 at 18 min | +57  | +94 | 8 / 24 |
| wrong side of HTF EMA9 | cut if wrong side of HTF EMA9 at 18 min | +87 T4R | +98 | 15 / 24 |
| never reached 25 % | half SL1 if never reached 25 % at 1st 15m close | +42 4 | +51 | 11 / 24 |
| never reached 50 % | half SL1 if never reached 50 % at 1st 15m close | +71 T | +85 | 15 / 24 |

**2. Costs:** 83 of 136 rules are better gross, 59 after costs. Avg cost of the rules: -23 pts.

**Top 8 rules after costs** (incl. with the TP rule where run)

1. cut if < 25 % of TP1 at 18 min + TP rule: **+96** after costs (gross +145) 4 (z +0.8, thirds +63 / -1 / +34, last 4 wk +5.3, 348 cuts, +64 trades)
2. SL1 to BE if < 25 % of TP1 at 18 min + TP rule: **+90** after costs (gross +129) T4 (z +0.7, thirds +52 / +12 / +25, last 4 wk +2.8, 250 cuts, +64 trades)
3. cut if wrong side of HTF EMA9 at 18 min: **+87** after costs (gross +98) T4R (z +1.6, thirds +25 / +18 / +44, last 4 wk +29.1, 91 cuts, +8 trades) — promising
4. SL1 to BE if wrong side of HTF EMA9 at 18 min: **+84** after costs (gross +95) T4R (z +1.5, thirds +25 / +18 / +42, last 4 wk +28.9, 87 cuts, +8 trades) — promising
5. cut if negative at 18 min: **+82** after costs (gross +112) T4 (z +0.9, thirds +23 / +10 / +48, last 4 wk +31.2, 244 cuts, +26 trades)
6. cut if < 25 % of TP1 at 18 min: **+78** after costs (gross +124) 4 (z +0.7, thirds +36 / -9 / +51, last 4 wk +8.7, 347 cuts, +51 trades)
7. half SL1 if wrong side of HTF EMA9 at 15 min: **+75** after costs (gross +82) T4R (z +1.3, thirds +35 / +25 / +15, last 4 wk +14.2, 50 cuts, +8 trades) — promising
8. half SL1 if never reached 50 % at 1st 15m close: **+71** after costs (gross +85) T (z +0.7, thirds +9 / +35 / +27, last 4 wk -25.0, 101 cuts, +19 trades)

TP rule alone (TP1 -> 65 % after 21 min): -2 after costs, thirds +28 / -11 / -19, last 4 wk -11.1.

**3. Walk-forward** (choose on the first two thirds, test on the last third, after costs)

- SL rules only: picked on thirds 1-2 = **SL1 to BE if < 50 % of TP1 at 18 min** (+66 in-sample) → last third **-10** (rank 108 of 136; median rule +14; current exits 0)
- with TP rule: picked on thirds 1-2 = **half SL1 if wrong side of HTF EMA9 at 15 min** (+69 in-sample) → last third **-14** (rank 104 of 136; median rule +3; current exits 0)

**5. Split by session / trigger** (Δ after costs)

| Rule | NY 09:30-16:00 | Other hours | HTF flip | Other triggers |
|---|---|---|---|---|
| cut if wrong side of HTF EMA9 at 18 min | +24 | +63 | +23 | +64 |
| SL1 to BE if wrong side of HTF EMA9 at 18 min | +21 | +63 | +23 | +61 |
| cut if negative at 18 min | +27 | +55 | +68 | +14 |

**6. Re-entry after a cut** (next same-direction trade starting within 30 min after the cut)

- cut if wrong side of HTF EMA9 at 18 min: 91 cuts → 8 re-entries, net -2, avg -0.24 vs all trades -0.02
- SL1 to BE if wrong side of HTF EMA9 at 18 min: 87 cuts → 8 re-entries, net -2, avg -0.24 vs all trades -0.03
- cut if negative at 18 min: 244 cuts → 24 re-entries, net +11, avg +0.45 vs all trades -0.03

**7. Session guards** (skip the rest of the session after K losses in a row or after −L pts; avg full SL1 loss 6.5 pts)

| Guard | on current exits | beyond random skipping* | on best rule (cut if wrong side of HTF EMA9 at 18 min) |
|---|---|---|---|
| 2 losses in a row + −1 x SL1 (7 pts) | +107  (thirds +126 / -95 / +77, last 4 wk -10.0, 852 skipped) | **+43** | +75 vs rule alone |
| 2 losses in a row + −2 x SL1 (13 pts) | +96  (thirds +101 / -101 / +96, last 4 wk +26.1, 725 skipped) | **+41** | +67 vs rule alone |
| 2 losses in a row | +84  (thirds +89 / -101 / +96, last 4 wk +26.1, 721 skipped) | **+30** | +56 vs rule alone |
| 2 losses in a row + −3 x SL1 (20 pts) | +84  (thirds +89 / -101 / +96, last 4 wk +26.1, 721 skipped) | **+30** | +56 vs rule alone |
| 3 losses in a row + −1 x SL1 (7 pts) | +58  (thirds +78 / -42 / +22, last 4 wk -46.2, 714 skipped) | **+4** | +23 vs rule alone |
| −1 x SL1 (7 pts) | +46  (thirds +76 / -40 / +10, last 4 wk -61.8, 678 skipped) | **-5** | +10 vs rule alone |
| 4 losses in a row + −1 x SL1 (7 pts) | +43  (thirds +76 / -45 / +12, last 4 wk -60.6, 682 skipped) | **-9** | +9 vs rule alone |
| 3 losses in a row + −2 x SL1 (13 pts) | +18  (thirds -1 / -2 / +21, last 4 wk +4.4, 417 skipped) | **-13** | -13 vs rule alone |
| 3 losses in a row + −3 x SL1 (20 pts) | +10  (thirds +25 / +9 / -24, last 4 wk +4.4, 312 skipped) | **-14** | -15 vs rule alone |
| −3 x SL1 (20 pts) | -10  (thirds +12 / -21 / -0, last 4 wk +11.4, 109 skipped) | **-18** | -22 vs rule alone |
| 3 losses in a row | -1  (thirds +33 / +4 / -37, last 4 wk +4.4, 303 skipped) | **-24** | -6 vs rule alone |
| −2 x SL1 (13 pts) | -9  (thirds -36 / +1 / +26, last 4 wk -6.0, 311 skipped) | **-33** | -28 vs rule alone |
| 4 losses in a row + −2 x SL1 (13 pts) | -9  (thirds -31 / -15 / +36, last 4 wk +4.7, 331 skipped) | **-34** | -36 vs rule alone |
| 4 losses in a row + −3 x SL1 (20 pts) | -27  (thirds +10 / -27 / -10, last 4 wk +15.9, 174 skipped) | **-40** | -39 vs rule alone |
| 4 losses in a row | -48  (thirds -6 / -35 / -6, last 4 wk +15.9, 123 skipped) | **-57** | -42 vs rule alone |

*Current exits lose 0.08 pts per trade after costs, so skipping ANY trades looks good. This column = guard result minus what skipping the same number of random trades would give; positive = the guard picks the bad trades.

## MNQ 3m — current exits: 1937 setups to 11/09, net +58 gross / -1627 after costs (0.87 pts per trade)

**1. When to check — best rule per check time (after costs; no TP rule)**

| Check | Best rule | Δ after costs | Gross | Thirds | Last 4 wk | Positive rules |
|---|---|---|---|---|---|---|
| 12 min | half SL1 if never reached 25 % | +130 4 | +155 | -69 / +149 / +50 | +51.0 | 1 / 17 |
| 15 min | half SL1 if never reached 25 % | +38 4 | +59 | -36 / +96 / -22 | +30.0 | 1 / 17 |
| 18 min | SL1 to BE if never reached 25 % | +162 4 | +195 | -33 / +164 / +32 | +28.7 | 8 / 17 |
| 21 min | cut if never reached 50 % | +38 4 | +122 | -56 / +125 / -31 | +138.1 | 1 / 17 |
| 24 min | cut if never reached 50 % | +160 4 | +226 | -24 / +253 / -69 | +81.2 | 5 / 17 |
| 1st 15m close | cut if wrong side of HTF EMA9 | -129  | -68 | +94 / +82 / -305 | -107.9 | 0 / 17 |
| 1st 15m close >= 12 min | cut if wrong side of HTF EMA9 | +46  | +79 | -108 / +110 / +44 | -18.0 | 2 / 17 |
| 2nd 15m close | cut if never reached 50 % | +152 4 | +213 | +22 / +223 / -92 | +39.0 | 6 / 17 |

**4. Which condition — best per condition (any check time / action, no TP rule)**

| Condition | Best rule | Δ after costs | Gross | Positive rules |
|---|---|---|---|---|
| negative | half SL1 if negative at 15 min | -30 4 | +19 | 0 / 16 |
| < 25 % of TP1 | half SL1 if < 25 % of TP1 at 18 min | -260 4 | -208 | 0 / 24 |
| < 50 % of TP1 | cut if < 50 % of TP1 at 24 min | -228 4 | -47 | 0 / 24 |
| wrong side of HTF EMA9 | cut if wrong side of HTF EMA9 at 18 min | +79 4 | +111 | 7 / 24 |
| never reached 25 % | SL1 to BE if never reached 25 % at 18 min | +162 4 | +195 | 7 / 24 |
| never reached 50 % | cut if never reached 50 % at 24 min | +160 4 | +226 | 10 / 24 |

**2. Costs:** 30 of 136 rules are better gross, 24 after costs. Avg cost of the rules: -91 pts.

**Top 8 rules after costs** (incl. with the TP rule where run)

1. SL1 to BE if never reached 25 % at 18 min: **+162** after costs (gross +195) 4 (z +0.6, thirds -33 / +164 / +32, last 4 wk +28.7, 68 cuts, +18 trades)
2. cut if never reached 50 % at 24 min: **+160** after costs (gross +226) 4 (z +0.4, thirds -24 / +253 / -69, last 4 wk +81.2, 148 cuts, +33 trades)
3. cut if never reached 25 % at 18 min: **+153** after costs (gross +189) 4 (z +0.5, thirds -21 / +171 / +4, last 4 wk +28.7, 81 cuts, +18 trades)
4. cut if never reached 50 % at 2nd 15m close: **+152** after costs (gross +213) 4 (z +0.4, thirds +22 / +223 / -92, last 4 wk +39.0, 143 cuts, +29 trades)
5. half SL1 if never reached 25 % at 12 min: **+130** after costs (gross +155) 4 (z +0.4, thirds -69 / +149 / +50, last 4 wk +51.0, 44 cuts, +16 trades)
6. half SL1 if never reached 50 % at 2nd 15m close: **+114** after costs (gross +133) T4 (z +0.4, thirds +22 / +75 / +16, last 4 wk +22.2, 33 cuts, +13 trades)
7. cut if never reached 50 % at 18 min: **+91** after costs (gross +203) 4 (z +0.2, thirds -46 / +123 / +13, last 4 wk +163.6, 262 cuts, +54 trades)
8. SL1 to BE if never reached 50 % at 2nd 15m close: **+89** after costs (gross +139) 4 (z +0.2, thirds -44 / +224 / -91, last 4 wk +22.3, 108 cuts, +27 trades)

**3. Walk-forward** (choose on the first two thirds, test on the last third, after costs)

- SL rules only: picked on thirds 1-2 = **cut if never reached 50 % at 2nd 15m close** (+244 in-sample) → last third **-92** (rank 59 of 136; median rule -108; current exits 0)

**5. Split by session / trigger** (Δ after costs)

| Rule | NY 09:30-16:00 | Other hours | HTF flip | Other triggers |
|---|---|---|---|---|
| SL1 to BE if never reached 25 % at 18 min | +27 | +135 | +42 | +119 |
| cut if never reached 50 % at 24 min | +126 | +34 | +147 | +13 |
| cut if never reached 25 % at 18 min | +4 | +150 | +23 | +130 |

**6. Re-entry after a cut** (next same-direction trade starting within 30 min after the cut)

- SL1 to BE if never reached 25 % at 18 min: 68 cuts → 13 re-entries, net -20, avg -1.53 vs all trades -0.75
- cut if never reached 50 % at 24 min: 148 cuts → 29 re-entries, net -174, avg -5.99 vs all trades -0.74
- cut if never reached 25 % at 18 min: 81 cuts → 17 re-entries, net -26, avg -1.55 vs all trades -0.75

**7. Session guards** (skip the rest of the session after K losses in a row or after −L pts; avg full SL1 loss 29.6 pts)

| Guard | on current exits | beyond random skipping* | on best rule (SL1 to BE if never reached 25 % at 18 min) |
|---|---|---|---|
| 2 losses in a row + −1 x SL1 (30 pts) | +1441 T (thirds +187 / +439 / +815, last 4 wk +206.5, 1062 skipped) | **+549** | +1179 vs rule alone |
| 3 losses in a row + −3 x SL1 (89 pts) | +931 T (thirds +46 / +362 / +523, last 4 wk +262.2, 512 skipped) | **+501** | +1015 vs rule alone |
| 3 losses in a row + −1 x SL1 (30 pts) | +1221 T (thirds +161 / +297 / +763, last 4 wk +224.5, 889 skipped) | **+475** | +1053 vs rule alone |
| 3 losses in a row | +900 T (thirds +46 / +331 / +523, last 4 wk +262.2, 511 skipped) | **+471** | +985 vs rule alone |
| −1 x SL1 (30 pts) | +1138 T (thirds +208 / +197 / +732, last 4 wk +262.4, 848 skipped) | **+426** | +920 vs rule alone |
| 4 losses in a row + −1 x SL1 (30 pts) | +1076 T (thirds +94 / +197 / +784, last 4 wk +262.4, 860 skipped) | **+354** | +900 vs rule alone |
| 4 losses in a row + −3 x SL1 (89 pts) | +575  (thirds -174 / +501 / +249, last 4 wk +67.9, 276 skipped) | **+344** | +553 vs rule alone |
| −3 x SL1 (89 pts) | +415  (thirds -77 / +260 / +232, last 4 wk +90.7, 199 skipped) | **+248** | +248 vs rule alone |
| 4 losses in a row | +337  (thirds -185 / +357 / +166, last 4 wk +42.0, 232 skipped) | **+142** | +378 vs rule alone |
| 4 losses in a row + −2 x SL1 (59 pts) | +483  (thirds +232 / -19 / +271, last 4 wk +162.9, 479 skipped) | **+81** | +737 vs rule alone |
| 2 losses in a row | +883 T (thirds +280 / +6 / +598, last 4 wk +182.4, 970 skipped) | **+69** | +731 vs rule alone |
| 2 losses in a row + −2 x SL1 (59 pts) | +883 T (thirds +280 / +6 / +598, last 4 wk +182.4, 970 skipped) | **+69** | +731 vs rule alone |
| 2 losses in a row + −3 x SL1 (89 pts) | +883 T (thirds +280 / +6 / +598, last 4 wk +182.4, 970 skipped) | **+69** | +731 vs rule alone |
| −2 x SL1 (59 pts) | +406  (thirds +382 / -163 / +188, last 4 wk +162.9, 451 skipped) | **+27** | +632 vs rule alone |
| 3 losses in a row + −2 x SL1 (59 pts) | +505  (thirds +129 / -25 / +401, last 4 wk +189.5, 596 skipped) | **+5** | +916 vs rule alone |

*Current exits lose 0.84 pts per trade after costs, so skipping ANY trades looks good. This column = guard result minus what skipping the same number of random trades would give; positive = the guard picks the bad trades.

## M2K 3m — current exits: 1948 setups to 11/09, net +78 gross / -604 after costs (0.35 pts per trade)

**1. When to check — best rule per check time (after costs; no TP rule)**

| Check | Best rule | Δ after costs | Gross | Thirds | Last 4 wk | Positive rules |
|---|---|---|---|---|---|---|
| 12 min | cut if wrong side of HTF EMA9 | +5 4 | +26 | -5 / +17 / -6 | +2.6 | 3 / 17 |
| 15 min | cut if wrong side of HTF EMA9 | +7 4 | +26 | -2 / +16 / -7 | +4.7 | 3 / 17 |
| 18 min | cut if negative | -37  | +30 | -6 / +20 / -51 | -14.4 | 0 / 17 |
| 21 min | half SL1 if never reached 25 % | -26  | -19 | +1 / -9 / -18 | -4.7 | 0 / 17 |
| 24 min | cut if wrong side of HTF EMA9 | -22  | -7 | +0 / +4 / -26 | -4.2 | 0 / 17 |
| 1st 15m close | half SL1 if wrong side of HTF EMA9 | +8 4 | +17 | +2 / +14 / -8 | +1.5 | 1 / 17 |
| 1st 15m close >= 12 min | half SL1 if wrong side of HTF EMA9 | -1 4 | +7 | -2 / +6 / -5 | +3.2 | 0 / 17 |
| 2nd 15m close | half SL1 if wrong side of HTF EMA9 | -19  | -13 | -5 / -0 / -13 | -6.0 | 0 / 17 |

**4. Which condition — best per condition (any check time / action, no TP rule)**

| Condition | Best rule | Δ after costs | Gross | Positive rules |
|---|---|---|---|---|
| negative | half SL1 if negative at 1st 15m close | -20 4 | +8 | 0 / 16 |
| < 25 % of TP1 | half SL1 if < 25 % of TP1 at 21 min | -49  | -27 | 0 / 24 |
| < 50 % of TP1 | SL1 to BE if < 50 % of TP1 at 24 min | -34  | +30 | 0 / 24 |
| wrong side of HTF EMA9 | half SL1 if wrong side of HTF EMA9 at 1st 15m close | +8 4 | +17 | 7 / 24 |
| never reached 25 % | SL1 to BE if never reached 25 % at 2nd 15m close | -24  | -9 | 0 / 24 |
| never reached 50 % | cut if never reached 50 % at 2nd 15m close | -38  | -1 | 0 / 24 |

**2. Costs:** 35 of 136 rules are better gross, 7 after costs. Avg cost of the rules: -44 pts.

**Top 8 rules after costs** (incl. with the TP rule where run)

1. half SL1 if wrong side of HTF EMA9 at 1st 15m close: **+8** after costs (gross +17) 4 (z +0.2, thirds +2 / +14 / -8, last 4 wk +1.5, 67 cuts, +7 trades)
2. cut if wrong side of HTF EMA9 at 15 min: **+7** after costs (gross +26) 4 (z +0.2, thirds -2 / +16 / -7, last 4 wk +4.7, 147 cuts, +14 trades)
3. SL1 to BE if wrong side of HTF EMA9 at 15 min: **+7** after costs (gross +25) 4 (z +0.2, thirds -2 / +16 / -7, last 4 wk +4.7, 141 cuts, +13 trades)
4. cut if wrong side of HTF EMA9 at 12 min: **+5** after costs (gross +26) 4 (z +0.1, thirds -5 / +17 / -6, last 4 wk +2.6, 162 cuts, +14 trades)
5. SL1 to BE if wrong side of HTF EMA9 at 12 min: **+3** after costs (gross +24) 4 (z +0.1, thirds -7 / +17 / -6, last 4 wk +2.6, 158 cuts, +14 trades)
6. half SL1 if wrong side of HTF EMA9 at 12 min: **+3** after costs (gross +11) 4 (z +0.1, thirds -7 / +5 / +4, last 4 wk +8.8, 60 cuts, +8 trades)
7. half SL1 if wrong side of HTF EMA9 at 15 min: **+0** after costs (gross +8) 4 (z +0.0, thirds +0 / +11 / -12, last 4 wk +0.5, 49 cuts, +8 trades)
8. half SL1 if wrong side of HTF EMA9 at 1st 15m close >= 12 min: **-1** after costs (gross +7) 4 (z -0.0, thirds -2 / +6 / -5, last 4 wk +3.2, 55 cuts, +7 trades)

**3. Walk-forward** (choose on the first two thirds, test on the last third, after costs)

- SL rules only: picked on thirds 1-2 = **cut if < 50 % of TP1 at 1st 15m close >= 12 min** (+16 in-sample) → last third **-84** (rank 134 of 136; median rule -37; current exits 0)

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
| 4 losses in a row + −3 x SL1 (12 pts) | +120 T (thirds +36 / +79 / +5, last 4 wk +5.8, 169 skipped) | **+67** | +127 vs rule alone |
| 4 losses in a row | +95 T (thirds +38 / +57 / +1, last 4 wk +6.8, 127 skipped) | **+56** | +97 vs rule alone |
| −3 x SL1 (12 pts) | +86 T (thirds +29 / +50 / +7, last 4 wk +8.6, 117 skipped) | **+50** | +89 vs rule alone |
| 3 losses in a row + −3 x SL1 (12 pts) | +111  (thirds +33 / +83 / -5, last 4 wk +9.3, 361 skipped) | **-1** | +115 vs rule alone |
| 4 losses in a row + −2 x SL1 (8 pts) | +96  (thirds -6 / +74 / +28, last 4 wk +18.7, 314 skipped) | **-2** | +79 vs rule alone |
| 3 losses in a row | +101  (thirds +28 / +78 / -5, last 4 wk +9.3, 357 skipped) | **-10** | +104 vs rule alone |
| −2 x SL1 (8 pts) | +79  (thirds -14 / +70 / +23, last 4 wk +18.7, 299 skipped) | **-14** | +54 vs rule alone |
| 3 losses in a row + −2 x SL1 (8 pts) | +111 T (thirds +7 / +91 / +13, last 4 wk +12.7, 422 skipped) | **-20** | +105 vs rule alone |
| 3 losses in a row + −1 x SL1 (4 pts) | +150 T (thirds +9 / +112 / +29, last 4 wk +37.2, 708 skipped) | **-69** | +183 vs rule alone |
| −1 x SL1 (4 pts) | +145 T (thirds +9 / +112 / +25, last 4 wk +37.2, 705 skipped) | **-73** | +181 vs rule alone |
| 4 losses in a row + −1 x SL1 (4 pts) | +145 T (thirds +9 / +112 / +25, last 4 wk +37.2, 705 skipped) | **-73** | +181 vs rule alone |
| 2 losses in a row | +194 T (thirds +70 / +117 / +8, last 4 wk +19.0, 921 skipped) | **-91** | +213 vs rule alone |
| 2 losses in a row + −2 x SL1 (8 pts) | +194 T (thirds +70 / +117 / +8, last 4 wk +19.0, 921 skipped) | **-91** | +213 vs rule alone |
| 2 losses in a row + −3 x SL1 (12 pts) | +194 T (thirds +70 / +117 / +8, last 4 wk +19.0, 921 skipped) | **-91** | +213 vs rule alone |
| 2 losses in a row + −1 x SL1 (4 pts) | +184 T (thirds +40 / +122 / +23, last 4 wk +26.3, 968 skipped) | **-116** | +221 vs rule alone |

*Current exits lose 0.31 pts per trade after costs, so skipping ANY trades looks good. This column = guard result minus what skipping the same number of random trades would give; positive = the guard picks the bad trades.

