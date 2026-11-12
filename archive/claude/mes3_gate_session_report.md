# MES 3m — entry gate off by session (11/09/2026)

## Summary

- **The MES 3m range gate is NOT session-specific: it helps in every session. Keep it on everywhere.** Turning it off loses money in every session and every combination: Asia −89, London −23, NY −84, all three −195. Third 3 and the last 4 weeks are negative in every row.
- The setups the gate blocks lose everywhere: Asia 170 trades −199 (−1.17 per trade), London 133 −52 (−0.39), NY 132 −293 (−2.22; z −3.4, negative in all thirds −138 / −89 / −66). They are worse than the setups the gate lets through in every session (−0.11 / −0.53 / −0.55 per trade).
- This is the opposite of MGC 3m, where the range-gated NY setups are profitable (+0.95 per trade) and turning the gate off in NY gains +154.
- Side note: MES setups stretched more than 4 ATR from VWAP (which no MES gate blocks) are positive in every session (+19 / +11 / +31, 52 trades), so a MES stretch gate would not help.
- Exits: live MES 3m (SL1 3 ATR min 5, TP1 1.75 ATR, 80/100 % by time of day); costs 0.50 per trade. The v10.81 flip-timing gate is not modelled.


Replay Jan 5 -> now, chop_sim rules, net after costs (0.50 pts/trade). Live gates = range gate (24 bars, top/bottom 20 %, < 5 ATR) (no stretch gate on MES 3m; the flip-timing gate is not modelled). "Off in X" = setups starting in that sub-session (ET: Asia 18:00-03:00, London 03:00-09:30, NY 09:30-16:00) are NOT gated; elsewhere the gate stays on. Δ vs gate on everywhere. ✓ = better in all three thirds.

## range gate — exits live (SL1 3 ATR / TP1 1.75 / 80-100 % by time): gate on everywhere = 1706 trades, net -847

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +112 | -9 | -25 | -55 | -6 | **-89** | -89 / +0 / +0 |  |
| London | +86 | +49 | -25 | -46 | -12 | **-23** | +0 / -23 / +0 |  |
| NY | +71 | -6 | -31 | -46 | -4 | **-84** | +0 / +0 / -84 |  |
| Asia + London | +198 | +40 | -50 | -102 | -19 | **-112** | -89 / -23 / +0 |  |
| Asia + NY | +183 | -15 | -56 | -102 | -11 | **-173** | -89 / +0 / -84 |  |
| London + NY | +157 | +42 | -56 | -93 | -17 | **-106** | +0 / -23 / -84 |  |
| Asia + London + NY | +269 | +33 | -81 | -148 | -23 | **-195** | -89 / -23 / -84 |  |

**Setups the gates block (gates off everywhere, exits live (SL1 3 ATR / TP1 1.75 / 80-100 % by time))** — trades / net / avg by session

| Session | Range-gated | Stretched > 4 ATR from VWAP (NOT gated on MES 3m, info only) | Neither |
|---|---|---|---|
| Asia | 170 / -199 / -1.17 | 17 / +19 / +1.11 | 574 / -66 / -0.11 |
| London | 133 / -52 / -0.39 | 18 / +11 / +0.59 | 496 / -262 / -0.53 |
| NY | 132 / -293 / -2.22 | 17 / +31 / +1.81 | 418 / -231 / -0.55 |
