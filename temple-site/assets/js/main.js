/* ==========================================================================
   MAIN SITE SCRIPT
   Handles: language switching, mobile nav, UPI link generation,
   simple form feedback, gallery filtering. No build step required —
   this file works by opening any .html file directly in a browser.
   ========================================================================== */

/* ---------- Language switching ---------- */
const LANG_KEY = "temple-lang";

function getLang(){
  return localStorage.getItem(LANG_KEY) || "en";
}

function applyTranslations(lang){
  const dict = TRANSLATIONS[lang] || TRANSLATIONS.en;
  document.documentElement.setAttribute("lang", lang);
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (dict[key] !== undefined) el.textContent = dict[key];
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
    const key = el.getAttribute("data-i18n-placeholder");
    if (dict[key] !== undefined) el.setAttribute("placeholder", dict[key]);
  });
  document.querySelectorAll(".lang-switch button").forEach(btn => {
    btn.classList.toggle("is-active", btn.getAttribute("data-lang") === lang);
  });
}

function setLang(lang){
  localStorage.setItem(LANG_KEY, lang);
  applyTranslations(lang);
}

function initLangSwitch(){
  document.querySelectorAll("[data-lang]").forEach(btn => {
    btn.addEventListener("click", () => setLang(btn.getAttribute("data-lang")));
  });
  applyTranslations(getLang());
}

/* ---------- Mobile nav ---------- */
function initMobileNav(){
  const btn = document.querySelector(".hamburger");
  const links = document.querySelector(".nav__links");
  if (!btn || !links) return;
  btn.addEventListener("click", () => {
    const open = links.classList.toggle("is-open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });
}

/* ---------- Mark current nav link ---------- */
function markActiveNav(){
  const path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav__links a").forEach(a => {
    const href = a.getAttribute("href");
    if (href === path) a.setAttribute("aria-current", "page");
  });
}

/* ---------- UPI payment link ---------- */
function buildUpiLink({ upiId, payeeName, amount, note, scheme = "upi" }){
  const cleanId = (upiId && upiId.indexOf("[ADD") !== 0) ? upiId : "jagadishjaga2004-1@okicici";
  const params = new URLSearchParams();
  params.set("pa", cleanId);
  params.set("pn", payeeName || "Jagadish M");
  if (amount) params.set("am", amount);
  params.set("cu", "INR");
  if (note) params.set("tn", note || "Temple Donation");
  return `${scheme}://pay?${params.toString()}`;
}

function initDonationForm(){
  const form = document.querySelector("[data-donation-form]");
  if (!form) return;

  const amountButtons = form.querySelectorAll(".amount-btn[data-amount]");
  const customInput = form.querySelector("[data-custom-amount]");
  const msg = form.querySelector("[data-donation-msg]");
  const qrImg = document.querySelector("[data-qr-img]");
  const amountDisplay = document.querySelector("[data-selected-amount-display]");
  const copyBtn = document.querySelector("[data-copy-upi]");
  const upiIdText = document.querySelector("[data-upi-id-text]");
  const appButtons = document.querySelectorAll("[data-app-scheme]");

  let selectedAmount = "500"; // default to 500
  const defaultUpiId = form.getAttribute("data-upi-id") || "jagadishjaga2004-1@okicici";
  const payeeName = form.getAttribute("data-payee-name") || "Jagadish M";

  function getActiveAmount(){
    if (customInput && customInput.value && Number(customInput.value) > 0) {
      return customInput.value;
    }
    return selectedAmount;
  }

  function updatePaymentState(){
    const currentAmount = getActiveAmount();
    if (amountDisplay) {
      amountDisplay.textContent = currentAmount ? `₹${currentAmount}` : "₹0";
    }

    const upiLink = buildUpiLink({
      upiId: defaultUpiId,
      payeeName,
      amount: currentAmount,
      note: "Donation"
    });

    if (qrImg) {
      const qrApiUrl = `https://api.qrserver.com/v1/create-qr-code/?size=240x240&data=${encodeURIComponent(upiLink)}`;
      qrImg.src = qrApiUrl;
    }
  }

  amountButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      amountButtons.forEach(b => b.classList.remove("is-active"));
      btn.classList.add("is-active");
      selectedAmount = btn.getAttribute("data-amount");
      if (customInput) customInput.value = "";
      updatePaymentState();
    });
  });

  if (customInput){
    customInput.addEventListener("input", () => {
      amountButtons.forEach(b => b.classList.remove("is-active"));
      selectedAmount = customInput.value;
      updatePaymentState();
    });
  }

  appButtons.forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const currentAmount = getActiveAmount();
      const dict = TRANSLATIONS[getLang()];
      if (!currentAmount || Number(currentAmount) <= 0){
        if (msg) {
          msg.textContent = dict["donations.enterAmountFirst"];
          msg.classList.add("is-shown");
        }
        return;
      }
      const scheme = btn.getAttribute("data-app-scheme") || "upi";
      const link = buildUpiLink({
        upiId: defaultUpiId,
        payeeName,
        amount: currentAmount,
        note: "Donation",
        scheme
      });
      window.location.href = link;
    });
  });

  if (copyBtn && upiIdText) {
    copyBtn.addEventListener("click", () => {
      const upiId = upiIdText.textContent.trim();
      navigator.clipboard.writeText(upiId).then(() => {
        const dict = TRANSLATIONS[getLang()];
        const originalText = copyBtn.textContent;
        copyBtn.textContent = dict["donations.copiedSuccess"] || "Copied!";
        copyBtn.classList.add("is-copied");
        setTimeout(() => {
          copyBtn.textContent = originalText;
          copyBtn.classList.remove("is-copied");
        }, 2500);
      }).catch(err => {
        console.error("Copy failed", err);
      });
    });
  }

  // Initial setup call
  updatePaymentState();
}

