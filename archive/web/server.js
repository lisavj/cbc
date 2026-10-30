// TradingView Webhook Dashboard
// -----------------------------
// - POST /webhook?token=YOUR_SECRET   <- point your TradingView alert's webhook URL here
// - GET  /                            <- live dashboard (auto-updates as alerts arrive)
// - GET  /alerts                      <- raw JSON of stored alerts (v8: ?days=N or ?limit=N to fetch less; gzip)
//                                        v9: ?from=YYYY-MM-DD[&to=YYYY-MM-DD] (ET dates) also reads the archive
// - GET  /bars?sym=MES&days=5          <- BarFeed bars for the Chart tab (v9: &from=YYYY-MM-DD[&to=] reads the archive)
// - GET  /archive                      <- v9: list of archived alert days and bar months
//   v10: DUPLICATE ALERTS. (1) A webhook alert whose text is identical to one stored within the last DUP_WINDOW_SEC
//        seconds (env, default 60) is ignored (answered 200 "Duplicate ignored"; counted in /health).
//        (2) GET /dedupe?token=SECRET = dry run over RAM + the whole archive; POST /dedupe?token=SECRET&apply=1
//        removes identical copies within the window (first copy kept). &mode=near also removes near duplicates
//        (same first line, Chart, Time and alert names, different text; the longest copy is kept). &window=SEC.
//   v9: LONG-TERM ARCHIVE on the Render Disk (DATA_DIR/archive). Nothing is thrown away any more:
//       - Alerts: every completed ET day is written to archive/alerts/YYYY-MM-DD.ndjson.gz (hourly + at startup).
//         RAM keeps only the last MEM_ALERT_DAYS (env, default 30) days; older alerts are dropped from RAM
//         only after they are in the archive. Alerts pushed out by MAX_ALERTS are archived first as well.
//       - Bars: candles older than BAR_KEEP_DAYS (env, default 60) are moved to
//         archive/bars/<SYM>/YYYY-MM.ndjson.gz instead of being deleted. POST /bars/import now also accepts
//         candles older than BAR_KEEP_DAYS (they go straight to the archive), so old CSV history can be backfilled.
//       - GET /alerts and GET /bars without from/to behave exactly as before (RAM only), so the dashboard is
//         unchanged; ?from= (or ?days= larger than the RAM window) merges archive + RAM, deduplicated.
//       - gzip files are small (~10x smaller than JSON), so a 1 GB Disk holds years of alerts and 3m bars.
//   v8: keeps the last 100000 alerts (was 5000; env MAX_ALERTS overrides). At ~2,000 alerts/day 5000 held only
//       ~2.5 days. To stay fast at that size: alerts.json is written compact (no indentation) and at most once
//       every 10 s (debounced, flushed on shutdown) instead of a full pretty-printed rewrite on every alert;
//       GET /alerts accepts ?days=N / ?limit=N and is gzip-compressed when the client accepts it (~10x smaller).
//   v7: POST /bars/import?...&replace=1 replaces candles that already exist (same time) instead of skipping them --
//       to fix stored bars after a BarFeed setting change (e.g. 2m feed sent 15m HTF fields before BarFeed v1.03).
//   v6: keeps the last 5000 alerts (was 500; env MAX_ALERTS overrides).
//   v5: Render log names each alert ("MES1! | LTF EMA20 Pierce - Entry: LONG") and logs every BarFeed candle
//       ("bar MGC 3m 10:51 ET LIVE c=4161.7") so live 1-minute updates can be checked in the log.
//   v4: BarFeed v1.01 re-sends the forming candle every minute ("live":1) -> replaced in place, appended to the file.
//   v3: one store per symbol AND chart timeframe -- key "MES" = 3m (unchanged), "MES_2" = 2m, "MGC_5" = 5m ...
//
// Alerts are kept in memory (fast, instant dashboard updates) and mirrored to alerts.json
// on disk so they survive a restart/redeploy. Only the most recent MAX_ALERTS are kept in RAM.
//
// PERSISTENCE ACROSS DEPLOYS (Render): Render's default web service disk is ephemeral —
// every new deploy (e.g. a git push) spins up a brand-new container, wiping any files not
// in the git repo, alerts.json included. To keep alerts across deploys, attach a Render
// "Disk" (Render dashboard -> your service -> Disks -> Add Disk), mount it at e.g. /data,
// then set an environment variable DATA_DIR=/data on the service. If DATA_DIR isn't set,
// this falls back to the old behavior (alerts.json next to the code) — same as before, so
// nothing changes for anyone not using a Disk.
const express = require('express');
const fs = require('fs');
const path = require('path');
const zlib = require('zlib'); // v8: gzip for GET /alerts (built into Node, no new dependency)

const app = express();
const SERVER_STARTED_AT = new Date().toISOString(); // used by GET /health to show how recently this process (re)started
const PORT = process.env.PORT || 3000;
const SECRET = process.env.WEBHOOK_SECRET || ''; // set this in your host's env vars
const DISCORD_WEBHOOK_URL = process.env.DISCORD_WEBHOOK_URL || ''; // optional: paste a Discord channel webhook URL here to forward alerts
const MAX_ALERTS = Number(process.env.MAX_ALERTS) || 100000; // v8: was 5000 (v6), 500 before
const ALERT_SAVE_DELAY_MS = 10000; // v8: debounce -- at 100000 alerts one write takes ~1 s, so at most one every 10 s
const DATA_DIR = process.env.DATA_DIR || __dirname; // point this at a mounted Render Disk to survive deploys
const DATA_FILE = path.join(DATA_DIR, 'alerts.json');

// Make sure DATA_DIR exists (a freshly-mounted Disk is already there on Render, but this
// covers a custom path elsewhere, e.g. local testing with DATA_DIR set to a new folder).
try {
  fs.mkdirSync(DATA_DIR, { recursive: true });
} catch (e) {
  console.error('Could not create DATA_DIR', DATA_DIR, e.message);
}

// ============================================================================
// v9: long-term archive (see header). One gzip NDJSON file per ET day (alerts) or per
// symbol + ET month (bars). Files are rewritten atomically (temp file + rename) when merged.
// ============================================================================
const ARCHIVE_DIR = path.join(DATA_DIR, 'archive');
const ALERT_ARCH_DIR = path.join(ARCHIVE_DIR, 'alerts');
const BAR_ARCH_DIR = path.join(ARCHIVE_DIR, 'bars');
const MEM_ALERT_DAYS = Number(process.env.MEM_ALERT_DAYS || 30);
[ALERT_ARCH_DIR, BAR_ARCH_DIR].forEach((d) => {
  try { fs.mkdirSync(d, { recursive: true }); } catch (e) { console.error('Could not create', d, e.message); }
});
const DAY_RE = /^\d{4}-\d{2}-\d{2}$/;
const ET_FMT = new Intl.DateTimeFormat('en-CA', { timeZone: 'America/New_York', year: 'numeric', month: '2-digit', day: '2-digit' });
function etDay(x) { return ET_FMT.format(new Date(x)); } // "YYYY-MM-DD" in New York time

function readGzLines(file) {
  let buf;
  try { buf = fs.readFileSync(file); } catch (e) { if (e.code !== 'ENOENT') console.error('Could not read', file, e.message); return []; }
  let text;
  try { text = zlib.gunzipSync(buf).toString('utf8'); } catch (e) { console.error('Could not unzip', file, e.message); return []; }
  const out = [];
  text.split('\n').forEach((l) => { if (!l.trim()) return; try { out.push(JSON.parse(l)); } catch (e) { /* skip a bad line */ } });
  return out;
}
function writeGzLines(file, list) {
  const tmp = file + '.tmp';
  fs.writeFileSync(tmp, zlib.gzipSync(list.map((x) => JSON.stringify(x)).join('\n') + '\n'));
  fs.renameSync(tmp, file);
}
function alertDayFile(day) { return path.join(ALERT_ARCH_DIR, day + '.ndjson.gz'); }
function listAlertArchiveDays() {
  try {
    return fs.readdirSync(ALERT_ARCH_DIR).filter((f) => f.endsWith('.ndjson.gz')).map((f) => f.slice(0, 10)).filter((d) => DAY_RE.test(d)).sort();
  } catch (e) { return []; }
}

// Merge a list of alerts into their ET-day archive files (dedup by id). Returns how many were new.
function mergeAlertsIntoArchive(list, failed) {
  const byDay = {};
  list.forEach((a) => { if (a && a.id && a.receivedAt) (byDay[etDay(a.receivedAt)] || (byDay[etDay(a.receivedAt)] = [])).push(a); });
  let added = 0;
  Object.keys(byDay).forEach((day) => {
    try {
      const file = alertDayFile(day);
      const old = readGzLines(file);
      const seen = new Set(old.map((a) => a.id));
      const add = byDay[day].filter((a) => !seen.has(a.id));
      if (!add.length) return;
      const all = old.concat(add).sort((x, y) => (x.receivedAt < y.receivedAt ? 1 : x.receivedAt > y.receivedAt ? -1 : 0)); // newest first, like /alerts
      writeGzLines(file, all);
      added += add.length;
    } catch (e) {
      console.error('Could not archive alerts for', day, e.message);
      if (failed) failed.add(day);
    }
  });
  return added;
}

