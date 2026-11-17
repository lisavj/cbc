## Week of 11/14/2026 summary

- STUDY SETTINGS STALE: the 11/13 settings sync (v10.96) lists 3 non-known MISMATCHes, NOT yet fixed in the project scripts, and they touch the 3m studies -- mes3_ema_grid LIVE still closes MES 3m 80/100 % by time of day (live since v10.95: 100 % at TP1 all day), and MGC 3m live is now FLIP 0 % (v10.96: nothing closed at TP1, BE, no trail, exit on HTF flip) while these replays use 80 % / trail 1.7 (MGCX) or 50 % / 3.5. Bot replay (H) is unaffected (part 1.0). Also new: the 11/14 X4 fix in mes3_ema_grid.py makes the MGC 3m VWAP-stretch gate actually block setups (MGC 3m 1193 setups vs 1707 last week), so MGC 3m numbers are not like-for-like with 11/09.
- MES 3m watch "TP 85 % after 18 min + half SL1 if negative at 18 min": **+226** (z 0.8; thirds +132 / +136 / -42; last 4 wk -104) vs +275 (z 0.9) on 11/07-11/09 -> WEAKER, third 3 now negative. Still the #1 combination by Δ, but no MES combination is better in all thirds (0 of 1000).
- MES 3m TP rule alone (85 % after 18 min) +196 TR (thirds +84 / +87 / +25, last 4 wk -46) -- the steadier half of the pair; the SL half adds +30 but costs third 3.
- MGC 3m watch "TP 65 % after 21 min + cut if < 25 % at 18 min": **+86** (z 0.45; thirds +72 / -10 / +23; last 4 wk +8) vs +145 T4R -> WEAKER (lost T). New top: "TP 70 % after 18 min + cut if negative at 18 min" +105 T4R (z 0.5); 169 combinations better in all thirds, 29 T+4+R, none with z >= 1.
- 18 min still stands out alone: best SL-alone check is 18 min on MGC (+102 vs <= +43 at other times) and the best TP-alone cell on MES is 18 min (+196); MES SL-alone best is 15 min (+117) with 18 min close (+107).
- Verdict: no change (nothing robust/promising; 0 weeks toward 3).

---

# Combined TP-reduction + time-stop study — MES 3m and MGC 3m — 11/14/2026 23:37

Combined time-based TP reduction + time-based stop / cut, MES 3m and MGC 3m -- 11/07/2026.
Both rules active together on the same trade (before TP1 only):
  TP rule (11/06 study, mode A "modified TP"): from the candle after Xtp minutes, TP1 becomes a limit at Ytp % of the TP1
          distance (fills when the high / low reaches it; at the open if the candle opens past it). Closes 100 %.
  SL rule (11/07 study): one check at the close of the candle Xsl minutes after entry; if the trade is negative / below
          Ysl % of TP1: CUT = close at that close; HALF = SL1 to half its distance (close now if already past it).
Grid: TP Xtp 12-42 (12,15,18,21,24,27,30,33,36,42) x Ytp 65/70/75/85 % + "TP rule off";
      SL CUT x (negative, < 25 %, < 50 %) and HALF x (negative, < 50 %), Xsl 12-24 by 3 + "SL rule off".
Replay = sltime_study / tptime_study engine on live settings (MES 3m TP1 1.75 ATR v10.82, MGC 3m MGCX). Jan 5 -> now.
Cell = Δ net pts vs current exits. T = better in all three thirds, 4 = better in the last 4 weeks, R = T and all neighbours
(Xtp ±1 grid step, Xsl ±3 min) better overall. z = Δ / (SD x sqrt(setups changed)). Also shown: what each rule gives alone,
and whether the combination adds up (combo vs TP-alone + SL-alone).

## MES 3m — current exits: 1738 setups to 11/13, net +47

**Best TP rule alone:** TP 85% after 18 min + SL off: **+196** TR (z +0.7, thirds +84 / +87 / +25, last 4 wk -45.9, win 52 %)

**Best SL rule alone:** TP off + cut if < 50 % at 15 min: **+117** (z +0.4, thirds +73 / +229 / -186, last 4 wk -198.4, win 48 %)

Combinations: 1000, positive 688, better in all thirds 0, T + neighbours (R) 0, T + 4 + R 0.

**Top 10 combinations by Δ**

