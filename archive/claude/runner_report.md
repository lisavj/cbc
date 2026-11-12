## Week of 11/09/2026 summary

- STUDY SETTINGS STALE: the 11/08 settings sync report lists 1 non-known MISMATCH (chop_sim GATE MGC 2m range gate R5=0) + late_study MES 3m tp=2.0 -- both already fixed in the project scripts used for this run, and neither affects these 3m studies.
- MGC 3m WATCH (50 % at TP1 + trail 3.5 = live default since v10.84; replay base still 80 % / 1.7): 'with recommended rules' flip kept, trail 3.5, TP2 off, 50 % -> **Δ +366** (net +568; Δ thirds +168 / +10 / +188; net thirds +214 / +90 / +263; last 4 wk +160 vs +68), T4 -> **HELD** (11/08: Δ +353). Third 2 gain is thin (+10). Plain setups: Δ +283 (11/08 +271; flags '4', not all thirds).
- **Weeks held: MGC runner 50 % / 3.5 1/3.** No revert needed.
- MES 3m: still no runner variant better in all three thirds (0 of 47 on both baselines); walk-forward pick third 3 -28 (plain) / -35 (with rules). Keep MES runner as is.
- Note: the 11/08 report also carried a hand-run MGC edge check (trail 4.5 / 6, 35 / 65 % at TP1); it is not part of runner_study.py and was not rerun.

---

Staying in strong moves longer -- MES 3m and MGC 3m -- 11/08/2026.
The MFE study showed trades give back almost all of their best move, and 20 % (MES) / 31 % (MGC) run 1.5 x TP1 or more. This tests
what happens AFTER TP1 is hit (before TP1 nothing changes):
  flip  = keep  : the HTF CBC flip still closes the runner (current) | ignore : after TP1 the flip no longer closes it
  trail = x ATR : the trailing stop on the runner (current 1.7) -- 1.7 / 2.5 / 3.5
  TP2   = k x TP1 distance : close the runner there (off / 1.5 / 2 / 3)
  part  = share closed at TP1 : current (MES 80 % in 06-16 and 18-22:30 ET, else 100 %; MGC 80 %) or 50 %
Breakeven after TP1, the 16:00 exit and a new opposite setup still close the runner.
Run on two baselines: plain current setups, and with the recommended entry rules (MES: shorts only below the 5-day EMA + stop after
2 losses / 2 flip-outs when the previous 5 sessions lost + half SL1 if negative at 18 min; MGC: skip against VWAP + London stops
after its first loss). Net after costs (commission + 1 tick per trade, +1 tick for a rule exit); Δ vs the same baseline with current
runner exits. T = better in all three thirds, 4 = better in the last 4 weeks, R = T and every one-step neighbour (trail / TP2) better too.

## MES 3m

### plain setups — current runner exits: Third 1 -20, Third 2 -732, Third 3 -94, Last 4 wk +160, Whole -847

**Δ whole period after costs** (flags: T all thirds better, 4 last 4 weeks better, R = T + neighbours better)

| Flip after TP1 / part at TP1 | Trail | TP2 off | TP2 1.5x | TP2 2x | TP2 3x |
|---|---|---|---|---|---|
| kept / current % | 1.7 | current | +14 | -40 4 | -7 |
| kept / current % | 2.5 | -27 | +15 | -54 | -35 |
| kept / current % | 3.5 | -53 | +18 | -55 | -35 4 |
| kept / 50 % | 1.7 | -19 4 | +21 | -48 4 | -33 4 |
| kept / 50 % | 2.5 | +2 | +25 | -33 | -13 |
| kept / 50 % | 3.5 | +9 4 | +23 | -36 | +5 4 |
| ignored / current % | 1.7 | -3 | +14 | -41 4 | -9 |
| ignored / current % | 2.5 | -39 | +11 | -51 | -35 |
| ignored / current % | 3.5 | -46 | +13 | -42 | -37 4 |
| ignored / 50 % | 1.7 | -25 4 | +20 | -51 4 | -38 4 |
| ignored / 50 % | 2.5 | -3 | +27 | -24 | +3 |
| ignored / 50 % | 3.5 | +25 4 | +25 | -10 | +29 4 |

**Better in all three thirds: 0 of 47.** Top 8 (net after costs, Δ in brackets):

| Runner rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Flags |
|---|---|---|---|---|---|---|

Walk-forward: best on thirds 1-2 = **flip kept, trail 2.5, TP2 1.5x, 50 % at TP1** → third 3 Δ **-28** (rank 44 of 47; median -10).

