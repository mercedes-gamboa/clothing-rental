from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from orders.models import Order, OrderLine, OrderStatus
from orders.forms import OrderForm, OrderLineForm, OrderStatusForm
# Create your views here.

"""Order Views"""
class OrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("order_list")
    template_name = "orders/add_order.html"



class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("order_list.html")
    template_name = "orders/delete_order.html"

class OrderDetailView(DeleteView):
    model = Order
    template_name = "orders/detail_order.html"

class OrderUpdateView(UpdateView):
    model = Order
    template_name = "orders/update_order.html"
    form_class = OrderForm

""" OrderStatus Views"""

class OrderStatusListView(ListView):
    model = OrderStatus
    template_name = "orders/order_line_list.html"

class OrderStatusCreateView(CreateView):
    model = OrderStatus
    form_class = OrderStatusForm
    success_url = reverse_lazy("order_list")
    template_name = "orders/add_order_status.html"

class OrderStatusDeleteView(DeleteView):
    model = OrderStatus
    success_url = reverse_lazy("order_list.html")
    template_name = "orders/delete_order_line.html"

class OrderStatusDetailView(DetailView):
    model = OrderStatus
    template_name = "orders/detail_order_status.html"

class OrderStatusUpdateView(UpdateView):
    model = OrderStatus
    template_name = "orders/update_order_status.html"
    form_class = OrderStatusForm


""" OrderLine Views"""

class OrderLineListView(ListView):
    model = OrderLine
    template_name = "orders/order_line_list.html"

class OrderLineCreateView(CreateView):
    model = OrderLine
    form_class = OrderStatusForm
    success_url = reverse_lazy("order_list")
    template_name = "orders/add_order_line.html"

class OrderLineDeleteView(DeleteView):
    model = OrderLine
    success_url = reverse_lazy("order_list.html")
    template_name = "orders/delete_status_line.html"

class OrderLineDetailView(DetailView):
    model = OrderLine
    template_name = "orders/detail_line_order.html"

class OrderLineUpdateView(UpdateView):
    model = OrderLine
    template_name = "orders/update_line_order.html"
    form_class = OrderLineForm

