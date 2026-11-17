① Auto Trade Setup inputs not studied before -- MES 3m and MGC 3m on the CBC EMA Slope branch (v1.05) -- 11/14/2026.
One change at a time on top of each chart's branch settings. Replay Jan 5 -> now (BarFeed / Databento bars, TV EMA20), net after costs
(MES 0.50, MGC 0.22). Entry filters are entry filters: a skipped setup can change later setups (cooldown, one-per-direction).
MES 3m base: ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR, HTF EMA20 slope >= 0.42 ATR; SL1 3 ATR min 5, TP1 1.75, 100 % at TP1;
  HTF CBC Flip setups ride to the HTF flip back / SL1 / 16:00 / next setup.
MGC 3m base: same filters with slope >= 0.30 + VWAP stretch 4 ATR; SL1 1.7 ATR min 5 cap 7, TP1 1.7 cap 6, 0 % at TP1 + BE, closed by the HTF flip.
Both: flip gates as live (close <= max(2 ATR, 8 pts) from the 3m EMA20 -- the replay engine has always used 8 pts for MGC too, live is 10;
  close beyond VWAP and EMA200 by 1 pt; VWAP slope agrees; flip ER >= 0.23); per-trigger ER mins LTF 0.08 / HTF 0.15; VWAP reclaim block 5 bars;
  min 10 candles between setups; skip a new setup while the same-direction one runs; ATR 14; setups end at 16:00.
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, better in all three thirds, last 4 wk >= 0; promising = z >= 1 and all thirds.
Not modelled: pivot reclaim block (R2/R3/S2/S3 not in the bar feed), TP/SL steps (pivot levels; ATR method is live), closed-15m-values mode,
act-on-flip-at-HTF-close, toward flips (studied 11/03), OR blocks (orb_all), min SL / SL / TP / trail / caps / time stop (other studies).

## Candidates (promising or better)

- MES 3m: LTF pierce late window 2 → +47, z +1.1, thirds +16 / +4 / +27, last 4 wk +5, max DD 254 vs 254 (promising)

## MES 3m -- base (v1.06, colour check ON): 833 setups, net +532, thirds +308 / -160 / +384, last 4 wk +173, max DD 254

Without the colour check (= earlier replays): 836 setups, net +533. By trigger (base): Flip 117 / +349 · LTF20 525 / +101 · HTF9 168 / +20 · HTF20 23 / +61

| Change (one at a time) | Setups | Net | Δ vs base | z | Δ by third | Δ last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Trigger HTF CBC Flip OFF | 763 | +191 | -341 | -2.9 | +29 / -26 / -344 | -108 | 296 | worse |
| Trigger LTF EMA20 Pierce OFF | 436 | +517 | -15 | -0.1 | -69 / +55 / -1 | -30 | 142 | worse |
| Trigger HTF EMA9 Pierce OFF | 679 | +509 | -23 | -0.2 | -95 / +122 / -50 | -12 | 160 | worse |
| Trigger HTF EMA20 Pierce OFF | 811 | +474 | -58 | -1.2 | -29 / -10 / -19 | -19 | 257 | worse |
| HTF EMA9 + EMA20 Pierce both OFF | 649 | +438 | -94 | -0.7 | -130 / +99 / -62 | -31 | 166 | worse |
| LTF pierce late window 0 | 787 | +546 | +14 | +0.2 | -24 / +19 / +19 | +10 | 235 | noise |
| LTF pierce late window 2 | 848 | +579 | +47 | +1.1 | +16 / +4 / +27 | +5 | 254 | promising |
| HTF pierce late window 0 | 815 | +528 | -4 | -0.1 | -6 / +14 / -13 | -18 | 240 | worse |
| HTF pierce late window 2 | 839 | +537 | +5 | +0.2 | +0 / +1 / +5 | +5 | 260 | noise |
| HTF pierce late window 3 | 841 | +526 | -6 | -0.2 | -5 / +1 / -1 | +5 | 260 | worse |
| HTF late confirm: trade-color candle OFF | 836 | +533 | +2 | +0.1 | +0 / +1 / +0 | +0 | 252 | noise |
| HTF EMA9/EMA20 Pierce replaces the current setup ON | 837 | +556 | +24 | +1.3 | -3 / -6 / +32 | +26 | 255 | noise |
| HTF pierce: also require close beyond LTF EMA9/20 (intended rule) | 690 | +566 | +34 | +0.3 | -72 / +110 / -3 | +0 | 157 | noise |
| HTF CBC Flip: require a pullback first, wait 10, two-step | 798 | +113 | -418 | -2.9 | -2 / -57 / -360 | -128 | 338 | robustly worse |
| ... wait 10, same candle (two-step OFF) | 777 | +95 | -437 | -3.2 | -25 / -67 / -345 | -109 | 338 | robustly worse |
| ... wait 5, two-step | 790 | +201 | -331 | -2.4 | +45 / -44 / -332 | -121 | 310 | worse |
| ... wait 20, two-step | 799 | +133 | -398 | -2.7 | -2 / -43 / -353 | -128 | 348 | robustly worse |

