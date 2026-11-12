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