/* ---------- Gallery filter ---------- */
function initGalleryFilter(){
  const filterBar = document.querySelector("[data-gallery-filters]");
  const grid = document.querySelector("[data-gallery-grid]");
  if (!filterBar || !grid) return;
  filterBar.addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-filter]");
    if (!btn) return;
    filterBar.querySelectorAll("button").forEach(b => b.classList.remove("is-active"));
    btn.classList.add("is-active");
    const filter = btn.getAttribute("data-filter");
    grid.querySelectorAll(".gallery-tile").forEach(tile => {
      const cat = tile.getAttribute("data-cat");
      tile.style.display = (filter === "all" || filter === cat) ? "" : "none";
    });
  });
}

/* ---------- Generic form feedback (volunteer / contact) ---------- */
function initSimpleForms(){
  document.querySelectorAll("[data-simple-form]").forEach(form => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const dict = TRANSLATIONS[getLang()];
      const msgKey = form.getAttribute("data-simple-form");
      const msg = form.querySelector("[data-form-msg]");
      if (msg){
        msg.textContent = dict[msgKey] || "Thank you.";
        msg.classList.add("is-shown");
      }
      form.reset();
    });
  });
}

/* ---------- Unique Theme Customizer ---------- */
const THEME_KEY = "temple-theme";

function getTheme(){
  return localStorage.getItem(THEME_KEY) || "sandalwood";
}

function setTheme(theme){
  localStorage.setItem(THEME_KEY, theme);
  document.documentElement.setAttribute("data-theme", theme);
  document.querySelectorAll(".theme-dot").forEach(dot => {
    dot.classList.toggle("is-active", dot.getAttribute("data-theme-val") === theme);
  });
}

function initThemeSwitcher(){
  document.querySelectorAll(".theme-dot").forEach(dot => {
    dot.addEventListener("click", () => {
      setTheme(dot.getAttribute("data-theme-val"));
    });
  });
  setTheme(getTheme());
}

