# Replacing placeholder temple information

This site was built with sample/placeholder content wherever real
information wasn't yet available. Search for the text `[ADD` across the
project to find every spot that needs a real value — or use the checklist
below.

## 1. Core details — `config/temple.json`
This file is the single source of truth. Fill in:
- `address`, `village`, `taluk`, `district`, `pincode`
- `phone`, `email`
- `upiId` (see donations section below)
- `googleMapsEmbedUrl`, `googleMapsDirectionsUrl`
- `socialMedia` links

## 2. Repeat the same details in the HTML pages
Because this first version is plain HTML (no backend yet — see
`docs/deployment.md` for the upgrade path), the same address/phone/email
also appear directly inside:
- `index.html` (footer + contact preview section)
- `contact.html`
- `location.html`
- every page's footer (`footer-address`, `footer-phone`, `footer-email`)

Use **Find & Replace** in your code editor for `[ADD TEMPLE ADDRESS]`,
`[ADD PHONE NUMBER]`, `[ADD EMAIL]` across all `.html` files at once.

## 3. Temple history — `history.html`
Replace each `[Add details...]` paragraph with verified history. If a
date or event isn't confirmed, leave the placeholder text rather than
guessing — the site is written so unverified sections are always
clearly marked with a "Sample content" tag.

## 4. Goddess / deity content — `deity.html`
Have the temple priests or trustees review and approve this page's
wording before publishing, since it describes religious practice.

## 5. Pooja timings — `pooja.html`, and the homepage's "Today's Pooja
   Timings" panel in `index.html`
Update the times in both places.

## 6. Festivals — `festivals.html`
Each `festival_card` block has a name, Tamil name, date and time.
Replace `[ADD FESTIVAL DATE]` / `[ADD TIME]` with confirmed dates.

## 7. UPI ID and QR code — donations
1. `config/temple.json` → `"upiId"`
2. `donations.html` → the `data-upi-id="..."` attribute on the **Donate
   Now** button
3. Add the QR image at `payment/upi-qr.png` (see `payment/README.md`)

## 8. Social media links
Only add links to accounts the temple actually manages. Replace
`href="#"` in the footer's social icons in every page.

## Full checklist
1. Temple address
2. Village
3. Taluk
4. District
5. Pincode
6. Phone
7. Email
8. Google Maps link
9. Official UPI ID
10. UPI QR image
11. Temple photos
12. Festival dates
13. Pooja timings
14. Temple history
15. Official social media links
