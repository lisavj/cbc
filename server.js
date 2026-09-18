// TradingView Webhook Dashboard
// -----------------------------
// - POST /webhook?token=YOUR_SECRET   <- point your TradingView alert's webhook URL here
// - GET  /                            <- live dashboard (auto-updates as alerts arrive)
// - GET  /alerts                      <- raw JSON of stored alerts
//
// Alerts are kept in memory (fast, instant dashboard updates) and mirrored to alerts.json
// on disk so they survive a restart/redeploy. Only the most recent MAX_ALERTS are kept.
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

const app = express();
const PORT = process.env.PORT || 3000;
const SECRET = process.env.WEBHOOK_SECRET || ''; // set this in your host's env vars
const DISCORD_WEBHOOK_URL = process.env.DISCORD_WEBHOOK_URL || ''; // optional: paste a Discord channel webhook URL here to forward alerts
const MAX_ALERTS = 500;
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

function saveJournal() {
  try {
    fs.writeFileSync(JOURNAL_FILE, JSON.stringify(journalEntries, null, 2));
  } catch (e) {
    console.error('Could not write journal.json:', e.message);
  }
}

function saveRules() {
  try {
    fs.writeFileSync(RULES_FILE, JSON.stringify(rulesEntries, null, 2));
  } catch (e) {
    console.error('Could not write rules.json:', e.message);
  }
}

function saveChecklist() {
  try {
    fs.writeFileSync(CHECKLIST_FILE, JSON.stringify(checklistEntries, null, 2));
  } catch (e) {
    console.error('Could not write checklist.json:', e.message);
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
  } catch (e) {
    console.error('Could not write autopsy.json:', e.message);
  }
}

// TradingView sends the alert body as plain text by default (whatever you typed in the
// alert message box). It can also be JSON if you formatted it that way. Accept both.
// NOTE: because this is registered for type '*/*', req.body is ALWAYS a raw string here —
// for ANY route, not just /webhook — so every route below that expects JSON must parse
// req.body itself (see /restore, /journal/:date, /rules/:date) rather than assuming
// Express already parsed it into an object.
app.use(express.text({ type: '*/*', limit: '1mb' }));

// ---- Load any alerts saved from a previous run ----
let alerts = [];
try {
  if (fs.existsSync(DATA_FILE)) {
    alerts = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
  }
} catch (e) {
  console.error('Could not read alerts.json, starting fresh:', e.message);
}

function saveAlerts() {
  try {
    fs.writeFileSync(DATA_FILE, JSON.stringify(alerts.slice(0, MAX_ALERTS), null, 2));
  } catch (e) {
    console.error('Could not write alerts.json:', e.message);
  }
}

// ---- Live-update clients (Server-Sent Events) ----
let sseClients = [];

function broadcast(alert) {
  const payload = `data: ${JSON.stringify(alert)}\n\n`;
  sseClients.forEach((res) => res.write(payload));
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

  const alert = {
    id: Date.now() + '-' + Math.random().toString(36).slice(2, 8),
    receivedAt: new Date().toISOString(),
    raw: typeof body === 'string' ? body : JSON.stringify(body),
    json: parsed,
  };

  alerts.unshift(alert);
  if (alerts.length > MAX_ALERTS) alerts = alerts.slice(0, MAX_ALERTS);
  saveAlerts();
  broadcast(alert);
  sendToDiscord(alert.raw);

  console.log(`[${alert.receivedAt}] alert received (${alert.raw.length} chars)`);
  res.status(200).send('OK');
});

// ---- JSON list of stored alerts (used by the dashboard on load) ----
app.get('/alerts', (req, res) => {
  res.json(alerts);
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

// ---- Clear all stored alerts ----
app.post('/clear', (req, res) => {
  if (SECRET && req.query.token !== SECRET) {
    return res.status(401).send('Unauthorized');
  }
  alerts = [];
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
  alerts = parsed.slice(0, MAX_ALERTS);
  saveAlerts();
  res.status(200).send(`Restored ${alerts.length} alert(s).`);
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
  saveJournal();
  res.json(entry);
});

app.delete('/journal/:date', (req, res) => {
  delete journalEntries[req.params.date];
  saveJournal();
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
// Checklist routes — same date-keyed upsert pattern as /rules.
// GET    /checklist        -> array of all entries
// PUT    /checklist/:date   -> upsert one day, body is { date, items: { <id>: {<field>: bool|string, ...} } }
// DELETE /checklist/:date   -> remove one day (used by the "Clear day" button)
//
// v4: items are no longer a fixed {checked, note} shape -- the frontend now has
// 5 different item field layouts (plain checkbox; a 5-box entry/stop/target/
// size/risk row; a risk-limit + stop-structure-type combo; a direction
// pulldown + confluence checkboxes; a plain checkbox group), each with its
// own field keys. Rather than whitelist every field name here (which would
// need updating every time the checklist's fields change), each item is
// passed through as-is except every field VALUE is coerced to either a bool
// or a string -- so a checkbox always saves as true/false and a text/select
// field always saves as a string, regardless of what field keys exist this
// round, while still rejecting anything that isn't plain JSON data (no
// functions, no nested objects/arrays sneaking into the saved file).
// ============================================================================
app.get('/checklist', (req, res) => {
  res.json(Object.values(checklistEntries));
});

app.put('/checklist/:date', (req, res) => {
  let body;
  try {
    body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
  } catch (e) {
    return res.status(400).send('Body is not valid JSON: ' + e.message);
  }
  const date = req.params.date;
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
  const entry = { date, items: cleanItems };
  checklistEntries[date] = entry;
  saveChecklist();
  res.json(entry);
});

app.delete('/checklist/:date', (req, res) => {
  delete checklistEntries[req.params.date];
  saveChecklist();
  res.status(200).send('Deleted');
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

app.listen(PORT, () => {
  console.log(`TradingView webhook dashboard running on port ${PORT}`);
  console.log(`Webhook URL path: /webhook${SECRET ? '?token=' + SECRET : ''}`);
});