// Read archived + in-RAM alerts whose ET day is in [from, to]; newest first, dedup by id.
function readAlertRange(from, to) {
  const seen = new Set();
  const out = [];
  alerts.forEach((a) => { const d = etDay(a.receivedAt); if (d >= from && d <= to && !seen.has(a.id)) { seen.add(a.id); out.push(a); } });
  listAlertArchiveDays().filter((d) => d >= from && d <= to).forEach((d) => {
    readGzLines(alertDayFile(d)).forEach((a) => { if (!seen.has(a.id)) { seen.add(a.id); out.push(a); } });
  });
  out.sort((x, y) => (x.receivedAt < y.receivedAt ? 1 : x.receivedAt > y.receivedAt ? -1 : 0));
  return out;
}

function barArchDir(sym) { return path.join(BAR_ARCH_DIR, sym); }
function listBarArchiveMonths(sym) {
  try {
    return fs.readdirSync(barArchDir(sym)).filter((f) => /^\d{4}-\d{2}\.ndjson\.gz$/.test(f)).map((f) => f.slice(0, 7)).sort();
  } catch (e) { return []; }
}
// Merge candles into archive/bars/<SYM>/YYYY-MM.ndjson.gz (dedup by t; replace=true overwrites). Returns new count.
function mergeBarsIntoArchive(sym, list, replace) {
  const byMonth = {};
  list.forEach((b) => { const m = etDay(b.t).slice(0, 7); (byMonth[m] || (byMonth[m] = [])).push(b); });
  let added = 0;
  if (!Object.keys(byMonth).length) return 0;
  try { fs.mkdirSync(barArchDir(sym), { recursive: true }); } catch (e) { /* reported by the write below */ }
  Object.keys(byMonth).forEach((m) => {
    try {
      const file = path.join(barArchDir(sym), m + '.ndjson.gz');
      const map = new Map(readGzLines(file).map((b) => [b.t, b]));
      let changed = false;
      byMonth[m].forEach((b) => {
        if (!map.has(b.t)) { map.set(b.t, b); added++; changed = true; } else if (replace) { map.set(b.t, b); changed = true; }
      });
      if (changed) writeGzLines(file, Array.from(map.values()).sort((x, y) => x.t - y.t));
    } catch (e) {
      console.error('Could not archive bars', sym, m, e.message);
    }
  });
  return added;
}

// Checklist attached-image storage: one file per date, so re-attaching for
// the same day overwrites rather than accumulating. Lives under DATA_DIR
// (same Render Disk as everything else) so it survives deploys too.
const CHECKLIST_UPLOADS_DIR = path.join(DATA_DIR, 'uploads', 'checklist');
try {
  fs.mkdirSync(CHECKLIST_UPLOADS_DIR, { recursive: true });
} catch (e) {
  console.error('Could not create CHECKLIST_UPLOADS_DIR', CHECKLIST_UPLOADS_DIR, e.message);
}

// ============================================================================
// Journal + Rules persistence — same "keep an in-memory copy, mirror to a JSON
// file on disk under DATA_DIR" pattern as alerts.json above, so a Render Disk
// keeps journal/rules entries across deploys the same way it does for alerts.
// Both files store a plain { "<date>": <entry> } object, easy to upsert by date
// and to write straight back out with JSON.stringify.
// ============================================================================
const JOURNAL_FILE = path.join(DATA_DIR, 'journal.json');
const RULES_FILE = path.join(DATA_DIR, 'rules.json');
const CHECKLIST_FILE = path.join(DATA_DIR, 'checklist.json');

let journalEntries = {};
try {
  if (fs.existsSync(JOURNAL_FILE)) {
    journalEntries = JSON.parse(fs.readFileSync(JOURNAL_FILE, 'utf8'));
  }
} catch (e) {
  console.error('Could not read journal.json, starting fresh:', e.message);
}
// Logged at every startup (including restarts) so the logs make it obvious
// when a restart happened and how many journal entries it found on disk —
// e.g. "loaded 0 journal entries" right after you know you had several
// saved is a strong signal the disk write isn't actually persisting.
console.log(`journal.json: loaded ${Object.keys(journalEntries).length} entries from ${JOURNAL_FILE}`);

let rulesEntries = {};
try {
  if (fs.existsSync(RULES_FILE)) {
    rulesEntries = JSON.parse(fs.readFileSync(RULES_FILE, 'utf8'));
  }
} catch (e) {
  console.error('Could not read rules.json, starting fresh:', e.message);
}

let checklistEntries = {};
try {
  if (fs.existsSync(CHECKLIST_FILE)) {
    checklistEntries = JSON.parse(fs.readFileSync(CHECKLIST_FILE, 'utf8'));
  }
} catch (e) {
  console.error('Could not read checklist.json, starting fresh:', e.message);
}

// v11: checklist entries are now keyed by DATE + SYMBOL (composite key
// "<date>::<SYMBOLKEY>"), not date alone -- so more than one symbol can be
// saved on the same calendar day instead of the second save overwriting the
// first. Older checklist.json files have entries keyed by date only;
// migrate those in place on startup using whatever was already in that
// entry's own `symbol` field (or a generic "no symbol" bucket if it was
// blank). Nothing is lost, this just re-keys existing records once.
function checklistSymbolKey(rawSymbol) {
  const s = (rawSymbol || '').toString().trim().toUpperCase();
  return s || '_BLANK_';
}
function checklistCompositeKey(date, symbolKey) {
  return date + '::' + symbolKey;
}
function migrateLegacyChecklistEntries() {
  let migrated = false;
  const next = {};
  Object.keys(checklistEntries).forEach((key) => {
    const entry = checklistEntries[key] || {};
    if (key.indexOf('::') !== -1) {
      // Already a composite date+symbol key -- keep as-is.
      next[key] = entry;
      return;
    }
    const date = entry.date || key;
    const symbolKey = checklistSymbolKey(entry.symbol);
    next[checklistCompositeKey(date, symbolKey)] = Object.assign({}, entry, { date });
    migrated = true;
  });
  checklistEntries = next;
  if (migrated) {
    console.log('Migrated legacy (date-only) checklist entries to date+symbol keys.');
    saveChecklist();
  }
}
migrateLegacyChecklistEntries();

// v6: save* helpers now return true/false instead of silently swallowing a
// write failure. Root cause of a reported "entry saves fine, then vanishes
// later" bug: PUT /journal/:date always responded 200 with the entry echoed
// back (built entirely from the in-memory object, which was always updated
// correctly) EVEN IF the fs.writeFileSync() to disk underneath it failed —
// the failure was only ever console.error'd server-side, never surfaced to
// the client. As long as the same process stays running, that's invisible
// (the in-memory copy is still correct, so every GET/PUT still looks fine).
// But if the process restarts for ANY reason afterward (redeploy, crash,
// host-initiated restart) before a *successful* write ever landed on disk,
// journal.json is read back on startup without that entry — it looks like
// data "disappeared later" even though nothing deleted it, because it was
// never actually durable. Now every route below checks the return value and
// returns a real error to the client (500, with the reason) instead of a
// false-positive 200, and GET /health (added below) reports whether each
// file's on-disk state actually matches what's in memory.
function saveJournal() {
  try {
    fs.writeFileSync(JOURNAL_FILE, JSON.stringify(journalEntries, null, 2));
    return true;
  } catch (e) {
    console.error('Could not write journal.json:', e.message);
    return false;
  }
}

function saveRules() {
  try {
    fs.writeFileSync(RULES_FILE, JSON.stringify(rulesEntries, null, 2));
    return true;
  } catch (e) {
    console.error('Could not write rules.json:', e.message);
    return false;
  }
}

function saveChecklist() {
  try {
    fs.writeFileSync(CHECKLIST_FILE, JSON.stringify(checklistEntries, null, 2));
    return true;
  } catch (e) {
    console.error('Could not write checklist.json:', e.message);
    return false;
  }
}

// Autopsy is a plain LIST, not date-keyed like Journal/Rules — you can log more
// than one impulsive trade in the same session. Stored as { "<id>": <entry> },
// same disk-mirroring pattern; ids are server-generated the same way alert ids are.
const AUTOPSY_FILE = path.join(DATA_DIR, 'autopsy.json');

let autopsyEntries = {};
try {
  if (fs.existsSync(AUTOPSY_FILE)) {
    autopsyEntries = JSON.parse(fs.readFileSync(AUTOPSY_FILE, 'utf8'));
  }
} catch (e) {
  console.error('Could not read autopsy.json, starting fresh:', e.message);
}

function saveAutopsy() {
  try {
    fs.writeFileSync(AUTOPSY_FILE, JSON.stringify(autopsyEntries, null, 2));
    return true;
  } catch (e) {
    console.error('Could not write autopsy.json:', e.message);
    return false;
  }
}

