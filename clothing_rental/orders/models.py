from django.db import models
from django.conf import settings
# Create your models here.
from accounts.models import User
from products.models import ClothingItem

class OrderStatus(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status
class Order(models.Model):
    user = models.ForeignKey(User, related_name='user_order_set', on_delete=models.DO_NOTHING)
    clothing_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    date_to_be_returned = models.DateField(auto_now_add=False)
    confirmed_returned_date = models.DateField(auto_now_add=False, default=date_to_be_returned)
    total_price = models.DecimalField(max_digits=60, decimal_places=2)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)

    def __str__(self):
        return f'This order {self.code} belongs to ({self.user}) and was created on {self.created_date}'

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    clothing_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.order