## MGC 3m -- base (v1.06, colour check ON): 634 setups, net +1135, thirds +545 / +78 / +512, last 4 wk +279, max DD 121

Without the colour check (= earlier replays): 634 setups, net +1135. By trigger (base): Flip 62 / +7 · LTF20 408 / +806 · HTF9 121 / +142 · HTF20 43 / +181

| Change (one at a time) | Setups | Net | Δ vs base | z | Δ by third | Δ last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Trigger HTF CBC Flip OFF | 594 | +1111 | -24 | -0.2 | +56 / +33 / -113 | +4 | 107 | worse |
| Trigger LTF EMA20 Pierce OFF | 338 | +844 | -292 | -0.9 | -158 / -38 / -96 | -166 | 73 | worse |
| Trigger HTF EMA9 Pierce OFF | 545 | +1062 | -73 | -0.4 | +67 / -24 / -116 | -68 | 114 | worse |
| Trigger HTF EMA20 Pierce OFF | 597 | +961 | -174 | -1.5 | -36 / -11 / -128 | -53 | 133 | worse |
| HTF EMA9 + EMA20 Pierce both OFF | 497 | +876 | -259 | -1.1 | +1 / -27 / -234 | -121 | 117 | worse |
| LTF pierce late window 0 | 597 | +1182 | +46 | +0.4 | -2 / +39 / +9 | +18 | 113 | noise |
| LTF pierce late window 2 | 646 | +1187 | +52 | +0.6 | +25 / +13 / +15 | -8 | 122 | noise |
| HTF pierce late window 0 | 615 | +1166 | +30 | +0.4 | +14 / +4 / +12 | +2 | 112 | noise |
| HTF pierce late window 2 | 641 | +1179 | +43 | +0.9 | +12 / +10 / +21 | -3 | 119 | noise |
| HTF pierce late window 3 | 641 | +1179 | +43 | +0.9 | +12 / +10 / +21 | -3 | 119 | noise |
| HTF late confirm: trade-color candle OFF | 634 | +1135 | +0 | +0.0 | +0 / +0 / +0 | +0 | 121 | noise |
| HTF EMA9/EMA20 Pierce replaces the current setup ON | 645 | +1163 | +28 | +0.5 | +3 / -0 / +25 | +0 | 127 | noise |
| HTF pierce: also require close beyond LTF EMA9/20 (intended rule) | 529 | +1064 | -72 | -0.4 | +3 / -13 / -61 | -0 | 120 | worse |
| HTF CBC Flip: require a pullback first, wait 10, two-step | 606 | +1084 | -52 | -0.3 | +47 / +28 / -126 | +4 | 114 | worse |
| ... wait 10, same candle (two-step OFF) | 601 | +1120 | -15 | -0.1 | +70 / +36 / -121 | +4 | 107 | worse |
| ... wait 5, two-step | 604 | +1083 | -53 | -0.3 | +47 / +28 / -128 | +4 | 114 | worse |
| ... wait 20, two-step | 608 | +1083 | -52 | -0.3 | +47 / +27 / -126 | +4 | 114 | worse |

## Neighbour check, MES 3m LTF late window

| LTF late window | Δ vs 1 | z | Δ by third | Δ last 4 wk |
|---|---|---|---|---|
| 0 | +14 | +0.2 | -24 / +19 / +19 | +10 |
| 2 | +47 | +1.1 | +16 / +4 / +27 | +5 |
| 3 | +38 | +0.8 | +18 / -10 / +29 | +5 |
| 4 | +25 | +0.5 | +18 / -15 / +22 | -1 |

## Verdict (11/14/2026)

