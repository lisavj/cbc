# Opening-range block weekly check -- 2026-11-07 09:50 ET (weekly run 2, rerun after data repair)

Weekly run 2, rerun after data repair (BarFeed bars repaired 11/07: MGC 3m had 5m candles mixed in, MES 2m/5m had gaps). Per the manual fire, this run REPLACES the 11/06 19:37 run as run 2 (run 1 = 11/01); the 11/07 09:46 entry is folded into this one (identical output). "Was" figures below are from the pre-repair 11/06 run. Data Jan 5 -> latest bars (2m: Jun 1 -> latest). Δ = turning that block OFF vs current (all three ON). Robust = z >= 2 and better in all three thirds.

## Since last week

| Chart | NY off: Δ (z; thirds) | London off | Asia off | All off |
|---|---|---|---|---|
| MES 3m | -62 (-1.4; -61/-23/+22) worse — was -62 (-1.5) | -1 (0.0) worse — same | -32 (-0.8; +16/-15/-33) worse — same | -94 (-1.3) worse — same |
| MGC 3m | **+109 (+2.5; -1/+65/+45) noise — was +112 (+2.6; -1/+65/+48)** | -0 (0.0) worse — was +1 | +67 (+1.4; +7/+13/+47) promising — was +62 (+1.3) promising | +176 (+2.3; -4/+51/+129) noise — was +174 (+2.3) |
| MES 2m | -26 (-0.8) worse — same | +54 (+1.6; -5/+10/+50) noise — same | +10 (+0.3) noise — same | +38 (+0.7) noise — same |
| MGC 2m | +1 (0.0) noise — was +2 | -58 (-1.6; -69/-1/+11) worse — same | +29 (+0.7; +11/+36/-18) noise — same | -28 (-0.4) worse — was -27 |
| MES 5m | +55 (+1.1; +37/-4/+16) noise — same | -25 (-0.6) worse — same | -49 (-1.1) worse — same | -19 (-0.2) worse — same |
| MGC 5m | -2 (0.0) worse — same | +9 (+0.2) noise — same | -44 (-0.8) worse — same | -37 (-0.4) worse — same |

**Consecutive robust weekly runs:** 0 for every row (no row has been robust on run 1 or this run 2). MGC 3m NY still misses only on Jan–Mar (-1, flat).

**Window setups the block removes (count / win % / net), this run vs the pre-repair 11/06 run:**

- MES 3m: NY 55 / 53 % / -21 (same); London 56 / 54 % / +4 (same); Asia 44 / 45 % / -32 (same)
- MGC 3m: **NY 47 / 67 % / +90 (was 46 / 69 % / +93)**; London 39 / 51 % / -11 (was 38 / 53 % / -6); Asia 60 / 55 % / +46 (was 59 / 54 % / +41)
- MES 2m: NY 43 / 51 % / -23; London 39 / 62 % / +32; Asia 29 / 55 % / +3 (all same)
- MGC 2m: NY 41 / 61 % / +43 (was 42 / 62 % / +51); London 48 / 38 % / -60 (same); Asia 59 / 59 % / +41 (same)
- MES 5m: NY 61 / 59 % / +61; London 36 / 44 % / -17; Asia 38 / 47 % / -7 (all same)
- MGC 5m: NY 47 / 57 % / +26; London 37 / 54 % / +17; Asia 53 / 55 % / -9 (all same)

**Live:** no Trade Setup alerts inside the windows since 10/13 — with the block ON nothing fires there, so there is no live evidence either way; the verdict rests on the replay only.

## Verdict: keep as is (all six charts, all three sessions)

No chart meets the rule (robust on >= 3 consecutive weekly runs + >= 30 removed setups net positive + positive in the latest third).

