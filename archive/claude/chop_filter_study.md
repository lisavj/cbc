# Chop filter study (ER + alternatives) — 10/24/2026

**Question:** is the Efficiency Ratio (ER) chop filter set right, and does any other chop filter do better?
**Data:** Databento 1m bars rebuilt to 2m / 3m (Jan 5 → Oct 23 2026, server archive), plus the real alerts 10/19–10/23.
**Simulator:** `claude/chop_sim.py`. It approximates the CBC v10.35 setup engine:
- Triggers: HTF CBC Flip (side gate, VWAP slope, flip-distance limit, flip ER minimum), LTF EMA20 Pierce, HTF EMA9 / EMA20 Pierce, each with the 1-bar late confirm.
- Rules: flip side AWAY only; 10-candle cooldown; one live setup per direction; an opposite setup replaces the live one; no setups 16:00–18:30 or while an opening range is forming; VWAP reclaim block.
- Case gates: R5 / X4 / MES 2m MTF gate.
- Exits: v10.31 per case.
- HTF EMA9/20 are taken as seen live, without look-ahead. A first run that used the final 15m values made results look far better, so the look-ahead had to go.
- Check against the real alerts 10/19–10/23: similar setup counts per case, but only about 50 % of real setups are matched exactly (same candle and direction). Treat the absolute numbers as approximate and the comparisons between settings as the useful part.

**Current settings (v10.35):**
- ER length 12, block below 0.23.
- Breakout exception: close through the last swing high/low or an opening-range high/low, for 3 bars.
- Per-trigger ER minimums: LTF EMA20 0.08, HTF EMA9 / EMA20 0.15.
- HTF flip ER minimum 0.23.

## Results (replay Jan–Oct; Δ = change in net points vs current; thirds = Jan–Mar / Apr–Jun / Jul–Oct)

| Setting | MGC 3m (1,133 setups) | MES 3m (1,663) | MGC 2m (2,826) | MES 2m (2,194) |
|---|---|---|---|---|
| Current, net | +181 | −53 | +413 | −47 |
| ER filter OFF (breakout exception irrelevant) | +22 | −49 | −29 | −47 |
| ER 0.15 / 0.20 / 0.26 / 0.30 | −1 / +34 / +24 / +53 | −28 / −6 / −14 / +30 | −124 / −76 / −15 / +14 | +9 / −91 / +4 / −50 |
| ER 0.40 (+ breakout) | +91 (3/3) | +66 (3/3) | +108 (3/3) | +68 (2/3) |
| **Remove breakout exception** | **−257** | −2 | **−324** | −69 |
| Flip ER minimum 0 (vs 0.23) | −48 | −4 | **−156 (0/3)** | −8 |
| ER length 16/20/30 (general filter only) | +57 / +20 / +82 | −6 / −110 / −69 | +144 / +150 / +130 | +231 / +94 / +200 |
| ER length 16 for **all** ER uses (incl. flip / trigger minimums) | +18 | +8 | +97 | −80 |
| + block EMA20/VWAP crosses ≥ 5 (12 bars) | +129 (3/3) | +162 (3/3) | +124 (2/3) | −20 |
| + block CHOP > 61.8 | −11 | +97 (3/3) | +26 | +62 (3/3) |
| + block ADX < 15/20, slope, range, HTF ER, low ATR | mixed / mostly negative in every case | | | |

**Noise:** one trade's result has a standard deviation of about 4.6–6.8 points. A change touching ~200–500 trades therefore moves net by ±70–150 points by chance (z ≈ 1). Only two things clear that bar:
- The breakout exception: z ≈ −1.8 / −2.0 on MGC when it is removed.
- Crosses ≥ 5 on MES 3m: z ≈ +2.4. That comes from about 80 settings tried, so it is borderline.

## Real alerts 10/19–10/23 (they already passed the current filter; blocked count / net of blocked)

| Extra block | MGC 3m (22) | MES 3m (41) | MGC 2m (34) | MES 2m (50) |
|---|---|---|---|---|
| ER12 < 0.30 | 16 / +10.3 (h1 −3.0, h2 +13.4) | 16 / −17.3 (both halves −) | 18 / −7.0 | 26 / −46.9 (both −) |
| Crosses ≥ 5 | 0 | 3 / **+8.5 (blocks winners)** | 4 / −8.8 (h1 only) | 10 / −45.1 (both −) |
| CHOP > 61.8 | 1 / +6.6 | 4 / −2.8 | 2 / −0.4 | 3 / +2.5 |
| ER16 < 0.20 | 11 / +19.7 | 20 / +4.9 | 22 / +6.6 (mixed halves) | 29 / −27.0 (both −) |

The real data is only 5 days. Its direction often disagrees with the replay (crosses: MES 3m vs MES 2m).

## Verdict

- **ER threshold 0.23: keep.** The filter is close to neutral in the replay: turning it off or moving the threshold between 0.15 and 0.30 changes net by less than noise in all four cases. 0.40 looks better in the replay for every case, but every gain is below z 1. On real data it would block 16 of 22 MGC 3m setups, net +10 of winners.
- **Breakout exception: keep. It does most of the work.** Low-ER setups that are breakouts (through a swing or opening-range high/low) are profitable. Without the exception, net drops by 260–320 points on MGC 3m and MGC 2m.
- **HTF flip ER minimum 0.23: keep.** Removing it costs MGC 2m 156 points, worse in all three thirds.
- **ER length on 2m charts:** 12 bars on a 2m chart is only 24 minutes, versus 36 minutes on 3m. A longer ER helps the general filter on both 2m cases in the replay (MES 2m length 16: +231, 3/3 thirds). But if the whole "Chop filters length" input is set to 16 (which also changes the flip and trigger minimums), MES 2m turns negative (−80). The result depends on details, so it is **not suggested**. Watch item.
- **Alternatives:**
  - No other chop filter is robust across cases.
  - EMA20/VWAP crosses ≥ 5 is the best replay candidate for the 3m charts (+129 / +162, 3/3 thirds), but it hurts MES 2m. On real MES 3m it blocked winners. Watch item, not adopted.
  - CHOP > 61.8 is small and mixed.
  - ADX, HTF EMA20 slope, N-bar range, HTF ER and low-ATR filters are inconsistent or negative.
- **Re-check when** each 3m case has about 40+ real setups that carry crosses / CHOP values in the alert's Filters line (needs ~2 more weeks).