One change at a time (Δ whole / third 3 / last 4 wk): ignore flip -3 / -1 / +0; trail 2.5 -27 / +12 / -8; trail 3.5 -53 / +15 / -16; TP2 1.5x +14 / -5 / -11; TP2 2x -40 / -5 / +0; TP2 3x -7 / -6 / -1; 50 % at TP1 -19 / +7 / +12

### with recommended rules — current runner exits: Third 1 +112, Third 2 -144, Third 3 +29, Last 4 wk +89, Whole -4

**Δ whole period after costs** (flags: T all thirds better, 4 last 4 weeks better, R = T + neighbours better)

| Flip after TP1 / part at TP1 | Trail | TP2 off | TP2 1.5x | TP2 2x | TP2 3x |
|---|---|---|---|---|---|
| kept / current % | 1.7 | current | +16 | -11 | -1 4 |
| kept / current % | 2.5 | -58 | +15 | -66 | -71 4 |
| kept / current % | 3.5 | -81 | +12 | -66 | -74 4 |
| kept / 50 % | 1.7 | -17 4 | +34 | -11 4 | -14 4 |
| kept / 50 % | 2.5 | -31 | +36 | -43 | -63 4 |
| kept / 50 % | 3.5 | -24 4 | +29 | -45 | -47 4 |
| ignored / current % | 1.7 | -1 | +16 | -11 | -2 4 |
| ignored / current % | 2.5 | -63 | +11 | -58 | -67 4 |
| ignored / current % | 3.5 | -122 | +8 | -58 | -90 4 |
| ignored / 50 % | 1.7 | -17 4 | +34 | -12 4 | -15 4 |
| ignored / 50 % | 2.5 | -10 | +39 | -22 | -37 4 |
| ignored / 50 % | 3.5 | -60 | +33 | -24 | -46 4 |

**Better in all three thirds: 0 of 47.** Top 8 (net after costs, Δ in brackets):

| Runner rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Flags |
|---|---|---|---|---|---|---|

Walk-forward: best on thirds 1-2 = **flip kept, trail 2.5, TP2 1.5x, 50 % at TP1** → third 3 Δ **-35** (rank 44 of 47; median -13).

One change at a time (Δ whole / third 3 / last 4 wk): ignore flip -1 / +0 / +0; trail 2.5 -58 / +9 / -2; trail 3.5 -81 / +2 / -5; TP2 1.5x +16 / -19 / -25; TP2 2x -11 / -6 / -8; TP2 3x -1 / +2 / +4; 50 % at TP1 -17 / -12 / +6

## MGC 3m

### plain setups — current runner exits: Third 1 -69, Third 2 -18, Third 3 -42, Last 4 wk +38, Whole -129

**Δ whole period after costs** (flags: T all thirds better, 4 last 4 weeks better, R = T + neighbours better)

| Flip after TP1 / part at TP1 | Trail | TP2 off | TP2 1.5x | TP2 2x | TP2 3x |
|---|---|---|---|---|---|
| kept / current % | 1.7 | current | -97 | -70 | -39 |
| kept / current % | 2.5 | +22 | -97 | -73 | -32 |
| kept / current % | 3.5 | +93 T | -97 | -70 | -33 |
| kept / 50 % | 1.7 | +60 4 | -92 | -96 | -31 4 |
| kept / 50 % | 2.5 | +190 T4 | -93 | -89 | -13 4 |
| kept / 50 % | 3.5 | +283 4 | -94 | -89 | -12 4 |
| ignored / current % | 1.7 | -1 4 | -97 | -71 | -36 |
| ignored / current % | 2.5 | +21 | -97 | -71 | -19 |
| ignored / current % | 3.5 | +110 T4 | -98 | -70 | -19 |
| ignored / 50 % | 1.7 | +66 4 | -92 | -98 | -24 4 |
| ignored / 50 % | 2.5 | +202 4 | -94 | -86 | +13 4 |
| ignored / 50 % | 3.5 | +298 4 | -95 | -89 | +8 4 |

**Better in all three thirds: 3 of 47.** Top 8 (net after costs, Δ in brackets):

| Runner rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Flags |
|---|---|---|---|---|---|---|
| flip kept, trail 2.5, TP2 off, 50 % at TP1 | +23 (+91) | -14 (+4) | +53 (+95) | +77 (+39) | +61 (+190) | T4 |
| flip ignored, trail 3.5, TP2 off, current % at TP1 | -40 (+29) | +12 (+30) | +9 (+51) | +59 (+21) | -19 (+110) | T4 |
| flip kept, trail 3.5, TP2 off, current % at TP1 | -40 (+29) | +17 (+35) | -13 (+29) | +35 (-3) | -36 (+93) | T |

