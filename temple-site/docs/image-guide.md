# Image guide

## Folder structure
```
assets/images/
  temple/       — temple building, gopuram, sanctum
  goddess/      — the deity (use respectful, priest-approved photos)
  festivals/    — festival celebrations
  pooja/        — daily/special pooja moments
  events/       — community events
  village/      — the village and surroundings
  renovation/   — before/after renovation photos
  devotees/     — devotees at the temple (get consent before publishing)
```

## Adding a temple photo
1. Compress the photo (aim for under ~300KB; WebP or JPG both work).
2. Copy it into `assets/images/temple/your-photo.webp`.
3. Open `index.html`, find the **hero section** at the top of `<body>`,
   and add an `<img>` tag, e.g.:
   ```html
   <img src="assets/images/temple/your-photo.webp" alt="Temple gopuram">
   ```

## Replacing the Goddess image
Open `deity.html` and replace the placeholder tile:
```html
<div class="gallery-tile" style="aspect-ratio:1/1;">
  <span class="icon" style="font-size:3rem;">🌸</span>
  ...
</div>
```
with:
```html
<img src="assets/images/goddess/amman.webp" alt="Throbathi Amman">
```

## Adding festival photos
Add files under `assets/images/festivals/`, then link them from the
matching festival's section in `festivals.html`.

## Adding gallery photos
Open `gallery.html`. Each tile currently looks like:
```html
<div class="gallery-tile" data-cat="temple">
  <span class="icon">🛕</span><span class="cat" data-i18n="gallery.catTemple"></span>
</div>
```
Keep the `data-cat="..."` attribute (it drives the category filter) but
replace the icon/span content with an `<img>` tag pointing at your photo.

## Rules
- Do not use copyrighted images found online without permission.
- Get consent before publishing recognizable photos of devotees,
  especially children.
- Prefer WebP for smaller file sizes and faster page loads.
