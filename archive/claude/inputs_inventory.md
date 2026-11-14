# ① ② ③ input inventory -- CBC EMA Slope v1.09 -- 11/14/2026

Every input in ① Auto Trade Setup (101), ② Setup Triggers (15), ③ Trade Setup Filters (52). "Effect" = what it does for setups / results; "Status" = where it was tested and the verdict (reports in claude/). Full numbers for the newest sweep: claude/all_report.md, claude/all_nb_report.md.

## ① Auto Trade Setup

| Input | Default | Effect | Status |
|---|---|---|---|
| TP1 step (+1 farther / -1 closer) (`ats_tp1_handle`) | 0.0 | pivot-level step (only with pivot TP/SL) | n/a: ATR method live |
| SL1 step (+1 farther / -1 closer) (`ats_sl1_handle`) | 0.0 | same | n/a |
| TP2 step (+1 farther / -1 closer) (`ats_tp2_handle`) | 0.0 | same | n/a |
| SL2 step (+1 farther / -1 closer) (`ats_sl2_handle`) | 0.0 | same | n/a |
| Auto-Draw Trade Setup (Entry/Stop/Target) (`auto_trade_setup_enabled`) | true | master switch | keep ON |
| Include 'toward' HTF flips (`ats_allow_toward`) | false | toward flips | toward_study 11/03 -> keep OFF |
|   ↳ toward flip: allow setups once a candle closes on the away side by (pts) (`ats_tw_late`) | true | late-away (global 1 pt) | all_study: MGC live uses it, strict vs 1 pt = noise |
| (value) (`ats_tw_pts`) | 1.0 | same | same |
|      ...per symbol/timeframe (pts; 0 = off) (`ats_tw_sym`) | "MNQ 3m 0, MES 3m 0, M2K 3m 0" | per chart late-away | M2K 0 (m2k study); MES / MNQ 0 |
| HTF CBC flip: skip setup if close is farther than (`ats_fd_mode`) | "x ATR from 3m EMA20" | flip distance | ats_inputs: keep |
| (value) (`ats_fd_x`) | 2.0 | flip distance 2 ATR | ats_inputs: 1.5/2.5/3/off worse (MGC 3/off robustly worse) |
|    ...or at least (pts) per symbol (`ats_fd_pts`) | "MGC 10, MES 8, MCL 0.3, BTC 300, MNQ 50" | flip distance floor | ats_inputs + all_study: MGC 10 = noise |
| HTF CBC flip: long only if close is above VWAP and EMA200 by (pts) (mirror for short) (`ats_fva_on`) | true | flip side gate | ats_inputs: inert / noise |
| (value) (`ats_fva_x`) | 1.0 | same | 0/2 pts noise |
| HTF CBC flip: skip the flip setup when the flip is a flop (EMA200 / VWAP) (`ats_flg`) | false | flop skip (flip) | ats_inputs: noise -> keep OFF |
|   ...also skip NON-flip setups while the HTF flip is a flop, per symbol/timeframe (`ats_fl2_sym`) | "MGC 2m 1" | flop skip (non-flip), MGC 2m | ats_inputs: MGC 3m ON -871 -> keep off on 3m |
| HTF CBC flip: minimum Efficiency Ratio (0 = off) (`ats_fer`) | 0.23 | flip min ER | ats_inputs / all_study: 0 / 0.15 / 0.30 noise or worse |
| Minimum ER: LTF EMA20 Pierce (`ats_erl`) | 0.08 | LTF pierce min ER (global) | ats_inputs |
| HTF EMA9 (`ats_er9`) | 0.15 | HTF pierce min ER | ats_inputs: 0 / 0.23 noise / worse |
| HTF EMA20 (`ats_er20`) | 0.15 | same | same |
|    ...LTF EMA20 Pierce min ER per symbol/timeframe (overrides; 0 = off) (`ats_erl_sym`) | "MES 3m 0.15, MNQ 3m 0.15, M2K 3m 0.23" | per chart LTF min ER | MES 0.15 (v1.06), MNQ 0.15 (v1.08), M2K 0.23 (v1.09) |
| HTF CBC flip: EMA200 slope must agree (rising for long / falling for short) (`ats_e2s`) | false | flip EMA200 slope | ats_inputs: inert |
| HTF CBC flip: VWAP slope must agree (rising for long / falling for short) (`ats_vws`) | true | flip VWAP slope | ats_inputs: OFF worse (MGC -33) |
| Skip setups against the MTF (60m) CBC direction (`ats_mtg`) | false | MTF 60m gate | ats_inputs + MTF check: ON worse on MES / MGC / MNQ -> keep OFF |
|    ...per symbol/timeframe (1 = skip, 0 = allow) (`ats_mtg_sym`) | "MES 2m 1" | MES 2m only | not studied here (2m) |
| Skip setups when HTF EMA slope is against the trade / min slope (pts) (`ats_h20s_on`) | "Off" | HTF EMA slope against gate | ats_inputs: noise / worse -> keep Off (slope filter covers it) |
| (value) (`ats_hsl_min`) | 0.0 | same | same |
| VWAP reclaim blocks setups for (bars) (`ats_vw_blk_on`) | true | VWAP reclaim block | ats_inputs: OFF / 3 / 8 noise |
| (value) (`ats_vw_blk_n`) | 5 | same | keep 5 |
| Pivot reclaim (R1-R3 / S1-S3) blocks setups (same bars) (`ats_pv_blk_on`) | true | pivot reclaim block | not replayable (R2/R3 not in bar feed) |
| Require price past both EMA clouds (`ats_req_clear`) | false | price past both clouds | ats_inputs: MES noise, MGC robustly worse -> keep OFF |
| ...also close beyond the HTF EMA9 (`ats_req_htf9`) | false | same | same |
| ...also close beyond the HTF EMA20 (`ats_req_htf20`) | false | same | same |
| Alert: new Trade Setup (`ats_alert_on`) | true | display / alert only |  |
| Reward zone (`col_trade_setup_reward`) | color.new(#22C55E | display / alert only |  |
| Risk zone (`col_trade_setup_risk`) | color.new(#EF4444 | display / alert only |  |
| Stop level (`ats_stop_level_pick`) | "Automatic (nearest)" | only with pivot SL | n/a |
| Target level (`ats_target_level_pick`) | "Automatic (nearest)" | only with pivot TP | n/a |
| Show TP2 (`auto_trade_setup_show_tp2`) | false | display / alert only |  |
| Flash a border around a new setup for its first (`ats_fl_on`) | true | display / alert only |  |
| candles (`ats_fl_n`) | 2 | display / alert only |  |
| (value) (`ats_fl_col`) | #FFD600 | display / alert only |  |
| Show SL2 (`auto_trade_setup_show_sl2`) | false | display / alert only |  |
| Reward zone 2 (TP1→TP2) (`col_trade_setup_reward2`) | color.new(#22C55E | display / alert only |  |
| Risk zone 2 (SL1→SL2) (`col_trade_setup_risk2`) | color.new(#EF4444 | display / alert only |  |
| SL2 level (`ats_stop2_level_pick`) | "Automatic (nearest)" | SL2 (display) | n/a |
| TP2 level (`ats_target2_level_pick`) | "Automatic (nearest)" | TP2 (display) | n/a |
| Keep previous setup when a new one fires (`ats_keep_old`) | true | display / alert only |  |
| Skip a new setup while the last same-direction setup is still running (`ats_one_on`) | true | skip same-direction while running | ats_inputs: OFF worse -> keep ON |
| Erase older setups, keep this many back (`ats_kn_on`) | true | display / alert only |  |
| (value) (`ats_kn`) | 50 | display / alert only |  |
| Use Lux-style Order Blocks as TP/SL levels (`ats_use_ob2`) | false | OB levels as TP/SL (pivot method only) | n/a |
| Minimum SL distance (pts) per symbol (`ats_min_sl_on`) | true | min SL | all_study: x0.6 / x1.4 noise or worse (MGC x0.6 -117) |
| (value) (`ats_min_sl`) | "MGC 5, MES 5, MNQ 25, M2K 3, MCL 0.3, BTC 300" | same | same |
|    ...minimum SL per symbol/timeframe (overrides; 0 = no minimum) (`ats_msl_sym`) | "" | same, per chart | empty |
| SL method: 3m ATR (instead of pivots) (`ats_atr_sl_on`) | true | SL method ATR | keep ON (all studies ATR) |
| SL1 placement (`ats_slm`) | "ATR / pivots (above)" | SL1 placement | keep ATR / pivots (alt modes not studied on branch) |
| ATR length / SL1 x / SL2 x (`ats_atr_len`) | 14 | ATR length | ats_inputs: 14 best; chart shows 15 (MES -77) -> set 14 |
| (value) (`ats_atr_m1`) | 1.7 | SL1 x ATR (global 1.7) | all_study: 1.5-3.5 all worse or noise on MGC / MNQ / M2K |
| (value) (`ats_atr_m2`) | 3.0 | SL2 (display) | n/a |
|    ...SL1 x ATR per symbol/timeframe (overrides) (`ats_slx_sym`) | "MES 3m 3" | per chart SL1 x (MES 3) | all_study: MES 1.5-3.5 -> 3 best |
| Time stop: candles per symbol/timeframe (0 = off) (`ats_ts_sym`) | "" | time stop | all_study: 10 / 20 candles worse or noise -> keep off |
|    ↳ time stop: minimum progress (x ATR) (`ats_ts_x`) | 0.5 | same | same |
| TP method: 3m ATR (instead of pivots) (`ats_atr_tp_on`) | true | TP method ATR | keep ON |
| TP1 x / TP2 x (`ats_atr_t1`) | 1.7 | TP1 x ATR (global 1.7) | all_study: 1.25-2.5 noise / worse |
| (value) (`ats_atr_t2`) | 3.0 | TP2 (display) | n/a |
| Trail SL1 after TP1 hit: x ATR (`ats_trail_on`) | true | trail after TP1 | all_study: 1.3 / 1.7 / 2.5 / 3.5 / none -- M2K keep 1.7; MES / MGC / MNQ no runner |
| (value) (`ats_trail_m0`) | 1.7 | same | same |
| HTF CBC Flip setups: no TP1 -- ride until the HTF CBC flips back / SL1 / 16:00 (per symbol (`ats_fx_sym`) | "MES 3m 1" | flip ride (MES 3m 1) | all_study: MES OFF -383 (robustly worse); ON worse for MGC / MNQ / M2K |
|    ...trail x ATR per symbol/timeframe (overrides) (`ats_trl_sym`) | "MGC 3m 0, MNQ 3m 0" | per chart trail | MGC / MNQ 0 (FLIP 0 %) |
|   ↳ trail from the high / low (moves live) (`ats_trail_hl`) | false | trail from high/low | not studied (only with a runner) |
| Close at TP1 (%) (`ats_part_pct`) | 80 | close at TP1 global 80 % | all_study: M2K 0 % promising (+52) / 25-50 % noise |
| Move remainder to breakeven at TP1 (`ats_be_on`) | true | breakeven at TP1 | all_study: OFF worse / noise |
| TP1 x ATR per symbol/timeframe (overrides) (`ats_tp1_sym`) | "MES 3m 1.75" | per chart TP1 (MES 1.75) | all_study: MES 1.25-2.5 -> 1.75 best |
|    ...close at TP1 (%) per symbol/timeframe (`ats_part_sym`) | "MES 3m 100, MGC 3m 0, MNQ 3m 0" | per chart close % | MES 100, MGC 0, MNQ 0 confirmed best |
|    ...breakeven at TP1 per symbol/timeframe (1 = on, 0 = off) (`ats_be_sym`) | "" | per chart BE | empty |
|    ...close at TP1 (%) by time of day, per symbol/timeframe (`ats_pw_sym`) | "" | close % by time of day | empty (v10.95) |
| Alert: TP1 partial (`ats_part_alert`) | true | display / alert only |  |
| Show exit markers (SL / trail / TP2 / HTF flip / 17:00 / replaced) (`ats_sl_lbl`) | true | display / alert only |  |
|   ↳ exit markers as lettered bubbles off the candles (OFF = text labels) (`ats_ex_tiny`) | true | display / alert only |  |
| label transp. % (`ats_ex_tr`) | 25 | display / alert only |  |
| Finished setup fill opacity (%) (`ats_done_op`) | 10 | display / alert only |  |
| Max ATR SL1 (pts) per symbol (`ats_cap_on`) | true | Max SL1 cap | all_study: MNQ cap 30 -> 60 / off +1068 promising (plateau 60-off); M2K 5 -> 8 / off +23 robust; MES n/a (0); MGC off +54 noise |
| (value) (`ats_cap_txt`) | "MES 3m 0, MGC 7, MES 8, MNQ 30, M2K 5, MCL 0.3, BTC 500" | same | same |
| Max ATR TP1 (pts) per symbol (`ats_tpc_on`) | true | Max TP1 cap | all_study: off = noise everywhere |
| (value) (`ats_tpc_txt`) | "MES 3m 0, MGC 6, MES 6, MNQ 40, M2K 3, MCL 0.3, BTC 300" | same | same |
| Show ⓘ setup info label (hover: trigger, CBC 3m/15m) (`ats_info_on`) | true | display / alert only |  |
| Keep only the last N chart markers (0 = all) (`mk_n`) | 200 | display / alert only |  |
| Setups: act on HTF flip at the HTF candle close (`ats_hc_on`) | true | act on flip at HTF close | not replayable (replay = ON) |
| Setups use closed 15m values only (no look-ahead) (`ats_cv_on`) | false | closed 15m values only | not replayable (look-ahead mode) |
| Min candles between setups (`ats_cd_bars`) | 10 | min candles between setups | ats_inputs: 5-20 noise -> keep 10 |
| No new setups between (ET) (`ats_q_on`) | true | no new setups 16:00-18:45 | time_blocks: MES 16:00-19:00 +45 promising (chart input, open) |
| (value) (`ats_q_win`) | "1600-1845" | same | same |
|    ...also no new setups per symbol/timeframe (ET, HHMM-HHMM) (`ats_qs_sym`) | "MES 3m 1300-1500" | per chart extra windows | MES 13:00-15:00 (v1.07); MGC blocks noise |
| No new setups during opening range (forming):  NY (`ats_orb_f`) | true | OR forming NY | time_blocks: keep |
| London (`ats_orb_f_ln`) | true | OR forming London | keep |
| Asia (`ats_orb_f_as`) | true | OR forming Asia | keep |
| No new setups inside opening range (after set):  NY (`ats_orb_in`) | false | inside OR after set NY | time_blocks: keep OFF |
| London (`ats_orb_in_ln`) | false | London | keep OFF |
| Asia (`ats_orb_in_as`) | false | Asia | keep OFF (MGC -421) |
| End setups at 16:00 ET (`ats_eod_end`) | true | end at 16:00 | time_blocks: MES OFF +74 promising (open); MGC worse |

## ② Setup Triggers

| Input | Default | Effect | Status |
|---|---|---|---|
| Trigger: LTF EMA20 Pierce (`auto_trade_setup_on_ltf_pierce`) | true | trigger | trig_inputs: OFF worse on MGC / MNQ -> keep |
| LTF pierce late-confirm window (bars) (`ats_ltf_late_bars`) | 1 | trigger | late_study + trig_inputs: keep 1 (MES 2 promising, watch) |
| Trigger: LTF EMA20 Touch (draws mid-candle) (`auto_trade_setup_on_ltf_touch`) | true | trigger (mid-candle) | not replayable (live only) |
| Trigger: HTF CBC Flip (confirmed) (`auto_trade_setup_on_htf_flip`) | true | trigger | trig_inputs: keep (MES OFF -341) |
| HTF CBC Flip: require a pullback first (`ats_flip_wait_on`) | false | flip pullback wait | trig_inputs: ON robustly worse MES (-418) -> keep OFF |
| HTF CBC Flip: wait for pullback (bars, 0 = enter at the flip) (`ats_flip_win_in`) | 10 | only with wait ON | tested 5/10/20 -> n/a |
| HTF CBC Flip: touch and close-back may be on separate candles (`ats_flip_two_step`) | true | only with wait ON | tested -> n/a |
| Trigger: HTF EMA9 Pierce (`auto_trade_setup_on_htf_ema9`) | true | trigger | trig_inputs: keep |
| Trigger: HTF EMA20 Pierce (`auto_trade_setup_on_htf_ema20`) | true | trigger | trig_inputs: keep |
| HTF EMA9/EMA20 Pierce replaces the current setup (`ats_hs_on`) | false | HTF pierces skip cooldown | trig_inputs: noise -> keep OFF |
| HTF pierce late-confirm window (bars) (`ats_htf_late_bars`) | 1 | trigger | trig_inputs: 0/2/3 noise -> keep 1 |
| HTF pierce late confirm: trade-color candle (`ats_htf_late_color`) | true | trigger | trig_inputs: noise -> keep ON |
| HTF pierce: also require close beyond LTF EMA9/20 (`ats_htf_req_ltf`) | false | inert unless "Require price past both EMA clouds" ON | trig_inputs: intended rule noise / worse -> keep OFF |
| Trigger: Momentum break (no pullback) (`auto_trade_setup_on_momo`) | true | trigger | not replayable (live only) |
| Trigger: HTF Pullback - Structure Confirmed (`auto_trade_setup_on_htf_pullback`) | true | trigger | not replayable (needs HTF structure) |

## ③ Trade Setup Filters

| Input | Default | Effect | Status |
|---|---|---|---|
| Block in chop: Choppiness Index above (`ats_f_chop_on`) | false | CHOP block | all_study: noise / worse |
| (value) (`ats_f_chop_max`) | 61.8 | same | same |
| Chop filters length (bars) (`ats_f_chop_len`) | 12 | length 12 for chop filters | not varied (filters off) |
| Block in chop: ADX below (`ats_c_adx_on`) | false | ADX block | all_study: noise / worse (M2K < 20 robustly worse) |
| (value) (`ats_c_adx`) | 20.0 | same | same |
| Block in chop: Efficiency Ratio below (`ats_c_er_on`) | true | ER chop filter | all_study: OFF / 0.18-0.30 noise or worse -> keep 0.23 |
| (value) (`ats_c_er`) | 0.23 | same | same |
|   ↳ except a breakout: close through the last swing high/low or an opening-range high/low  (`ats_er_bo`) | true | breakout exception | all_study + orpa: OFF worse (MNQ -2321) -> keep ON |
| (value) (`ats_er_bn`) | 3 | breakout window 3 | orpa: 1 / 2 / 5 worse -> keep 3 |
|     ↳ skip the breakout candle itself (only the next candles) (`ats_er_bs`) | false | skip breakout candle | not re-tested on branch (breakout_flip earlier: no) |
|   ↳ colour candles by Efficiency Ratio band (ER 0.23 and below) (`ats_er_bg`) | false | display / alert only |  |
| Block in chop: EMA20 / VWAP crosses >= (`ats_c_x_on`) | false | crosses block | all_study: noise / worse |
| (value) (`ats_c_x`) | 4 | same | same |
| Block in chop: HTF EMA20 slope below (x ATR) (`ats_c_sl_on`) | false | slope filter (global) | per chart list used instead |
| (value) (`ats_c_sl`) | 0.3 | same | same |
| ...HTF EMA20 slope x ATR per symbol/timeframe (overrides; 0 = off) (`ats_c_sl_sym`) | "MES 3m 0.42, MGC 3m 0.3, MNQ 3m 0.75, M2K 3m 0.48" | per chart slope | slope_grid / mnq / m2k: MES 0.42, MGC 0.3, MNQ 0.75, M2K 0.48 |
| Block in chop: N-bar range below (x ATR) (`ats_c_rg_on`) | false | N-bar range block | all_study: noise / worse (MNQ < 3 robustly worse) |
| (value) (`ats_c_rg`) | 2.0 | same | same |
| Block in chop: mixed chart structure (LH + HL or HH + LL) (`ats_c_st_on`) | false | mixed structure block | not modelled |
| Block when stretched from VWAP: more than (x ATR) (`ats_f_ext_on`) | false | VWAP stretch (global) | per chart list |
| (value) (`ats_f_ext_max`) | 3.0 | same | same |
|    ...stretch x ATR per symbol (overrides; 0 = off) (`ats_f_ext_sym`) | "MGC 3m 4, M2K 3m 4" | per chart stretch | all_study: MGC 4 keep; M2K 4 (OFF robustly worse); MNQ ON robustly worse |
| Skip when in the top / bottom % of a tight N-bar range (`ats_rp_on`) | false | range gate (global) | per chart list |
|   ↳ N bars / zone % / range under (x ATR) (`ats_rp_n`) | 24 | range gate 24 bars | not varied |
| (value) (`ats_rp_z`) | 20.0 | zone 20 % | all_study: MGC 30 % noise |
| (value) (`ats_rp_x`) | 5.0 | range under 5 ATR | all_study: MES 6 robustly worse; MGC 4 promising (+169) but neighbours noise -> watch |
|    ...range under x ATR per symbol (overrides; 0 = off) (`ats_rp_sym`) | "MGC 3m 5, MGC 2m 5, MES 3m 5" | per chart range gate | keep MES / MGC 5; ON for MNQ / M2K noise or worse |
|    ...zone % per symbol (overrides) (`ats_rpz_sym`) | "" | per chart zone % | empty |
| Skip setup if the first opposing level / OB is within x × TP1 (per symbol/timeframe) (`ats_rm_sym`) | "" | room filter | room_study: keep OFF |
| TP1 just before the first opposing level when it is nearer than TP1 (`ats_rm_tp`) | false | TP1 before first level | room_study: keep OFF |
| min x ATR (`ats_rm_min`) | 0.5 | same | same |
| Show blocked setups (shadow) + \"Setup Blocked\" alert (`ats_sh_on`) | true | shadow setups (display + alerts; not traded) | no effect on results |
| keep (`ats_sh_n`) | 20 | display / alert only |  |
| Block after frequent HTF flips: flips >= (`ats_f_flip_on`) | false | flip-count block | all_study: 2 / 3 / 4 worse (MGC robustly) |
| (value) (`ats_f_flip_n`) | 2 | same | same |
|    ...flips >= per symbol (overrides; 0 = off) (`ats_f_flip_sym`) | "MES 2m 4" | MES 2m 4 | 2m only |
| Skip new setups from x HTF candles after the HTF CBC flip, per symbol/timeframe (`ats_fa_sym`) | "MES 2m 9" | skip all setups x HTF candles after flip (MES 2m 9) | all_study: 6 / 9 / 12 noise or worse on 3m |
| Skip NON-flip setups from x HTF candles after the HTF CBC flip, per symbol/timeframe (`ats_fw_sym`) | "" | skip non-flip setups from x ... (empty = off) | flip_timing: C-002 MES 3m 5-8 open |
|    ...to y HTF candles (last one blocked), per symbol/timeframe (`ats_fw2_sym`) | "MES 3m 8" | ... to y (MES 3m 8) | inert while ats_fw_sym empty |
| in last HTF candles (`ats_f_flip_win`) | 8 | flip-count window 8 | same |
| Block if VWAP from -pts / +pts (`ats_nv_on`) | false | VWAP -3/+2 block | all_study: noise / worse |
| (value) (`ats_nv`) | 3.0 | same | same |
| (value) (`ats_nv2`) | 2.0 | same | same |
|   ↳ unless the whole candle is beyond VWAP by (pts) (`ats_nv_w`) | 1.0 | same | same |
| Block if EMA200 from -pts / +pts (`ats_ne_on`) | false | EMA200 -3/+2 block | all_study: noise / worse |
| (value) (`ats_ne`) | 3.0 | same | same |
| (value) (`ats_ne2`) | 2.0 | same | same |
| Environment: long only when EMA200 > VWAP, short only when EMA200 < VWAP (`ats_env_on`) | false | EMA200 vs VWAP | all_study: worse (MGC robustly) |
| Skip if the Max ATR SL1 cap is below x ATR (`ats_vc_on`) | false | skip if SL cap < 1.5 ATR | all_study: robustly worse MGC / MNQ |
| (value) (`ats_vc_x`) | 1.5 | same | same |
| Skip while ATR is above x times ATR(100) (`ats_va_on`) | false | skip high ATR | all_study: noise / worse |
| (value) (`ats_va_x`) | 1.8 | same | same |
