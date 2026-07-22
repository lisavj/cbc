// TradingView Webhook Dashboard
// -----------------------------
// - POST /webhook?token=YOUR_SECRET   <- point your TradingView alert's webhook URL here
// - GET  /                            <- live dashboard (auto-updates as alerts arrive)
// - GET  /alerts                      <- raw JSON of stored alerts
//
// Alerts are kept in memory (fast, instant dashboard updates) and mirrored to alerts.json
// on disk so they survive a restart/redeploy. Only the most recent MAX_ALERTS are kept.

const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const SECRET = process.env.WEBHOOK_SECRET || ''; // set this in your host's env vars
const DISCORD_WEBHOOK_URL = process.env.DISCORD_WEBHOOK_URL || ''; // optional: paste a Discord channel webhook URL here to forward alerts
const MAX_ALERTS = 500;
const DATA_FILE = path.join(__dirname, 'alerts.json');

// TradingView sends the alert body as plain text by default (whatever you typed in the
// alert message box). It can also be JSON if you formatted it that way. Accept both.
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
      name: line.slice(0, idx).slice(0, 256) || '\u200b',
      value: line.slice(idx + 2).slice(0, 1024) || '\u200b',
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

app.listen(PORT, () => {
  console.log(`TradingView webhook dashboard running on port ${PORT}`);
  console.log(`Webhook URL path: /webhook${SECRET ? '?token=' + SECRET : ''}`);
});
