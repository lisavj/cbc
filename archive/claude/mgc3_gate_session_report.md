# MGC 3m — entry gate off by session (11/09/2026)

## Summary

- **It is session-specific, and it is the range gate.** Turning the range gate OFF in **NY only** (stretch gate still on) gains **+154** with live exits (50 % / trail 3.5), better in all three thirds (+96 / +25 / +32) and in the last 4 weeks (+15). With the old 80 % / 1.7 exits it gains +128, also ✓ in all thirds. It is the only setting that is ✓ for both exit sets.
- Turning it off in **London** hurts third 2 (−104) and the last 4 weeks (−27). In **Asia** it does nothing (+5). Adding London or Asia to NY adds a little in total but loses the ✓ (third 2 negative). **Keep the gate on in Asia and London.**
- The setups the range gate blocks (live exits): NY 106 trades **+101** (+0.95 per trade, better than NY's ungated setups at +0.17), London 155 trades −40, Asia 168 trades +23.
- How strong it is: the 106 NY setups alone come out at z ≈ 1.2, thirds +85 / +21 / −6, and +0.6 over the last 4 weeks (15 trades). The rest of the +154 comes from knock-on effects on other trades. **Promising, not robust**: by your usual rule, watch it for 3 weeks before changing CBC.
- **Stretch gate (VWAP > 4 ATR): keep it on in every session.** Turning it off loses or does nothing everywhere (NY −18, Asia −7; few setups).
- If it holds, the CBC change would be to exempt MGC 3m NY (09:30-16:00 ET) from the range gate. CBC has no such per-session input today, so this would need a Pine change.


Replay Jan 5 -> 11/09, chop_sim rules, net after costs (0.22 pts/trade). Live gates = range gate (24 bars, top/bottom 20 %, < 5 ATR) + VWAP stretch (> 4 ATR). "Off in X" = setups starting in that sub-session (ET: Asia 18:00-03:00, London 03:00-09:30, NY 09:30-16:00) are NOT gated; elsewhere the gate stays on. Δ vs gate on everywhere. ✓ = better in all three thirds.

## both gates (range + stretch) — exits live 50 % / trail 3.5: gate on everywhere = 1593 trades, net +154

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +102 | +35 | -35 | -0 | -5 | **-1** | -5 / +5 / +0 |  |
| London | +91 | +57 | -97 | +56 | -27 | **+15** | +0 / +18 / -3 |  |
| NY | +83 | +88 | +19 | +38 | +18 | **+144** | +0 / +0 / +144 | ✓ |
| Asia + London | +193 | +92 | -133 | +55 | -31 | **+15** | -5 / +23 / -3 |  |
| Asia + NY | +185 | +123 | -16 | +37 | +14 | **+144** | -5 / +5 / +144 |  |
| London + NY | +174 | +145 | -79 | +93 | -8 | **+160** | +0 / +18 / +142 |  |
| Asia + London + NY | +276 | +180 | -114 | +93 | -13 | **+159** | -5 / +23 / +142 |  |

## range gate only (stretch stays on) — exits live 50 % / trail 3.5: gate on everywhere = 1593 trades, net +154

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +96 | +42 | -47 | +10 | -5 | **+5** | -0 / +5 / +0 |  |
| London | +85 | +61 | -104 | +56 | -27 | **+14** | +0 / +16 / -3 |  |
| NY | +70 | +96 | +25 | +32 | +15 | **+154** | +0 / +0 / +154 | ✓ |
| Asia + London | +181 | +103 | -151 | +66 | -31 | **+18** | -0 / +21 / -3 |  |
| Asia + NY | +166 | +138 | -22 | +42 | +10 | **+158** | -0 / +5 / +154 |  |
| London + NY | +155 | +158 | -79 | +88 | -12 | **+167** | +0 / +16 / +151 |  |
| Asia + London + NY | +251 | +200 | -126 | +98 | -16 | **+172** | -0 / +21 / +151 |  |

## stretch gate only (range stays on) — exits live 50 % / trail 3.5: gate on everywhere = 1593 trades, net +154

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +5 | -7 | +10 | -10 | +0 | **-7** | -7 / +0 / +0 |  |
| London | +7 | -4 | +3 | +6 | -4 | **+4** | +0 / +4 / +0 |  |
| NY | +14 | -12 | -11 | +5 | +3 | **-18** | +0 / +0 / -18 |  |
| Asia + London | +12 | -12 | +14 | -5 | -4 | **-3** | -7 / +4 / +0 |  |
| Asia + NY | +19 | -20 | -1 | -5 | +3 | **-25** | -7 / +0 / -18 |  |
| London + NY | +21 | -17 | -8 | +11 | -1 | **-14** | +0 / +4 / -18 |  |
| Asia + London + NY | +26 | -24 | +2 | +1 | -1 | **-21** | -7 / +4 / -18 |  |

**Setups the gates block (gates off everywhere, exits live 50 % / trail 3.5)** — trades / net / avg by session

| Session | Range-gated | Stretch-gated | Not gated |
|---|---|---|---|
| Asia | 168 / +23 / +0.14 | 6 / +5 / +0.81 | 566 / +411 / +0.73 |
| London | 155 / -40 / -0.26 | 8 / +3 / +0.42 | 457 / -231 / -0.51 |
| NY | 106 / +101 / +0.95 | 18 / -24 / -1.33 | 385 / +65 / +0.17 |

## both gates (range + stretch) — exits old 80 % / trail 1.7: gate on everywhere = 1707 trades, net -129

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +122 | +20 | -65 | +21 | -15 | **-24** | -26 / +2 / +0 |  |
| London | +106 | +75 | -103 | +52 | -23 | **+24** | +0 / +24 / +0 |  |
| NY | +92 | +46 | +28 | +43 | +30 | **+118** | +0 / +0 / +118 | ✓ |
| Asia + London | +228 | +95 | -168 | +73 | -38 | **-1** | -26 / +26 / +0 |  |
| Asia + NY | +214 | +66 | -37 | +64 | +15 | **+93** | -26 / +2 / +118 |  |
| London + NY | +198 | +121 | -75 | +95 | +6 | **+141** | +0 / +24 / +118 |  |
| Asia + London + NY | +320 | +141 | -139 | +116 | -9 | **+117** | -26 / +26 / +118 |  |

## range gate only (stretch stays on) — exits old 80 % / trail 1.7: gate on everywhere = 1707 trades, net -129

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +111 | +33 | -62 | +34 | -8 | **+5** | +3 / +2 / +0 |  |
| London | +96 | +78 | -112 | +57 | -18 | **+24** | +0 / +24 / +0 |  |
| NY | +74 | +50 | +39 | +39 | +26 | **+128** | +0 / +0 / +128 | ✓ |
| Asia + London | +207 | +112 | -174 | +92 | -25 | **+29** | +3 / +26 / +0 |  |
| Asia + NY | +185 | +83 | -23 | +73 | +19 | **+133** | +3 / +2 / +128 |  |
| London + NY | +170 | +128 | -73 | +96 | +9 | **+152** | +0 / +24 / +128 |  |
| Asia + London + NY | +281 | +162 | -135 | +131 | +1 | **+157** | +3 / +26 / +128 |  |

## stretch gate only (range stays on) — exits old 80 % / trail 1.7: gate on everywhere = 1707 trades, net -129

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +10 | -13 | -1 | -17 | -7 | **-31** | -31 / +0 / +0 |  |
| London | +12 | -4 | +6 | -3 | -10 | **-1** | +0 / -1 / +0 |  |
| NY | +19 | -6 | -16 | +4 | +3 | **-18** | +0 / +0 / -18 |  |
| Asia + London | +22 | -17 | +5 | -21 | -17 | **-32** | -31 / -1 / +0 |  |
| Asia + NY | +29 | -20 | -17 | -13 | -4 | **-49** | -31 / +0 / -18 |  |
| London + NY | +31 | -10 | -10 | +1 | -7 | **-19** | +0 / -1 / -18 |  |
| Asia + London + NY | +41 | -23 | -11 | -16 | -14 | **-50** | -31 / -1 / -18 |  |

**Setups the gates block (gates off everywhere, exits old 80 % / trail 1.7)** — trades / net / avg by session

| Session | Range-gated | Stretch-gated | Not gated |
|---|---|---|---|
| Asia | 172 / +39 / +0.23 | 11 / -17 / -1.59 | 620 / +145 / +0.23 |
| London | 156 / -5 / -0.03 | 13 / -1 / -0.10 | 509 / -304 / -0.60 |
| NY | 107 / +68 / +0.63 | 22 / -22 / -1.00 | 417 / +86 / +0.21 |