/* ---------- Geolocation & Directions ---------- */
function initGeolocation(){
  const btn = document.querySelector("[data-get-location-btn]");
  const directionLink = document.querySelector("[data-direction-link]");
  const statusMsg = document.querySelector("[data-location-status]");

  const defaultMapsUrl = "https://maps.app.goo.gl/MZkAEkMwwRaAJEMG9?g_st=aw";

  if (directionLink) {
    directionLink.href = defaultMapsUrl;
    directionLink.target = "_blank";
  }

  if (!btn) return;

  btn.addEventListener("click", (e) => {
    e.preventDefault();
    const dict = TRANSLATIONS[getLang()];
    if (!navigator.geolocation) {
      if (statusMsg) {
        statusMsg.textContent = dict["location.locDenied"] || "Geolocation is not supported by your browser.";
        statusMsg.style.display = "block";
      }
      return;
    }

    if (statusMsg) {
      statusMsg.textContent = dict["location.locating"] || "Finding your GPS location...";
      statusMsg.style.display = "block";
    }

    navigator.geolocation.getCurrentPosition(
      (position) => {
        const lat = position.coords.latitude;
        const lng = position.coords.longitude;
        const directionsUrl = `https://www.google.com/maps/dir/?api=1&origin=${lat},${lng}&destination=12.5694,79.5298`;
        
        if (directionLink) {
          directionLink.href = directionsUrl;
        }

        if (statusMsg) {
          statusMsg.textContent = dict["location.locFound"] || "Location found! Dynamic Google Maps route updated.";
          statusMsg.style.color = "var(--success)";
        }
        window.open(directionsUrl, "_blank");
      },
      (error) => {
        console.warn("Geolocation error:", error);
        if (statusMsg) {
          statusMsg.textContent = dict["location.locDenied"] || "Location permission denied. Showing standard directions.";
          statusMsg.style.color = "var(--primary-dark)";
        }
      },
      { timeout: 10000, enableHighAccuracy: true }
    );
  });
}

/* ---------- Share Location for Others ---------- */
function initShareLocation(){
  const whatsappBtn = document.querySelector("[data-share-whatsapp]");
  const copyBtn = document.querySelector("[data-copy-map-link]");
  const mapLinkText = document.querySelector("[data-map-link-val]");
  const shareMsg = document.querySelector("[data-share-status-msg]");

  const locationUrl = "https://maps.app.goo.gl/MZkAEkMwwRaAJEMG9?g_st=aw";
  const shareText = "Chinna Thennal Throbathi Amman Kovil Location Pin:\n" + locationUrl;

  if (whatsappBtn) {
    whatsappBtn.href = `https://api.whatsapp.com/send?text=${encodeURIComponent(shareText)}`;
    whatsappBtn.target = "_blank";
  }

  if (copyBtn) {
    copyBtn.addEventListener("click", (e) => {
      e.preventDefault();
      const urlToCopy = (mapLinkText && mapLinkText.textContent.trim()) ? mapLinkText.textContent.trim() : locationUrl;
      navigator.clipboard.writeText(urlToCopy).then(() => {
        const dict = TRANSLATIONS[getLang()];
        const originalText = copyBtn.textContent;
        copyBtn.textContent = dict["location.copiedLinkMsg"] || "Copied!";
        copyBtn.classList.add("is-copied");
        if (shareMsg) {
          shareMsg.textContent = dict["location.copiedLinkMsg"] || "Location link copied to clipboard!";
          shareMsg.style.display = "block";
          shareMsg.style.color = "var(--success)";
        }
        setTimeout(() => {
          copyBtn.textContent = originalText;
          copyBtn.classList.remove("is-copied");
          if (shareMsg) shareMsg.style.display = "none";
        }, 2500);
      }).catch(err => {
        console.error("Copy map link error", err);
      });
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  initThemeSwitcher();
  initLangSwitch();
  initMobileNav();
  markActiveNav();
  initDonationForm();
  initGalleryFilter();
  initSimpleForms();
  initGeolocation();
  initShareLocation();
});
