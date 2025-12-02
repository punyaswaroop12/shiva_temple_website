# Shiva Temple Website

A Django-based website for a Lord Shiva temple with informational pages and a UPI-enabled donations page.

## Features
- Home, About, Services, Events, Gallery, Contact, and Donations pages.
- UPI donation QR code generation with configurable payment link and preset amounts.
- Bank transfer details and guidance for acknowledgement emails.
- Responsive layout styled with a simple CSS theme.

## Getting started
1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run migrations** to set up the SQLite database:
   ```bash
   python manage.py migrate
   ```
4. **Start the development server**:
   ```bash
   python manage.py runserver
   ```
5. Open http://127.0.0.1:8000 in your browser.

## Configuration
Environment variables (optional) allow you to customize donation details:
- `UPI_PAYMENT_LINK` – full UPI deep link for the QR (default: `upi://pay?pa=temple@bank&pn=Shiva%20Temple&cu=INR`).
- `UPI_ID` – displayed UPI handle (default: `temple@bank`).
- `BANK_ACCOUNT_NAME`, `BANK_ACCOUNT_NUMBER`, `BANK_IFSC`, `BANK_BRANCH` – shown in the bank transfer section.
- `DJANGO_ALLOWED_HOSTS` – comma-separated hostnames for production.
- `DJANGO_SECRET_KEY` – override the development secret key.

## Notes
- Static files live in `temple_site/core/static/` and templates in `temple_site/core/templates/`.
- Add models and register them in `temple_site/core/admin.py` to manage content through the Django admin.
