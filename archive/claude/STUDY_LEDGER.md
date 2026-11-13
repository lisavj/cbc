# CBC Study Ledger -- updated 2026-11-12 23:34 ET

**At a glance** (newest Pine = **v10.93**, 11/12; v10.88-v10.93 are ▶ Bot changes only)
- Open changes: **8** -- C-002 MES 3m flip-timing gate ON (5-8 HTF; weekly check 11/13) · C-003 / C-005 LTF EMA20 Pierce cooldown (MGC 2m 5, 8th run / MES 3m 8, 4th run, now positive under both rules) · C-006..C-009 loser-hour blocks (MES 3m, MGC 2m, MNQ 2m, MNQ 3m) · C-010 MES 3m runner trail 1.7 -> 1.3 ATR (optional). **C-001 WITHDRAWN 11/12** (daily stats no longer supports it). C-004 withdrawn 11/09. None of the open items is in v10.93.
- Done in the last 7 days (11/06-11/12): v10.77-v10.87 (MGC 2m gates, exit-rule alerts, flip-timing gates, MES 3m TP1 1.75, MGC 3m runner, VWAP Bounce, bot windows / short filter) + **11/12 v10.88** bot trigger "LTF EMA20 Pierce (not beyond EMA9)" ON, **v10.89-90** entry-only windows (default off), **v10.91-93** bot flip-only exit for HTF CBC Flip 09:30-16:00 (ON). All user decisions, not ledger items.
- Stale studies: **none** (settings sync back: 11/12 16:47; all weekday studies ran 11/12 after the 11/10-11/11 usage-limit failures).
- Settings sync (11/12 16:47): v10.93, 0 MISMATCH, 1 known; server v14 live, stored duplicates not yet cleaned. Bot replays do not model the v10.92 flip-only exit. Open checks: **MES 3m alerts thin** (silent 11/09-11/11, 59 on 11/12); **MGC 3m no Trade Setup / Setup Ended since 11/11** (remaining alert may lack those boxes); MGC 2m range gate (v10.77) still not confirmed live -- confirm only one CBC alert on the chart.

## 1. Changes warranted (open)

| ID | Flagged | Last confirmed | Chart | Exact change | Evidence | Source | Status |
|---|---|---|---|---|---|---|---|
| C-010 | 11/09 | 11/12 | MES 3m | ats_trl_sym = "MGC 3m 3.5, MES 3m 1.3" (runner trail 1.7 -> 1.3 ATR) | grid 119 setups (no new MES 3m setups since 11/08): SL 3 / TP1 1.75 / 80 % / trail 1.3 = +189.2 R (thirds +38.4 / +9.1 / +141.8) vs live proxy trail 1.7 +180.9; Δ +8.3; trail 1.3 best in every row; "Ready to change: YES" (R cell, 60+ setups); bot (100 % at TP1) unaffected | mes_sltp_grid_report.md | OPEN -- "optional low-stakes tweak"; not in v10.93 |
| C-001 | 11/06 | 11/09 | MES 2m | ats_fl2_sym = "MGC 2m 1, MES 2m 1" | 11/09: non-flip FL 34 · -103.5; 11/12: flop-warning row 65 · 42 % · -65.4, halves -66.3 / +0.9 (2nd half no longer negative) | cbc_daily_report.md | WITHDRAWN 11/12 (daily stats: "no standing items"; 2nd half +0.9) |
| C-002 | 11/07 | 11/07 | MES 3m | ats_fw_sym = "MES 3m 5" (ats_fw2_sym "MES 3m 8" already set) | sim 237 / -88.9, thirds -35 / -52 / -2; live 18 / -14.2 (pierces 17 / -20.8); 3/3 weekly checks; cbc_daily 11/12: MES 3m pierces since 11/06 came 1-5 HTF bars after the flip | flip_timing_report.md | OPEN -- gate built v10.81 but OFF; waits for 11/13 check; not in v10.93 |
| C-003 | <=11/07 (5th run) | 11/12 (8th run) | MGC 2m | ltf_ema20_pierce_cooldown = 5 (MGC 2m chart only) | 1049 alerts at current; cd 5: (a) -271.8 vs -450.5, (b) +68.1 vs -3.7; validation 82 / 75 %; still negative under (a) ("less bad") | alert_param_report.md | OPEN -- not taken in v10.83; not in v10.93 (default 3) |
| C-004 | 11/07 (1st run) | 11/07 | MES 2m | ltf_ema20_pierce_cooldown = 5 (MES 2m chart only) | 11/12: still unreliable (validation 66 / 68 %) | alert_param_report.md | WITHDRAWN 11/09 (replay validation < 70 %) |
| C-005 | 11/07 (1st run) | 11/12 (4th run) | MES 3m | ltf_ema20_pierce_cooldown = 8 (MES 3m chart only) | 683 alerts at current; cd 8: (a) +99.2 vs -272.5, (b) +188.5 vs -4.6 (positive under both, stronger); validation 81 / 77 % | alert_param_report.md | OPEN -- not in v10.93 (default 3) |
| C-006 | 11/07 | 11/07 | MES 3m | Pine change needed: no new setups 06-07 and 13-15 ET (alert_hours_sym already mutes 13:00-14:00 alerts; bot_win drops 13:00-14:00 since v10.87) | live 06-07 10 / -18.2; 13-15 22 / -82.2; !! both halves, held 2 runs | hour_loss_weekly_report.md | OPEN -- partly covered (alerts + bot only); not in v10.93 |
| C-007 | 11/07 | 11/07 | MGC 2m | Pine change needed: no new setups 04-05, 07-08, 21-22 ET (or alert_hours_sym MGC 2m windows) | live 12 / -15.4; 10 / -26.2; 13 / -29.0; !! both halves, held 2 runs | hour_loss_weekly_report.md | OPEN -- not in v10.93 |
| C-008 | 11/07 | 11/07 | MNQ 2m | Pine change needed: no new setups 04-05 and 14-15 ET | live 14 / -45.5; 14 / -77.2; !! both halves, held 2 runs | hour_loss_weekly_report.md | OPEN -- not in v10.93 |
| C-009 | 11/07 | 11/07 | MNQ 3m | Pine change needed: no new setups 06-07 and 13-14 ET | live 10 / -109.2; 10 / -162.5; !! both halves, held 2 runs | hour_loss_weekly_report.md | OPEN -- not in v10.93 |

