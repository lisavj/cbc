## Week of 11/14/2026 summary

- STUDY SETTINGS STALE: the 11/13 settings sync (v10.96) lists 3 non-known MISMATCHes, NOT yet fixed in the project scripts, and they touch the 3m studies -- mes3_ema_grid LIVE still closes MES 3m 80/100 % by time of day (live since v10.95: 100 % at TP1 all day), and MGC 3m live is now FLIP 0 % (v10.96: nothing closed at TP1, BE, no trail, exit on HTF flip) while these replays use 80 % / trail 1.7 (MGCX) or 50 % / 3.5. Bot replay (H) is unaffected (part 1.0). Also new: the 11/14 X4 fix in mes3_ema_grid.py makes the MGC 3m VWAP-stretch gate actually block setups (MGC 3m 1193 setups vs 1707 last week), so MGC 3m numbers are not like-for-like with 11/09.
- NOTE: since CBC v10.96 (11/13) MGC 3m live is FLIP 0 % (not 50 % / trail 3.5); this replay still measures 50 % / 3.5 vs 80 % / 1.7 and does not model FLIP 0 %. MGC 3m live alerts 11/09-11/12 were partly on old exits (data note 2).
- MGC 3m watch "flip kept, trail 3.5, TP2 off, 50 % at TP1", with recommended rules: **Δ +285** (net +559; Δ thirds +150 / +28 / +108; last 4 wk +163 vs +117) vs 11/09 Δ +366 -> **HELD** (-22 %, all thirds and last 4 weeks better). Weeks held 2/3. Plain setups: Δ +244 (thirds +128 / +17 / +99), T4. Walk-forward picks "flip ignored, trail 3.5, 50 %" (third 3 +142, rank 1 of 47).
- No revert flag: 50 % / 3.5 still beats 80 % / 1.7 in every third. Whether FLIP 0 % beats 50 % / 3.5 is not tested here.
- MES 3m: still **no runner variant better in all three thirds** (0 of 47 on both baselines) -> keep MES runner exits.

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

### plain setups — current runner exits: Third 1 -20, Third 2 -733, Third 3 -68, Last 4 wk +124, Whole -822

**Δ whole period after costs** (flags: T all thirds better, 4 last 4 weeks better, R = T + neighbours better)

| Flip after TP1 / part at TP1 | Trail | TP2 off | TP2 1.5x | TP2 2x | TP2 3x |
|---|---|---|---|---|---|
| kept / current % | 1.7 | current | +9 | -45 | -18 |
| kept / current % | 2.5 | -35 | +2 | -63 | -54 |
| kept / current % | 3.5 | -60 | +5 | -63 | -43 |
| kept / 50 % | 1.7 | -17 4 | +10 | -58 | -58 |
| kept / 50 % | 2.5 | -9 | +16 | -46 | -49 |
| kept / 50 % | 3.5 | +16 4 | +15 | -46 | -5 |
| ignored / current % | 1.7 | -3 | +9 | -46 | -20 |
| ignored / current % | 2.5 | -48 | -2 | -60 | -53 |
| ignored / current % | 3.5 | -50 | +0 | -51 | -42 |
| ignored / 50 % | 1.7 | -22 4 | +9 | -61 | -64 |
| ignored / 50 % | 2.5 | -14 | +18 | -37 | -33 |
| ignored / 50 % | 3.5 | +24 | +16 | -21 | +13 |

**Better in all three thirds: 0 of 47.** Top 8 (net after costs, Δ in brackets):

| Runner rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Flags |
|---|---|---|---|---|---|---|

Walk-forward: best on thirds 1-2 = **flip ignored, trail 2.5, TP2 1.5x, 50 % at TP1** → third 3 Δ **-42** (rank 40 of 47; median -25).

One change at a time (Δ whole / third 3 / last 4 wk): ignore flip -3 / -1 / +0; trail 2.5 -35 / +2 / -20; trail 3.5 -60 / +6 / -34; TP2 1.5x +9 / -14 / -30; TP2 2x -45 / -11 / -18; TP2 3x -18 / -20 / -18; 50 % at TP1 -17 / +12 / +16

### with recommended rules — current runner exits: Third 1 +112, Third 2 -116, Third 3 -31, Last 4 wk +7, Whole -36

**Δ whole period after costs** (flags: T all thirds better, 4 last 4 weeks better, R = T + neighbours better)

