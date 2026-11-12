## Week of 11/09/2026 summary

- STUDY SETTINGS STALE: the 11/08 settings sync report lists 1 non-known MISMATCH (chop_sim GATE MGC 2m range gate R5=0) + late_study MES 3m tp=2.0 -- both already fixed in the project scripts used for this run, and neither affects these 3m studies.
- MES watch 'TP 85 % after 18 min + half SL1 if negative at 18 min': **+275 TR, z 0.9** (thirds +132 / +128 / +15, last 4 wk -78) -- identical to 11/07 (+275, z 0.9). Still below z 1 and the last 4 weeks are negative -> not a candidate.
- MGC watch 'TP 65 % after 21 min + cut if < 25 % at 18 min': **+145 T4R, z 0.6** (thirds +76 / +18 / +51, last 4 wk +10.9) -- same as 11/07 (+145). z < 1 -> not a candidate.
- 18 min still stands out: MES best TP-alone = 85 % after 18 min (+215 TR), best SL-alone = cut < 50 % at 18 min (+177, third 3 -118), grid best row Xtp 18; every top MGC combination uses the 18-min SL check.
- Combos positive: MES 870 / 1000 (14 better in all thirds), MGC 701 / 1000 (160 in all thirds, 36 T4R). Verdict: no change on either chart.

---

# Combined TP-reduction + time-stop study — MES 3m and MGC 3m — 11/09/2026 13:58

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

## MES 3m — current exits: 1705 setups to 11/09, net +6

**Best TP rule alone:** TP 85% after 18 min + SL off: **+215** TR (z +0.7, thirds +84 / +91 / +40, last 4 wk -20.3, win 52 %)

**Best SL rule alone:** TP off + cut if < 50 % at 18 min: **+177** (z +0.6, thirds +83 / +211 / -118, last 4 wk -150.8, win 47 %)

Combinations: 1000, positive 870, better in all thirds 14, T + neighbours (R) 14, T + 4 + R 0.

**Top 10 combinations by Δ**

1. TP 85% after 18 min + half SL1 if negative at 18 min: **+275** TR (z +0.9, thirds +132 / +128 / +15, last 4 wk -77.7, win 49 %)
2. TP 85% after 12 min + half SL1 if negative at 18 min: **+269** TR (z +0.9, thirds +102 / +136 / +31, last 4 wk -69.3, win 50 %)
3. TP 85% after 21 min + half SL1 if negative at 18 min: **+267** TR (z +0.9, thirds +123 / +129 / +15, last 4 wk -66.0, win 49 %)
4. TP 75% after 21 min + half SL1 if negative at 18 min: **+261** TR (z +0.9, thirds +103 / +156 / +2, last 4 wk -92.3, win 50 %)
5. TP 75% after 18 min + half SL1 if negative at 18 min: **+245** TR (z +0.8, thirds +85 / +157 / +2, last 4 wk -106.6, win 50 %)
6. TP 75% after 21 min + cut if < 25 % at 18 min: **+244** (z +0.8, thirds +74 / +262 / -92, last 4 wk -114.5, win 46 %)
7. TP 75% after 21 min + cut if negative at 18 min: **+238** (z +0.8, thirds +51 / +244 / -58, last 4 wk -100.1, win 44 %)
8. TP 85% after 15 min + half SL1 if negative at 18 min: **+238** TR (z +0.8, thirds +94 / +112 / +32, last 4 wk -60.2, win 49 %)
9. TP 85% after 12 min + cut if < 50 % at 12 min: **+237** (z +0.8, thirds -2 / +284 / -45, last 4 wk -159.4, win 49 %)
10. TP 85% after 18 min + half SL1 if < 50 % at 18 min: **+236** (z +0.8, thirds +174 / +118 / -56, last 4 wk -134.8, win 48 %)

**Steadiest combinations (all thirds better AND every neighbour better), top 10 by Δ**

