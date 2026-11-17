# MGC 3m range gate watch -- 2026-11-13 20:13 ET (weekly run 3)

Bars Jan 5 -> Nov 13. Live = gate 5 ATR / 24 bars / zone 20 % (+ MGC 3m VWAP stretch 4, ER 0.23 + breakout), base exits (ss.QB — the chop_sim EXIT mismatch in settings_sync_report does not enter these runs). Run history: 11/02 = run 1, 11/07 (repaired-data rerun) = run 2, this = run 3. "Last 4 wk" = Oct 16 -> Nov 13.

## Since last week

| MGC 3m row | Δ vs live | z | Thirds (Jan–Mar / Apr–Jun / Jul–Nov) | Verdict | Last 4 wk | vs 11/07 | Robust runs in a row |
|---|---|---|---|---|---|---|---|
| **Gate 4.0, zone 30 % (candidate)** | +151 | 1.6 | +76 / +9 / +66 | promising | **−28.2** | was +169, z 1.8, Jul–Nov +84, last 4 wk +7.8 → weaker | 0 |
| Gate 4.0, zone 35 % | +109 | 1.1 | +54 / +27 / +27 | promising | −23.2 | was +127, z 1.3 | 0 |
| Gate 4.5, zone 30 % | +106 | 1.2 | +48 / +27 / +31 | promising | −21.7 | was +118, z 1.3 | 0 |
| Gate 4.0, zone 40 % | +96 | 0.9 | +56 / +36 / +4 | noise | −29.5 | was +114 promising | 0 |
| Gate 4.0, zone 25 % | +91 | 1.0 | +96 / −13 / +8 | noise | −44.0 | was +116 | 0 |
| Gate 4.0, zone 20 % | +64 | 0.8 | +83 / −28 / +9 | noise | −44.0 | was +92 | 0 |
| Gate 3.5, zone 30 % | +76 | 0.7 | +81 / −27 / +22 | noise | −34.2 | was +97 | 0 |
| Gate 5.0, zone 30 % | −17 | −0.2 | −13 / −3 / −1 | worse | −7.8 | was −9 | 0 |

This week's MGC 3m trading went against every looser gate: all rows lost 22-44 pts vs live over the last 4 weeks, and the candidate slipped to z 1.6. Still promising, never robust; the 3-run streak has not started.

MES 3m gate rows (zone 20 %): OFF +139 (z 1.1, Jul–Nov −63, last 4 wk +23.0), 3.0 +163 (Jul–Nov −44), 3.5 +131 (−16), 4.0 +68 (−36, last 4 wk +29.4), 4.5 +30 (−12, +23.1), 5.5 −36, 6.0 −42. Looser is still better Jan–Jun but worse Jul–Nov (now with positive last 4 weeks) → gate 5 stays; MES 3m zone change stays out (MGC 3m only).

**Verdict: no change — keep waiting.** Rule needs the candidate robust (z ≥ 2, all thirds better) 3 weekly runs in a row with last-4-weeks Δ ≥ 0 and Jul–Nov positive each time; this run it is z 1.6 with last 4 weeks −28.2.

---

## rgate_watch.py (MGC 3m candidate + neighbours)

| Variant | Setups | Win % | Net | Δ vs live (5) | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Nov) | Verdict | Last 4 wk |
|---|---|---|---|---|---|---|---|---|
| Gate 4.0, zone 30 % (candidate) | 1254 | 52% | +472 | +151 | +1.6 | +76 / +9 / +66 | promising | -28.2 |
| Gate 4.0, zone 25 % | 1276 | 52% | +412 | +91 | +1.0 | +96 / -13 / +8 | noise | -44.0 |
| Gate 4.0, zone 35 % | 1224 | 52% | +429 | +109 | +1.1 | +54 / +27 / +27 | promising | -23.2 |
| Gate 4.0, zone 40 % | 1199 | 52% | +417 | +96 | +0.9 | +56 / +36 / +4 | noise | -29.5 |
| Gate 3.5, zone 30 % | 1321 | 52% | +397 | +76 | +0.7 | +81 / -27 / +22 | noise | -34.2 |
| Gate 4.5, zone 30 % | 1147 | 52% | +426 | +106 | +1.2 | +48 / +27 / +31 | promising | -21.7 |
| Gate 4.0, zone 20 % | 1297 | 51% | +385 | +64 | +0.8 | +83 / -28 / +9 | noise | -44.0 |
| Gate 5.0, zone 30 % | 1067 | 51% | +304 | -17 | -0.2 | -13 / -3 / -1 | worse | -7.8 |

