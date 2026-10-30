# Market structure (HH/HL vs LH/LL) analysis — 10/22/2026

Question: would requiring LTF / HTF structure to agree with the trade improve results? Judged per symbol + chart TF (rule: 20+ setups, holds in both halves).

## 1. Bug found first: CBC's HTF Structure is stuck at "LH / HL"
Actual Trade Setup alerts since 10/19 (167 with results): the "Structure (15m/10m)" line reads **LH / HL in ~90 %** of alerts, for longs and shorts, MES and MGC alike.
Cause: `htf_piv_hi_raw/lo_raw` come from `request.security(..., lookahead_off)` without `gaps_on`, so the same HTF pivot value repeats on every chart bar of the next HTF candle. On the 2nd chart bar the pivot is compared with itself → "Lower High" / "Higher Low". Same bug makes every HTF pivot an HTF EQH/EQL (`abs(piv - h_last_hi) <= tol` with itself) and freezes the HTF BOS/CHoCH trend.
Affected: Status-table Structure (HTF) row, confluence factor "Structure HTF", HTF Pullback Structure trigger (needs HH/HL → almost never fires), HTF EQH/EQL in the pivot table and TP/SL candidate pool, alert text.
Fix (proposed, not yet made): process an HTF pivot only on the first chart bar it arrives (e.g. `htf_piv_bar_t != htf_piv_bar_t[1]`, or `gaps_on` on that request). LTF structure (native `ta.pivothigh(2,2)`) is fine.
→ HTF structure from alerts cannot be analysed; HTF results below come from a bar replay with correct 15m/10m pivots.

## 2. Bar replay (proxy) — claude/struct_replay.py
BarFeed bars (MGC 3m 10/07–10/22, MES 3m 10/05–, MGC 2m 9/30–, MES 2m 10/06–). Proxy setups: HTF CBC flip (side gate, ER ≥ 0.23) + LTF EMA20 pierce (pullback, ER ≥ 0.08), 10-candle spacing, no setups 16:00–18:45, R5 (3m) / X4 (MGC 3m) gates, current exits per case. Structure at the setup candle: LTF pivots N=2, HTF pivots N=1 on aggregated 15m/10m candles. Proxy ≠ the full CBC engine (more setups, simplified triggers).
"Pullback side intact" = long: last swing low is HL; short: last swing high is LH.

| Case | N / net | LTF structure | HTF structure |
|---|---|---|---|
| MGC 3m | 117 / −41.5 | "with" no edge (−0.22/trade); LTF pullback-side intact −78.9 vs broken +37.4 (counter-intuitive, actual alerts disagree on small N) | **HTF pullback side broken: 67 trades −57.9 (h1 −17.5 / h2 −40.4); intact +16.4** — mostly LTF EMA20 pierces (52, −52.5) |
| MGC 2m | 318 / +88.8 | intact +84.6 vs broken +4.3 (h2 reverses) | opposite of MGC 3m: broken +87.0, intact +1.8 |
| MES 3m | 141 / +135.4 | all buckets positive; "against" best | "with" best (+1.49/trade both halves); "against" weakest (+0.36, h2 −4.5) — nothing worth blocking |
| MES 2m | 220 / −42.6 | "mixed" −49.6 (both halves) | "mixed" −56.3 (both halves); flips with HTF broken −25.9 vs +11.0 intact, pierces opposite |

Actual alerts (LTF only, 10/19–10/22, small N): MES 3m LTF "with" 10 setups −36.0 (10 % win); MES 2m LTF "mixed" 18 setups −56.2 (both halves) — consistent with the replay.

## 3. Verdict
- No general "trade with structure" edge: LTF "with" was never better than average in any case.
- Only candidate that passes the rule: **MGC 3m — skip setups when the 15m pullback side is broken** (long after a 15m Lower Low, short after a 15m Higher High). Proxy only; needs the HTF-structure bug fixed first, then re-check on real alerts.
- MES 2m "mixed" structure is consistently negative but is not a clean rule; watch.
- Do not apply the MGC 3m rule to MGC 2m (opposite result).
