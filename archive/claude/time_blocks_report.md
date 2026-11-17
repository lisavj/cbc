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

- MES 3m: No new setups 16:00-19:00 → +45, z +1.5, thirds +7 / +34 / +4, last 4 wk +0, max DD 215 vs 249 (promising)
- MES 3m: End setups at 16:00 OFF → +74, z +1.9, thirds +21 / +32 / +21, last 4 wk +8, max DD 230 vs 249 (promising)
- MES 3m: No new setups 18:00-19:00 → +45, z +1.5, thirds +7 / +34 / +4, last 4 wk +0, max DD 215 vs 249 (promising)
- MES 3m: No new setups 13:00-14:00 → +112, z +1.7, thirds +12 / +61 / +39, last 4 wk +32, max DD 199 vs 249 (promising)
- MES 3m: No new setups 14:00-15:00 → +69, z +1.1, thirds +0 / +54 / +14, last 4 wk +0, max DD 219 vs 249 (promising)

## MES 3m -- base (v1.06, colour check ON): 825 setups, net +518, thirds +307 / -174 / +385, last 4 wk +173, max DD 249

Without the colour check (= earlier replays): 828 setups, net +519. By trigger (base): Flip 113 / +371 · LTF20 521 / +89 · HTF9 168 / -4 · HTF20 23 / +61

| Change (one at a time) | Setups | Net | Δ vs base | z | Δ by third | Δ last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| No new setups 16:00-18:00 | 857 | +539 | +22 | +0.4 | -0 / -13 / +35 | +20 | 261 | noise |
| No new setups 16:00-18:30 (old replay value) | 832 | +516 | -1 | -0.1 | +2 / -1 / -2 | +0 | 249 | worse |
| No new setups 16:00-19:00 | 815 | +563 | +45 | +1.5 | +7 / +34 / +4 | +0 | 215 | promising |
| No new setups 16:00-19:30 | 792 | +548 | +31 | +0.6 | -12 / +36 / +7 | +9 | 199 | noise |
| No new setups 16:00-20:00 | 770 | +545 | +27 | +0.4 | -17 / +36 / +9 | +14 | 196 | noise |
| No new setups window OFF | 889 | +554 | +36 | +0.5 | -3 / +5 / +34 | +20 | 253 | noise |
| OR forming block NY OFF | 847 | +508 | -10 | -0.2 | -8 / -58 / +56 | +25 | 288 | worse |
| OR forming block London OFF | 849 | +496 | -22 | -0.4 | +13 / -19 / -16 | -12 | 268 | worse |
| OR forming block Asia OFF | 848 | +517 | -1 | -0.0 | -13 / +5 / +7 | +1 | 246 | worse |
| OR forming blocks all OFF | 894 | +485 | -32 | -0.4 | -8 / -71 / +47 | +15 | 304 | worse |
| Inside OR after set: NY ON | 756 | +538 | +20 | +0.2 | +1 / +76 / -56 | -56 | 178 | noise |
| Inside OR after set: London ON | 762 | +497 | -21 | -0.3 | -33 / +14 / -2 | +15 | 239 | worse |
| Inside OR after set: Asia ON | 733 | +475 | -43 | -0.5 | -22 / -11 / -10 | -23 | 249 | worse |
| End setups at 16:00 OFF | 825 | +591 | +74 | +1.9 | +21 / +32 / +21 | +8 | 230 | promising |
| No new setups 18:00-19:00 | 815 | +563 | +45 | +1.5 | +7 / +34 / +4 | +0 | 215 | promising |
| No new setups 19:00-20:00 | 780 | +500 | -18 | -0.3 | -25 / +2 / +5 | +14 | 230 | worse |
| No new setups 20:00-21:00 | 808 | +522 | +4 | +0.1 | -14 / +19 / -1 | -7 | 223 | noise |
| No new setups 21:00-22:00 | 785 | +461 | -57 | -0.9 | +12 / -14 / -55 | -14 | 255 | worse |
| No new setups 22:00-23:00 | 805 | +544 | +26 | +0.5 | +19 / +9 / -1 | +1 | 238 | noise |
| No new setups 23:00-00:00 | 789 | +518 | +1 | +0.0 | -19 / +2 / +18 | +9 | 245 | noise |
| No new setups 00:00-01:00 | 780 | +434 | -84 | -1.1 | +14 / -85 / -13 | -8 | 324 | worse |
| No new setups 01:00-02:00 | 778 | +481 | -36 | -0.5 | -59 / +23 / +0 | +21 | 221 | worse |
| No new setups 02:00-03:00 | 767 | +528 | +11 | +0.1 | +8 / -16 / +18 | +5 | 254 | noise |
| No new setups 03:00-04:00 | 809 | +508 | -9 | -0.2 | +7 / -6 / -10 | +0 | 250 | worse |
| No new setups 04:00-05:00 | 798 | +493 | -24 | -0.4 | -11 / +7 / -20 | -4 | 253 | worse |
| No new setups 05:00-06:00 | 795 | +498 | -20 | -0.4 | +9 / -5 / -24 | -13 | 259 | worse |
| No new setups 06:00-07:00 | 787 | +478 | -40 | -0.6 | -17 / -9 / -14 | -1 | 246 | worse |
| No new setups 07:00-08:00 | 799 | +536 | +18 | +0.3 | +9 / -3 / +12 | +0 | 255 | noise |
| No new setups 08:00-09:00 | 774 | +385 | -132 | -1.9 | -97 / +17 / -52 | -27 | 241 | worse |
| No new setups 09:00-10:00 | 795 | +313 | -205 | -3.9 | -34 / -36 / -135 | -1 | 295 | robustly worse |
| No new setups 10:00-11:00 | 787 | +431 | -87 | -1.4 | -67 / -11 / -8 | -16 | 261 | worse |
| No new setups 11:00-12:00 | 791 | +340 | -177 | -2.9 | +13 / +1 / -192 | -144 | 226 | worse |
| No new setups 12:00-13:00 | 783 | +563 | +45 | +0.7 | -22 / +70 / -3 | -14 | 203 | noise |
| No new setups 13:00-14:00 | 792 | +630 | +112 | +1.7 | +12 / +61 / +39 | +32 | 199 | promising |
| No new setups 14:00-15:00 | 788 | +587 | +69 | +1.1 | +0 / +54 / +14 | +0 | 219 | promising |
| No new setups 15:00-16:00 | 781 | +505 | -13 | -0.2 | -44 / +44 / -13 | -23 | 240 | worse |

