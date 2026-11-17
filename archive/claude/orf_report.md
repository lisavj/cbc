# Opening-range block weekly check -- 2026-11-14 12:13 ET (weekly run 3)

Weekly run 3 (run 1 = 11/01, run 2 = 11/07 rerun after data repair). Data Jan 5 -> latest bars (2m: Jun 1 -> latest; the "Jul–Oct" third now includes November). Δ = turning that block OFF vs current (all three ON). Robust = z >= 2 and better in all three thirds.

**STUDY SETTINGS STALE:** settings_sync_report (11/13, v10.96) lists 3 non-known MISMATCHes — chop_sim `EXIT` MES 3m (still 'tod' 80/100 %, live is 100 % at TP1 all day since v10.95) and MGC 3m (still 50 % + trail 3.5, live is FLIP 0 % since v10.96), and mes3_ema_grid `LIVE` part. This study passes its own base exits (`QB`: SL1 1.7 ATR, TP1 1.7, 80 % at TP1, BE, trail 1.7) for every chart, so those constants are not read here; but the replay exits for MES 3m and MGC 3m are therefore not the live exits. Gates (R5 / X4 / MTF, MGC 2m range gate) match live.

**MGC 2m baseline jump:** the 11/08 script sync turned the MGC 2m range gate ON (live since v10.77). MGC 2m figures below are not comparable to run 2 — that change, not the market, explains the move.

## Since last week

| Chart | NY off: Δ (z; thirds) | London off | Asia off | All off |
|---|---|---|---|---|
| MES 3m | -57 (-1.3; -61/-23/+27) worse — was -62 (-1.4) | +4 (+0.1) noise — was -1 | -32 (-0.8; +16/-15/-33) worse — same | -84 (-1.2) worse — was -94 |
| MGC 3m | **+111 (+2.5; -1/+65/+48) noise — was +109 (+2.5; -1/+65/+45)** | -2 (-0.1) worse — was -0 | +72 (+1.5; +7/+13/+51) promising — was +67 (+1.4) | +181 (+2.4; -4/+51/+133) noise — was +176 (+2.3) |
| MES 2m | -26 (-0.8) worse — same | +54 (+1.6; -5/+10/+50) noise — same | +14 (+0.5) noise — was +10 | +43 (+0.8) noise — was +38 |
| MGC 2m (range gate now ON) | -35 (-1.2; -12/+2/-25) worse — was +1 | -7 (-0.2) worse — was -58 (-1.6) | -6 (-0.2) worse — was +29 (+0.7) | -48 (-0.8) worse — was -28 |
| MES 5m | +54 (+1.1; +37/-4/+15) noise — was +55 | -25 (-0.6) worse — same | -54 (-1.2; -21/-11/-12) worse — was -49 | -24 (-0.3) worse — was -19 |
| MGC 5m | -9 (-0.2) worse — was -2 | +9 (+0.2) noise — same | -39 (-0.7) worse — was -44 | -39 (-0.5) worse — was -37 |

**Consecutive robust weekly runs:** 0 for every row (no row has been robust on runs 1, 2 or 3). MGC 3m NY still fails only on Jan–Mar (-1).

**Window setups the block removes (count / win % / net), this run vs run 2:**

- MES 3m: NY 56 / 54 % / -16 (was 55 / 53 % / -21); London 59 / 54 % / +9 (was 56 / 54 % / +4); Asia 45 / 44 % / -40 (was 44 / 45 % / -32)
- MGC 3m: **NY 48 / 68 % / +92 (was 47 / 67 % / +90)**; London 40 / 50 % / -14 (was 39 / 51 % / -11); Asia 61 / 56 % / +51 (was 60 / 55 % / +46)
- MES 2m: NY 43 / 51 % / -23 (same); London 40 / 60 % / +27 (was 39 / 62 % / +32); Asia 31 / 58 % / +12 (was 29 / 55 % / +3)
- MGC 2m (range gate ON, not comparable): NY 31 / 55 % / +1 (was 41 / 61 % / +43); London 40 / 45 % / -8 (was 48 / 38 % / -60); Asia 50 / 48 % / +2 (was 59 / 59 % / +41)
- MES 5m: NY 63 / 60 % / +70 (was 61 / 59 % / +61); London 36 / 44 % / -17 (same); Asia 39 / 46 % / -11 (was 38 / 47 % / -7)
- MGC 5m: NY 48 / 56 % / +19 (was 47 / 57 % / +26); London 37 / 54 % / +17 (same); Asia 56 / 54 % / -18 (was 53 / 55 % / -9)

