# சின்ன தென்னல் திரௌபதி அம்மன் கோவில் — Chinna Thennal Throbathi Amman Kovil

A bilingual (Tamil + English) digital home for the village temple:
temple information, daily pooja timings, festivals, announcements, a
gallery, UPI/GPay/PhonePe donations, volunteer sign-up and contact
details — designed to be maintained by the temple community, not just
developers.

## 1. What's in this first version
This version is a **static site** — plain HTML, CSS and JavaScript,
with no build tools, servers or database required. It works by
opening `index.html` in any browser, and can be hosted for free (see
`docs/deployment.md`). See that file for why, and for the upgrade path
to a full React + Node + MongoDB platform with an admin login later.

## 2. Features
- Full bilingual UI (English / தமிழ்) via a language switch in the header
- Home, About, History, Goddess, Pooja & Seva, Festivals, Announcements,
  Gallery, Donations, Volunteers, Contact, Location pages
- Temple-inspired design system (maroon/gold/cream palette, gopuram-tier
  dividers, kolam dot texture) driven by CSS variables
- UPI payment-link generator for Google Pay / PhonePe / any UPI app —
  builds a `upi://pay?...` link from the temple's UPI ID and chosen
  amount; the site never asks for or stores banking details
- Mobile-first responsive layout with a hamburger menu and sticky
  "Donate" button on small screens
- Organized image folders per gallery category, with instructions
- SEO basics: page titles, meta descriptions, Open Graph tags,
  `robots.txt`, `sitemap.xml`
- Every unverified fact (address, phone, history, timings, festival
  dates) is a clearly marked placeholder — see `docs/temple-information.md`

## 3. Technologies used
Plain **HTML5, CSS3, vanilla JavaScript**. No framework, no npm
install required to run the site. A small Python script
(`build.py`) was used once to generate the HTML pages from shared
header/footer templates — you don't need Python to use or edit the
site day-to-day, only if you want to change the shared header/footer
and regenerate all 12 pages at once.

## 4. Running the site
No installation needed.
1. Download or clone this project.
2. Double-click `index.html` — it opens in your default browser.

To serve it locally (recommended for accurate testing of things like
relative links):
```bash
cd chinna-thennal-throbathi-amman
python3 -m http.server 8000
# then open http://localhost:8000
```

## 5. Project structure
```
chinna-thennal-throbathi-amman/
├── index.html, about.html, history.html, deity.html, pooja.html,
│   festivals.html, announcements.html, gallery.html, donations.html,
│   volunteers.html, contact.html, location.html
├── assets/
│   ├── css/style.css        — design system (colors, type, components)
│   ├── js/locales.js        — all English + Tamil text
│   ├── js/main.js           — language switch, UPI link, forms, gallery filter
│   └── images/<category>/   — photo folders, one per gallery category
├── config/
│   └── temple.json          — single source of truth for temple details
├── payment/
│   ├── upi-qr.png           — add the real QR code here
│   └── README.md
├── docs/
│   ├── temple-information.md — what to replace, and where
│   ├── image-guide.md        — how to add/replace photos
│   └── deployment.md         — hosting + future backend upgrade
├── build.py                  — regenerates the HTML pages (optional)
├── robots.txt, sitemap.xml
├── .gitignore, .env.example, LICENSE
└── README.md
```

## 6. Editing temple information
Almost everything you need to change lives in **`config/temple.json`**
plus a few repeated spots in the HTML (address/phone/email appear in
each page's footer, and again on the Contact/Location pages). Full
instructions: `docs/temple-information.md`.

## 7. Adding Tamil / English content
All UI text lives in one file: `assets/js/locales.js`, split into an
`en` object and a `ta` object with matching keys (e.g.
`"about.introBody"`). To change any text on the site:
1. Open `assets/js/locales.js`.
2. Find the key (search for the English text you see on the page).
3. Edit the value in **both** `en` and `ta` sections so the two
   languages stay in sync.

## 8. Adding temple/festival/gallery photos
See `docs/image-guide.md`.

## 9. Updating pooja timings and festivals
- Daily timings: `pooja.html` and the "Today's Pooja Timings" panel in
  `index.html`.
- Festivals: `festivals.html` — copy an existing festival card block
  and edit the name, date and description.

## 10. Updating the UPI ID and QR code
See `payment/README.md` and `docs/temple-information.md` §7.

## 11. Google Maps configuration
Open `location.html` and `index.html`, and replace the
`[ADD GOOGLE MAPS URL]` placeholder link with the temple's real Google
Maps share link. Once you have a Google Maps **embed** URL, you can
also swap the placeholder `.map-frame` div for an `<iframe>`.

## 12. Admin setup
This first version has no login-protected admin panel — content is
edited directly in the files above by anyone the temple trusts with
the project. `docs/deployment.md` §Phase 2 describes how to add a real
admin dashboard (Node/Express + MongoDB + secure login) when the
temple is ready for that step.

## 13. Deployment
See `docs/deployment.md` for free hosting on GitHub Pages, Netlify or
Vercel, plus custom domain setup.

## 14. Uploading to GitHub
```bash
cd chinna-thennal-throbathi-amman
git init
git add .
git commit -m "Initial temple website"
git branch -M main
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
```
`.gitignore` already excludes `.env`, `node_modules/` and similar files
so secrets are never committed.

## 15. Security notes
- Never enter or ask devotees for UPI PIN, ATM PIN, OTP, CVV or
  net-banking passwords — this site never does, and never should.
- Never commit `.env`, admin passwords, or payment gateway secret keys.
- The UPI donation flow only ever opens the devotee's own UPI app; this
  site does not process or store payments itself.

## 16. Future features (not built yet, architecture allows for them)
Online pooja booking, festival registration, donation history and
digital receipts, SMS/WhatsApp/email/push notifications, a live temple
calendar, devotee accounts, admin roles, priest and inventory
management, and donation/annual reports — see `docs/deployment.md`
Phase 2 for how the backend would support these.

---
*Made with devotion for the temple community.*
