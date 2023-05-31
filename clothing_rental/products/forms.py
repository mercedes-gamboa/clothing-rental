from django import forms

from .models import Clothes, Category, Variation

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