---

## rgate_study.py

Range gate sweep (MES 3m / MGC 3m) -- 11/02/2026.
Range gate = block a new setup when the 24-bar range is under x ATR and the close is in the top 20 % (long) / bottom 20 % (short).
x = OFF, 3.0 ... 6.0 by 0.5, one change on top of each chart's live settings (filter_sweep.LIVE: ER 0.23 + breakout, MGC 3m VWAP stretch 4).
Bars Jan 5 - Nov 2, base exits (ss.QB). Also: what the current gate (5) blocks, by trigger.
z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all thirds (Jan-Mar / Apr-Jun / Jul-Nov); promising = z >= 1 and all three.

## MES 3m — current (range gate 5 ATR): 1756 setups, win 50%, net -3, thirds +123 / -214 / +88

| Range gate | Setups | Win % | Net | Δ vs 5 | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|
| OFF | 2046 | 52% | +136 | +139 | +1.1 | +130 / +71 / -63 | noise | +23.0 |
| 3.0 ATR | 2033 | 52% | +160 | +163 | +1.3 | +116 / +91 / -44 | noise | +17.2 |
| 3.5 ATR | 1986 | 51% | +128 | +131 | +1.1 | +78 / +68 / -16 | noise | +10.0 |
| 4.0 ATR | 1909 | 51% | +65 | +68 | +0.7 | +62 / +43 / -36 | noise | +29.4 |
| 4.5 ATR | 1828 | 50% | +28 | +30 | +0.5 | +35 / +8 / -12 | noise | +23.1 |
| 5.0 ATR | 1756 | 50% | -3 | +0 | +0.0 | +0 / +0 / +0 | current | +0.0 |
| 5.5 ATR | 1711 | 49% | -39 | -36 | -0.8 | +6 / -7 / -35 | worse | -7.5 |
| 6.0 ATR | 1686 | 49% | -45 | -42 | -0.7 | +17 / -27 / -32 | worse | +0.2 |

Setups present with the gate OFF but not with 5 ATR (by trigger, their OFF-run result): flip 292 / +70 (win 57%), ltf20 93 / +12 (win 56%), h20 34 / -3 (win 50%), h9 47 / -44 (win 43%)

## MGC 3m — current (range gate 5 ATR): 1199 setups, win 51%, net +320, thirds +161 / +2 / +157

| Range gate | Setups | Win % | Net | Δ vs 5 | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|
| OFF | 1364 | 52% | +370 | +50 | +0.5 | +97 / -53 / +6 | noise | -33.2 |
| 3.0 ATR | 1359 | 52% | +406 | +86 | +0.8 | +109 / -43 / +20 | noise | -33.2 |
| 3.5 ATR | 1336 | 52% | +376 | +55 | +0.5 | +74 / -46 / +27 | noise | -33.1 |
| 4.0 ATR | 1297 | 51% | +385 | +64 | +0.8 | +83 / -28 / +9 | noise | -44.0 |
| 4.5 ATR | 1241 | 51% | +362 | +41 | +0.8 | +32 / +4 / +6 | noise | -22.8 |
| 5.0 ATR | 1199 | 51% | +320 | +0 | +0.0 | +0 / +0 / +0 | current | +0.0 |
| 5.5 ATR | 1164 | 51% | +330 | +9 | +0.2 | -2 / +16 / -5 | noise | -8.2 |
| 6.0 ATR | 1142 | 50% | +264 | -57 | -0.9 | -28 / -18 / -11 | worse | -13.3 |

Setups present with the gate OFF but not with 5 ATR (by trigger, their OFF-run result): flip 156 / +29 (win 54%), h9 28 / +68 (win 71%), ltf20 55 / -9 (win 47%), h20 23 / -24 (win 39%)

