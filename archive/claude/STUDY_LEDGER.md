# CBC Study Ledger -- updated 2026-11-11 23:34 ET

**At a glance** (newest Pine = v10.87, 11/08; no new version since)
- Open changes: **9** -- C-001 MES 2m non-flip flop gate · C-002 MES 3m flip-timing gate ON (5-8 HTF) · C-003 / C-005 LTF EMA20 Pierce cooldown (MGC 2m 5 / MES 3m 8) · C-006..C-009 loser-hour blocks (MES 3m, MGC 2m, MNQ 2m, MNQ 3m) · C-010 MES 3m runner trail 1.7 -> 1.3 ATR (optional). C-004 WITHDRAWN 11/09. No item changed this run.
- Done in the last 7 days (11/05-11/11): v10.75-v10.87 -- alert hours + VWAP Bounce (v10.75/83), MGC 2m gates (v10.77), exit-rule alerts (v10.79), flip-timing gates (v10.81), MES 3m TP1 1.75 (v10.82), MGC 3m runner (v10.84), bot windows / short filter (v10.85-87). Nothing new since 11/09.
- **No new study runs since 11/09.** Scheduled runs on 11/11 (settings sync 14:43, MES watch 17:37, room daily 17:47; likely the other weekday studies too) **FAILED: usage limit reached**; 11/10 runs also left no reports. Weekday studies are 2 days behind (not stale yet; stale after 11/13).
- Stale studies: **CBC settings sync check -- STALE** (last 11/09 14:43, > 2 days; 11/11 run failed on usage limit).
- Settings sync (last good 11/09 14:43): v10.87, 0 MISMATCH, 1 known. Open action from daily stats: **MGC 2m range gate (v10.77) not confirmed live** -- load v10.87 on the MGC 2m chart and recreate its alert.

## 1. Changes warranted (open)

| ID | Flagged | Last confirmed | Chart | Exact change | Evidence | Source | Status |
|---|---|---|---|---|---|---|---|
| C-010 | 11/09 | 11/09 | MES 3m | ats_trl_sym = "MGC 3m 3.5, MES 3m 1.3" (runner trail 1.7 -> 1.3 ATR) | grid 119 setups: SL 3 / TP1 1.75 / 80 % / trail 1.3 = +189.2 ✱ T R (thirds +38.4 / +9.1 / +141.8) vs live proxy trail 1.7 +180.9 (+32.3 / +5.0 / +143.6); Δ +8.3 (~+0.07/setup), last third -1.8; trail 1.3 best in every row; bot (100 % at TP1) unaffected | mes_sltp_grid_report.md | OPEN -- "optional low-stakes tweak"; not in v10.87 |
| C-001 | 11/06 | 11/09 | MES 2m | ats_fl2_sym = "MGC 2m 1, MES 2m 1" | non-flip FL 34 · 24 % · -103.5 (-3.05/setup), halves -64.6 / -39.0 vs no-FL 54 · +15.2; since 10/28 FL 12 / -31.0 vs 24 / +36.5; 11/09: 2 more FL losers (-12.8) | cbc_daily_report.md | OPEN -- not in v10.87 (default "MGC 2m 1") |
| C-002 | 11/07 | 11/07 | MES 3m | ats_fw_sym = "MES 3m 5" (ats_fw2_sym "MES 3m 8" already set) | sim 237 / -88.9, thirds -35 / -52 / -2; live 18 / -14.2 (pierces 17 / -20.8); 3/3 weekly checks | flip_timing_report.md | OPEN -- gate built v10.81 but OFF; waits for 11/13 check (last third -2) |
| C-003 | <=11/07 (5th run) | 11/09 (6th run) | MGC 2m | ltf_ema20_pierce_cooldown = 5 (MGC 2m chart only) | 1035 alerts at current; cd 5: (a) -36.5 vs -196.8, (b) +50.9 vs -10.2; validation 82 / 77 % | alert_param_report.md | OPEN -- not taken in v10.83 ("still loses under (a)"); not in v10.87 |
| C-004 | 11/07 (1st run) | 11/07 | MES 2m | ltf_ema20_pierce_cooldown = 5 (MES 2m chart only) | 11/07: (a) -206.2 vs -365.5, (b) +97.7 vs +77.4; 11/09: validation 68 / 71 % -> unreliable | alert_param_report.md | WITHDRAWN 11/09 (replay validation fell below 70 %; study dropped it) |
| C-005 | 11/07 (1st run) | 11/09 (2nd run) | MES 3m | ltf_ema20_pierce_cooldown = 8 (MES 3m chart only) | 679 alerts at current; cd 8: (a) +19.0 vs -256.5, (b) +165.9 vs +14.1 (now positive under both); validation 81 / 79 % | alert_param_report.md | OPEN -- not taken in v10.83; not in v10.87 |
| C-006 | 11/07 | 11/07 | MES 3m | Pine change needed: no new setups 06-07 and 13-15 ET (alert_hours_sym already mutes 13:00-14:00 alerts; bot_win drops 13:00-14:00 since v10.87) | live 06-07 10 / -18.2; 13-15 22 / -82.2; !! both halves, held 2 runs | hour_loss_weekly_report.md | OPEN -- partly covered (alerts + bot only) |
| C-007 | 11/07 | 11/07 | MGC 2m | Pine change needed: no new setups 04-05, 07-08, 21-22 ET (or alert_hours_sym MGC 2m windows) | live 12 / -15.4; 10 / -26.2; 13 / -29.0; !! both halves, held 2 runs | hour_loss_weekly_report.md | OPEN -- not in v10.87 |
| C-008 | 11/07 | 11/07 | MNQ 2m | Pine change needed: no new setups 04-05 and 14-15 ET | live 14 / -45.5; 14 / -77.2; !! both halves, held 2 runs | hour_loss_weekly_report.md | OPEN -- not in v10.87 |
| C-009 | 11/07 | 11/07 | MNQ 3m | Pine change needed: no new setups 06-07 and 13-14 ET | live 10 / -109.2; 10 / -162.5; !! both halves, held 2 runs | hour_loss_weekly_report.md | OPEN -- not in v10.87 |