// TradingView sends the alert body as plain text by default (whatever you typed in the
// alert message box). It can also be JSON if you formatted it that way. Accept both.
// NOTE: because this is registered for type '*/*', req.body is ALWAYS a raw string here —
// for ANY route, not just /webhook — so every route below that expects JSON must parse
// req.body itself (see /restore, /journal/:date, /rules/:date) rather than assuming
// Express already parsed it into an object.
// Bumped from 1mb to 8mb at v5 to fit the Checklist's attached-image upload
// (a base64 data URL, resized/compressed client-side before it's sent, but
// still comfortably bigger than every other route's small JSON/text body).
// v8: 200mb so POST /restore can take a full 100000-alert backup (~160 MB).
app.use(express.text({ type: '*/*', limit: '200mb' }));

// ---- Load any alerts saved from a previous run ----
let alerts = [];
try {
  if (fs.existsSync(DATA_FILE)) {
    alerts = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
  }
} catch (e) {
  console.error('Could not read alerts.json, starting fresh:', e.message);
}
console.log(`alerts.json: loaded ${alerts.length} alerts (MAX_ALERTS ${MAX_ALERTS}, MEM_ALERT_DAYS ${MEM_ALERT_DAYS})`);

// v8: compact JSON, written to a temp file then renamed (a crash mid-write can't leave a half-written alerts.json).
function saveAlerts() {
  try {
    const tmp = DATA_FILE + '.tmp';
    fs.writeFileSync(tmp, JSON.stringify(alerts.slice(0, MAX_ALERTS)));
    fs.renameSync(tmp, DATA_FILE);
    return true;
  } catch (e) {
    console.error('Could not write alerts.json:', e.message);
    return false;
  }
}

// v8: debounced save -- a burst of alerts in the same second costs one write, not one per alert.
let alertSaveTimer = null;
function scheduleSaveAlerts() {
  if (alertSaveTimer) return;
  alertSaveTimer = setTimeout(() => { alertSaveTimer = null; saveAlerts(); }, ALERT_SAVE_DELAY_MS);
}
function flushAlerts() {
  if (alertSaveTimer) { clearTimeout(alertSaveTimer); alertSaveTimer = null; saveAlerts(); }
}
// Render sends SIGTERM before stopping the old container on a deploy -- write any pending alerts first.
['SIGTERM', 'SIGINT'].forEach((sig) => process.on(sig, () => { flushAlerts(); process.exit(0); }));

// v9: archive every completed ET day that is in RAM, then drop alerts older than MEM_ALERT_DAYS from RAM.
// archivedCount remembers how many alerts of each day were archived, so unchanged days are not re-read.
const archivedCount = {};
let lastArchiveRun = null;
function archiveAlerts() {
  const today = etDay(Date.now());
  const byDay = {};
  alerts.forEach((a) => { const d = etDay(a.receivedAt); if (d < today) (byDay[d] || (byDay[d] = [])).push(a); });
  let added = 0;
  const failed = new Set();
  Object.keys(byDay).forEach((d) => {
    if (archivedCount[d] === byDay[d].length) return;
    added += mergeAlertsIntoArchive(byDay[d], failed);
    if (!failed.has(d) && fs.existsSync(alertDayFile(d))) archivedCount[d] = byDay[d].length; else failed.add(d);
  });
  const cut = new Date(Date.now() - MEM_ALERT_DAYS * 86400000).toISOString();
  const n0 = alerts.length;
  // only drop an alert from RAM if its day is safely in the archive
  alerts = alerts.filter((a) => a.receivedAt >= cut || failed.has(etDay(a.receivedAt)) || etDay(a.receivedAt) >= today);
  const dropped = n0 - alerts.length;
  if (dropped) scheduleSaveAlerts();
  lastArchiveRun = new Date().toISOString();
  if (added || dropped || failed.size) console.log(`archive: ${added} alert(s) archived, ${dropped} dropped from RAM (older than ${MEM_ALERT_DAYS} d)${failed.size ? ', FAILED days: ' + Array.from(failed).join(' ') : ''}`);
}

// ============================================================================
// v10: duplicate alerts.
//   (1) LIVE GUARD: an alert whose text is IDENTICAL to one received within the last DUP_WINDOW_SEC seconds
//       (env, default 60) is ignored -- not stored, not broadcast, not sent to Discord. The webhook still
//       answers 200 ("Duplicate ignored") so TradingView does not retry. BarFeed candles are not affected
//       (they already replace each other by candle time).
//   (2) CLEAN-UP of what is already stored (RAM + every archive day file):
//         GET  /dedupe?token=SECRET                 -> dry run: what would be removed (nothing changes)
//         POST /dedupe?token=SECRET&apply=1         -> removes them
//       Add &mode=near to also remove NEAR duplicates: same first line, same "Chart:" and "Time:" lines and the
//       same set of "•" alert names within the window, but slightly different text (e.g. two alerts on the same
//       chart). For near duplicates the LONGEST text is kept (the fuller snapshot); for identical ones the first.
//       &window=SEC overrides the window for the clean-up only. Alerts are compared across day boundaries.
// ============================================================================
const DUP_WINDOW_MS = Math.max(1, Number(process.env.DUP_WINDOW_SEC || 60)) * 1000;
const recentRaw = new Map(); // raw text -> last receivedAt (ms) of a STORED alert with that text
let duplicatesIgnored = 0;
let lastDedupe = null;

function isLiveDuplicate(raw, nowMs) {
  // prune old entries (Map keeps insertion order, oldest first)
  for (const [k, t] of recentRaw) { if (nowMs - t > DUP_WINDOW_MS) recentRaw.delete(k); else break; }
  const t = recentRaw.get(raw);
  return t !== undefined && nowMs - t <= DUP_WINDOW_MS;
}
function rememberRaw(raw, nowMs) { recentRaw.delete(raw); recentRaw.set(raw, nowMs); }

function alertRawText(a) { return typeof a.raw === 'string' ? a.raw : JSON.stringify(a.raw); }
function nearKey(raw) {
  const lines = raw.split('\n');
  const ch = /Chart: ([^\n]*)/.exec(raw);
  const tm = /Time: ([^\n]*)/.exec(raw);
  if (!ch || !tm) return null; // only alerts with a chart + time line can be near duplicates
  const names = lines.filter((l) => l.trim().startsWith('•')).map((l) => l.trim().split(':')[0]).sort().join('|');
  return [(lines[0] || '').trim(), ch[1].trim(), tm[1].trim(), names].join('##');
}

// Finds duplicate ids over RAM + archive. Reads one day file at a time and keeps only small summaries.
function findDuplicates(mode, windowMs) {
  const days = new Set(listAlertArchiveDays());
  const ramByDay = {};
  alerts.forEach((a) => { const d = etDay(a.receivedAt); days.add(d); (ramByDay[d] || (ramByDay[d] = [])).push(a); });
  const remove = new Map(); // id -> { day, kind }
  const lastExact = new Map(); // raw -> ms of the kept copy
  const lastNear = new Map(); // nearKey -> { id, ms, len, day }
  let scanned = 0;
  Array.from(days).sort().forEach((day) => {
    const seen = new Set();
    const list = [];
    (ramByDay[day] || []).concat(readGzLines(alertDayFile(day))).forEach((a) => {
      if (!a || !a.id || seen.has(a.id)) return;
      seen.add(a.id);
      const raw = alertRawText(a);
      list.push({ id: a.id, ms: Date.parse(a.receivedAt), raw, len: raw.length, day });
    });
    list.sort((x, y) => x.ms - y.ms || (x.id < y.id ? -1 : 1));
    scanned += list.length;
    list.forEach((x) => {
      const t = lastExact.get(x.raw);
      if (t !== undefined && x.ms - t <= windowMs) { remove.set(x.id, { day, kind: 'identical' }); return; }
      lastExact.set(x.raw, x.ms);
      if (mode !== 'near') return;
      const k = nearKey(x.raw);
      if (!k) return;
      const p = lastNear.get(k);
      if (p && x.ms - p.ms <= windowMs) {
        if (x.len > p.len) { remove.set(p.id, { day: p.day, kind: 'near' }); lastNear.set(k, { id: x.id, ms: p.ms, len: x.len, day }); }
        else remove.set(x.id, { day, kind: 'near' });
        return;
      }
      lastNear.set(k, { id: x.id, ms: x.ms, len: x.len, day });
    });
    // forget entries that can no longer match (keeps memory small over a long archive)
    const lastMs = list.length ? list[list.length - 1].ms : 0;
    for (const [k, t] of lastExact) if (lastMs - t > windowMs) lastExact.delete(k);
    for (const [k, p] of lastNear) if (lastMs - p.ms > windowMs) lastNear.delete(k);
  });
  return { scanned, remove };
}

