# CBC settings sync -- 2026-11-12 16:47 ET

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

### Today's data health (16:48 ET)

- Server: serverVersion **14** (started 11/12 15:19 ET), so near-copy dedupe on arrival is live (window 60 s, nearLiveGuard on; ignoredSinceStart 0, nearIgnoredSinceStart 0).
- Duplicates: `lastDedupe` = **null**. The stored alerts have NOT been cleaned yet, so keep de-duplicating 11/08-11/12 alerts when you read them (note 1).
- Alert archive: 10/19 -> 11/11 (21 days), last archive run 11/12 16:19 ET.
- BarFeed (/bars): all 15 active feeds (MES, MGC, MNQ, M2K, MCL x 3m / 2m / 5m) current. Last candles 16:45 / 16:46 ET, 3-4 open-market minutes old. **No stale feeds.** BTC feeds have 0 bars (not watched).

## Newest Pine

**pine/CBC_v10_93.pine** (indicator "v10.93", uploaded 11/12 12:37 ET). Previous snapshot: v10.87. Versions v10.88-v10.93 all came out 11/12 and are all ▶ Bot (CrossTrade) changes.

## A. Input changes since the last snapshot (v10.87 -> v10.93)

Changed default (1):
- `bot_t_ln` "Trigger: LTF EMA20 Pierce (not beyond EMA9)": false -> **true** (v10.88; already in data note 4).

New inputs (5), all under ▶ Bot:
- `bot_eow` "Entry-only windows: no exit orders": `""` (off) (v10.89)
- `bot_eof` "...but still exit on an HTF CBC flip against the trade": `false` (v10.90)
- `bot_fow` "Flip-only windows: no TP, closed by the HTF CBC flip": **`"0930-1600"`** (v10.91, ON by default since v10.92)
- `bot_foall` "...applies to": `"HTF CBC Flip only"` (v10.92; other choice "All bot triggers")
- `bot_fosl` "...keep SL1 as a safety stop": `true` (v10.92)

Removed inputs: none. Count 192 -> 197 ats_ / bot_ / xr_ / ema_ inputs.

What it means: since v10.92 a MES 3m **bot** entry from an HTF CBC Flip on a candle closing 09:30-16:00 ET is sent with SL1 but **no TP**, and is closed by the HTF CBC flip against it / SL1 / 15:57 / the next bot entry. Other bot triggers and all non-bot (chart) setups keep the normal exits. v10.93 is a compile fix only (same behaviour as v10.92).

## B. Script constants vs v10.93 defaults

Scripts checked (project copies, none changed since the last run): mes3_ema_grid.py (11/04), late_study.py (11/07), chop_sim.py (10/24 upload with the 11/08 live EXIT / GATE values), botwin.py (11/08). No ats_ / xr_ / ema_ input changed, so every mapping holds.

### mes3_ema_grid.py `LIVE` (MES 3m) -- MATCH
sl 3.0 = ats_slx_sym "MES 3m 3"; mn 5 = MES 5 (ats_msl_sym ""); cap 1e9 = ats_cap_txt "MES 3m 0"; tp 1.75 = ats_tp1_sym "MES 3m 1.75"; tcap 1e9 = ats_tpc_txt "MES 3m 0"; part 'tod' = ats_pw_sym "MES 3m 0600-1600 80, MES 3m 1800-2230 80" + ats_part_sym "MES 3m 100"; be True = ats_be_on true; tr 1.7 = ats_trail_m0 1.7 (no MES 3m in ats_trl_sym).

### mes3_ema_grid.py `BASEX` -- MATCH
sl 1.7 = ats_atr_m1; mn 5; cap 8 = MES 8; tp 1.7 = ats_atr_t1; tcap 6 = MES 6; part 0.8 = ats_part_pct 80; be True; tr 1.7 = ats_trail_m0.

### late_study.py
- `MGCX`: sl 1.7 / mn 5 / cap 7 / tp 1.7 / tcap 6 / be -> MATCH (MGC 2m / 5m base also MATCH).
- `MGCX` part 0.8 / tr 1.7 vs MGC 3m live ats_part_sym "MGC 3m 50" / ats_trl_sym "MGC 3m 3.5" -> **known** (runner-study comparison base since v10.84).
- `MESX` = BASEX -> MATCH.

### chop_sim.py `EXIT`
- (MGC,3) part 0.5 / tr 3.5 / sl 1.7 / tp 1.7 / cap 7 / tcap 6 -> MATCH.
- (MES,3) = LIVE -> MATCH.
- (MGC,2), (MES,2) base exits -> MATCH.

### chop_sim.py `GATE`
- (MGC,3) R5=1, X4=1 = ats_rp_sym "MGC 3m 5", ats_f_ext_sym "MGC 3m 4" -> MATCH.
- (MES,3) R5=1 = "MES 3m 5" -> MATCH. (MGC,2) R5=1 = "MGC 2m 5" -> MATCH. (MES,2) MTF=1 = ats_mtg_sym "MES 2m 1" -> MATCH.
- cur_rule thr 0.23 = ats_c_er / ats_fer 0.23 -> MATCH.

### botwin.py
- `inwin` 18:30-22:00, 03:00-13:00, 15:00-15:30 = bot_win "1830-2200, 0300-1300, 1500-1530" -> MATCH.
- short filter ('d5','S') = bot_d5 true -> MATCH.

### Not in the settings map (info -- new bot behaviour the replays do not model)
- **Bot flip-only exit** (`bot_fow` "0930-1600", `bot_foall` "HTF CBC Flip only", `bot_fosl` true): botwin.py (and bot_tp.py / bot_alerts_study.py / bot_trig.py, which use the MES 3m live exits for bot trades) replay HTF CBC Flip bot trades 09:30-16:00 with TP1 1.75 + partial / trail, while the live bot now holds them to the HTF flip with SL1 only. Their "bot exits" results for Flip trades in that window no longer describe the live bot. flip_exit_bot.py (11/12) is the study behind this change and is the natural place to take the model from.
- **Bot triggers** (`bot_t_ln` now true): botwin.py says "bot trigger choices are not modelled"; bot_trig.py / bot_alerts_study.py already use the three-trigger set (data note 4).
- Not modelled, unchanged: ats_fl2_sym "MGC 2m 1", ats_fw2_sym "MES 3m 8", ats_fa_sym "MES 2m 9", xr_cut / xr_lock exit rules.

### Count
14 MATCH (LIVE, BASEX, MGCX non-runner fields, MESX, EXIT x4, GATE x4, inwin, bot_d5), **0 MISMATCH**, 1 known (MGCX part / trail). 1 new unmodelled bot exit rule (info).

## C. Affected scripts / studies and fixes

- Mismatches: none -- no constant changes needed.
- Suggested (not a constant fix, needs a small model change; not done here): give the bot replays a flip-only exit option for HTF CBC Flip entries on candles closing 09:30-16:00 ET (no TP, exit on HTF flip against / SL1 / 15:57 / next bot entry) in botwin.py / bot_tp.py / bot_alerts_study.py, and add a SETTINGS_MAP.md row for `bot_fow` / `bot_foall` / `bot_fosl` so this check tracks them.

### Known (no action)
- late_study.py MGCX part 0.8 / tr 1.7 vs MGC 3m 50 % / trail 3.5 (runner study comparison base).
