# CBC settings sync -- 2026-11-12 09:45 ET (manual re-run for the failed 11/11 run; same result as 09:44)

Newest Pine: **pine/CBC_v10_87.pine** (indicator "v10.87"). Previous snapshot (claude/CBC_SETTINGS_prev.md): v10.87.

Result: **no input changes; every mapped script constant MATCHES.** 1 known difference. No action needed.

## A. Input changes since the last snapshot

- Version: v10.87 -> v10.87 (unchanged; pine/CBC_v10_87.pine still the newest file, uploaded 11/08 15:48 UTC, not replaced since).
- Changed defaults: none. New inputs: none. Removed inputs: none (192 ats_ / bot_ / xr_ / ema_ inputs, same as the last snapshot).
- Cosmetic (unchanged): the "Latest changelog entries" block lists v10.00-v10.07 (regex takes the first 8 in file order).

## B. Script constants vs v10.87 defaults

Scripts checked (project copies): mes3_ema_grid.py (11/04), late_study.py (11/07), chop_sim.py (10/24 upload, EXIT/GATE already carry the 11/08 live values), botwin.py (11/08). None changed since the last run.

### mes3_ema_grid.py `LIVE` (MES 3m) -- all MATCH
| Field | Script | Pine v10.87 | |
|---|---|---|---|
| sl | 3.0 | ats_slx_sym "MES 3m 3" | MATCH |
| mn | 5 | ats_min_sl "MES 5", ats_msl_sym "" | MATCH |
| cap | 1e9 | ats_cap_txt "MES 3m 0" (0 = none) | MATCH |
| tp | 1.75 | ats_tp1_sym "MES 3m 1.75" | MATCH |
| tcap | 1e9 | ats_tpc_txt "MES 3m 0" | MATCH |
| part | 'tod' (80 % 06:00-16:00 / 18:00-22:30, else 100 %) | ats_pw_sym "MES 3m 0600-1600 80, MES 3m 1800-2230 80", ats_part_sym "MES 3m 100" | MATCH |
| be | True | ats_be_on true, ats_be_sym "" | MATCH |
| tr | 1.7 | no MES 3m in ats_trl_sym -> ats_trail_m0 1.7 | MATCH |

### mes3_ema_grid.py `BASEX` -- MATCH
sl 1.7 = ats_atr_m1; mn 5 = MES 5; cap 8 = MES 8; tp 1.7 = ats_atr_t1; tcap 6 = MES 6; part 0.8 = ats_part_pct 80; be True; tr 1.7 = ats_trail_m0.

### late_study.py
- `MGCX`: sl 1.7, mn 5, cap 7, tp 1.7, tcap 6, be True -> MATCH; part 0.8 / tr 1.7 vs MGC 3m live 50 % / trail 3.5 -> **known** (runner-study comparison base since v10.84). For MGC 2m / 5m base: MATCH.
- `MESX`: = BASEX -> MATCH.
- `CHARTS` MES 3m rows use `dict(m.LIVE)` -> MATCH. `CHARTS2` MGC 2m `R5=1` vs ats_rp_sym "MGC 2m 5" -> MATCH; MES 2m `MTF=1` vs ats_mtg_sym "MES 2m 1" -> MATCH.

### chop_sim.py `EXIT`
- (MGC,3): sl 1.7 / mn 5 / cap 7 / tp 1.7 / tcap 6 / part 0.5 / be / tr 3.5 vs ats_part_sym "MGC 3m 50", ats_trl_sym "MGC 3m 3.5" -> MATCH.
- (MES,3): sl 3.0 / tp 1.75 / no caps / 'tod' / tr 1.7 = LIVE -> MATCH.
- (MGC,2): sl 1.7, mn 5, tp 1.7, part 0.8, be, tr 1.7, cap 7, tcap 6 (sim1 default) -> MATCH.
- (MES,2): same with cap 8 / tcap 6 -> MATCH.

### chop_sim.py `GATE`
- (MGC,3) R5=1, X4=1 -> ats_rp_sym "MGC 3m 5", ats_f_ext_sym "MGC 3m 4" -> MATCH.
- (MES,3) R5=1 -> "MES 3m 5" -> MATCH.
- (MGC,2) R5=1 -> "MGC 2m 5" -> MATCH.
- (MES,2) MTF=1, R5=0 -> ats_mtg_sym "MES 2m 1", MES 2m not in ats_rp_sym -> MATCH.
- `cur_rule` thr 0.23 = ats_c_er 0.23 (flip ER 0.23 = ats_fer) -> MATCH.
- Not modelled (info, unchanged): ats_fl2_sym "MGC 2m 1", ats_fw2_sym "MES 3m 8", ats_fa_sym "MES 2m 9", xr_cut / xr_lock exit rules.

### botwin.py
- `inwin`: candle close 18:30-22:00, 03:00-13:00, 15:00-15:30 ET vs bot_win "1830-2200, 0300-1300, 1500-1530" -> MATCH.
- Short filter rows ('d5','S') model bot_d5 = true -> MATCH.

### Count
14 MATCH (LIVE, BASEX, MGCX non-runner fields, MESX, EXIT x4, GATE x4, inwin, bot_d5), 0 MISMATCH, 1 known (MGCX part / trail).

## C. Affected scripts / studies

None -- no mismatches, no fixes needed.
Not re-checked this run (outside the mapped files): other range-gate copies (mgc2_study.py P0, orf_study.py CHARTS, filter_sweep.py LIVE).

### Known (no action)
- late_study.py MGCX part 0.8 / tr 1.7 vs MGC 3m 50 % / trail 3.5 (runner study comparison base).