## MGC 3m -- base (v1.06, colour check ON): 627 setups, net +1164, thirds +564 / +82 / +517, last 4 wk +279, max DD 117

Without the colour check (= earlier replays): 627 setups, net +1164. By trigger (base): Flip 60 / +11 · LTF20 406 / +818 · HTF9 118 / +154 · HTF20 43 / +181

| Change (one at a time) | Setups | Net | Δ vs base | z | Δ by third | Δ last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| No new setups 16:00-18:00 | 673 | +1158 | -6 | -0.0 | +54 / -14 / -46 | -10 | 122 | worse |
| No new setups 16:00-18:30 (old replay value) | 634 | +1136 | -28 | -0.4 | -19 / -3 / -6 | -0 | 121 | worse |
| No new setups 16:00-19:00 | 611 | +1208 | +45 | +0.5 | +21 / +16 / +7 | +2 | 114 | noise |
| No new setups 16:00-19:30 | 582 | +1036 | -127 | -1.0 | -19 / -11 / -98 | -105 | 109 | worse |
| No new setups 16:00-20:00 | 550 | +872 | -291 | -1.8 | -64 / +30 / -257 | -105 | 102 | worse |
| No new setups window OFF | 686 | +1127 | -37 | -0.3 | +22 / -25 / -34 | -10 | 127 | worse |
| OR forming block NY OFF | 646 | +1194 | +30 | +0.4 | -22 / +41 / +11 | +11 | 118 | noise |
| OR forming block London OFF | 647 | +1162 | -2 | -0.0 | -25 / +10 / +13 | -3 | 122 | worse |
| OR forming block Asia OFF | 655 | +1201 | +37 | +0.3 | +62 / +30 / -54 | +0 | 128 | noise |
| OR forming blocks all OFF | 694 | +1229 | +65 | +0.4 | +14 / +81 / -30 | +9 | 134 | noise |
| Inside OR after set: NY ON | 570 | +997 | -166 | -1.2 | -136 / -47 / +17 | +0 | 116 | worse |
| Inside OR after set: London ON | 558 | +1175 | +11 | +0.1 | +13 / +25 / -26 | -18 | 107 | noise |
| Inside OR after set: Asia ON | 527 | +743 | -421 | -2.3 | -343 / -3 / -75 | -68 | 114 | robustly worse |
| End setups at 16:00 OFF | 627 | +1148 | -15 | -0.3 | -7 / -8 / -0 | +0 | 117 | worse |
| No new setups 18:00-19:00 | 610 | +1211 | +48 | +0.6 | +21 / +16 / +10 | +2 | 114 | noise |
| No new setups 19:00-20:00 | 570 | +839 | -325 | -2.3 | -86 / +29 / -268 | -107 | 105 | worse |
| No new setups 20:00-21:00 | 607 | +1171 | +8 | +0.1 | +10 / +23 / -25 | +2 | 102 | noise |
| No new setups 21:00-22:00 | 577 | +1186 | +23 | +0.2 | +14 / +47 / -38 | +7 | 111 | noise |
| No new setups 22:00-23:00 | 591 | +1083 | -81 | -0.7 | -49 / -29 / -3 | +4 | 138 | worse |
| No new setups 23:00-00:00 | 592 | +1183 | +19 | +0.2 | -0 / -17 / +36 | -9 | 104 | noise |
| No new setups 00:00-01:00 | 598 | +997 | -167 | -1.8 | +6 / -28 / -144 | -105 | 113 | worse |
| No new setups 01:00-02:00 | 592 | +1094 | -70 | -0.6 | -12 / -63 / +5 | +9 | 153 | worse |
| No new setups 02:00-03:00 | 599 | +836 | -328 | -3.5 | -261 / -11 / -57 | -8 | 118 | robustly worse |
| No new setups 03:00-04:00 | 613 | +1190 | +26 | +0.3 | +23 / +10 / -7 | +0 | 117 | noise |
| No new setups 04:00-05:00 | 604 | +1205 | +42 | +0.4 | +19 / +24 / -1 | -2 | 122 | noise |
| No new setups 05:00-06:00 | 604 | +1210 | +46 | +0.5 | +40 / -0 / +7 | -1 | 104 | noise |
| No new setups 06:00-07:00 | 608 | +1154 | -10 | -0.1 | +7 / -39 / +22 | +5 | 104 | worse |
| No new setups 07:00-08:00 | 605 | +982 | -181 | -2.2 | -156 / +13 / -38 | -43 | 100 | worse |
| No new setups 08:00-09:00 | 585 | +1133 | -30 | -0.3 | -12 / +2 / -21 | -41 | 121 | worse |
| No new setups 09:00-10:00 | 615 | +1173 | +9 | +0.1 | +15 / -2 / -4 | -14 | 102 | noise |
| No new setups 10:00-11:00 | 594 | +1141 | -22 | -0.2 | -39 / -2 / +19 | -3 | 118 | worse |
| No new setups 11:00-12:00 | 607 | +985 | -179 | -2.3 | -142 / -37 / -0 | +0 | 111 | robustly worse |
| No new setups 12:00-13:00 | 613 | +1211 | +47 | +0.7 | +23 / +7 / +17 | +5 | 117 | noise |
| No new setups 13:00-14:00 | 615 | +1176 | +13 | +0.2 | +13 / +1 / -2 | +0 | 117 | noise |
| No new setups 14:00-15:00 | 613 | +1149 | -14 | -0.2 | -26 / +6 / +6 | +4 | 117 | worse |
| No new setups 15:00-16:00 | 616 | +1170 | +6 | +0.1 | +11 / -3 / -1 | +0 | 103 | noise |