function dedupeHandler(req, res) {
  if (SECRET && req.query.token !== SECRET) return res.status(401).send('Unauthorized');
  const mode = req.query.mode === 'near' ? 'near' : 'identical';
  const windowMs = Number(req.query.window) > 0 ? Number(req.query.window) * 1000 : DUP_WINDOW_MS;
  const apply = req.method === 'POST' && (req.query.apply === '1' || req.query.apply === 'true');
  flushAlerts();
  const { scanned, remove } = findDuplicates(mode, windowMs);
  const perDay = {};
  let identical = 0, near = 0;
  remove.forEach((v) => { perDay[v.day] = (perDay[v.day] || 0) + 1; if (v.kind === 'near') near++; else identical++; });
  let filesRewritten = 0, ramRemoved = 0;
  const errors = [];
  if (apply && remove.size) {
    Object.keys(perDay).forEach((day) => {
      const file = alertDayFile(day);
      if (!fs.existsSync(file)) return;
      try {
        const old = readGzLines(file);
        const keep = old.filter((a) => !remove.has(a.id));
        if (keep.length !== old.length) { writeGzLines(file, keep); filesRewritten++; }
      } catch (e) { errors.push(day + ': ' + e.message); }
    });
    const n0 = alerts.length;
    alerts = alerts.filter((a) => !remove.has(a.id));
    ramRemoved = n0 - alerts.length;
    Object.keys(archivedCount).forEach((d) => { delete archivedCount[d]; }); // recount on the next archive run
    saveAlerts();
  }
  lastDedupe = { at: new Date().toISOString(), mode, windowSec: windowMs / 1000, applied: apply, scanned, found: remove.size, identical, near, filesRewritten, ramRemoved };
  console.log(`dedupe (${mode}, ${windowMs / 1000} s, ${apply ? 'APPLIED' : 'dry run'}): scanned ${scanned}, duplicates ${remove.size} (identical ${identical}, near ${near}), files rewritten ${filesRewritten}, RAM removed ${ramRemoved}${errors.length ? ', errors: ' + errors.join('; ') : ''}`);
  res.json(Object.assign({}, lastDedupe, { perDay, errors, note: apply ? 'Removed.' : 'Dry run -- nothing changed. POST with &apply=1 to remove.' }));
}

// ---- Live-update clients (Server-Sent Events) ----
let sseClients = [];

function broadcast(alert) {
  const payload = `data: ${JSON.stringify(alert)}\n\n`;
  sseClients.forEach((res) => res.write(payload));
}

// v2 (10/07/2026): named SSE events (e.g. "bar") -- the page's default onmessage handler never sees them,
// so older pages simply ignore bar updates.
function broadcastEvent(name, obj) {
  const payload = `event: ${name}\ndata: ${JSON.stringify(obj)}\n\n`;
  sseClients.forEach((res) => res.write(payload));
}

// ============================================================================
// v2 (10/07/2026): BarFeed bars for the Alert Feed Chart tab.
// The "BarFeed" Pine indicator sends one JSON alert per closed 3m candle:
//   {"type":"bar","sym":"MES","tf":3,"t":<open ms>,"o":..,"h":..,"l":..,"c":..,"v":..,"e9":..,...,"fl":"S1"}
// These are NOT added to the alert list (no feed spam, no Discord). They go to
// DATA_DIR/bars/<SYM>.ndjson (one JSON line per bar, appended), are kept in
// memory per symbol sorted by time, and are trimmed to BAR_KEEP_DAYS (60).
// v9: trimmed candles are moved to archive/bars/<SYM>/YYYY-MM.ndjson.gz, not deleted.
// A re-sent candle (same t) replaces the old one (last line wins on reload).
// ============================================================================
const BARS_DIR = path.join(DATA_DIR, 'bars');
try { fs.mkdirSync(BARS_DIR, { recursive: true }); } catch (e) { console.error('Could not create BARS_DIR', BARS_DIR, e.message); }
const BAR_KEEP_DAYS = Number(process.env.BAR_KEEP_DAYS || 60);
const BAR_NUM_FIELDS = ['o', 'h', 'l', 'c', 'v', 'e9', 'e20', 'h9', 'h20', 'e200', 'vw', 'pp', 'r1', 's1', 'ydh', 'ydl', 'nyh', 'nyl', 'lnh', 'lnl', 'ash', 'asl', 'hc', 'hf'];
const BAR_SYM_RE = /^[A-Z0-9]{1,12}(_[0-9]{1,3})?$/; // v3: key = SYMBOL, or SYMBOL_<minutes> for a non-3m feed
let bars = {}; // sym -> array of bars sorted by t (ms)

function barFile(sym) { return path.join(BARS_DIR, sym + '.ndjson'); }

function cleanBar(b) {
  const t = Number(b && b.t);
  if (!Number.isFinite(t) || t <= 0) return null;
  const out = { t: Math.round(t) };
  BAR_NUM_FIELDS.forEach((k) => {
    const v = b[k];
    out[k] = (v === null || v === undefined || v === '' || !Number.isFinite(Number(v))) ? null : Number(v);
  });
  if (out.o === null || out.h === null || out.l === null || out.c === null) return null;
  out.fl = typeof b.fl === 'string' ? b.fl.slice(0, 80) : '';
  return out;
}

function barCutoff() { return Date.now() - BAR_KEEP_DAYS * 86400000; }

// Insert or replace by t, keeping the array sorted. Returns true if it was a brand-new candle.
function upsertBar(sym, bar) {
  const arr = bars[sym] || (bars[sym] = []);
  if (!arr.length || arr[arr.length - 1].t < bar.t) { arr.push(bar); return true; }
  let lo = 0, hi = arr.length - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    if (arr[mid].t === bar.t) { arr[mid] = bar; return false; }
    if (arr[mid].t < bar.t) lo = mid + 1; else hi = mid - 1;
  }
  arr.splice(lo, 0, bar);
  return true;
}

function rewriteBarFile(sym) {
  try {
    fs.writeFileSync(barFile(sym), (bars[sym] || []).map((b) => JSON.stringify(b)).join('\n') + '\n');
    return true;
  } catch (e) {
    console.error('Could not write bars file', sym, e.message);
    return false;
  }
}

function trimBars(rewrite) {
  const cut = barCutoff();
  Object.keys(bars).forEach((sym) => {
    const arr = bars[sym];
    let i = 0;
    while (i < arr.length && arr[i].t < cut) i++;
    if (i > 0) {
      const n = mergeBarsIntoArchive(sym, arr.slice(0, i), true); // v9: archive (RAM copy is the newest) before trimming
      console.log(`bars archive ${sym}: ${i} candle(s) moved to archive (${n} new)`);
      bars[sym] = arr.slice(i);
      if (rewrite) rewriteBarFile(sym);
    }
  });
}

function loadBars() {
  let files = [];
  try { files = fs.readdirSync(BARS_DIR).filter((f) => f.endsWith('.ndjson')); } catch (e) { return; }
  files.forEach((f) => {
    const sym = f.replace(/\.ndjson$/, '');
    if (!BAR_SYM_RE.test(sym)) return;
    bars[sym] = [];
    try {
      fs.readFileSync(path.join(BARS_DIR, f), 'utf8').split('\n').forEach((line) => {
        if (!line.trim()) return;
        try { const b = cleanBar(JSON.parse(line)); if (b) upsertBar(sym, b); } catch (e) { /* skip a bad line */ }
      });
    } catch (e) {
      console.error('Could not read bars file', f, e.message);
    }
  });
  trimBars(false);
  Object.keys(bars).forEach((sym) => rewriteBarFile(sym)); // compact: one line per candle, trimmed
  console.log('bars: loaded ' + Object.keys(bars).map((s) => s + '=' + bars[s].length).join(', '));
}
loadBars();
setInterval(() => trimBars(true), 3600000); // hourly: move candles older than BAR_KEEP_DAYS to the archive

// v9: archive alerts shortly after startup and then hourly.
setTimeout(archiveAlerts, 5000);
setInterval(archiveAlerts, 3600000);

function handleBar(parsed) {
  const root = String(parsed.sym || '').toUpperCase().replace(/[^A-Z0-9]/g, '');
  const tf = parseInt(parsed.tf, 10) || 3;
  const sym = tf === 3 ? root : root + '_' + tf; // v3: 3m keeps the plain key so existing files stay valid
  if (!BAR_SYM_RE.test(sym)) return 'bad symbol';
  const bar = cleanBar(parsed);
  if (!bar) return 'bad bar';
  upsertBar(sym, bar);
  try {
    // v4: the newest candle (new, or a BarFeed v1.01 "live" re-send of the forming candle) is just appended -- the
    // reload at startup keeps the last line per candle, so no full-file rewrite every minute. Older candles rewrite.
    if (bars[sym][bars[sym].length - 1] === bar) fs.appendFileSync(barFile(sym), JSON.stringify(bar) + '\n');
    else rewriteBarFile(sym);
  } catch (e) {
    console.error('Could not append bar', sym, e.message);
  }
  broadcastEvent('bar', { sym, bar });
  return null;
}

