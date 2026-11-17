## Week of 11/14/2026 summary

- STUDY SETTINGS STALE: the 11/13 settings sync (v10.96) lists 3 non-known MISMATCHes, NOT yet fixed in the project scripts, and they touch the 3m studies -- mes3_ema_grid LIVE still closes MES 3m 80/100 % by time of day (live since v10.95: 100 % at TP1 all day), and MGC 3m live is now FLIP 0 % (v10.96: nothing closed at TP1, BE, no trail, exit on HTF flip) while these replays use 80 % / trail 1.7 (MGCX) or 50 % / 3.5. Bot replay (H) is unaffected (part 1.0). Also new: the 11/14 X4 fix in mes3_ema_grid.py makes the MGC 3m VWAP-stretch gate actually block setups (MGC 3m 1193 setups vs 1707 last week), so MGC 3m numbers are not like-for-like with 11/09. (This study uses bot exits = 100 % at TP1 and is not affected.) Current bot set = Flip + LTF beyond EMA9 + LTF NOT beyond EMA9 (v10.88, data note 4).
- Current bot set replay **-253** (thirds -81 / -203 / +31, last 4 wk +118), ranks 61 of 63; no combination positive in all thirds.
- Watch "turn ON HTF EMA20 Pierce (incl. late)": **Δ +72** (Δ thirds +125 / -27 / -26, last 4 wk -16); live in bot windows 5 / +10.5 -> not qualifying. **Bot HTF EMA20 Pierce: weeks qualifying 0/3.**
- Current triggers: HTF Flip replay thirds -93 / -67 / +36 (live in windows 13 / +43.1); LTF beyond EMA9 +87 / -94 / -17 (live 7 / +4.6) -- neither negative in all three thirds -> keep.
- New watch (data note 4) "LTF EMA20 Pierce (not beyond EMA9)": replay thirds -75 / -42 / +13 (negative in 2 of 3), live in bot windows 23 / +15.4 (CBC chart exits, since 10/19) -- run 1 of 3; turning it OFF would be Δ +105 (thirds +75 / +42 / -13, last 4 wk -97). Not yet a flag.
- Verdict: keep bot triggers as is.

---

MES 3m BOT trigger checkboxes -- which setup types should the bot take? -- 11/08/2026.
REPLAY: all CBC setups (every trigger on, as CBC draws them), then the bot takes only setups whose trigger is ticked, inside the v10.87
windows (candle close 18:30-22:00, 03:00-13:00, 15:00-15:30 ET) with the 5-day short filter; bot exits = 100 % at TP1 1.75 ATR, SL1 3 ATR,
CBC setup end / 16:00. Net after costs (0.50 per trade). LIVE: real MES 3m Trade Setup -> Setup Ended pairs since 10/19 (CBC chart exits,
not bot exits), same windows + short filter.

## 1. Every trigger type (replay Jan 5 -> Nov 6 + live since 10/19)

| Trigger (bot checkbox) | Bot now | Replay trades | Replay net | Win % | Avg | Thirds | Last 4 wk | Live (bot windows) n / net / avg | Live all hours n / net |
|---|---|---|---|---|---|---|---|---|---|
| HTF CBC Flip | ON | 151 | -125 | 55 % | -0.83 | -93 / -67 / +36 | +35 | 13 / +43.1 / +3.31 | 16 / +23.0 |
| LTF EMA20 Pierce (closed beyond EMA9) | ON | 110 | -24 | 52 % | -0.21 | +87 / -94 / -17 | -14 | 7 / +4.6 / +0.65 | 16 / -13.6 |
| LTF EMA20 Pierce (not beyond EMA9) | ON | 219 | -105 | 42 % | -0.48 | -75 / -42 / +13 | +97 | 23 / +15.4 / +0.67 | 32 / -6.9 |
| LTF EMA20 Pierce (late confirm) | off | 100 | +7 | 56 % | +0.07 | +2 / +7 / -3 | +20 | 17 / -2.4 / -0.14 | 20 / -21.1 |
| HTF EMA9 Pierce | off | 195 | -28 | 47 % | -0.14 | +30 / -89 / +32 | +9 | 9 / +20.1 / +2.23 | 12 / +10.6 |
| HTF EMA9 Pierce (late) | off | 16 | +17 | 56 % | +1.08 | +16 / +9 / -8 | +4 | 2 / -5.9 / -2.94 | 2 / -5.9 |
| HTF EMA20 Pierce | off | 112 | +65 | 50 % | +0.58 | +125 / -27 / -33 | -21 | 3 / +4.5 / +1.48 | 5 / -5.8 |
| HTF EMA20 Pierce (late) | off | 3 | +7 | 67 % | +2.32 | +0 / +0 / +7 | +5 | 2 / +6.0 / +3.00 | 3 / +0.8 |
| HTF Pullback Structure | off | (not in replay) | | | | | | 0 / +0.0 / +0.00 | 2 / -9.1 |

