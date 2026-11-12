# 5m charts: exits, filters, session stops and all combined — MES 5m and MGC 5m — 11/08/2026

## Summary

- MES 5m: current -600 after costs → best combined (filter / stop / current exits) -184; thirds -113 / +29 / -100; last 4 wk -44 vs -91
- MGC 5m: current -370 after costs → best combined (filter / stop / current exits) -98; thirds -143 / +128 / -82; last 4 wk -81 vs -138


5m version of the 3m exit / filter / stop work -- MES 5m and MGC 5m -- 11/08/2026.
Same steps as on 3m, re-searched on 5m (the 3m settings are not assumed to carry over):
 1. EXITS: TP rule (TP1 -> Y % of its distance from the candle after X min) x SL rule (one check X min after entry: CUT = close,
    HALF = SL1 to half distance, if negative / < 25 % / < 50 % of TP1). X = 10-40 min (5m candles).
 2. ENTRY FILTERS: skip setups against 60m CBC / EMA200 slope 1 h, 3 h / VWAP / previous session close / 5-day EMA (both sides or
    shorts only).
 3. SESSION STOPS: per 18-18 session (K losses in a row or N flip-outs), the same only when the previous 5 sessions lost, and K
    losses counted separately in Asia (18-03 ET) / London (03-09:30) / NY (09:30-16).
 4. COMBINED: the best of each step (best = largest whole-period gain among rules better than current in all three thirds after
    costs / beyond random), every combination re-simulated together.
Each step also shows a walk-forward check: the rule picked on thirds 1-2 only, scored on third 3.
Replay = chop_sim rules (late window 1, NY OR block 30) on CBC default 5m exits: SL1 1.7 x ATR, min 5, cap MES 8 / MGC 7,
TP1 1.7 x ATR cap 6, 80 % at TP1 + BE + trail 1.7; no range / stretch gate (5m charts are not listed). 5m bars Jan 5 -> now.
Costs: commission + 1 tick per trade (MES 0.50 / MGC 0.22 pts), +1 tick for a rule exit at the candle close.
Cells: net after costs; (beyond random) = gain minus dropping the same number of trades at random.

## MES 5m — current exits: 1183 setups 01/06–11/06

Current exits after costs: Third 1 -254, Third 2 -87, Third 3 -259, Last 4 wk -91, Whole -600. Full stats (trades / net / win % / profit factor / max drawdown): 1183 / -600 / 50 % / 0.83 / 607

### 1. Exit rules (Δ vs current exits after costs; T = better in all three thirds, 4 = better in the last 4 weeks)

**TP rule alone — Δ whole period**

| X min | 65 % | 75 % | 85 % |
|---|---|---|---|
| 10 | -71  | +27 4 | +25 4 |
| 15 | -9  | +62 4 | +49 4 |
| 20 | -50  | +0 4 | +50 4 |
| 25 | -45  | +2 4 | +37 4 |
| 30 | +22 4 | +56 4 | +65 4 |
| 40 | +41 4 | +69 4 | +58 4 |

**SL rule alone — Δ whole period**

| X min | close negative | close < 25 % | close < 50 % | half SL1 negative | half SL1 < 50 % |
|---|---|---|---|---|---|
| 10 | -52 4 | -157  | -115  | +22 4 | -4 4 |
| 15 | -71  | -112  | -182  | -39 4 | -9 4 |
| 20 | -98  | -104  | -142  | -42  | -32 4 |
| 25 | -68 4 | -106  | -135  | -53 4 | -112  |
| 30 | -32 4 | -30  | -94 4 | -52  | -75 4 |

Combinations better in all three thirds: 0 of 493. Top 5:

| Rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|

Walk-forward: picked on thirds 1-2 = **TP1 -> 75 % after 40 min + close if < 25 % at 20 min** → third 3 Δ **-102** (rank 467 of 493; median -15).

### 2. Entry filters (current exits; net after costs, beyond random in brackets; ✓ = beyond random positive in all three thirds)

| Rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|
| skip against 5-day EMA | -140 (+54) | +14 (+42) | -115 (+71) | -25 (+43) | -241 (+167) | 804 | ✓ |
| skip against EMA200 slope 3 h | -108 (+99) | -79 (-36) | -135 (+79) | -35 (+43) | -322 (+142) | 913 |  |
| skip against EMA200 slope 1 h | -125 (+88) | -101 (-48) | -185 (+30) | -64 (+12) | -411 (+71) | 950 |  |
| skip against EMA200 slope 3 h (shorts only) | -157 (+71) | -142 (-79) | -200 (+35) | -64 (+19) | -499 (+27) | 1037 |  |
| skip against 5-day EMA (shorts only) | -201 (+25) | -79 (-30) | -207 (+18) | -86 (-3) | -487 (+12) | 985 |  |
| skip against 60m CBC | -209 (-10) | -25 (+6) | -206 (-14) | -51 (+21) | -440 (-18) | 833 |  |
| skip against prev session close | -192 (+28) | -128 (-81) | -188 (+34) | -59 (+21) | -508 (-19) | 963 |  |
| skip against EMA200 slope 1 h (shorts only) | -180 (+52) | -146 (-77) | -241 (-4) | -83 (+0) | -567 (-29) | 1060 |  |
| skip against prev session close (shorts only) | -211 (+32) | -129 (-64) | -251 (-15) | -68 (+18) | -591 (-47) | 1073 |  |
| skip against VWAP | -234 (+7) | -112 (-44) | -260 (-21) | -95 (-9) | -607 (-58) | 1081 |  |
| skip against VWAP (shorts only) | -221 (+26) | -131 (-56) | -282 (-31) | -115 (-26) | -634 (-62) | 1127 |  |
| skip against 60m CBC (shorts only) | -221 (+8) | -125 (-59) | -272 (-44) | -111 (-28) | -618 (-95) | 1030 |  |

Walk-forward: picked on thirds 1-2 = **skip against 5-day EMA** → third 3 beyond random **+71** (rank 2 of 12).

### 3. Session stops (current exits, no filter) — 17 of 79 qualify (✓); top 8 qualifying, then top 5 overall

| Rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|
| session, only after 5 losing sessions: 2 losses or 3 flip-outs | -173 (+32) | -30 (+27) | -175 (+45) | -66 (+11) | -378 (+104) | 950 | ✓ |
| session, only after 5 losing sessions: 2 losses | -173 (+32) | -30 (+27) | -181 (+42) | -66 (+11) | -384 (+101) | 955 | ✓ |
| session, only after 5 losing sessions: 2 losses or 2 flip-outs | -187 (+17) | -16 (+40) | -186 (+32) | -70 (+7) | -389 (+89) | 943 | ✓ |
| sub-session losses: Asia off / London 1 / NY 1 | -190 (+22) | -8 (+34) | -196 (+21) | -84 (-3) | -394 (+78) | 930 | ✓ |
| sub-session losses: Asia 1 / London 1 / NY 1 | -176 (+15) | +10 (+35) | -163 (+27) | -72 (-0) | -328 (+77) | 800 | ✓ |
| sub-session losses: Asia off / London 1 / NY 3 | -192 (+43) | -47 (+15) | -217 (+17) | -90 (-6) | -456 (+75) | 1047 | ✓ |
| sub-session losses: Asia 1 / London 1 / NY 3 | -178 (+36) | -28 (+16) | -184 (+23) | -78 (-4) | -390 (+75) | 917 | ✓ |
| sub-session losses: Asia off / London 1 / NY off | -192 (+43) | -36 (+27) | -233 (+3) | -90 (-6) | -460 (+74) | 1053 | ✓ |

Walk-forward: picked on thirds 1-2 = **sub-session losses: Asia off / London 1 / NY off** → third 3 beyond random **+3** (rank 65 of 79).

### 4. Combined (the best qualifying rule of each step)

- Exits: none qualified (kept current)
- Filter: skip against 5-day EMA
- Session stop: session, only after 5 losing sessions: 2 losses or 3 flip-outs

| Filter / stop / exits | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|
| filter / stop / current exits | -113 (+54) | +29 (+43) | -100 (+70) | -44 (+19) | -184 (+167) | 692 | ✓↑ |
| filter / — / current exits | -140 (+54) | +14 (+42) | -115 (+71) | -25 (+43) | -241 (+167) | 804 | ✓↑ |
| — / stop / current exits | -173 (+32) | -30 (+27) | -175 (+45) | -66 (+11) | -378 (+104) | 950 | ✓↑ |
| — / — / current exits | -254 (+0) | -87 (+0) | -259 (+0) | -91 (+0) | -600 (+0) | 1183 | ↑ |

