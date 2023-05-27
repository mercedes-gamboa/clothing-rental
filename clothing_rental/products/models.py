from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

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
    clothing_image = models.ImageField(width_field=None, height_field=None)

    def __str__(self):
        return self.clothing_name

class Variation(models.Model):
    variation_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.variation_name

class VariationOption(models.Model):
    value = models.CharField(max_length=200)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)

