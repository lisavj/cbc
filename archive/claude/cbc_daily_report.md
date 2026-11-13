# CBC daily report -- 2026-11-12 17:26 ET

Settings sync (11/12 16:47 ET): newest Pine v10.93 (v10.88–v10.93 are ▶ Bot changes only); 0 MISMATCH, 1 known item (late_study MGCX runner base). No stale-settings warning.
Data: 45,409 alerts stored, 43,905 after removing duplicates (DATA_NOTES: server v14 running, `lastDedupe` still null). 516 setups with results (MGC 3m 74 · MGC 2m 193 · MES 3m 107 · MES 2m 142). Every setup matched to bars (no BarFeed-gap skips).
Today (session 11/12, from Wed 18:00 ET): MGC 3m 0 · MGC 2m 13 · −10.4 · MES 3m 2 · −13.4 · MES 2m 7 · −30.9.
Alert flow: MES 3m alerts are back on 11/12 (59 alerts; none on 11/10–11/11). MGC 3m dropped from ~300+ to 60 alerts a day after the duplicate alert was deleted, which fits removing the doubled copy.

**Gate checks:**

- MES 2m flip counter + 1H MTF gate are live: 0 MES 2m setups with "HTF flips 4/8"+ or 1H against since 10/28.
- 3m range gates are live: 0 MGC 3m / MES 3m setups whose alert shows ≥ 80 % of the 24-bar range at < 5 ATR (non-momentum).
- MES 3m flip-timing gate: pierce setups since 11/06 came 1–5 HTF bars after the flip (11/12 10:03 LTF pierce: 2 bars). No late ones.
- **MGC 2m gates (v10.77): still not confirmed live, but no new range violations today.** The last violation by alert text is 11/11 21:40 (Flip short, 89 % / 3.8 ATR, −5.85). There were none in the 11/12 day session.
  - Non-flip setups with a "Flip flop" line: 9 since 11/06 08:46 (net +15.0). The latest is 11/12 05:32 (+4.18).
  - The MGC 2m alerts came in doubled until 11/12, so some of these may have come from the older duplicate alert. Watch for a clean day from 11/13.

## Verdicts

- **MGC 3m (50 % at TP1 / trail 3.5):** since 11/09 there are 7 setups · +32.5 (+4.64/setup), vs the 10/29–11/07 baseline (80 % / 1.7) of 29 · −24.3 (−0.84/setup; halves −30.1 / +5.8).
  - The runner made +29.3 of the +32.5, mostly from the 11/08 19:24 long (+24.9 on the runner half).
  - There were no new MGC 3m setups after 11/11 06:15.
  - Caveat: 11/09–11/12 results are partly on the old exits (DATA_NOTES 2). Where both existed, the "0.5×(TP1)" result was used.
  - **Revert flag count starts 11/13: 0/20.**
- **MES 3m (SL1 3 ATR / TP1 1.75 ATR from 11/03, without the 11/06 TP1 2.0 day):** 19 setups · +7.4 (+0.39/setup), halves +10.7 / −3.4.
  - SL1 hit 21 % (4), TP1 hit 37 % (7).
  - Today: the 09:30 Flip short lost −18.7 (SL1) and the 10:03 LTF pierce long made +5.25.
  - Under 20 setups on these exits, so no judgment.
- **MGC 2m:** 193 · −64.2 all stored. Since v10.77: 49 · −3.0 (−0.06/setup), halves −14.4 / +11.4.
  - Today: 13 · −10.4. Of the 6 losers, 4 came 11:40–15:30 on a big down day for gold (VWAP 17–20 ATR away).
- **MES 2m:** 142 · −82.5 all stored. Today was weak: 7 · −30.9, with 6 losers (2 Asia flip shorts, then 3 NY losers 11:28–14:08).
- **MES 3m bot set** (bot windows; current three-trigger set: Flip + LTF EMA20 Pierce beyond / not beyond EMA9; 5-day short filter; bracket replay 100 % at TP1, 0.5 pt cost):
  - Since 10/19: 40 setups · chart +84.1 · bot replay +55.9 (+1.40/setup), halves +12.5 / +43.5.
  - The old two-trigger set alone: 17 · +49.5.
  - Since 11/09: 2 · −14.8. Both were LTF pierces not beyond EMA9: 11/08 20:36 −19.5 and 11/12 10:03 +4.75.
  - The short filter again skipped today's 09:30 Flip short (−18.7 on the chart). It has skipped 7 shorts in total (−34.8).
  - Not modelled in the replay (v10.92 flip-only exit, 09:30–16:00 Flip entries): the 4 such Flip trades since 10/19 would be +90.0 held to the HTF flip, vs +34.0 with the TP1 bracket.

