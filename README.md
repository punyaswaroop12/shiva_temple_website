# Shiva Temple Website

A Flask-based website for a Lord Shiva temple with informational pages and a UPI-enabled donations page.

## Features
- Home, About, Services, Events, Gallery, Contact, and Donations pages.
- UPI donation QR code generation with configurable payment link and preset amounts.
- Bank transfer details and guidance for acknowledgement emails.
- Responsive layout styled with a simple CSS theme.

## Running locally with Conda + Flask
1. **Create and activate a Conda environment** (Python 3.11+ recommended):
   ```bash
   conda create -n shiva-temple python=3.11
   conda activate shiva-temple
   ```

2. **Install dependencies** (inside the Conda env):
   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Start the development server**:
   ```bash
   python app.py
   ```
   The site will be available at http://127.0.0.1:5000.

## Configuration
Environment variables (optional) allow you to customize donation details:
- `UPI_PAYMENT_LINK` – full UPI deep link for the QR (default: `upi://pay?pa=temple@bank&pn=Shiva%20Temple&cu=INR`).
- `UPI_ID` – displayed UPI handle (default: `temple@bank`).
- `BANK_ACCOUNT_NAME`, `BANK_ACCOUNT_NUMBER`, `BANK_IFSC`, `BANK_BRANCH` – shown in the bank transfer section.

## Project layout
- Flask app entrypoint: `app.py`.
- Templates: `temple_site/core/templates/core/`.
- Static assets: `temple_site/core/static/` (e.g., CSS in `css/styles.css`).
