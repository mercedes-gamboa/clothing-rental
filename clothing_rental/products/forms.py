from django import forms

from .models import Clothes, Category, Variation, ClothingItem, ClothingConfiguration, VariationOption, Inventory

from accounts.models import Favourite

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ["category", "clothing_name", "description", "clothing_image"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category_name"]


class VariationForm(forms.ModelForm):
    class Meta:
        model = Variation
        fields = ["category", "variation_name"]


class ClothingItemForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields = ["quantity_in_stock", "item_image", "price", "clothes", "code", "name"]


class ClothingConfigurationForm(forms.ModelForm):
    class Meta:
        model = ClothingConfiguration
        fields = ["clothing_item", "variation_option"]


class VariationOptionForms(forms.ModelForm):
    class Meta:
        model = VariationOption
        fields = ["value", "variation"]


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ["clothes_item", "detail", "code", "price"]

class FavouriteForm(forms.ModelForm):
    class Meta:
        model = Favourite
        fields = ["user", "clothing_items"]