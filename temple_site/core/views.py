import base64
import io

import qrcode
from django.conf import settings
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "highlights": [
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
                ],
                "cta_links": [
                    {"label": "Plan a visit", "href": "#visit"},
                    {"label": "Upcoming events", "href": "/events/"},
                    {"label": "Donate", "href": "/donate/"},
                ],
            }
        )
        return context


class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["story"] = (
            "The temple stands as a beacon of devotion to Lord Shiva, preserving rituals, music, and architecture "
            "that have served devotees for generations. The sanctum welcomes pilgrims seeking blessings, "
            "peace, and community."
        )
        return context


class ServicesView(TemplateView):
    template_name = "core/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = [
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
        context["booking_email"] = "bookings@shivatemple.org"
        return context


class EventsView(TemplateView):
    template_name = "core/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = [
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
        return context


class GalleryView(TemplateView):
    template_name = "core/gallery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = [
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
        return context


class ContactView(TemplateView):
    template_name = "core/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "phone": "+91 98765 43210",
                "email": "info@shivatemple.org",
                "address": "123 Temple Street, Sacred Town, India",
                "map_link": "https://www.google.com/maps",
            }
        )
        return context


class DonationView(TemplateView):
    template_name = "core/donate.html"

    def _build_qr_data_uri(self):
        qr_image = qrcode.make(settings.UPI_PAYMENT_LINK)
        buffer = io.BytesIO()
        qr_image.save(buffer, format="PNG")
        encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return f"data:image/png;base64,{encoded}"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "upi_link": settings.UPI_PAYMENT_LINK,
                "upi_id": settings.UPI_ID,
                "qr_data_uri": self._build_qr_data_uri(),
                "bank_details": settings.BANK_DETAILS,
                "preset_amounts": [501, 1001, 2501, 5001],
            }
        )
        return context
