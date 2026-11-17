# MES 3m bot flip-exit watch -- 2026-11-14 13:37 ET

STUDY SETTINGS STALE: settings_sync_report.md (11/13 16:47 ET) lists 3 non-"known" MISMATCHes -- mes3_ema_grid `LIVE` part 'tod' (live MES 3m is 100 % at TP1 all day since v10.95), chop_sim `EXIT[('MES',3)]` part 'tod', chop_sim `EXIT[('MGC',3)]` 50 % / trail 3.5 (live MGC 3m is FLIP 0 % since v10.96). The two flip-exit replays override the exit to `dict(m.LIVE, part=1.0)` and only use MES 3m, so this watch is not affected.

Data notes followed: stored alerts still not de-duplicated (lastDedupe null) -- both scripts key live events by (type, candle, direction), so near copies count once. No MES 3m BarFeed gaps listed. 11/13 (Friday) is the only new session since the 11/12 baseline.

## Verdict: HELD -- Flip-exit weeks held: 1

| Check | Result | Rule | Pass |
|---|---|---|---|
| Bot-window replay, HTF CBC Flip (46): flip+SL vs bracket+flip, total | +52.2 vs -73.5 (**+125.7**) | flip+SL better | yes |
| ...by third (Jan 5-Apr 19 / Apr 19-Aug 1 / Aug 1-Nov 13) | **+71 / -20 / +75** (flip+SL -3 / -41 / +96 vs old -74 / -21 / +21) | 2 of 3 better | yes |
| Live HTF CBC Flip bot trades since 11/13 | **0** | 10+ needed to count | n/a |

Replay unchanged from the 11/12 baseline (no new HTF CBC Flip setup in the bot windows on 11/13).

## 1. Replay, bot windows (09:30-13:00 + 15:00-15:30 ET, 5-day short filter), Jan 5 -> 11/13, net after 0.50

| Trigger | n | Bracket | Bracket + flip (old) | Flip + SL | Flip only | Flip+SL vs old by third |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 46 | -21.8 | -73.5 | **+52.2** | +60.8 | +71 / -20 / +75 |
| LTF Pierce beyond EMA9 | 34 | -78.6 | -19.8 | -5.5 | +0.5 | +19 / -5 / 0 |
| LTF Pierce not beyond EMA9 | 63 | -36.2 | -80.9 | -264.2 | -249.8 | -47 / -25 / -111 |
| HTF EMA9 Pierce | 60 | +62.7 | +63.3 | -53.7 | -61.2 | -- |
| HTF EMA20 Pierce | 35 | +149.0 | +126.9 | +186.5 | +197.2 | -- |
| LTF Pierce late | 29 | +42.1 | -37.8 | -23.7 | -20.8 | -- |
| ALL | 267 | +117.2 | -21.9 | -108.5 | -73.2 | -- |

All entries 09:30-15:45 (flip_exit_report.md): HTF CBC Flip 91 setups (was 90): bracket+flip -192.1, flip+SL -68.9, flip only -87.0; flip-only vs old by third +121 / -29 / +14. LTF Pierce beyond EMA9 77: old -59.6, flip+SL -9.3. LTF Pierce not beyond EMA9 124: old -160.1, flip+SL -268.9.

## 2. Live check (alerts since 11/13)

- MES 3m Trade Setups with first trigger HTF CBC Flip in 09:30-13:00 / 15:00-15:30: **0**. The only MES 3m Trade Setup on 11/13 was an LTF EMA20 Pierce (beyond EMA9) LONG at 08:33, ended SL1 -16.32 (bracket trigger, not part of this watch).
- "• Bot Order (preview)" alerts: 1 (11/13 08:33, buy limit 7662, take_profit=7671.00, stop_loss=7645.25 -- the LTF trade, correctly bracketed). Previews without take_profit= (flip-only orders): **0** -- v10.92 not yet confirmed live, as no HTF CBC Flip bot entry occurred.

## 3. Next trigger to switch?

LTF Pierce beyond EMA9 (bot windows): flip+SL -5.5 vs old -19.8 (+14.3), thirds +19 / -5 / 0 -- small and not consistent; not yet a case to switch. LTF Pierce not beyond EMA9 stays clearly worse with flip exit (-183 pts).

## Notes

- Scripts run as stored (flip_exit_study.py, flip_exit_bot.py); helper modules saved locally with their engine parts only. No script needed a fix.
- Thirds for flip+SL vs bracket+flip computed from the same bot-window replay run (the report table's "by third" column is flip-only vs old).

## History

| Run | HTF CBC Flip bot-window replay: old / flip+SL / flip+SL-vs-old thirds | Live n / old / flip+SL | Verdict | Weeks held |
|---|---|---|---|---|
| 2026-11-14 | -73.5 / +52.2 / +71 / -20 / +75 | 0 / -- / -- | HELD | 1 |
| 2026-11-12 (week 0, baseline) | -73.5 / +52.2 / flip-only thirds +79 / -27 / +82 | -- | baseline | 0 |