| Flip after TP1 / part at TP1 | Trail | TP2 off | TP2 1.5x | TP2 2x | TP2 3x |
|---|---|---|---|---|---|
| kept / current % | 1.7 | current | +21 | -10 | -1 |
| kept / current % | 2.5 | -60 | +12 | -66 | -73 |
| kept / current % | 3.5 | -81 | +9 | -64 | -74 4 |
| kept / 50 % | 1.7 | -31 | +32 | -21 | -28 |
| kept / 50 % | 2.5 | -45 | +36 | -53 | -77 |
| kept / 50 % | 3.5 | -35 4 | +30 | -51 | -57 4 |
| ignored / current % | 1.7 | -1 | +20 | -10 | -2 |
| ignored / current % | 2.5 | -65 | +8 | -58 | -68 |
| ignored / current % | 3.5 | -118 | +5 | -57 | -87 4 |
| ignored / 50 % | 1.7 | -30 | +32 | -22 | -29 |
| ignored / 50 % | 2.5 | -24 | +39 | -31 | -52 |
| ignored / 50 % | 3.5 | -72 | +33 | -31 | -58 4 |

**Better in all three thirds: 0 of 47.** Top 8 (net after costs, Δ in brackets):

| Runner rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Flags |
|---|---|---|---|---|---|---|

Walk-forward: best on thirds 1-2 = **flip ignored, trail 2.5, TP2 1.5x, 50 % at TP1** → third 3 Δ **-39** (rank 40 of 47; median -22).

One change at a time (Δ whole / third 3 / last 4 wk): ignore flip -1 / +0 / +0; trail 2.5 -60 / +6 / -1; trail 3.5 -81 / -0 / -11; TP2 1.5x +21 / -18 / -15; TP2 2x -10 / -6 / -8; TP2 3x -1 / -1 / -2; 50 % at TP1 -31 / -22 / -6

## MGC 3m

### plain setups — current runner exits: Third 1 -10, Third 2 -7, Third 3 +72, Last 4 wk +101, Whole +55

**Δ whole period after costs** (flags: T all thirds better, 4 last 4 weeks better, R = T + neighbours better)

| Flip after TP1 / part at TP1 | Trail | TP2 off | TP2 1.5x | TP2 2x | TP2 3x |
|---|---|---|---|---|---|
| kept / current % | 1.7 | current | -90 | -73 | -36 |
| kept / current % | 2.5 | +33 | -89 | -64 | -11 |
| kept / current % | 3.5 | +63 T | -89 | -60 | -13 |
| kept / 50 % | 1.7 | +81 4 | -87 | -77 | +5 4 |
| kept / 50 % | 2.5 | +176 4 | -85 | -47 | +33 4 |
| kept / 50 % | 3.5 | +244 T4 | -85 | -45 | +29 |
| ignored / current % | 1.7 | +6 4 | -91 | -76 | -34 |
| ignored / current % | 2.5 | +55 T | -90 | -67 | -2 |
| ignored / current % | 3.5 | +129 T4 | -90 | -63 | +2 |
| ignored / 50 % | 1.7 | +96 4 | -89 | -84 | +10 4 |
| ignored / 50 % | 2.5 | +202 T4 | -86 | -54 | +56 T4 |
| ignored / 50 % | 3.5 | +333 T4 | -87 | -53 | +56 T4 |

**Better in all three thirds: 8 of 47.** Top 8 (net after costs, Δ in brackets):

| Runner rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Flags |
|---|---|---|---|---|---|---|
| flip ignored, trail 3.5, TP2 off, 50 % at TP1 | +131 (+141) | +39 (+46) | +218 (+146) | +191 (+90) | +388 (+333) | T4 |
| flip kept, trail 3.5, TP2 off, 50 % at TP1 | +118 (+128) | +10 (+17) | +171 (+99) | +166 (+65) | +299 (+244) | T4 |
| flip ignored, trail 2.5, TP2 off, 50 % at TP1 | +67 (+77) | -1 (+6) | +191 (+119) | +166 (+65) | +257 (+202) | T4 |
| flip ignored, trail 3.5, TP2 off, current % at TP1 | +36 (+46) | +29 (+36) | +118 (+46) | +106 (+5) | +183 (+129) | T4 |
| flip kept, trail 3.5, TP2 off, current % at TP1 | +15 (+25) | +15 (+22) | +88 (+16) | +93 (-8) | +118 (+63) | T |
| flip ignored, trail 2.5, TP2 3.0x, 50 % at TP1 | +28 (+38) | -7 (+0) | +90 (+18) | +102 (+1) | +111 (+56) | T4 |
| flip ignored, trail 3.5, TP2 3.0x, 50 % at TP1 | +32 (+42) | +1 (+8) | +77 (+5) | +102 (+1) | +110 (+56) | T4 |
| flip ignored, trail 2.5, TP2 off, current % at TP1 | -3 (+7) | +15 (+22) | +99 (+27) | +96 (-5) | +110 (+55) | T |

