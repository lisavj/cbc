# MES 3m BOT WINDOWS ONLY (entries 09:30-13:00 + 15:00-15:30 ET, 5-day short filter) -- HTF CBC flip exit vs bracket, every alert type -- 2026-11-12 12:30 ET

MES 3m, 09:30-16:00 ET: does exiting on the HTF (15m) CBC flip beat the other exits? -- every alert type -- 11/12/2026.
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
| Outside HTF ORB | 48 | -38.3 | +103.7 | +342.3 | +288.2 | +184.6 | +55.8 / +128.8 | 50 % | **FLIP+SL** |
| High Confluence Setup | 46 | +197.6 | +143.3 | +219.9 | +217.2 | +74.0 | -66.6 / +140.5 | 54 % | **FLIP+SL** |
| HTF CBC Flip + LTF Agreement | 44 | +111.7 | +129.9 | +66.5 | +43.5 | -86.4 | -160.5 / +74.1 | 43 % | **BRACKET+FLIP** |
| LTF EMA20 Pierce | 44 | +88.7 | +44.4 | +132.3 | +155.2 | +110.8 | +82.0 / +28.8 | 43 % | **FLIP ONLY** |
| HTF EMA9 Pierce | 39 | -30.2 | +36.6 | +82.6 | +110.0 | +73.4 | +58.4 / +14.9 | 41 % | **FLIP ONLY** |
| A+ Setup | 30 | -88.3 | -74.7 | -37.6 | -59.2 | +15.4 | -65.1 / +80.5 | 37 % | **FLIP+SL** |
| ORB Pass + | 29 | -52.2 | +45.8 | -18.9 | -81.2 | -127.0 | -18.2 / -108.8 | 59 % | **BRACKET+FLIP** |
| HTF EMA20 Touch - Pullback Entry | 25 | -148.7 | -137.7 | -127.6 | -163.8 | -26.1 | -83.1 / +57.0 | 24 % | **FLIP+SL** |
| Key Level Alert | 25 | +62.8 | +73.2 | +109.8 | +150.0 | +76.8 | +15.9 / +60.9 | 40 % | **FLIP ONLY** |
| Price Enters HTF EMA9/20 Zone | 20 | -189.9 | -154.8 | -173.2 | -163.8 | -8.9 | -19.8 / +10.9 | 30 % | **BRACKET+FLIP** |
| HTF EMA20 Pierce | 19 | +22.2 | +17.0 | +100.7 | +20.8 | +3.7 | +26.4 / -22.7 | 47 % | **FLIP+SL** |
| ORB Pass - | 11 | +26.2 | +53.4 | +154.2 | +154.2 | +100.8 | +1.0 / +99.9 | 64 % | **FLIP+SL** |
| ALL live alerts (types with 10+) | 380 | -38.5 | +280.2 | +850.9 | +671.2 | +391.0 | -123.9 / +514.9 | 44 % | **FLIP+SL** |

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