**Live:** no Trade Setup alerts inside the windows since 10/13 — with the block ON nothing fires there, so there is no live evidence either way; the verdict rests on the replay only.

## Verdict: keep as is (all six charts, all three sessions)

No chart meets the rule (robust on >= 3 consecutive weekly runs + >= 30 removed setups net positive + positive in the latest third).

- **Main watch, MGC 3m NY:** steady for a third week — Δ +111, z 2.5, removed 48 setups at 68 % win / +92, latest third +48. Still not "robust" only because Jan–Mar is -1 (that third is closed history, so it will not change unless the data or engine changes); robust-run count stays 0. If it ever qualified, the change would be ① Auto Trade Setup → "No new setups during opening range (forming)" → untick NY on MGC 3m only, then recreate the MGC 3m TradingView alert. Caveat: replay uses base exits, not the live MGC 3m FLIP 0 % exit.
- **MGC 3m Asia:** promising, edged up again (+72, z 1.5, thirds +7 / +13 / +51); removed 61 setups +51. Needs z >= 2.
- **MES 5m NY:** unchanged (+54, z 1.1, Apr–Jun -4); noise.
- **Keep-confirmations (block OFF worse):** MES 3m NY (-57, z -1.3) and Asia (-32), MES 5m Asia (-54, z -1.2, all three thirds negative), MGC 2m NY (-35, z -1.2) now that the range gate is on. None robustly worse (no z <= -2). MGC 2m London is no longer a strong keep-confirmation with the range gate on (-7, z -0.2).

---

# Opening-range block study -- 2026-11-14 12:13 ET (weekly run 3)

Opening-range block study -- 11/01/2026 (11/08: MGC 2m range gate ON as live since v10.77).

Question: CBC v9.60+ "No new setups during opening range (forming)" is ON for NY (9:30-10:00 ET), London (3:00-3:30) and
Asia (20:00-20:30). Is it helping? Replay with the block per session ON (current) vs OFF, per chart on its live settings
(MES 3m range gate; MGC 3m range gate + VWAP stretch 4; MGC 2m range gate; MES 2m 1H MTF gate; 5m no gates; base exits; chart / HTF EMAs 9 / 20).
Engine: chop_sim_or.py = chop_sim.py with the OR-window skip replaced by a label (otherwise identical; with every block ON it
reproduces chop_sim). A blocked setup is not just removed: the setups after it can change (cooldown, one open setup at a time).
Also lists the setups the block removes (window setups when it is OFF) and the live alerts in the windows.
z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds; promising = z >= 1 and all three.
Usage: python3 orf_study.py

## MES 3m — current (all three blocks ON): 1757 setups, net +9, win 50%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1803 | 50% | -48 | -57 | -1.3 | -61 / -23 / +27 | worse |
| Block OFF: London only | 1810 | 50% | +13 | +4 | +0.1 | +19 / -13 / -2 | noise |
| Block OFF: Asia only | 1791 | 50% | -23 | -32 | -0.8 | +16 / -15 / -33 | worse |
| Block OFF: all three | 1890 | 50% | -75 | -84 | -1.2 | -26 / -51 / -7 | worse |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 56 | 54% | -16.3 | -0.29 | ltf20 31 / +13, h9 6 / +5, flip 16 / -17, h20 3 / -17 |
| London | 59 | 54% | +8.5 | +0.14 | h20 8 / -4, flip 12 / +19, ltf20 25 / -20, h9 14 / +13 |
| Asia | 45 | 44% | -40.1 | -0.89 | flip 12 / -25, ltf20 22 / -21, h20 3 / -1, h9 8 / +7 |

## MGC 3m — current (all three blocks ON): 1199 setups, net +320, win 51%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1239 | 52% | +432 | +111 | +2.5 | -1 / +65 / +48 | noise |
| Block OFF: London only | 1235 | 51% | +318 | -2 | -0.1 | -10 / -27 / +35 | worse |
| Block OFF: Asia only | 1249 | 51% | +392 | +72 | +1.5 | +7 / +13 / +51 | promising |
| Block OFF: all three | 1325 | 52% | +501 | +181 | +2.4 | -4 / +51 / +133 | noise |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 48 | 68% | +92.2 | +1.92 | ltf20 20 / +45, h20 11 / +48, h9 9 / -16, flip 8 / +15 |
| London | 40 | 50% | -13.7 | -0.34 | ltf20 22 / -3, h9 10 / -7, flip 3 / -7, h20 5 / +3 |
| Asia | 61 | 56% | +50.5 | +0.83 | ltf20 40 / +10, flip 5 / -6, h9 8 / +35, h20 8 / +11 |

