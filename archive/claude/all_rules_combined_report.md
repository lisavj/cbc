## Week of 11/09/2026 summary

- STUDY SETTINGS STALE: the 11/08 settings sync report lists 1 non-known MISMATCH (chop_sim GATE MGC 2m range gate R5=0) + late_study MES 3m tp=2.0 -- both already fixed in the project scripts used for this run, and neither affects these 3m studies.
- MGC 3m 'London stop after 1st loss' alone (— / stop / current exits): net **+97**, beyond random +84 / +92 / +31, last 4 wk +55 vs +38 -> **HELD** (11/08: +89; +83 / +98 / +24).
- MGC 3m VWAP + London stop (filter / stop / current exits): net **+202**, beyond random +103 / +89 / +108, last 4 wk +68 vs +38 -> **HELD** (11/08 +193). MGC filter / stop / TP + SL rules +275 (11/08 +266).
- MES 3m balanced (filter / stop / SL rule): net **-4** (thirds +112 / -144 / +29; beyond random +50 / +439 / **+2**), last 4 wk +89 vs current +160 (44 % below, limit 40 %) -> **WEAKER** (11/08: +11, last 4 wk +106 vs +176).
- **Weeks held: MGC London stop 1/3, MGC VWAP+London 1/3, MES balanced set 0/3.**
- Also rewritten this run (read skip_why.pkl): skip_fix.md and sess_loss_report.md (local working copies only).

---

Everything together, MES 3m and MGC 3m -- 11/08/2026.
Entry filter x session stop x exit rules, all in one replay (net after costs; gain beyond random skipping in brackets).
MES 3m: filter = skip shorts when price is below... above the 5-day EMA rule (shorts only when price is below the 5-day EMA of session closes);
        stop = 2 losses in a row or 2 flip-outs per 18-18 session, ONLY when the previous 5 sessions lost (regime switch);
        TP rule = TP1 -> 85 % after 18 min; SL rule = SL1 to half its distance if negative at 18 min.
MGC 3m: filter = skip setups against VWAP; stop = London (03:00-09:30 ET) stops after its first loss;
        TP rule = TP1 -> 65 % after 21 min; SL rule = close if under 25 % of TP1 at 18 min.
Costs: commission + 1 tick per trade (MES 0.50 / MGC 0.22), +1 tick for a rule exit at the candle close.

## MES 3m

Filter / session stop / exits. ✓ = beyond random positive in all three thirds; ↑ = last 4 weeks not worse than current exits.

| Filter / stop / exits | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|
| filter / stop / TP + SL rules | +140 (+88) | -131 (+457) | -9 (-28) | +46 (-124) | -0 (+517) | 1042 |  |
| filter / stop / SL rule | +112 (+50) | -144 (+439) | +29 (+2) | +89 (-86) | -4 (+491) | 997 | ✓ |
| filter / stop / TP rule | +97 (+44) | -184 (+402) | +45 (+24) | +98 (-74) | -42 (+471) | 1032 | ✓ |
| — / stop / TP + SL rules | +147 (+126) | -173 (+428) | -36 (-34) | +42 (-120) | -61 (+520) | 1171 |  |
| filter / stop / current exits | +74 (+12) | -217 (+364) | +67 (+39) | +128 (-48) | -76 (+415) | 988 | ✓ |
| — / stop / TP rule | +128 (+103) | -220 (+379) | +4 (+7) | +96 (-68) | -88 (+490) | 1163 | ✓ |
| — / stop / SL rule | +94 (+64) | -154 (+438) | -36 (-42) | +85 (-83) | -96 (+460) | 1121 |  |
| — / stop / current exits | +75 (+41) | -245 (+345) | -10 (-15) | +126 (-43) | -180 (+372) | 1112 |  |
| filter / — / TP rule | +79 (+63) | -440 (+234) | -31 (+18) | +133 (-30) | -393 (+314) | 1424 | ✓ |
| filter / — / TP + SL rules | +128 (+113) | -445 (+232) | -94 (-39) | +75 (-87) | -411 (+306) | 1445 |  |
| filter / — / SL rule | +63 (+40) | -497 (+171) | -62 (-16) | +121 (-44) | -496 (+195) | 1391 |  |
| filter / — / current exits | +23 (-1) | -523 (+141) | -10 (+29) | +158 (-9) | -510 (+169) | 1368 |  |
| — / — / TP + SL rules | +94 (+126) | -628 (+121) | -107 (+8) | +74 (-79) | -641 (+256) | 1805 | ✓ |
| — / — / TP rule | +55 (+84) | -653 (+91) | -69 (+40) | +135 (-20) | -667 (+215) | 1775 | ✓ |
| — / — / SL rule | +15 (+37) | -673 (+65) | -108 (-6) | +122 (-37) | -766 (+96) | 1736 |  |
| — / — / current exits | -20 (+0) | -732 (+0) | -94 (+0) | +160 (+0) | -847 (+0) | 1705 | ↑ |

**Full stats** (after costs): trades / net / win %% / profit factor / max drawdown

