from django.urls import path
from about import views


urlpatterns = [
    path("about/", views.about_page, name='about'),
    path("contact/", views.ContactUs.as_view(), name='contact_us')
]