## 2. Changes made

| Date | Version | Chart | Change | Why (evidence) | Follow-up / latest check |
|---|---|---|---|---|---|
| 11/12 | v10.93 | MES 3m bot | compile fix (CE10295), v10.89-92 logic moved into f_bot_send(); same behaviour | build | settings sync 11/12: no behaviour change |
| 11/12 | v10.91-92 | MES 3m bot | bot_fow = "0930-1600" (flip-only: no TP, closed by HTF CBC flip against / SL1 / 15:57 / next entry); bot_foall = "HTF CBC Flip only"; bot_fosl = true | user decision; flip_exit_bot_report 11/12: HTF CBC Flip 46 (bot windows) bracket+flip -73.5 -> flip+SL +52.2 (flip only +60.8, thirds +79 / -27 / +82); flip_exit_report: HTF Flip 90 -177.7 -> -54.6; LTF not beyond EMA9 worse with flip exit (-80.9 -> -264.2) so kept on bracket | MES 3m bot flip-exit watch (Sat, week 0 = 11/12); cbc_daily 11/12: 4 such Flip trades since 10/19 +90.0 held to flip vs +34.0 bracket; bot replays (botwin / bot_tp / bot_alerts) do not model it yet |
| 11/12 | v10.89-90 | MES 3m bot | new bot_eow "Entry-only windows" = "" (off); bot_eof = false | build (user) | not in use (default off) |
| 11/12 | v10.88 | MES 3m bot | bot_t_ln = true (trigger "LTF EMA20 Pierce (not beyond EMA9)" ON; bot set = Flip + LTF beyond + LTF not beyond) | user decision; note: bot_alerts_report 11/12 said "keep unticked" (24 live bot-window trades -8.7, replay thirds -75 / -42 / +8) | watch item (data note 4): "consider unticking" if still negative after 3 more weekly runs with 20+ new trades; mes3_ema_watch 11/12: MES 3m LTF not beyond 32 / -6.9 (halves +3.2 / -10.1), 3-trigger set 63 / +18.8 vs 2-trigger 31 / +25.7; cbc_daily: since 11/09 2 bot trades · -14.8, both LTF not beyond |
| 11/08 | v10.87 | MES 3m bot | bot_win = "1830-2200, 0300-1300, 1500-1530" | 13:30-14:00 -198 pts, 3.5 SD from chance, neg every third; replay -674 -> -412 (mes3_time_zones_table.md) | botwin 11/09: 13:00-14:00 still 88 / -242 -> removal right; settings sync 11/12 inwin MATCH |
| 11/08 | v10.86 | MES 3m bot | bot_d5 = true (no shorts above 5-day EMA) | botwin + entry_slots: -702 -> -409; DD 907 -> 647 | botwin 11/09: WEAKER 0/3; cbc_daily 11/12: skipped 7 shorts in total (-34.8), incl. 11/12 09:30 Flip short -18.7 |
| 11/08 | v10.85 | MES 3m bot | bot_win = 6-window set | mes3_entry_slots_report.md: -735 -> -229 | superseded by v10.87 |
| 11/08 | v10.84 | MGC 3m | ats_part_sym += "MGC 3m 50"; ats_trl_sym = "MGC 3m 3.5" | runner 11/08: Δ +353 (50 % / 3.5), all thirds, last 4 wk +146 vs +66; walk-fwd rank 2/39 | runner 11/09: HELD 1/3 (Δ +366); cbc_daily 11/12: since 11/09 7 · +32.5 (runner +29.3; partly old exits until 11/12 duplicate deleted) -- **revert-flag count starts 11/13: 0/20**; mgc_sltp_grid 11/12: keep v10.84, 50 % beats 80 % everywhere |
| 11/07 | v10.83 | MGC 2m / MES 3m / MES 2m | vb_tw_sym += "MGC 2m 0000-2400 0.01, MES 3m 0000-2400 4, MES 2m 0000-2400 4" | alert_param 11/07: MGC 2m (a) +451 vs +102; MES 3m (a) +84 vs -61; MES 2m (a) +288 vs +111 | alert_param 11/12: MES 2m 4 best ((a) +290.5), MGC 2m 0 best ((a) +452.1); MES 3m 4 validates (5 alerts), 0 tops the sum but not in both halves |
| 11/07 | v10.82 | MES 3m | ats_tp1_sym = "MES 3m 1.75" (reverts v10.67) | 117 setups: 1.75 +202.6 vs 2.0 +184.5 | mes3_ema_watch (B) 11/12: keep 1.75 (107: 2.0 +3.9, halves -6.3 / +10.2); mes_sltp_grid 11/12: row R |
| 11/07 | v10.81 | MES 2m / MES 3m | ats_fa_sym = "MES 2m 9"; ats_fw2_sym = "MES 3m 8" (from-list empty = OFF) | flip_timing: MES 2m 9-16 HTF sim 105 / -78.2 all thirds, live 14 / -27.8 | cbc_daily 11/12: no late MES 3m pierces; MES 3m ON = C-002 |
| 11/06 | v10.79 | MES 3m / MGC 3m | xr_cut_sym "MES 3m" (21 min / 70 % / ATR 1.5x); xr_lock_sym "MGC 3m" (75 % -> +55 %); alerts only | 11/06 exit-ideas replay: MES +131 z 2.1; MGC +209 z 1.6 | mes3_ema_watch (E) 11/12: first MES TP cut hit 11/12 10:30 +11.44 vs CBC +5.25 (+6.19); MGC lock 5 hits, 2 comparable +5.10 vs -3.00 (+8.10) |
| 11/06 | v10.77 | MGC 2m | ats_fl2_sym = "MGC 2m 1"; ats_rp_sym += "MGC 2m 5" | daily stats 11/05: non-flip FL 43 / -71.0; range-gated 25 / -35.9 | cbc_daily 11/12: **still not confirmed live**; last range violation 11/11 21:40 (-5.85, while duplicates still arrived), none on 11/12; since v10.77 49 · -3.0 |
| 11/06 | v10.77 | MES 3m bot | bot_win = "1830-2200, 0300-1400, 1500-1530" | evidence not found in project | superseded by v10.85 / v10.87 |
| 11/05 | v10.75 | MGC 3m / MES 3m | vb_tw_sym = "MGC 3m 0300-1700 0.01"; alert_hours_sym = "MES 3m 1830-2100, 0430-1300, 1400-1430" | MGC 3m sweep 11/05: (a) +$4,388 vs +$997 | alert_param 11/12: MGC 3m tod still best ((a) +378.4, (b) +14.9 ✱) |
| 11/05 | v10.71-76 | MES 3m bot | CrossTrade bot (Flip + LTF beyond EMA9), EOD 1557, no entries 1545, late cutoff 20 s, preview ON | build | trigger set changed v10.88; flip exit v10.92 |
| 11/05 | v10.70 | MES 3m | ema_f_sym = "", ema_s_sym = "MES 2m 14" (MES 3m back to 9 / 20) | mes3_ema_watch: slow 14 not robust | mes3_ema_watch 11/12: keep 9 / 20 (14 Δ +207 z 0.7; 16 Δ +226 z 0.9) |
| 11/04 | v10.68 | MES 3m | ema_f_sym "MES 3m 7", ema_s_sym += "MES 3m 14" | mes3_ema_grid 11/04: slow 14 +293, z 1.1 | reverted v10.70 |
| 11/04 | v10.67 | MES 3m | ats_tp1_sym = "MES 3m 2" | grid 108 setups: 3.0 / 2.0 / 100 % +143.8 R | reverted v10.82 |
| 11/03 | v10.60 | MNQ 3m / MES 3m | ats_tw_sym = "MNQ 3m 0, MES 3m 0" (late-away OFF) | toward_report 11/03: MNQ 3m +1518 z 2.1, MES 3m +262 z 1.7 | no scheduled follow-up |
| 11/03 | v10.55-56 | MES 3m | ats_pw_sym = "MES 3m 0600-1600 80, MES 3m 1800-2230 80" (else 100 %) | tp1_tod_report 11/03: time mix +153.7 vs +139.2 | re-check at 150+ setups; mes_sltp_grid: 80 % > 90 % > 100 % in every row |
| 11/03 | v10.54 | MES 3m | ats_slx_sym "MES 3m 3", ats_tp1_sym "MES 3m 1.75", ats_part_sym "MES 3m 100", caps "MES 3m 0" | mes_sltp_grid 10/30 + 11/02: 3.0 / 1.75 / 100 % +141.6 vs +41.3 | mes_sltp_grid 11/12: row still R; trail 1.3 tweak = C-010; cbc_daily 11/12: 19 setups · +7.4 on these exits (< 20, no judgment) |
| 11/02 | v10.52 | MGC 3m | ats_rpz_sym input (default empty) | rgate4 candidate +180 z 2.0 (run 1 of 3) | rgate 11/07: 0 robust runs |
| 11/01 | v10.51 | MES 2m | ema_s_sym = "MES 2m 14" | MES 2m replay Jun-Oct +206 z 1.7 | ema5 11/07: no revert flag |
| 10/30 | v10.48-49 | MGC 3m | shadow setups (VWAP-stretch blocked), default ON | replay: stretch filter still pays (+77) | stretch 11/12: 17 shadows, 11 wins, +18.1; keep "MGC 3m 4" |
| 10/29 | v10.47 | all | room line + room filters (default OFF) | 10/29 live | room_daily 11/12: MES 3m 0.2 x TP1 candidate (OOS 3 / 8), MGC 3m keep off |
| 10/28 | v10.45 | MGC 3m | MGC 3m back to base exits | daily stats revert flag 2 sessions | runner part superseded by v10.84 |
| 10/27 | v10.42 | MES 2m / MES 3m | ats_f_flip_sym = "MES 2m 4"; MES 3m back to base exits | MES 2m flips >= 4 blocked 9 / -34.7 | cbc_daily 11/12: flip counter + MTF gate live (0 violations since 10/28) |
| 10/20 | v10.32 | MES 2m | ats_mtg_sym = "MES 2m 1" | 16 against-MTF setups -21.9 | cbc_daily 11/12: gated row 16 / -21.9; xtf 11/12 baseline: MES 2m 1H gate not supported by replay |
| 10/19 | v10.31 | MGC 3m / MES 3m | TP1 2.0, 50 / 80 % at TP1, no BE | replay 10/12-10/19 | superseded |