## 2. Changes made

| Date | Version | Chart | Change | Why (evidence) | Follow-up / latest check |
|---|---|---|---|---|---|
| 11/08 | v10.87 | MES 3m bot | bot_win = "1830-2200, 0300-1300, 1500-1530" | 13:30-14:00 -198 pts, 3.5 SD from chance, neg every third; 13:00-13:30 neg every third; replay -674 -> -412 (mes3_time_zones_table.md) | botwin 11/09: 13:00-14:00 still 88 / -242 (-47 / -123 / -71) -> removal right; settings sync 11/09 botwin inwin MATCH |
| 11/08 | v10.86 | MES 3m bot | bot_d5 = true (no shorts above 5-day EMA) | botwin + entry_slots: -702 -> -409; beyond random +5 / +84 / +58; last 4 wk +139 vs +130; DD 907 -> 647 | botwin 11/09: WEAKER 0/3 (beyond random -1 / +71 / +63; last 4 wk +149 vs +150); keep ON. cbc_daily 11/09: filter skipped 1 short (-5.0) |
| 11/08 | v10.85 | MES 3m bot | bot_win = 6-window set (dropped 03:30-04, 06-06:30, 07:30-08, 13-14) | mes3_entry_slots_report.md: -735 -> -229 (no filter) | superseded by v10.87 (other removals = noise, additions hindsight) |
| 11/08 | v10.84 | MGC 3m | ats_part_sym += "MGC 3m 50"; ats_trl_sym = "MGC 3m 3.5" | runner 11/08: Δ +353 (50 % / 3.5), all thirds, last 4 wk +146 vs +66; walk-fwd rank 2/39 | runner 11/09: HELD 1/3 (Δ +366); cbc_daily 11/09: 4 live · +14.3 (revert flag 4/20); mgc_sltp_grid 11/09: 50 % beats 80 % at every stop floor |
| 11/07 | v10.83 | MGC 2m / MES 3m / MES 2m | vb_tw_sym += "MGC 2m 0000-2400 0.01, MES 3m 0000-2400 4, MES 2m 0000-2400 4" | alert_param 11/07: MGC 2m (a) +451 vs +102 (9 runs); MES 3m (a) +84 vs -61; MES 2m (a) +288 vs +111 | alert_param 11/09: v10.83 values best on MES 2m ((a) +319.8) and MGC 2m ((a) +527.6); post-change alerts match replay (MES 2m 4/4, MGC 2m 9/9); MES 3m 4 ~ level with 2 (small sample) |
| 11/07 | v10.82 | MES 3m | ats_tp1_sym = "MES 3m 1.75" (reverts v10.67) | 117 setups: 1.75 +202.6 (thirds +35.8 / +13.7 / +153.2) vs 2.0 +184.5 | mes_sltp_grid 11/09: SL 3 / TP1 1.75 row fully R (7/7), 119 setups; mes3_ema_watch (B) 11/09: keep 1.75 (2.0 +3.9, halves -6.8 / +10.7) |
| 11/07 | v10.81 | MES 2m / MES 3m | ats_fa_sym = "MES 2m 9"; ats_fw2_sym = "MES 3m 8" (from-list empty = OFF) | flip_timing: MES 2m 9-16 HTF sim 105 / -78.2 all thirds, live 14 / -27.8; 3 weekly checks | flip_timing 11/07 rerun: both rules still meet; cbc_daily 11/09: no MES 3m flip-timing violations; MES 3m ON = C-002 |
| 11/06 | v10.79 | MES 3m / MGC 3m | xr_cut_sym "MES 3m" (21 min / 70 % / ATR 1.5x); xr_lock_sym "MGC 3m" (75 % -> +55 %); alerts only | 11/06 exit-ideas replay: MES +131 z 2.1 all thirds; MGC +209 z 1.6 all thirds -- report: evidence not found in project | mes3_ema_watch (E) 11/09: first live hit MGC 3m lock 11/09 11:00 +3.2 vs CBC +2.0 (+1.2); MES 0 hits; replay MES +168 z 2.8, MGC +307 z 2.4 (last 4 wk -45) |
| 11/06 | v10.77 | MGC 2m | ats_fl2_sym = "MGC 2m 1"; ats_rp_sym += "MGC 2m 5" | daily stats 11/05: non-flip FL 43 / -71.0 vs 58 / +28.5; range-gated 25 / -35.9 (halves -9.6 / -26.3) | cbc_daily 11/09: **NOT confirmed live** -- 11/09 05:22 LONG at 87 % / 4.3 ATR came through (-3.6); since 11/06 10 · -16.1; action: load v10.87 on MGC 2m + recreate alert |
| 11/06 | v10.77 | MES 3m bot | bot_win = "1830-2200, 0300-1400, 1500-1530" (was 0930-1545) | evidence not found in project | superseded by v10.85 / v10.87 |
| 11/05 | v10.75 | MGC 3m / MES 3m | vb_tw_sym = "MGC 3m 0300-1700 0.01"; alert_hours_sym = "MES 3m 1830-2100, 0430-1300, 1400-1430" | MGC 3m sweep 11/05: (a) +$4,388 vs +$997; alert hours: evidence not found in project | alert_param 11/09: MGC 3m tod still best row ((a) +445.2, (b) +25.2) |
| 11/05 | v10.71-76 | MES 3m bot | CrossTrade bot (Flip + LTF beyond EMA9), EOD 1557, no entries 1545, late cutoff 20 s, preview ON | build, not study-driven -- evidence not found in project | bot_trigger 11/09: keep triggers (current set -158, rank 38/63); mes3_ema_watch 11/09: bot set 30 / +44.4 vs rest 75 / -42.6 |
| 11/05 | v10.70 | MES 3m | ema_f_sym = "", ema_s_sym = "MES 2m 14" (MES 3m back to 9 / 20; reverts v10.68) | mes3_ema_watch: slow 14 not robust (z 0.6), last 5 days -34 | mes3_ema_watch 11/09: keep 9 / 20 (14 Δ +204 z 0.7; 16 Δ +201 z 0.8) |
| 11/04 | v10.68 | MES 3m | ema_f_sym "MES 3m 7", ema_s_sym += "MES 3m 14" | mes3_ema_grid 11/04: slow 14 +293, last 4 wk +134; z 1.1 | reverted v10.70 |
| 11/04 | v10.67 | MES 3m | ats_tp1_sym = "MES 3m 2" | grid 108 setups: 3.0 / 2.0 / 100 % +143.8 R | reverted v10.82 |
| 11/03 | v10.60 | MNQ 3m / MES 3m | ats_tw_sym = "MNQ 3m 0, MES 3m 0" (late-away OFF) | toward_report 11/03: MNQ 3m +1518 z 2.1, MES 3m +262 z 1.7, all thirds | no scheduled follow-up |
| 11/03 | v10.55-56 | MES 3m | ats_pw_sym = "MES 3m 0600-1600 80, MES 3m 1800-2230 80" (else 100 %) | tp1_tod_report 11/03: time mix +153.7 vs 100 % all day +139.2, ✱T, 102 setups | re-check at 150+ setups (no scheduled task); mes_sltp_grid 11/09: 80 % > 90 % > 100 % in every row |
| 11/03 | v10.54 | MES 3m | ats_slx_sym "MES 3m 3", ats_tp1_sym "MES 3m 1.75", ats_part_sym "MES 3m 100", caps "MES 3m 0" | mes_sltp_grid 10/30 + 11/02: 3.0 / 1.75 / 100 % +141.6 vs +41.3, both halves, all thirds | mes_sltp_grid 11/09: row still R 7/7; trail 1.3 tweak = C-010 |
| 11/02 | v10.52 | MGC 3m | ats_rpz_sym input (default empty = no change) | rgate4 candidate +180 z 2.0 (run 1 of 3) | rgate 11/07: gate 4 / zone 30 % +169 z 1.8, 0 robust runs |
| 11/01 | v10.51 | MES 2m | ema_s_sym = "MES 2m 14" | MES 2m replay Jun-Oct +206 z 1.7, all thirds | ema5 11/07: MES 2m U2 9/16 watch (noise); no revert flag |
| 10/30 | v10.48-49 | MGC 3m | shadow setups (VWAP-stretch blocked), default ON | 10/30 trend day; replay says stretch filter still pays (+77) | stretch 11/07: 8 shadows, 4/8 win, +1.4 |
| 10/29 | v10.47 | all | room line + room filters (default OFF) | 10/29 live: MES 3m L5 -1.77 vs +0.07; MGC 3m OB -1.63 vs +0.33 | room_study 11/07: keep both OFF; room_daily 11/09: MES 3m room x TP1 < 0.2 candidate (waiting OOS), MGC 3m keep off |
| 10/28 | v10.45 | MGC 3m | MGC 3m back to base exits (SL1 1.7 + min 5, TP1 1.7 cap 6, 80 %, BE, trail 1.7) | daily stats revert flag 2 sessions; 29 setups -0.4 vs +16.9 base | cbc_daily 11/07: confirmed; runner part superseded by v10.84 |
| 10/27 | v10.42 | MES 2m / MES 3m | ats_f_flip_sym = "MES 2m 4"; MES 3m back to base exits | MES 2m flips >= 4 blocked 9 / -34.7; MES 3m 43 setups -38.0 -> -9.0 | cbc_daily 11/09: flip counter live (0 violations since 10/28); MES 3m exits superseded v10.54 |
| 10/20 | v10.32 | MES 2m | ats_mtg_sym = "MES 2m 1" | 16 against-MTF setups -21.9, both halves | cbc_daily 11/09: gated row 16 / -21.9; mgc2: MTF gate on MGC 2m -311 (keep OFF there) |
| 10/19 | v10.31 | MGC 3m / MES 3m | TP1 2.0, 50 / 80 % at TP1, no BE (per symbol) | replay 10/12-10/19: MGC -9.7 -> +10.3, MES +63.5 -> +82.6 | superseded by v10.42 / v10.45 / v10.54 |

