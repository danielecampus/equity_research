# Greeks Dashboard — Vite app

Optional Vite setup for the GREEKS.jsx dashboard. Use this for a proper dev experience (HMR, fast build).
Not required to view the dashboard — `Market_Risk/index.html` is a self-contained version using CDN scripts.

## Prerequisites

Install Node.js LTS (>= 18):

```powershell
winget install OpenJS.NodeJS.LTS
```

Then reopen the terminal so `node` and `npm` are on PATH.

## Run locally

```powershell
cd Market_Risk/vite-app
npm install
npm run dev
```

Open the URL Vite prints (usually http://localhost:5173).

## Build & preview production output

```powershell
npm run build
npm run preview
```

## How it wires GREEKS.jsx

`src/App.jsx` re-exports the default export of `../../GREEKS.jsx`, so the source of truth stays in `Market_Risk/GREEKS.jsx`. `vite.config.js` allows reading from the parent folder via `server.fs.allow`.

## Deploy

The repo-root workflow at `.github/workflows/deploy-pages.yml` deploys the **standalone** `Market_Risk/index.html` to GitHub Pages. If you want to deploy the Vite build instead, change the workflow's `upload-pages-artifact` path to `Market_Risk/vite-app/dist` and add an `npm ci && npm run build` step.