## MES 3m combinations (time_combo.py)

| Change | Setups | Net | Δ vs base | z | Δ by third | Δ last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Block 13:00-15:00 | 749 | +691 | +173 | +2.0 | +19 / +101 / +53 | +36 | 169 | promising |
| Window 16:00-19:00 + block 13:00-14:00 | 782 | +674 | +157 | +2.2 | +19 / +95 / +43 | +32 | 165 | robust |
| Window 16:00-19:00 + block 13:00-15:00 | 739 | +736 | +218 | +2.4 | +26 / +135 / +57 | +36 | 135 | robust |
| Window 16:00-19:00 + End 16:00 OFF | 815 | +636 | +119 | +2.4 | +28 / +65 / +25 | +8 | 196 | robust |
| Window 16:00-19:00 + block 13:00-14:00 + End 16:00 OFF | 782 | +748 | +230 | +2.8 | +40 / +126 / +64 | +39 | 155 | robust |
| Window 16:00-19:00 + block 13:00-15:00 + End 16:00 OFF | 739 | +809 | +291 | +2.9 | +47 / +166 / +78 | +44 | 142 | robust |
| Block 12:00-15:00 | 705 | +724 | +206 | +1.9 | -19 / +174 / +51 | +22 | 123 | noise |

## Verdict (11/14/2026)

