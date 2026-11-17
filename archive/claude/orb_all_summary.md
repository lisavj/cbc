# Opening-range blocks -- 2026-11-15 12:47 ET

STUDY SETTINGS STALE: settings_sync_report (11/13) lists 3 non-"known" MISMATCHes -- mes3_ema_grid LIVE part 'tod' (live = 100 %), chop_sim EXIT MES 3m part 'tod' (live = 100 %), chop_sim EXIT MGC 3m 50 % / trail 3.5 (live = FLIP 0 %). This study is NOT affected: orb_all_study.liveq() sets its own exits and matches CBC v10.96 (MES 3m 100 % at TP1, SL1 3, TP1 1.75; MGC 3m 0 % at TP1, no trail = FLIP 0 %), so liveq() was left unchanged.

Data: bars Jan 5 (3m/5m) / Jun 1 (2m) -> Fri 11/13 16:57 ET. Run 1 uses the same bars as run 0 (no trading since), so the numbers repeat the 11/13 baseline exactly.

Question: "No new setups during opening range (forming)" -- NY 9:30-10:00, London 3:00-3:30, Asia 20:00-20:30 ET -- keep, per chart and session?

## Rows that are promising / robust / "block robustly right"

| Chart | Exits | Block OFF | Δ | z | Δ by third | Δ last 4 wk | Window setups (n / net) | Verdict |
|---|---|---|---|---|---|---|---|---|
| MGC 3m | bracket | NY | +90 | +1.3 | +39 / +20 / +31 | +18 | 47 / +88 | promising |
| MGC 3m | bracket | Asia | +79 | +1.0 | +16 / +27 / +36 | +21 | 60 / +52 | promising |
| M2K 3m | bracket | NY | -88 | -2.2 | -57 / -14 / -17 | +3 | 79 / -79 | block robustly right |

No "robust" row anywhere. Other clearly-right blocks (strong negative Δ, not all thirds): MES 3m NY -140 z -2.4 (both exits; thirds -148 / -19 / +27), MNQ 3m Asia -365 live / -700 bracket (z -1.5 / -1.9).

## Watch items (runs qualifying = robust with BOTH exits, window n >= 30 and net > 0, last 4 wk Δ >= 0)

| Item | Live Δ / z / thirds | Bracket Δ / z / thirds | Runs qualifying |
|---|---|---|---|
| MGC 3m NY | +82 / +0.8 / -19 +74 +28 (noise) | +90 / +1.3 / +39 +20 +31 (promising) | 0 of 2 |
| MGC 3m Asia | +72 / +0.6 / +53 +54 -35 (noise) | +79 / +1.0 / +16 +27 +36 (promising) | 0 of 2 |

## Verdict

Keep all opening-range blocks on every chart (MES / MGC / MNQ / M2K 3m, MES / MGC 2m, MES / MGC 5m). No block meets the rule (robust with both exit sets on 2 consecutive runs). No change to ① Auto Trade Setup -> "No new setups during opening range (forming)".

## History

| Run | Date | Data through | Robust rows | MGC 3m NY (live / bracket Δ, z) | MGC 3m Asia (live / bracket Δ, z) | Verdict |
|---|---|---|---|---|---|---|
| 0 | 2026-11-13 | 11/13 | 0 | +82 z0.8 / +90 z1.3 | +72 z0.6 / +79 z1.0 | keep all |
| 1 | 2026-11-15 12:47 ET | 11/13 16:57 (same bars) | 0 | +82 z0.8 / +90 z1.3 | +72 z0.6 / +79 z1.0 | keep all |