1. TP 85% after 18 min + half SL1 if negative at 18 min: **+226** (z +0.8, thirds +132 / +136 / -42, last 4 wk -103.6, win 49 %)
2. TP 85% after 12 min + half SL1 if negative at 18 min: **+220** (z +0.7, thirds +102 / +142 / -25, last 4 wk -93.2, win 50 %)
3. TP 85% after 21 min + half SL1 if negative at 18 min: **+217** (z +0.7, thirds +123 / +137 / -43, last 4 wk -92.4, win 49 %)
4. TP 75% after 21 min + half SL1 if negative at 18 min: **+203** (z +0.7, thirds +103 / +162 / -63, last 4 wk -124.2, win 50 %)
5. TP 85% after 12 min + cut if < 50 % at 12 min: **+189** (z +0.6, thirds -2 / +297 / -106, last 4 wk -173.4, win 49 %)
6. TP 85% after 15 min + half SL1 if negative at 18 min: **+188** (z +0.6, thirds +94 / +118 / -24, last 4 wk -88.2, win 49 %)
7. TP 85% after 18 min + half SL1 if < 50 % at 18 min: **+187** (z +0.6, thirds +174 / +126 / -114, last 4 wk -160.7, win 48 %)
8. TP 85% after 12 min + half SL1 if < 50 % at 18 min: **+186** (z +0.6, thirds +145 / +129 / -87, last 4 wk -150.4, win 49 %)
9. TP 75% after 18 min + half SL1 if negative at 18 min: **+186** (z +0.6, thirds +85 / +166 / -65, last 4 wk -137.8, win 50 %)
10. TP 85% after 21 min + half SL1 if < 50 % at 18 min: **+182** (z +0.6, thirds +169 / +128 / -115, last 4 wk -149.5, win 48 %)

**Steadiest combinations (all thirds better AND every neighbour better), top 10 by Δ**

- none

**Does adding the SL rule help the TP rule?** (top 5 TP rules; best SL partner; combo vs TP alone)

| TP rule | TP alone | + best SL rule | Combo | SL adds | SL alone |
|---|---|---|---|---|---|
| TP 85% after 18 min | +196 | half SL1 if negative at 18 min | +226 | +30 | +66 |
| TP 85% after 12 min | +191 | half SL1 if negative at 18 min | +220 | +29 | +66 |
| TP 85% after 21 min | +187 | half SL1 if negative at 18 min | +217 | +30 | +66 |
| TP 75% after 21 min | +162 | half SL1 if negative at 18 min | +203 | +40 | +66 |
| TP 85% after 15 min | +159 | half SL1 if negative at 18 min | +188 | +30 | +66 |

**Grid: best combo Δ per TP cell (any SL rule) / TP alone**

| Xtp \ Ytp | 65% | 70% | 75% | 85% |
|---|---|---|---|---|
| 12 | +120 / +20 | +128 / +38 | +137 / +89 | +220 / +191 |
| 15 | +150 / +50 | +146 / +59 | +138 / +90 | +188 / +159 |
| 18 | +153 / +74 | +143 / +80 | +186 / +146 | +226 / +196 |
| 21 | +127 / +68 | +146 / +99 | +203 / +162 | +217 / +187 |
| 24 | +132 / +62 | +160 / +100 | +168 / +126 | +175 / +140 |
| 27 | +138 / +15 | +143 / +55 | +156 / +99 | +152 / +108 |
| 30 | +165 / +104 | +166 / +112 | +162 / +109 | +149 / +108 |
| 33 | +135 / +36 | +131 / +40 | +139 / +65 | +131 / +44 |
| 36 | +125 / +38 | +132 / +44 | +138 / +57 | +137 / +37 |
| 42 | +124 / -2 | +128 / +6 | +132 / -1 | +133 / +9 |

## MGC 3m — current exits: 1193 setups to 11/13, net +317

**Best TP rule alone:** TP 70% after 18 min + SL off: **+71** T4R (z +0.4, thirds +28 / +11 / +32, last 4 wk +0.5, win 53 %)

**Best SL rule alone:** TP off + cut if negative at 18 min: **+102** T4R (z +0.5, thirds +44 / +17 / +42, last 4 wk +24.6, win 47 %)

Combinations: 1000, positive 819, better in all thirds 169, T + neighbours (R) 153, T + 4 + R 29.

**Top 10 combinations by Δ**

