## Week of 11/14/2026 summary

- STUDY SETTINGS STALE: the 11/13 settings sync (v10.96) lists 3 non-known MISMATCHes, NOT yet fixed in the project scripts, and they touch the 3m studies -- mes3_ema_grid LIVE still closes MES 3m 80/100 % by time of day (live since v10.95: 100 % at TP1 all day), and MGC 3m live is now FLIP 0 % (v10.96: nothing closed at TP1, BE, no trail, exit on HTF flip) while these replays use 80 % / trail 1.7 (MGCX) or 50 % / 3.5. Bot replay (H) is unaffected (part 1.0). Also new: the 11/14 X4 fix in mes3_ema_grid.py makes the MGC 3m VWAP-stretch gate actually block setups (MGC 3m 1193 setups vs 1707 last week), so MGC 3m numbers are not like-for-like with 11/09. Here: MES 3m replays use 80/100 % by time of day, not the live 100 % at TP1.
- Turning the MES 3m range gate off still loses in every single session: Asia -98, London -6 (thirds +49 / -25 / -30), NY -47; all three -151.
- Blocked setups (range gate): Asia 171 / -208, London 134 / -48, NY 135 / -247 (NYR5 z -2.8, thirds -138 / -61 / -48).
- Verdict: **keep the MES 3m range gate on in all sessions** (no single-session OFF row is ✓).

---

# MES 3m — entry gate off by session (11/14/2026)

Replay Jan 5 -> now, chop_sim rules, net after costs (0.50 pts/trade). Live gates = range gate (24 bars, top/bottom 20 %, < 5 ATR) (no stretch gate on MES 3m; the flip-timing gate is not modelled). "Off in X" = setups starting in that sub-session (ET: Asia 18:00-03:00, London 03:00-09:30, NY 09:30-16:00) are NOT gated; elsewhere the gate stays on. Δ vs gate on everywhere. ✓ = better in all three thirds.

## range gate — exits live (SL1 3 ATR / TP1 1.75 / 80-100 % by time): gate on everywhere = 1738 trades, net -822

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +113 | -9 | -38 | -51 | -18 | **-98** | -98 / +0 / +0 |  |
| London | +87 | +49 | -25 | -30 | +25 | **-6** | +0 / -6 / +0 |  |
| NY | +73 | -6 | -13 | -28 | +33 | **-47** | +0 / +0 / -47 |  |
| Asia + London | +200 | +40 | -63 | -81 | +8 | **-104** | -98 / -6 / +0 |  |
| Asia + NY | +186 | -15 | -51 | -79 | +15 | **-145** | -98 / +0 / -47 |  |
| London + NY | +160 | +42 | -38 | -58 | +58 | **-54** | +0 / -6 / -47 |  |
| Asia + London + NY | +273 | +33 | -76 | -109 | +41 | **-151** | -98 / -6 / -47 |  |

**Setups the gates block (gates off everywhere, exits live (SL1 3 ATR / TP1 1.75 / 80-100 % by time))** — trades / net / avg by session

| Session | Range-gated | Stretch-gated | Not gated |
|---|---|---|---|
| Asia | 171 / -208 / -1.22 | 154 / -58 / -0.37 | 449 / -13 / -0.03 |
| London | 134 / -48 / -0.36 | 173 / +43 / +0.25 | 349 / -271 / -0.78 |
| NY | 135 / -247 / -1.83 | 128 / -5 / -0.04 | 318 / -167 / -0.53 |
