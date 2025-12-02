import base64
import io
import os
from typing import Dict, List

import qrcode
from flask import Flask, render_template


def build_qr_data_uri(upi_link: str) -> str:
    qr_image = qrcode.make(upi_link)
    buffer = io.BytesIO()
    qr_image.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


def load_config() -> Dict[str, object]:
    return {
        "upi_link": os.getenv(
            "UPI_PAYMENT_LINK", "upi://pay?pa=temple@bank&pn=Shiva%20Temple&cu=INR"
        ),
        "upi_id": os.getenv("UPI_ID", "temple@bank"),
        "bank_details": {
            "account_name": os.getenv("BANK_ACCOUNT_NAME", "Shiva Temple Trust"),
            "account_number": os.getenv("BANK_ACCOUNT_NUMBER", "1234567890"),
            "ifsc": os.getenv("BANK_IFSC", "BANK0001234"),
            "branch": os.getenv("BANK_BRANCH", "Main Branch"),
        },
        "preset_amounts": [501, 1001, 2501, 5001],
    }


def create_app() -> Flask:
    app = Flask(__name__)

    config = load_config()

    highlights: List[Dict[str, str]] = [
        {
            "title": "Ancient Heritage",
            "description": "Discover the centuries-old temple dedicated to Lord Shiva with rich traditions.",
        },
        {
            "title": "Daily Rituals",
            "description": "Join daily abhishekam, archana, and special poojas performed by our priests.",
        },
        {
            "title": "Community Service",
            "description": "Support charitable activities including annadanam, education, and healthcare.",
        },
    ]

    services: List[Dict[str, str]] = [
        {
            "name": "Rudrabhishekam",
            "description": "A sacred offering to Lord Shiva performed every Monday and Pradosham days.",
        },
        {
            "name": "Archana",
            "description": "Personalized prayers and blessings offered on behalf of devotees.",
        },
        {
            "name": "Annadanam",
            "description": "Contribute to our free meal service offered to visitors and the needy.",
        },
    ]

    events: List[Dict[str, str]] = [
        {
            "date": "Every Monday",
            "title": "Rudrabhishekam",
            "details": "Morning and evening sessions with Vedic chanting and archana.",
        },
        {
            "date": "Pradosham",
            "title": "Pradosha Pooja",
            "details": "Special puja with devotees performing pradakshina around the prakaram.",
        },
        {
            "date": "Monthly",
            "title": "Chandra Darshan",
            "details": "Evening bhajans and moonlight darshan at the temple courtyard.",
        },
    ]

    gallery_images: List[Dict[str, str]] = [
        {
            "src": "https://images.unsplash.com/photo-1517772833180-4d5d2d9e9ff0?auto=format&fit=crop&w=800&q=80",
            "alt": "Temple entrance",
        },
        {
            "src": "https://images.unsplash.com/photo-1516637090014-cb1ab0d08fc7?auto=format&fit=crop&w=800&q=80",
            "alt": "Lamp lighting",
        },
        {
            "src": "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=800&q=80",
            "alt": "Temple corridor",
        },
    ]

    contact_details = {
        "phone": "+91 98765 43210",
        "email": "info@shivatemple.org",
        "address": "123 Temple Street, Sacred Town, India",
        "map_link": "https://www.google.com/maps",
    }

    @app.route("/")
    def home():
        return render_template(
            "home.html",
            highlights=highlights,
            cta_links=[
                {"label": "Plan a visit", "href": "#visit"},
                {"label": "Upcoming events", "href": "/events"},
                {"label": "Donate", "href": "/donate"},
            ],
        )

    @app.route("/about")
    def about():
        story = (
            "The temple stands as a beacon of devotion to Lord Shiva, preserving rituals, music, and architecture "
            "that have served devotees for generations. The sanctum welcomes pilgrims seeking blessings, "
            "peace, and community."
        )
        return render_template("about.html", story=story)

    @app.route("/services")
    def services_page():
        return render_template(
            "services.html",
            services=services,
            booking_email="bookings@shivatemple.org",
        )

    @app.route("/events")
    def events_page():
        return render_template("events.html", events=events)

    @app.route("/gallery")
    def gallery_page():
        return render_template("gallery.html", images=gallery_images)

    @app.route("/contact")
    def contact_page():
        return render_template("contact.html", **contact_details)

    @app.route("/donate")
    def donate():
        qr_data_uri = build_qr_data_uri(config["upi_link"])
        return render_template("donate.html", qr_data_uri=qr_data_uri, **config)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
