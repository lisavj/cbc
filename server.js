// ============================================================================
// Journal + Rules persistence — same pattern as alerts.json (in-memory copy,
// mirrored to disk under DATA_DIR so a Render Disk keeps it across deploys).
// Add this block near your existing DATA_FILE / alerts setup.
// ============================================================================

const JOURNAL_FILE = path.join(DATA_DIR, 'journal.json');
const RULES_FILE = path.join(DATA_DIR, 'rules.json');

// Both are stored as { "<date>": <entry> } objects on disk — easiest to
// upsert-by-date and to write straight back out with JSON.stringify.
let journalEntries = {};
let rulesEntries = {};

function loadKeyedStore(file) {
  try {
    const raw = fs.readFileSync(file, 'utf8');
    const parsed = JSON.parse(raw);
    return (parsed && typeof parsed === 'object') ? parsed : {};
  } catch (e) {
    // Missing file on first run is normal — anything else is worth knowing about.
    if (e.code !== 'ENOENT') console.error('Could not read', file, e.message);
    return {};
  }
}

function saveKeyedStore(file, store) {
  try {
    fs.writeFileSync(file, JSON.stringify(store, null, 2));
  } catch (e) {
    console.error('Could not write', file, e.message);
  }
}

journalEntries = loadKeyedStore(JOURNAL_FILE);
rulesEntries = loadKeyedStore(RULES_FILE);

// ---- Journal ----
// GET  /journal          -> array of all entries (frontend keys them by .date itself)
// PUT  /journal/:date     -> upsert one day, body is the full entry, echoes it back
// DELETE /journal/:date   -> remove one day

app.get('/journal', (req, res) => {
  res.json(Object.values(journalEntries));
});

app.put('/journal/:date', (req, res) => {
  const date = req.params.date;
  const body = req.body || {};
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
  saveKeyedStore(JOURNAL_FILE, journalEntries);
  res.json(entry);
});

app.delete('/journal/:date', (req, res) => {
  delete journalEntries[req.params.date];
  saveKeyedStore(JOURNAL_FILE, journalEntries);
  res.status(200).send('Deleted');
});

// ---- Rules ----
// GET  /rules           -> array of all entries
// PUT  /rules/:date      -> upsert one day, body is { date, items: { <id>: {answer, note} } }

app.get('/rules', (req, res) => {
  res.json(Object.values(rulesEntries));
});

app.put('/rules/:date', (req, res) => {
  const date = req.params.date;
  const body = req.body || {};
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
  saveKeyedStore(RULES_FILE, rulesEntries);
  res.json(entry);
});

// Optional — not currently used by the frontend (there's no delete button in
// the Rules tab), but here in case you want one later, matching /journal's shape.
app.delete('/rules/:date', (req, res) => {
  delete rulesEntries[req.params.date];
  saveKeyedStore(RULES_FILE, rulesEntries);
  res.status(200).send('Deleted');
});
