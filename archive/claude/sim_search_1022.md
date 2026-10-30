# Filter + exit search — 10/22/2026 (claude/sim2.py, search.py, robust.py)

Replay proxy on BarFeed bars (MGC 3m 10/07–10/22, MES 3m 10/05–, MGC 2m 9/30–, MES 2m 10/06–): HTF flip (side gate, ER ≥ 0.23) + LTF EMA20 pierce setups, current gates/exits per case. Searched ~650 entry filters (12 candle/trend features × 9 thresholds × all/pierce/flip, sessions, cloud, 15m structure) and 208 exit combos per case. Pass rule: ≥ 20 blocked, better in both halves, then re-checked by thirds and neighbouring thresholds.

| Case | Replay base | Robust candidate (all 3 thirds better, neighbours consistent) | Result |
|---|---|---|---|
| MGC 3m | 114 / −46.3 | Setup candle must close in the trade direction with body ≥ 0.2 ATR (0.3 stronger) | 40 / +11.7 (0.3: 28 / +49.4) |
| MGC 3m | | Exits: 100 % at TP1 1.5 ATR, SL 1.7 ATR (conflicts with the 10/12–10/19 real-setup replay behind v10.28/v10.31) | 123 / +30.5 |
| MGC 3m | | Both together | 42 / +62.6 |
| MES 2m | 216 / −50.7 | ER minimum 0.20 for all triggers (now 0.08 for LTF pierce); 0.15–0.26 all better | 168 / +32.5 |
| MGC 2m | 314 / +80.5 | Skip flip setups when ATR(14) > its 100-bar average | 279 / +134.5 |
| MES 3m | 140 / +115.6 | nothing robust; leave as is | — |

Rejected: MES 2m SL 1.0 / TP1 3.0 (gain only in the last third); body / ER filters on MES 3m and MGC 2m (hurt).

Real-alert check (10/19–10/22 only, small N) does NOT confirm yet: MGC 3m body ≥ 0.2 7 / +1.7 vs < 0.2 10 / +2.6; MES 2m real setups with ER ≥ 0.2 still 35 / −62.1. Replay MES 3m +0.83/setup vs real −1.16 since 10/19 → the proxy differs a lot from the real engine. ~1,800 combos tested → some false positives expected.

Next: re-run on real setups once 20+ per case accumulate (alert store now keeps 100k); log body / ER / ATR ratio in setup alerts if wanted.
