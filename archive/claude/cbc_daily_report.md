# CBC daily report -- Thu 10/29/2026 (run 17:27 ET)

Data: 19,566 alerts stored, from **10/19**. CBC v10.45 defaults from 10/29. **v10.45 looks loaded:** MGC 3m SL1 losses since 10/29 are −7.00 / −5.02 (≥ 5 pts) and no "Time stop" exit since 10/29 (last one 10/28 12:21). **v10.42 still OK:** 0 MES 2m setups with "HTF flips 4/8"+ since 10/28 18:00. **No "Room:" lines yet** (v10.47 not loaded). "Today" = Wed 10/28 17:27 → Thu 10/29 close. Halves = setups split by time.

## Verdicts

- **MGC 3m — base exits day 1: weak, too early (6 setups since 10/29).** Since 10/29: 6 setups, −10.9 (−1.82/setup vs base-replay +0.58 and v10.31 live −0.14); SL1 2 (33 %), trail/TP1 1 (17 %), CBC flip 3 (50 %). Revert flag not testable before 20 setups. All stored: 44 setups −20.9.
- **MES 3m — base exits still negative, N 15 < 20.** Since 10/28: 15 setups, −30.5 (−2.03/setup vs +1.77 baseline); halves −2.04 / −2.03; SL1 8 (53 %), trail 4 (27 %), CBC flip 2, 16:00 1. Today 7 setups −8.2. Judge at 20+.
- **MGC 2m — bad day, no default change.** Today 12 setups, 3 wins, −36.5; all stored 81 setups −35.7 (−0.44/setup). Flip-flop warning setups drive it (see suggestion 1).
- **MES 2m — flip counter working, still negative.** Since 10/28: 8 setups −15.0 (−1.88/setup vs −2.07 baseline, tiny N). Today 3 setups −4.7. All stored 77 setups −126.6.

## Gate table (all stored 10/19→10/29 · blocked · win % · net of blocked · halves h1 / h2; negative = gate would have helped)

| Gate | MGC 3m (44) | MGC 2m (81) | MES 3m (70) | MES 2m (77) |
|---|---|---|---|---|
| Range 24/20 %/<5 ATR (live on 3m) | 3 · 33 % · −8.1 (h1 only) | 12 · 50 % · −14.6 (−2.5 / −12.1) | 2 · 0 % · −14.0 (h1 only) | 14 · 43 % · −19.8 (−12.8 / −7.1) |
| Range <6 ATR | 5 · 20 % · −13.8 (−8.1 / −5.7) | 18 · 44 % · −23.7 (−7.5 / −16.1) | 8 · 38 % · −12.1 (−11.6 / −0.5) | 21 · 43 % · −23.1 (−6.1 / −17.1) |
| VWAP stretch >4 ATR (live MGC 3m) | 2 · 50 % · −3.0 | 30 · 53 % · +1.9 (+6.1 / −4.1) | 12 · 50 % · +1.4 | 26 · 38 % · −24.8 (−0.0 / −24.8) |
| VWAP stretch >6 ATR | 1 · +2.0 | 15 · 67 % · +16.1 | 4 · 75 % · +10.4 | 14 · 29 % · −22.3 (−5.8 / −16.4) |
| Flips ≥ 4/8 | 5 · 80 % · +24.4 (hurts) | 10 · 20 % · −25.3 (−3.9 / −21.5) | 18 · 50 % · +11.4 (hurts both) | 18 · −49.3 → live `MES 2m 4`; 0 since 10/28 ✓ |
| 1H MTF against | 21 · 38 % · −9.7 (+10.6 / −20.3) | 36 · 53 % · +4.3 | 28 · 36 % · −20.5 (**−25.9 / +5.4**) | 16 · −21.9 (gated) |
| Side gate | 0 | 0 | 0 | 0 |
| Opposing OB before TP1 | **18 · 28 % · −29.4 (−4.9 / −24.5); −1.63 vs +0.33** | 42 · −15.4 (+5.3 / −20.7) | 26 · −1.9 (−13.1 / +11.2) | 30 · −45.2 (−18.5 / −26.7) |
| Level/OB < 0.5× TP1 | 32 · −11.3 (+11.3 / −22.6) | 62 · −34.6 (−7.8 / −26.8) | **48 · 38 % · −57.8 (−37.3 / −20.4)** | 51 · −81.8 (−46.9 / −34.8) |
| Flip flop warning | 29 · +7.9 (hurts) | **42 · 38 % · −47.3 (−16.1 / −31.2); −1.13 vs +0.30** | 47 · −29.6 (−22.4 / −7.2) | 35 · −71.4 (−39.8 / −31.6) |
| 15m EMA cloud against | **16 · 31 % · −22.4 (−12.0 / −10.4); −1.40 vs +0.05** | 22 · −12.8 (−8.1 / −4.7) | 21 · −18.2 (−18.7 / +0.6) | 12 · −35.1 (−33.0 / −2.2) |