## 2. Turning one checkbox on / off (replay, bot exits, after costs; Δ vs the current bot set Flip + LTF beyond + not beyond EMA9 (v10.88) = -253, thirds -81 / -203 / +31, last 4 wk +118)

| Change | Trades | Net | Δ | Δ by third | Δ last 4 wk | Better in all thirds |
|---|---|---|---|---|---|---|
| turn OFF Trigger: HTF CBC Flip | 329 | -128 | +125 | +93 / +67 / -36 | -35 |  |
| turn OFF Trigger: LTF EMA20 Pierce (closed beyond EMA9) | 370 | -230 | +24 | -87 / +94 / +17 | +14 |  |
| turn OFF Trigger: LTF EMA20 Pierce (not beyond EMA9) | 261 | -149 | +105 | +75 / +42 / -13 | -97 |  |
| turn ON Trigger: LTF EMA20 Pierce (late confirm) | 580 | -246 | +7 | +2 / +7 / -3 | +20 |  |
| turn ON Trigger: HTF EMA9 Pierce (incl. late) | 691 | -264 | -10 | +46 / -80 / +24 | +12 |  |
| turn ON Trigger: HTF EMA20 Pierce (incl. late) | 595 | -181 | +72 | +125 / -27 / -26 | -16 |  |

## 3. Best checkbox combinations (replay, all 63)

| Checkboxes ON | Trades | Net | Thirds | Last 4 wk | All thirds positive |
|---|---|---|---|---|---|
| LTF EMA20 Pierce (late confirm) + HTF EMA20 Pierce (incl. late) | 215 | +79 | +128 / -20 / -29 | +4 |  |
| HTF EMA20 Pierce (incl. late) | 115 | +72 | +125 / -27 / -26 | -16 |  |
| LTF EMA20 Pierce (late confirm) + HTF EMA9 Pierce (incl. late) + HTF EMA20 Pierce (incl. late) | 426 | +69 | +173 / -100 / -5 | +16 |  |
| HTF EMA9 Pierce (incl. late) + HTF EMA20 Pierce (incl. late) | 326 | +61 | +171 / -107 / -2 | -4 |  |
| LTF EMA20 Pierce (closed beyond EMA9) + LTF EMA20 Pierce (late confirm) + HTF EMA20 Pierce (incl. late) | 325 | +55 | +215 / -114 / -46 | -10 |  |
| LTF EMA20 Pierce (closed beyond EMA9) + HTF EMA20 Pierce (incl. late) | 225 | +48 | +212 / -121 / -43 | -30 |  |
| LTF EMA20 Pierce (closed beyond EMA9) + LTF EMA20 Pierce (late confirm) + HTF EMA9 Pierce (incl. late) + HTF EMA20 Pierce (incl. late) | 536 | +45 | +261 / -194 / -22 | +2 |  |
| LTF EMA20 Pierce (closed beyond EMA9) + HTF EMA9 Pierce (incl. late) + HTF EMA20 Pierce (incl. late) | 436 | +38 | +258 / -201 / -19 | -17 |  |

Current (Flip + LTF beyond EMA9 + LTF not beyond EMA9, v10.88) ranks 61 of 63 by net. Walk-forward: best on thirds 1-2 = LTF EMA20 Pierce (late confirm) + HTF EMA20 Pierce (incl. late) -> third 3 -29 (rank 59 of 63; current +31).