from django.urls import path
from accounts import views

urlpatterns = [
    path("register/", views.register, name='register'),
    path("profile/", views.update_profile, name='profile'),
    # path("login/", views.user_login, name='login'),
]

