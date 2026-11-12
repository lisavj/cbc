# MGC 3m range gate watch -- 2026-11-07 09:51 ET (weekly run 2 -- rerun after data repair; replaces the 11/06 run)

Bars Jan 5 -> Nov 6. Live = gate 5 ATR / 24 bars / zone 20 % (+ MGC 3m VWAP stretch 4, ER 0.23 + breakout). **Rerun after the BarFeed bar-data repair (MGC 3m had 5m candles mixed in) — replaces the 11/06 run as weekly run 2** (11/02 = run 1). "vs 11/06" below = vs the pre-repair 11/06 numbers; the repair moved mainly the Jul–Nov third (MGC 3m live net +186 → +278).

## Since last week

| MGC 3m row | Δ vs live | z | Thirds (Jan–Mar / Apr–Jun / Jul–Nov) | Verdict | Last 4 wk | vs 11/06 | Robust runs in a row |
|---|---|---|---|---|---|---|---|
| **Gate 4.0, zone 30 % (candidate)** | +169 | 1.8 | +76 / +9 / +84 | promising | +7.8 | +160, z 1.7, Jul–Nov +75, last 4 wk −1.5 → slightly better | 0 |
| Gate 4.0, zone 35 % | +127 | 1.3 | +54 / +27 / +46 | promising | +4.8 | was +101 noise | 0 |
| Gate 4.0, zone 40 % | +114 | 1.1 | +56 / +36 / +22 | promising | −1.5 | was +85 noise | 0 |
| Gate 4.5, zone 30 % | +118 | 1.3 | +48 / +27 / +44 | promising | +4.9 | was +125 promising | 0 |
| Gate 4.0, zone 25 % | +116 | 1.3 | +96 / −13 / +32 | noise | −14.0 | was +119 noise | 0 |
| Gate 4.0, zone 20 % | +92 | 1.2 | +83 / −28 / +37 | noise | −15.8 | was +88 noise | 0 |
| Gate 3.5, zone 30 % | +97 | 0.9 | +81 / −27 / +43 | noise | −2.8 | was +101 noise | 0 |
| Gate 5.0, zone 30 % | −9 | −0.1 | −13 / −3 / +7 | worse | +12.2 | was −2 | 0 |

The candidate is back to a positive last 4 weeks (+7.8) but z 1.8 is still under 2 → promising, not robust; the 3-run streak has not started.

MES 3m gate rows (zone 20 %): OFF +111 (z 0.9, Jul–Nov −90, last 4 wk −18.0), 3.0 +136 (Jul–Nov −72), 3.5 +109 (−38), 4.0 +46 (−59), 4.5 +20 (Jul–Nov −22, last 4 wk +1.9), 5.5 −36, 6.0 −42. Same picture: looser is better Jan–Jun but worse Jul–Nov → gate 5 stays right.

**Verdict: no change — keep waiting.** Rule needs the candidate robust (z ≥ 2, all thirds better) 3 weekly runs in a row with last-4-weeks Δ ≥ 0 and Jul–Nov positive each time.

---

## rgate_watch.py (MGC 3m candidate + neighbours)

| Variant | Setups | Win % | Net | Δ vs live (5) | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Nov) | Verdict | Last 4 wk |
|---|---|---|---|---|---|---|---|---|
| Gate 4.0, zone 30 % (candidate) | 1236 | 52% | +447 | +169 | +1.8 | +76 / +9 / +84 | promising | +7.8 |
| Gate 4.0, zone 25 % | 1257 | 52% | +393 | +116 | +1.3 | +96 / -13 / +32 | noise | -14.0 |
| Gate 4.0, zone 35 % | 1206 | 52% | +405 | +127 | +1.3 | +54 / +27 / +46 | promising | +4.8 |
| Gate 4.0, zone 40 % | 1181 | 52% | +392 | +114 | +1.1 | +56 / +36 / +22 | promising | -1.5 |
| Gate 3.5, zone 30 % | 1300 | 52% | +375 | +97 | +0.9 | +81 / -27 / +43 | noise | -2.8 |
| Gate 4.5, zone 30 % | 1130 | 52% | +396 | +118 | +1.3 | +48 / +27 / +44 | promising | +4.9 |
| Gate 4.0, zone 20 % | 1277 | 51% | +370 | +92 | +1.2 | +83 / -28 / +37 | noise | -15.8 |
| Gate 5.0, zone 30 % | 1051 | 50% | +268 | -9 | -0.1 | -13 / -3 / +7 | worse | +12.2 |

