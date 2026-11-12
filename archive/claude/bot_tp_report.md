MES 3m BOT exits: the bot closes its whole position at TP1 (bracket), so test TP rules with 100 % at TP1 -- 11/08/2026.
Bot setups only: 5-day short filter, proposed entry windows (1830-2200, 0300-0330, 0400-0600, 0630-0730, 0800-1300, 1400-1545),
net after costs (0.50 per trade, +0.25 for a rule exit at market).

| Bot exits | Trades | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Win % | Max DD | vs bot now: thirds |
|---|---|---|---|---|---|---|---|---|---|
| CBC chart exits (80/100 % by time + runner) — for reference | 884 | +139 | -335 | +95 | +268 | -102 | 49 % | 545 | -15 / -39 / -22  |
| BOT now: 100 % at TP1 1.75 ATR, no exit rule | 913 | +153 | -296 | +117 | +274 | -26 | 50 % | 517 | +0 / +0 / +0  |
| Bot + current exit rule (21 min -> 70 %, only ATR >= 1.5x avg), flatten ON | 918 | +156 | -272 | +100 | +253 | -15 | 50 % | 486 | +3 / +24 / -16  |
| Bot + TP1 -> 75 % after 12 min (all trades) | 929 | +78 | -246 | +60 | +208 | -109 | 54 % | 464 | -75 / +50 / -57  |
| Bot + TP1 -> 85 % after 12 min (all trades) | 925 | +129 | -257 | +96 | +242 | -32 | 52 % | 489 | -25 / +39 / -21  |
| Bot + TP1 -> 75 % after 15 min (all trades) | 929 | +74 | -232 | +58 | +205 | -101 | 53 % | 456 | -80 / +64 / -59  |
| Bot + TP1 -> 85 % after 15 min (all trades) | 924 | +136 | -263 | +83 | +236 | -45 | 52 % | 494 | -18 / +33 / -34  |
| Bot + TP1 -> 75 % after 18 min (all trades) | 928 | +120 | -217 | +58 | +211 | -38 | 53 % | 450 | -33 / +79 / -59  |
| Bot + TP1 -> 85 % after 18 min (all trades) | 924 | +163 | -257 | +80 | +239 | -14 | 52 % | 495 | +9 / +39 / -36  |
| Bot + TP1 -> 75 % after 21 min (all trades) | 928 | +138 | -219 | +62 | +218 | -18 | 53 % | 457 | -15 / +77 / -55  |
| Bot + TP1 -> 85 % after 21 min (all trades) | 923 | +158 | -259 | +71 | +244 | -29 | 51 % | 512 | +5 / +37 / -45  |
| Bot + TP1 -> 75 % after 24 min (all trades) | 927 | +139 | -211 | +45 | +219 | -28 | 53 % | 470 | -14 / +85 / -72  |
| Bot + TP1 -> 85 % after 24 min (all trades) | 922 | +163 | -256 | +57 | +241 | -35 | 51 % | 514 | +10 / +40 / -59  |
| Bot, TP1 1.25 ATR (no rule) | 937 | -21 | -180 | -22 | +158 | -223 | 57 % | 422 | -175 / +116 / -139  |
| Bot, TP1 1.50 ATR (no rule) | 928 | +99 | -225 | +69 | +219 | -57 | 54 % | 442 | -54 / +70 / -48  |
| Bot, TP1 2.00 ATR (no rule) | 900 | +159 | -296 | +157 | +284 | +19 | 47 % | 505 | +5 / -0 / +40  |
| Bot, TP1 2.50 ATR (no rule) | 874 | +61 | -239 | +167 | +316 | -12 | 42 % | 500 | -93 / +57 / +50  |