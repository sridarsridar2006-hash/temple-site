# Deployment

## Why this version is a static site
The full brief describes a React + Node/Express + MongoDB platform with
an admin dashboard. That's the right architecture for a temple that
wants staff to edit content through a login screen — but it needs a
server, a database and ongoing hosting costs, which is a lot to take on
before the temple even has its first real content ready.

This first version is deliberately a **plain HTML/CSS/JS site** — no
build step, no server, no database. It can be opened by double-clicking
`index.html`, hosted for free on GitHub Pages/Netlify/Vercel, and
edited by anyone comfortable with basic HTML — the temple's own content
(`config/temple.json`, and the text inside each `.html` file) is easy
to update by hand. When the temple is ready for an admin login screen,
Section 2 below describes the upgrade path.

## Phase 1 — deploy the static site (recommended first step)

### Option A: GitHub Pages (free)
1. Create a GitHub repository and push this project (see `README.md`
   for git commands).
2. In the repo, go to **Settings → Pages**.
3. Under "Build and deployment", choose **Deploy from a branch**,
   branch `main`, folder `/ (root)`.
4. Your site will be live at `https://your-username.github.io/repo-name/`.

### Option B: Netlify (free)
1. Go to netlify.com and sign in with GitHub.
2. "Add new site" → "Import an existing project" → pick this repo.
3. Leave the build command empty and publish directory as `/`.
4. Deploy — Netlify gives you a free `.netlify.app` URL, and you can
   later attach a custom domain.

### Option C: Vercel (free)
1. Go to vercel.com and sign in with GitHub.
2. "Add New Project" → pick this repo.
3. Framework preset: "Other" (no build step needed).
4. Deploy.

### Custom domain
All three options let you attach a real domain (e.g.
`chinnathennaltemple.org`) for free once you own the domain name from a
registrar.

## Phase 2 — optional future backend (admin panel, bookings, database)
When the temple wants staff to log in and edit content, festival
bookings, or donation records without touching code, build:

- **Backend:** Node.js + Express, following the `backend/` folder
  layout suggested in the original project brief (`controllers/`,
  `models/`, `routes/`, `middleware/`, `config/`, `server.js`).
- **Database:** MongoDB Atlas (free tier is enough to start).
- **Frontend:** the current site's content can be migrated into a
  React + Vite app that fetches from the new API instead of using
  static HTML, or the API can simply feed JSON back into
  `config/temple.json`-style files that this static site reads.
- **Auth:** secure, hashed-password or OAuth admin login — never store
  plaintext admin passwords, and never commit `.env` secrets.

This is intentionally not built in the first version, per the rule of
not adding complex features before they're needed — but the folder
names above are reserved so the project can grow into this shape later
without a rewrite.
