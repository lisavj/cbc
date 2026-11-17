# CBC Study Ledger -- updated 2026-11-16 23:34 ET

**At a glance** (newest CBC Pine = **v10.97** (11/14), unchanged; branch indicator **CBC EMA Slope v1.23** (11/15); CBC_SETTINGS.md still says v10.96)
- Open changes: **15** -- **C-010 RE-FLAGGED 11/16: MES 3m chart exits 80 % at TP1 + BE + trail 1.3** (mes_sltp_grid "Ready to change: YES", ✱ T R on 125 setups, source says low conviction) · C-018 MES 2m no new setups 14-15 ET · C-019 MNQ 2m 03-04 / 13-14 / 20-21 · C-006 MES 3m 06-07 + 13-15 · C-007 MGC 2m 04-05 / 07-08 / 21-22 · C-009 MNQ 3m 06-07 / 12-14 / 20-21 · C-011 MES 5m EMAs 16 / 34 / 120 · C-012 MES 5m ER 0.18 · C-013 / C-014 MGC 2m / 5m London alert window to 09:30 · C-015..C-017 alert-type unticks · C-002 MES 3m flip-timing gate 5 · C-003 MGC 2m LTF pierce cooldown 5. None is in v10.97.
- Done in the last 7 days (11/10-11/16): CBC v10.88-v10.97 (bot trigger / flip-only exit / news blackout; v10.95 MES 3m 100 % at TP1; v10.96 MGC 3m FLIP 0 %; v10.97 EMA200-vs-VWAP checkbox OFF); branch EMA Slope v1.13-v1.23. Nothing new done today.
- Monday 11/16 runs seen: only **cbc_daily 17:27** and **MES / MGC 3m SL-TP grid 17:27**. MES watch (17:37) and room daily (17:47) reports still show 11/13. **8 report docs are no longer in the project** (alert_param, breakout_flip, ob_setup, stop_sweep, evening_session, flip_timing, sl_reversal, room_study) -- removed after 11/15 (project knowledge over its limit, 2.03 / 2.00 MB); their studies' last known runs are kept below. Stale studies: **none yet** -- but settings sync is stale after Tue 11/17 16:47, the weekday studies without a Monday report (MES watch, room daily, alert param, breakout + flip-ER) after Tue 11/17 ~17:05-17:48, stretch filter after Wed 11/18 17:09.
- Live data problems (cbc_daily 11/16): **MES 2m CBC alert silent since Sun 11/15 19:22 ET**; MES 3m alerts stopped after 14:30 ET; **MES 3m 100 %-at-TP1 closes send no "Setup Ended"** (v10.95 side effect? -> MES 3m live stats since v10.95 biased toward losers; 2 TP1 winners ≈ +12 each unrecorded today); MGC 3m alert silent Sun 22:21 -> Mon 14:39; MES 5m alerts silent since 11/12 (last MES watch). Alert store still not de-duplicated.
- Settings sync (11/13 16:47, Tue/Thu/Fri): v10.96, **3 MISMATCH** still open (MES 3m 'tod' in mes3_ema_grid LIVE + chop_sim EXIT; MGC 3m 50 % / 3.5 in chop_sim EXIT). Next sync Tue 11/17 should pick up v10.97.

## 1. Changes warranted (open)

| ID | Flagged | Last confirmed | Chart | Exact change | Evidence | Source | Status |
|---|---|---|---|---|---|---|---|
| C-010 | 11/09 (re-flagged 11/16) | 11/16 | MES 3m (chart copy only; bot stays 100 %) | ats_part_sym = "MES 3m 80, MGC 3m 0" (was MES 3m 100) + ats_trl_sym = "MGC 3m 0, MES 3m 1.3" (BE at TP1 stays on) -- i.e. 80 % at TP1 + BE + trail 1.3 ATR, SL1 3 / TP1 1.75 unchanged | 11/16 (125 setups): stop 3.0 / TP1 1.75 / 80 % / trail 1.3 = **+140.7 ✱ T R** (halves +61.2 / +79.6, thirds +42.5 / +2.3 / +96.0); with BE exact levels +145.4; beats live 100 % proxy (+127.3 ✱ T R) by +13.4, edge all in the last third; same row R -> not R -> R over the last 3 runs; "Ready to change: YES", source: "rule met on paper, low conviction ... otherwise no change and re-check after ~20 more live v10.95 setups". Earlier: 11/12 trail 1.3 +189.2 R; 11/13 +159.5 ✱ not T (withdrawn) | mes_sltp_grid_report.md | **OPEN -- re-flagged 11/16** (was WITHDRAWN 11/13: no longer met rule + v10.95 100 % at TP1 left no runner); not in v10.97 (ats_part_sym "MES 3m 100, MGC 3m 0", ats_trl_sym "MGC 3m 0") |
| C-018 | 11/14 | 11/14 | MES 2m | Pine change needed: no new setups 14:00-15:00 ET on MES 2m (or alert_hours_sym MES 2m windows that skip 14-15) | 11/14: 14-15 n 15, losers 67 %, net -23.0, halves 71 % (7) / 62 % (8), 7d 60 % (5); !! held 2 runs (11/07, 11/14); meets rule "!! both halves, n >= 8, held 2+ runs" | hour_loss_weekly_report.md | OPEN -- NEW 11/14; not in v10.97. Note: EMASlope branch handoff lists "MES 2m block 06-07" (different hour) as not implemented |
| C-019 | 11/14 | 11/14 | MNQ 2m | Pine change needed: no new setups 03-04, 13-14 and 20-21 ET on MNQ 2m | 03-04 n 12 · 75 % · -181.4 (60 % / 86 %); 13-14 n 15 · 67 % · -98.4 (62 % / 71 %); 20-21 n 9 · 78 % · -57.9 (60 % / 100 %); 03-04 / 13-14 held 2 runs, 20-21 3 runs; also block 19-22 42 · -146.4 | hour_loss_weekly_report.md | OPEN -- NEW 11/14 (replaces withdrawn C-008); not in v10.97 |
| C-011 | 11/13 | 11/13 | MES 5m | "Chart EMA fast / slow / 200" = 16 / 34 / 120 on the MES 5m chart only (per-symbol route: ema_f_sym "MES 5m 16", ema_s_sym += "MES 5m 34"; EMA200 length 120 has no per-symbol list -> set on the MES 5m CBC copy); recreate the MES 5m alert | "UPDATE WARRANTED (confirmed by the Friday run)": N 16/34/120 robust 3 consecutive weekly runs (10/31, 11/06, 11/13) +504, z 3.2, thirds +200 / +136 / +168; neighbours I 16/34/200 (+466, z 3.1), H 14/30, L 20/40 robust; live MES 5m LTF EMA20 Pierce on 9/20 44 ended -19.8; htf_ema A+ robust 8 runs in a row | ema5_report.md (+ htf_ema_report.md; 11/15 run 9: A+ +504 z 3.2 robust 9 runs in a row, C+ / G+ / H+ 9 runs, I+ 5 runs) | OPEN -- not in v10.97 (ema_f_sym "", ema_s_sym "MES 2m 14") |
| C-012 | 11/13 | 11/13 | MES 5m | ③ Trade Setup Filters "Block in chop: Efficiency Ratio below" (ats_c_er) = 0.18 on the MES 5m chart's CBC copy only (global default stays 0.23; a per-symbol ER list would need a Pine change); recreate the MES 5m alert | "UPDATE WARRANTED -- MES 5m": robust [3] 11/01 +183 z 2.3, 11/07 +187 z 2.3, 11/13 +198 z 2.5, thirds +37 / +51 / +110; neighbour 0.20 robust [3] (+148 z 2.3); latest third positive all 3 runs (+94 / +99 / +110) | filter_sweep_report.md | OPEN -- chart input; not verifiable from defaults (ats_c_er 0.23 in v10.97) |
| C-013 | 11/13 | 11/13 | MGC 2m | ⑤ Alerts "London window" 0300-0745 -> 0300-0930 (or NY start 09:30 -> 07:45) on the MGC 2m copy; recreate the alert | "UPDATE WARRANTED (3-run rule met)": 07:45-09:30 gap 165 setups +79, thirds +7 / +11 / +61, avg +0.48 vs +0.16 inside; with range gate on 146 / +65 (+3 / +35 / +27); 3/3 runs | all_alerts_report.md | OPEN -- not in v10.97 (alert_london_window "0300-0745") |
| C-014 | 11/13 | 11/13 | MGC 5m | ⑤ Alerts "London window" 0300-0745 -> 0300-0930 on the MGC 5m copy; recreate the alert | gap 137 setups +141, thirds +48 / +36 / +57, avg +1.03 vs -0.25; 3/3 runs | all_alerts_report.md | OPEN -- not in v10.97 |
| C-015 | 11/13 | 11/13 | MES 3m, MNQ 3m, MES 2m, MGC 2m, MES 5m, MGC 5m | Untick alert "Price Enters HTF EMA9/20 Zone - Entry" on those charts (not MGC 3m: 1 run) | both exit rules negative 3 runs, 30+ alerts each | all_alerts_report.md | OPEN -- chart alert ticks; not verifiable from defaults |
| C-016 | 11/13 | 11/13 | MES 3m, MNQ 3m, MES 2m, MES 5m | Untick "Alert: EMA20 Touch - Pullback Entry (LTF/HTF)" on those charts (MGC charts: wait) | both exit rules negative 3 runs, 30+ alerts each | all_alerts_report.md | OPEN -- chart alert ticks |
| C-017 | 11/13 | 11/13 | MES 2m | Untick "A+ Setup (Long/Short)" alert | 279 alerts, (a) -187 / (b) -117, 3 runs | all_alerts_report.md | OPEN -- chart alert tick |
| C-001 | 11/06 | 11/09 | MES 2m | ats_fl2_sym = "MGC 2m 1, MES 2m 1" | 11/12: flop row 65 · -65.4, halves -66.3 / +0.9; 11/16: 67 · -66.5 (-67.8 / +1.3) | cbc_daily_report.md | WITHDRAWN 11/12 (2nd half positive) |
| C-002 | 11/07 | 11/13 | MES 3m | ats_fw_sym = "MES 3m 5" (ats_fw2_sym "MES 3m 8" already set) | 11/13 (4th straight check): sim 243 · -93.3, thirds -37 / -51 / -5; HTF EMA9 sub-cell 60 · -61.9; live 18 · -14.2 (none in 5-8 since v10.81); cbc_daily 11/16: 05:36 LTF pierce 1 HTF bar after flip -> nothing late | flip_timing_report.md (doc no longer in project after 11/15) | OPEN -- gate built v10.81 but OFF (ats_fw_sym "" in v10.97) |
| C-003 | <=11/07 (5th run) | 11/13 (9th run) | MGC 2m | ltf_ema20_pierce_cooldown = 5 (MGC 2m chart only) | 1052 alerts at current; cd 5: (a) -330.4 vs -513.1, (b) +100.4 vs +20.3; validation 81 / 76 %; still negative under (a) ("less bad") | alert_param_report.md (doc no longer in project after 11/15) | OPEN -- not in v10.97 (default 3) |
| C-004 | 11/07 (1st run) | 11/07 | MES 2m | ltf_ema20_pierce_cooldown = 5 (MES 2m chart only) | 11/13: still unreliable (validation 65 / 67 %) | alert_param_report.md | WITHDRAWN 11/09 (replay validation < 70 %) |
| C-005 | 11/07 (1st run) | 11/12 (4th run) | MES 3m | ltf_ema20_pierce_cooldown = 8 (MES 3m chart only) | 11/13: 8 still best and ✱ ((a) +148.8 vs -215.0, (b) +203.5 vs +33.9) but neighbour 5 worse than current (-125.2 / -68.1) | alert_param_report.md | **WITHDRAWN 11/13** ("no change yet: neighbours disagree", isolated spike at 8) |
| C-006 | 11/07 | 11/14 | MES 3m | Pine change needed: no new setups 06-07 and 13-15 ET (alert_hours_sym already mutes 13:00-14:00 alerts; bot_win drops 13:00-14:00 since v10.87) | 11/14 (3rd run): 06-07 10 · 70 % · -18.2 (67 % / 75 %); 13-14 9 · -49.9; 14-15 13 · -32.3; block 13-15 22 · -82.2, all !! held 3 runs; block 06-08 grew to 06-09 (20 · -68.1); only 5 new MES 3m setups this week | hour_loss_weekly_report.md | OPEN -- partly covered (alerts + bot only); not in v10.97. EMASlope branch v1.07+ has a MES 3m 13-15 block (sessions_report: NY PM -234 -> -45; time_blocks robust combo +291 z 2.9) |
| C-007 | 11/07 | 11/14 | MGC 2m | Pine change needed: no new setups 04-05, 07-08, 21-22 ET (or alert_hours_sym MGC 2m windows) | 11/14 (3rd run): 04-05 17 · 76 % · -33.6; 07-08 11 · 82 % · -31.2; 21-22 18 · 72 % · -51.3, all !! 3 runs; block 04-08 61 · -91.2; 06-07 new !! (if it holds next week the whole 04-08 block qualifies); cbc_daily 11/16: MGC 2m losers 04:04 -5.3, 07:30 -5.0 | hour_loss_weekly_report.md | OPEN -- not in v10.97. Note: C-013 would open MGC 2m alerts 07:45-09:30 (overlaps the 07-08 block) |
| C-008 | 11/07 | 11/07 | MNQ 2m | Pine change needed: no new setups 04-05 and 14-15 ET | 11/07: live 14 / -45.5; 14 / -77.2. 11/14: 04-05 19 · -14.7, 14-15 20 · -4.9 -> only "!" | hour_loss_weekly_report.md | **WITHDRAWN 11/14** (both hours dropped off the blocking list; MNQ 2m now C-019) |
| C-009 | 11/07 | 11/14 | MNQ 3m | Pine change needed: no new setups 06-07, 12-14 and 20-21 ET (widened 11/14 from 06-07 + 13-14) | 11/14: 06-07 10 · -109.2 (3 runs); 12-14 block 20 · -274.9 (13-14 3 runs, 12-13 new to list); 20-21 8 · -73.0 (3 runs, n now >= 8); MNQ 3m chart net -1028.5 on 120 setups | hour_loss_weekly_report.md | OPEN -- not in v10.97. EMASlope branch mnq_report: candidate MNQ 3m set slope 0.75 + FLIP 0 % (+6261 z 5.1) would change the base |

