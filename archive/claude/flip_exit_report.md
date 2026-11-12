# MES 3m 09:30-16:00 ET -- HTF CBC flip exit vs bracket, every alert type -- 2026-11-12 12:00 ET

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
| High Confluence Setup | 90 | +191.2 | +146.7 | +116.1 | +122.5 | -24.2 | -101.4 / +77.1 | 47 % | **BRACKET** |
| LTF EMA20 Pierce | 83 | +133.8 | +57.7 | +64.5 | +96.5 | +38.8 | +25.6 / +13.2 | 41 % | **BRACKET** |
| HTF CBC Flip + LTF Agreement | 73 | +24.0 | +71.8 | -113.5 | -127.5 | -199.3 | -185.7 / -13.6 | 34 % | **BRACKET+FLIP** |
| HTF EMA9 Pierce | 71 | -36.8 | +41.9 | +110.3 | +167.5 | +125.6 | +57.5 / +68.1 | 39 % | **FLIP ONLY** |
| Outside HTF ORB | 62 | -30.7 | +164.8 | +525.3 | +471.2 | +306.4 | +30.8 / +275.6 | 52 % | **FLIP+SL** |
| A+ Setup | 53 | -143.2 | -79.1 | -18.0 | -34.5 | +44.6 | -109.2 / +153.8 | 32 % | **FLIP+SL** |
| HTF EMA20 Touch - Pullback Entry | 50 | -233.8 | -301.8 | -297.4 | -332.8 | -31.0 | -76.0 / +45.0 | 18 % | **BRACKET** |
| Key Level Alert | 46 | +181.0 | +183.0 | +219.0 | +289.5 | +106.5 | +58.6 / +47.9 | 46 % | **FLIP ONLY** |
| Price Enters HTF EMA9/20 Zone | 45 | -378.4 | -319.4 | -367.0 | -367.0 | -47.6 | -14.6 / -33.0 | 18 % | **BRACKET+FLIP** |
| HTF EMA20 Pierce | 43 | -56.4 | -57.3 | +6.7 | -71.8 | -14.4 | +9.2 / -23.7 | 40 % | **FLIP+SL** |
| ORB Pass + | 35 | -116.5 | -2.6 | -67.3 | -114.8 | -112.2 | -19.5 / -92.6 | 54 % | **BRACKET+FLIP** |
| LTF EMA20 Touch - Pullback Entry | 18 | -91.1 | -61.7 | -61.8 | -42.0 | +19.7 | +19.8 / -0.0 | 28 % | **FLIP ONLY** |
| ORB Pass - | 16 | +3.9 | +65.8 | +277.2 | +277.2 | +211.5 | +17.2 / +194.3 | 56 % | **FLIP+SL** |
| VWAP Bounce - High R | 13 | +52.3 | +61.7 | +126.3 | +123.8 | +62.0 | -15.3 / +77.3 | 62 % | **FLIP+SL** |
| SETUP: LTF Pierce not beyond EMA9 | 13 | +5.7 | +20.1 | +9.8 | +1.5 | -18.6 | -68.3 / +49.7 | 38 % | **BRACKET+FLIP** |
| SETUP: LTF Pierce beyond EMA9 | 10 | -13.3 | +16.6 | +24.5 | +24.5 | +7.9 | -11.7 / +19.5 | 40 % | **FLIP+SL** |
| ALL live alerts (types with 10+) | 721 | -508.4 | +8.4 | +554.7 | +484.0 | +475.6 | -355.5 / +831.1 | 39 % | **FLIP+SL** |

## Replay Trade Setups Jan 5 -> now, by trigger (thirds Jan-Mar / Apr-Jul / Aug-Nov approx.)

| Trigger | Trades | Bracket (TP/SL only) | Bracket + flip (now) | Flip + SL | FLIP ONLY | Flip only vs now | ...by third | Flip-only win % | Best |
|---|---|---|---|---|---|---|---|---|---|
| LTF Pierce not beyond EMA9 | 124 | -89.3 | -160.1 | -268.9 | -260.8 | -100.7 | +49 / -7 / -143 | 28 % | **BRACKET** |
| HTF EMA9 Pierce | 97 | -99.2 | -41.5 | -165.3 | -172.8 | -131.2 | -65 / -23 / -43 | 32 % | **BRACKET+FLIP** |
| HTF CBC Flip | 90 | -155.9 | -177.7 | -54.6 | -71.2 | +106.5 | +121 / -29 / +15 | 38 % | **FLIP+SL** |
| LTF Pierce beyond EMA9 | 77 | -166.3 | -59.6 | -9.3 | -5.0 | +54.6 | +32 / +25 / -2 | 35 % | **FLIP ONLY** |
| HTF EMA20 Pierce | 70 | +120.7 | +109.1 | +102.2 | +111.0 | +1.9 | -11 / +61 / -48 | 39 % | **BRACKET** |
| LTF Pierce late | 48 | +80.5 | -45.6 | -76.1 | -68.0 | -22.4 | +12 / -48 / +14 | 35 % | **BRACKET** |
| ALL replay setups | 506 | -309.5 | -375.5 | -471.9 | -466.8 | -91.3 | +138 / -22 / -207 | 34 % | **BRACKET** |