**Full stats, after costs** (trades / net / win % / profit factor / max drawdown)

| Period | Current exits | Best combined (filter / stop / current exits) |
|---|---|---|
| Third 1 | 389 / -254 / 49 % / 0.79 / 319 | 216 / -113 / 51 % / 0.83 / 167 |
| Third 2 | 388 / -87 / 53 % / 0.92 / 169 | 244 / +29 / 55 % / 1.05 / 90 |
| Third 3 | 406 / -259 / 50 % / 0.77 / 314 | 232 / -100 / 52 % / 0.84 / 168 |
| Last 4 wk | 109 / -91 / 48 % / 0.72 / 95 | 54 / -44 / 48 % / 0.75 / 48 |
| Whole | 1183 / -600 / 50 % / 0.83 / 607 | 692 / -184 / 53 % / 0.90 / 195 |

## MGC 5m — current exits: 1163 setups 01/06–11/06

Current exits after costs: Third 1 -244, Third 2 +37, Third 3 -163, Last 4 wk -138, Whole -370. Full stats (trades / net / win % / profit factor / max drawdown): 1163 / -370 / 51 % / 0.90 / 384

### 1. Exit rules (Δ vs current exits after costs; T = better in all three thirds, 4 = better in the last 4 weeks)

**TP rule alone — Δ whole period**

| X min | 65 % | 75 % | 85 % |
|---|---|---|---|
| 10 | -72 4 | -86 4 | -30 4 |
| 15 | -52 4 | -62 4 | -1 4 |
| 20 | -58  | -70  | -46  |
| 25 | -53  | -59  | -44  |
| 30 | -50 4 | -38 4 | -42 4 |
| 40 | -35  | -4  | -23 4 |

**SL rule alone — Δ whole period**

| X min | close negative | close < 25 % | close < 50 % | half SL1 negative | half SL1 < 50 % |
|---|---|---|---|---|---|
| 10 | +35 4 | +12 4 | +36 4 | -12 4 | -19 4 |
| 15 | -51 4 | -60 4 | -157 4 | -34 4 | -98 4 |
| 20 | -34 4 | -69 4 | -154 4 | -29 4 | -123 4 |
| 25 | -36 4 | -3 4 | -17 4 | -59 4 | -61 4 |
| 30 | -13 4 | -27 4 | -9 4 | -15 4 | -25 4 |

Combinations better in all three thirds: 0 of 493. Top 5:

| Rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|

Walk-forward: picked on thirds 1-2 = **TP off + close if negative at 20 min** → third 3 Δ **-49** (rank 493 of 493; median +25).

### 2. Entry filters (current exits; net after costs, beyond random in brackets; ✓ = beyond random positive in all three thirds)

| Rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|
| skip against prev session close | -164 (+54) | +50 (-4) | -119 (+24) | -99 (+34) | -232 (+74) | 964 |  |
| skip against VWAP | -197 (+33) | +61 (+12) | -151 (+3) | -119 (+17) | -287 (+48) | 1053 | ✓ |
| skip against VWAP (shorts only) | -221 (+14) | +48 (+5) | -153 (+5) | -130 (+6) | -325 (+24) | 1098 | ✓ |
| skip against 5-day EMA | -148 (+56) | +30 (-43) | -113 (+11) | -114 (+13) | -231 (+23) | 796 |  |
| skip against 5-day EMA (shorts only) | -206 (+16) | +34 (-16) | -126 (+17) | -96 (+37) | -298 (+17) | 990 |  |
| skip against EMA200 slope 1 h | -242 (-21) | +53 (-1) | -103 (+34) | -96 (+35) | -292 (+12) | 953 |  |
| skip against EMA200 slope 1 h (shorts only) | -266 (-31) | +60 (+15) | -125 (+24) | -120 (+14) | -331 (+8) | 1065 |  |
| skip against prev session close (shorts only) | -261 (-29) | +39 (-7) | -141 (+11) | -116 (+19) | -363 (-25) | 1062 |  |
| skip against 60m CBC (shorts only) | -199 (+31) | +25 (-28) | -180 (-35) | -124 (+9) | -353 (-33) | 1006 |  |
| skip against 60m CBC | -186 (+24) | +27 (-45) | -160 (-37) | -125 (+2) | -319 (-58) | 820 |  |
| skip against EMA200 slope 3 h | -213 (+2) | -3 (-63) | -135 (-1) | -80 (+51) | -351 (-61) | 910 |  |
| skip against EMA200 slope 3 h (shorts only) | -248 (-15) | +6 (-43) | -160 (-13) | -119 (+14) | -403 (-71) | 1041 |  |