## 2. Changes made

| Date | Version | Chart | Change | Why (evidence) | Follow-up / latest check |
|---|---|---|---|---|---|
| 11/15 | branch CBC EMA Slope v1.16-v1.23 (separate indicator, not CBC v10.x) | 5m charts, MGC / M2K 2m, MGC 3m, MNQ 3m, M2K 3m | v1.17: new `ats_slk_sym` slope lookback per chart = "MES 5m 3, MGC 5m 3, MNQ 5m 3, M2K 5m 3, MGC 2m 4, M2K 2m 4"; v1.18: MGC 3m lookback "MGC 3m 5" + slope `ats_c_sl_sym` MGC 3m 0.3 -> 0.165; v1.19: MNQ 3m Max SL1 cap "MNQ 3m 60" + NY OR forming block OFF (new `ats_orbf_sym` "MNQ 3m 0"); M2K 3m `ats_slx_sym` "M2K 3m 3.5" + `ats_part_sym` "M2K 3m 0"; v1.16 / v1.20-v1.23 token-limit fixes, no logic change | slk_report 11/15 (5m 15 min best on all 4: MES 5m +316 z 3.6, MGC 5m +424 z 2.7; MGC 2m 8 min +409 z 3.7; M2K 2m robust plateau); all3v 11/15: MGC 3m 15-min 0.165 +601 z 1.8 PROMISING only (last 4 wk -51); MNQ 3m v1.19 +2511 z 3.9 robust; M2K 3m +111 z 2.6 robust (DD 25 -> 47) -- adopted before the 3-week check | **3m weekly watch (Tue 17:09) setup run 11/15**: tallies 0 / 0 / 0 (no bars since go-live 11/16); first real run Tue 11/17. revert rules: MGC since-go-live negative 3 runs or z < 1; MNQ / M2K old-settings row positive 3 runs or z > -1. blk119 11/15: MES 13-15 block + window to 19:00 confirmed. v1.23 compile not confirmed in project |
| 11/14 | v10.97 | all (built for MES 3m) | new ③ checkbox `ats_env_on` "Environment: long only when EMA200 > VWAP, short only when EMA200 < VWAP" = **false** (OFF, no behaviour change) | CBC Engine idea study 11/14 (cbce_report): MES 3m -241 vs -801, +560 z 2.5, all thirds better; tsf 11/14 +560 z 2.5 but last 4 wk -20; MGC 3m EMA200 -377 (keep off) | volflip watch 11/14: MES W1 +560 z 2.5, tallies 0/3; not modelled by other studies; settings sync not yet run on v10.97 |
| 11/14 | branch CBC EMASlope v1.13-v1.15 (separate indicator, not CBC v10.x) | all 12 charts (MES / MGC / MNQ / M2K x 2m / 3m / 5m) | per-chart HTF slope gate (e.g. MES 2m 0.75, MGC 2m 0.42, MNQ 2m 0.55 + FLIP 0 %, MES 5m 0.70 + stretch 4, MGC 5m 0.48, MNQ 5m stretch 7, MGC 5m SL1 cap 10, M2K cap 8 ...) | two_report / five_report / all5 / all / m2k / mnq / time_blocks / tsf 11/14: e.g. MES 2m +724 z 4.7, MNQ 2m +5825 z 4.8, MES 5m DD 877 -> 46 (in-sample replays) | EMASLOPE_HANDOFF: v1.15 compile NOT YET CONFIRMED; load on all 12 charts pending; MES 3m chart ATR length back to 14; 8 candidates not implemented. No scheduled study watches the branch yet |
| 11/13 | v10.96 | MGC 3m | ats_part_sym = "MES 3m 100, MGC 3m 0"; ats_trl_sym = "MGC 3m 0" -> exit "FLIP 0 %" (nothing closed at TP1, stop to BE, no trail; closed by HTF CBC flip against / BE / 16:00 / next setup). A listed 0 % is now honoured. Bot unaffected | user decision; tp1flip study 11/13: replay +557 vs +178 (TRAIL 50 %), thirds +292 / -96 / +360, last 4 wk +299, max DD 294, z 1.7 (not yet robust) | **tp1flip 11/14: HELD 1, revert streak 0/2** -- FLIP 0 % +642 vs TRAIL 50 % +299; mgc_sltp_grid 11/16: FLIP proxy +79.2 (not ✱, thirds -31.6 / -62.2 / +173.0) vs v10.84 50 % / 3.5 +62.5 -> "keep v10.96"; cbc_daily 11/16: live FLIP 0 % 4 · +2.1, judge at 20+; mgc_sl 11/13: keep SL1 1.7 + cap 7 |
| 11/13 | v10.95 | MES 3m (+ all) | ats_pw_sym = "" (was "MES 3m 0600-1600 80, MES 3m 1800-2230 80") -> MES 3m 100 % at TP1 all day; trail 0 in ats_trl_sym now = no trail | user decision; tp1flip study 11/13: MES 3m every variant within ±150, nothing better in all thirds | **mes_sltp_grid 11/16: live proxy 3.0 / 1.75 / 100 % +127.3 ✱ T R (R again)** but 80 % + trail 1.3 +140.7 R -> C-010 re-flagged; tp1flip 11/14: no change; live from 11/13: 3 recorded · -16.8 (all 11/16) + 2 TP1 winners ≈ +24 with no "Setup Ended" (cbc_daily 11/16: possible v10.95 side effect) |
| 11/13 | v10.94 | MES 3m bot | bot_news = "" (off), bot_nwm = 5 -- news blackout ± N min for bot entries | build (user) | not modelled; off by default |
| 11/12 | v10.93 | MES 3m bot | compile fix (CE10295), v10.89-92 logic moved into f_bot_send(); same behaviour | build | settings sync 11/12: no behaviour change |
| 11/12 | v10.91-92 | MES 3m bot | bot_fow = "0930-1600" (flip-only: no TP, closed by HTF CBC flip against / SL1 / 15:57 / next entry); bot_foall = "HTF CBC Flip only"; bot_fosl = true | user decision; flip_exit_bot_report 11/12: HTF CBC Flip 46 (bot windows) bracket+flip -73.5 -> flip+SL +52.2 (flip only +60.8, thirds +79 / -27 / +82); flip_exit_report: HTF Flip 90 -177.7 -> -54.6; LTF not beyond worse with flip exit (-80.9 -> -264.2) so kept on bracket | **flip-exit watch 11/14: HELD, weeks held 1** (flip+SL +52.2 vs -73.5, thirds +71 / -20 / +75); live HTF Flip bot trades 0 -> v10.92 not yet seen live; cbc_daily 11/16: 12:30 Flip S ≈ +11.6 in bot window (unrecorded TP1); flipwin 11/14 (branch): 09:30-16:00 +149 z 2.9 HELD |
| 11/12 | v10.89-90 | MES 3m bot | new bot_eow "Entry-only windows" = "" (off); bot_eof = false | build (user) | not in use (default off) |
| 11/12 | v10.88 | MES 3m bot | bot_t_ln = true (trigger "LTF EMA20 Pierce (not beyond EMA9)" ON; bot set = Flip + LTF beyond + LTF not beyond) | user decision; note: bot_alerts_report 11/12 said "keep unticked" (24 live bot-window trades -8.7, replay thirds -75 / -42 / +8) | **bot_trigger 11/14: run 1 of 3** -- replay thirds -75 / -42 / +13 (neg 2 of 3), live in bot windows 23 / +15.4 -> not a flag; cbc_daily 11/16: none today (23 · +6.4 unchanged); turning OFF Δ +105 (last 4 wk -97) |
| 11/08 | v10.87 | MES 3m bot | bot_win = "1830-2200, 0300-1300, 1500-1530" | 13:30-14:00 -198 pts, 3.5 SD from chance, neg every third; replay -674 -> -412 (mes3_time_zones_table.md) | botwin 11/14: 13:00-14:00 still 91 / -250 (-47 / -114 / -88) -> keep out; settings sync 11/13 inwin MATCH |
| 11/08 | v10.86 | MES 3m bot | bot_d5 = true (no shorts above 5-day EMA) | botwin + entry_slots: -702 -> -409; DD 907 -> 647 | **botwin 11/14: WEAKER 0/3** (-229, beyond random +2 / +108 / +28, last 4 wk +165 vs +174; not FAILED); cbc_daily 11/16: 5-day EMA above price, shorts allowed |
| 11/08 | v10.85 | MES 3m bot | bot_win = 6-window set | mes3_entry_slots_report.md: -735 -> -229 | superseded by v10.87 |
| 11/08 | v10.84 | MGC 3m | ats_part_sym += "MGC 3m 50"; ats_trl_sym = "MGC 3m 3.5" | runner 11/08: Δ +353 (50 % / 3.5), all thirds, last 4 wk +146 vs +66; walk-fwd rank 2/39 | **superseded 11/13 by v10.96** (FLIP 0 %); runner 11/14 still HELD 2/3 vs 80 % / 1.7 (Δ +285) but does not test FLIP 0 %; tp1flip 11/14: FLIP 0 % beats it by +343; mgc_sltp_grid 11/16: 50 % / 3.5 proxy +62.5 vs FLIP +79.2 |
| 11/07 | v10.83 | MGC 2m / MES 3m / MES 2m | vb_tw_sym += "MGC 2m 0000-2400 0.01, MES 3m 0000-2400 4, MES 2m 0000-2400 4" | alert_param 11/07: MGC 2m (a) +451 vs +102; MES 3m (a) +84 vs -61; MES 2m (a) +288 vs +111 | alert_param 11/13: MES 2m 4 best ((a) +268.5); MGC 2m 0 best ((a) +366.1); MES 3m 4 vs 0: replay unreliable (8 stored). Report doc no longer in project after 11/15 |
| 11/07 | v10.82 | MES 3m | ats_tp1_sym = "MES 3m 1.75" (reverts v10.67) | 117 setups: 1.75 +202.6 vs 2.0 +184.5 | mes3 watch (B) 11/13: keep 1.75; mes_sltp_grid 11/16: TP1 1.75 rows R (4 of 7 cells), TP1 2.25 row all R, TP1 2.0 no T |
| 11/07 | v10.81 | MES 2m / MES 3m | ats_fa_sym = "MES 2m 9"; ats_fw2_sym = "MES 3m 8" (from-list empty = OFF) | flip_timing: MES 2m 9-16 HTF sim 105 / -78.2 all thirds, live 14 / -27.8 | flip_timing 11/13: MES 2m 9-16 still weak (107 · -83.9), 0 live setups at 9+ since 11/06 -> gate working; MES 3m ON = C-002 |
| 11/06 | v10.79 | MES 3m / MGC 3m | xr_cut_sym "MES 3m" (21 min / 70 % / ATR 1.5x); xr_lock_sym "MGC 3m" (75 % -> +55 %); alerts only | 11/06 exit-ideas replay: MES +131 z 2.1; MGC +209 z 1.6 | mes3 watch (E) 11/13: live MES 1 hit (+6.19), MGC 2 comparable (+8.10); replay on current exits: MES cut +17 z 0.3, MGC lock on FLIP 0 % +28 z 0.1 -> "likely DROP" if live confirms |
| 11/06 | v10.77 | MGC 2m | ats_fl2_sym = "MGC 2m 1"; ats_rp_sym += "MGC 2m 5" | daily stats 11/05: non-flip FL 43 / -71.0; range-gated 25 / -35.9 | **cbc_daily 11/16: range gate now looks live** (12 bar violations all 11/09-11/12 = duplicate old alert, none since); flop gate live (last non-flip FL 11/12 05:32); since v10.77 68 · -35.5 (halves +0.9 / -36.3) |
| 11/06 | v10.77 | MES 3m bot | bot_win = "1830-2200, 0300-1400, 1500-1530" | evidence not found in project | superseded by v10.85 / v10.87 |
| 11/05 | v10.75 | MGC 3m / MES 3m | vb_tw_sym = "MGC 3m 0300-1700 0.01"; alert_hours_sym = "MES 3m 1830-2100, 0430-1300, 1400-1430" | MGC 3m sweep 11/05: (a) +$4,388 vs +$997 | alert_param 11/13: MGC 3m tod still best ((a) +387.9); all_alerts 11/13: MES 3m 22:30-03:00 gap 3/3 on paper but alert hours govern MES 3m -> no change |
| 11/05 | v10.71-76 | MES 3m bot | CrossTrade bot (Flip + LTF beyond EMA9), EOD 1557, no entries 1545, late cutoff 20 s, preview ON | build | trigger set changed v10.88; flip exit v10.92; news blackout v10.94 |
| 11/05 | v10.70 | MES 3m | ema_f_sym = "", ema_s_sym = "MES 2m 14" (MES 3m back to 9 / 20) | mes3_ema_watch: slow 14 not robust | mes3 watch 11/13: keep 9 / 20; ema716 11/14 (branch): 7/16 -39 z -0.1 -> keep 9 / 20 |
| 11/04 | v10.68 | MES 3m | ema_f_sym "MES 3m 7", ema_s_sym += "MES 3m 14" | mes3_ema_grid 11/04: slow 14 +293, z 1.1 | reverted v10.70 |
| 11/04 | v10.67 | MES 3m | ats_tp1_sym = "MES 3m 2" | grid 108 setups: 3.0 / 2.0 / 100 % +143.8 R | reverted v10.82 |
| 11/03 | v10.60 | MNQ 3m / MES 3m | ats_tw_sym = "MNQ 3m 0, MES 3m 0" (late-away OFF) | toward_report 11/03: MNQ 3m +1518 z 2.1, MES 3m +262 z 1.7 | no scheduled follow-up |
| 11/03 | v10.55-56 | MES 3m | ats_pw_sym = "MES 3m 0600-1600 80, MES 3m 1800-2230 80" (else 100 %) | tp1_tod_report 11/03: time mix +153.7 vs +139.2 | **superseded 11/13 by v10.95** (list emptied, 100 % all day) |
| 11/03 | v10.54 | MES 3m | ats_slx_sym "MES 3m 3", ats_tp1_sym "MES 3m 1.75", ats_part_sym "MES 3m 100", caps "MES 3m 0" | mes_sltp_grid 10/30 + 11/02: 3.0 / 1.75 / 100 % +141.6 vs +41.3 | mes_sltp_grid 11/16: live proxy R again (+127.3, thirds +52.0 / +4.1 / +71.2); cbc_daily 11/16: 23 recorded · -25.7 on these exits (TP1 winners since v10.95 under-recorded) |
| 11/02 | v10.52 | MGC 3m | ats_rpz_sym input (default empty) | rgate4 candidate +180 z 2.0 (run 1 of 3) | rgate 11/13: 0 robust runs (4.0 / 30 % +151 z 1.6, last 4 wk -28) |
| 11/01 | v10.51 | MES 2m | ema_s_sym = "MES 2m 14" | MES 2m replay Jun-Oct +206 z 1.7 | ema5 11/13: no revert flag |
| 10/30 | v10.48-49 | MGC 3m | shadow setups (VWAP-stretch blocked), default ON | replay: stretch filter still pays (+77) | stretch 11/12: 17 shadows, 11 wins, +18.1; keep "MGC 3m 4"; 11/14 X4 fix: the gate now really blocks in replays (mgc3_gate_session: stretch gate OFF loses in every session -> keep) |
| 10/29 | v10.47 | all | room line + room filters (default OFF) | 10/29 live | room_daily 11/13: MES 3m 0.2 x TP1 candidate (OOS 3 / 8); room_study 11/13: keep OFF |
| 10/28 | v10.45 | MGC 3m | MGC 3m back to base exits | daily stats revert flag 2 sessions | superseded by v10.84 / v10.96 |
| 10/27 | v10.42 | MES 2m / MES 3m | ats_f_flip_sym = "MES 2m 4"; MES 3m back to base exits | MES 2m flips >= 4 blocked 9 / -34.7 | cbc_daily 11/16: flip counter + MTF gate live (0 violations since 10/28); MES 2m alert dead since 11/15 19:22 |
| 10/20 | v10.32 | MES 2m | ats_mtg_sym = "MES 2m 1" | 16 against-MTF setups -21.9 | cbc_daily 11/16: gated row 16 / -21.9; xtf 11/12 baseline: MES 2m 1H gate not supported by replay; EMASlope branch v1.13 turns the MES 2m MTF gate OFF |
| 10/19 | v10.31 | MGC 3m / MES 3m | TP1 2.0, 50 / 80 % at TP1, no BE | replay 10/12-10/19 | superseded |