## Gate table (all stored 10/19 → 11/12, after dedupe · blocked · win % · net of blocked · halves h1 / h2; negative = gate would have helped)

| Gate | MGC 3m (74) | MGC 2m (193) | MES 3m (107) | MES 2m (142) |
|---|---|---|---|---|
| Range 24/20 %/<5 ATR (live 3m; MGC 2m v10.77) | 3 · 33 % · −8.1 | **39 · 49 % · −34.6 (−25.0 / −9.7)** (gate should be live) | 2 · 0 % · −14.0 | 27 · 52 % · −6.5 (−19.8 / +13.3) |
| Range <6 ATR | 6 · 33 % · −6.8 | 53 · 45 % · −49.3 (−34.7 / −14.7) | 9 · 44 % · +3.1 | 38 · 53 % · −2.5 |
| VWAP stretch >4 ATR (live MGC 3m) | 2 · 50 % · −3.0 | 73 · 53 % · +15.2 (hurts) | 22 · 41 % · −8.4 (+1.4 / −9.8) | 66 · 47 % · −10.7 (−13.7 / +3.0) |
| VWAP stretch >6 ATR | 1 · +2.0 | 47 · 57 % · +23.4 (hurts) | 10 · 50 % · −10.8 (+10.4 / −21.2) | 41 · 44 % · −16.5 (−16.2 / −0.4) |
| Flips ≥ 4/8 | 7 · 86 % · +54.2 (hurts) | 30 · 30 % · −40.9 (−16.6 / −24.2) | 22 · 50 % · −6.5 (+18.1 / −24.7) | 18 · −49.3 → live `MES 2m 4` |
| 1H MTF against | 34 · 38 % · +0.9 | 74 · 49 % · −18.2 (+6.8 / −25.0) | 38 · 45 % · +0.0 (−10.2 / +10.2) | 16 · −21.9 (gated) |
| Side gate | 0 | 0 | 0 | 0 |
| Opposing OB before TP1 | **25 · 36 % · −21.0 (−18.8 / −2.3)** | 80 · −19.3 (−5.1 / −14.1) | 37 · +0.6 | 42 · +2.0 (−46.5 / +48.5) |
| Level/OB < 0.5× TP1 | 55 · −1.3 (−0.6 / −0.6) | 136 · −36.5 (−14.9 / −21.5) | **72 · 44 % · −56.8 (−35.2 / −21.6)** | 79 · −27.2 (−75.3 / +48.0) |
| Flip flop warning | 44 · 48 % · +20.3 (hurts) | **75 · 40 % · −70.7 (−57.1 / −13.6)** → v10.77 | 68 · 51 % · +40.6 (hurts) | 65 · 42 % · −65.4 (−66.3 / +0.9) |
| 15m EMA cloud against | **29 · 34 % · −41.3 (−18.8 / −22.5)** | 56 · −30.2 (−10.4 / −19.7) | 26 · +22.7 (hurts) | 17 · −26.4 (−35.1 / +8.8) |

Pattern WITH vs none: MGC 3m 20 · −15.0 vs 54 · +13.3; MGC 2m 63 · −17.7 vs 130 · −46.6; MES 3m 39 · −44.5 vs 68 · +32.8; MES 2m 54 · −28.7 vs 88 · −53.8.

Note: MGC 2m / MGC 3m VWAP extensions of ±17–29 ATR on 11/10 and 11/12 come from the alerts themselves (e.g. 11/12 11:40 "VWAP ext +17.2 ATR"). On these gold trend days price was far from VWAP. These setups inflate the stretch rows.

**MGC 2m flips ≥ 4 (30 · −40.9, both halves negative):** not listed as a suggestion.

- It overlaps the v10.77 flop gate: without the FL setups it's 17 · −6.1.
- The 11/07 MGC 2m replay (Jun–Nov) scores "flips ≥ 4 block" −15 (worse, z −0.3).
- Since v10.77: 8 · −24.2, so it stays on watch. It becomes a candidate if the non-FL subset turns clearly negative over 20+ setups.

### Watch items

**Pullback, LTF EMA20 Pierce (< 0.75 ATR vs ≥ 0.75 ATR):**