## MES 2m — current (all three blocks ON): 1277 setups, net -211, win 49%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1315 | 49% | -237 | -26 | -0.8 | -1 / -6 / -19 | worse |
| Block OFF: London only | 1306 | 49% | -157 | +54 | +1.6 | -5 / +10 / +50 | noise |
| Block OFF: Asia only | 1301 | 49% | -196 | +14 | +0.5 | -6 / +10 / +10 | noise |
| Block OFF: all three | 1368 | 50% | -168 | +43 | +0.8 | -13 / +14 / +41 | noise |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 43 | 51% | -22.7 | -0.53 | flip 21 / -54, h9 5 / +16, ltf20 16 / +4, h20 1 / +10 |
| London | 40 | 60% | +27.4 | +0.69 | flip 10 / -11, ltf20 22 / +29, h20 1 / +3, h9 7 / +6 |
| Asia | 31 | 58% | +11.9 | +0.38 | ltf20 18 / +3, h20 1 / +0, flip 8 / +10, h9 4 / -1 |

## MGC 2m — current (all three blocks ON): 1352 setups, net +389, win 52%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1377 | 51% | +354 | -35 | -1.2 | -12 / +2 / -25 | worse |
| Block OFF: London only | 1387 | 52% | +383 | -7 | -0.2 | -19 / -4 / +16 | worse |
| Block OFF: Asia only | 1399 | 51% | +383 | -6 | -0.2 | +1 / +18 / -25 | worse |
| Block OFF: all three | 1459 | 51% | +341 | -48 | -0.8 | -31 / +17 / -33 | worse |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 31 | 55% | +1.2 | +0.04 | ltf20 15 / -5, h9 5 / -11, flip 6 / +7, h20 5 / +11 |
| London | 40 | 45% | -8.0 | -0.20 | h20 4 / -1, ltf20 27 / +10, flip 5 / -18, h9 4 / +1 |
| Asia | 50 | 48% | +1.5 | +0.03 | flip 7 / +0, ltf20 30 / -15, h20 8 / +4, h9 5 / +12 |

## MES 5m — current (all three blocks ON): 1203 setups, net +22, win 51%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1255 | 52% | +76 | +54 | +1.1 | +37 / -4 / +15 | noise |
| Block OFF: London only | 1231 | 51% | -4 | -25 | -0.6 | -0 / -2 / -4 | worse |
| Block OFF: Asia only | 1231 | 51% | -32 | -54 | -1.2 | -21 / -11 / -12 | worse |
| Block OFF: all three | 1311 | 51% | -3 | -24 | -0.3 | +16 / -17 / -1 | worse |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 63 | 60% | +70.2 | +1.11 | h20 7 / -12, h9 9 / -6, ltf20 33 / +89, flip 14 / -0 |
| London | 36 | 44% | -17.2 | -0.48 | ltf20 15 / +5, h20 6 / -18, h9 8 / +6, flip 7 / -10 |
| Asia | 39 | 46% | -11.4 | -0.29 | flip 19 / +7, ltf20 15 / -19, h20 4 / -3, h9 1 / +3 |

## MGC 5m — current (all three blocks ON): 1189 setups, net -100, win 51%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1235 | 51% | -108 | -9 | -0.2 | +30 / -16 / -18 | worse |
| Block OFF: London only | 1217 | 51% | -91 | +9 | +0.2 | -16 / -13 / +25 | noise |
| Block OFF: Asia only | 1232 | 51% | -139 | -39 | -0.7 | -3 / +31 / -9 | worse |
| Block OFF: all three | 1306 | 51% | -139 | -39 | -0.5 | +11 / +2 / -3 | worse |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 48 | 56% | +19.2 | +0.40 | ltf20 26 / +24, h20 8 / +7, flip 7 / +1, h9 7 / -12 |
| London | 37 | 54% | +17.4 | +0.47 | ltf20 13 / -45, flip 12 / +44, h20 5 / +18, h9 7 / +1 |
| Asia | 56 | 54% | -18.1 | -0.32 | ltf20 26 / -11, flip 22 / +6, h9 5 / -13, h20 3 / -1 |

## Live Trade Setup alerts inside the OR windows (should be none since the v9.60 default, 10/13)

None.