Walk-forward: picked on thirds 1-2 = **skip against prev session close** → third 3 beyond random **+24** (rank 2 of 12).

### 3. Session stops (current exits, no filter) — 11 of 79 qualify (✓); top 8 qualifying, then top 5 overall

| Rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|
| sub-session losses: Asia 1 / London off / NY 1 | -184 (+29) | +114 (+54) | -101 (+33) | -98 (+34) | -172 (+116) | 904 | ✓ |
| sub-session losses: Asia 1 / London 3 / NY 1 | -184 (+29) | +114 (+54) | -106 (+28) | -102 (+29) | -176 (+111) | 903 | ✓ |
| sub-session losses: Asia off / London off / NY 1 | -230 (+3) | +94 (+49) | -142 (+10) | -133 (+2) | -277 (+63) | 1069 | ✓ |
| sub-session losses: Asia off / London 3 / NY 1 | -230 (+3) | +94 (+49) | -147 (+5) | -137 (-3) | -282 (+58) | 1068 | ✓ |
| sub-session losses: Asia 1 / London off / NY off | -199 (+26) | +56 (+4) | -122 (+23) | -103 (+32) | -265 (+53) | 998 | ✓ |
| sub-session losses: Asia 1 / London 3 / NY off | -199 (+26) | +56 (+4) | -127 (+18) | -108 (+27) | -269 (+48) | 997 | ✓ |
| sub-session losses: Asia 1 / London off / NY 2 | -210 (+13) | +68 (+14) | -126 (+18) | -109 (+26) | -267 (+45) | 981 | ✓ |
| sub-session losses: Asia 1 / London off / NY 3 | -209 (+15) | +56 (+4) | -122 (+23) | -103 (+32) | -275 (+42) | 995 | ✓ |
| sub-session losses: Asia 2 / London off / NY 1 | -206 (+22) | +99 (+48) | -151 (-4) | -138 (-4) | -257 (+66) | 1016 |  |
| sub-session losses: Asia 1 / London 2 / NY 1 | -218 (-7) | +111 (+49) | -110 (+23) | -89 (+42) | -217 (+65) | 884 |  |

Walk-forward: picked on thirds 1-2 = **sub-session losses: Asia 1 / London off / NY 1** → third 3 beyond random **+33** (rank 1 of 79).

### 4. Combined (the best qualifying rule of each step)

- Exits: none qualified (kept current)
- Filter: skip against VWAP
- Session stop: sub-session losses: Asia 1 / London off / NY 1

| Filter / stop / exits | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|
| filter / stop / current exits | -143 (+63) | +128 (+60) | -82 (+47) | -81 (+49) | -98 (+170) | 840 | ✓↑ |
| — / stop / current exits | -184 (+29) | +114 (+54) | -101 (+33) | -98 (+34) | -172 (+116) | 904 | ✓↑ |
| filter / — / current exits | -197 (+33) | +61 (+12) | -151 (+3) | -119 (+17) | -287 (+48) | 1053 | ✓↑ |
| — / — / current exits | -244 (+0) | +37 (+0) | -163 (+0) | -138 (+0) | -370 (+0) | 1163 | ↑ |

**Full stats, after costs** (trades / net / win % / profit factor / max drawdown)

| Period | Current exits | Best combined (filter / stop / current exits) |
|---|---|---|
| Third 1 | 402 / -244 / 50 % / 0.82 / 288 | 282 / -143 / 49 % / 0.85 / 157 |
| Third 2 | 379 / +37 / 54 % / 1.03 / 101 | 281 / +128 / 57 % / 1.17 / 81 |
| Third 3 | 382 / -163 / 48 % / 0.86 / 258 | 277 / -82 / 50 % / 0.90 / 161 |
| Last 4 wk | 105 / -138 / 42 % / 0.62 / 153 | 80 / -81 / 46 % / 0.70 / 95 |
| Whole | 1163 / -370 / 51 % / 0.90 / 384 | 840 / -98 / 52 % / 0.96 / 163 |