## 3. Watch list

| Item | Chart | Study | Tally | Latest numbers | Still needed |
|---|---|---|---|---|---|
| FLIP 0 % exit (live v10.96) -- revert watch vs TRAIL 50 % / 3.5 | MGC 3m | TP1 % vs flip study (Sat) + cbc_daily + mgc_sltp_grid | **weeks held 1; revert streak 0/2** (11/14) | 11/14: FLIP 0 % +642 (+356 / -10 / +297, last 4 wk +262) vs TRAIL 50 % +299; mgc_sltp_grid 11/16: FLIP proxy +79.2 vs 50 % / 3.5 +62.5 (neither ✱); live 4 · +2.1 (11/16) | "consider reverting" if FLIP 0 % worse than TRAIL 50 % (total, 2 of 3 thirds, or last 4 wk by > 30) on 2 consecutive runs; live judge at 20+ |
| Runner 50 % at TP1 + trail 3.5 (v10.84) | MGC 3m | runner (Sat) + cbc_daily | **SUPERSEDED 11/13** (v10.96); runner study HELD 2/3 (vs 80 % / 1.7 only) | 11/14: Δ +285 with rules (+150 / +28 / +108), plain +244 T4 | -- (revert fallback above) |
| MES 3m 100 % at TP1 all day (live v10.95) vs 80 % + trail 1.3 | MES 3m | TP1 % vs flip (Sat) + mes_sltp_grid (weekdays) | week 1 (11/14): no challenger in tp1flip; **mes_sltp_grid 11/16: challenger R -> C-010** | live proxy +127.3 ✱ T R; 80 % / trail 1.3 +140.7 ✱ T R (+13.4, last third only); tp1flip FLIP 75 % -25 z -0.1 (0/3); live 3 · -16.8 recorded + 2 unrecorded TP1 wins | ~20 more live v10.95 setups (source); fix missing "Setup Ended" on TP1 closes first |
| Bot flip-only exit for HTF CBC Flip 09:30-16:00 (live v10.92) | MES 3m bot | bot flip-exit watch (Sat) | **HELD, weeks held 1** (11/14) | +52.2 vs -73.5 (thirds +71 / -20 / +75); live HTF Flip bot trades 0 | HELD weekly; FAILED -> "consider reverting" (live 15+ worse by > 30); next trigger to switch: LTF beyond EMA9 -5.5 vs -19.8 (not consistent) |
| Bot trigger "LTF EMA20 Pierce (not beyond EMA9)" (live v10.88) | MES 3m bot | bot_trigger (Sat, data note 4) | **run 1 of 3** (11/14) | replay thirds -75 / -42 / +13 (neg 2 of 3); live in bot windows 23 / +15.4; cbc_daily 11/16 23 · +6.4; OFF Δ +105 (last 4 wk -97) | 2 more weekly runs + 20 new trades still negative live and in 2+ thirds -> "consider unticking" |
| Bot 5-day short filter (live v10.86) | MES 3m bot | botwin (Sat) | WEAKER 0/3 (11/09, 11/14) | 11/14: -229 vs current -469; beyond random +2 / +108 / +28; last 4 wk +165 vs +174 | 3 held weeks; not FAILED yet |
| Bot windows 13:00-14:00 removed (live v10.87) | MES 3m bot | botwin (Sat) | holds | 11/14: 91 / -250 (-47 / -114 / -88) | keep checking weekly |
| Room x TP1 < 0.2 skip | MES 3m | room_daily (weekdays) + cbc_daily | candidate; OOS 3 of 8 blocked (11/13) | 36 blocked / -47.4 (avg -1.32), halves -19.0 / -28.4, thirds -16.1 / -23.0 / -8.2; kept avg +0.27; OOS 3 / -2.4; cbc_daily 11/16: would have blocked 10:51 (0.12x, -0.75) and the unrecorded 14:27 TP1 winner (0.10x) | 8+ out-of-sample blocked (room daily 11/16 run not seen) |
| Skip against VWAP | MGC 3m | trend_guard (Sat) | **2/3** (11/14) | beyond random +190 (+64 / +47 / +79), last 4 wk +24 (stretch gate now in base; 80 % / 1.7 exits) | 1 more HELD week (then check on FLIP 0 % exits) |
| 5-day EMA + 2 losses / 2 flip-outs guard | MNQ 3m | trend_guard (Sat) | **2/3** (11/14) | beyond random +875 (+195 / +358 / +322); last 4 wk +761 | 1 more HELD week |
| 5-day EMA shorts-only filter | M2K 3m | trend_guard (Sat) | **2/3** (11/14) | beyond random +140 (+39 / +60 / +42); last 4 wk +22 | 1 more HELD week (m2k_report 11/14: treat M2K 3m as no-edge) |
| London stop after 1st loss | MGC 3m | all_rules (Sat) | **2/3** (11/14, "barely") | net +139; beyond random +91 (+66 / +24 / +1); last 4 wk +94 vs +101 | 1 more HELD week |
| VWAP filter + London stop | MGC 3m | all_rules (Sat) | **2/3** (11/14) | net +274; beyond random +234 (+95 / +50 / +88); last 4 wk +117 vs +101 | 1 more HELD week |
| Balanced set (filter / stop / SL rule) | MES 3m | all_rules (Sat) | WEAKER 0/3 (11/09, 11/14) | net -36 (+112 / -116 / -31); last 4 wk +7 vs +124 | last 4 wk within 40 % of current |
| Cut if wrong side of HTF EMA9 at 18 min | MGC 3m | exit_lab (Sat) | promising 3 weeks (11/07, 11/09, 11/14) -- NOT recommended | 11/14: +63 after costs z 1.25 T4R (+26 / +6 / +31), last 4 wk +17; walk-forward pick differs (SL-only last third -19); run on 80 % / 1.7 exits | rerun on FLIP 0 % exits + walk-forward pick positive |
| TP 85 % after 18 min + half SL1 if negative at 18 min | MES 3m | combo TP + SL (Sat) | WEAKER 11/14 (0 weeks) | +226 z 0.8 (+132 / +136 / -42), last 4 wk -104; TP rule alone +196 TR | all thirds + last 4 wk |
| TP 65 % after 21 min + cut if < 25 % at 18 min (now top: TP 70 % / 18 + cut if negative at 18) | MGC 3m | combo TP + SL (Sat) | WEAKER 11/14 (lost T); new top T4R | watch +86 z 0.45 (+72 / -10 / +23); new top +105 T4R z 0.5 (+52 / +8 / +45); none z >= 1 | z >= 1 + robust 3 weeks (on FLIP 0 % exits) |
| Bot trigger HTF EMA20 Pierce ON | MES 3m bot | bot_trigger (Sat) | 0/3 | 11/14: Δ +72 (+125 / -27 / -26), last 4 wk -16; live 5 / +10.5 | all thirds + live n >= 15 |
| Range gate OFF in NY only | MGC 3m | mgc3_gate_session (Sat) | **FAILED 11/14** (reset 1/3 -> 0/3) | Δ +43 (+31 / -2 / +14) on 50 % / 3.5; old exits +47 ✓; vs 11/09 +154 (X4 fix) | 3 weeks; Pine change needed |
| MES 3m range gate on in all sessions | MES 3m | mes3_gate_session (Sat) | keep (11/14) | gate OFF loses in every session (Asia -98, London -6, NY -47) | -- (no candidate) |
| MGC 5m runner 80 % / trail 2.5 (and 50 % / 3.5) | MGC 5m | MGC 5m runner watch (Sat) | weeks robust 0 / 0 (11/14) | current -489; 80/2.5 +111 z 1.0 (+27 / +53 / +7) promising, last 4 wk -2.1; 50/3.5 +158 z 1.0 (+1 / +109 / -60) noise; still net negative under every exit | robust (z >= 2, all thirds) 3 weeks + last 4 wk Δ >= 0 |
| SL1 cap removal (Max ATR SL1 "MGC 3m 0") | MGC 3m | MGC 3m SL1 size + cap (on demand) + mgc_slx (11/14) | run 1 (11/13), 0 qualifying | 1.7 ATR no cap +171 z 0.8; mgc_slx 11/14: 2.0 ATR no cap +266 z 1.0 (noise) | 3 qualifying runs >= 7 days apart + z >= 2 |
| Max setups per HTF flip N=4 | MES 3m | flip order (Sun) | **1/3** (11/15; 2/3 if the 11/12 baseline is counted) | replay #5+ bot 62 · -57 (-28 / -7 / -22), chart 60 · -66; live #5+ bot -0.89 (549) vs 1-4 -0.33; kept 1-4 beats all by only +0.01; tiny replay sample, chart rows on stale exits | 2 more qualifying weeks (same N); Pine change needed (no input exists) |
| Max setups per HTF flip N=1 | MES 5m | flip order (Sun) | **1/3** (11/15; 2/3 if baseline counted) | replay #2+ bot 936 · -899 (-448 / -391 / -60), chart -682; live #2+ bot -0.83 vs #1 -0.80, chart -0.59 vs -0.04; #1 alone still negative | 2 more qualifying weeks; Pine change needed |
| Setup order cut-off (MGC 3m first 2; MES 2m N=1; MGC 5m N=2) | MGC 3m, MES 2m, MGC 5m | flip order (Sun) | 0/3 (11/15) | MGC 3m replay #3+ -192 bot / -269 chart but live #3+ +0.04 (1044); MES 2m fails only chart-exit (c) (-0.72 vs -0.62); MGC 5m live #3+ +0.22 | replay + live agree 3 weeks |
| OR block OFF (MGC 3m NY / Asia; M2K 3m NY) | MGC 3m, M2K 3m | orf (Fri) + opening-range blocks (every 2 wk Sun) + blk119 | **0 of 2** (orb_all run 1, 11/15, same bars as baseline) | orb_all 11/15: MGC NY live +82 z 0.8 / bracket +90 z 1.3; Asia +72 z 0.6 / +79 z 1.0 (promising bracket only); M2K 3m NY block robustly right (-88 z -2.2); blk119 11/15 (v1.19 branch): MGC Asia OFF +164 z 1.4 promising, M2K 3m NY OFF +46 z 1.7 promising; orf 11/14 MGC NY +111 z 2.5 (Jan-Mar -1) | robust with both exits on 2 consecutive runs, window setups >= 30 and positive |
| 1H / 4H CBC gates (MES 5m skip 1H against; MES 2m / M2K 5m / M2K 2m skip 4H against) | MES 5m, MES 2m, M2K | 1H/4H XTF study (on demand) | run 1 (11/12) | MES 5m 1H against replay 716 / -596 (-204 / -53 / -340), live kept +0.17 vs -0.74; MES 2m 4H 1162 / -679 | 3 qualifying runs >= 7 days apart |
| Exit-rule alerts live hits (v10.79) | MES 3m / MGC 3m | mes3_ema_watch (E) | MES 1 / MGC 2 of 15 | live MES TP cut +6.19, MGC lock +8.10; replay on current exits: MES +17 z 0.3, MGC +28 z 0.1 (last third -45) | 15 live hits each; likely DROP if live confirms |
| Chart slow EMA 14 / 16 | MES 3m | mes3_ema_watch (A) | last-4-wk beat 4 of 6 / 5 of 6 | 'tod': 14 Δ +197 z 0.7, 16 Δ +226 z 0.9 (-1 / +79 / +148); last 4 wk 14 -14 / 16 +58 | 5 of last 7 runs (16 met) + z >= 2 all thirds |
| 5m confirmation (rule fixed 11/13) | MES 2m / MES 3m | mes3_ema_watch (C) | keep watching (counts reset) | 2m 23 conf +0.41 vs 123 unconf -0.89, replay Δ +0.01 z 0.0; 3m conf worse, replay +0.49 z 1.3 | 40 ended + replay z >= 1 all thirds; MES 5m alerts missing since 11/12 |
| LTF Pierce LATE trigger off | MES 2m / 3m / 5m | mes3_ema_watch (D) | no trigger 40 ended | 2m 19 / -32.0, 3m 20 / -21.1, 5m 15 / -7.5; replay window 0 worse on all | 40 ended + replay |
| Late + room < 0.5 x TP1 skip | MES 2m / 3m / 5m | mes3_ema_watch (F) | too few | MES 2m 6 / -24.2; MES 3m 8 / +7.2; MES 5m 5 / +13.5 | more ended setups |
| Stop floor min 6 + TP1 2 ATR no cap, 50 % | MGC 3m | mgc_sltp_grid | **lost ✱ 11/16** (not T) | 11/16: +85.6 (thirds +11.9 / -40.1 / +113.8; first half -2.7) vs FLIP 0 % proxy +79.2; only ✱ in floor block: 2 ATR 80 % min 6 +66.8; main grid ✱ cells 24 -> 6 | ✱ + T + neighbours ✱ |
| Breakout window 5 bars | MGC 3m | breakout_flip | promising (4 runs) | +111 z 1.2 (+77 / +0 / +33) (old 50 % / 3.5 exits) | robust 3 weeks; re-check after chop_sim EXIT sync (report doc no longer in project after 11/15) |
| Levels + prior-day H/L | MGC 3m | breakout_flip | **FAILED 11/09** | -20 (still worse 11/13) | dropped by study |
| Clean break >= 0.25 ATR | MES 3m | breakout_flip | **FAILED 11/09** | +1 z 0.0 | count restarted |
| Block OPPOSING order block | MNQ 2m | ob_setup (weekly Fri) | worth testing (4 runs) | 11/13: v1.08 OPP 54 · 33 % · -5.82, Δavg -5.00 | more runs; Pine change (report doc no longer in project after 11/15) |
| VWAP 4 + HTF EMA20 cap 3 ATR | MGC 3m | ema_stretch | promising 8 runs, robust 0 | +62 z 1.1 (+33 / +8 / +20) | robust (new input needed) |
| EMA200 cap 4 ATR (and cap 12) | MES 2m | ema_stretch | cap 4 promising 4 runs; cap 12 promising 2 runs; robust 0 | cap 4 +185 z 1.6 (+17 / +1 / +167); cap 12 +39 z 1.6 | robust (new input needed) |
| HTF EMA9 Pierce off / both pierces off / HTF 7-16 | MES 3m | htf_ema + trigger | promising, 0 robust | htf_ema 11/13: both off +198 z 1.6; trigger 11/13: untick HTF EMA9 Pierce +164 z 1.7, live 12 ended +10.6; trig_inputs 11/14 (branch): keep every trigger ON | robust + 20 live ended |
| Chart EMAs 16 / 34 / 120 | MES 5m | ema5 (Fri) + htf_ema | **QUALIFIED 11/13 -> C-011** | ema5 robust 3/3 (+504 z 3.2); htf_ema A+ robust 9 runs | -- |
| ER threshold 0.18 | MES 5m | filter_sweep (Fri) | **QUALIFIED 11/13 -> C-012** | robust 3/3, +198 z 2.5 | -- |
| ER filter OFF | MES 5m | filter_sweep (Fri) | robust 1/3 | +315 z 2.1 | 2 more robust runs |
| MES 2m breakout window 1 bar / CHOP > 58 | MES 2m | filter_sweep (Fri) | robust 1/3 each | 1-bar +150 z 2.2; CHOP > 58 +175 z 2.2 | 2 more robust runs |
| CHOP > 58 block | MGC 5m | filter_sweep (Fri) | promising 0 robust | +168; live blocked 14 · -40.4 | robust |
| Crosses >= 4 block | MGC 3m | filter_sweep (Fri) | promising, 0 robust | +174 z 1.8 | robust |
| Crosses >= 6 block | MES 3m | filter_sweep (Fri) + tsf (11/14) | promising, 0 robust | +64 z 1.5; tsf 11/14 (v10.97 base): +133 z 2.3 | robust |
| EMA200 vs VWAP environment (`ats_env_on`, built v10.97 OFF) | MES 3m | volflip / cbce (11/14) | tallies 0/3 | +560 z 2.5 (cbce: all thirds better); last 4 wk -20; MGC 3m -377 | volflip rule: 3 weeks robust incl. last 4 wk |
| Range gate 4.0 / zone 30 % (and gate OFF) | MGC 3m | rgate (Fri) + all3v (11/15) | 0/3 robust | 11/13: +151 z 1.6, last 4 wk -28.2; all3v 11/15 (branch v1.17): gate 4 +180 z 1.2, gate OFF +263 z 1.3 (last 4 wk -24), promising | 3 robust runs + last 4 wk >= 0 |
| Alerts in 22:30-03:00 gap | MES 3m | all_alerts (Fri) | 3/3 on paper -> **no change** | +56 (+14 / +19 / +24) | not applicable (alert_hours_sym governs MES 3m) |
| Alerts in 22:30-03:00 gap | MGC 3m | all_alerts (Fri) | 2/3 | +165 (+120 / +35 / +10) | run 4 on 11/20 |
| Alerts in 07:45-09:30 gap | MGC 2m / MGC 5m | all_alerts (Fri) | **QUALIFIED 11/13 -> C-013 / C-014** | MGC 2m +79, MGC 5m +141 (all thirds) | -- |
| Untick LTF EMA20 Pierce | MES 2m | trigger (Fri) + ema5 | promising, 0 robust | 11/13: +129 z 1.2; live 67 ended -44.6 | robust (z >= 2) |
| Wider SL1 0.75 ATR | MES 5m | sl_reversal (Fri) | **streak reset 3 -> 0 (11/14)** | sim 3/3 earlier, live failed | live net positive + new streak (report doc no longer in project after 11/15) |
| Wider SL1 +0.75 ATR | MGC 2m | sl_reversal (Fri) | streak 1 (11/14, new) | starts streak | 3-run streak + live |
| HTF slope Both, min 0.5 pt / chart-EMA20 slope | MES 3m | ema_slope (Fri) + cbc_daily | promising, 0 robust (streak 0, 11/14) | 11/07 +194 z 1.3; cbc_daily 11/16: >= 0.5 54 · +27.0 (-18.2 / +45.2) vs < 0.5 57 · -71.7 (-20.5 / -51.2); on current exits 14 · +2.5 vs 9 · -28.2; kept side not positive both halves -> watch; slope_grid 11/14 (branch): 0.42 +212 vs 0.30 z 1.4 | 3 robust weeks |
| Shallow pullback < 0.75 ATR skip | MGC 2m | cbc_daily | reached 21 setups 11/16 -> **no change** (2nd half positive) | 21 · -19.2, halves -28.3 / +9.0; since v10.77 6 · +4.6 | both halves negative |
| Flips >= 4 block (non-FL subset) | MGC 2m | cbc_daily | watch | since v10.77 13 · -38.0 (-12.7 / -25.3); non-FL 11 · -26.4 (11/16, unchanged) | 20+ since v10.77 with both halves negative -> "MGC 2m 4" |
| Skip LTF EMA20 Pierce 18:00-20:30 | MGC 2m | evening (Fri) | **FAILED 11/13** (live positive) | sim 57 / -40.7; live 12 / +7.1 | live turns negative |
| No new setups 18:45-20:00 / HTF Flip in window | MES 2m | evening (Fri) | new 11/13, fails | window sim 73 / -71.6 (-48 / +13 / -37), live 12 / -42.5; HTF Flip sim 35 / -44.3, live 5 / -10.3 | all thirds (window) / live >= 10 (Flip) |
| London flip-candle entries | MES 3m | flip_timing (Fri) | sim ⚠ 11/13, live negative | sim 241 · -75.6; live 12 · -18.4 | Pine change; weekly history |
| NY 5-8 HTF candles | MES 2m | flip_timing (Fri) | new 11/13 (1 week) | sim 55 · -16.4; live 13 · -15.6 | more weeks |
| Room L5 (< 0.5x TP1) skip | MES 3m | room_study (Fri) + cbc_daily | live meets (b), sim no | live -0.79 vs +0.80; sim skip -118 z -0.7; cbc_daily 11/16: Level/OB < 0.5x TP1 74 · -64.0 (-37.3 / -26.8) | sim robust |
| 15m cloud against skip | MGC 3m | room_study + cbc_daily | live watch | 31 · -40.7 (-17.4 / -23.3) (11/16) | sim support |
| Pierce 3-4 HTF candles | MES 5m | flip_timing (Fri) | sim meets, live fails | sim 122 / -94.4; live 10 · +5.9 | live negative |
| MGC 2m live-vs-replay gap flag | MGC 2m | mgc2 (Fri) | 1 of 3 weeks | live -67.7 vs replay +47.9 (gap -116) | 3 weeks running -> flag |
| MGC 3m slope lookback 15 min / 0.165 (branch v1.18, live from 11/16) | MGC 3m | 3m weekly watch (Tue 17:09) | CONFIRMED 0 · revert streak 0/3 (setup run 11/15) | full period +601 z 1.8 (+361 / +160 / +79), last 4 wk -51; since go-live: no bars yet | CONFIRMED: z >= 2, all thirds + last 4 wk positive; REVERT: since go-live negative 3 runs or z < 1 |
| MNQ 3m cap 60 + NY OR block OFF; M2K 3m SL1 3.5 + 0 % (branch v1.19) | MNQ 3m, M2K 3m | 3m weekly watch (Tue 17:09) | revert streak 0/3 each (11/15) | MNQ old settings -2511 z -3.3 (every third worse); M2K old -111 z -1.4 (every third worse, DD 25 vs 47) | REVERT if old-settings row positive since go-live 3 runs or z > -1 |
| 2m slope lookback MES 2m 8 min / MNQ 2m 10 min (branch, not in v1.17 list) | MES 2m, MNQ 2m | slk (one-off 11/15) | 1 run | MES 2m 8 min 0.225 +190 z 2.1 robust (6/6 thresholds better); MNQ 2m 10 min 0.275 +2434 z 2.1 robust (6/6) | not scheduled; in-sample heavy search -- rerun before adopting |
| Loser-hour candidates (not yet on the list) | MGC 2m, MES 2m, MCL | loser-hour (Sat) | new !! 11/14 (1 run) | MGC 2m 06-07 16 · -16.9 (would complete 04-08 block); MES 2m 19-20 11 · -34.8; MCL 3m 10-11 (10); MCL 5m 11-12 (8) | hold !! next week (n >= 8) |