1. TP 85% after 18 min + half SL1 if negative at 18 min: **+275** TR (z +0.9, thirds +132 / +128 / +15, last 4 wk -77.7, win 49 %)
2. TP 85% after 12 min + half SL1 if negative at 18 min: **+269** TR (z +0.9, thirds +102 / +136 / +31, last 4 wk -69.3, win 50 %)
3. TP 85% after 21 min + half SL1 if negative at 18 min: **+267** TR (z +0.9, thirds +123 / +129 / +15, last 4 wk -66.0, win 49 %)
4. TP 75% after 21 min + half SL1 if negative at 18 min: **+261** TR (z +0.9, thirds +103 / +156 / +2, last 4 wk -92.3, win 50 %)
5. TP 75% after 18 min + half SL1 if negative at 18 min: **+245** TR (z +0.8, thirds +85 / +157 / +2, last 4 wk -106.6, win 50 %)
6. TP 85% after 15 min + half SL1 if negative at 18 min: **+238** TR (z +0.8, thirds +94 / +112 / +32, last 4 wk -60.2, win 49 %)
7. TP 65% after 30 min + half SL1 if negative at 18 min: **+225** TR (z +0.8, thirds +88 / +123 / +15, last 4 wk -80.0, win 50 %)
8. TP 85% after 12 min + half SL1 if negative at 21 min: **+216** TR (z +0.7, thirds +91 / +117 / +7, last 4 wk -62.5, win 50 %)
9. TP 85% after 27 min + half SL1 if negative at 18 min: **+199** TR (z +0.7, thirds +102 / +96 / +2, last 4 wk -61.7, win 48 %)
10. TP 75% after 15 min + half SL1 if negative at 18 min: **+197** TR (z +0.7, thirds +21 / +152 / +23, last 4 wk -94.9, win 51 %)

**Does adding the SL rule help the TP rule?** (top 5 TP rules; best SL partner; combo vs TP alone)

| TP rule | TP alone | + best SL rule | Combo | SL adds | SL alone |
|---|---|---|---|---|---|
| TP 85% after 18 min | +215 | half SL1 if negative at 18 min | +275 | +60 | +115 |
| TP 85% after 12 min | +210 | half SL1 if negative at 18 min | +269 | +60 | +115 |
| TP 85% after 21 min | +206 | half SL1 if negative at 18 min | +267 | +61 | +115 |
| TP 75% after 21 min | +192 | half SL1 if negative at 18 min | +261 | +69 | +115 |
| TP 85% after 15 min | +178 | half SL1 if negative at 18 min | +238 | +60 | +115 |

**Grid: best combo Δ per TP cell (any SL rule) / TP alone**

| Xtp \\ Ytp | 65% | 70% | 75% | 85% |
|---|---|---|---|---|
| 12 | +196 / +61 | +194 / +73 | +193 / +119 | +269 / +210 |
| 15 | +223 / +90 | +214 / +94 | +203 / +119 | +238 / +178 |
| 18 | +226 / +114 | +215 / +115 | +245 / +176 | +275 / +215 |
| 21 | +201 / +108 | +217 / +134 | +261 / +192 | +267 / +206 |
| 24 | +206 / +100 | +231 / +133 | +225 / +154 | +224 / +159 |
| 27 | +188 / +50 | +192 / +86 | +211 / +125 | +199 / +125 |
| 30 | +225 / +137 | +223 / +142 | +216 / +135 | +198 / +126 |
| 33 | +185 / +45 | +187 / +47 | +195 / +70 | +186 / +44 |
| 36 | +180 / +45 | +187 / +50 | +193 / +60 | +192 / +36 |
| 42 | +191 / +1 | +195 / +9 | +201 / -0 | +189 / +7 |

## MGC 3m — current exits: 1707 setups to 11/09, net +247

**Best TP rule alone:** TP 65% after 21 min + SL off: **+7** (z +0.0, thirds +29 / -8 / -15, last 4 wk -10.0, win 52 %)

**Best SL rule alone:** TP off + cut if < 25 % at 18 min: **+124** T4 (z +0.5, thirds +49 / +8 / +67, last 4 wk +13.7, win 49 %)

Combinations: 1000, positive 701, better in all thirds 160, T + neighbours (R) 88, T + 4 + R 36.

**Top 10 combinations by Δ**

1. TP 65% after 30 min + cut if < 25 % at 18 min: **+146** T4 (z +0.6, thirds +72 / +27 / +48, last 4 wk +1.8, win 50 %)
2. TP 65% after 21 min + cut if < 25 % at 18 min: **+145** T4R (z +0.6, thirds +76 / +18 / +51, last 4 wk +10.9, win 50 %)
3. TP 65% after 27 min + cut if < 25 % at 18 min: **+144** T4 (z +0.6, thirds +70 / +22 / +53, last 4 wk +8.5, win 50 %)
4. TP 65% after 24 min + cut if < 25 % at 18 min: **+144** T4R (z +0.6, thirds +69 / +14 / +61, last 4 wk +17.2, win 50 %)
5. TP 70% after 21 min + cut if < 25 % at 18 min: **+129** T4R (z +0.6, thirds +58 / +21 / +49, last 4 wk +12.8, win 50 %)
6. TP 70% after 18 min + cut if < 25 % at 18 min: **+128** T4R (z +0.6, thirds +44 / +29 / +54, last 4 wk +8.0, win 50 %)
7. TP 75% after 21 min + cut if < 50 % at 18 min: **+124** T4R (z +0.5, thirds +70 / +10 / +44, last 4 wk +7.6, win 51 %)
8. TP 65% after 24 min + cut if < 50 % at 18 min: **+123** T4R (z +0.5, thirds +69 / +7 / +47, last 4 wk +7.0, win 51 %)
9. TP 75% after 21 min + cut if < 25 % at 18 min: **+123** T4 (z +0.5, thirds +61 / +11 / +51, last 4 wk +15.0, win 50 %)
10. TP 65% after 21 min + cut if < 50 % at 18 min: **+121** T4R (z +0.5, thirds +69 / +6 / +46, last 4 wk +5.5, win 51 %)