// ---- Discord forwarding ----
// Turns the plain-text alert body into a Discord embed: bullet lines (the "• LTF(3)..." headline
// lines) become the description, and every "Key: Value" line becomes its own field — giving
// something visually closer to the on-chart Status table than a wall of plain text.
function buildDiscordEmbed(rawText) {
  const lines = rawText.split('\n').map((l) => l.trim()).filter((l) => l.length > 0);
  const title = lines[0] || 'TradingView Alert';
  const bulletLines = lines.filter((l) => l.startsWith('•'));
  const fieldLines = lines.filter((l) => !l.startsWith('•') && l.includes(': ') && l !== lines[0]);

  const upper = rawText.toUpperCase();
  const bullish = (upper.match(/LONG|BULLISH/g) || []).length;
  const bearish = (upper.match(/SHORT|BEARISH/g) || []).length;
  const color = bullish > bearish ? 0x22c55e : bearish > bullish ? 0xef4444 : 0x6b7280;

  const fields = fieldLines.slice(0, 25).map((line) => {
    const idx = line.indexOf(': ');
    return {
      name: line.slice(0, idx).slice(0, 256) || '​',
      value: line.slice(idx + 2).slice(0, 1024) || '​',
      inline: true,
    };
  });

  return {
    title: title.slice(0, 256),
    description: bulletLines.join('\n').slice(0, 4096) || undefined,
    color,
    fields,
    timestamp: new Date().toISOString(),
  };
}

async function sendToDiscord(rawText) {
  if (!DISCORD_WEBHOOK_URL) return;
  try {
    const embed = buildDiscordEmbed(rawText);
    const resp = await fetch(DISCORD_WEBHOOK_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ embeds: [embed] }),
    });
    if (!resp.ok) {
      console.error('Discord forward failed:', resp.status, await resp.text());
    }
  } catch (e) {
    console.error('Discord forward error:', e.message);
  }
}

// ---- Webhook endpoint: TradingView posts here ----
app.post('/webhook', (req, res) => {
  if (SECRET && req.query.token !== SECRET) {
    return res.status(401).send('Unauthorized: bad or missing token');
  }

  let body = req.body;
  let parsed = null;
  if (typeof body === 'string') {
    try {
      parsed = JSON.parse(body);
    } catch (e) {
      parsed = null; // plain text alert, that's fine
    }
  }

  // v2: BarFeed candles go to the bar store, not the alert list.
  if (parsed && parsed.type === 'bar') {
    const err = handleBar(parsed);
    const bt = new Date(Number(parsed.t)).toLocaleTimeString('en-US', { timeZone: 'America/New_York', hour: '2-digit', minute: '2-digit', hour12: false });
    console.log(`bar ${parsed.sym} ${parsed.tf}m ${bt} ET ${parsed.live ? 'LIVE' : 'CLOSE'} c=${parsed.c}${err ? ' REJECTED: ' + err : ''}`);
    if (err) return res.status(400).send(err);
    return res.status(200).send('OK');
  }

  // v10: ignore an alert identical to one stored within the last DUP_WINDOW_SEC seconds (TradingView double-send,
  // or the same alert set up twice). Answer 200 so TradingView does not retry.
  const rawText = typeof body === 'string' ? body : JSON.stringify(body);
  const nowMs = Date.now();
  if (isLiveDuplicate(rawText, nowMs)) {
    duplicatesIgnored++;
    console.log(`alert DUPLICATE ignored (identical within ${DUP_WINDOW_MS / 1000} s): ${(rawText.split('\n')[0] || '').slice(0, 60)}`);
    return res.status(200).send('Duplicate ignored');
  }
  rememberRaw(rawText, nowMs);
  const alert = {
    id: Date.now() + '-' + Math.random().toString(36).slice(2, 8),
    receivedAt: new Date().toISOString(),
    raw: typeof body === 'string' ? body : JSON.stringify(body),
    json: parsed,
  };

  alerts.unshift(alert);
  if (alerts.length > MAX_ALERTS) {
    mergeAlertsIntoArchive(alerts.slice(MAX_ALERTS)); // v9: archive before the RAM cap drops them
    alerts.length = MAX_ALERTS; // v8: trim in place (no 100k-element copy per alert)
  }
  scheduleSaveAlerts(); // v8: debounced
  broadcast(alert);
  sendToDiscord(alert.raw);

  const lines = alert.raw.split('\n').map((l) => l.trim()).filter(Boolean);
  const what = lines.filter((l) => l.startsWith('•')).map((l) => l.replace(/^•\s*/, '')).slice(0, 3).join(' + ') || (lines[1] || '').slice(0, 80);
  console.log(`alert ${(lines[0] || '').replace(/\s*—\s*$/, '')} | ${what} (${alert.raw.length} chars)`);
  res.status(200).send('OK');
});

function sendJsonMaybeGzip(req, res, obj) {
  const body = JSON.stringify(obj);
  res.set('Content-Type', 'application/json; charset=utf-8');
  if (/\bgzip\b/.test(req.headers['accept-encoding'] || '')) {
    zlib.gzip(body, { level: 6 }, (err, gz) => {
      if (err) return res.send(body);
      res.set('Content-Encoding', 'gzip');
      res.set('Vary', 'Accept-Encoding');
      res.send(gz);
    });
  } else {
    res.send(body);
  }
}

// ---- JSON list of stored alerts (used by the dashboard on load) ----
// v8: optional ?days=N (only alerts received in the last N days) and ?limit=N (newest N); no params = all
// in RAM, same as before. Sent gzip-compressed when the client accepts it (browsers and urllib with the header do).
// v9: ?from=YYYY-MM-DD[&to=YYYY-MM-DD] (ET days, inclusive) reads archive + RAM. ?days=N larger than
// MEM_ALERT_DAYS also reads the archive.
app.get('/alerts', (req, res) => {
  let list = alerts;
  const days = Number(req.query.days);
  const from = String(req.query.from || '');
  const to = String(req.query.to || '');
  if ((from && !DAY_RE.test(from)) || (to && !DAY_RE.test(to))) return res.status(400).send('from / to must be YYYY-MM-DD');
  if (from || to) {
    list = readAlertRange(from || '0000-00-00', to || '9999-99-99');
  } else if (Number.isFinite(days) && days > 0) {
    const cut = new Date(Date.now() - days * 86400000).toISOString();
    if (days > MEM_ALERT_DAYS) list = readAlertRange(etDay(Date.now() - days * 86400000), '9999-99-99');
    let n = 0;
    while (n < list.length && list[n].receivedAt >= cut) n++; // newest first, so stop at the first older one
    list = list.slice(0, n);
  }
  const limit = Number(req.query.limit);
  if (Number.isFinite(limit) && limit > 0) list = list.slice(0, Math.floor(limit));
  sendJsonMaybeGzip(req, res, list);
});

// ---- v9: what is in the archive ----
app.get('/archive', (req, res) => {
  const fsz = (f) => { try { return fs.statSync(f).size; } catch (e) { return 0; } };
  const days = listAlertArchiveDays();
  let barSyms = [];
  try { barSyms = fs.readdirSync(BAR_ARCH_DIR).filter((s) => BAR_SYM_RE.test(s)).sort(); } catch (e) { /* none yet */ }
  res.json({
    memAlertDays: MEM_ALERT_DAYS,
    barKeepDays: BAR_KEEP_DAYS,
    lastArchiveRun,
    alerts: { days: days.length, first: days[0] || null, last: days[days.length - 1] || null, bytes: days.reduce((s, d) => s + fsz(alertDayFile(d)), 0), list: days },
    bars: barSyms.map((s) => {
      const months = listBarArchiveMonths(s);
      return { sym: s, months, bytes: months.reduce((t, m) => t + fsz(path.join(barArchDir(s), m + '.ndjson.gz')), 0) };
    }),
  });
});

// ---- v10: remove duplicate alerts already stored (see the v10 block near the top) ----
app.get('/dedupe', dedupeHandler);   // dry run only
app.post('/dedupe', dedupeHandler);  // &apply=1 removes

// ---- v2: BarFeed bars for the Chart tab ----
// GET /bars                     -> [{ sym, count, first, last, archivedMonths }]
// GET /bars?sym=MES&days=5      -> { sym, bars: [...] } (last N days; v9: N > BAR_KEEP_DAYS reads the archive)
// GET /bars?sym=MES&from=2026-08-01[&to=2026-09-30]  -> v9: ET days, inclusive, archive + RAM
app.get('/bars', (req, res) => {
  const sym = String(req.query.sym || '').toUpperCase();
  if (!sym) {
    return res.json(Object.keys(bars).sort().map((s) => ({
      sym: s, tf: s.includes('_') ? Number(s.split('_')[1]) : 3, count: bars[s].length,
      first: bars[s].length ? bars[s][0].t : null,
      last: bars[s].length ? bars[s][bars[s].length - 1].t : null,
      archivedMonths: listBarArchiveMonths(s).length,
    })));
  }
  if (!BAR_SYM_RE.test(sym)) return res.status(400).send('bad symbol');
  const from = String(req.query.from || '');
  const to = String(req.query.to || '');
  if ((from && !DAY_RE.test(from)) || (to && !DAY_RE.test(to))) return res.status(400).send('from / to must be YYYY-MM-DD');
  const mem = bars[sym] || [];
  let lo, hi;
  if (from || to) {
    lo = from || '0000-00-00'; hi = to || '9999-99-99';
  } else {
    const days = Math.max(1, Number(req.query.days) || 5);
    const cut = Date.now() - days * 86400000;
    if (cut >= barCutoff() || days <= BAR_KEEP_DAYS) return res.json({ sym, bars: mem.filter((b) => b.t >= cut) }); // unchanged fast path
    lo = etDay(cut); hi = '9999-99-99';
  }
  const map = new Map();
  listBarArchiveMonths(sym).filter((m) => m >= lo.slice(0, 7) && m <= hi.slice(0, 7)).forEach((m) => {
    readGzLines(path.join(barArchDir(sym), m + '.ndjson.gz')).forEach((b) => map.set(b.t, b));
  });
  mem.forEach((b) => map.set(b.t, b)); // RAM copy wins
  const out = Array.from(map.values()).filter((b) => { const d = etDay(b.t); return d >= lo && d <= hi; }).sort((x, y) => x.t - y.t);
  sendJsonMaybeGzip(req, res, { sym, bars: out });
});