- **Main watch, MGC 3m NY:** steady — Δ +109, z 2.5, removed 47 setups at 67 % win / +90, latest third +45. Not "robust" only because Jan–Mar is -1; robust-run count stays 0. If it turns robust it needs 3 straight weekly runs; the change would then be ① Auto Trade Setup → "No new setups during opening range (forming)" → untick NY on MGC 3m only, then recreate the MGC 3m TradingView alert.
- **MGC 3m Asia:** promising, edged up again (+67, z 1.4, thirds +7 / +13 / +47); removed 60 setups +46. Needs z >= 2.
- **MES 5m NY:** unchanged (+55, z 1.1, Apr–Jun -4); noise.
- **Keep-confirmations (block OFF worse):** MES 3m NY (-62, z -1.4), MGC 2m London (-58, z -1.6; removed setups 38 % win), MES 5m Asia (-49, z -1.1, all thirds negative). None robustly worse (no z <= -2), but all consistent with prior runs.

---

# Opening-range block study -- 2026-11-07 09:50 ET (weekly run 2, rerun after data repair)

Opening-range block study -- 11/01/2026.

Question: CBC v9.60+ "No new setups during opening range (forming)" is ON for NY (9:30-10:00 ET), London (3:00-3:30) and
Asia (20:00-20:30). Is it helping? Replay with the block per session ON (current) vs OFF, per chart on its live settings
(MES 3m range gate; MGC 3m range gate + VWAP stretch 4; MES 2m 1H MTF gate; 5m no gates; base exits; chart / HTF EMAs 9 / 20).
Engine: chop_sim_or.py = chop_sim.py with the OR-window skip replaced by a label (otherwise identical; with every block ON it
reproduces chop_sim). A blocked setup is not just removed: the setups after it can change (cooldown, one open setup at a time).
Also lists the setups the block removes (window setups when it is OFF) and the live alerts in the windows.
z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds; promising = z >= 1 and all three.
Usage: python3 orf_study.py

## MES 3m — current (all three blocks ON): 1720 setups, net +27, win 50%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1765 | 50% | -34 | -62 | -1.4 | -61 / -23 / +22 | worse |
| Block OFF: London only | 1770 | 50% | +27 | -1 | -0.0 | +19 / -13 / -7 | worse |
| Block OFF: Asia only | 1754 | 50% | -4 | -32 | -0.8 | +16 / -15 / -33 | worse |
| Block OFF: all three | 1849 | 50% | -67 | -94 | -1.3 | -26 / -51 / -17 | worse |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 55 | 53% | -21.1 | -0.38 | ltf20 30 / +8, h9 6 / +5, flip 16 / -17, h20 3 / -17 |
| London | 56 | 54% | +3.6 | +0.06 | h20 7 / +1, flip 11 / +14, ltf20 25 / -20, h9 13 / +8 |
| Asia | 44 | 45% | -32.1 | -0.73 | flip 11 / -17, ltf20 22 / -21, h20 3 / -1, h9 8 / +7 |

## MGC 3m — current (all three blocks ON): 1180 setups, net +278, win 51%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1219 | 51% | +387 | +109 | +2.5 | -1 / +65 / +45 | noise |
| Block OFF: London only | 1215 | 51% | +278 | -0 | -0.0 | -10 / -27 / +37 | worse |
| Block OFF: Asia only | 1229 | 51% | +345 | +67 | +1.4 | +7 / +13 / +47 | promising |
| Block OFF: all three | 1303 | 52% | +454 | +176 | +2.3 | -4 / +51 / +129 | noise |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 47 | 67% | +90.1 | +1.92 | ltf20 20 / +45, h20 10 / +46, h9 9 / -16, flip 8 / +15 |
| London | 39 | 51% | -11.3 | -0.29 | ltf20 21 / -1, h9 10 / -7, flip 3 / -7, h20 5 / +3 |
| Asia | 60 | 55% | +45.7 | +0.76 | ltf20 39 / +5, flip 5 / -6, h9 8 / +35, h20 8 / +11 |

