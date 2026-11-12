# Where the replay studies keep CBC settings (11/08/2026)

The scheduled studies replay history with settings HARD-CODED in these project scripts; they do NOT read the Pine file.
The daily "CBC settings sync check" compares them with the newest `pine/CBC_v*.pine` (via `claude/cbc_settings.py` -> `claude/CBC_SETTINGS.md`).

| Script constant | Chart | Live CBC input(s) it must match | Notes |
|---|---|---|---|
| `mes3_ema_grid.py` `LIVE` = dict(sl, mn, cap, tp, tcap, part, be, tr) | MES 3m | sl = ats_slx_sym "MES 3m x"; mn = ats_msl_sym / ats_min_sl MES; cap = ats_cap_txt "MES 3m 0" (0 -> 1e9); tp = ats_tp1_sym "MES 3m x"; tcap = ats_tpc_txt "MES 3m 0" (0 -> 1e9); part = 'tod' when ats_pw_sym has MES 3m windows (80 % inside, ats_part_sym "MES 3m 100" outside); be = ats_be_on / ats_be_sym; tr = ats_trl_sym "MES 3m x" else ats_trail_m0 | used by almost every MES 3m study |
| `mes3_ema_grid.py` `BASEX` | MES / MGC 5m, 2m "base exits" | ats_atr_m1, ats_min_sl, ats_cap_txt, ats_atr_t1, ats_tpc_txt, ats_part_pct, ats_trail_m0 | per-symbol caps: MES 8 / 6, MGC 7 / 6 |
| `late_study.py` `MGCX` | MGC 3m (and MGC 2m / 5m base) | sl ats_atr_m1, mn MGC min SL, cap MGC 7, tp ats_atr_t1, tcap MGC 6, part = ats_part_sym "MGC 3m x" else ats_part_pct, tr = ats_trl_sym "MGC 3m x" else ats_trail_m0 | INTENTIONAL: runner_study.py / weekly Study E use MGCX 80 % / 1.7 as the comparison base for the v10.84 change (50 % / 3.5). MGC 3m live since v10.84 = 50 % / trail 3.5. |
| `late_study.py` `MESX` | MES 2m / 5m base | as BASEX | |
| `chop_sim.py` `EXIT[(sym, tf)]` | MGC 3m, MES 3m, MGC 2m, MES 2m | as above | 11/08: updated to live -- MES 3m = LIVE (3 / 1.75 / 'tod'), MGC 3m = v10.84 live (50 % at TP1, trail 3.5). Case.sim1 now honours `tcap` and part='tod'. Used by scripts that call `s.run(...)` WITHOUT `q=`. |
| `chop_sim.py` `GATE` | 3m / 2m gates | ats_rp_sym (R5 = range gate: MGC 3m, MES 3m, MGC 2m since v10.77), ats_f_ext_sym (X4 = MGC 3m stretch 4), ats_mtg_sym (MTF = MES 2m 1) | 11/08: MGC 2m R5=1. Also hard-coded in filter_sweep.py LIVE, orf_study.py CHARTS, mgc2_study.py P0, late_study.py CHARTS2 |
| `botwin.py` `inwin` | MES 3m bot | bot_win | v10.87: 1830-2200, 0300-1300, 1500-1530 |
| `botwin.py` / `bot_tp.py` short filter | MES 3m bot | bot_d5 | ON since v10.86 |
| `CH` / `SET` dicts in sltime_study, combo_study, exit_lab, trend_guard_study, runner_study, all_combo, study5 | per study | import LIVE / MGCX / MESX (see above) | MNQ / M2K 3m use CBC defaults written inline |
| `mes3_ema_grid.py` slow EMA (section A) | MES 3m | ema_s_sym (MES 3m entry) else 20; ema_f_sym | MES 2m slow 14 (ema_s_sym "MES 2m 14") |
| `chop_sim.cur_rule` thr 0.23 | all | "Block in chop: Efficiency Ratio below" | |
| flip-timing gate | MES 3m | ats_fw_sym / ats_fw2_sym ("MES 3m 8" in the "to" list, "from" list empty = off) | not modelled in the replay |
