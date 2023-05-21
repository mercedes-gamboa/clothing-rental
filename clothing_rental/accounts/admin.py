from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistrationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    form = UserRegistrationForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)