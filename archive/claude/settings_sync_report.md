# CBC settings sync -- 2026-11-13 16:47 ET

## Data notes (read before using live alerts or bars)

# Data notes for the live-alert studies (read with claude/settings_sync_report.md)

Updated 2026-11-12. Applies to every study that reads live alerts (/alerts) or BarFeed bars (/bars).

1. DUPLICATE ALERTS, 11/08 evening -> 11/12: MGC 2m, MGC 3m, MGC 5m and MCL 2m each had TWO CBC alerts in TradingView, so most
   of their alerts arrived twice within ~1 s (also a few on MGC 3m 10/19-10/20 and 11/03, MES 3m 11/03). Until the store is
   cleaned (GET https://tv-webhook-dashboard.onrender.com/health -> duplicates.lastDedupe.applied = true), treat alerts with the same chart ("Chart:" line), the same "Time:" line and
   the same set of "•" alert names received within 60 s as ONE alert (keep the longest text). Server v14 drops such
   near copies on arrival once it is deployed (/health serverVersion 14).
2. MGC 3m, 11/08 evening -> until the old alert was deleted (11/12): the second MGC 3m alert ran OLD exits (80 % at TP1, trail 1.7)
   next to the current v10.84 one (50 % at TP1, trail 3.5). Its setups cannot be told apart from the current ones, and its
   "Setup Ended" / "Shadow Ended" can carry a different result for the same setup. When two results exist for one setup,
   use the one whose breakdown shows "0.5×(TP1)"; say in the report that MGC 3m live results from 11/09 to 11/12 are partly
   on the old exits. Do not start the v10.84 revert-flag count for MGC 3m before 11/13.
3. BARFEED GAPS: MGC 3m missing 11/08 22:12 -> 11/09 06:21 (~157 candles) and 11/09 13:06 -> 11/10 01:33 (228 candles).
   Replays over those hours have no MGC 3m candles; setups there cannot be matched to bars. Other feeds complete (11/12).
4. MES 3m BOT TRIGGERS changed 11/12 (CBC v10.88, user decision): the bot now takes HTF CBC Flip + LTF EMA20 Pierce closed beyond
   EMA9 + LTF EMA20 Pierce NOT beyond EMA9 (the user ticked it on the bot copy on 11/12; v10.88 makes it the default). Any study
   text that says "current bot set = Flip + LTF beyond EMA9" is out of date: use the three-trigger set as "current" (bot_trig.py
   and bot_alerts_study.py already do). Watch item: "LTF EMA20 Pierce (not beyond EMA9)" in the bot windows with bot exits --
   11/12 baseline 24 live trades -8.7 pts, replay thirds -75 / -42 / +8. If after 3 more weekly runs it is still negative live
   (20+ new trades) and in 2+ replay thirds, say "consider unticking 'Trigger: LTF EMA20 Pierce (not beyond EMA9)' in ▶ Bot".

### Today's data health (16:51 ET)

- Server: serverVersion **14** (restarted 11/13 10:11 ET); near-copy dedupe on arrival is live (window 60 s, nearLiveGuard on; ignoredSinceStart 0, nearIgnoredSinceStart 0).
- Duplicates: `lastDedupe` = **null**. The stored alerts have still NOT been cleaned, so keep de-duplicating the 11/08-11/12 alerts when you read them (note 1).
- Alert archive: 10/19 -> 11/12 (22 days); last archive run 11/13 16:11 ET.
- BarFeed (/bars): all 15 active feeds (MES, MGC, MNQ, M2K, MCL x 3m / 2m / 5m) are current. Last candles 16:48 (3m) / 16:50 (2m, 5m) ET, 1-3 minutes old. **No stale feeds.** BTC feeds have 0 bars (not watched).

## Newest Pine

**pine/CBC_v10_96.pine** (indicator "v10.96", uploaded 11/13 10:59 ET). Previous snapshot: v10.93.
- v10.94 (11/13): bot news blackout. No bot entry within ± N minutes of the times in a listed news calendar.
- v10.95 (11/13): the "...close at TP1 (%) by time of day" list is now empty by default, so MES 3m closes 100 % at TP1 all day. A trail of 0 in "...trail x ATR per symbol/timeframe" now means no trail.
- v10.96 (11/13): MGC 3m exit is "FLIP 0 %". Nothing is closed at TP1; the stop goes to breakeven, there is no trail, and the trade is closed by the HTF CBC flip against it, BE, 16:00 or the next setup. A listed 0 % at TP1 is now honoured. The bot is unaffected (always 100 % at TP1).

## A. Input changes since the last snapshot (v10.93 -> v10.96)

Changed defaults (3):
- `ats_part_sym` "...close at TP1 (%) per symbol/timeframe": `"MES 3m 100, MGC 3m 50"` -> **`"MES 3m 100, MGC 3m 0"`** (v10.96)
- `ats_pw_sym` "...close at TP1 (%) by time of day, per symbol/timeframe": `"MES 3m 0600-1600 80, MES 3m 1800-2230 80"` -> **`""`** (v10.95)
- `ats_trl_sym` "...trail x ATR per symbol/timeframe": `"MGC 3m 3.5"` -> **`"MGC 3m 0"`** (v10.96; 0 = no trail since v10.95)

New inputs (2), both under ▶ Bot (v10.94):
- `bot_news` "News blackout list (USD red folder, ET)": `""` (off)
- `bot_nwm` "News blackout ± minutes": `5`

Removed inputs: none. Count 197 -> 199 ats_ / bot_ / xr_ / ema_ inputs.

What it means for the replays:
- **MES 3m chart exits** are now SL1 3 ATR, TP1 1.75 ATR and **100 % at TP1 at every hour**. The old rule closed 80 % with BE + trail 1.7 between 06:00-16:00 and 18:00-22:30.
- **MGC 3m chart exits** are now SL1 1.7 ATR (min 5, cap 7), TP1 1.7 ATR (cap 6), **0 % at TP1**. At TP1 the stop moves to BE with no trail, and the whole trade exits on the HTF flip against it, BE, 16:00 or the next setup. This replaces 50 % + trail 3.5 (v10.84).

## B. Script constants vs v10.96 defaults

### mes3_ema_grid.py `LIVE` (MES 3m) -- **MISMATCH**
- `part 'tod'` vs ats_pw_sym `""` + ats_part_sym "MES 3m 100" -> **MISMATCH**. The live value is 1.0 (100 % at TP1 all day).
- These fields match the live inputs:
  - sl 3.0 = ats_slx_sym "MES 3m 3"
  - mn 5
  - cap 1e9 = "MES 3m 0"
  - tp 1.75 = ats_tp1_sym "MES 3m 1.75"
  - tcap 1e9
  - be True
  - tr 1.7 = ats_trail_m0 (not used at 100 %)

### mes3_ema_grid.py `BASEX` -- MATCH
- sl 1.7, mn 5, cap 8, tp 1.7, tcap 6, part 0.8 (ats_part_pct 80), be True, tr 1.7.

### late_study.py
- `MGCX`: sl 1.7, mn 5, cap 7, tp 1.7, tcap 6 and be -> MATCH. The MGC 2m / 5m base also MATCHES.
- `MGCX` part 0.8 / tr 1.7 vs MGC 3m live -> **known** (the runner study's comparison base). Note: MGC 3m live is now **0 % / no trail (FLIP)**, not 50 % / 3.5.
- `MESX` = BASEX -> MATCH.

### chop_sim.py `EXIT`
- (MGC,3): part 0.5 / tr 3.5 vs ats_part_sym "MGC 3m 0" / ats_trl_sym "MGC 3m 0" -> **MISMATCH**. sl, tp, cap and tcap match.
- (MES,3): part 'tod' vs 100 % all day -> **MISMATCH**. The other fields match.
- (MGC,2) and (MES,2) base exits -> MATCH.

### chop_sim.py `GATE`
- (MGC,3) R5=1 / X4=1 -> MATCH.
- (MES,3) R5=1 -> MATCH.
- (MGC,2) R5=1 -> MATCH.
- (MES,2) MTF=1 -> MATCH.
- cur_rule thr 0.23 -> MATCH.

### botwin.py
- `inwin` = bot_win "1830-2200, 0300-1300, 1500-1530" -> MATCH.
- Short filter ('d5','S') = bot_d5 true -> MATCH.
- Note: botwin replays bot trades with `cb.CH['MES']` = `m.LIVE` ('tod'). The live bot is always 100 % at TP1, so fixing LIVE also brings botwin closer to the live bot.

### Outside the settings map (info, same root cause)
- `mes3_watch_a.py` keeps its own `LIVE` copy with `part='tod'`. `mes3_watch_tp1.py` hard-codes the 80 / 100 % time-of-day rule inline. Both are now stale for MES 3m.
- `gate_session.py` labels `dict(ls.MGCX, part=.5, tr=3.5)` as "live 50 % / trail 3.5". The MGC 3m live exit is now FLIP 0 %.
- `combo_study`, `exit_lab`, `sltime_study` and `trend_guard_study` use `ls.MGCX` (80 % / 1.7) as their MGC 3m "CH" exits. This is the same known MGCX difference, but those studies are now two exit changes behind live MGC 3m.
- `tp1flip_study.py` already models v10.96 (MES 100 %, MGC FLIP 0 %). OK.
- Bot replays (`bot_tp`, `bot_trig`, `bot_alerts_study`, `flip_exit_bot`, `flip_exit_study`) override to `dict(m.LIVE, part=1.0)` and are not affected.
- The bot news blackout (`bot_news`) is not modelled. It is empty by default, so there is no effect.

### Count
12 MATCH (BASEX, MGCX non-runner fields, MESX, EXIT MGC 2m / MES 2m, GATE x4, cur_rule, inwin, bot_d5), **3 MISMATCH** (LIVE part, EXIT MES 3m part, EXIT MGC 3m part / trail), 1 known (MGCX part / trail).

## C. Affected scripts / studies and fixes (not applied -- ask Claude)

1. **mes3_ema_grid.py `LIVE`**
   - Fix: `LIVE = dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=True, tr=1.7)`
   - Scripts that use it: late_study (CHARTS), combo_study / sltime_study / exit_lab / trend_guard_study (CH['MES']), plus runner_study, all_combo, skip_why (-> skip_fix, sess_loss), botwin, gate_session (MES) and the bot_* scripts (overridden to 1.0 already).
   - Same change for the own copy in `mes3_watch_a.py`. In `mes3_watch_tp1.py`, change `part = .8 if inside(tr['t']) else 1.0` to `part = 1.0`.
   - Studies: "Weekly exit + filter studies (3m charts) A-I" (Sat 18:27); "MES study: EMA, TP1, 5m-confirm, per-trigger, exit rules" (weekdays 17:37).
2. **chop_sim.py `EXIT[('MES',3)]`**
   - Fix: `('MES',3):dict(sl=3.0,mn=5,tp=1.75,tcap=1e9,part=1.0,be=True,ts=0,tr=1.7,cap=1e9)`
   - Used through `s.run(...)` without `q=` or through `cs.EXIT[...]` by: tp1flip_study (sets its own part), xtf_study, flip_order_study, ema_slope_study and breakout_flip_study. sl_reversal / flip_timing / evening_study overwrite MES 3m with base exits, so they are not affected.
   - Studies: "CBC setup order since HTF flip" (Sun), "CBC 1H MTF + 4H XTF" (on demand), "CBC EMA slope gate weekly check" (Fri 17:41), "Breakout + flip-ER variant study" (weekdays 17:28).
3. **chop_sim.py `EXIT[('MGC',3)]`**
   - Fix: `('MGC',3):dict(sl=1.7,mn=5,tp=1.7,tcap=6,part=0,be=True,ts=0,tr=0,cap=7)`
   - The constant alone is not enough. `Case.sim1` (and the copy in `mes3_ema_grid.MCase.sim1` and the 'tod' handlers in combo_study, exit_lab and sltime_study) would treat `tr=0` as a trail AT the close. Each needs the one-line guard `if hit and q['tr']>0:` in place of `if hit:` before the trail update.
   - Same scripts / studies as item 2, plus the evening / flip-timing and sl_reversal studies (they keep the chop_sim MGC 3m exits).
   - Optionally relabel gate_session.py's "live 50 % / trail 3.5" as "previous", and add `'live FLIP 0 %': dict(ls.MGCX, part=0, tr=0)`.
4. Also add rows to SETTINGS_MAP.md for `mes3_watch_a.py LIVE` / `mes3_watch_tp1.py` (MES 3m time-of-day rule) so this check tracks them.

### Known (no action)
- late_study.py MGCX part 0.8 / tr 1.7 vs MGC 3m live (runner-study comparison base). Live is now 0 % / no trail since v10.96.
