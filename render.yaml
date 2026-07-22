services:
  - type: web
    name: tv-webhook-dashboard
    env: node
    plan: free
    buildCommand: npm install
    startCommand: npm start
    envVars:
      - key: WEBHOOK_SECRET
        generateValue: true
