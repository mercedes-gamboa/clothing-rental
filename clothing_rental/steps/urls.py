from django.urls import path
from steps import views


urlpatterns = [
    path("how-it-works/", views.how_it_works, name='how-it-works'),
]