## MES 2m — current (all three blocks ON): 1223 setups, net -174, win 49%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1261 | 49% | -200 | -26 | -0.8 | -1 / -6 / -19 | worse |
| Block OFF: London only | 1252 | 50% | -120 | +54 | +1.6 | -5 / +10 / +50 | noise |
| Block OFF: Asia only | 1246 | 49% | -165 | +10 | +0.3 | -6 / +10 / +6 | noise |
| Block OFF: all three | 1313 | 50% | -136 | +38 | +0.7 | -13 / +14 / +36 | noise |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 43 | 51% | -22.7 | -0.53 | flip 21 / -54, h9 5 / +16, ltf20 16 / +4, h20 1 / +10 |
| London | 39 | 62% | +32.4 | +0.83 | flip 9 / -6, ltf20 22 / +29, h20 1 / +3, h9 7 / +6 |
| Asia | 29 | 55% | +3.3 | +0.11 | ltf20 18 / +3, h20 1 / +0, flip 6 / +1, h9 4 / -1 |

## MGC 2m — current (all three blocks ON): 1495 setups, net +351, win 52%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1528 | 52% | +352 | +1 | +0.0 | +4 / +5 / -8 | noise |
| Block OFF: London only | 1533 | 52% | +292 | -58 | -1.6 | -69 / -1 / +11 | worse |
| Block OFF: Asia only | 1547 | 52% | +380 | +29 | +0.7 | +11 / +36 / -18 | noise |
| Block OFF: all three | 1618 | 52% | +322 | -28 | -0.4 | -54 / +41 / -15 | worse |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 41 | 61% | +43.4 | +1.06 | ltf20 16 / +3, h9 6 / -0, flip 15 / +24, h20 4 / +16 |
| London | 48 | 38% | -59.9 | -1.25 | h20 4 / -11, flip 15 / -24, ltf20 25 / -27, h9 4 / +2 |
| Asia | 59 | 59% | +41.1 | +0.70 | flip 12 / +20, ltf20 33 / +4, h20 7 / -2, h9 7 / +19 |

## MES 5m — current (all three blocks ON): 1178 setups, net -6, win 51%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1230 | 51% | +49 | +55 | +1.1 | +37 / -4 / +16 | noise |
| Block OFF: London only | 1206 | 51% | -31 | -25 | -0.6 | -0 / -2 / -4 | worse |
| Block OFF: Asia only | 1205 | 51% | -55 | -49 | -1.1 | -21 / -11 / -7 | worse |
| Block OFF: all three | 1285 | 51% | -25 | -19 | -0.2 | +16 / -17 / +5 | worse |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 61 | 59% | +60.6 | +0.99 | h20 7 / -12, h9 9 / -6, ltf20 31 / +79, flip 14 / -0 |
| London | 36 | 44% | -17.2 | -0.48 | ltf20 15 / +5, h20 6 / -18, h9 8 / +6, flip 7 / -10 |
| Asia | 38 | 47% | -6.9 | -0.18 | flip 19 / +7, ltf20 14 / -14, h20 4 / -3, h9 1 / +3 |

## MGC 5m — current (all three blocks ON): 1168 setups, net -110, win 51%

| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |
|---|---|---|---|---|---|---|---|
| Block OFF: NY only | 1213 | 51% | -111 | -2 | -0.0 | +30 / -16 / -11 | worse |
| Block OFF: London only | 1196 | 51% | -101 | +9 | +0.2 | -16 / -13 / +25 | noise |
| Block OFF: Asia only | 1210 | 51% | -154 | -44 | -0.8 | -3 / +31 / -14 | worse |
| Block OFF: all three | 1283 | 51% | -147 | -37 | -0.4 | +11 / +2 / -0 | worse |

**Setups inside the windows when the block is OFF** (what the block removes):

| Window | Setups | Win % | Net | Avg | by trigger |
|---|---|---|---|---|---|
| NY | 47 | 57% | +26.2 | +0.56 | ltf20 26 / +24, h20 8 / +7, flip 7 / +1, h9 6 / -5 |
| London | 37 | 54% | +17.4 | +0.47 | ltf20 13 / -45, flip 12 / +44, h20 5 / +18, h9 7 / +1 |
| Asia | 53 | 55% | -8.9 | -0.17 | ltf20 25 / -16, flip 21 / +13, h9 5 / -13, h20 2 / +6 |

## Live Trade Setup alerts inside the OR windows (should be none since the v9.60 default, 10/13)

None.