## 4. Studies

| Study | Schedule | Last run | Report | Latest verdict | Change warranted? |
|---|---|---|---|---|---|
| CBC settings sync check | Tue/Thu/Fri 16:47 (was daily 14:43) | 11/13 16:47 | settings_sync_report.md | v10.96; **3 MISMATCH** in study scripts (MES 3m 'tod', MGC 3m 50 % / 3.5) -- fixes not applied; v10.97 not yet synced; stale if no run by Tue 11/17 16:47 | no |
| Weekly 3m: time stop / cut (A) | Sat 18:27 | 11/14 23:35 | sl_time_rule_report.md | no candidates; keep exits on all 4 charts (MGC 18-min cells T4R but z 0.5) | no |
| Weekly 3m: TP + SL combo (B) | Sat 18:27 | 11/14 23:37 | combo_tp_sl_report.md | no change; MES + MGC watch combos WEAKER | no |
| Weekly 3m: exit lab (C) | Sat 18:27 | 11/14 23:37 | exit_lab_report.md | MGC h9 cut at 18 min promising wk 3, not recommended (old exits, walk-fwd differs) | no |
| Weekly 3m: trend guard (D) | Sat 18:27 | 11/14 23:37 | trend_guard_report.md | MGC VWAP / MNQ guard / M2K shorts HELD 2/3 | no |
| Weekly 3m: runner (E) | Sat 18:27 | 11/14 | runner_report.md | MGC 50 % / 3.5 HELD 2/3 vs 80 % / 1.7 (superseded by v10.96); MES no runner variant | no |
| Weekly 3m: all rules combined (F) | Sat 18:27 | 11/14 | all_rules_combined_report.md | MGC London 2/3, VWAP+London 2/3; MES balanced WEAKER | no |
| Weekly 3m: bot windows (G) | Sat 18:27 | 11/14 | botwin_report.md | short filter WEAKER 0/3; 13-14 removal right (91 / -250) | no |
| Weekly 3m: bot triggers (H) | Sat 18:27 | 11/14 | bot_trigger_report.md | keep triggers; HTF EMA20 0/3; LTF not beyond run 1/3 | no |
| Weekly 3m: gate by session (I) | Sat 18:27 | 11/14 | mgc3_gate_session_report.md, mes3_gate_session_report.md | MGC NY range gate off FAILED (0/3); MES keep gate on | no |
| MES study: EMA, TP1, 5m-confirm, trigger, exit rules | weekdays 17:37 | 11/13 17:37 (Mon 11/16 run not in report) | mes3_ema_watch_report.md | keep 9 / 20 + TP1 1.75; exit-rule replay edge mostly gone; MES 5m alerts silent since 11/12 18:40 | no |
| CBC room-to-first-level daily check | weekdays 17:47 | 11/13 17:48 (Mon 11/16 run not in report) | room_daily_report.md | MES 3m 0.2 x TP1 candidate (OOS 3 / 8); MGC 3m keep off | no |
| CBC daily stats checklist | weekdays 17:26 | **11/16 17:27** | cbc_daily_report.md | no suggestion meets rule; MGC 2m range gate now looks live; MES 2m alert dead since 11/15 19:22, MES 3m TP1 closes send no Setup Ended | no |
| MES + MGC 3m stop / TP grid | weekdays 17:27 | **11/16 17:27** | mes_sltp_grid_report.md, mgc_sltp_grid_report.md | MES: **Ready to change YES** (80 % + BE + trail 1.3 ✱ T R, low conviction; live 100 % also R); MGC: keep FLIP 0 % (no T cell) | **YES -> C-010 (re-flagged)** |
| Breakout + flip-ER variants | weekdays 17:28 | 11/13 17:29 (last known) | breakout_flip_report.md -- **doc no longer in project** | no change; MGC 5-bar window promising (old exits) | no |
| Setups in order blocks | Fri 17:05 (was weekdays) | 11/13 17:07 (last known) | ob_setup_report.md -- **doc no longer in project** | MNQ 2m block OPPOSING worth testing | no |
| Alert parameter sweep | weekdays 17:05 | 11/13 17:06 (last known) | alert_param_report.md -- **doc no longer in project** | MGC 2m cd 5 worth considering (9th run); MES 3m cd 8 dropped | YES -> C-003 |
| Stretch filter check | every 3 days 18:37 | 11/12 17:09 (run 8; 11/15 run not seen) | ema_stretch_report.md, stretch_study_report.md | keep "MGC 3m 4"; 3 promising, 0 robust; stale if no run by 11/18 17:09 | no |
| HTF EMA length check | every 2 days 19:13 | 11/15 19:13 (run 9) | htf_ema_report.md | keep HTF 9 / 20 on all 4 charts; MES 5m 16/34/120 rows robust 9 runs (A+ +504 z 3.2); no new live HTF pierce setups | no (-> C-011 via ema5) |
| Stop points + max loss sweep | Fri 16:29 | 11/13 16:30 (last known) | stop_sweep_report.md -- **doc no longer in project** | no change on every case | no |
| EMA slope gate | Fri 17:41 | 11/14 11:24 (catch-up) | ema_slope_report.md | keep Off on MGC 3m + MES 3m; streak 0 | no |
| Evening session + flip timing | Fri 17:53 | 11/13 17:53 (last known) | evening_session_report.md, flip_timing_report.md -- **docs no longer in project** | evening: nothing; flip timing: MES 3m 5-8 meets rule (4th check) | YES -> C-002 |
| Stop-out reversal | Fri 18:07 | 11/14 11:47 (catch-up, last known) | sl_reversal_report.md -- **doc no longer in project** | no change; MGC 2m +0.75 ATR streak 1; MES 5m streak reset | no |
| Room-to-resistance weekly | Fri 18:23 | 11/13 18:23 (check 5, last known) | room_study_report.md -- **doc no longer in project** | keep OFF | no |
| Chart EMA length weekly (5m) | Fri 18:47 | 11/13 18:47 | ema5_report.md | **MES 5m UPDATE WARRANTED: 16 / 34 / 120** | YES -> C-011 |
| Opening-range block weekly | Fri 19:37 | 11/14 12:13 (catch-up, run 3) | orf_report.md | keep as is on all charts / sessions; MGC 3m NY +111 z 2.5 (Jan-Mar -1) | no |
| Trade Setup Filters sweep + MGC 3m range gate | Fri 20:13 | 11/13 20:13 | filter_sweep_report.md, rgate_report.md | **MES 5m UPDATE WARRANTED: ER 0.18**; rgate no change | YES -> C-012 |
| Alerts + alert-session weekly | Fri 20:43 | 11/13 20:43 | all_alerts_report.md | **UPDATE WARRANTED**: MGC 2m / 5m London window to 09:30 + alert-type unticks | YES -> C-013..C-017 |
| Setup Triggers weekly | Fri 21:17 | 11/13 21:18 | trigger_report.md | keep all (MES 3m HTF EMA9 off promising z 1.7) | no |
| MGC 2m weekly improvement | Fri 21:49 | 11/13 21:49 | mgc2_report.md | no change | no |
| Weekly loser-by-hour | Sat 10:17 | 11/14 10:17 | hour_loss_weekly_report.md | 12 chart-hours / blocks meet blocking rule; MNQ 2m 04-05 / 14-15 dropped | YES -> C-006, C-007, C-009, C-018, C-019 (C-008 withdrawn) |
| MES 3m bot flip-exit watch | Sat 13:37 | 11/14 13:37 | flip_exit_watch.md (+ flip_exit_report.md, flip_exit_bot_report.md) | HELD, weeks held 1; 0 live HTF Flip bot trades | no |
| TP1 % vs HTF flip exit, MES / MGC 3m | Sat 13:53 | 11/14 13:53 | tp1flip_summary.md, tp1flip_report.md | no change both; MGC FLIP 0 % held 1, revert 0/2 | no |
| MGC 5m runner exit watch | Sat 14:13 | 11/14 14:13 | mgc5_runner_report.md | no change yet; 0 robust; MGC 5m net negative under every exit | no |
| Setup order since HTF flip | Sun 13:23 | 11/15 13:23 | flip_order_summary.md | MES 3m N=4 and MES 5m N=1 meet the rule this week (1/3 each, Pine change needed); MGC 3m / MGC 5m replay vs live disagree; chart-exit MES / MGC 3m rows on stale exits | no (watch 1/3) |
| Opening-range blocks NY / London / Asia | every 2 weeks Sun 12:47 | 11/15 12:47 (run 1, same bars as baseline) | orb_all_summary.md | keep all blocks on every chart; no robust row; MGC 3m NY / Asia promising (bracket) 0 of 2 | no |
| 3m weekly watch: MGC 3m slope lookback + MES / MNQ / M2K 3m (branch v1.18-v1.19) | Tue 17:09 (from report header) | 11/15 (setup check, data to 11/13) | mgc3_lk_watch.md | MGC 15-min lookback promising (+601 z 1.8); MNQ / M2K v1.19 better in every third; MES keep; tallies 0; first real run Tue 11/17 | no |
| 1H MTF + 4H XTF confirmation | on demand | no report yet (run 1 11/12 in task text) | xtf_summary.md | MES 5m 1H / MES 2m, M2K 4H candidates run 1 | no |
| MGC 3m SL1 size + cap | on demand | 11/13 (run 1) | mgc_sl_summary.md | keep SL1 1.7 ATR + MGC 7-pt cap | no |
| Other: EMASlope branch battery -- 2m charts | one-off | 11/14 | two_report.md | branch v1.13: MES 2m +724 z 4.7, MGC 2m +403 z 2.5, MNQ 2m +5825 z 4.8, M2K 2m +638 (thin) | branch only (v1.13) |
| Other: EMASlope branch -- 5m charts | one-off | 11/14 | five_report.md, all5_report.md | MES 5m slope 0.70 + stretch 4 (z 5.1, DD 877 -> 46); MGC 5m slope 0.48 (z 3.6); MNQ 5m stretch 7 (+606 z 2.2); MGC 5m cap 10 (+160 z 1.9) | branch only (v1.12-1.15) |
| Other: ①②③ input sweeps on branch (3m) | one-off | 11/14 | all_report.md, all_nb_report.md, ats_inputs_report.md, time_blocks_report.md, tsf_report.md, trig_inputs_report.md, orpa_report.md, orsess_report.md | MES 3m 13-15 block + 16-19 no-new-setups combo +291 z 2.9 (robust); MES LTF pierce min ER 0.15 promising; MNQ cap OFF +1068 z 1.8; keep OR / pivot / triggers / sessions | branch only; MES 3m 13-15 = C-006 |
| Other: MNQ 3m / M2K 3m branch studies | one-off | 11/14 | mnq_report.md, m2k_report.md, alerts_mnq_report.md | MNQ 3m candidate slope 0.75 + FLIP 0 % (+6261 z 5.1); M2K 3m "treat as no-edge" | branch candidates (not CBC v10.x) |
| Other: branch version compare / sessions | one-off | 11/14 | vcmp_report.md, vcmp2_report.md, sessions_report.md | MES 3m branch v1.07 +1525 z 6.0 vs v10.97; MGC +406 z 1.1 | no |
| Other: slope grid / per-trigger slope | one-off | 11/14 | slope_grid_report.md, trig_slope_report.md | MES 3m slope 0.42 candidate (+212 z 1.4); MGC keep 0.30; keep filter on all triggers | no |
| Other: MGC 3m X4 fix + SL mechanisms | one-off | 11/14 | mgc_x4_report.md, mgc_slx_report.md | X4 stretch gate fix; FLIP 0 % best exit; SL 2.0 ATR no cap noise | no |
| Other: chart EMA 7/16 (MES 3m) | one-off | 11/14 | ema716_report.md | keep 9 / 20 (7/16 -39 z -0.1) | no |
| Other: MES next ideas / flip window | one-off | 11/14 | mes_next_report.md, flipwin_summary.md | flip exit flip + SL1 no TP +245 z 3.7 (robust) -> branch v1.00 flip ride; HELD | branch only |
| Other: CBC Engine ideas / volume flip + EMA200 | one-off | 11/14 09:01 | cbce_report.md, volflip_report.md, volflip_summary.md | MES EMA200 vs VWAP +560 z 2.5 -> built v10.97 (OFF); tallies 0/3 | done (v10.97, off) |
| Other: EMASlope branch v1.16-v1.23 build + 3m checks | one-off | 11/15 | all3v_report.md, slk_report.md, mtf_report.md, blk119_report.md, tooltips_v1_19.md | all3v: MES 3m nothing promising, MGC 3m 15-min lookback / range gate OFF / late-away 2 promising; slk: 5m 15 min best on all 4, 2m 6-10 min; mtf: 60m / 4h EMA slope adds nothing (keep HTF slope alone); blk119: no new hour block, MES 13-15 confirmed | branch only (v1.17-v1.19 adopted) |
| Other: EMASlope handoff | one-off | 11/14 | EMASLOPE_HANDOFF.md | v1.15 compile not confirmed; load on 12 charts pending; 8 candidates not implemented | user action (branch) |
| Other: flip exit (MES 3m 09:30-16:00) | one-off | 11/12 12:00 | flip_exit_report.md | live favours flip exits, replay the bracket | done (v10.91-92) |
| Other: flip exit in bot windows | one-off | 11/12 12:30 | flip_exit_bot_report.md | HTF Flip flip+SL +52.2 vs -73.5 | done (v10.92) |
| Other: bot alerts / trigger choice | one-off | 11/12 10:02 | bot_alerts_report.md | tick nothing; keep LTF not beyond unticked (user ticked it in v10.88) | no |
| Other: time + progress lock | one-off | 11/08 | time_lock_report.md | no lock rule | no |
| Other: bot TP rules | one-off | 11/08 | bot_tp_report.md | TP1 2.0 +19 (not all thirds) | no |
| Other: MES 3m entry slots | one-off | 11/08 | mes3_entry_slots_report.md | basis of v10.85 / v10.86 | done (v10.85-87) |
| Other: MFE study | one-off | 11/08 | mfe_report.md | runner study basis | done (v10.84) |
| Other: 5m study | one-off | 11/08 | study_5m_report.md | MES 5m 5-day EMA + losing-stretch stop | no |
| Other: session loss stop / guard fix | one-off | 11/08 | session_loss_stop_report.md, guard_fix_report.md | feeds all_rules | no |
| Other: MES 3m EMA grid | one-off | 11/04 | mes3_ema_grid_report.md | basis of v10.68 (reverted) | no |
| Other: toward-flip | one-off | 11/03 | toward_report.md | basis of v10.60 | done (v10.60) |
| Other: TP1 % by time of day | one-off | 11/03 | tp1_tod_report.md | basis of v10.55-56 | done (v10.55-56; superseded v10.95) |
| Other: loser by hour (first run) | one-off | 11/03 | hour_loss_report.md | first run | no |