## 3. Watch list

| Item | Chart | Study | Tally | Latest numbers | Still needed |
|---|---|---|---|---|---|
| Runner 50 % at TP1 + trail 3.5 (live v10.84) | MGC 3m | runner (Sat) + cbc_daily | HELD 1/3; revert flag count 0/20 from 11/13 | Δ +366 (11/09); live since 11/09 7 · +32.5 (+4.64/setup) vs baseline 29 · -24.3 | 2 more held weeks; 20 live setups from 11/13 |
| Bot flip-only exit for HTF CBC Flip 09:30-16:00 (live v10.92) | MES 3m bot | bot flip-exit watch (Sat) | week 0 (11/12) | bot windows HTF Flip 46: -73.5 -> +52.2 (flip only thirds +79 / -27 / +82); live (cbc_daily) 4 trades +90.0 vs +34.0 bracket | HELD weekly; FAILED -> "consider reverting" (live 15+ worse by > 30) |
| Bot trigger "LTF EMA20 Pierce (not beyond EMA9)" (live v10.88) | MES 3m bot | Sat bot study (data note 4) | 0 of 3 weekly runs | baseline 24 live -8.7, replay thirds -75 / -42 / +8; chart 32 / -6.9; since 11/09 2 bot trades -14.8 | 3 more weekly runs + 20 new trades still negative -> "consider unticking" |
| Bot 5-day short filter (live v10.86) | MES 3m bot | botwin (Sat) | WEAKER 0/3 | beyond random -1 / +71 / +63; live 7 shorts skipped -34.8 | 3 held weeks; not FAILED yet |
| Bot windows 13:00-14:00 removed (live v10.87) | MES 3m bot | botwin (Sat) | holds | 88 / -242 (-47 / -123 / -71) | keep checking weekly |
| Room x TP1 < 0.2 skip | MES 3m | room_daily (weekdays) | candidate; OOS 3 of 8 blocked | 36 blocked / -47.4 (avg -1.32), halves -19.0 / -28.4, thirds -16.1 / -23.0 / -8.2; kept avg +0.50; OOS 3 / -2.4 | 8+ out-of-sample blocked (MES 3m setups thin) |
| Skip against VWAP | MGC 3m | trend_guard (Sat) | 1/3 | beyond random +151 (+54 / +34 / +63) | 2 more weeks |
| 5-day EMA + 2 losses / 2 flip-outs guard | MNQ 3m | trend_guard (Sat) | 1/3 | beyond random +840 (+266 / +408 / +166); last 4 wk +439 | 2 more weeks |
| 5-day EMA shorts-only filter | M2K 3m | trend_guard (Sat) | 1/3 | beyond random +132 (+38 / +54 / +40) | 2 more weeks |
| London stop after 1st loss | MGC 3m | all_rules (Sat) | 1/3 | net +97; beyond random +84 / +92 / +31 | 2 more weeks |
| VWAP filter + London stop | MGC 3m | all_rules (Sat) | 1/3 | net +202; beyond random +103 / +89 / +108 | 2 more weeks |
| Balanced set (filter / stop / SL rule) | MES 3m | all_rules (Sat) | WEAKER 0/3 | net -4; last 4 wk +89 vs +160 | last 4 wk within 40 % of current |
| Cut if wrong side of HTF EMA9 at 18 min | MGC 3m | exit_lab (Sat) | promising 2 wk | +87 after costs T4R z 1.6 (+25 / +18 / +44) | 3rd week + walk-fwd pick positive |
| Bot trigger HTF EMA20 Pierce ON | MES 3m bot | bot_trigger (Sat) | 0/3 | Δ +89 (+125 / -27 / -9); live 5 / +10.5 | all thirds + live n >= 15 |
| Range gate OFF in NY only | MGC 3m | mgc3_gate_session (Sat) | 1 run (11/09) | Δ +154 (+96 / +25 / +32) | 3 weeks; Pine change needed |
| MGC 5m runner 80 % / trail 2.5 (and 50 % / 3.5) | MGC 5m | MGC 5m runner watch (Sat, new) | week 0 (11/12) | current -486; 80/2.5 +112 z 1.0 (+27 / +53 / +8) promising; 50/3.5 +162 z 1.0 (+1 / +109 / -56) noise | robust (z >= 2, all thirds) 3 weeks + last 4 wk Δ >= 0 |
| Setup order cut-off after HTF flip (MGC 3m first 2) | MGC 3m (+ MES / MGC 2m-5m) | flip order (Sun, new) | week 0 (11/12) | replay #3+ 203 / -192 bot, -269 chart (all thirds); live disagrees (#6+ +0.30) | 3 weeks replay + live agree; Pine change needed |
| 1H / 4H CBC gates (MES 5m skip 1H against; MES 2m / M2K 5m / M2K 2m skip 4H against) | MES 5m, MES 2m, M2K | 1H/4H XTF study (on demand, new) | run 1 (11/12) | MES 5m 1H against replay 716 / -596 (-204 / -53 / -340), live kept +0.17 vs -0.74; MES 2m 4H 1162 / -679 | 3 qualifying runs >= 7 days apart (MES 5m = add "MES 5m 1" to 1H MTF list; 4H = Pine change) |
| Exit-rule alerts live hits (v10.79) | MES 3m / MGC 3m | mes3_ema_watch (E) | MES 1 / MGC 2 of 15 | MES TP cut +6.19 vs CBC; MGC lock +8.10 (2 comparable) | 15 live hits each |
| Chart slow EMA 14 / 16 | MES 3m | mes3_ema_watch (A) | beat last 4 wk 4 of 5 / 4 of 5 | 14 Δ +207 z 0.7 (+6 / +37 / +164); 16 Δ +226 z 0.9 (-1 / +79 / +148); last 4 wk +29 / +77; TP1 1.5: 16 +221 z 1.0 all thirds + | 5 of last 7 runs + z >= 2 all thirds |
| 5m confirmation | MES 2m / MES 3m | mes3_ema_watch (C) | keep watching | live 2m 88 conf +0.10 vs 54 unconf -1.69; 3m 77 +0.09 vs 30 -0.63; replay 2m z -0.1, 3m z 0.4; ~0 unconfirmed since 10/28 | replay z >= 1 all thirds; needs new CBC filter |
| LTF Pierce LATE trigger off | MES 2m / 3m / 5m | mes3_ema_watch (D) | no trigger 40 ended | 2m 18 / -24.0, 3m 20 / -21.1, 5m 15 / -7.5; replay disagrees | 40 ended + replay |
| Late + room < 0.5 x TP1 skip | MES 2m / 3m / 5m | mes3_ema_watch (F) | too few | MES 3m 8 / +7.2; MES 2m 5 / -16.2; MES 5m 5 / +13.5 | more ended setups |
| Stop floor min 6 + TP1 2-2.5 ATR no cap, 50 % | MGC 3m | mgc_sltp_grid | ✱ (both halves), not T | 11/12: min 6 + 2.5 ATR 50 % +58.4 (+5.9 / -37.7 / +90.1); min 5 +41.0 / min 7 +46.4 not ✱ | middle third (10/26-11/03) positive + neighbours ✱ |
| Breakout window 5 bars | MGC 3m | breakout_flip | promising (3 runs, week of 11/09) | +111 z 1.2 (+77 / +0 / +33) | robust 3 weeks |
| Levels + prior-day H/L | MGC 3m | breakout_flip | **FAILED 11/09** | -20 (still worse 11/12) | dropped by study |
| Clean break >= 0.25 ATR | MES 3m | breakout_flip | **FAILED 11/09** | +1 z 0.0 | count restarted |
| Block OPPOSING order block | MNQ 2m | ob_setup (now weekly Fri) | worth testing (3 runs, gap narrower) | 11/12: OPP 51 · 33 % · -5.55 avg, net -282.9 (halves -186.2 / -96.7); Δavg -4.98 (CBC -4.91) | more runs; Pine change |
| VWAP 4 + HTF EMA20 cap 3 ATR | MGC 3m | ema_stretch | promising 8 runs, robust 0 | +62 z 1.1 (+33 / +8 / +20) | robust (new input needed) |
| EMA200 cap 4 ATR | MES 2m | ema_stretch | promising 4 runs, robust 0 | +185 z 1.6 (+17 / +1 / +167) | robust (new input needed) |
| HTF EMA9 Pierce off / both pierces off / HTF 7-16 | MES 3m | htf_ema + trigger | promising, 0 robust | 11/12: both off +198 z 1.6 (+42 / +56 / +100); EMA9 off +154 z 1.6; 9/26 newly promising | robust + 20 live ended |
| Chart EMAs 16 / 34 / 120 | MES 5m | ema5 (Fri) + htf_ema | ema5 robust 2/3; htf_ema A+/H+/G+/C+ robust 7 runs in a row | htf_ema 11/12: A+ +490 z 3.1 (+200 / +136 / +154); live 2/8 ended | robust on 11/13 ema5 run |
| ER threshold 0.18 | MES 5m | filter_sweep (Fri) | robust 2/3 | +187 z 2.3 (+37 / +51 / +99) | robust on 11/13 |
| Crosses >= 4 block | MGC 3m | filter_sweep (Fri) | promising, 0 robust | +167 z 1.8 | robust |
| Crosses >= 6 block | MES 3m | filter_sweep (Fri) | promising, 0 robust | +64 z 1.6 | robust |
| Range gate 4.0 / zone 30 % | MGC 3m | rgate (Fri) | 0/3 robust | +169 z 1.8 (+76 / +9 / +84) | 3 robust runs |
| OR block NY OFF | MGC 3m | orf (Fri) | 0 robust | +109 z 2.5 (-1 / +65 / +45) | 3 robust runs |
| Alerts in 22:30-03:00 gap | MES 3m | all_alerts (Fri) | 2/3 | +71 (+14 / +19 / +38) | run 3 on 11/13 |
| Alerts in 07:45-09:30 gap | MGC 2m | all_alerts (Fri) | 2/3 | +92 (+7 / +11 / +74) | run 3 on 11/13 |
| Alerts in 07:45-09:30 gap | MGC 5m | all_alerts (Fri) | 2/3 | +120 (+48 / +36 / +36) | run 3 on 11/13 |
| Untick LTF EMA20 Pierce | MES 2m | trigger (Fri) | promising, 0 robust | +109 z 1.1; live 51 / -37.6 | robust |
| Wider SL1 0.75 ATR | MES 5m | sl_reversal (Fri) | sim 3/3, live fails | live -1.7 / -17.1 / -23.1 | live net positive |
| HTF slope Both, min 0.5 pt | MES 3m | ema_slope (Fri) + cbc_daily | promising, 0 robust | +194 z 1.3; live 11/12 >= 0.5 52 / +52.8 vs < 0.5 55 / -64.4 (neg both halves) | 3 robust weeks |
| Shallow pullback < 0.75 ATR skip | MGC 2m | cbc_daily | candidate, < 20 setups | 16 · -18.6, halves -26.0 / +7.4 | 20 setups + both halves negative |
| Flips >= 4 block (non-FL subset) | MGC 2m | cbc_daily | watch (new 11/12) | 30 · -40.9 (both halves); without FL 17 · -6.1; replay -15 z -0.3 | non-FL subset clearly negative over 20+ |
| Skip LTF EMA20 Pierce 18:00-20:30 | MGC 2m | evening (Fri) | sim neg 3 checks | sim 48 / -51.5; live 9 / -2.1 | live >= 10 negative |
| Room L5 (< 0.5x TP1) skip | MES 3m | room_study (Fri) | live meets (b), sim no | live 69 -0.79 vs +1.88 | sim robust |
| Pierce 3-4 HTF candles | MES 5m | flip_timing (Fri) | sim meets, live fails | sim 118 / -102.1; live 9 / +1.1 | live negative |