- Keep every trigger ON on both charts. HTF CBC Flip is the biggest earner on MES 3m with the flip ride (117 setups / +349; OFF -341, z -2.9); LTF EMA20 Pierce is MGC's (408 / +806; OFF -292). Turning off HTF EMA9 Pierce on MES (promising on the old settings) is now slightly worse (-23): the slope filter already removed its losers.
- "HTF CBC Flip: require a pullback first" stays OFF: MES -418 (robustly worse, z -2.9) at wait 10, -331 to -437 for every wait / two-step setting; MGC -15 to -53.
- MES 3m LTF pierce late window 2: +47, z 1.1, all thirds positive = promising but small, and neighbours are noise (3: +38 with the middle third -10; 4: +25). The earlier late-window study (old settings) had 2 worse than 1. Not enough to change; watch.
- Everything else is noise: HTF late window 0 / 2 / 3, trade-color candle OFF (+2 / +0), "replaces the current setup" ON (MES +24 z 1.3 but thirds -3 / -6 / +32).
- CODE NOTE: "HTF pierce: also require close beyond LTF EMA9/20" does nothing on its own. In CBC the trigger uses ema_clear_long, and ESLib2 f_clr makes that TRUE whenever "Require price past both EMA clouds" is OFF, so the box only works with that rule ON. The row above tests the intended rule: MES +34 (thirds -72 / +110 / -3, noise), MGC -72. No reason to fix it now.
- Base now includes the live trade-color check on HTF late confirms: MES 833 / +532 vs 836 / +533 without it, MGC unchanged -- the earlier replays were effectively right.

## ⑤ Alerts "Pierce/Touch: pullbacks only" OFF (pbo_study.py, 11/14)

This alert-group box also gates LTF EMA20 Pierce / HTF EMA9-20 Pierce / EMA20 Touch setups (ltf_from_above / f_ats_hep pbo). OFF = a pierce also counts when the previous candle was on the wrong side of the line (only "previous candle did not touch it" remains).
- MES 3m: 843 setups, +505, Δ -27, z -0.7, thirds -6 / +4 / -26, last 4 wk -22 -> worse.
- MGC 3m: 651 setups, +1133, Δ -2, z 0.0, thirds -29 / +36 / -9, last 4 wk -4 -> worse.
Keep ON. Also note: "Alert: LTF EMA20 Pierce - Entry" must stay ON -- the LTF EMA20 Pierce setup trigger needs it (ltf_pierce_ready); the "LTF EMA20 Pierce: cooldown bars" alert input (3) also changes setups.

## ⑤ Alerts "LTF EMA20 Pierce: cooldown bars" (live 3; gates the LTF pierce trigger) -- lcd_study.py, 11/14

| Cooldown | MES 3m Δ | z | thirds | last 4 wk | MGC 3m Δ | z | thirds | last 4 wk |
|---|---|---|---|---|---|---|---|---|
| 0 bars | -14 | -0.2 | +14 / -28 / +0 | +9 | +40 | +0.4 | +2 / +39 / -1 | -5 |
| 1 bars | -14 | -0.2 | +14 / -28 / +0 | +9 | +40 | +0.4 | +2 / +39 / -1 | -5 |
| 2 bars | -45 | -1.0 | -13 / -25 / -7 | +0 | -18 | -0.2 | +0 / -9 / -9 | -5 |
| 4 bars | +2 | +0.1 | +1 / -6 / +7 | +10 | -8 | -0.2 | +2 / -10 / +0 | +0 |
| 5 bars | +43 | +0.8 | +16 / -0 / +28 | +4 | -65 | -0.8 | -15 / -43 / -7 | -7 |
| 6 bars | +6 | +0.1 | -2 / -3 / +10 | -6 | -94 | -1.0 | -15 / -61 / -18 | -19 |
| 8 bars | -13 | -0.2 | -11 / -6 / +4 | -4 | -84 | -0.8 | -27 / -44 / -13 | -19 |
| 10 bars | -6 | -0.1 | +6 / +2 / -15 | -9 | -68 | -0.6 | -14 / -44 / -10 | -19 |

Keep 3 on both (0 and 1 replay the same: a pierce needs the previous candle off the line). MES 5 = +43 z 0.8 and MGC 0/1 = +40 z 0.4: noise, neighbours disagree. HTF Pullback - Structure Confirmed (alert box + recent flip window 4) cannot be replayed (HTF HH/HL structure not in the bar feed). Alert hours / sessions do not change setups or results (bot follows its own windows).
