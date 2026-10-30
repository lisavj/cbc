# ER filter re-run — MGC (10/29/2026 routine)

**Data:** al.json pulled 10/29 14:08 UTC (server keeps only the last ~18.4k alerts → MGC alerts cover **10/19 03:45 – 10/29 09:57 ET** only; 10/12–10/18 has rolled off). mgc60.json = 20,052 3m bars, 8/30 – 10/29.
**Script changes:** regex now `Time: MM/DD` (any month); CBC Flip regex accepts any `HTF(n)`. Everything else (ATR14 RMA, ER12 on 3m closes, sim: SL clamp 5–7, TP1 min(1.7×ATR,6), 80% at TP1, BE + 1.7×ATR trail, exit on HTF flip / 17:00) unchanged.
**Caveat:** alerts now come from a **2m** chart while bars are 3m. The original exact-timestamp match keeps only 439 of 757 triggers (those landing on a 3m boundary). A "floor" variant (map to the 3m bar containing the alert) keeps all 757 but has up to ~1–2 min look-ahead on entry. Exact match is the primary result.

## 1. Replay (simulated) — exact match, n=439

| ER band | n | win % | total pts | avg |
|---|---|---|---|---|
| < 0.18 | 204 | 46.1 | −106.6 | **−0.52** |
| 0.18–0.23 | 53 | 54.7 | +52.8 | **+1.00** |
| ≥ 0.23 | 182 | 55.5 | +58.2 | **+0.32** |
| ALL | 439 | 51.0 | +4.4 | +0.01 |
| 0.23–0.30 | 67 | 52.2 | −2.0 | −0.03 |
| 0.30–0.40 | 58 | 62.1 | +77.3 | +1.33 |
| 0.40–0.50 | 28 | 53.6 | −4.2 | −0.15 |
| 0.50–0.70 | 26 | 53.8 | −4.9 | −0.19 |
| 0.70+ | 3 | 33.3 | −7.9 | −2.65 |

Floor variant (n=757): <0.18 −0.15 (n=360), 0.18–0.23 +0.93 (n=88), ≥0.23 +0.50 (n=309); fine: 0.23–0.30 −0.17, 0.30–0.40 +1.57, 0.40–0.50 −0.93, 0.50–0.70 +1.26, 0.70+ −0.58 (n=7). Same shape.

**By trigger (exact; avg pts <0.18 / 0.18–0.23 / ≥0.23):**
- HTF CBC Flip (n=138): −0.32 / −0.79 / −0.52 — no ER edge, net −64.6
- HTF EMA20 Pierce (n=66): −1.04 / +0.64 / +1.02
- HTF EMA9 Pierce (n=118): −0.29 / +0.80 / +1.01
- LTF EMA20 Pierce (n=117): −0.67 / +2.94 (n=15) / +0.58

## 2. Actual MGC Trade Setups (alerts, ER from Filters line, result from matching Setup Ended)

161 setups, 143 matched to a Setup Ended (18 open/unmatched; a few duplicate setup alerts are counted twice).

| ER band | n | win % | total | avg |
|---|---|---|---|---|
| < 0.18 | 37 | 37.8 | −33.7 | −0.91 |
| 0.18–0.23 | 15 | 53.3 | +5.2 | +0.34 |
| 0.23–0.30 | 34 | 52.9 | −2.6 | −0.08 |
| 0.30–0.40 | 29 | 48.3 | −1.1 | −0.04 |
| 0.40–0.50 | 15 | 46.7 | −14.5 | −0.97 |
| 0.50–0.70 | 12 | 58.3 | −1.3 | −0.11 |
| 0.70+ | 1 | 0 | −5.1 | −5.07 |
| **≥ 0.23** | 91 | 50.5 | −24.6 | −0.27 |
| **≥ 0.40** | 28 | 50.0 | −20.9 | −0.75 |

By trigger (actual): HTF CBC Flip n=33 (all ER ≥0.23) +2.3, 61% win; HTF EMA9 Pierce n=14 +5.4 (≥0.23: +15.8, n=11); HTF EMA20 Pierce n=14 −2.5; **LTF EMA20 Pierce n=81 −51.4, 40% win** (≥0.40: −28.8, n=9). Note: Pierce setups fire with ER < 0.23, so the ER gate currently only appears to apply to CBC Flip setups.

## 3. Versus 10/12–10/15 baseline
Baseline replay: <0.18 −2.21 (n=49), 0.18–0.23 −1.53 (n=16), ≥0.23 −1.12 (n=51). Now: −0.52 / +1.00 / +0.32. The "<0.18 is worst" ranking holds; 0.18–0.23 flipped from bad to the best band. The baseline finding that actual setups at ER ≥0.40 were 5/6 winners (+12.4) **did not repeat**: ≥0.40 was 14/28 winners, −20.9.

## Recommendation
- Evidence still supports filtering **ER < 0.18** (worst band in both replay runs and in actual setups).
- Evidence does **not** support keeping the cut at 0.23 over 0.18, nor raising it to 0.40: 0.18–0.23 was positive in both replay variants (n=53/88) and actual (n=15), and the ≥0.40 edge from the baseline vanished. The fine-band pattern (0.30–0.40 strong, neighbours flat/negative) looks like noise.
- Reasonable action: **keep 0.23 for now, or test lowering to ~0.18**; do not raise it. ER is not the lever for LTF EMA20 Pierce setups — they lost across all bands (−51 pts); trigger choice matters more than ER here.
- Caveats: ~8 trading days, one regime (gold falling ~4200→4000), replay ≠ live exits, 2m alerts vs 3m bars, wide band-to-band variance (±1 pt avg on n≈30). Treat as directional only.
