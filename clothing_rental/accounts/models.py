from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
class Customer(models.Model):
    MEMBERSHIP_STANDARD = 'Standard'
    MEMBERSHIP_FASHIONISTA = 'Fashionista'
    MEMBERSHIP_RUNWAY = 'Runway'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_STANDARD, 'Standard'),
        (MEMBERSHIP_FASHIONISTA, 'Fashionista'),
        (MEMBERSHIP_RUNWAY, 'Runway'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=50, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_STANDARD)
