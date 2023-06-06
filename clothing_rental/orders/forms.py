from django import forms

from .models import Order, OrderStatus, OrderLine

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["user", "clothing_item", "date_to_be_returned", "confirmed_returned_date",
                  "total_price", "status", "code"]

class OrderLineForm(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields = ["order", "inventory"]

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = OrderStatus
        fields = ["status"]