**Steadiest combinations (all thirds better AND every neighbour better), top 10 by Δ**

1. TP 65% after 21 min + cut if < 25 % at 18 min: **+145** T4R (z +0.6, thirds +76 / +18 / +51, last 4 wk +10.9, win 50 %)
2. TP 65% after 24 min + cut if < 25 % at 18 min: **+144** T4R (z +0.6, thirds +69 / +14 / +61, last 4 wk +17.2, win 50 %)
3. TP 70% after 21 min + cut if < 25 % at 18 min: **+129** T4R (z +0.6, thirds +58 / +21 / +49, last 4 wk +12.8, win 50 %)
4. TP 70% after 18 min + cut if < 25 % at 18 min: **+128** T4R (z +0.6, thirds +44 / +29 / +54, last 4 wk +8.0, win 50 %)
5. TP 75% after 21 min + cut if < 50 % at 18 min: **+124** T4R (z +0.5, thirds +70 / +10 / +44, last 4 wk +7.6, win 51 %)
6. TP 65% after 24 min + cut if < 50 % at 18 min: **+123** T4R (z +0.5, thirds +69 / +7 / +47, last 4 wk +7.0, win 51 %)
7. TP 65% after 21 min + cut if < 50 % at 18 min: **+121** T4R (z +0.5, thirds +69 / +6 / +46, last 4 wk +5.5, win 51 %)
8. TP 85% after 21 min + cut if < 50 % at 18 min: **+120** T4R (z +0.5, thirds +71 / +15 / +33, last 4 wk +2.1, win 50 %)
9. TP 70% after 24 min + cut if < 50 % at 18 min: **+119** T4R (z +0.5, thirds +70 / +1 / +48, last 4 wk +7.6, win 51 %)
10. TP 70% after 21 min + cut if < 50 % at 18 min: **+118** T4R (z +0.5, thirds +70 / +8 / +41, last 4 wk +6.4, win 51 %)

**Does adding the SL rule help the TP rule?** (top 5 TP rules; best SL partner; combo vs TP alone)

| TP rule | TP alone | + best SL rule | Combo | SL adds | SL alone |
|---|---|---|---|---|---|
| TP 65% after 21 min | +7 | cut if < 25 % at 18 min | +145 | +138 | +124 |
| TP 70% after 18 min | +3 | cut if < 25 % at 18 min | +128 | +125 | +124 |
| TP 85% after 12 min | +1 | cut if < 50 % at 18 min | +88 | +87 | +109 |
| TP 85% after 18 min | -0 | cut if < 50 % at 18 min | +108 | +108 | +109 |
| TP 70% after 21 min | -0 | cut if < 25 % at 18 min | +129 | +129 | +124 |

**Grid: best combo Δ per TP cell (any SL rule) / TP alone**

| Xtp \\ Ytp | 65% | 70% | 75% | 85% |
|---|---|---|---|---|
| 12 | +58 / -56 | +75 / -29 | +61 / -30 | +88 / +1 |
| 15 | +83 / -34 | +98 / -10 | +92 / -3 | +88 / -12 |
| 18 | +115 / -6 | +128 / +3 | +113 / -4 | +108 / -0 |
| 21 | +145 / +7 | +129 / -0 | +124 / -1 | +120 / -7 |
| 24 | +144 / -9 | +120 / -24 | +116 / -21 | +108 / -29 |
| 27 | +144 / -6 | +110 / -24 | +118 / -3 | +112 / -25 |
| 30 | +146 / -22 | +110 / -41 | +117 / -16 | +113 / -24 |
| 33 | +119 / -53 | +92 / -55 | +91 / -44 | +101 / -34 |
| 36 | +120 / -40 | +96 / -42 | +95 / -32 | +102 / -29 |
| 42 | +121 / -36 | +107 / -29 | +109 / -18 | +113 / -16 |

