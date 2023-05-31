from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

import products


# Create your models here.
class Category(models.Model):
    # TOPS = 'Tops'
    # BOTTOMS = 'Bottoms'
    # DRESSSES = 'Dresses'
    # SKIRTS = 'Skirts'
    # COATS_JACKETS = 'Coats & Jackets'
    # OUTWEAR = 'Outerwear'
    # ACCESSORIES = 'Accessories'
    # FORMAL_WEAR = 'Formal Wear'
    # VINTAGE = 'Vintage'
    # SUMMER = 'Summer'
    # WINTER = 'Winter'
    # FALL = 'Fall'
    # SPRING = 'Spring'
    #
    # CATEGORY_CHOICES = (
    #     (TOPS, 'Tops'),
    #     (BOTTOMS, 'Bottoms'),
    #     (DRESSSES, 'Dresses'),
    #     (SKIRTS, 'Skirts'),
    #     (COATS_JACKETS, 'Coats & Jackets'),
    #     (OUTWEAR, 'Outerwear'),
    #     (ACCESSORIES, 'Accessories'),
    #     (FORMAL_WEAR, 'Formal Wear'),
    #     (VINTAGE, 'Vintage'),
    #     (SUMMER, 'Summer'),
    #     (WINTER, 'Winter'),
    #     (FALL, 'Fall'),
    #     (SPRING,'Spring')
    # )

    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
class Clothes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    clothing_name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    clothing_image = models.ImageField(width_field=None, height_field=None, null=True, blank=True)

    def __str__(self):
        return self.clothing_name

class Variation(models.Model):
    variation_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.variation_name} ({self.category})'

class VariationOption(models.Model):
    value = models.CharField(max_length=200)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)

    def __str__(self):
        return self.value

class ClothingItem(models.Model):
    quantity_in_stock = models.IntegerField(validators=[MinValueValidator(0)])
    item_image = models.ImageField(width_field=None, height_field=None)
    price = models.DecimalField(max_digits=65, decimal_places=2, default=0)
    clothes = models.ForeignKey(Clothes, on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=300)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name} ({self.code})'

class ClothingConfiguration(models.Model):
    clothing_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    variation_option = models.ForeignKey(VariationOption, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.clothing_item} ({self.variation_option})'