---

## rgate_study.py

Range gate sweep (MES 3m / MGC 3m) -- 11/02/2026.
Range gate = block a new setup when the 24-bar range is under x ATR and the close is in the top 20 % (long) / bottom 20 % (short).
x = OFF, 3.0 ... 6.0 by 0.5, one change on top of each chart's live settings (filter_sweep.LIVE: ER 0.23 + breakout, MGC 3m VWAP stretch 4).
Bars Jan 5 - Nov 2, base exits (ss.QB). Also: what the current gate (5) blocks, by trigger.
z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all thirds (Jan-Mar / Apr-Jun / Jul-Nov); promising = z >= 1 and all three.

## MES 3m — current (range gate 5 ATR): 1719 setups, win 50%, net +16, thirds +123 / -214 / +107

| Range gate | Setups | Win % | Net | Δ vs 5 | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|
| OFF | 2004 | 52% | +127 | +111 | +0.9 | +130 / +71 / -90 | noise | -18.0 |
| 3.0 ATR | 1991 | 52% | +151 | +136 | +1.1 | +116 / +91 / -72 | noise | -23.7 |
| 3.5 ATR | 1945 | 51% | +124 | +109 | +1.0 | +78 / +68 / -38 | noise | -15.3 |
| 4.0 ATR | 1868 | 51% | +62 | +46 | +0.5 | +62 / +43 / -59 | noise | -0.9 |
| 4.5 ATR | 1790 | 50% | +36 | +20 | +0.3 | +35 / +8 / -22 | noise | +1.9 |
| 5.0 ATR | 1719 | 50% | +16 | +0 | +0.0 | +0 / +0 / +0 | current | +0.0 |
| 5.5 ATR | 1676 | 49% | -21 | -36 | -0.8 | +6 / -7 / -35 | worse | -22.6 |
| 6.0 ATR | 1651 | 49% | -26 | -42 | -0.7 | +17 / -27 / -32 | worse | -3.6 |

Setups present with the gate OFF but not with 5 ATR (by trigger, their OFF-run result): flip 286 / +48 (win 56%), ltf20 92 / +7 (win 55%), h20 34 / -3 (win 50%), h9 46 / -51 (win 41%)

## MGC 3m — current (range gate 5 ATR): 1180 setups, win 51%, net +278, thirds +161 / +2 / +114

| Range gate | Setups | Win % | Net | Δ vs 5 | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|
| OFF | 1342 | 52% | +353 | +76 | +0.7 | +97 / -53 / +32 | noise | -10.5 |
| 3.0 ATR | 1337 | 52% | +390 | +112 | +1.1 | +109 / -43 / +46 | noise | -10.5 |
| 3.5 ATR | 1315 | 51% | +354 | +76 | +0.8 | +74 / -46 / +48 | noise | -8.4 |
| 4.0 ATR | 1277 | 51% | +370 | +92 | +1.2 | +83 / -28 / +37 | noise | -15.8 |
| 4.5 ATR | 1222 | 51% | +341 | +64 | +1.3 | +32 / +4 / +28 | promising | -4.0 |
| 5.0 ATR | 1180 | 51% | +278 | +0 | +0.0 | +0 / +0 / +0 | current | +0.0 |
| 5.5 ATR | 1146 | 50% | +281 | +3 | +0.1 | -2 / +16 / -11 | noise | -22.3 |
| 6.0 ATR | 1124 | 50% | +215 | -63 | -1.0 | -28 / -18 / -17 | worse | -27.4 |

Setups present with the gate OFF but not with 5 ATR (by trigger, their OFF-run result): flip 152 / +28 (win 54%), h9 28 / +68 (win 71%), ltf20 54 / -4 (win 48%), h20 23 / -24 (win 39%)