## 4. Studies

| Study | Schedule | Last run | Report | Latest verdict | Change warranted? |
|---|---|---|---|---|---|
| CBC settings sync check | Tue/Thu/Fri 16:47 (was daily 14:43) | 11/12 16:47 | settings_sync_report.md | v10.93 (bot-only changes), 0 MISMATCH, 1 known; flip-only bot exit not modelled | no |
| Weekly 3m: time stop / cut (A) | Sat 18:27 | 11/09 13:58 | sl_time_rule_report.md | no candidates | no |
| Weekly 3m: TP + SL combo (B) | Sat 18:27 | 11/09 13:58 | combo_tp_sl_report.md | no change | no |
| Weekly 3m: exit lab (C) | Sat 18:27 | 11/09 13:58 | exit_lab_report.md | MGC h9 cut promising wk 2 | no |
| Weekly 3m: trend guard (D) | Sat 18:27 | 11/09 13:58 | trend_guard_report.md | MGC VWAP / MNQ guard / M2K shorts HELD 1/3 | no |
| Weekly 3m: runner (E) | Sat 18:27 | 11/09 | runner_report.md | MGC 50 % / 3.5 HELD 1/3 | no (DONE v10.84) |
| Weekly 3m: all rules combined (F) | Sat 18:27 | 11/09 | all_rules_combined_report.md | MGC London 1/3, VWAP+London 1/3; MES balanced WEAKER | no |
| Weekly 3m: bot windows (G) | Sat 18:27 | 11/09 | botwin_report.md | short filter WEAKER 0/3; 13-14 removal right | no |
| Weekly 3m: bot triggers (H) | Sat 18:27 | 11/09 | bot_trigger_report.md | keep triggers (v10.88 since added LTF not beyond) | no |
| Weekly 3m: gate by session (I) | Sat 18:27 | 11/09 | mgc3_gate_session_report.md, mes3_gate_session_report.md | MGC NY range gate off promising | no |
| MES study: EMA, TP1, 5m-confirm, trigger, exit rules | weekdays 17:37 | 11/12 17:37 | mes3_ema_watch_report.md | keep 9 / 20 + TP1 1.75; first MES TP-cut hit +6.19; MES 3m alerts thin; MGC 3m no setups since 11/11 | no |
| CBC room-to-first-level daily check | weekdays 17:47 | 11/12 17:48 | room_daily_report.md | MES 3m 0.2 x TP1 candidate (OOS 3 / 8); MGC 3m keep off | no |
| CBC daily stats checklist | weekdays 17:26 | 11/12 17:26 | cbc_daily_report.md | no suggestion meets the rule; MGC 3m revert count starts 11/13; MGC 2m gate still unconfirmed | no (C-001 withdrawn 11/12) |
| MES + MGC 3m stop / TP grid | weekdays 17:27 | 11/12 08:45 | mes_sltp_grid_report.md, mgc_sltp_grid_report.md | MES unchanged (no new setups), trail 1.3 still meets rule; MGC keep v10.84 | YES -> C-010 |
| Breakout + flip-ER variants | weekdays 17:28 | 11/12 17:28 | breakout_flip_report.md | no change; MGC 5-bar window promising | no |
| Setups in order blocks | Fri 17:05 (was weekdays) | 11/12 09:59 | ob_setup_report.md | MNQ 2m block OPPOSING worth testing (gap narrower) | no |
| Alert parameter sweep | weekdays 17:05 | 11/12 17:07 | alert_param_report.md | MES 3m cd 8 (4th run, stronger), MGC 2m cd 5 (8th run) worth considering | YES -> C-003, C-005 |
| Stretch filter check | every 3 days 18:37 | 11/12 17:09 | ema_stretch_report.md, stretch_study_report.md | keep "MGC 3m 4"; 2 promising, 0 robust | no |
| HTF EMA length check | every 2 days 19:13 | 11/12 09:58 (run 7) | htf_ema_report.md | keep HTF 9 / 20; MES 5m 16/34/120 robust 7 runs (chart-EMA signal) | no |
| Stop points + max loss sweep | Fri 16:29 | 11/07 09:50 | stop_sweep_report.md | no change | no |
| EMA slope gate | Fri 17:41 | 11/07 09:48 | ema_slope_report.md | keep Off | no |
| Evening session + flip timing | Fri 17:53 | 11/07 09:52 | evening_session_report.md, flip_timing_report.md | flip timing: MES 3m 5-8 meets rule | YES -> C-002 |
| Stop-out reversal | Fri 18:07 | 11/07 09:51 | sl_reversal_report.md | no change | no |
| Room-to-resistance weekly | Fri 18:23 | 11/07 09:52 | room_study_report.md | keep OFF | no |
| Chart EMA length weekly (5m) | Fri 18:47 | 11/07 09:57 | ema5_report.md | keep; MES 5m N 2/3 | no |
| Opening-range block weekly | Fri 19:37 | 11/07 09:50 | orf_report.md | keep as is | no |
| Trade Setup Filters sweep + MGC 3m range gate | Fri 20:13 | 11/07 09:51 | filter_sweep_report.md, rgate_report.md | MES 5m ER 0.18 robust 2/3 | no |
| Alerts + alert-session weekly | Fri 20:43 | 11/07 09:52 | all_alerts_report.md | 3 session gaps at 2/3 | no |
| Setup Triggers weekly | Fri 21:17 | 11/07 09:50 | trigger_report.md | keep all | no |
| MGC 2m weekly improvement | Fri 21:49 | 11/07 09:50 | mgc2_report.md | no change | no |
| Weekly loser-by-hour | Sat 10:17 | 11/07 10:17 | hour_loss_weekly_report.md | 9 chart-hours meet blocking rule | YES -> C-006..C-009 |
| MES 3m bot flip-exit watch (new 11/12) | Sat 13:37 | no report yet (baseline 11/12) | flip_exit_watch.md (+ flip_exit_report.md, flip_exit_bot_report.md) | first run 11/14 | no |
| MGC 5m runner exit watch (new 11/12) | Sat 14:13 | no report yet (baseline 11/12) | mgc5_runner_report.md | first run 11/14 | no |
| Setup order since HTF flip (new 11/12) | Sun 13:23 | 11/12 14:48 (baseline) | flip_order_summary.md | no cut-off that replay and live agree on | no |
| 1H MTF + 4H XTF confirmation (new 11/12) | on demand | no report yet (run 1 11/12 in task text) | xtf_summary.md | MES 5m 1H / MES 2m, M2K 4H candidates run 1 | no |
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
| Other: TP1 % by time of day | one-off | 11/03 | tp1_tod_report.md | re-check at 150+ | done (v10.55-56) |
| Other: loser by hour (first run) | one-off | 11/03 | hour_loss_report.md | first run | no |

## 5. Run log

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
