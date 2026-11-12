# Current baseline (updated 11/07/2026)

Use these as the working versions going forward:

| File | Project path | Notes |
|---|---|---|
| CBC v10.82 | NOT in the project (project full on 11/07; file delivered in chat as CBC_v10_82.pine). Last project copy: pine/CBC_v10_77.pine | Main indicator. v10.82 = v10.81 (user upload 11/07) + MES 3m TP1 2.0 -> 1.75 x ATR (default "TP1 x ATR per symbol/timeframe" = "MES 3m 1.75"; reverts v10.67). Basis: 11/07 replay of the live MES 3m exits, 117 setups: 1.75 +202.6 vs 2.0 +184.5, middle third +13.7 vs +1.2. v10.78-v10.81 (bot risk sizing, exit rules, CE10117 fix via ESLib3 v7, flip-timing gates) are only in the uploaded/delivered files |
| ESLib (upload "ESLib_63") | pine/ESLib.pine | CBC imports `samuelsuss8/ESLib/60` (marked PLACEHOLDER in CBC) |
| ESLib2 (upload "ESLib2_27") | pine/ESLib2.pine | CBC imports `samuelsuss8/ESLib2/31` (PLACEHOLDER) |
| ESLib3 | pine/ESLib3.pine | v10.80+ imports ESLib3/7 (PLACEHOLDER per v10.80 changelog); project copy may be older |
| M2K 3m export | data/M2K_3m_110326.csv | CME_MINI:M2K1! 3m, 1,053 bars, 10/28 14:21 – 10/30 20:57 UTC, CBC export columns |

Live MES 3m exits (v10.82): SL1 3 x ATR (min 5), TP1 1.75 x ATR, no SL1/TP1 caps, 80 % at TP1 + BE + trail 1.7 inside 0600-1600 / 1800-2230 ET, 100 % outside.
Live MGC 3m exits: base (SL1 1.7 ATR + min 5, TP1 1.7 ATR cap 6, 80 %, BE, trail 1.7, no time stop).
Note: the weekday SL/TP grid routine prompt still describes MES 3m as on the base exits -- its step 5 is stale.

Decision 11/07/26 09:22 (user): no per-symbol/timeframe "no new setups" hours yet -- keep studying via the weekly hour-loss routine (claude/hour_loss_weekly_report.md). Proposed but NOT applied: MES 3m bot entry window 0300-1400 -> 0300-1300 (block 13-15 ET, the only !! block that also lost on setups after 11/03: 5 new, -44 pts; 22 setups / -82 pts total). Revisit after 2-3 more weekly runs; judge on setups added since the previous run, since the weekly report is cumulative. MNQ 3m loses at most hours (-948 pts) -- looks like a chart/exit problem, not an hour problem.

Open item: project is at its size limit -- remove old pine versions (e.g. CBC_v10_75/76) or old web/index versions to make room for CBC v10.82.
Open item: confirm the real published ESLib / ESLib2 / ESLib3 numbers and update CBC's import lines.
Watch (claude/mes3_ema_grid_report.md, 11/04): MES 3m slow chart EMA 14 / 16 vs 20 -- not robust yet.
Watch: MES 3m TP1 1.75 vs 2.0 on the weekday SL/TP grid (edge is modest; v10.67 had moved it the other way on 11/04).
Watch from v10.77 load: MGC 2m net per setup vs −0.40/setup (138 setups 10/19–11/05).