| Period | Current exits | All four (filter + stop + TP + SL) | Best row (filter / stop / TP + SL rules) |
|---|---|---|---|
| Third 1 | 520 / -20 / 51 % / 0.99 / 222 | 375 / +140 / 53 % / 1.13 / 102 | 375 / +140 / 53 % / 1.13 / 102 |
| Third 2 | 570 / -732 / 42 % / 0.63 / 808 | 280 / -131 / 44 % / 0.81 / 219 | 280 / -131 / 44 % / 0.81 / 219 |
| Third 3 | 615 / -94 / 51 % / 0.94 / 344 | 387 / -9 / 51 % / 0.99 / 117 | 387 / -9 / 51 % / 0.99 / 117 |
| Last 4 wk | 150 / +160 / 58 % / 1.37 / 80 | 130 / +46 / 52 % / 1.12 / 97 | 130 / +46 / 52 % / 1.12 / 97 |
| Whole | 1705 / -847 / 48 % / 0.84 / 1088 | 1042 / -0 / 50 % / 1.00 / 249 | 1042 / -0 / 50 % / 1.00 / 249 |

## MGC 3m

Filter / session stop / exits. ✓ = beyond random positive in all three thirds; ↑ = last 4 weeks not worse than current exits.

| Filter / stop / exits | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|
| filter / stop / TP + SL rules | +99 (+157) | +80 (+89) | +96 (+130) | +82 (+41) | +275 (+375) | 1333 | ✓↑ |
| filter / stop / SL rule | +83 (+141) | +59 (+68) | +102 (+135) | +81 (+40) | +244 (+344) | 1321 | ✓↑ |
| filter / stop / current exits | +46 (+103) | +81 (+89) | +75 (+108) | +68 (+27) | +202 (+300) | 1298 | ✓↑ |
| filter / stop / TP rule | +67 (+125) | +45 (+54) | +57 (+91) | +65 (+25) | +170 (+270) | 1326 | ✓↑ |
| — / stop / TP + SL rules | +68 (+130) | +60 (+72) | +33 (+70) | +68 (+28) | +161 (+273) | 1475 | ✓↑ |
| — / stop / SL rule | +54 (+116) | +51 (+64) | +38 (+74) | +71 (+32) | +143 (+254) | 1462 | ✓↑ |
| filter / — / TP + SL rules | +39 (+103) | +28 (+42) | +41 (+80) | +59 (+20) | +109 (+226) | 1547 | ✓↑ |
| — / stop / current exits | +22 (+84) | +80 (+92) | -5 (+31) | +55 (+15) | +97 (+206) | 1440 | ✓↑ |
| filter / — / SL rule | +8 (+72) | +13 (+27) | +60 (+98) | +59 (+19) | +81 (+197) | 1535 | ✓↑ |
| — / stop / TP rule | +35 (+97) | +42 (+55) | -7 (+30) | +54 (+15) | +71 (+182) | 1470 | ✓↑ |
| filter / — / current exits | -9 (+54) | +21 (+34) | +26 (+63) | +58 (+18) | +38 (+151) | 1489 | ✓↑ |
| filter / — / TP rule | +23 (+86) | +4 (+18) | -8 (+30) | +45 (+6) | +18 (+134) | 1526 | ✓↑ |
| — / — / TP + SL rules | -6 (+64) | -19 (+1) | -8 (+36) | +43 (+6) | -33 (+101) | 1771 | ✓↑ |
| — / — / SL rule | -32 (+37) | -28 (-8) | +9 (+52) | +47 (+9) | -51 (+82) | 1758 | ↑ |
| — / — / current exits | -69 (+0) | -18 (+0) | -42 (+0) | +38 (+0) | -129 (+0) | 1707 | ↑ |
| — / — / TP rule | -41 (+28) | -29 (-10) | -61 (-17) | +27 (-11) | -131 (+1) | 1747 |  |

**Full stats** (after costs): trades / net / win %% / profit factor / max drawdown

| Period | Current exits | All four (filter + stop + TP + SL) | Best row (filter / stop / TP + SL rules) |
|---|---|---|---|
| Third 1 | 597 / -69 / 51 % / 0.96 / 170 | 453 / +99 / 52 % / 1.09 / 69 | 453 / +99 / 52 % / 1.09 / 69 |
| Third 2 | 565 / -18 / 49 % / 0.99 / 111 | 447 / +80 / 50 % / 1.09 / 59 | 447 / +80 / 50 % / 1.09 / 59 |
| Third 3 | 545 / -42 / 48 % / 0.97 / 143 | 433 / +96 / 49 % / 1.11 / 92 | 433 / +96 / 49 % / 1.11 / 92 |
| Last 4 wk | 152 / +38 / 49 % / 1.11 / 59 | 120 / +82 / 54 % / 1.39 / 29 | 120 / +82 / 54 % / 1.39 / 29 |
| Whole | 1707 / -129 / 49 % / 0.97 / 285 | 1333 / +275 / 50 % / 1.10 / 145 | 1333 / +275 / 50 % / 1.10 / 145 |
