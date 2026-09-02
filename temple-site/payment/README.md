# UPI QR code

Put the temple's official UPI QR code image here as:

    payment/upi-qr.png

Then open `donations.html` and replace the placeholder QR box:

```html
<div class="qr-frame"><span data-i18n="donations.qrTitle" ...></span></div>
```

with:

```html
<div class="qr-frame"><img src="payment/upi-qr.png" alt="Temple UPI QR code"></div>
```

Also update the UPI ID in **two** places:
1. `config/temple.json` → `"upiId"`
2. `donations.html` → the `data-upi-id="..."` attribute on the Donate Now button

Never commit real bank account numbers, IFSC codes, or payment gateway
secret keys to this folder or to GitHub — only the public UPI ID and QR
image, which are already meant to be shared with devotees.
