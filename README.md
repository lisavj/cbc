# TradingView Webhook Dashboard

Receives your MapleStax alert webhooks, shows them live in a browser page, and (optionally)
forwards each one to a Discord channel as a formatted embed. No email inbox required.

## What's in this folder

- `server.js` — the whole app (Express server: webhook endpoint + live dashboard + Discord forwarding)
- `public/index.html` — the dashboard page you'll look at
- `package.json` — tells the host what to install and how to start it
- `render.yaml` — lets Render set itself up automatically (only needed for the Render path)

You don't need to edit any of these.

---

## Choose where to run it

| | Render (cloud) | Your Windows PC |
|---|---|---|
| Needs your computer on 24/7 | No | **Yes** |
| Setup effort | One-time, ~10 min | One-time, ~10 min, but ngrok's free URL changes every restart |
| Best for | "Set it and forget it" | Trying it out, or if you're always at that PC anyway |

Pick one path below.

---

## Path A — Render (cloud, recommended)

### 1. Put the files on GitHub (no command line needed)
1. Go to [github.com](https://github.com) and sign in (or create a free account).
2. Click the **+** in the top right → **New repository**. Name it anything, click **Create repository**.
3. On the new repo's page, click **uploading an existing file**.
4. Drag in every file from this folder (`server.js`, `package.json`, `render.yaml`, `.gitignore`, and the `public` folder with `index.html` inside it), then **Commit changes**.

### 2. Deploy it on Render (free tier)
1. Go to [render.com](https://render.com) and sign in with your GitHub account.
2. **New +** → **Blueprint** → pick your repo. Render reads `render.yaml` and sets everything up automatically, including a random `WEBHOOK_SECRET`.
3. Click **Apply** and wait a minute or two.
4. Render gives you a URL like `https://tv-webhook-dashboard-xxxx.onrender.com` — that's your app.

*(If "Blueprint" isn't available: **New +** → **Web Service** instead, Build Command `npm install`, Start Command `npm start`, then add an Environment variable `WEBHOOK_SECRET` set to any password-like string yourself.)*

### 3. Point TradingView at it
In TradingView, open your MapleStax alert → **Notifications** tab → check **Webhook URL** → paste:
```
https://YOUR-APP-NAME.onrender.com/webhook?token=YOUR_SECRET
```
Leave the alert **Message** box as the script already fills it in. Save.

### 4. Watch it live
Open `https://YOUR-APP-NAME.onrender.com/` in any browser and leave the tab open.

**Caveat:** Render's free plan sleeps after 15 minutes idle, then takes ~30-60 seconds to wake on the next alert. A paid instance (a few $/month) removes this — no code change needed, just the plan.

---

## Path B — Your Windows PC

### 1. Install Node.js
Download and install from [nodejs.org](https://nodejs.org) (the "LTS" version). Just click through the installer with defaults.

### 2. Get the app onto your PC
Copy this whole folder onto your PC anywhere convenient (e.g. `C:\tv-webhook-dashboard`).

### 3. Install and run it
Open **Command Prompt** (search "cmd" in the Start menu), then:
```
cd C:\tv-webhook-dashboard
npm install
node server.js
```
You should see `TradingView webhook dashboard running on port 3000`. Leave this window open — closing it stops the app.

### 4. Make it reachable from the internet (ngrok)
TradingView's servers need a public URL to send to — your PC doesn't have one by default. [ngrok](https://ngrok.com) creates one for you without touching your router.
1. Sign up free at [ngrok.com](https://ngrok.com), download it, and follow their one-line setup command (adds your auth token).
2. In a **second** Command Prompt window (leave the first one running the server):
   ```
   ngrok http 3000
   ```
3. ngrok prints a URL like `https://a1b2-c3d4.ngrok-free.app` — that's your public address. **This URL changes every time you restart ngrok** on the free plan, so you'll need to update the TradingView webhook URL each time you restart it.

### 5. Point TradingView at it
Same as Path A step 3, but using your ngrok URL:
```
https://a1b2-c3d4.ngrok-free.app/webhook?token=YOUR_SECRET
```
Set `WEBHOOK_SECRET` before starting the server if you want a token — on Windows:
```
set WEBHOOK_SECRET=mySecret2026xyz
node server.js
```

### 6. Watch it live
Open `http://localhost:3000/` in your browser on the same PC (or your ngrok URL from any device).

**Caveat:** if your PC sleeps, restarts, loses power, or you close the two Command Prompt windows, alerts stop arriving until you start both again.

---

## Optional: forward alerts to Discord

1. In Discord, go to your server → the channel you want alerts in → the gear icon (Edit Channel) → **Integrations** → **Webhooks** → **New Webhook**. Copy its **Webhook URL**.
2. Set it as an environment variable named `DISCORD_WEBHOOK_URL`:
   - **Render:** service → **Environment** tab → add `DISCORD_WEBHOOK_URL` = (paste the URL).
   - **Windows:** in Command Prompt, before starting the server: `set DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...` then `node server.js`.
3. That's it — every alert now also posts to that Discord channel as a color-coded embed (green-tinted for LONG/Bullish-heavy alerts, red for SHORT/Bearish-heavy), with each `Key: Value` line from the alert shown as its own field. Leave `DISCORD_WEBHOOK_URL` unset if you don't want this — nothing else changes.

---

## Good to know

- **The token isn't a real login system** — it's a shared secret in the URL to keep random strangers from spamming your `/webhook` endpoint. Keep your dashboard URL, secret, and Discord webhook URL private.
- **History:** the last 500 alerts are kept in `alerts.json` next to the server, so they survive a restart. Older ones roll off.
- **Multiple people can view the dashboard:** anyone with the URL can watch — no login to *view*, only the webhook itself is token-protected.
- **Want Slack instead of/as well as Discord, or longer-term storage?** Both would go in the same spot in `server.js` (right where `sendToDiscord(...)` is called) — happy to add either.