1. TP 70% after 18 min + cut if negative at 18 min: **+105** T4R (z +0.5, thirds +52 / +8 / +45, last 4 wk +14.0, win 49 %)
2. TP 75% after 27 min + cut if negative at 18 min: **+101** 4 (z +0.5, thirds +66 / -0 / +35, last 4 wk +10.2, win 48 %)
3. TP 70% after 18 min + cut if < 25 % at 18 min: **+99** T4R (z +0.5, thirds +67 / +2 / +30, last 4 wk +7.8, win 51 %)
4. TP 70% after 18 min + half SL1 if negative at 18 min: **+97** 4 (z +0.5, thirds +49 / -7 / +56, last 4 wk +12.7, win 51 %)
5. TP 65% after 24 min + cut if negative at 18 min: **+96** T4R (z +0.5, thirds +54 / +6 / +36, last 4 wk +13.2, win 48 %)
6. TP 75% after 24 min + cut if negative at 18 min: **+95** T4R (z +0.5, thirds +62 / +0 / +33, last 4 wk +18.2, win 48 %)
7. TP 75% after 30 min + cut if negative at 18 min: **+93** T4R (z +0.5, thirds +66 / +3 / +23, last 4 wk +3.6, win 48 %)
8. TP 65% after 27 min + cut if negative at 18 min: **+92** T4R (z +0.5, thirds +60 / +3 / +29, last 4 wk +6.2, win 48 %)
9. TP 65% after 21 min + cut if negative at 18 min: **+92** T4R (z +0.5, thirds +57 / +1 / +35, last 4 wk +12.8, win 49 %)
10. TP 70% after 24 min + cut if negative at 18 min: **+91** 4 (z +0.5, thirds +58 / -5 / +38, last 4 wk +15.5, win 48 %)

**Steadiest combinations (all thirds better AND every neighbour better), top 10 by Δ**

1. TP 70% after 18 min + cut if negative at 18 min: **+105** T4R (z +0.5, thirds +52 / +8 / +45, last 4 wk +14.0, win 49 %)
2. TP 70% after 18 min + cut if < 25 % at 18 min: **+99** T4R (z +0.5, thirds +67 / +2 / +30, last 4 wk +7.8, win 51 %)
3. TP 65% after 24 min + cut if negative at 18 min: **+96** T4R (z +0.5, thirds +54 / +6 / +36, last 4 wk +13.2, win 48 %)
4. TP 75% after 24 min + cut if negative at 18 min: **+95** T4R (z +0.5, thirds +62 / +0 / +33, last 4 wk +18.2, win 48 %)
5. TP 75% after 30 min + cut if negative at 18 min: **+93** T4R (z +0.5, thirds +66 / +3 / +23, last 4 wk +3.6, win 48 %)
6. TP 65% after 27 min + cut if negative at 18 min: **+92** T4R (z +0.5, thirds +60 / +3 / +29, last 4 wk +6.2, win 48 %)
7. TP 65% after 21 min + cut if negative at 18 min: **+92** T4R (z +0.5, thirds +57 / +1 / +35, last 4 wk +12.8, win 49 %)
8. TP 85% after 18 min + cut if negative at 18 min: **+91** T4R (z +0.5, thirds +52 / +14 / +25, last 4 wk +10.9, win 48 %)
9. TP 70% after 18 min + cut if negative at 15 min: **+90** TR (z +0.5, thirds +29 / +35 / +25, last 4 wk -9.8, win 48 %)
10. TP 85% after 24 min + cut if negative at 18 min: **+89** T4R (z +0.5, thirds +59 / +2 / +27, last 4 wk +15.2, win 48 %)

**Does adding the SL rule help the TP rule?** (top 5 TP rules; best SL partner; combo vs TP alone)

| TP rule | TP alone | + best SL rule | Combo | SL adds | SL alone |
|---|---|---|---|---|---|
| TP 70% after 18 min | +71 | cut if negative at 18 min | +105 | +33 | +102 |
| TP 65% after 21 min | +59 | cut if negative at 18 min | +92 | +34 | +102 |
| TP 70% after 21 min | +57 | cut if negative at 18 min | +84 | +27 | +102 |
| TP 75% after 27 min | +54 | cut if negative at 18 min | +101 | +47 | +102 |
| TP 65% after 18 min | +53 | cut if negative at 18 min | +87 | +34 | +102 |

**Grid: best combo Δ per TP cell (any SL rule) / TP alone**

| Xtp \ Ytp | 65% | 70% | 75% | 85% |
|---|---|---|---|---|
| 12 | +43 / -13 | +54 / +20 | +39 / +8 | +63 / +8 |
| 15 | +37 / +2 | +57 / +29 | +51 / +24 | +66 / +6 |
| 18 | +87 / +53 | +105 / +71 | +88 / +47 | +91 / +31 |
| 21 | +92 / +59 | +84 / +57 | +88 / +53 | +85 / +29 |
| 24 | +96 / +45 | +91 / +44 | +95 / +46 | +89 / +17 |
| 27 | +92 / +38 | +89 / +42 | +101 / +54 | +87 / +12 |
| 30 | +88 / +4 | +82 / +11 | +93 / +29 | +87 / +8 |
| 33 | +73 / -19 | +69 / -12 | +68 / -5 | +74 / -5 |
| 36 | +72 / -12 | +70 / -4 | +71 / +3 | +74 / -1 |
| 42 | +77 / -14 | +74 / -5 | +76 / +4 | +79 / +2 |

