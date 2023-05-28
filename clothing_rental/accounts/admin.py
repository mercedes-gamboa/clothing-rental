from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import Profile
from products.models import Clothes, Category, Variation, VariationOption, ClothingItem, ClothingConfiguration

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...


# Register your models here.
admin.site.register(Profile)

admin.site.register(Clothes)
admin.site.register(Category)
admin.site.register(Variation)
admin.site.register(VariationOption)
admin.site.register(ClothingItem)
admin.site.register(ClothingConfiguration)