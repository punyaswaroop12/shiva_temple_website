from django.contrib import admin
from django.urls import path
from temple_site.core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("services/", views.ServicesView.as_view(), name="services"),
    path("events/", views.EventsView.as_view(), name="events"),
    path("gallery/", views.GalleryView.as_view(), name="gallery"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("donate/", views.DonationView.as_view(), name="donate"),
]