// POST /bars/import?token=SECRET&sym=MES  -- history backfill from TradingView "Export chart data" (CSV, with
// BarFeed on the chart so its Data Window columns e9, e20, h9 ... are included) or a JSON array of bars.
// Candles that already exist (from the live feed) are kept; only missing ones are added.
// v7: add &replace=1 to overwrite existing candles (same open time) with the file's values.
// v9: candles older than BAR_KEEP_DAYS go straight to the archive (before v9 they were silently skipped).
function splitCsvLine(line) {
  const out = []; let cur = ''; let q = false;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (q) { if (ch === '"') { if (line[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += ch; }
    else if (ch === '"') q = true;
    else if (ch === ',') { out.push(cur); cur = ''; }
    else cur += ch;
  }
  out.push(cur);
  return out;
}
function csvToBars(text) {
  const lines = text.split(/\r?\n/).filter((l) => l.trim());
  if (lines.length < 2) return [];
  const head = splitCsvLine(lines[0]).map((h) => h.trim().toLowerCase());
  const col = (names) => head.findIndex((h) => names.includes(h));
  const iT = col(['time', 'date', 'datetime']);
  const map = { o: col(['open']), h: col(['high']), l: col(['low']), c: col(['close']), v: col(['volume']) };
  BAR_NUM_FIELDS.slice(5).forEach((k) => { map[k] = col([k]); });
  const iFl = col(['fl']);
  if (iT < 0 || map.o < 0 || map.c < 0) throw new Error('CSV needs time, open, high, low, close columns');
  return lines.slice(1).map((l) => {
    const c = splitCsvLine(l);
    const raw = (c[iT] || '').trim();
    const tNum = Number(raw);
    const t = Number.isFinite(tNum) ? (tNum < 1e12 ? tNum * 1000 : tNum) : Date.parse(raw);
    const b = { t };
    Object.keys(map).forEach((k) => { if (map[k] >= 0) b[k] = c[map[k]]; });
    if (iFl >= 0 && Number(c[iFl]) === 1) b.fl = 'flop';
    return b;
  });
}
app.post('/bars/import', (req, res) => {
  if (SECRET && req.query.token !== SECRET) return res.status(401).send('Unauthorized');
  const sym = String(req.query.sym || '').toUpperCase();
  if (!BAR_SYM_RE.test(sym)) return res.status(400).send('Add ?sym=MES (or MGC, or MES_2 / MGC_5 / MES_1 for a 2m / 5m / 1m feed)');
  let list;
  try {
    const body = typeof req.body === 'string' ? req.body : '';
    list = body.trim().startsWith('[') ? JSON.parse(body) : csvToBars(body);
  } catch (e) {
    return res.status(400).send('Could not read the file: ' + e.message);
  }
  const cut = barCutoff();
  const replace = req.query.replace === '1' || req.query.replace === 'true'; // v7
  const have = new Set((bars[sym] || []).map((b) => b.t));
  let added = 0, replaced = 0;
  const old = []; // v9: older than BAR_KEEP_DAYS -> archive
  list.forEach((raw) => {
    const b = cleanBar(raw);
    if (!b) return;
    if (b.t < cut) { old.push(b); return; }
    if (have.has(b.t)) {
      if (!replace) return;
      upsertBar(sym, b); replaced++;
      return;
    }
    upsertBar(sym, b); have.add(b.t); added++;
  });
  if (added || replaced) rewriteBarFile(sym);
  const archived = old.length ? mergeBarsIntoArchive(sym, old, replace) : 0;
  console.log(`bars import ${sym}: ${added} added, ${replaced} replaced${replace ? ' (replace on)' : ''}, ${old.length} older than ${BAR_KEEP_DAYS} d -> archive (${archived} new)`);
  res.send(`Imported ${added} new candle(s)` + (replace ? ` and replaced ${replaced} existing candle(s)` : '') + ` for ${sym} (${(bars[sym] || []).length} stored)` +
    (old.length ? `; ${old.length} older candle(s) went to the archive (${archived} new).` : '.'));
});

// ---- Live stream for the dashboard ----
app.get('/stream', (req, res) => {
  res.set({
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache',
    Connection: 'keep-alive',
  });
  res.flushHeaders();
  sseClients.push(res);

  req.on('close', () => {
    sseClients = sseClients.filter((c) => c !== res);
  });
});

// ---- Dashboard page ----
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// ---- Checklist attached images (served straight off disk) ----
app.use('/checklist-uploads', express.static(CHECKLIST_UPLOADS_DIR));

// ---- Clear all stored alerts ----
// v9: clears the alerts in RAM / alerts.json only; the archive on disk is left alone.
app.post('/clear', (req, res) => {
  if (SECRET && req.query.token !== SECRET) {
    return res.status(401).send('Unauthorized');
  }
  alerts = [];
  flushAlerts();
  saveAlerts();
  res.status(200).send('Cleared');
});

// ---- Restore alerts from a previously-saved backup ----
// Use this to bring back alert history after moving to a new/empty disk (e.g. the one-time
// switch to a Render persistent Disk): first save a backup by visiting /alerts in a browser
// and saving what it returns, then after the switch POST that same JSON here, e.g.:
//   curl -X POST "https://YOUR-APP.onrender.com/restore?token=YOUR_SECRET" \
//        -H "Content-Type: application/json" --data-binary @alerts.json
// Replaces whatever alerts are currently stored (same "last MAX_ALERTS win" trimming as normal).
// v9: also merged into the archive, so older backups (e.g. a saved 10/12-10/18 /alerts file) land there.
app.post('/restore', (req, res) => {
  if (SECRET && req.query.token !== SECRET) {
    return res.status(401).send('Unauthorized');
  }
  let parsed;
  try {
    parsed = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
  } catch (e) {
    return res.status(400).send('Body is not valid JSON: ' + e.message);
  }
  if (!Array.isArray(parsed)) {
    return res.status(400).send('Expected a JSON array of alerts (the same shape /alerts returns).');
  }
  const archived = mergeAlertsIntoArchive(parsed.filter((a) => a && a.receivedAt && etDay(a.receivedAt) < etDay(Date.now())));
  alerts = parsed.slice(0, MAX_ALERTS);
  flushAlerts();
  saveAlerts();
  archiveAlerts(); // drop anything older than MEM_ALERT_DAYS from RAM (now safely archived)
  res.status(200).send(`Restored ${parsed.length} alert(s); ${archived} new in the archive; ${alerts.length} kept in RAM.`);
});

// ============================================================================
// Journal routes
// GET    /journal        -> array of all entries (frontend keys them by .date itself)
// PUT    /journal/:date   -> upsert one day, body is the full entry, echoes it back
// DELETE /journal/:date   -> remove one day
// ============================================================================
app.get('/journal', (req, res) => {
  res.json(Object.values(journalEntries));
});

app.put('/journal/:date', (req, res) => {
  let body;
  try {
    body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
  } catch (e) {
    return res.status(400).send('Body is not valid JSON: ' + e.message);
  }
  const date = req.params.date;
  const entry = {
    date,
    title: body.title || '',
    amount: (body.amount === null || body.amount === undefined || body.amount === '' || isNaN(body.amount))
      ? null : Number(body.amount),
    premarket: body.premarket || '',
    losses: body.losses || '',
    issues: body.issues || '',
    wins: body.wins || '',
  };
  journalEntries[date] = entry;
  if (!saveJournal()) {
    return res.status(500).json({ error: 'Saved in memory but failed to write journal.json to disk — this entry will be lost if the server restarts before a write succeeds. Check server logs / DATA_DIR permissions.', entry });
  }
  res.json(entry);
});

app.delete('/journal/:date', (req, res) => {
  delete journalEntries[req.params.date];
  if (!saveJournal()) {
    return res.status(500).send('Deleted in memory but failed to write journal.json to disk — check server logs / DATA_DIR permissions.');
  }
  res.status(200).send('Deleted');
});

// ============================================================================
// Rules routes
// GET    /rules        -> array of all entries
// PUT    /rules/:date   -> upsert one day, body is { date, items: { <id>: {answer, note} } }
// ============================================================================
app.get('/rules', (req, res) => {
  res.json(Object.values(rulesEntries));
});

app.put('/rules/:date', (req, res) => {
  let body;
  try {
    body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
  } catch (e) {
    return res.status(400).send('Body is not valid JSON: ' + e.message);
  }
  const date = req.params.date;
  const items = (body.items && typeof body.items === 'object') ? body.items : {};
  // Normalize so a malformed/missing item never breaks the frontend's expectations.
  const cleanItems = {};
  Object.keys(items).forEach((id) => {
    const it = items[id] || {};
    const answer = (it.answer === 'Y' || it.answer === 'N') ? it.answer : null;
    cleanItems[id] = { answer, note: it.note || '' };
  });
  const entry = { date, items: cleanItems };
  rulesEntries[date] = entry;
  saveRules();
  res.json(entry);
});

// Optional — not currently used by the frontend (there's no delete button in
// the Rules tab), but here in case you want one later, matching /journal's shape.
app.delete('/rules/:date', (req, res) => {
  delete rulesEntries[req.params.date];
  saveRules();
  res.status(200).send('Deleted');
});

// ============================================================================
// Checklist routes — v11: keyed by DATE + SYMBOL, not date alone, so more
// than one symbol can have its own checklist entry on the same calendar day.
// GET    /checklist                    -> array of ALL entries, every date+symbol
// PUT    /checklist/:date/:symbol       -> upsert one entry, body is { date, time, symbol, items: {...} }
// DELETE /checklist/:date/:symbol       -> remove one entry (used by "Clear entry")
//
// :symbol in the URL is either an encoded, uppercased symbol (e.g. "MES1%21")
// or the literal "_none_" placeholder for an entry with a blank Symbol field
// -- URL segments can't be truly empty, so the frontend sends that literal
// and the server maps it back to the same "_BLANK_" bucket the migration
// above uses. The `symbol` field actually saved/returned is whatever display
// text the frontend sent (original casing), independent of the URL key.
//
// v4: items are no longer a fixed {checked, note} shape -- the frontend now has
// several different item field layouts (plain checkbox; a boxes row; a
// risk-limit + stop-structure-type combo; a direction pulldown + confluence
// checkboxes; a plain checkbox group). Rather than whitelist every field name
// here (which would need updating every time the checklist's fields change),
// each item is passed through as-is except every field VALUE is coerced to
// either a bool or a string -- so a checkbox always saves as true/false and a
// text/select field always saves as a string, regardless of what field keys
// exist this round, while still rejecting anything that isn't plain JSON
// data (no functions, no nested objects/arrays sneaking into the saved file).
// ============================================================================
const CHECKLIST_DATE_RE = /^\d{4}-\d{2}-\d{2}$/;

// A URL symbol segment is either the literal "_none_" (blank symbol) or an
// encoded token made only of the characters a real symbol could produce
// once uppercased/trimmed client-side -- blocks anything path-traversal-ish
// from riding in on this segment before it ever reaches checklistSymbolKey.
function parseChecklistSymbolParam(raw) {
  if (raw === '_none_') return '_BLANK_';
  let decoded;
  try {
    decoded = decodeURIComponent(raw);
  } catch (e) {
    return null;
  }
  const key = checklistSymbolKey(decoded);
  if (!/^[A-Z0-9!._-]{1,20}$/.test(key)) return null;
  return key;
}

app.get('/checklist', (req, res) => {
  res.json(Object.values(checklistEntries));
});

app.put('/checklist/:date/:symbol', (req, res) => {
  const date = req.params.date;
  if (!CHECKLIST_DATE_RE.test(date)) {
    return res.status(400).send('Invalid date, expected YYYY-MM-DD');
  }
  const symbolKey = parseChecklistSymbolParam(req.params.symbol);
  if (!symbolKey) {
    return res.status(400).send('Invalid symbol');
  }
  let body;
  try {
    body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
  } catch (e) {
    return res.status(400).send('Body is not valid JSON: ' + e.message);
  }
  const items = (body.items && typeof body.items === 'object') ? body.items : {};
  const cleanItems = {};
  Object.keys(items).forEach((id) => {
    const it = items[id] || {};
    const cleanFields = {};
    Object.keys(it).forEach((key) => {
      const val = it[key];
      cleanFields[key] = typeof val === 'boolean' ? val : (val === null || val === undefined ? '' : String(val));
    });
    cleanItems[id] = cleanFields;
  });
  const time = body.time === null || body.time === undefined ? '' : String(body.time);
  const symbol = body.symbol === null || body.symbol === undefined ? '' : String(body.symbol);
  // Keep whatever images were already attached to this date+symbol entry --
  // this route only ever touches time/symbol/items, images are managed by
  // the routes below.
  const compositeKey = checklistCompositeKey(date, symbolKey);
  const priorImages = (checklistEntries[compositeKey] && Array.isArray(checklistEntries[compositeKey].images))
    ? checklistEntries[compositeKey].images : [];
  const entry = { date, time, symbol, items: cleanItems, images: priorImages };
  checklistEntries[compositeKey] = entry;
  saveChecklist();
  res.json(entry);
});

app.delete('/checklist/:date/:symbol', (req, res) => {
  const date = req.params.date;
  const symbolKey = parseChecklistSymbolParam(req.params.symbol);
  if (!CHECKLIST_DATE_RE.test(date) || !symbolKey) {
    return res.status(400).send('Invalid date or symbol');
  }
  delete checklistEntries[checklistCompositeKey(date, symbolKey)];
  saveChecklist();
  res.status(200).send('Deleted');
});

// ============================================================================
// Checklist attached-image routes — MULTIPLE images per date+symbol entry,
// each stored as its own file on disk (not inside checklist.json, which just
// holds an `images` array of {filename, url, name, uploadedAt} references)
// so the JSON store stays small and fast to read/write.
//
// v7: filenames are date+time+original-name based, e.g.
//   2026-09-18_14-32-05-a1b2_entry-screenshot.jpg
// v11: filenames also fold in the symbol, e.g.
//   2026-09-18_MES1!_14-32-05-a1b2_entry-screenshot.jpg
// so every upload gets its own file (nothing overwrites a prior attach) and
// the filename itself is human-readable in a folder listing, including
// which symbol it belongs to. The random 4-char tag guards against two
// uploads landing in the same second.
//
// POST   /checklist/:date/:symbol/image             -> body { dataUrl, originalName? } ; appends one image, returns updated entry
// DELETE /checklist/:date/:symbol/image/:filename   -> removes one image by filename, returns updated entry
// ============================================================================

// Only allow a small known set of image mime types through, and map each to
// a fixed extension.
const IMAGE_MIME_EXT = {
  'image/jpeg': 'jpg',
  'image/jpg': 'jpg',
  'image/png': 'png',
  'image/webp': 'webp',
  'image/gif': 'gif',
};

// Strips any extension, then keeps only filesystem-safe characters -- this
// is the ONLY thing derived from client input that ends up in the filename,
// so it's tightly whitelisted (no slashes, dots, or path-traversal tricks).
function sanitizeImageBaseName(name) {
  const noExt = String(name || '').replace(/\.[a-zA-Z0-9]{1,6}$/, '');
  const safe = noExt.replace(/[^a-zA-Z0-9_-]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 60);
  return safe || 'image';
}

function pad2(n) { return String(n).padStart(2, '0'); }

// Builds a unique, sortable, human-readable filename: date + symbol key +
// time + a short random tag (collision guard) + the sanitized original name
// + extension.
function buildChecklistImageFilename(date, symbolKey, ext, originalName) {
  const now = new Date();
  const timePart = `${pad2(now.getHours())}-${pad2(now.getMinutes())}-${pad2(now.getSeconds())}`;
  const rand = Math.random().toString(36).slice(2, 6);
  const base = sanitizeImageBaseName(originalName);
  const safeSymbol = symbolKey.replace(/[^A-Z0-9!._-]/g, '') || 'SYM';
  return `${date}_${safeSymbol}_${timePart}-${rand}_${base}.${ext}`;
}

// A filename supplied back to us for deletion must exactly match this shape
// (same charset buildChecklistImageFilename produces) before it's allowed
// anywhere near the filesystem -- blocks path traversal / arbitrary unlink.
const CHECKLIST_IMAGE_FILENAME_RE = /^[a-zA-Z0-9!._-]+\.(jpg|png|webp|gif)$/;

app.post('/checklist/:date/:symbol/image', (req, res) => {
  const date = req.params.date;
  if (!CHECKLIST_DATE_RE.test(date)) {
    return res.status(400).send('Invalid date, expected YYYY-MM-DD');
  }
  const symbolKey = parseChecklistSymbolParam(req.params.symbol);
  if (!symbolKey) {
    return res.status(400).send('Invalid symbol');
  }
  let body;
  try {
    body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
  } catch (e) {
    return res.status(400).send('Body is not valid JSON: ' + e.message);
  }
  const dataUrl = typeof body.dataUrl === 'string' ? body.dataUrl : '';
  const match = /^data:(image\/[a-zA-Z+]+);base64,(.+)$/.exec(dataUrl);
  if (!match) {
    return res.status(400).send('Expected a base64 image data URL in body.dataUrl');
  }
  const mime = match[1].toLowerCase();
  const ext = IMAGE_MIME_EXT[mime];
  if (!ext) {
    return res.status(400).send('Unsupported image type: ' + mime);
  }
  let buffer;
  try {
    buffer = Buffer.from(match[2], 'base64');
  } catch (e) {
    return res.status(400).send('Could not decode base64 image data: ' + e.message);
  }
  if (buffer.length === 0) {
    return res.status(400).send('Decoded image is empty');
  }

  const filename = buildChecklistImageFilename(date, symbolKey, ext, body.originalName);
  const filePath = path.join(CHECKLIST_UPLOADS_DIR, filename);
  try {
    fs.writeFileSync(filePath, buffer);
  } catch (e) {
    console.error('Could not write checklist image', filePath, e.message);
    return res.status(500).send('Could not save image: ' + e.message);
  }

  const compositeKey = checklistCompositeKey(date, symbolKey);
  const bodySymbol = body.symbol === null || body.symbol === undefined ? '' : String(body.symbol);
  const existing = checklistEntries[compositeKey] || { date, time: '', symbol: bodySymbol, items: {} };
  if (!Array.isArray(existing.images)) existing.images = [];
  // Drop the old single-image field from a pre-v7 entry, if present.
  if (existing.image) delete existing.image;
  existing.images.push({
    filename,
    url: `/checklist-uploads/${filename}`,
    name: (body.originalName ? String(body.originalName) : filename),
    uploadedAt: new Date().toISOString(),
  });
  checklistEntries[compositeKey] = existing;
  saveChecklist();
  res.json(existing);
});

app.delete('/checklist/:date/:symbol/image/:filename', (req, res) => {
  const date = req.params.date;
  const filename = req.params.filename;
  const symbolKey = parseChecklistSymbolParam(req.params.symbol);
  if (!CHECKLIST_DATE_RE.test(date) || !symbolKey) {
    return res.status(400).send('Invalid date or symbol');
  }
  if (!CHECKLIST_IMAGE_FILENAME_RE.test(filename)) {
    return res.status(400).send('Invalid image filename');
  }
  const filePath = path.join(CHECKLIST_UPLOADS_DIR, filename);
  try {
    if (fs.existsSync(filePath)) fs.unlinkSync(filePath);
  } catch (e) {
    console.error('Could not remove checklist image', filePath, e.message);
  }
  const compositeKey = checklistCompositeKey(date, symbolKey);
  const existing = checklistEntries[compositeKey];
  if (existing && Array.isArray(existing.images)) {
    existing.images = existing.images.filter((img) => img.filename !== filename);
    saveChecklist();
  }
  res.json(existing || { date, symbol: '', time: '', items: {}, images: [] });
});

// ============================================================================
// Autopsy routes — a list, not date-keyed: you can log more than one
// impulsive trade in the same session.
// GET    /autopsy       -> array of all entries
// POST   /autopsy       -> create a new entry (server assigns the id), echoes it back
// PUT    /autopsy/:id   -> update an existing entry by id, echoes it back
// DELETE /autopsy/:id   -> remove one entry
// ============================================================================
function cleanAutopsyBody(body) {
  const oneOf = (v, allowed) => (allowed.includes(v) ? v : null);
  return {
    dateSession: body.dateSession || '',
    symbol: body.symbol || '',
    instrument: body.instrument || '',
    direction: body.direction || '',
    size: body.size || '',
    inPlan: oneOf(body.inPlan, ['Yes', 'No', 'Partially']),
    trigger: body.trigger || '',
    story: body.story || '',
    warningSignals: body.warningSignals || '',
    outcome: oneOf(body.outcome, ['Winner', 'Loser', 'Scratch']),
    pnl: body.pnl || '',
    reinforced: oneOf(body.reinforced, ['Yes', 'No']),
    differently: body.differently || '',
    score: body.score || '',
    reason: body.reason || '',
  };
}

app.get('/autopsy', (req, res) => {
  res.json(Object.values(autopsyEntries));
});

app.post('/autopsy', (req, res) => {
  let body;
  try {
    body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
  } catch (e) {
    return res.status(400).send('Body is not valid JSON: ' + e.message);
  }
  const id = Date.now() + '-' + Math.random().toString(36).slice(2, 8);
  const entry = { id, ...cleanAutopsyBody(body) };
  autopsyEntries[id] = entry;
  saveAutopsy();
  res.json(entry);
});

app.put('/autopsy/:id', (req, res) => {
  let body;
  try {
    body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
  } catch (e) {
    return res.status(400).send('Body is not valid JSON: ' + e.message);
  }
  const id = req.params.id;
  const entry = { id, ...cleanAutopsyBody(body) };
  autopsyEntries[id] = entry;
  saveAutopsy();
  res.json(entry);
});

app.delete('/autopsy/:id', (req, res) => {
  delete autopsyEntries[req.params.id];
  saveAutopsy();
  res.status(200).send('Deleted');
});

// ============================================================================
// GET /health — diagnostic endpoint added to track down a reported "journal
// entry saves fine, then disappears later" bug. Since journal/rules/
// checklist/autopsy/alerts are all kept in memory and only MIRRORED to disk
// (see saveJournal() etc. above), an entry can look completely fine for the
// rest of the current process's life even if its write to disk silently
// failed — the only way that becomes visible is a restart, at which point
// whatever never made it to disk is gone. This endpoint surfaces exactly the
// facts needed to tell the difference between "the process restarted
// recently" (redeploy / spin-down / crash) and "writes are failing" (bad
// DATA_DIR permissions, disk full, wrong mount path) without needing to dig
// through server logs. Hit GET /health any time; nothing here is sensitive
// (no entry contents, just file metadata and counts).
// ============================================================================
function fileStatus(file) {
  try {
    const st = fs.statSync(file);
    return { exists: true, sizeBytes: st.size, modifiedAt: st.mtime.toISOString() };
  } catch (e) {
    return { exists: false };
  }
}
app.get('/health', (req, res) => {
  // Live round-trip write test — separate from the real data files, so this
  // never risks corrupting anything, but proves whether DATA_DIR is
  // *actually* writable from this exact process right now (a stale/incorrect
  // permission or mount can pass at container boot and fail later, or vice
  // versa on a fresh mount that hasn't caught up yet).
  const probeFile = path.join(DATA_DIR, '.health-write-test');
  let dataDirWritable = false;
  let dataDirWriteError = null;
  try {
    fs.writeFileSync(probeFile, String(Date.now()));
    fs.unlinkSync(probeFile);
    dataDirWritable = true;
  } catch (e) {
    dataDirWriteError = e.message;
  }
  const mem = process.memoryUsage(); // v8: watch this once the alert store grows toward 100000
  const archDays = listAlertArchiveDays();
  res.json({
    serverVersion: 10,
    duplicates: { windowSec: DUP_WINDOW_MS / 1000, ignoredSinceStart: duplicatesIgnored, lastDedupe },
    serverStartedAt: SERVER_STARTED_AT,
    uptimeSeconds: Math.round(process.uptime()),
    pid: process.pid,
    dataDir: DATA_DIR,
    dataDirSource: process.env.DATA_DIR ? 'DATA_DIR env var' : 'default (__dirname — NOT persistent across redeploys unless this IS a mounted Disk path)',
    dataDirWritable,
    dataDirWriteError,
    maxAlerts: MAX_ALERTS,
    memAlertDays: MEM_ALERT_DAYS,
    barKeepDays: BAR_KEEP_DAYS,
    oldestAlertAt: alerts.length ? alerts[alerts.length - 1].receivedAt : null,
    archive: { alertDays: archDays.length, firstAlertDay: archDays[0] || null, lastAlertDay: archDays[archDays.length - 1] || null, lastArchiveRun },
    memoryMB: { rss: Math.round(mem.rss / 1048576), heapUsed: Math.round(mem.heapUsed / 1048576) },
    files: {
      'journal.json': Object.assign({ inMemoryEntryCount: Object.keys(journalEntries).length }, fileStatus(JOURNAL_FILE)),
      'rules.json': Object.assign({ inMemoryEntryCount: Object.keys(rulesEntries).length }, fileStatus(RULES_FILE)),
      'checklist.json': Object.assign({ inMemoryEntryCount: Object.keys(checklistEntries).length }, fileStatus(CHECKLIST_FILE)),
      'autopsy.json': Object.assign({ inMemoryEntryCount: Object.keys(autopsyEntries).length }, fileStatus(AUTOPSY_FILE)),
      'alerts.json': Object.assign({ inMemoryEntryCount: alerts.length }, fileStatus(DATA_FILE)),
    },
    bars: Object.keys(bars).map((s) => Object.assign({ sym: s, inMemoryCount: bars[s].length, archivedMonths: listBarArchiveMonths(s).length }, fileStatus(barFile(s)))),
  });
});

app.listen(PORT, () => {
  console.log(`TradingView webhook dashboard v10 running on port ${PORT}`);
  console.log(`Webhook URL path: /webhook${SECRET ? '?token=' + SECRET : ''}`);
  console.log(`DATA_DIR: ${DATA_DIR} (${process.env.DATA_DIR ? 'from DATA_DIR env var' : 'default __dirname — set DATA_DIR to a mounted Disk to persist across redeploys'})`);
});
