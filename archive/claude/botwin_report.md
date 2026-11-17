## Week of 11/14/2026 summary

- STUDY SETTINGS STALE: the 11/13 settings sync (v10.96) lists 3 non-known MISMATCHes, NOT yet fixed in the project scripts, and they touch the 3m studies -- mes3_ema_grid LIVE still closes MES 3m 80/100 % by time of day (live since v10.95: 100 % at TP1 all day), and MGC 3m live is now FLIP 0 % (v10.96: nothing closed at TP1, BE, no trail, exit on HTF flip) while these replays use 80 % / trail 1.7 (MGCX) or 50 % / 3.5. Bot replay (H) is unaffected (part 1.0). Also new: the 11/14 X4 fix in mes3_ema_grid.py makes the MGC 3m VWAP-stretch gate actually block setups (MGC 3m 1193 setups vs 1707 last week), so MGC 3m numbers are not like-for-like with 11/09. Here: botwin replays MES 3m chart exits with 80/100 % by time of day; the live bot is 100 % at TP1 (see bot_trigger_report for bot exits).
- MES 3m BOT windows (v10.87), after costs: current **-469** (thirds +29 / -476 / -22, last 4 wk +174, max DD 794).
- **5-day short filter (live since v10.86): -229** (beyond random +2 / +108 / +28, last 4 wk +165 vs +174, max DD 564) -> **WEAKER** (beyond random >= 0 in every third, but last 4 weeks 9 pts behind current; not FAILED). **Bot short filter: weeks held 0/3.**
- TP1 -> 85 % after 18 min: -398 (beyond random +38 / +36 / +15, last 4 wk +130). Filter + TP rule: -215 (beyond random +23 / +150 / -5). Balanced filter + losing-stretch stop + SL rule: -99 (beyond random -64 / +229 / +43; max DD 334, PF 0.96) -- none better in all thirds AND last 4 weeks.
- Windows: 13:00-14:00 (removed) still loses: 91 setups -250, all thirds negative (-47 / -114 / -88) -> keep it out.

---

# MES 3m bot-window check — run 11/14/2026

Replay of MES 3m setups that START inside the bot entry windows (candle close 18:30-22:00, 03:00-13:00, 15:00-15:30 ET = v10.87 bot windows), live MES 3m exits, net after costs (0.50 pts per trade, +0.25 for a rule exit). Brackets = gain beyond dropping the same number of trades at random. Bot trigger choices are not modelled.

| Rule set (bot windows only) | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | PF | Max DD |
|---|---|---|---|---|---|---|---|---|
| Current exits | +29 (+0) | -476 (+0) | -22 (+0) | +174 (+0) | -469 (+0) | 1124 | 0.88 | 794 |
| TP1 -> 85 % after 18 min | +62 (+38) | -446 (+36) | -15 (+15) | +130 (-42) | -398 (+88) | 1167 | 0.89 | 717 |
| SL: half SL1 if negative at 18 min | +18 (-10) | -469 (+9) | -47 (-20) | +143 (-29) | -498 (-20) | 1145 | 0.87 | 778 |
| TP + SL rules | +60 (+37) | -445 (+39) | -42 (-8) | +112 (-59) | -427 (+68) | 1186 | 0.88 | 720 |
| 5-day short filter | +57 (+2) | -327 (+108) | +40 (+28) | +165 (-12) | -229 (+139) | 884 | 0.92 | 564 |
| Filter + TP rule | +72 (+23) | -290 (+150) | +2 (-5) | +122 (-54) | -215 (+167) | 917 | 0.93 | 540 |
| Balanced: filter + losing-stretch stop + SL rule | -2 (-64) | -180 (+229) | +84 (+43) | +135 (-42) | -99 (+207) | 734 | 0.96 | 334 |
| Filter + losing-stretch stop + TP rule | -4 (-62) | -206 (+206) | +93 (+54) | +117 (-60) | -117 (+197) | 753 | 0.95 | 366 |
