# MES 3m BOT WINDOWS ONLY (entries 09:30-13:00 + 15:00-15:30 ET, 5-day short filter) -- HTF CBC flip exit vs bracket, every alert type -- 2026-11-14 13:43 ET

(flip_exit_bot.py = bot windows 09:30-13:00 + 15:00-15:30 + 5-day short filter)  MES 3m, 09:30-16:00 ET: does exiting on the HTF (15m) CBC flip beat the other exits? -- every alert type -- 11/12/2026.
Entry = close of the alert / setup candle, candle closing 09:30-15:45 ET (no filters: every alert of the type, both directions).
Exit variants (all flat at the 15:57 candle close at the latest; 0.50 pt cost per trade; ATR = 14 on 3m):
  BRACKET      SL 3 ATR / TP 1.75 ATR only (the bot bracket, no flip exit)
  BRACKET+FLIP SL 3 ATR / TP 1.75 ATR, or exit at the close of the candle where the HTF CBC flips against the trade (current bot)
  FLIP+SL      no target: SL 3 ATR, else exit on the HTF CBC flip against
  FLIP ONLY    no target, no stop: exit on the HTF CBC flip against (or 15:57)
LIVE = alert store since 10/19 (duplicates removed). REPLAY = Trade Setups from the chop_sim replay Jan 5 -> now, by trigger.

## Live alerts since 10/19 (net pts after costs)

| Alert type | Trades | Bracket (TP/SL only) | Bracket + flip (now) | Flip + SL | FLIP ONLY | Flip only vs now | ...by half | Flip-only win % | Best |
|---|---|---|---|---|---|---|---|---|---|
| Outside HTF ORB | 50 | -6.2 | +135.8 | +361.3 | +307.2 | +171.5 | +36.4 / +135.1 | 50 % | **FLIP+SL** |
| High Confluence Setup | 47 | +169.1 | +114.8 | +191.4 | +162.8 | +48.0 | -66.6 / +114.5 | 53 % | **FLIP+SL** |
| HTF CBC Flip + LTF Agreement | 46 | +144.2 | +145.7 | +47.2 | +24.2 | -121.5 | -153.1 / +31.6 | 41 % | **BRACKET+FLIP** |
| LTF EMA20 Pierce | 45 | +60.5 | +16.2 | +104.1 | +114.2 | +98.0 | +82.0 / +16.0 | 42 % | **FLIP ONLY** |
| HTF EMA9 Pierce | 39 | -30.2 | +36.6 | +82.6 | +110.0 | +73.4 | +58.4 / +14.9 | 41 % | **FLIP ONLY** |
| A+ Setup | 31 | -72.5 | -58.8 | -56.8 | -78.5 | -19.7 | -65.1 / +45.4 | 35 % | **FLIP+SL** |
| ORB Pass + | 30 | -36.5 | +61.5 | -47.2 | -106.0 | -167.5 | -16.1 / -151.4 | 57 % | **BRACKET+FLIP** |
| Key Level Alert | 27 | +97.3 | +107.7 | +122.5 | +162.8 | +55.0 | +11.7 / +43.3 | 41 % | **FLIP ONLY** |
| HTF EMA20 Touch - Pullback Entry | 25 | -148.7 | -137.7 | -127.6 | -163.8 | -26.1 | -83.1 / +57.0 | 24 % | **FLIP+SL** |
| Price Enters HTF EMA9/20 Zone | 20 | -189.9 | -154.8 | -173.2 | -163.8 | -8.9 | -19.8 / +10.9 | 30 % | **BRACKET+FLIP** |
| HTF EMA20 Pierce | 19 | +22.2 | +17.0 | +100.7 | +20.8 | +3.7 | +26.4 / -22.7 | 47 % | **FLIP+SL** |
| ORB Pass - | 12 | +42.9 | +70.2 | +186.5 | +186.5 | +116.3 | +10.5 / +105.9 | 67 % | **FLIP+SL** |
| ALL live alerts (types with 10+) | 391 | +52.2 | +354.2 | +791.4 | +576.5 | +222.3 | -72.7 / +295.0 | 44 % | **FLIP+SL** |

## Replay Trade Setups Jan 5 -> now, by trigger (thirds Jan-Mar / Apr-Jul / Aug-Nov approx.)

| Trigger | Trades | Bracket (TP/SL only) | Bracket + flip (now) | Flip + SL | FLIP ONLY | Flip only vs now | ...by third | Flip-only win % | Best |
|---|---|---|---|---|---|---|---|---|---|
| LTF Pierce not beyond EMA9 | 63 | -36.2 | -80.9 | -264.2 | -249.8 | -168.9 | -42 / -18 / -110 | 30 % | **BRACKET** |
| HTF EMA9 Pierce | 60 | +62.7 | +63.3 | -53.7 | -61.2 | -124.5 | -60 / -16 / -48 | 33 % | **BRACKET+FLIP** |
| HTF CBC Flip | 46 | -21.8 | -73.5 | +52.2 | +60.8 | +134.3 | +79 / -27 / +82 | 41 % | **FLIP ONLY** |
| HTF EMA20 Pierce | 35 | +149.0 | +126.9 | +186.5 | +197.2 | +70.4 | +41 / +59 / -29 | 46 % | **FLIP ONLY** |
| LTF Pierce beyond EMA9 | 34 | -78.6 | -19.8 | -5.5 | +0.5 | +20.3 | +19 / +2 / -0 | 38 % | **FLIP ONLY** |
| LTF Pierce late | 29 | +42.1 | -37.8 | -23.7 | -20.8 | +17.1 | -3 / -4 / +25 | 45 % | **BRACKET** |
| ALL replay setups | 267 | +117.2 | -21.9 | -108.5 | -73.2 | -51.3 | +33 / -5 / -80 | 37 % | **BRACKET** |