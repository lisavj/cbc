# TP1 % vs HTF flip exits -- 2026-11-14 13:53 ET

STUDY SETTINGS STALE: claude/settings_sync_report.md (11/13 16:47 ET) lists 3 non-"known" MISMATCHes -- mes3_ema_grid LIVE part 'tod' (live MES 3m = 100 %), chop_sim EXIT MES 3m part 'tod' and EXIT MGC 3m 50 % / trail 3.5 (live = 0 % / no trail). tp1flip_study.py models the live exits itself (lp / lm), but it builds the setup sequence with cs.EXIT, so which setups get replaced by the next one still follows the old exits. Effect on the ranking is likely small but not zero.

Settings check: CBC_SETTINGS.md (v10.96) and the newest pine/CBC_v10_97.pine both have ats_part_sym "MES 3m 100, MGC 3m 0", ats_pw_sym "", ats_trl_sym "MGC 3m 0" = same as the v10.96 defaults. Live constants unchanged (MES TRAIL 100 %, MGC FLIP 0 %). v10.97 only adds the "Environment: EMA200 vs VWAP" checkbox (default OFF), not modelled.

Baseline note: claude/mes3_ema_grid.py got an 11/14 fix (MCase.gen now sets X4, so the MGC 3m 4-ATR VWAP stretch gate really blocks setups). MGC 3m now replays 1142 setups instead of the larger pre-fix set, so MGC numbers are NOT comparable with the 11/13 baseline. MES 3m (X4 off) is unaffected; its change is just one more week of data.

## MES 3m -- 1738 setups; live = TRAIL 100 % at TP1 (CBC v10.96 defaults: MES 3m TRAIL 100 %, MGC 3m FLIP 0 % = 0 % at TP1 + trail 0)

| Exit | Close at TP1 | Net | Δ vs live | z | Thirds | Last 4 wk | Win % | Max DD |
|---|---|---|---|---|---|---|---|---|
| TRAIL | 0 % | -1124 | -314 | -1.6 | -116 / -896 / -113 | +129 | 36 % | 1381 |
| TRAIL | 25 % | -1046 | -235 | -1.2 | -89 / -853 / -103 | +125 | 48 % | 1283 |
| TRAIL | 50 % | -967 | -157 | -0.8 | -63 / -810 / -94 | +121 | 48 % | 1213 |
| TRAIL | 75 % | -889 | -78 | -0.4 | -37 / -766 / -85 | +118 | 48 % | 1142 |
| **TRAIL (live)** | 100 % | -811 | +0 | +0.0 | -11 / -723 / -76 | +114 | 48 % | 1072 |
| FLIP | 0 % | -912 | -102 | -0.5 | -80 / -875 / +43 | +191 | 25 % | 1274 |
| FLIP | 25 % | -887 | -76 | -0.4 | -63 / -837 / +13 | +172 | 48 % | 1218 |
| FLIP | 50 % | -861 | -51 | -0.3 | -46 / -799 / -17 | +152 | 48 % | 1169 |
| FLIP | 75 % | -836 | -25 | -0.1 | -29 / -761 / -47 | +133 | 48 % | 1120 |
| FLIP-noBE | 0 % | -958 | -148 | -0.7 | -149 / -894 / +85 | +206 | 34 % | 1393 |
| FLIP-noBE | 25 % | -921 | -111 | -0.6 | -115 / -851 / +44 | +183 | 37 % | 1302 |
| FLIP-noBE | 50 % | -885 | -74 | -0.4 | -80 / -808 / +4 | +160 | 43 % | 1223 |
| FLIP-noBE | 75 % | -848 | -37 | -0.2 | -46 / -766 / -36 | +137 | 48 % | 1147 |
| FLIP+SL | - | -958 | -148 | -0.7 | -149 / -894 / +85 | +206 | 34 % | 1393 |

Largest: TRAIL 100 % = -811. Better than live in all three thirds: none

## MGC 3m -- 1142 setups; live = FLIP 0 % at TP1 (CBC v10.96 defaults: MES 3m TRAIL 100 %, MGC 3m FLIP 0 % = 0 % at TP1 + trail 0)