## 5. Run log

- 11/16 23:34 | Ledger | 3 new runs (cbc_daily, MES + MGC SL/TP grid); **C-010 re-flagged (MES 3m 80 % + BE + trail 1.3)**; nothing done; 8 report docs no longer in project; Monday MES watch / room daily / alert param / breakout runs not seen | C-010
- 11/16 17:27 | MES + MGC SL/TP grid | MES: Ready to change YES -- 3.0 / 1.75 / 80 % / trail 1.3 +140.7 ✱ T R (low conviction; live 100 % +127.3 R too); MGC: keep FLIP 0 % (proxy +79.2, no T cell; floor min 6 lost ✱) | C-010
- 11/16 17:27 | Daily stats | no suggestion meets rule; MGC 2m shallow pullback 21 but h2 +9.0; MGC 2m range gate looks live; MES 2m alert dead since 11/15 19:22; MES 3m TP1 closes send no Setup Ended | -
- 11/15 23:34 | Ledger | 4 new scheduled runs + 11/15 branch one-offs; no new open item, none done; flip-order MES 3m N=4 / MES 5m N=1 added to watch (1/3); branch v1.16-v1.23 added to section 2; new Tue 3m watch added | -
- 11/15 19:13 | HTF EMA length (run 9) | keep 9 / 20; MES 5m 16/34/120 robust 9 runs (weekend: numbers unchanged) | - (supports C-011)
- 11/15 (setup) | 3m weekly watch (MGC 3m lookback + MNQ / M2K v1.19) | MGC 15-min promising +601 z 1.8; MNQ -2511 / M2K -111 for old settings; tallies 0 | -
- 11/15 15:26-18:54 | One-offs: mtf (60m / 4h slope), slk (slope lookback all 12 charts), all3v (MES / MGC 3m full sweep), blk119 (time blocks on v1.19) | branch v1.17-v1.19 adopted; mtf / blk119 keep; MGC Asia OR OFF promising | - (branch)
- 11/15 13:23 | Setup order since HTF flip | MES 3m N=4 + MES 5m N=1 meet rule (1/3); MGC 3m / 5m replay vs live disagree; MES 2m near miss | -
- 11/15 12:47 | Opening-range blocks (run 1) | keep all blocks; MGC 3m NY / Asia promising 0 of 2; same bars as baseline | -
- 11/14 23:34 | Ledger | 17 new study runs + 11/14 one-offs; 2 new open items (C-018, C-019); C-008 withdrawn; C-006 / C-007 / C-009 re-confirmed (C-009 widened); v10.97 + EMASlope branch added to section 2 | C-018, C-019
- 11/14 23:37 | Weekly 3m (B) TP + SL combo | no change; MES TP85/18 + half SL WEAKER (+226, third 3 -42); MGC TP65/21 + cut WEAKER, new top TP70/18 + cut neg +105 T4R z 0.5 | -
- 11/14 23:37 | Weekly 3m (C) exit lab | MGC h9 cut at 18 min promising wk 3 (+63 z 1.25 T4R) but not recommended; keep exits all 4 charts | -
- 11/14 23:37 | Weekly 3m (D) trend guard | MGC VWAP +190 / MNQ guard +875 / M2K shorts +140 HELD 2/3 | -
- 11/14 23:35 | Weekly 3m (A) time stop | no candidates | -
- 11/14 (no time) | Weekly 3m (E) runner | MGC 50 % / 3.5 HELD 2/3 (Δ +285; superseded by FLIP 0 %); MES none | -
- 11/14 (no time) | Weekly 3m (F) all rules | MGC London 2/3 (barely), VWAP+London 2/3 (+234); MES balanced WEAKER | -
- 11/14 (no time) | Weekly 3m (G) bot windows | short filter WEAKER 0/3 (-229); 13-14 still -250 | -
- 11/14 (no time) | Weekly 3m (H) bot triggers | keep; HTF EMA20 0/3 (Δ +72); LTF not beyond watch run 1/3 (live +15.4) | -
- 11/14 (no time) | Weekly 3m (I) gate by session | MGC NY range-gate off FAILED (Δ +43, reset 0/3); MES keep gate on | -
- 11/14 14:13 | MGC 5m runner watch | no change yet; 80/2.5 +111 z 1.0 promising; 0 robust | -
- 11/14 13:53 | TP1 % vs flip (tp1flip) | no change; MGC FLIP 0 % +642 vs TRAIL 50 % +299, held 1, revert 0/2; MES TRAIL 100 % best | -
- 11/14 13:37 | Bot flip-exit watch | HELD, weeks held 1 (+52.2 vs -73.5); 0 live HTF Flip bot trades | -
- 11/14 12:13 | Opening-range block (catch-up, run 3) | keep as is; MGC 3m NY +111 z 2.5 (Jan-Mar -1) | -
- 11/14 11:47 | Stop-out reversal (catch-up) | no change; MGC 2m streak 1; MES 5m streak reset | -
- 11/14 11:24 | EMA slope gate (catch-up) | keep Off; streak 0 | -
- 11/14 10:17 | Loser by hour (run 3) | C-006 / C-007 / C-009 held 3 runs; MNQ 2m 04-05 / 14-15 dropped; new MES 2m 14-15, MNQ 2m 03-04 / 13-14 / 20-21 | C-018, C-019; C-008 withdrawn
- 11/14 (09:01-18:56) | One-offs: EMASlope branch battery (2m / 5m / 3m sweeps, MNQ / M2K, vcmp, sessions, slope grid, X4 fix, EMA 7/16, CBC Engine, volflip, flipwin, handoff) | branch v1.13-v1.15 (compile not confirmed); v10.97 adds EMA200-vs-VWAP checkbox OFF | - (branch / done v10.97)
- 11/13 23:34 | Ledger | 18 new study runs; 7 new open items (C-011..C-017); C-005 + C-010 withdrawn; v10.94-96 added to section 2 | C-011..C-017
- 11/13 21:49 | MGC 2m weekly (run 3) | no change; live-vs-replay gap flag 1/3 | -
- 11/13 21:18 | Setup Triggers (run 3) | keep all; MES 3m HTF EMA9 off promising z 1.7; MES 2m LTF EMA20 off z 1.2 | -
- 11/13 20:43 | Alerts + sessions (run 3) | UPDATE WARRANTED: MGC 2m / 5m London window 0300-0930; untick HTF EMA9/20 Zone Entry (6 charts), EMA20 Touch Pullback Entry (4), A+ Setup (MES 2m); MES 3m gap no change | C-013, C-014, C-015, C-016, C-017
- 11/13 20:13 | Filter sweep + rgate (run 3) | UPDATE WARRANTED: MES 5m ER 0.18 (robust 3/3, +198 z 2.5); rgate keep waiting (+151 z 1.6) | C-012
- 11/13 19:13 | HTF EMA length (run 8) | keep 9 / 20; MES 5m 16/34/120 robust 8 runs | -
- 11/13 18:47 | Chart EMA 5m (run 3) | UPDATE WARRANTED: MES 5m 16 / 34 / 120 (robust 3/3, +504 z 3.2) | C-011
- 11/13 18:23 | Room-to-resistance (check 5) | keep OFF; MES 3m L5 live only | -
- 11/13 17:53 | Evening + flip timing (check 4) | flip timing MES 3m 5-8 meets rule again; evening nothing (MGC 2m LTF window live +7.1 -> FAILED) | C-002
- 11/13 17:48 | Room-to-first-level daily | MES 3m candidate, OOS 3 / 8 (-2.4); MGC 3m keep off | -
- 11/13 17:37 | MES watch (Fri, all replays) | keep 9 / 20 + TP1 1.75; (C) rule fixed; exit-rule replay edge mostly gone; MES 5m alerts silent | -
- 11/13 17:29 | Breakout + flip-ER | no change; MGC 5-bar window promising z 1.2 | -
- 11/13 17:27 | MES + MGC SL/TP grid | MES no change (trail 1.3 no longer T, live 100 % not R); MGC keep FLIP 0 % | C-010 withdrawn
- 11/13 17:27 | Daily stats | no suggestion meets rule; MGC 3m revert flag superseded; MGC 2m range gate violation 11:26 | -
- 11/13 17:07 | OB setups | MNQ 2m OPPOSING worth testing (gap wider) | -
- 11/13 17:06 | Alert parameter sweep | MGC 2m cd 5 (9th run); MES 3m cd 8 dropped (neighbours disagree) | C-003; C-005 withdrawn
- 11/13 16:47 | Settings sync | v10.96: ats_part_sym MGC 3m 0, ats_pw_sym "", ats_trl_sym MGC 3m 0, bot_news / bot_nwm; 3 MISMATCH in scripts | -
- 11/13 16:30 | Stop sweep | no change | -
- 11/13 (no time) | MGC 3m SL1 size + cap (run 1, on demand) | keep SL1 1.7 + cap 7 | -
- 11/13 (baseline) | TP1 % vs flip (tp1flip) / opening-range blocks (orb_all) | basis of v10.95-96; keep all OR blocks | - (done v10.95-96)
- 11/12 23:34 | Ledger | 16 new study runs since 11/11; C-001 withdrawn; v10.88-93 added to section 2; settings sync no longer stale | -
- 11/12 17:48 | Room-to-first-level daily | MES 3m 0.2 x TP1 candidate, OOS 3 / 8 (-2.4); MGC 3m keep off | -
- 11/12 17:37 | MES watch | keep 9 / 20 + TP1 1.75; first MES TP-cut hit +6.19; MGC 3m no setups since 11/11 | -
- 11/12 17:28 | Breakout + flip-ER | no change; MGC 5-bar window promising (z 1.2) | -
- 11/12 17:26 | Daily stats | no suggestion meets rule; MES 2m flop gate no longer supported (h2 +0.9) | C-001 withdrawn
- 11/12 17:09 | Stretch filter (run 8) | keep MGC 3m 4; VWAP4+cap3 promising 8th, MES 2m EMA200 cap 4 promising 4th | -
- 11/12 17:07 | Alert parameter sweep | MES 3m cd 8 (4th, (a) +99 vs -273), MGC 2m cd 5 (8th) | C-003, C-005
- 11/12 16:47 | Settings sync | v10.93, 1 changed default (bot_t_ln), 5 new bot inputs; 0 mismatch | -
- 11/12 14:48 | Setup order since HTF flip (baseline) | no agreed cut-off; MGC 3m first-2 replay only | -
- 11/12 12:30 | Flip exit (bot windows) | HTF Flip flip+SL +52.2 vs -73.5 -> basis v10.92 | - (done v10.92)
- 11/12 12:00 | Flip exit (09:30-16:00) | live favours flip, replay bracket | -
- 11/12 10:02 | Bot alerts / triggers | tick nothing; keep LTF not beyond unticked | -
- 11/12 09:59 | OB setups (catch-up) | MNQ 2m OPPOSING worth testing (gap narrower) | -
- 11/12 09:58 | HTF EMA length (run 7) | keep 9 / 20; MES 5m 16/34/120 robust 7 runs | -
- 11/12 09:58 | Alert parameter sweep (catch-up) | same flags | C-003, C-005
- 11/12 09:46 | Room daily (re-run of 11/11) | MES 3m candidate, OOS 2 / 8 | -
- 11/12 09:44 | MES watch (stands in for 11/11) | keep 9 / 20 + 1.75 | -
- 11/12 08:45 | MES + MGC SL/TP grid | MES no new setups, trail 1.3 still meets rule; MGC keep v10.84 | C-010
- 11/11 23:34 | Ledger check (no study run) | 11/11 runs failed (usage limit); settings sync STALE | -
- 11/09 19:13 | HTF EMA length (run 6) | keep 9 / 20; MES 5m 16/34/120 robust 6 runs | -
- 11/09 17:48 | Room-to-first-level daily (first report) | MES 3m room x TP1 < 0.2 candidate, OOS 2 / 8 | -
- 11/09 17:38 | MES watch | keep 9 / 20 + TP1 1.75; first live exit-rule hit (MGC lock +1.2) | -
- 11/09 17:29 | Breakout + flip-ER | no change; MGC prior-day H/L failed | -
- 11/09 17:28 | MES + MGC SL/TP grid | MES live row R 7/7; trail 1.3 meets rule (optional) | C-010
- 11/09 17:27 | Daily stats | MES 2m flop gate suggestion stronger; MGC 2m range gate not live | C-001
- 11/09 17:06 | Alert parameter sweep | MES 3m cd 8 (2nd), MGC 2m cd 5 (6th); MES 2m cd 5 dropped | C-003, C-005; C-004 withdrawn
- 11/09 17:06 | OB setups | MNQ 2m block OPPOSING worth testing | -
- 11/09 14:43 | Settings sync | v10.87, 0 mismatch, 1 known | -
- 11/09 (no time) | Weekly 3m (I) gate by session | MGC 3m NY range gate off +154 promising | -
- 11/09 (no time) | Weekly 3m (G) bot windows | short filter WEAKER 0/3 | -
- 11/09 (no time) | Weekly 3m (H) bot triggers | keep; HTF EMA20 Pierce 0/3 | -
- 11/09 (no time) | Weekly 3m (F) all rules | MGC London 1/3, VWAP+London 1/3 | -
- 11/09 (no time) | Weekly 3m (E) runner | MGC 50 % / 3.5 HELD 1/3 | -
- 11/09 13:58 | Weekly 3m (D) trend guard | MGC VWAP / MNQ guard / M2K shorts HELD 1/3 | -
- 11/09 13:58 | Weekly 3m (C) exit lab | MGC h9 cut promising wk 2 | -
- 11/09 13:58 | Weekly 3m (B) TP + SL combo | no candidate | -
- 11/09 13:58 | Weekly 3m (A) time stop | no candidate | -
- 11/08 14:43 | Settings sync | no input changes | -
- 11/08 | One-offs (time lock, bot TP, entry slots, MFE, 5m, session loss, guard fix) | see section 4 | -
- 11/07 19:13 | HTF EMA length | keep 9 / 20 | -
- 11/07 18:38 | Stretch filter | keep MGC 3m 4 | -
- 11/07 10:17 | Loser by hour | 9 chart-hours meet blocking rule | C-006, C-007, C-008, C-009
- 11/07 09:57 | Chart EMA 5m | MES 5m N robust 2/3 | -
- 11/07 09:52 | Room-to-resistance | keep OFF | -
- 11/07 09:52 | Alerts + sessions | no change; 3 gaps 2/3 | -
- 11/07 09:52 | Evening + flip timing | flip timing rules met (MES 3m, MES 2m) | C-002
- 11/07 09:51 | Stop-out reversal | no change | -
- 11/07 09:51 | Filter sweep + rgate | MES 5m ER 0.18 robust 2/3 | -
- 11/07 09:50 | Setup Triggers | keep all | -
- 11/07 09:50 | MGC 2m battery | no change | -
- 11/07 09:50 | Opening-range block | keep | -
- 11/07 09:50 | Stop sweep | no change | -
- 11/07 09:49 | Breakout + flip-ER | MGC 3m prior-day H/L robust 2/3 | -
- 11/07 09:48 | Alert parameter sweep | cooldown MGC 2m 5 / MES 2m 5 / MES 3m 8 worth considering | C-003, C-004, C-005
- 11/07 09:48 | OB setups | MNQ 2m OPPOSING worth testing | -
- 11/07 09:48 | EMA slope gate | keep Off | -
- 11/07 09:47 | MES + MGC SL/TP grid | MES ready YES (done v10.54/82) | -
- 11/07 09:46 | Daily stats | MES 2m non-flip flop gate suggested | C-001
- 11/07 09:44 | MES watch (11/06 run) | keep 9 / 20 | -
- 11/04 | One-off MES 3m EMA grid | basis v10.68 | -
- 11/03 | One-offs (toward, TP1 by time, loser by hour) | basis v10.60 / v10.55 | -