| Case | Shallow < 0.75 ATR | Shallow halves | Deep ≥ 0.75 ATR |
|---|---|---|---|
| MGC 3m | 10 · −28.4 (−2.84/setup) | −7.7 / −20.7 | 33 · +32.4 |
| **MGC 2m (candidate)** | 16 · −18.6 (−1.16/setup) | −26.0 / +7.4 | 83 · −0.1 |
| MES 3m | 5 · −7.9 | −11.6 / +3.7 | 62 · −17.3 |
| MES 2m | 17 · −27.9 | −33.3 / +5.5 | 64 · −27.6 |

The MGC 2m candidate has 16 setups (< 20) and its 2nd half is positive. No change.

**MES 3m HTF EMA9 Pierce pullback:** > 2.5 ATR is 3 · −9.4 vs ≤ 2.5 ATR 11 · +14.2. Too few setups.

**MES 3m HTF EMA slope (both 15m slopes ≥ 0.5 pt vs < 0.5):**

- ≥ 0.5 pt: 52 · +52.8 (+1.01/setup), halves −11.8 / +64.6.
- < 0.5: 55 · −64.4 (−1.17/setup), halves −27.1 / −37.3.
- On the current exits only: ≥ 0.5 is 12 · +28.3, < 0.5 is 7 · −20.9.
- The gate stays Off per the checklist (watch item). A fresh slope study is worth doing once the current exits reach 20+ setups.

**Room/context:**

- MGC 3m opposing OB and 15m cloud, and MES 3m L5, are negative in both halves. They stay watch-only.
- The room daily task (11/12) has the MES 3m 0.2× TP1 gate as a candidate waiting for out-of-sample data (2 blocked). It doesn't recommend it yet.

## Losers today (session 11/12)

| Case | Time | Dir | Trigger | Result | Ended | Gates |
|---|---|---|---|---|---|---|
| MGC 2m | 11/11 21:28 | L | LTF EMA20 Pierce | −5.70 | SL1 hit | F,FL,L5,M |
| MGC 2m | 11/11 21:40 | S | HTF CBC Flip | −5.85 | SL1 hit | F,FL,**R5**,R6 |
| MGC 2m | 11/12 11:40 | S | HTF CBC Flip | −6.41 | SL1 hit | L5,OB,R5*,R6,X4,X6 (*bar calc; alert says 23 % → not gated) |
| MGC 2m | 11/12 13:14 | L | HTF EMA20 Pierce (late) | −5.00 | SL1 hit | CL,R6 |
| MGC 2m | 11/12 13:46 | L | LTF EMA20 Pierce | −5.00 | SL1 hit | CL,L5 |
| MGC 2m | 11/12 15:30 | L | LTF EMA20 Pierce (late) | −3.10 | CBC flip | L5 |
| MES 3m | 11/12 09:30 | S | HTF CBC Flip | −18.70 | SL1 hit | – (bot: skipped by 5-day short filter) |
| MES 2m | 11/11 19:00 | S | HTF CBC Flip | −7.72 | SL1 hit | FL,R5,R6 |
| MES 2m | 11/11 19:50 | S | HTF CBC Flip | −5.38 | SL1 hit | FL |
| MES 2m | 11/11 22:08 | L | LTF EMA20 Pierce | −1.75 | CBC flip | CL,FL,L5 |
| MES 2m | 11/12 11:28 | L | LTF EMA20 Pierce | −8.00 | SL1 hit | FL,X4,X6 |
| MES 2m | 11/12 12:20 | L | HTF EMA9 Pierce | −8.00 | SL1 hit | X4 |
| MES 2m | 11/12 14:08 | S | LTF EMA20 Pierce | −5.25 | CBC flip | CL |

## Suggested changes

None meet the rule this run (20+ setups for the case, evidence holds in both halves, not contradicted by the replay). There are no standing items from earlier days, and the MGC 3m revert flag can't be checked yet (count starts 11/13).

Not a settings change, but worth checking:

- **MGC 2m:** confirm only ONE CBC alert (v10.87+) is left on the chart. The last range-gate violation was 11/11 21:40, while duplicates were still arriving.

Done (not suggestions):

- MGC 3m 50 % / trail 3.5 (v10.84)
- MES 3m exits (SL1 3 / TP1 1.75)
- MGC 2m range + flop gate (v10.77)
- MES 3m flip-timing gate
- Bot windows, the 5-day short filter, the three-trigger bot set (v10.88) and the flip-only bot exit (v10.92)
- MES 2m flip counter and MTF gate
