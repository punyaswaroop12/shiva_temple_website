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
- Templates: `templates/`.
- Static assets: `static/` (e.g., CSS in `css/styles.css`).

## Deploying for free (Render example)
You can keep the site updated by connecting this repository to a free-tier Render Web Service. Typical steps:

1. Push your code to GitHub (or another Git provider).
2. Create a new **Web Service** on [Render](https://render.com) and connect the repo.
3. Use these settings:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
   - **Environment:** `Python 3.11` (or your preferred 3.x version)
4. Add environment variables for your donation info (e.g., `UPI_PAYMENT_LINK`, `UPI_ID`, `BANK_ACCOUNT_NAME`, `BANK_ACCOUNT_NUMBER`, `BANK_IFSC`, `BANK_BRANCH`).
5. Click **Deploy**. Render will build and host the app for free (the free plan sleeps on inactivity but is enough for testing and small traffic).

### Updating the live site
- Commit and push changes to your main branch; Render auto-deploys on new commits.
- For urgent fixes, trigger **Manual Deploy** in Render’s dashboard after pushing.

### Alternatives
- **Railway (free tier)** or **Fly.io** can run the same `gunicorn app:app` command; configure environment variables similarly.
- For a quick demo without an account, use **GitHub Codespaces** or **Gitpod** to run `python app.py` and share the forwarded port URL (session must stay active).