- MES 3m, robust combination: "No new setups between" 16:00-19:00 (live 16:00-18:45) + no new setups 13:00-15:00 + "End setups at 16:00" OFF = +291, z 2.9, thirds +47 / +166 / +78, last 4 wk +44, max DD 142 vs 249. Each part alone is promising (18:00-19:00 +45 z 1.5; 13-14 +112 z 1.7; 14-15 +69 z 1.1; End OFF +74 z 1.9).
- Caveat: 24 one-hour blocks were tried per chart, so one or two "promising" hours can be luck. 13:00-15:00 has independent support: live C-006 (13-15 22 setups -82.2, both halves) and the bot already skips 13:00-15:00 (bot_win), so the bot is unaffected by this change.
- How: window 16:00-19:00 and End 16:00 OFF are chart inputs (End OFF on MES only: MGC -15). A 13:00-15:00 block needs a Pine change (only one "No new setups" window exists) -- e.g. a per-symbol list "MES 3m 1300-1500".
- MGC 3m: keep all current time blocks. Nothing promising; Inside OR after set Asia (-421) and blocks 02-03 / 11-12 robustly worse. 16:00-19:00 +45 (noise, all thirds +) -- harmless if the default changes.
- Base note: with the live window on candle OPEN time (16:00-18:45), base = MES 825 / +518, MGC 627 / +1164 (earlier replays 16:00-18:30 on close time: +532 / +1135).

## MGC 3m combined blocks (mgc_blocks.py, 11/14) -- base 627 / +1164

| Change | Setups | Net | Δ vs base | z | Δ by third | Δ last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Block 12:00-16:00 | 570 | +1228 | +64 | +0.5 | +28 / +15 / +21 | +10 | 102 | noise |
| Block 12:00-13:00 + 18:00-19:00 | 596 | +1259 | +95 | +0.9 | +45 / +23 / +27 | +7 | 114 | noise |
| Block 12:00-13:00 | 613 | +1211 | +47 | +0.7 | +23 / +7 / +17 | +5 | 117 | noise |
| Block 18:00-19:00 | 610 | +1211 | +48 | +0.6 | +21 / +16 / +10 | +2 | 114 | noise |
| Block 12:00-14:00 | 600 | +1224 | +60 | +0.6 | +36 / +8 / +16 | +5 | 116 | noise |
| Block 13:00-16:00 | 585 | +1180 | +16 | +0.1 | +5 / +7 / +4 | +5 | 102 | noise |
| Block 12:00-16:00 + 18:00-19:00 | 553 | +1275 | +112 | +0.7 | +49 / +31 / +31 | +11 | 99 | noise |
| Block 12:00-13:00 + 18:00-19:00 + 04:00-06:00 | 546 | +1363 | +200 | +1.2 | +107 / +53 / +40 | +11 | 101 | promising |

MGC verdict: no change. Every combination is positive in all thirds but z <= 0.9, except the 4-hour pick (04-06 + 12-13 + 18-19: +200, z 1.2) -- those are the four best of 22 hours tried, so in-sample selection, not evidence. 12:00-16:00 (+64, z 0.5, DD 102 vs 117) is the only block with a reason beyond the data (NY afternoon loses in every third, sessions_report) -- watch, re-run monthly.
