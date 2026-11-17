# CBC EMA Slope branch -- handoff (11/15/2026)

Branch of CBC v10.97 (main line stays v10.97 for separate analysis). Current file: pine/CBC_EMASlope_v1_22.pine ("CBC EMA Slope v1.22", short "CBC-ES 1.22"). Library: pine/ESLib3_v9.pine (published as ESLib3/9, confirmed 11/14). Main line v10.97 imports ESLib3/8 -> keep pine/ESLib3_v8.pine too.

## Rules
- Every revision: bump the version in the indicator name, short title, file name and a changelog line together (v1.23, v1.24 ...). Main line, if changed: v10.98 ...
- Keep only the newest branch file in the project. Before deleting, give the user a verified archive (zip + SHA256SUMS) and wait for their OK. Keep key files: libraries (ESLib*.pine), studies (claude/*), main line v10.97, current branch file (user, 11/14). User keeps the archives in GitHub.
- Tooltips: the user wants every input tooltip kept (v1.20 removed them, v1.21 restored them). Texts also in claude/tooltips_v1_19.md.
- Deleted after user archived them: CBC_EMASlope v1.04-v1.07, v1.10-v1.15, v1.17-v1.20, CBC_v10_96; 11/15 17 old October studies (stop_sweep, breakout_flip, ob_setup, alert_param, room_study, sl_reversal, flip_timing, evening_study / evening_session_report, pullback_report). v1.08 / v1.09 / v1.16 / v1.21 never stored in the project (in the cbc_archive_* zips). Study scripts not in the project are in the zips: v1.12-v1.13 (2m), v1.15-v1.17 (slope lookback / MTF / 4h), v1.17-v1.18 (all_eng117.py, all3v_study.py, mgc3_nb.py, nb3.py).
- Don't run the branch and v10.97 with alerts on the same chart / bot (alerts don't say which indicator sent them).

## What the branch has (vs v10.97) -- all per symbol/timeframe lists, inputs only unless noted
| Item | MES 3m | MGC 3m | MNQ 3m | M2K 3m | MES 5m | MGC 5m | MNQ 5m | M2K 5m | MES 2m | MGC 2m | MNQ 2m | M2K 2m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ③ HTF EMA20 slope x ATR (ats_c_sl_sym) | 0.42 | 0.165 | 0.75 | 0.48 | 0.19 | 0.13 | 0.15 | 0.25 | 0.75 | 0.14 | 0.55 | 0.3 |
| ③ Slope lookback, chart bars (ats_slk_sym, v1.17 code) | 12 | 5 (15 min) | 12 | 12 | 3 (15 min) | 3 | 3 | 3 | 12 | 4 (8 min) | 12 | 4 |
| ① LTF EMA20 Pierce min ER (ats_erl_sym, v1.06 code) | 0.15 | box | 0.15 | 0.23 | box | box | box | box | box | box | box | 0.2 |
| ① Flip ride (ats_fx_sym, v1.00 code) | 1 | - | - | - | - | - | - | - | - | - | - | - |
| ① SL1 x ATR (ats_slx_sym) | 3 | 1.7 | 1.7 | 3.5 | 1.7 | 1.7 | 1.7 | 1.7 | 1.7 | 1.7 | 1.7 | 1.7 |
| ① Close at TP1 % / trail | 100 % | 0 % / 0 | 0 % / 0 | 0 % / 1.7 | 80 % / 1.7 | 80 % / 1.7 | 80 % / 1.7 | 50 % / 1.7 | 80 % / 1.7 | 80 % / 1.7 | 0 % / 0 | 80 % / 1.7 |
| ① Extra no-new-setup windows (ats_qs_sym, v1.07 code) | 1300-1500, 1845-1900 | - | - | - | - | - | - | - | - | - | - | - |
| ① End setups at 16:00 per chart (ats_eod_sym, v1.14 code) | 0 (off) | box | box | box | box | box | box | box | box | box | box | box |
| ① NY OR forming block per chart (ats_orbf_sym, v1.19 code) | box | box | 0 (off) | box | box | box | box | box | box | box | box | box |
| ③ VWAP stretch (ats_f_ext_sym) | - | 4 | - | 4 | 4 | - | 7 | - | - | - | - | - |
| ③ Range gate (ats_rp_sym) | 5 | 5 | - | - | - | - | - | - | - | 5 (pre-branch) | - | - |
| ① Toward late-away (ats_tw_sym) | 0 | 1 pt | 0 | 0 | 1 pt | 1 pt | 1 pt | 1 pt | 0 | 1 pt | 1 pt | 1 pt |
| ① Max ATR SL1 cap (ats_cap_txt) | 0 (none) | 7 | 60 | 8 | 8 | 10 | 30 | 8 | 0 (none) | 7 | 30 | 8 |
| ① MTF (60m) gate (ats_mtg_sym) | - | - | - | - | - | - | - | - | 0 (was 1) | - | - | - |
Pre-branch 2m entries kept: MES 2m flips >= 4 in 8, skip all new setups from 9 HTF candles after the flip, slow EMA 14, VWAP Bounce 4; MGC 2m range gate 5, flip-flop skip, VWAP Bounce.
Code notes: v1.17 slope gate in local f_slk() (|se20 - se20[k]| < threshold x ATR, k = ats_slk_sym else Chop filters length 12), not passed to ESLib f_ats_chop2 (whose length also drives ADX / ER / crosses / range); alert / tooltip "Slope" still shows the 12-bar slope. v1.19 NY OR forming block = f_sv(ats_orb_f, 1.0, ats_orbf_sym) > 0 in ats_g; tooltips removed from 5 branch inputs (ats_eod_sym / ats_erl_sym / ats_qs_sym / ats_c_sl_sym / ats_fx_sym). v1.22 token relief: default arguments dropped (", alert.freq_once_per_bar" x9, ", lookahead=barmerge.lookahead_off" x9, color.new(<opaque>, 0) x12).
Versions: v1.00-1.04 slope list + flip ride + compile fixes (ESLib3 v9); v1.05 MES 0.42; v1.06 LTF ER list; v1.07 MES 13-15 block; v1.08 MNQ 3m set; v1.09 M2K 3m set; v1.10 M2K cap 8; v1.11 5m set; v1.12 MNQ 5m stretch 7 + MGC 5m cap 10; v1.13 2m set; v1.14 MES 3m no new setups to 19:00 + End at 16:00 off; v1.15 CE10189 fix; v1.16 CE10117 token fix; v1.17 per-chart slope lookback + re-picked thresholds; v1.18 MGC 3m 15-min lookback 0.165 (PROMISING); v1.19 MNQ 3m cap 60 + NY OR block off, M2K 3m SL1 3.5 + 0 % at TP1; v1.20 all tooltips removed (reverted); v1.21 tooltips restored (= v1.19); v1.22 token fix with tooltips kept.

## Compile history
- v1.04 COMPILES (user, 11/14). v1.14 CE10189 -> fixed v1.15. v1.15 CE10117 100,287 -> v1.16. User reported 102,327 (v1.19), then 100,327 (taken as v1.21 = v1.19 code; the 102,327 was likely a typo). v1.22 NOT YET CONFIRMED (estimate ~99,860, ~400 under). The ~137 yellow CW10003 warnings are pre-existing and harmless. If CE10117 again: more default-argument cuts, or move f_bot_send / f_fire_alerts into ESLib3 v10 (needs a publish). Do not remove tooltips.

## Replay results (in-sample; vcmp2_report, mnq_report, m2k_report, five_report, all5_report, two_report, slk_report, all3v_report, mgc3_lk_watch, blk119_report)
| Chart | v10.97 trades / net (DD) | Branch v1.16 | v1.22 (= v1.19 logic) |
|---|---|---|---|
| MES 3m | 1787 / -834 (1074) | 739 / +809 (142) | same |
| MGC 3m | 1120 / +758 (216) | 800 / +1182 (166)* | 615 / +1782 (114) |
| MNQ 3m | 2007 / -2317 (2461) | 443 / +3944 (285) | 448 / +6455 (278) |
| M2K 3m | 2299 / -756 (783) | 365 / +110 (25) | 362 / +221 (47) |
| MES 5m | 1544 / -873 (877) | 228 / +248 (46) | 303 / +564 (40) |
| MGC 5m | 1576 / -238 (298) | 624 / +672 (94) | 576 / +1096 (55) |
| MNQ 5m | 1544 / +1428 (891) | 1484 / +2033 (777) | 516 / +4511 (181), last 4 wk negative |
| M2K 5m | 1459 / -364 (390) | 216 / +86 (36) | 346 / +265 (24) |
| MES 2m | 1322 / -490 (512) | 483 / +310 (41) | same |
| MGC 2m | 1789 / -74 (238) | 863 / +329 (93) | 791 / +737 (43) |
| MNQ 2m | 2179 / -2259 (3140) | 732 / +3566 (844) | same |
| M2K 2m | 1756 / -606 (606) | 198 / +33 (23) | 286 / +141 (14) |
3m / 5m Jan 5 - Nov 13; 2m Jun 1 - Nov 13. *MGC 3m with the live 1 pt late-away modelled (earlier replays used strict away: 627 / +1164 / 117). MNQ replay never validated vs live. M2K thin: chart only.

## Studies on the branch (reports in claude/)
- ema716 / mgc_x4, slope_grid, mnq_report, m2k_report, five_report, ats_inputs / trig_inputs / pbo / lcd / time_blocks / orpa / orsess / alerts_mnq / all_report + all_nb_report (3m sweep), all5_report (5m), two_report (2m). ① ② ③ covered on all 12 charts; inventory claude/inputs_inventory.md.
- mtf_report (11/15): 60m / 4h EMA20 slope combinations on MES / MGC 3m -- all worse.
- slk_report (11/15): slope lookback 5-60 min on all 12 charts -> v1.17 / v1.18.
- all3v_report (11/15): full ① ② ③ sweep on MES / MGC 3m (MES nothing; MGC 15-min lookback -> v1.18). MNQ / M2K 3m sweep + neighbours -> v1.19 (claude/mgc3_lk_watch.md).
- blk119_report (11/15): one-hour blocks + time windows + OR blocks on the v1.19 3m settings -- no new block promising; current blocks confirmed. Promising only: MGC 3m Asia OR block OFF (+164, z 1.4), M2K 3m NY OR block OFF (+46, z 1.7). Script claude/blk_watch.py (standalone, for the planned every-3-weeks Sunday task -- task NOT created yet: the approval was interrupted 11/15).
- Note: the biweekly opening-range task (orb_all_summary) found MNQ 3m Asia block right on older settings; v1.19 only turns the NY block off on MNQ 3m (London / Asia off alone were worse).

## Open items
- Load v1.22 on all 12 charts, confirm compile, recreate alerts (MNQ 3m, M2K 3m, MGC 3m changed); don't leave v10.97 alerts on the same charts / bot. MES 3m chart: ATR length back to 14; leave "End setups at 16:00" ON.
- Create the every-3-weeks Sunday ~2:35 pm ET time-block task (blk_watch.py) if the user still wants it.
- Weekly task "CBC 3m weekly watch: MGC slope lookback + MES / MNQ / M2K (Tuesdays)" 5:09 pm ET -> claude/mgc3_lk_watch.md / .py: revert checks for MGC 3m (v1.18) and MNQ / M2K 3m (v1.19); MES 3m re-check.
- Lookback candidates not implemented: M2K 3m 12 min, MES 2m 8 min (+190), MNQ 2m 10 min (+2434).
- Other candidates not implemented: MGC 3m Asia OR block off (+164); M2K 3m NY OR block off (+46); MGC 3m range gate off (+261 noise); MES 3m LTF late window 2; MNQ 2m HTF pierce min ER 0 (+974); MGC 2m 0 % at TP1 (+114); MES 2m block 06:00-07:00 (+44); MES 5m no new setups to 19:00 (+27). Ledger C-011 / C-012 not combined.
- Other scheduled watches still model v10.96/v10.97; once live, move baselines to the branch.
- Watches: Sunday volflip, Tuesday flipwin, Tuesday 3m watch, live vs replay on every chart.
