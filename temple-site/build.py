#!/usr/bin/env python3
"""
Build script — assembles every page of the temple website from a shared
header/footer and per-page content blocks defined below.

This is a ONE-TIME generation script (not needed to run the site).
It exists so the header/footer stay identical across all pages.
Run again with `python3 build.py` only if you edit the template blocks
below and want to regenerate the static .html files.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [
    ("index.html", "nav.home"),
    ("about.html", "nav.about"),
    ("history.html", "nav.history"),
    ("deity.html", "nav.deity"),
    ("pooja.html", "nav.pooja"),
    ("festivals.html", "nav.festivals"),
    ("announcements.html", "nav.announcements"),
    ("gallery.html", "nav.gallery"),
    ("donations.html", "nav.donations"),
    ("volunteers.html", "nav.volunteers"),
    ("contact.html", "nav.contact"),
    ("location.html", "nav.location"),
]

TEMPLE_MARK_SVG = '''<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2 L14 8 L10 8 Z" fill="#7A1420"/>
  <rect x="7" y="9" width="10" height="9" fill="#7A1420"/>
  <path d="M5 18 H19 L21 22 H3 Z" fill="#7A1420"/>
  <circle cx="12" cy="5.4" r="1.1" fill="#7A1420"/>
</svg>'''

TIER_DIVIDER_SVG = '''<svg viewBox="0 0 220 26" xmlns="http://www.w3.org/2000/svg">
  <polygon points="0,26 20,6 40,26" fill="#C79A3B"/>
  <polygon points="40,26 60,10 80,26" fill="#E8B94D"/>
  <polygon points="80,26 110,2 140,26" fill="#7A1420"/>
  <polygon points="140,26 160,10 180,26" fill="#E8B94D"/>
  <polygon points="180,26 200,6 220,26" fill="#C79A3B"/>
</svg>'''

def nav_links(active):
    items = []
    for href, key in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ""
        items.append(f'<li><a href="{href}" data-i18n="{key}"{cur}></a></li>')
    return "\n        ".join(items)

def header(active, title_key="nav.home"):
    return f'''  <header class="site-header">
    <div class="site-header__bar">
      <a class="brand" href="index.html">
        <span class="brand__mark">{TEMPLE_MARK_SVG}</span>
        <span class="brand__text">
          <span class="ta">சின்ன தென்னல் திரௌபதி அம்மன் கோவில்</span>
          <span class="en">Chinna Thennal Throbathi Amman Kovil</span>
        </span>
      </a>
      <nav class="nav" aria-label="Main navigation">
        <ul class="nav__links">
        {nav_links(active)}
        </ul>
        <div class="lang-switch" role="group" aria-label="Language">
          <button type="button" data-lang="en">EN</button>
          <button type="button" data-lang="ta">தமிழ்</button>
        </div>
        <a class="btn btn--gold btn--sm" href="donations.html" data-i18n="nav.donateBtn"></a>
        <button class="hamburger" aria-label="Toggle menu" aria-expanded="false">
          <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
        </button>
      </nav>
    </div>
  </header>
  <a href="donations.html" class="btn btn--primary donate-fab" data-i18n="nav.donateBtn"></a>
'''

def footer():
    return f'''  <footer class="site-footer">
    <div class="container grid-4">
      <div>
        <h4 data-i18n="footer.quicklinks"></h4>
        <ul>
          <li><a href="about.html" data-i18n="nav.about"></a></li>
          <li><a href="festivals.html" data-i18n="nav.festivals"></a></li>
          <li><a href="gallery.html" data-i18n="nav.gallery"></a></li>
          <li><a href="volunteers.html" data-i18n="nav.volunteers"></a></li>
        </ul>
      </div>
      <div>
        <h4 data-i18n="footer.timingsTitle"></h4>
        <ul>
          <li>காலை பூஜை — 06:00 AM</li>
          <li>உச்சிகால பூஜை — 12:00 PM</li>
          <li>மாலை பூஜை — 06:00 PM</li>
          <li>இரவு பூஜை — 08:00 PM</li>
        </ul>
      </div>
      <div>
        <h4 data-i18n="footer.contactTitle"></h4>
        <ul>
          <li id="footer-address">119, Perumal Kovil Street, Chinna Thennal, Tamil Nadu 631051</li>
          <li id="footer-phone"><a href="tel:+919500418125" style="color:inherit;text-decoration:none;">+91 95004 18125</a></li>
          <li id="footer-email"><a href="mailto:sridarm2006@gmail.com" style="color:inherit;text-decoration:none;">sridarm2006@gmail.com</a></li>
        </ul>
      </div>
      <div>
        <h4 data-i18n="footer.donationTitle"></h4>
        <p data-i18n="footer.donationText" style="font-size:.88rem;"></p>
        <a href="donations.html" class="btn btn--gold btn--sm" data-i18n="nav.donateBtn"></a>
        <h4 style="margin-top:22px;" data-i18n="footer.socialTitle"></h4>
        <div class="social-row">
          <a href="#" aria-label="YouTube">YT</a>
          <a href="#" aria-label="Facebook">FB</a>
          <a href="#" aria-label="Instagram">IG</a>
          <a href="#" aria-label="WhatsApp">WA</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p data-i18n="footer.copyright" style="margin:0 0 4px;"></p>
      <p data-i18n="footer.madeWith" style="margin:0;"></p>
    </div>
  </footer>
'''

def page(filename, active, title_ta, title_en, description, content, extra_head=""):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_en} | Chinna Thennal Throbathi Amman Kovil</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title_en} | Chinna Thennal Throbathi Amman Kovil">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Inter:wght@400;500;600;700&family=Noto+Sans+Tamil:wght@400;500;600;700&family=Noto+Serif+Tamil:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{extra_head}
</head>
<body>
{header(active)}
{content}
{footer()}
  <script src="assets/js/locales.js"></script>
  <script src="assets/js/main.js"></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)

def page_hero(title_key, sub_key=None, active="", breadcrumb_key=None):
    sub = f'<p data-i18n="{sub_key}"></p>' if sub_key else ""
    return f'''  <section class="page-hero">
    <div class="container">
      <p class="breadcrumb"><a href="index.html" data-i18n="common.backHome"></a></p>
      <h1 data-i18n="{title_key}"></h1>
      {sub}
    </div>
  </section>
'''

# ==========================================================================
# HOME PAGE
# ==========================================================================
home_content = f'''  <section class="hero">
    <div class="kolam-bg"></div>
    <div class="container hero__inner">
      <div class="hero__mark">{TEMPLE_MARK_SVG.replace('#7A1420','#E8B94D')}</div>
      <p class="hero__title-ta">சின்ன தென்னல் திரௌபதி அம்மன் கோவில்</p>
      <p class="hero__title-en">Chinna Thennal Throbathi Amman Kovil</p>
      <p class="hero__tagline" data-i18n="home.introTitle"></p>
      <div class="hero__actions">
        <a class="btn btn--gold" href="about.html" data-i18n="home.heroCta1"></a>
        <a class="btn btn--outline" href="festivals.html" data-i18n="home.heroCta2"></a>
        <a class="btn btn--outline" href="donations.html" data-i18n="home.heroCta3"></a>
      </div>
    </div>
  </section>
  <div class="tier-divider">{TIER_DIVIDER_SVG}</div>

  <section class="section">
    <div class="container">
      <div class="section-heading">
        <span class="kicker" data-i18n="home.heroKicker"></span>
        <h2 data-i18n="home.introTitle"></h2>
        <p data-i18n="home.introText"></p>
      </div>
      <div class="qi-grid">
        <a class="qi-card" href="about.html"><span class="qi-card__icon">🛕</span><h3 data-i18n="home.qiTemple"></h3><p data-i18n="home.qiTempleDesc"></p></a>
        <a class="qi-card" href="pooja.html"><span class="qi-card__icon">🪔</span><h3 data-i18n="home.qiPooja"></h3><p data-i18n="home.qiPoojaDesc"></p></a>
        <a class="qi-card" href="festivals.html"><span class="qi-card__icon">📅</span><h3 data-i18n="home.qiFestivals"></h3><p data-i18n="home.qiFestivalsDesc"></p></a>
        <a class="qi-card" href="pooja.html#seva"><span class="qi-card__icon">🙏</span><h3 data-i18n="home.qiSpecial"></h3><p data-i18n="home.qiSpecialDesc"></p></a>
        <a class="qi-card" href="donations.html"><span class="qi-card__icon">💰</span><h3 data-i18n="home.qiDonations"></h3><p data-i18n="home.qiDonationsDesc"></p></a>
        <a class="qi-card" href="location.html"><span class="qi-card__icon">📍</span><h3 data-i18n="home.qiLocation"></h3><p data-i18n="home.qiLocationDesc"></p></a>
        <a class="qi-card" href="contact.html"><span class="qi-card__icon">📞</span><h3 data-i18n="home.qiContact"></h3><p data-i18n="home.qiContactDesc"></p></a>
      </div>
    </div>
  </section>

  <section class="section section--surface">
    <div class="container grid-2">
      <div class="panel panel--arch">
        <span class="tag tag--sample" data-i18n="home.sampleLabel"></span>
        <h2 data-i18n="home.todayPoojaTitle"></h2>
        <p data-i18n="home.todayPoojaSub" style="margin-bottom:18px;"></p>
        <table>
          <tbody>
            <tr><td>காலை பூஜை / Morning Pooja</td><td>06:00 AM</td></tr>
            <tr><td>உச்சிகால பூஜை / Uchikala Pooja</td><td>12:00 PM</td></tr>
            <tr><td>மாலை பூஜை / Evening Pooja</td><td>06:00 PM</td></tr>
            <tr><td>இரவு பூஜை / Night Pooja</td><td>08:00 PM</td></tr>
          </tbody>
        </table>
      </div>
      <div class="panel panel--arch">
        <span class="tag tag--sample" data-i18n="home.sampleLabel"></span>
        <h2 data-i18n="home.festivalTitle"></h2>
        <p><strong>Aadi Thiruvizha / ஆடி திருவிழா</strong><br>[ADD FESTIVAL DATE] · [ADD FESTIVAL TIME]</p>
        <p>[Add a short description of the upcoming festival once confirmed by the temple administration.]</p>
        <a class="btn btn--outline-dark btn--sm" href="festivals.html" data-i18n="home.festivalCta"></a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-heading">
        <h2 data-i18n="home.announceTitle"></h2>
      </div>
      <div style="max-width:760px;margin:0 auto;">
        <div class="announce-item is-high">
          <div class="announce-item__meta">01 September 2026</div>
          <strong>Kumbhabhishekam Planning Meeting / கும்பாபிஷேக ஆலோசனை கூட்டம்</strong>
          <p style="margin:6px 0 0;">[Sample announcement — replace with real temple news.]</p>
        </div>
        <div class="announce-item">
          <div class="announce-item__meta">28 August 2026</div>
          <strong>Weekly Abhishekam Schedule / வார அபிஷேக அட்டவணை</strong>
          <p style="margin:6px 0 0;">[Sample announcement — replace with real temple news.]</p>
        </div>
      </div>
      <div style="text-align:center;margin-top:24px;">
        <a class="btn btn--outline-dark btn--sm" href="announcements.html" data-i18n="home.announceCta"></a>
      </div>
    </div>
  </section>

  <section class="section section--surface">
    <div class="container grid-2">
      <div>
        <span class="tag tag--sample" data-i18n="home.sampleLabel"></span>
        <h2 data-i18n="home.aboutTitle"></h2>
        <p data-i18n="about.introBody"></p>
        <a class="btn btn--outline-dark btn--sm" href="about.html" data-i18n="home.aboutCta"></a>
      </div>
      <div>
        <span class="tag tag--sample" data-i18n="home.sampleLabel"></span>
        <h2 data-i18n="home.deityTitle"></h2>
        <p data-i18n="deity.introBody"></p>
        <a class="btn btn--outline-dark btn--sm" href="deity.html" data-i18n="home.deityCta"></a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-heading">
        <h2 data-i18n="home.galleryTitle"></h2>
      </div>
      <div class="gallery-grid">
        <div class="gallery-tile"><span class="icon">🛕</span><span class="cat">Temple</span></div>
        <div class="gallery-tile"><span class="icon">🌸</span><span class="cat">Goddess</span></div>
        <div class="gallery-tile"><span class="icon">🎉</span><span class="cat">Festival</span></div>
        <div class="gallery-tile"><span class="icon">🪔</span><span class="cat">Pooja</span></div>
      </div>
      <div style="text-align:center;margin-top:24px;">
        <a class="btn btn--outline-dark btn--sm" href="gallery.html" data-i18n="home.galleryCta"></a>
      </div>
    </div>
  </section>

  <section class="section section--surface">
    <div class="container" style="max-width:640px;text-align:center;">
      <h2 data-i18n="home.donateTitle"></h2>
      <p data-i18n="home.donateText"></p>
      <a class="btn btn--primary" href="donations.html" data-i18n="home.donateCta"></a>
    </div>
  </section>

  <section class="section">
    <div class="container grid-2">
      <div>
        <h2 data-i18n="home.locationTitle"></h2>
        <div class="map-frame"><span data-i18n="location.mapPending"></span></div>
        <div style="margin-top:14px;">
          <a class="btn btn--outline-dark btn--sm" href="location.html" data-i18n="home.locationCta"></a>
        </div>
      </div>
      <div>
        <h2 data-i18n="home.contactTitle"></h2>
        <ul class="info-list">
          <li><b data-i18n="contact.addressTitle"></b><span>119, Perumal Kovil Street, Chinna Thennal, Tamil Nadu 631051</span></li>
          <li><b data-i18n="contact.phoneTitle"></b><a href="tel:+919500418125" style="color:var(--primary);text-decoration:none;">+91 95004 18125</a></li>
          <li><b data-i18n="contact.emailTitle"></b><a href="mailto:sridarm2006@gmail.com" style="color:var(--primary);text-decoration:none;">sridarm2006@gmail.com</a></li>
        </ul>
        <a class="btn btn--outline-dark btn--sm" href="contact.html" data-i18n="nav.contact"></a>
      </div>
    </div>
  </section>
'''

# ==========================================================================
# ABOUT
# ==========================================================================
about_content = page_hero("about.title") + f'''  <section class="section">
    <div class="container" style="max-width:760px;">
      <span class="tag tag--sample" data-i18n="home.sampleLabel"></span>
      <h2 data-i18n="about.introHeading"></h2>
      <p data-i18n="about.introBody"></p>
      <h3 data-i18n="about.significanceHeading"></h3>
      <p data-i18n="about.significanceBody"></p>
      <h3 data-i18n="about.villageHeading"></h3>
      <p data-i18n="about.villageBody"></p>
      <h3 data-i18n="about.communityHeading"></h3>
      <p data-i18n="about.communityBody"></p>
      <div class="disclaimer-box" style="margin-top:24px;"><p data-i18n="about.placeholderNote" style="margin:0;"></p></div>
    </div>
  </section>
'''

# ==========================================================================
# HISTORY
# ==========================================================================
def timeline_item(dot_label, heading_key, desc_key):
    return f'''      <div class="timeline__item">
        <span class="timeline__dot"></span>
        <span class="tag tag--sample" data-i18n="home.sampleLabel"></span>
        <h3 data-i18n="{heading_key}"></h3>
        <p data-i18n="{desc_key}"></p>
      </div>'''

history_content = page_hero("history.title", "history.intro") + '''  <section class="section">
    <div class="container">
      <div class="timeline">
''' + "\n".join([
    timeline_item("1", "history.origin", "history.originDesc"),
    timeline_item("2", "history.early", "history.earlyDesc"),
    timeline_item("3", "history.events", "history.eventsDesc"),
    timeline_item("4", "history.renovation", "history.renovationDesc"),
    timeline_item("5", "history.current", "history.currentDesc"),
]) + '''
      </div>
    </div>
  </section>
'''

# ==========================================================================
# DEITY
# ==========================================================================
deity_content = page_hero("deity.title") + f'''  <section class="section">
    <div class="container grid-2">
      <div class="gallery-tile" style="aspect-ratio:1/1;">
        <span class="icon" style="font-size:3rem;">🌸</span>
        <span class="cat" data-i18n="nav.deity"></span>
      </div>
      <div>
        <span class="tag tag--sample" data-i18n="home.sampleLabel"></span>
        <h2 data-i18n="deity.introHeading"></h2>
        <p style="font-family:var(--font-ta-display);font-size:1.3rem;color:var(--primary);" data-i18n="deity.tamilName"></p>
        <p data-i18n="deity.introBody"></p>
      </div>
    </div>
  </section>
  <section class="section section--surface">
    <div class="container grid-2">
      <div>
        <h3 data-i18n="deity.significanceHeading"></h3>
        <p data-i18n="deity.significanceBody"></p>
      </div>
      <div>
        <h3 data-i18n="deity.worshipHeading"></h3>
        <p data-i18n="deity.worshipBody"></p>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container" style="max-width:760px;">
      <div class="disclaimer-box"><p data-i18n="deity.note" style="margin:0;"></p></div>
    </div>
  </section>
'''

# ==========================================================================
# POOJA
# ==========================================================================
pooja_content = page_hero("pooja.title", "pooja.intro") + f'''  <section class="section">
    <div class="container">
      <div class="table-wrap">
        <table>
          <thead><tr><th data-i18n="pooja.nameCol"></th><th data-i18n="pooja.timeCol"></th><th data-i18n="pooja.noteCol"></th></tr></thead>
          <tbody>
            <tr><td data-i18n-name="0">காலை பூஜை / Morning Pooja</td><td>06:00 AM</td><td class="tag tag--sample" data-i18n="home.sampleLabel" style="display:inline-block;"></td></tr>
            <tr><td>உச்சிகால பூஜை / Uchikala Pooja</td><td>12:00 PM</td><td class="tag tag--sample" data-i18n="home.sampleLabel" style="display:inline-block;"></td></tr>
            <tr><td>மாலை பூஜை / Evening Pooja</td><td>06:00 PM</td><td class="tag tag--sample" data-i18n="home.sampleLabel" style="display:inline-block;"></td></tr>
            <tr><td>இரவு பூஜை / Night Pooja</td><td>08:00 PM</td><td class="tag tag--sample" data-i18n="home.sampleLabel" style="display:inline-block;"></td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section class="section section--surface" id="seva">
    <div class="container">
      <div class="section-heading">
        <h2 data-i18n="pooja.sevaTitle"></h2>
        <p data-i18n="pooja.sevaIntro"></p>
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr>
            <th data-i18n="pooja.sevaName"></th><th data-i18n="pooja.sevaDate"></th>
            <th data-i18n="pooja.sevaTime"></th><th data-i18n="pooja.sevaAmount"></th><th data-i18n="pooja.sevaAvail"></th>
          </tr></thead>
          <tbody>
            <tr><td data-i18n="pooja.archana"></td><td>[ADD DATE]</td><td>[ADD TIME]</td><td>₹50 (sample)</td><td data-i18n="pooja.available"></td></tr>
            <tr><td data-i18n="pooja.abhishekam"></td><td>[ADD DATE]</td><td>[ADD TIME]</td><td>₹250 (sample)</td><td data-i18n="pooja.available"></td></tr>
            <tr><td data-i18n="pooja.festivalPooja"></td><td>[ADD DATE]</td><td>[ADD TIME]</td><td>—</td><td data-i18n="pooja.contactOffice"></td></tr>
            <tr><td data-i18n="pooja.communityPooja"></td><td>[ADD DATE]</td><td>[ADD TIME]</td><td>—</td><td data-i18n="pooja.contactOffice"></td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
'''

# ==========================================================================
# FESTIVALS
# ==========================================================================
def festival_card(name, tamil, date, time):
    return f'''      <div class="panel panel--arch">
        <span class="tag tag--sample" data-i18n="home.sampleLabel"></span>
        <h3>{name}</h3>
        <p style="font-family:var(--font-ta-display);color:var(--primary);margin-bottom:6px;">{tamil}</p>
        <p style="margin-bottom:4px;"><strong data-i18n="festivals.date"></strong>: {date}</p>
        <p style="margin-bottom:12px;"><strong data-i18n="festivals.time"></strong>: {time}</p>
        <p>[Add a short description of this festival's schedule and rituals.]</p>
      </div>'''

festivals_content = page_hero("festivals.title") + '''  <section class="section">
    <div class="container">
      <div class="section-heading" style="text-align:left;max-width:none;">
        <h2 data-i18n="festivals.upcoming"></h2>
      </div>
      <div class="grid-3">
''' + "\n".join([
    festival_card("Aadi Thiruvizha", "ஆடி திருவிழா", "[ADD FESTIVAL DATE]", "[ADD TIME]"),
    festival_card("Navaratri Pooja", "நவராத்திரி பூஜை", "[ADD FESTIVAL DATE]", "[ADD TIME]"),
    festival_card("Thai Pongal Special Pooja", "தை பொங்கல் சிறப்பு பூஜை", "[ADD FESTIVAL DATE]", "[ADD TIME]"),
]) + '''
      </div>
    </div>
  </section>
  <section class="section section--surface">
    <div class="container">
      <div class="section-heading" style="text-align:left;max-width:none;">
        <h2 data-i18n="festivals.past"></h2>
      </div>
      <p data-i18n="festivals.noPast"></p>
    </div>
  </section>
'''

# ==========================================================================
# ANNOUNCEMENTS
# ==========================================================================
announcements_content = page_hero("announcements.title", "announcements.intro") + '''  <section class="section">
    <div class="container" style="max-width:780px;">
      <div class="announce-item is-high">
        <div class="announce-item__meta"><span data-i18n="announcements.priority.high"></span> · <span data-i18n="announcements.published"></span>: 01 September 2026</div>
        <strong>Kumbhabhishekam Planning Meeting / கும்பாபிஷேக ஆலோசனை கூட்டம்</strong>
        <p style="margin:6px 0 0;">[Sample announcement text — replace with real temple news from the administration.]</p>
      </div>
      <div class="announce-item">
        <div class="announce-item__meta"><span data-i18n="announcements.priority.normal"></span> · <span data-i18n="announcements.published"></span>: 28 August 2026</div>
        <strong>Weekly Abhishekam Schedule / வார அபிஷேக அட்டவணை</strong>
        <p style="margin:6px 0 0;">[Sample announcement text — replace with real temple news from the administration.]</p>
      </div>
      <div class="announce-item">
        <div class="announce-item__meta"><span data-i18n="announcements.priority.normal"></span> · <span data-i18n="announcements.published"></span>: 15 August 2026</div>
        <strong>Volunteer Registration Open / தன்னார்வலர் பதிவு தொடங்கியது</strong>
        <p style="margin:6px 0 0;">[Sample announcement text — replace with real temple news from the administration.]</p>
      </div>
    </div>
  </section>
'''

# ==========================================================================
# GALLERY
# ==========================================================================
gallery_cats = [
    ("temple", "gallery.catTemple", "🛕"), ("goddess", "gallery.catGoddess", "🌸"),
    ("festivals", "gallery.catFestivals", "🎉"), ("pooja", "gallery.catPooja", "🪔"),
    ("events", "gallery.catEvents", "🎊"), ("village", "gallery.catVillage", "🏘️"),
    ("renovation", "gallery.catRenovation", "🧱"), ("devotees", "gallery.catDevotees", "🙏"),
]
gallery_tiles = ""
for cat, key, icon in gallery_cats:
    for i in range(2):
        gallery_tiles += f'''        <div class="gallery-tile" data-cat="{cat}"><span class="icon">{icon}</span><span class="cat" data-i18n="{key}"></span></div>\n'''

gallery_filters = f'<button type="button" data-filter="all" class="is-active" data-i18n="gallery.filterAll"></button>\n'
for cat, key, icon in gallery_cats:
    gallery_filters += f'        <button type="button" data-filter="{cat}" data-i18n="{key}"></button>\n'

gallery_content = page_hero("gallery.title", "gallery.intro") + f'''  <section class="section">
    <div class="container">
      <div class="gallery-filters" data-gallery-filters>
        {gallery_filters}
      </div>
      <div class="gallery-grid" data-gallery-grid>
{gallery_tiles}      </div>
    </div>
  </section>
'''

# ==========================================================================
# DONATIONS
# ==========================================================================
donations_content = page_hero("donations.title", "donations.intro") + '''  <section class="section">
    <div class="container grid-2">
      <div class="panel panel--arch" data-donation-form>
        <h2 data-i18n="donations.chooseAmount"></h2>
        <div class="amount-grid">
          <button type="button" class="amount-btn" data-amount="100">₹100</button>
          <button type="button" class="amount-btn" data-amount="250">₹250</button>
          <button type="button" class="amount-btn" data-amount="500">₹500</button>
          <button type="button" class="amount-btn" data-amount="1000">₹1000</button>
        </div>
        <div class="field">
          <label data-i18n="donations.customAmount"></label>
          <input type="number" min="1" data-custom-amount placeholder="₹">
        </div>
        <button class="btn btn--primary btn--block" data-pay-btn data-upi-id="jagadishjaga2004-1@okicici" data-payee-name="Jagadish M" data-i18n="donations.donateNow"></button>
        <p class="form-msg" data-donation-msg></p>
        <p style="margin-top:14px;font-size:.85rem;color:var(--text-soft);" data-i18n="donations.payVia"></p>
        <div class="upi-apps"><span>Google Pay</span><span>PhonePe</span><span>UPI</span></div>
      </div>
      <div>
        <div class="panel" style="margin-bottom:18px;">
          <p style="font-size:.85rem;color:var(--text-soft);margin-bottom:4px;" data-i18n="donations.upiIdLabel"></p>
          <p style="font-family:monospace;font-size:1.05rem;">jagadishjaga2004-1@okicici</p>
          <div class="qr-box" style="margin-top:14px;">
            <div class="qr-frame"><img data-qr-img src="payment/upi-qr.png" alt="UPI QR Code - Jagadish M"></div>
            <p style="font-size:.82rem;color:var(--text-soft);margin:0;" data-i18n="donations.qrCaption"></p>
          </div>
        </div>
        <div class="security-box" style="margin-bottom:14px;">
          <h4 style="margin:0 0 6px;color:var(--primary-dark);font-family:var(--font-en-display);" data-i18n="donations.securityTitle"></h4>
          <p style="margin:0;font-size:.9rem;" data-i18n="donations.securityText"></p>
        </div>
        <div class="disclaimer-box">
          <p style="margin:0;" data-i18n="donations.disclaimer"></p>
        </div>
      </div>
    </div>
  </section>
  <section class="section section--surface">
    <div class="container" style="max-width:640px;">
      <h2 data-i18n="donations.receiptTitle"></h2>
      <p data-i18n="donations.receiptText"></p>
      <table>
        <tbody>
          <tr><td data-i18n="donations.statusPending"></td><td>—</td></tr>
        </tbody>
      </table>
    </div>
  </section>
'''

# ==========================================================================
# VOLUNTEERS
# ==========================================================================
volunteers_content = page_hero("volunteers.title", "volunteers.intro") + '''  <section class="section">
    <div class="container" style="max-width:600px;">
      <form class="panel panel--arch" data-simple-form="volunteers.thankYou">
        <div class="field"><label data-i18n="volunteers.formName"></label><input type="text" required></div>
        <div class="field"><label data-i18n="volunteers.formPhone"></label><input type="tel" required></div>
        <div class="field"><label data-i18n="volunteers.formEmail"></label><input type="email"></div>
        <div class="field"><label data-i18n="volunteers.formArea"></label><input type="text"></div>
        <div class="field">
          <label data-i18n="volunteers.formActivity"></label>
          <select>
            <option data-i18n="volunteers.actFestival"></option>
            <option data-i18n="volunteers.actCleaning"></option>
            <option data-i18n="volunteers.actDecoration"></option>
            <option data-i18n="volunteers.actAnnouncements"></option>
            <option data-i18n="volunteers.actCommunity"></option>
            <option data-i18n="volunteers.actDigital"></option>
          </select>
        </div>
        <button type="submit" class="btn btn--primary btn--block" data-i18n="volunteers.submit"></button>
        <p style="font-size:.82rem;color:var(--text-soft);margin-top:12px;" data-i18n="volunteers.submitNote"></p>
        <p class="form-msg" data-form-msg></p>
      </form>
    </div>
  </section>
'''

# ==========================================================================
# CONTACT
# ==========================================================================
contact_content = page_hero("contact.title") + '''  <section class="section">
    <div class="container grid-2">
      <div>
        <ul class="info-list">
          <li><b data-i18n="contact.addressTitle"></b><span>119, Perumal Kovil Street, Chinna Thennal, Nemili, Tamil Nadu 631051</span></li>
          <li><b data-i18n="contact.phoneTitle"></b><a href="tel:+919500418125" style="color:var(--primary);text-decoration:none;">+91 95004 18125</a></li>
          <li><b data-i18n="contact.emailTitle"></b><a href="mailto:sridarm2006@gmail.com" style="color:var(--primary);text-decoration:none;">sridarm2006@gmail.com</a></li>
        </ul>
      </div>
      <div class="panel panel--arch">
        <h2 data-i18n="contact.formTitle">Send Enquiry</h2>
        <p style="font-size:.9rem;color:var(--text-soft);margin-bottom:24px;">Choose how you would like to contact us:</p>

        <!-- Method 1: Email Enquiry -->
        <div class="enquiry-card" style="border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:16px;background:var(--surface-2,#faf7f2);">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;">
            <span style="font-size:1.6rem;">📧</span>
            <div>
              <h3 style="margin:0;font-size:1rem;color:var(--heading);">Email Enquiry</h3>
              <p style="margin:0;font-size:.82rem;color:var(--text-soft);">Send us a message by email</p>
            </div>
          </div>
          <div class="field"><label style="font-size:.85rem;font-weight:600;color:var(--text-soft);display:block;margin-bottom:4px;">Your Name</label><input type="text" id="eq-name" placeholder="Enter your name" style="width:100%;padding:9px 12px;border:1px solid var(--border);border-radius:8px;font-size:.9rem;background:var(--bg);color:var(--text);box-sizing:border-box;"></div>
          <div class="field" style="margin-top:10px;"><label style="font-size:.85rem;font-weight:600;color:var(--text-soft);display:block;margin-bottom:4px;">Your Message</label><textarea id="eq-message" rows="3" placeholder="Type your enquiry here..." style="width:100%;padding:9px 12px;border:1px solid var(--border);border-radius:8px;font-size:.9rem;background:var(--bg);color:var(--text);box-sizing:border-box;resize:vertical;"></textarea></div>
          <button id="btn-email-enquiry" onclick="sendEmailEnquiry()" class="btn btn--primary btn--block" style="margin-top:12px;">✉️ Send via Email</button>
        </div>

        <!-- Method 2: WhatsApp Enquiry -->
        <div class="enquiry-card" style="border:1px solid #25D366;border-radius:12px;padding:20px;background:#f0fff4;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;">
            <span style="font-size:1.6rem;">💬</span>
            <div>
              <h3 style="margin:0;font-size:1rem;color:#128C7E;">WhatsApp Enquiry</h3>
              <p style="margin:0;font-size:.82rem;color:#555;">Chat directly for further details</p>
            </div>
          </div>
          <p style="font-size:.88rem;color:#333;margin-bottom:14px;">Click below to open our official WhatsApp and send your enquiry directly to <strong>+91 95004 18125</strong>.</p>
          <a id="btn-whatsapp-enquiry" href="https://wa.me/919500418125?text=Namaskaram%2C%20I%20would%20like%20to%20know%20more%20about%20Chinna%20Thennal%20Throbathi%20Amman%20Kovil." target="_blank" rel="noopener" class="btn btn--block" style="background:#25D366;color:#fff;border:none;border-radius:8px;padding:12px;text-align:center;font-size:.95rem;font-weight:600;text-decoration:none;display:block;">
            💬 Chat on WhatsApp
          </a>
          <p style="font-size:.78rem;color:#777;margin-top:10px;text-align:center;">Opens WhatsApp app &bull; Official number: 9500418125</p>
        </div>
      </div>
    </div>
  </section>
  <script>
  function sendEmailEnquiry(){
    var name = document.getElementById("eq-name").value.trim();
    var msg  = document.getElementById("eq-message").value.trim();
    if(!name || !msg){ alert("Please enter your name and message."); return; }
    var subject = encodeURIComponent("Temple Enquiry from " + name);
    var body    = encodeURIComponent("Name: " + name + "\\n\\nMessage:\\n" + msg + "\\n\\n-- Sent from Chinna Thennal Throbathi Amman Kovil website");
    window.location.href = "mailto:sridarm2006@gmail.com?subject=" + subject + "&body=" + body;
  }
  </script>
'''

# ==========================================================================
# LOCATION
# ==========================================================================
location_content = page_hero("location.title", "location.intro") + '''  <section class="section">
    <div class="container">
      <div class="map-frame">
        <iframe src="https://maps.google.com/maps?q=Chinna+Thennal+Throbathi+Amman+Kovil+Tamil+Nadu&t=&z=15&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Chinna Thennal Throbathi Amman Kovil Location Map"></iframe>
      </div>
      <div style="text-align:center;margin-top:20px;display:flex;flex-wrap:wrap;justify-content:center;gap:12px;">
        <a class="btn btn--primary" href="https://maps.app.goo.gl/MZkAEkMwwRaAJEMG9?g_st=aw" target="_blank" rel="noopener" data-direction-link data-i18n="location.getDirections">📍 See Real-Time Location on Maps</a>
      </div>
      <ul class="info-list" style="max-width:520px;margin:32px auto 0;">
        <li><b data-i18n="contact.addressTitle"></b><span id="location-address">119, Perumal Kovil Street, Chinna Thennal, Tamil Nadu 631051</span></li>
        <li><b data-i18n="contact.phoneTitle"></b><a href="tel:+919500418125" style="color:var(--primary);text-decoration:none;">+91 95004 18125</a></li>
        <li><b data-i18n="contact.emailTitle"></b><a href="mailto:sridarm2006@gmail.com" style="color:var(--primary);text-decoration:none;">sridarm2006@gmail.com</a></li>
      </ul>
    </div>
  </section>
'''

# ==========================================================================
# WRITE PAGES
# ==========================================================================
page("index.html", "index.html",
     "சின்ன தென்னல் திரௌபதி அம்மன் கோவில்", "Home",
     "Official digital home of Chinna Thennal Throbathi Amman Kovil village temple — pooja timings, festivals, donations and more.",
     home_content)

page("about.html", "about.html", "About", "About the Temple",
     "About Chinna Thennal Throbathi Amman Kovil — temple introduction and community significance.", about_content)

page("history.html", "history.html", "History", "Temple History",
     "Timeline history of Chinna Thennal Throbathi Amman Kovil.", history_content)

page("deity.html", "deity.html", "Goddess", "Throbathi Amman",
     "About Throbathi Amman, the presiding deity of Chinna Thennal Throbathi Amman Kovil.", deity_content)

page("pooja.html", "pooja.html", "Pooja", "Pooja & Seva",
     "Daily pooja timings and special seva at Chinna Thennal Throbathi Amman Kovil.", pooja_content)

page("festivals.html", "festivals.html", "Festivals", "Festivals",
     "Upcoming and past festivals at Chinna Thennal Throbathi Amman Kovil.", festivals_content)

page("announcements.html", "announcements.html", "Announcements", "Announcements",
     "Latest announcements and temple news.", announcements_content)

page("gallery.html", "gallery.html", "Gallery", "Temple Gallery",
     "Photo gallery of the temple, goddess, festivals and village life.", gallery_content)

page("donations.html", "donations.html", "Donations", "Donations",
     "Support Chinna Thennal Throbathi Amman Kovil via UPI, Google Pay or PhonePe.", donations_content)

page("volunteers.html", "volunteers.html", "Volunteers", "Volunteer at the Temple",
     "Register as a volunteer for Chinna Thennal Throbathi Amman Kovil.", volunteers_content)

page("contact.html", "contact.html", "Contact", "Contact the Temple",
     "Contact details and enquiry form for Chinna Thennal Throbathi Amman Kovil.", contact_content)

page("location.html", "location.html", "Location", "Temple Location",
     "Map, address and directions to Chinna Thennal Throbathi Amman Kovil.", location_content)

print("\\nAll pages generated.")
