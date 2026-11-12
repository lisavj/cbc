## Week of 11/09/2026 summary

- STUDY SETTINGS STALE: the 11/08 settings sync report lists 1 non-known MISMATCH (chop_sim GATE MGC 2m range gate R5=0) + late_study MES 3m tp=2.0 -- both already fixed in the project scripts used for this run, and neither affects these 3m studies.
- Current (bot windows 1830-2200 / 0300-1300 / 1500-1530, CBC chart exits): **-531** (thirds +29 / -459 / -101, last 4 wk +150, max DD 794) vs 11/08 -506.
- 5-day short filter (live in bot since v10.86): **-287**, beyond random **-1** / +71 / +63, last 4 wk +149 vs +150, max DD 564 -> **WEAKER** (third 1 a hair below 0 and last 4 wk 1 pt below current; not clearly negative, so not FAILED; keep the filter on). **Bot short filter: weeks held 0/3.**
- TP1 -> 85 % after 18 min -446 (+39 / +38 / +28, last 4 wk +129); Filter + TP rule -258; Balanced filter + losing-stretch stop + SL rule -111 (-69 / +190 / +115, last 4 wk +151, max DD 334).
- Windows note: setups closing 13:00-14:00 (removed in v10.87) still lose in the replay: 88 trades, -242 after costs, every third negative (-47 / -123 / -71; 13:30-14:00 -135) -> removal still right.

---

# MES 3m bot-window check — run 11/09/2026

Replay of MES 3m setups that START inside the bot entry windows (candle close 18:30-22:00, 03:00-13:00, 15:00-15:30 ET = v10.87 bot windows), live MES 3m exits, net after costs (0.50 pts per trade, +0.25 for a rule exit). Brackets = gain beyond dropping the same number of trades at random. Bot trigger choices are not modelled.

| Rule set (bot windows only) | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | PF | Max DD |
|---|---|---|---|---|---|---|---|---|
| Current exits | +29 (+0) | -459 (+0) | -101 (+0) | +150 (+0) | -531 (+0) | 1108 | 0.86 | 794 |
| TP1 -> 85 % after 18 min | +62 (+39) | -427 (+38) | -81 (+28) | +129 (-19) | -446 (+105) | 1150 | 0.88 | 717 |
| SL: half SL1 if negative at 18 min | +18 (-10) | -463 (-2) | -69 (+38) | +152 (+3) | -514 (+27) | 1129 | 0.86 | 778 |
| TP + SL rules | +60 (+38) | -437 (+31) | -68 (+46) | +115 (-31) | -446 (+115) | 1169 | 0.88 | 720 |
| 5-day short filter | +57 (-1) | -343 (+71) | -2 (+63) | +149 (-5) | -287 (+132) | 875 | 0.90 | 564 |
| Filter + TP rule | +72 (+20) | -304 (+115) | -27 (+41) | +124 (-28) | -258 (+176) | 907 | 0.91 | 540 |
| Balanced: filter + losing-stretch stop + SL rule | -2 (-69) | -193 (+190) | +84 (+115) | +151 (-1) | -111 (+236) | 725 | 0.95 | 334 |
| Filter + losing-stretch stop + TP rule | -4 (-67) | -220 (+167) | +63 (+96) | +118 (-34) | -160 (+196) | 743 | 0.93 | 366 |