## 3. Watch list

| Item | Chart | Study | Tally | Latest numbers | Still needed |
|---|---|---|---|---|---|
| Runner 50 % at TP1 + trail 3.5 (live v10.84) | MGC 3m | runner (Sat) + cbc_daily | HELD 1/3; live revert flag 4/20 | Δ +366 (+168 / +10 / +188); last 4 wk +160 vs +68; live 4 · +14.3 (+3.56/setup) | 2 more held weeks; 20 live setups for revert check |
| Bot 5-day short filter (live v10.86) | MES 3m bot | botwin (Sat) | WEAKER 0/3 | beyond random -1 / +71 / +63; last 4 wk +149 vs +150 | 3 held weeks; not FAILED yet |
| Bot windows 13:00-14:00 removed (live v10.87) | MES 3m bot | botwin (Sat) | holds | 88 / -242 (-47 / -123 / -71) | keep checking weekly |
| Room x TP1 < 0.2 skip | MES 3m | room_daily (weekdays) | candidate; OOS 2 of 8 blocked | 35 blocked / -52.6 (avg -1.50), halves -19.0 / -33.7, thirds -16.1 / -23.0 / -13.5; kept avg +0.78 vs +0.02; OOS (from 11/06 12:00) 2 / -7.6 | 8+ out-of-sample blocked setups (rule d) |
| Skip against VWAP | MGC 3m | trend_guard (Sat) | 1/3 | beyond random +151 (+54 / +34 / +63); last 4 wk +19.5 | 2 more weeks; walk-fwd third 3 -105 |
| 5-day EMA + 2 losses / 2 flip-outs guard | MNQ 3m | trend_guard (Sat) | 1/3 | beyond random +840 (+266 / +408 / +166); last 4 wk +439 | 2 more weeks |
| 5-day EMA shorts-only filter | M2K 3m | trend_guard (Sat) | 1/3 | beyond random +132 (+38 / +54 / +40) | 2 more weeks |
| London stop after 1st loss | MGC 3m | all_rules (Sat) | 1/3 | net +97; beyond random +84 / +92 / +31; last 4 wk +55 vs +38 | 2 more weeks |
| VWAP filter + London stop | MGC 3m | all_rules (Sat) | 1/3 | net +202; beyond random +103 / +89 / +108; last 4 wk +68 vs +38 | 2 more weeks |
| Balanced set (filter / stop / SL rule) | MES 3m | all_rules (Sat) | WEAKER 0/3 | net -4; beyond random +50 / +439 / +2; last 4 wk +89 vs +160 | last 4 wk within 40 % of current |
| Cut if wrong side of HTF EMA9 at 18 min | MGC 3m | exit_lab (Sat) | promising 2 wk | +87 after costs T4R z 1.6 (+25 / +18 / +44); last 4 wk +29 | 3rd week + walk-fwd pick positive |
| Bot trigger HTF EMA20 Pierce ON | MES 3m bot | bot_trigger (Sat) | 0/3 | Δ +89 (+125 / -27 / -9); live 5 / +10.5 | all thirds + live n >= 15 |
| Range gate OFF in NY only | MGC 3m | mgc3_gate_session (Sat) | 1 run (11/09) | Δ +154 (+96 / +25 / +32); last 4 wk +15; NY gated 106 / +101 z 1.2 | 3 weeks; Pine change needed (per-session) |
| Exit-rule alerts live hits (v10.79) | MES 3m / MGC 3m | mes3_ema_watch (E) | MES 0 / MGC 1 of 15 live | MGC lock 1 hit +1.2 vs CBC; replay MES +168 z 2.8; MGC +307 z 2.4 (last 4 wk -45) | 15 live hits each |
| Chart slow EMA 14 / 16 | MES 3m | mes3_ema_watch (A) | beat last 4 wk 2 of 3 / 2 of 3 | TP1 1.75: 14 Δ +204 z 0.7 (+6 / +45 / +153); 16 Δ +201 z 0.8 (-1 / +78 / +124); last 4 wk +35 / +59; last 5 days -85 / -28 | 5 of last 7 runs + z >= 2 all thirds |
| 5m confirmation | MES 2m / MES 3m | mes3_ema_watch (C) | keep watching | live 2m 66 conf +0.14 vs 54 unconf -1.69 (+1.83), 3m +0.91 (halves disagree); replay 2m z -0.1, 3m z 0.4; 0 unconfirmed since 11/06 | replay z >= 1 all thirds; needs new CBC filter |
| LTF Pierce LATE trigger off | MES 2m / 3m / 5m | mes3_ema_watch (D) | no trigger 40 ended | live 2m 15 / -27.0, 3m 20 / -21.1, 5m 9 / -4.7; replay disagrees (2m z -1.0, 5m z -1.7) | 40 ended + replay |
| Late + room < 0.5 x TP1 skip | MES 2m / 3m / 5m | mes3_ema_watch (F) | too few (new 11/09) | MES 3m 8 / +7.2 (not losing); MES 2m 3 / -8.4; MES 5m 2 / +7.0 | more ended setups |
| Stop floor min 6 + TP1 2-2.5 ATR no cap, 50 % | MGC 3m | mgc_sltp_grid | ✱, not T | min 6 + 2.5 ATR 50 % +41.4 ✱ (+13.7 / -45.1 / +72.7); min 5 / 7 neighbours not ✱ | middle third (10/25-10/30) positive + neighbours ✱ |
| Breakout window 5 bars | MGC 3m | breakout_flip | promising (week of 11/09 #1 after reset) | +103 z 1.1 (+77 / +0 / +25) | robust 3 weeks |
| Levels + prior-day H/L | MGC 3m | breakout_flip | **FAILED 11/09** (robust 2/3 then worse) | -20 z -0.5 (-10 / -6 / -3) under synced live exits | dropped by study (streak reset) |
| Clean break >= 0.25 ATR | MES 3m | breakout_flip | **FAILED 11/09** (promising -> noise) | +1 z 0.0 (+39 / +4 / -43) | count restarted after 11/08 script sync |
| Block OPPOSING order block | MNQ 2m | ob_setup | worth testing (2 runs, gap widened) | v1.08 OPP 40 · 32 % · -5.73 vs rest, Δavg -6.33; CBC 30, Δavg -8.40; both halves neg | more runs; no CBC input (Pine change) |
| VWAP 4 + HTF EMA20 cap 3 ATR | MGC 3m | ema_stretch | promising 6 runs, robust 0 | +62 z 1.1 (+33 / +8 / +20) | robust (new input needed) |
| EMA200 cap 4 ATR | MES 2m | ema_stretch | promising 2 runs | +125 z 1.1 (+17 / +1 / +107) | robust |
| HTF EMA9 Pierce off / both pierces off / HTF 7-16 | MES 3m | htf_ema + trigger | promising, 0 robust | 11/09: EMA9 off +137 z 1.5; both off +176 z 1.4; HTF 7 / 16 +148 z 1.1; trigger OFF +145 z 1.6; live EMA9 15 / +4.8 | robust + 20 live ended |
| Chart EMAs 16 / 34 / 120 | MES 5m | ema5 (Fri) + htf_ema | ema5 robust 2/3; htf_ema A+ robust 6 runs in a row | htf_ema 11/09: A+ +496 z 3.2 (+200 / +136 / +160); ema5: +499 z 3.2; live LTF20 33 / -34.5 | robust on 11/13 ema5 run |
| ER threshold 0.18 | MES 5m | filter_sweep (Fri) | robust 2/3 | +187 z 2.3 (+37 / +51 / +99) | robust on 11/13 |
| Crosses >= 4 block | MGC 3m | filter_sweep (Fri) | promising, 0 robust | +167 z 1.8 (+110 / +54 / +3); live 9 / -14.2 | robust |
| Crosses >= 6 block | MES 3m | filter_sweep (Fri) | promising, 0 robust | +64 z 1.6 (+18 / +33 / +13) | robust |
| Range gate 4.0 / zone 30 % | MGC 3m | rgate (Fri) | 0/3 robust | +169 z 1.8 (+76 / +9 / +84); last 4 wk +7.8 | 3 robust runs |
| OR block NY OFF | MGC 3m | orf (Fri) | 0 robust (Jan-Mar -1) | +109 z 2.5 (-1 / +65 / +45); removed 47 / +90 | 3 robust runs |
| Alerts in 22:30-03:00 gap | MES 3m | all_alerts (Fri) | 2/3 | +71 (+14 / +19 / +38) | run 3 on 11/13 (alert_hours_sym now overrides sessions) |
| Alerts in 07:45-09:30 gap | MGC 2m | all_alerts (Fri) | 2/3 | +92 (+7 / +11 / +74) | run 3 on 11/13 |
| Alerts in 07:45-09:30 gap | MGC 5m | all_alerts (Fri) | 2/3 | +120 (+48 / +36 / +36) | run 3 on 11/13 |
| Untick LTF EMA20 Pierce | MES 2m | trigger (Fri) | promising, 0 robust | +109 z 1.1 (+32 / +20 / +58); live 51 / -37.6 | robust |
| Wider SL1 0.75 ATR (Max SL1 cap) | MES 5m | sl_reversal (Fri) | sim 3/3, live fails | live -1.7 / -17.1 / -23.1 at 0.5 / 0.75 / 1.0 | live net positive |
| HTF slope Both, min 0.5 pt | MES 3m | ema_slope (Fri) + cbc_daily | promising, 0 robust | +194 z 1.3 (+0 / +129 / +65); live 11/09 >= 0.5 51 / +71.5 vs < 0.5 54 / -69.7 (neg both halves; mixed exit versions) | 3 robust weeks |
| Shallow pullback < 0.75 ATR skip (LTF EMA20 Pierce) | MGC 2m | cbc_daily | candidate, < 20 setups | 17 · -23.6, halves -26.0 / +2.4 (disagree) vs deep 67 · -22.9 | 20 setups + both halves negative |
| Skip LTF EMA20 Pierce 18:00-20:30 | MGC 2m | evening (Fri) | sim neg 3 checks | sim 48 / -51.5 (-9 / -20 / -22); live 9 / -2.1 | live >= 10 negative |
| Room L5 (< 0.5x TP1) skip | MES 3m | room_study (Fri) | live meets (b), sim no | live 69 -0.79 vs +1.88; sim -103 z -0.6 | sim robust |
| Pierce 3-4 HTF candles | MES 5m | flip_timing (Fri) | sim meets, live fails | sim 118 / -102.1; live 9 / +1.1 | live negative |

## 4. Studies

Note 11/11: scheduled runs on 11/11 failed with "usage limit reached" (settings sync, MES watch, room daily confirmed via the task list); no weekday study wrote a report on 11/10 or 11/11.

| Study | Schedule | Last run | Report | Latest verdict | Change warranted? |
|---|---|---|---|---|---|
| CBC settings sync check | daily 14:43 | 11/09 14:43 -- **STALE** (11/11 run failed: usage limit) | settings_sync_report.md | v10.87, no input changes; 0 MISMATCH, 1 known (MGCX runner base) | no |
| Weekly 3m: time stop / cut (A) | Sat 18:27 | 11/09 13:58 (as titled) | sl_time_rule_report.md | no candidates; keep exits on 4 charts | no |
| Weekly 3m: TP + SL combo (B) | Sat 18:27 | 11/09 13:58 | combo_tp_sl_report.md | MES +275 z 0.9, MGC +145 z 0.6; no change | no |
| Weekly 3m: exit lab (C) | Sat 18:27 | 11/09 13:58 | exit_lab_report.md | MGC h9 cut promising wk 2; keep exits | no |
| Weekly 3m: trend guard (D) | Sat 18:27 | 11/09 13:58 | trend_guard_report.md | MGC VWAP / MNQ guard / M2K shorts HELD 1/3 | no |
| Weekly 3m: runner (E) | Sat 18:27 | 11/09 (week-of; no time) | runner_report.md | MGC 50 % / 3.5 HELD 1/3 (Δ +366) | no (DONE v10.84) |
| Weekly 3m: all rules combined (F) | Sat 18:27 | 11/09 (week-of; no time) | all_rules_combined_report.md | MGC London 1/3, VWAP+London 1/3; MES balanced WEAKER 0/3 | no |
| Weekly 3m: bot windows (G) | Sat 18:27 | 11/09 (no time) | botwin_report.md | short filter WEAKER 0/3; 13-14 removal right | no |
| Weekly 3m: bot triggers (H) | Sat 18:27 | 11/09 (week-of; no time) | bot_trigger_report.md | keep triggers; HTF EMA20 Pierce 0/3 | no |
| Weekly 3m: gate by session (I) | Sat 18:27 | 11/09 (no time) | mgc3_gate_session_report.md, mes3_gate_session_report.md | MGC NY range gate off promising; MES keep gate | no |
| MES study: EMA, TP1, 5m-confirm, trigger, exit rules | weekdays 17:37 | 11/09 17:38 (11/11 run failed: usage limit) | mes3_ema_watch_report.md | keep 9 / 20 and TP1 1.75; 5m confirm / late trigger keep watching; first live exit-rule hit (MGC +1.2) | no |
| CBC room-to-first-level daily check | weekdays 17:47 | 11/09 17:48 (11/11 run failed: usage limit) | room_daily_report.md | MES 3m room x TP1 < 0.2 candidate, waiting OOS (2 of 8); MGC 3m keep off | no |
| CBC daily stats checklist | weekdays 17:26 | 11/09 17:27 (no 11/10-11/11 report) | cbc_daily_report.md | MES 2m non-flip flop gate stronger; MGC 2m range gate not live (reload v10.87 + recreate alert) | YES -> C-001 |
| MES + MGC 3m stop / TP grid | weekdays 17:27 | 11/09 17:28 (no 11/10-11/11 report) | mes_sltp_grid_report.md, mgc_sltp_grid_report.md | MES live exits R 7/7; trail 1.3 meets rule (optional); MGC no T cell, keep v10.84 | YES -> C-010 |
| Breakout + flip-ER variants | weekdays 17:28 | 11/09 17:29 (no 11/10-11/11 report) | breakout_flip_report.md | no change; MGC prior-day H/L streak failed; MGC 5-bar window promising | no |
| Setups in order blocks | weekdays 17:05 | 11/09 17:06 (no 11/10-11/11 report) | ob_setup_report.md | MNQ 2m block OPPOSING worth testing (gap widened); rest not enough | no |
| Alert parameter sweep | weekdays 17:05 | 11/09 17:06 (no 11/10-11/11 report) | alert_param_report.md | MES 3m cd 8 (2nd run), MGC 2m cd 5 (6th run) worth considering; MES 2m cd 5 dropped | YES -> C-003, C-005 (C-004 withdrawn) |
| Stretch filter check | every 3 days 18:37 | 11/07 18:38 (11/10 run missing) | ema_stretch_report.md, stretch_study_report.md | keep "MGC 3m 4"; 2 promising | no |
| HTF EMA length check | every 2 days 19:13 | 11/09 19:13 (11/11 run missing) | htf_ema_report.md | keep HTF 9 / 20; MES 3m pierce-off promising; MES 5m 16/34/120 robust 6 runs (chart-EMA signal) | no |
| Stop points + max loss sweep | Fri 16:29 | 11/07 09:50 | stop_sweep_report.md | no change on any chart | no |
| EMA slope gate | Fri 17:41 | 11/07 09:48 | ema_slope_report.md | keep Off; MES Both 0.5 promising | no |
| Evening session + flip timing | Fri 17:53 | 11/07 09:52 | evening_session_report.md, flip_timing_report.md | evening: none; flip timing: MES 3m 5-8 + MES 2m 9-16 meet rule | YES -> C-002 (MES 2m done v10.81) |
| Stop-out reversal | Fri 18:07 | 11/07 09:51 | sl_reversal_report.md | no change; MES 5m live fails | no |
| Room-to-resistance weekly | Fri 18:23 | 11/07 09:52 | room_study_report.md | keep room settings OFF | no |
| Chart EMA length weekly (5m) | Fri 18:47 | 11/07 09:57 | ema5_report.md | keep 9 / 20 / 200; MES 5m N 2/3 | no |
| Opening-range block weekly | Fri 19:37 | 11/07 09:50 | orf_report.md | keep as is; MGC 3m NY watch | no |
| Trade Setup Filters sweep + MGC 3m range gate | Fri 20:13 | 11/07 09:51 | filter_sweep_report.md, rgate_report.md | MES 5m ER 0.18 robust 2/3; rgate 0 robust | no |
| Alerts + alert-session weekly | Fri 20:43 | 11/07 09:52 | all_alerts_report.md | no change; 3 session gaps at 2/3 | no |
| Setup Triggers weekly | Fri 21:17 | 11/07 09:50 | trigger_report.md | keep all triggers | no |
| MGC 2m weekly improvement | Fri 21:49 | 11/07 09:50 | mgc2_report.md | no change; live gap flag 0/3 | no |
| Weekly loser-by-hour | Sat 10:17 | 11/07 10:17 | hour_loss_weekly_report.md | 9 chart-hours meet blocking rule | YES -> C-006..C-009 |
| Other: time + progress lock | one-off | 11/08 | time_lock_report.md | MES 0 of 64 better all thirds; no lock rule | no |
| Other: bot TP rules | one-off | 11/08 | bot_tp_report.md | bot 100 % at TP1 1.75 -26; TP1 2.0 +19 (+5 / -0 / +40) | no |
| Other: MES 3m entry slots | one-off | 11/08 | mes3_entry_slots_report.md | basis of v10.85 / v10.86 | done (v10.85-87) |
| Other: MFE study | one-off | 11/08 | mfe_report.md | trades give back best move; 20 % MES / 31 % MGC reach 1.5x TP1 -> runner study | done (v10.84) |
| Other: 5m study | one-off | 11/08 | study_5m_report.md | MES 5m: 5-day EMA filter + losing-stretch stop ✓ (-600 -> -184 after costs) | no (not on a rule) |
| Other: session loss stop / guard fix | one-off | 11/08 | session_loss_stop_report.md, guard_fix_report.md | feeds all_rules (stop only after 5 losing sessions) | no |
| Other: MES 3m EMA grid | one-off | 11/04 | mes3_ema_grid_report.md | basis of v10.68 (reverted v10.70) | no |
| Other: toward-flip | one-off | 11/03 | toward_report.md | basis of v10.60 | done (v10.60) |
| Other: TP1 % by time of day | one-off | 11/03 | tp1_tod_report.md | time mix +153.7 vs +139.2; re-check at 150+ | done (v10.55-56) |
| Other: loser by hour (first run) | one-off | 11/03 | hour_loss_report.md | first run of the weekly loser-by-hour check | no |

## 5. Run log

- 11/11 23:34 | Ledger check (no study run) | no new reports since 11/09; 11/11 settings sync / MES watch / room daily failed (usage limit); settings sync now STALE | -
- 11/09 19:13 | HTF EMA length (run 6) | keep 9 / 20; MES 3m pierce-off promising; MES 5m 16/34/120 robust 6 runs (chart-EMA) | -
- 11/09 17:48 | Room-to-first-level daily (first report) | MES 3m room x TP1 < 0.2 candidate, OOS 2 / 8; MGC 3m keep off | -
- 11/09 17:38 | MES watch | keep 9 / 20 + TP1 1.75; first live exit-rule hit (MGC lock +1.2) | -
- 11/09 17:29 | Breakout + flip-ER | no change; MGC prior-day H/L failed; MGC 5-bar window promising | -
- 11/09 17:28 | MES + MGC SL/TP grid | MES live row R 7/7; trail 1.3 meets rule (optional); MGC no change | C-010
- 11/09 17:27 | Daily stats | MES 2m flop gate suggestion stronger; MGC 2m range gate not live | C-001
- 11/09 17:06 | Alert parameter sweep | MES 3m cd 8 (2nd), MGC 2m cd 5 (6th); MES 2m cd 5 dropped (unreliable) | C-003, C-005; C-004 withdrawn
- 11/09 17:06 | OB setups | MNQ 2m block OPPOSING worth testing (gap widened) | -
- 11/09 14:43 | Settings sync | v10.87, 0 mismatch, 1 known | -
- 11/09 (no time) | Weekly 3m (I) gate by session | MGC 3m NY range gate off +154 promising; MES keep gate | -
- 11/09 (no time) | Weekly 3m (G) bot windows | short filter WEAKER 0/3; 13-14 still -242 | -
- 11/09 (no time) | Weekly 3m (H) bot triggers | keep; HTF EMA20 Pierce 0/3 | -
- 11/09 (no time) | Weekly 3m (F) all rules | MGC London 1/3, VWAP+London 1/3; MES balanced WEAKER | -
- 11/09 (no time) | Weekly 3m (E) runner | MGC 50 % / 3.5 HELD 1/3 (Δ +366) | -
- 11/09 13:58 | Weekly 3m (D) trend guard | MGC VWAP / MNQ guard / M2K shorts HELD 1/3 | -
- 11/09 13:58 | Weekly 3m (C) exit lab | MGC h9 cut promising wk 2; keep exits | -
- 11/09 13:58 | Weekly 3m (B) TP + SL combo | no candidate | -
- 11/09 13:58 | Weekly 3m (A) time stop | no candidate | -
- 11/08 14:43 | Settings sync | no input changes; 1 mismatch + 1 inline | -
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
- 11/07 09:47 | MES + MGC SL/TP grid | MES ready YES (done v10.54/82); MGC no change | -
- 11/07 09:46 | Daily stats | MES 2m non-flip flop gate suggested | C-001
- 11/07 09:44 | MES watch (11/06 run) | keep 9 / 20; 0 exit-rule hits | -
- 11/04 | One-off MES 3m EMA grid | basis v10.68 | -
- 11/03 | One-offs (toward, TP1 by time, loser by hour) | basis v10.60 / v10.55 | -