Walk-forward: best on thirds 1-2 = **flip kept, trail 3.5, TP2 off, 50 % at TP1** → third 3 Δ **+146** (rank 2 of 47; median -10).

One change at a time (Δ whole / third 3 / last 4 wk): ignore flip -1 / -0 / +1; trail 2.5 +22 / -15 / -26; trail 3.5 +93 / +29 / -3; TP2 1.5x -97 / -47 / -51; TP2 2x -70 / -13 / -31; TP2 3x -39 / -3 / -14; 50 % at TP1 +60 / +55 / +66

### with recommended rules — current runner exits: Third 1 +46, Third 2 +81, Third 3 +75, Last 4 wk +68, Whole +202

**Δ whole period after costs** (flags: T all thirds better, 4 last 4 weeks better, R = T + neighbours better)

| Flip after TP1 / part at TP1 | Trail | TP2 off | TP2 1.5x | TP2 2x | TP2 3x |
|---|---|---|---|---|---|
| kept / current % | 1.7 | current | -143 | -117 | -95 |
| kept / current % | 2.5 | +57 T | -142 | -113 | -49 |
| kept / current % | 3.5 | +129 T4 | -142 | -110 | -63 |
| kept / 50 % | 1.7 | +90 4 | -143 | -125 | -96 4 |
| kept / 50 % | 2.5 | +251 T4 | -140 | -112 | -16 4 |
| kept / 50 % | 3.5 | +366 T4 | -141 | -112 | -25 4 |
| ignored / current % | 1.7 | -0 4 | -144 | -117 | -93 |
| ignored / current % | 2.5 | +48 T | -143 | -112 | -52 |
| ignored / current % | 3.5 | +143 T4 | -143 | -110 | -72 |
| ignored / 50 % | 1.7 | +98 4 | -145 | -125 | -90 4 |
| ignored / 50 % | 2.5 | +262 T4 | -143 | -108 | -11 4 |
| ignored / 50 % | 3.5 | +410 T4 | -144 | -110 | -30 |

**Better in all three thirds: 8 of 47.** Top 8 (net after costs, Δ in brackets):

| Runner rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Flags |
|---|---|---|---|---|---|---|
| flip ignored, trail 3.5, TP2 off, 50 % at TP1 | +241 (+195) | +109 (+28) | +262 (+187) | +169 (+102) | +612 (+410) | T4 |
| flip kept, trail 3.5, TP2 off, 50 % at TP1 | +214 (+168) | +90 (+10) | +263 (+188) | +160 (+92) | +568 (+366) | T4 |
| flip ignored, trail 2.5, TP2 off, 50 % at TP1 | +160 (+114) | +96 (+15) | +208 (+133) | +114 (+46) | +464 (+262) | T4 |
| flip kept, trail 2.5, TP2 off, 50 % at TP1 | +141 (+95) | +103 (+22) | +210 (+134) | +113 (+46) | +453 (+251) | T4 |
| flip ignored, trail 3.5, TP2 off, current % at TP1 | +103 (+57) | +127 (+47) | +115 (+40) | +87 (+19) | +345 (+143) | T4 |
| flip kept, trail 3.5, TP2 off, current % at TP1 | +87 (+41) | +122 (+41) | +123 (+47) | +83 (+16) | +331 (+129) | T4 |
| flip kept, trail 2.5, TP2 off, current % at TP1 | +51 (+5) | +124 (+44) | +84 (+9) | +59 (-8) | +259 (+57) | T |
| flip ignored, trail 2.5, TP2 off, current % at TP1 | +56 (+10) | +114 (+34) | +79 (+4) | +57 (-10) | +250 (+48) | T |

Walk-forward: best on thirds 1-2 = **flip ignored, trail 3.5, TP2 off, 50 % at TP1** → third 3 Δ **+187** (rank 2 of 47; median -7).

One change at a time (Δ whole / third 3 / last 4 wk): ignore flip -0 / -0 / +1; trail 2.5 +57 / +9 / -8; trail 3.5 +129 / +47 / +16; TP2 1.5x -143 / -41 / -38; TP2 2x -117 / -20 / -29; TP2 3x -95 / -7 / -14; 50 % at TP1 +90 / +63 / +55
