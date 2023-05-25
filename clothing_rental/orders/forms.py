from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

class Order(models.Model):
    ORDERED = "ORDERED"
    PREPARING = "PREPARING"
    ON_THE_WAY = "ON THE WAY"
    CLIENT_WARDROBE = "CLIENT WARDROBE"
    RETURNED = "RETURNED"
    DONE = "DONE"

    STATUSES = (
        (ORDERED, "Ordered"),
        (PREPARING, "Preparing"),
        (ON_THE_WAY, "On the way"),
        (CLIENT_WARDROBE, "Client's wardrobe"),
        (RETURNED, "Returned"),
        (DONE, "Done"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="orders", on_delete=models.CASCADE
    )

    # product
    # price
    # total price

    status = models.CharField(max_length=50, choices=STATUSES, default=ORDERED)
    created_at = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now=False, blank=True)
    returned_at = models.DateTimeField(auto_now=True)