Watch items:

- **Pullback, LTF EMA20 Pierce (< 0.75 vs ≥ 0.75 ATR):** MGC 3m 8 · −19.9 vs 18 · +6.2 · **MGC 2m 10 · −28.3 (−19.2 / −9.1) vs 38 · +4.2** (no new shallow setups today; N 10 < 20) · MES 3m 4 · −12.9 vs 37 · −42.5 · MES 2m 9 · −28.1 vs 29 · −67.4.
- **MES 3m HTF EMA9 Pierce pullback:** > 2.5 ATR 4 · −4.8 vs ≤ 2.5 ATR 21 · −25.7 (same per setup). No signal.
- **MES 3m HTF EMA slope (both ≥ 0.5 pt):** ≥ 0.5: 31 · −43.6 vs < 0.5: 39 · −23.1 (< 0.5 halves −31.2 / +8.1) → still fails. Gate stays Off.
- **Room/context rows:** MGC 3m opposing OB and 15m cloud against both still negative in both halves (N 18 / 16 flagged). MES 3m Level/OB < 0.5× TP1 negative in both halves. Room gates stay watch items (Friday room study did not confirm; no "Room:" lines yet).
- **MGC 2m flop on non-flip setups:** FL 31 · −36.1 (−1.17/setup; halves −22.5 / −13.6) vs no FL 28 · +10.4 (+0.37/setup) → meets the candidate rule (see Suggested changes).
- MES 3m 1H-against: h1 −25.9 / h2 +5.4 — still no MTF gate for MES 3m.

## Losers today (Wed 10/28 17:27 → Thu 10/29 close)

