# MES 3m 09:30-16:00 ET -- HTF CBC flip exit vs bracket, every alert type -- 2026-11-14 13:43 ET

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
| High Confluence Setup | 91 | +162.7 | +118.3 | +87.6 | +68.0 | -50.3 | -101.4 / +51.1 | 46 % | **BRACKET** |
| LTF EMA20 Pierce | 84 | +105.6 | +29.5 | +36.3 | +55.5 | +26.0 | +26.0 / -0.0 | 40 % | **BRACKET** |
| HTF CBC Flip + LTF Agreement | 76 | +71.8 | +102.9 | -100.0 | -114.0 | -216.9 | -202.0 / -14.9 | 34 % | **BRACKET+FLIP** |
| HTF EMA9 Pierce | 71 | -36.8 | +41.9 | +110.3 | +167.5 | +125.6 | +57.5 / +68.1 | 39 % | **FLIP ONLY** |
| Outside HTF ORB | 65 | -18.6 | +176.9 | +524.3 | +469.5 | +292.6 | +7.3 / +285.3 | 51 % | **FLIP+SL** |
| A+ Setup | 55 | -114.2 | -50.1 | +10.7 | -5.8 | +44.4 | -115.6 / +160.0 | 33 % | **FLIP+SL** |
| HTF EMA20 Touch - Pullback Entry | 52 | -213.5 | -297.9 | -279.7 | -315.0 | -17.1 | -71.3 / +54.1 | 19 % | **BRACKET** |
| Key Level Alert | 49 | +224.7 | +226.7 | +315.7 | +386.2 | +159.5 | +58.6 / +100.9 | 47 % | **FLIP ONLY** |
| Price Enters HTF EMA9/20 Zone | 45 | -378.4 | -319.4 | -367.0 | -367.0 | -47.6 | -14.6 / -33.0 | 18 % | **BRACKET+FLIP** |
| HTF EMA20 Pierce | 43 | -56.4 | -57.3 | +6.7 | -71.8 | -14.4 | +9.2 / -23.7 | 40 % | **FLIP+SL** |
| ORB Pass + | 37 | -119.6 | -5.7 | -114.3 | -164.5 | -158.8 | -17.4 / -141.4 | 51 % | **BRACKET+FLIP** |
| LTF EMA20 Touch - Pullback Entry | 18 | -91.1 | -61.7 | -61.8 | -42.0 | +19.7 | +19.8 / -0.0 | 28 % | **FLIP ONLY** |
| ORB Pass - | 17 | +20.6 | +82.5 | +309.5 | +309.5 | +227.0 | +17.2 / +209.8 | 59 % | **FLIP+SL** |
| VWAP Bounce - High R | 15 | +71.6 | +81.0 | +143.3 | +140.8 | +59.7 | -7.6 / +67.3 | 60 % | **FLIP+SL** |
| SETUP: LTF Pierce not beyond EMA9 | 13 | +5.7 | +20.1 | +9.8 | +1.5 | -18.6 | -68.3 / +49.7 | 38 % | **BRACKET+FLIP** |
| SETUP: LTF Pierce beyond EMA9 | 10 | -13.3 | +16.6 | +24.5 | +24.5 | +7.9 | -11.7 / +19.5 | 40 % | **FLIP+SL** |
| ALL live alerts (types with 10+) | 741 | -379.2 | +104.4 | +655.9 | +543.0 | +438.6 | -406.5 / +845.0 | 39 % | **FLIP+SL** |

## Replay Trade Setups Jan 5 -> now, by trigger (thirds Jan-Mar / Apr-Jul / Aug-Nov approx.)

| Trigger | Trades | Bracket (TP/SL only) | Bracket + flip (now) | Flip + SL | FLIP ONLY | Flip only vs now | ...by third | Flip-only win % | Best |
|---|---|---|---|---|---|---|---|---|---|
| LTF Pierce not beyond EMA9 | 124 | -89.3 | -160.1 | -268.9 | -260.8 | -100.7 | +49 / -7 / -143 | 28 % | **BRACKET** |
| HTF EMA9 Pierce | 98 | -88.4 | -30.7 | -130.0 | -137.5 | -106.8 | -65 / -23 / -19 | 33 % | **BRACKET+FLIP** |
| HTF CBC Flip | 91 | -170.3 | -192.1 | -68.9 | -87.0 | +105.1 | +121 / -29 / +14 | 37 % | **FLIP+SL** |
| LTF Pierce beyond EMA9 | 77 | -166.3 | -59.6 | -9.3 | -5.0 | +54.6 | +32 / +25 / -2 | 35 % | **FLIP ONLY** |
| HTF EMA20 Pierce | 70 | +120.7 | +109.1 | +102.2 | +111.0 | +1.9 | -11 / +61 / -48 | 39 % | **BRACKET** |
| LTF Pierce late | 49 | +89.6 | -36.5 | -70.3 | -62.2 | -25.8 | +12 / -48 / +10 | 37 % | **BRACKET** |
| ALL replay setups | 509 | -303.9 | -369.9 | -445.2 | -441.5 | -71.6 | +138 / -22 / -187 | 34 % | **BRACKET** |