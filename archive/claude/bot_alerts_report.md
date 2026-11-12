# MES 3m bot -- every alert type and which checkboxes to tick -- 2026-11-12 10:02 ET

MES 3m BOT -- every alert / trigger type and which bot checkboxes should be ticked -- 11/12/2026.

Bot rules (CBC v10.87): MES 3m only; entry windows 18:30-22:00, 03:00-13:00, 15:00-15:30 ET (candle close); no new entries from
15:45; flatten 15:57; no shorts while price is above the 5-day EMA (bot_d5); 100 % closed at TP1 (bracket TP1 / SL1).
A. REPLAY Jan 5 -> now (chop_sim engine, every CBC trigger on, then the bot filters): per trigger type, bot exits
   (SL1 3 ATR, TP1 1.75 ATR, 100 % at TP1, CBC setup end / 16:00), 0.50 pt cost per trade.
B. LIVE since 10/19: real MES 3m Trade Setup alerts, re-run with the BOT exits on the BarFeed candles (TP1 / SL1 from the alert,
   stop first if one candle touches both, else exit at the close of the candle that ended CBC's setup ("Setup Ended" Time) or
   the 15:57 flatten), 0.50 pt cost. Limit-entry fills are assumed. Also the CBC chart result (Setup Ended) for reference.
C. ALL OTHER ALERT TYPES on MES 3m (not tradable by the bot today -- no checkbox): each directional alert scored with the bot's
   bracket (entry = alert candle close, SL 3 ATR / TP 1.75 ATR, else exit on the opposite HTF CBC flip or the 15:57 flatten),
   inside the bot windows + short filter, 0.50 pt cost -- shows whether any could become a bot trigger later.
Duplicates: alerts with the same chart, Time line and alert names within 60 s count once.
Verdict per checkbox: CHECK = replay positive in all three thirds AND live (bot windows, bot exits) >= 15 trades with net > 0;
KEEP OFF = replay negative in 2+ thirds AND live <= 0 (or <5 live trades and replay negative in all thirds); else WATCH.

Replay 01/05 -> 11/12. Live alerts since 10/19 (13 MES 3m duplicates dropped). Live halves split at 10/27.

## 1. Bot checkboxes (Trade Setup triggers)

| Checkbox | Now | Replay trades / net | Replay thirds | Replay last 4 wk | Live in bot windows: n / bot-exit net / win % (halves) | Live CBC result same setups | Live all hours (bot exits) | Verdict |
|---|---|---|---|---|---|---|---|---|
| HTF CBC Flip | ON | 151 / -125 | -93 / -67 / +36 | +51 | 13 / +35.3 / 62 % (+3.7 / +31.6) | +43.1 | 16 / +12.1 | **WATCH** |
| LTF EMA20 Pierce (closed beyond EMA9) | ON | 110 / -24 | +87 / -94 / -17 | -16 | 6 / +16.1 / 83 % (-0.4 / +16.5) | +20.9 | 15 / +7.9 | **WATCH** |
| LTF EMA20 Pierce (not beyond EMA9) | off | 218 / -109 | -75 / -42 / +8 | +92 | 24 / -8.7 / 50 % (-2.5 / -6.2) | +7.6 | 31 / -31.0 | **KEEP OFF** |
| LTF EMA20 Pierce (late confirm) | off | 100 / +7 | +2 / +7 / -3 | +20 | 17 / -17.3 / 47 % (-3.8 / -13.5) | -2.4 | 20 / -37.6 | **WATCH** |
| HTF EMA9 Pierce (incl. late) | off | 211 / -10 | +46 / -80 / +24 | +12 | 11 / +0.5 / 45 % (-8.5 / +9.0) | +14.2 | 14 / -9.2 | **WATCH** |
| HTF EMA20 Pierce (incl. late) | off | 114 / +89 | +125 / -27 / -9 | +1 | 5 / +4.5 / 60 % (-3.5 / +8.0) | +10.4 | 8 / -12.5 | **WATCH** |
| Momentum break | off | not in replay | - | - | 0 / +0.0 / 0 % (+0.0 / +0.0) | +0.0 | 0 / +0.0 | **WATCH (live only)** |
| HTF Pullback Structure | off | not in replay | - | - | 0 / +0.0 / 0 % (+0.0 / +0.0) | +0.0 | 2 / -10.1 | **WATCH (live only)** |
| LTF EMA20 Touch (mid-candle) | off | not in replay | - | - | 0 / +0.0 / 0 % (+0.0 / +0.0) | +0.0 | 0 / +0.0 | **WATCH (live only)** |

