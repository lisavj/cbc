## Week of 11/09/2026 summary

- STUDY SETTINGS STALE: the 11/08 settings sync report lists 1 non-known MISMATCH (chop_sim GATE MGC 2m range gate R5=0) + late_study MES 3m tp=2.0 -- both already fixed in the project scripts used for this run, and neither affects these 3m studies.
- Current bot set (Flip + LTF EMA20 Pierce closed beyond EMA9): replay **-158** (thirds -6 / -161 / +8, last 4 wk +61), ranks 38 of 63; no combination positive in all thirds; walk-forward pick -12 on third 3 (11/08: -153, 41 of 63).
- MAIN WATCH 'turn ON Trigger: HTF EMA20 Pierce (incl. late)': **Δ +89** (Δ thirds +125 / -27 / -9, Δ last 4 wk +4); live HTF EMA20 Pierce in bot windows **5 / +10.5** (unchanged). Does not qualify (thirds 2 and 3 negative, live n < 15). **Bot HTF EMA20 Pierce: weeks qualifying 0/3.**
- Current triggers: HTF CBC Flip -135 (-93 / -67 / +25; live 13 / +43.1), LTF beyond EMA9 -24 (+87 / -94 / -17; live 6 / +20.9) -- neither negative in all thirds -> **keep bot triggers as is**.
- LTF NOT beyond EMA9 still negative in all thirds (-75 / -58 / -29) -> keep off. LTF late +7 (live 17 / -2.4) -> keep off.
- Live alert store only added a few setups since 11/06 (weekend). Header text 'Jan 5 -> Nov 6' is hard-coded in bot_trig.py; replay data now run to 11/09.

---

MES 3m BOT trigger checkboxes -- which setup types should the bot take? -- 11/08/2026.
REPLAY: all CBC setups (every trigger on, as CBC draws them), then the bot takes only setups whose trigger is ticked, inside the v10.87
windows (candle close 18:30-22:00, 03:00-13:00, 15:00-15:30 ET) with the 5-day short filter; bot exits = 100 % at TP1 1.75 ATR, SL1 3 ATR,
CBC setup end / 16:00. Net after costs (0.50 per trade). LIVE: real MES 3m Trade Setup -> Setup Ended pairs since 10/19 (CBC chart exits,
not bot exits), same windows + short filter.

## 1. Every trigger type (replay Jan 5 -> Nov 6 + live since 10/19)

| Trigger (bot checkbox) | Bot now | Replay trades | Replay net | Win % | Avg | Thirds | Last 4 wk | Live (bot windows) n / net / avg | Live all hours n / net |
|---|---|---|---|---|---|---|---|---|---|
| HTF CBC Flip | ON | 150 | -135 | 55 % | -0.90 | -93 / -67 / +25 | +54 | 13 / +43.1 / +3.31 | 15 / +41.7 |
| LTF EMA20 Pierce (closed beyond EMA9) | ON | 110 | -24 | 52 % | -0.21 | +87 / -94 / -17 | +7 | 6 / +20.9 / +3.48 | 15 / +2.8 |
| LTF EMA20 Pierce (not beyond EMA9) | off | 213 | -163 | 40 % | -0.76 | -75 / -58 / -29 | +40 | 22 / +10.2 / +0.46 | 31 / -12.2 |
| LTF EMA20 Pierce (late confirm) | off | 100 | +7 | 56 % | +0.07 | +2 / +7 / -3 | +16 | 17 / -2.4 / -0.14 | 20 / -21.1 |
| HTF EMA9 Pierce | off | 194 | -25 | 47 % | -0.13 | +30 / -94 / +39 | +11 | 9 / +20.1 / +2.23 | 12 / +10.6 |
| HTF EMA9 Pierce (late) | off | 16 | +17 | 56 % | +1.08 | +16 / +9 / -8 | +4 | 2 / -5.9 / -2.94 | 2 / -5.9 |
| HTF EMA20 Pierce | off | 111 | +82 | 50 % | +0.74 | +125 / -27 / -16 | -1 | 3 / +4.5 / +1.48 | 5 / -5.8 |
| HTF EMA20 Pierce (late) | off | 3 | +7 | 67 % | +2.32 | +0 / +0 / +7 | +5 | 2 / +6.0 / +3.00 | 3 / +0.8 |
| HTF Pullback Structure | off | (not in replay) | | | | | | 0 / +0.0 / +0.00 | 2 / -9.1 |

## 2. Turning one checkbox on / off (replay, bot exits, after costs; Δ vs the current bot set Flip + LTF beyond EMA9 = -158, thirds -6 / -161 / +8, last 4 wk +61)

| Change | Trades | Net | Δ | Δ by third | Δ last 4 wk | Better in all thirds |
|---|---|---|---|---|---|---|
| turn OFF Trigger: HTF CBC Flip | 110 | -24 | +135 | +93 / +67 / -25 | -54 |  |
| turn OFF Trigger: LTF EMA20 Pierce (closed beyond EMA9) | 150 | -135 | +24 | -87 / +94 / +17 | -7 |  |
| turn ON Trigger: LTF EMA20 Pierce (not beyond EMA9) | 473 | -321 | -163 | -75 / -58 / -29 | +40 |  |
| turn ON Trigger: LTF EMA20 Pierce (late confirm) | 360 | -151 | +7 | +2 / +7 / -3 | +16 |  |
| turn ON Trigger: HTF EMA9 Pierce (incl. late) | 470 | -167 | -8 | +46 / -85 / +31 | +15 |  |
| turn ON Trigger: HTF EMA20 Pierce (incl. late) | 374 | -70 | +89 | +125 / -27 / -9 | +4 |  |

## 3. Best checkbox combinations (replay, all 63)

| Checkboxes ON | Trades | Net | Thirds | Last 4 wk | All thirds positive |
|---|---|---|---|---|---|
| LTF EMA20 Pierce (late confirm) + HTF EMA20 Pierce (incl. late) | 214 | +96 | +128 / -20 / -12 | +20 |  |
| HTF EMA20 Pierce (incl. late) | 114 | +89 | +125 / -27 / -9 | +4 |  |
| LTF EMA20 Pierce (late confirm) + HTF EMA9 Pierce (incl. late) + HTF EMA20 Pierce (incl. late) | 424 | +88 | +173 / -105 / +19 | +35 |  |
| HTF EMA9 Pierce (incl. late) + HTF EMA20 Pierce (incl. late) | 324 | +81 | +171 / -112 / +21 | +18 |  |
| LTF EMA20 Pierce (closed beyond EMA9) + LTF EMA20 Pierce (late confirm) + HTF EMA20 Pierce (incl. late) | 324 | +72 | +215 / -114 / -29 | +27 |  |
| LTF EMA20 Pierce (closed beyond EMA9) + HTF EMA20 Pierce (incl. late) | 224 | +65 | +212 / -121 / -26 | +11 |  |
| LTF EMA20 Pierce (closed beyond EMA9) + LTF EMA20 Pierce (late confirm) + HTF EMA9 Pierce (incl. late) + HTF EMA20 Pierce (incl. late) | 534 | +64 | +261 / -198 / +2 | +41 |  |
| LTF EMA20 Pierce (closed beyond EMA9) + HTF EMA9 Pierce (incl. late) + HTF EMA20 Pierce (incl. late) | 434 | +57 | +258 / -205 / +4 | +25 |  |

Current (Flip + LTF beyond EMA9) ranks 38 of 63 by net. Walk-forward: best on thirds 1-2 = LTF EMA20 Pierce (late confirm) + HTF EMA20 Pierce (incl. late) -> third 3 -12 (rank 41 of 63; current +8).