| Exit | Close at TP1 | Net | Δ vs live | z | Thirds | Last 4 wk | Win % | Max DD |
|---|---|---|---|---|---|---|---|---|
| TRAIL | 0 % | +600 | -42 | -0.4 | +290 / +1 / +310 | +288 | 20 % | 257 |
| TRAIL | 25 % | +449 | -192 | -0.6 | +204 / +5 / +240 | +227 | 50 % | 223 |
| TRAIL | 50 % | +299 | -343 | -1.0 | +118 / +10 / +171 | +166 | 50 % | 190 |
| TRAIL | 75 % | +148 | -494 | -1.5 | +32 / +14 / +102 | +105 | 50 % | 159 |
| TRAIL | 100 % | -2 | -644 | -1.9 | -54 / +19 / +33 | +44 | 50 % | 176 |
| **FLIP (live)** | 0 % | +642 | +0 | +0.0 | +356 / -10 / +297 | +262 | 18 % | 246 |
| FLIP | 25 % | +481 | -161 | -0.5 | +253 / -3 / +231 | +208 | 50 % | 214 |
| FLIP | 50 % | +320 | -322 | -1.0 | +151 / +4 / +165 | +153 | 50 % | 184 |
| FLIP | 75 % | +159 | -483 | -1.5 | +49 / +11 / +99 | +99 | 50 % | 157 |
| FLIP-noBE | 0 % | +409 | -233 | -0.9 | +198 / +69 / +142 | +221 | 28 % | 329 |
| FLIP-noBE | 25 % | +306 | -336 | -1.0 | +135 / +57 / +114 | +177 | 32 % | 269 |
| FLIP-noBE | 50 % | +203 | -439 | -1.4 | +72 / +44 / +87 | +133 | 37 % | 215 |
| FLIP-noBE | 75 % | +100 | -542 | -1.6 | +9 / +31 / +60 | +89 | 50 % | 169 |
| FLIP+SL | - | +409 | -233 | -0.9 | +198 / +69 / +142 | +221 | 28 % | 329 |

Largest: FLIP 0 % = +642. Better than live in all three thirds: none

## Verdicts

- **MES 3m: no change.** Live TRAIL 100 % -811 (thirds -11 / -723 / -76, last 4 wk +114). No variant is better in all three thirds; every variant is worse in total (all z <= 0). Closest: FLIP 75 % -25 (z -0.1), FLIP-noBE 75 % -37 (z -0.2). Same picture as 11/13 (everything within about +-150 of live, leaders = higher % at TP1).
- **MGC 3m: no change.** Live FLIP 0 % +642 (+356 / -10 / +297, last 4 wk +262, max DD 246, win 18 %) is the largest net of all variants. Closest: TRAIL 0 % -42 (z -0.4; thirds +290 / +1 / +310 = better only in the middle third; last 4 wk +288 > live) and FLIP 25 % -161 (z -0.5).
- **MGC 3m revert watch:** FLIP 0 % +642 vs TRAIL 50 % (old default, trail 3.5) +299 -> FLIP 0 % better by +343 in total, better in 2 of 3 thirds (+356 vs +118, -10 vs +10, +297 vs +171) and better in the last 4 weeks (+262 vs +166, +96). Revert flag NOT raised.

## Tallies

- MES 3m weeks robust: FLIP 75 % 0/3 · FLIP-noBE 75 % 0/3
- MGC 3m weeks robust: TRAIL 0 % 0/3 · FLIP 25 % 0/3
- MGC FLIP 0 % weeks held: 1 (revert-flag streak 0/2)

## History

| Run | MES live TRAIL 100 % (thirds / last 4 wk) | MES best challengers | MGC live FLIP 0 % (thirds / last 4 wk) | MGC TRAIL 50 % (old) | MGC best challengers | Verdict |
|---|---|---|---|---|---|---|
| 11/13 baseline | -796 (-11 / -723 / -62, +128) | all within ~+-150 | +557 (+292 / -96 / +360, +299) | +178 (+69 / -38 / +147) | TRAIL 0 % +512, FLIP 25 % +379 | MGC switched to FLIP 0 % (user, not yet robust) |
| 11/14 13:53 ET | -811 (-11 / -723 / -76, +114) | FLIP 75 % -25 (z -0.1), FLIP-noBE 75 % -37 | +642 (+356 / -10 / +297, +262) * | +299 (+118 / +10 / +171) * | TRAIL 0 % -42 (z -0.4), FLIP 25 % -161 (z -0.5) | no change; revert not flagged |

\* after the 11/14 X4 gate fix (1142 MGC setups); not comparable with earlier MGC rows.