## 2. Every other MES 3m alert type, scored as if the bot traded it (bot windows + short filter, SL 3 / TP 1.75 ATR, after costs)

Baseline (no signal: EVERY 3m candle in the bot windows, same bracket): long avg -0.42 (5214), short avg +0.13 (3074) -- an alert type is only useful if it beats these.

| Alert type | Trades | Win % | Net | Avg | Long n / avg | Short n / avg | 1st half / 2nd half | Note |
|---|---|---|---|---|---|---|---|---|
| Outside HTF ORB | 147 | 68 % | +368.8 | +2.51 | 92 / +1.97 | 55 / +3.40 | +97.8 / +271.0 | positive in both halves |
| Key Level Alert | 69 | 80 % | +290.8 | +4.21 | 43 / +4.31 | 26 / +4.06 | +80.9 / +209.9 | positive in both halves |
| High Confluence Setup | 145 | 70 % | +233.8 | +1.61 | 76 / +1.90 | 69 / +1.29 | +135.0 / +98.8 | positive in both halves |
| ORB Pass - | 54 | 69 % | +143.7 | +2.66 | 0 / +0.00 | 54 / +2.66 | +46.6 / +97.1 | positive in both halves |
| VWAP Bounce - High R | 53 | 74 % | +139.5 | +2.63 | 31 / +2.53 | 22 / +2.77 | +77.2 / +62.3 | positive in both halves |
| HTF EMA20 Pierce | 84 | 64 % | +94.8 | +1.13 | 55 / -0.09 | 29 / +3.44 | +72.8 / +22.1 | positive in both halves |
| ORB Pass + | 79 | 61 % | +87.7 | +1.11 | 79 / +1.11 | 0 / +0.00 | +41.2 / +46.5 | positive in both halves |
| HTF CBC Flip + LTF Agreement | 125 | 62 % | +72.4 | +0.58 | 75 / -0.71 | 50 / +2.52 | +66.0 / +6.4 | positive in both halves |
| LTF EMA20 Pierce | 135 | 64 % | +70.8 | +0.52 | 88 / +1.31 | 47 / -0.95 | +75.0 / -4.2 |  |
| HTF EMA9 Pierce | 137 | 57 % | +0.3 | +0.00 | 65 / +0.46 | 72 / -0.41 | -5.7 / +6.0 |  |
| HTF Pullback Entry - Structure Confirmed | 1 | 0 % | -18.2 | -18.17 | 1 / -18.17 | 0 / +0.00 | +0.0 / -18.2 | too few |
| LTF EMA20 Touch - Pullback Entry | 33 | 48 % | -63.7 | -1.93 | 18 / -3.99 | 15 / +0.54 | -62.2 / -1.6 |  |
| A+ Setup | 136 | 47 % | -183.7 | -1.35 | 65 / -0.37 | 71 / -2.25 | -233.5 / +49.8 |  |
| Price Enters HTF EMA9/20 Zone | 61 | 33 % | -280.1 | -4.59 | 39 / -3.35 | 22 / -6.80 | -178.3 / -101.8 |  |
| HTF EMA20 Touch - Pullback Entry | 100 | 28 % | -424.8 | -4.25 | 57 / -5.66 | 43 / -2.37 | -232.8 / -192.1 |  |

## Summary

- Tick: nothing passes the CHECK rule
- Keep unticked: LTF EMA20 Pierce (not beyond EMA9)
- Watch (not enough evidence either way): HTF CBC Flip, LTF EMA20 Pierce (closed beyond EMA9), LTF EMA20 Pierce (late confirm), HTF EMA9 Pierce (incl. late), HTF EMA20 Pierce (incl. late), Momentum break, HTF Pullback Structure, LTF EMA20 Touch (mid-candle)
- Other alert types positive in both halves with 20+ trades (would need a new bot checkbox): 8