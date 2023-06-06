from django.urls import path
from orders import views

urlpatterns = [
    path("add/order/", views.OrderCreateView.as_view(), name="add_order"),
    path("list/order/", views.OrderListView.as_view(), name="order_list"),
    path("delete/order/<int:pk>/", views.OrderDeleteView.as_view(), name="delete_order"),
    path("detail/order/<int:pk>/", views.OrderDetailView.as_view(), name="detail_order"),
    path("update/order/<int:pk>/", views.OrderUpdateView.as_view(), name="update_order"),

    path("add/order-status/", views.OrderStatusCreateView.as_view(), name="add_order_status"),
    path("list/order-status/", views.OrderStatusListView.as_view(), name="order_status_list"),
    path("delete/order-status/<int:pk>/", views.OrderStatusDeleteView.as_view(), name="delete_status_order"),
    path("detail/order-status/<int:pk>/", views.OrderStatusDetailView.as_view(), name="detail_status_order"),
    path("update/order-status/<int:pk>/", views.OrderStatusUpdateView.as_view(), name="update_status_order"),

    path("add/order-status/", views.OrderStatusCreateView.as_view(), name="add_order_line"),
    path("list/order-status/", views.OrderStatusListView.as_view(), name="order_line_list"),
    path("delete/order-status/<int:pk>/", views.OrderStatusDeleteView.as_view(), name="delete_line_order"),
    path("detail/order-status/<int:pk>/", views.OrderStatusDetailView.as_view(), name="detail_line_order"),
    path("update/order-status/<int:pk>/", views.OrderStatusUpdateView.as_view(), name="update_line_order"),
]