| Case | Time | Dir | Trigger | Result | Ended | Ext ATR | Range pos/width | Flips | 1H | Gates |
|---|---|---|---|---|---|---|---|---|---|---|
| MGC 3m | 10/28 21:09 | S | HTF Pullback Structure | −6.91 | SL1 hit | +0.5 | 51 % / 5.6 | 3 | Bear | FL |
| MGC 3m | 10/29 05:00 | S | LTF EMA20 Pierce (late), HTF | −7.00 | SL1 hit | +4.0 | 57 % / 4.2 | 3 | Bear | L5 |
| MGC 3m | 10/29 06:21 | L | LTF EMA20 + HTF EMA9 Pierce | −3.50 | CBC flip | −3.5 | 54 % / 4.9 | 3 | Bear | CL,L5,M |
| MGC 3m | 10/29 10:51 | L | LTF EMA20 + HTF EMA9 Pierce | −5.60 | CBC flip | −0.7 | 72 % / 3.9 | 2 | Bear | FL,M,OB |
| MGC 3m | 10/29 13:27 | L | HTF EMA9 Pierce | −5.02 | SL1 hit | −4.6 | 64 % / 4.9 | 2 | Bear | CL,FL,L5,M,OB |
| MGC 2m | 10/28 19:40 | S | HTF EMA9 Pierce (late) | −5.00 | SL1 hit | +2.2 | 75 % / 3.4 | 1 | Bear | FL,L5,OB |
| MGC 2m | 10/28 21:04 | S | HTF EMA9 Pierce (late) | −5.44 | SL1 hit | +2.1 | 47 % / 3.9 | 0 | Bear | FL,L5 |
| MGC 2m | 10/28 22:00 | L | Flip | −6.64 | SL1 hit | +2.5 | 66 % / 4.9 | 4 | Bear | F,M |
| MGC 2m | 10/29 05:00 | S | LTF EMA20 Pierce (late), HTF | −6.99 | SL1 hit | +4.6 | 56 % / 4.8 | 2 | Bear | X4 |
| MGC 2m | 10/29 05:16 | L | HTF EMA20 Pierce | −7.00 | SL1 hit | −2.7 | 69 % / 5.4 | 3 | Bear | CL,FL,L5,M,OB |
| MGC 2m | 10/29 06:22 | L | LTF EMA20 Pierce (late), HTF | −5.00 | SL1 hit | −3.9 | 89 % / 4.5 | 1 | Bear | CL,FL,L5,M,OB,R5 |
| MGC 2m | 10/29 06:30 | S | Flip | −3.40 | CBC flip | +5.8 | 69 % / 3.5 | 1 | Bear | FL,L5,X4 |
| MGC 2m | 10/29 11:28 | S | LTF EMA20 Pierce | −2.60 | CBC flip | +4.1 | 84 % / 5.7 | 1 | Bear | FL,L5,OB,R6,X4 |
| MGC 2m | 10/29 13:16 | L | HTF EMA20 Pierce | −2.30 | CBC flip | −5.0 | 73 % / 5.9 | 2 | Bear | CL,FL,L5,M,OB |
| MES 3m | 10/28 19:51 | S | LTF EMA20 Pierce (late) | −7.39 | SL1 hit | +0.7 | 63 % / 4.0 | 2 | Bull | FL,M |
| MES 3m | 10/29 04:36 | L | HTF EMA9 + EMA20 Pierce | −5.48 | SL1 hit | +0.9 | 73 % / 5.0 | 3 | Bear | CL,FL,L5,M,OB |
| MES 3m | 10/29 06:18 | L | LTF EMA20 Pierce | −4.00 | CBC flip | +3.0 | 56 % / 4.3 | 1 | Bull | FL,L5,OB |
| MES 3m | 10/29 12:06 | L | LTF EMA20 + HTF EMA20 Pierce | −8.00 | SL1 hit | +1.0 | 65 % / 4.5 | 1 | Bear | FL,L5,M,OB |
| MES 2m | 10/29 07:16 | L | LTF EMA20 Pierce | −5.00 | SL1 hit | +5.2 | 85 % / 5.8 | 3 | Bull | FL,L5,OB,R6,X4 |
| MES 2m | 10/29 14:32 | S | LTF EMA20 Pierce (late) | −6.09 | SL1 hit | +6.1 | 79 % / 4.1 | 1 | Bear | X4,X6 |

## Suggested changes

1. **MGC 2m — candidate flop gate for non-flip setups (needs a Pine change; the v10.16 flop gate covers HTF CBC Flip setups only).** Block MGC 2m setups that carry the "Flip flop" warning. Evidence: 81 MGC 2m setups; non-flip setups with the warning 31 · −36.1 (−1.17/setup), halves −22.5 / −13.6, vs non-flip without it 28 · +10.4 (+0.37/setup); all MGC 2m FL 42 · −47.3 vs no FL 39 · +11.6. Both groups ≥ 20, negative in both halves. Suggest a per-case input (e.g. `MGC 2m` only), OFF on other cases (FL hurts on MGC 3m: +7.9).
2. Done / standing: MGC 3m exit revert (v10.45) — live, now tracking. MES 2m flip counter `MES 2m 4` (v10.42) — verified.

Not suggested / watch:

- MGC 3m base exits (6 setups) and MES 3m base exits (15 setups since 10/28): below 20 — no judgment.
- MGC 2m min pullback 0.75 ATR: −28.3, both halves negative, but N 10 < 20.
- Room gates (MGC 3m OB / cloud, MES 3m Level/OB < 0.5× TP1): watch only until the Friday room study recommends one.
- MES 3m slope gate: fails halves; stays Off.