Walk-forward: best on thirds 1-2 = **flip ignored, trail 3.5, TP2 off, 50 % at TP1** → third 3 Δ **+146** (rank 1 of 47; median -30).

One change at a time (Δ whole / third 3 / last 4 wk): ignore flip +6 / -0 / +1; trail 2.5 +33 / +24 / -9; trail 3.5 +63 / +16 / -8; TP2 1.5x -90 / -51 / -37; TP2 2x -73 / -38 / -27; TP2 3x -36 / -11 / -15; 50 % at TP1 +81 / +52 / +53

### with recommended rules — current runner exits: Third 1 +79, Third 2 +38, Third 3 +157, Last 4 wk +117, Whole +274

**Δ whole period after costs** (flags: T all thirds better, 4 last 4 weeks better, R = T + neighbours better)

| Flip after TP1 / part at TP1 | Trail | TP2 off | TP2 1.5x | TP2 2x | TP2 3x |
|---|---|---|---|---|---|
| kept / current % | 1.7 | current | -117 | -99 | -62 |
| kept / current % | 2.5 | +68 T | -115 | -92 | -21 |
| kept / current % | 3.5 | +104 T | -115 | -88 | -27 |
| kept / 50 % | 1.7 | +79 4 | -114 | -99 | -40 4 |
| kept / 50 % | 2.5 | +192 T4 | -109 | -74 | +18 |
| kept / 50 % | 3.5 | +285 T4 | -109 | -72 | +11 |
| ignored / current % | 1.7 | +7 4 | -119 | -101 | -61 |
| ignored / current % | 2.5 | +89 T4 | -116 | -93 | -15 |
| ignored / current % | 3.5 | +178 T4 | -117 | -89 | -23 |
| ignored / 50 % | 1.7 | +96 4 | -118 | -103 | -36 4 |
| ignored / 50 % | 2.5 | +227 T4 | -112 | -77 | +32 |
| ignored / 50 % | 3.5 | +414 T4 | -113 | -76 | +25 |

**Better in all three thirds: 8 of 47.** Top 8 (net after costs, Δ in brackets):

| Runner rule | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Flags |
|---|---|---|---|---|---|---|
| flip ignored, trail 3.5, TP2 off, 50 % at TP1 | +262 (+183) | +127 (+88) | +298 (+142) | +177 (+59) | +687 (+414) | T4 |
| flip kept, trail 3.5, TP2 off, 50 % at TP1 | +229 (+150) | +66 (+28) | +264 (+108) | +163 (+46) | +559 (+285) | T4 |
| flip ignored, trail 2.5, TP2 off, 50 % at TP1 | +164 (+85) | +65 (+27) | +272 (+116) | +162 (+45) | +501 (+227) | T4 |
| flip kept, trail 2.5, TP2 off, 50 % at TP1 | +147 (+68) | +50 (+12) | +268 (+112) | +154 (+37) | +466 (+192) | T4 |
| flip ignored, trail 3.5, TP2 off, current % at TP1 | +142 (+63) | +102 (+63) | +207 (+51) | +122 (+5) | +451 (+178) | T4 |
| flip kept, trail 3.5, TP2 off, current % at TP1 | +117 (+39) | +72 (+34) | +189 (+32) | +116 (-1) | +378 (+104) | T |
| flip ignored, trail 2.5, TP2 off, current % at TP1 | +93 (+14) | +76 (+37) | +194 (+38) | +120 (+3) | +363 (+89) | T4 |
| flip kept, trail 2.5, TP2 off, current % at TP1 | +82 (+3) | +67 (+28) | +193 (+36) | +116 (-1) | +342 (+68) | T |

Walk-forward: best on thirds 1-2 = **flip ignored, trail 3.5, TP2 off, 50 % at TP1** → third 3 Δ **+142** (rank 1 of 47; median -31).

One change at a time (Δ whole / third 3 / last 4 wk): ignore flip +7 / -0 / +1; trail 2.5 +68 / +36 / -1; trail 3.5 +104 / +32 / -1; TP2 1.5x -117 / -47 / -26; TP2 2x -99 / -35 / -19; TP2 3x -62 / -10 / -11; 50 % at TP1 +79 / +37 / +33
