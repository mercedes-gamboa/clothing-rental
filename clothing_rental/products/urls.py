from django.urls import path
from products import views

urlpatterns = [
    # path("register/", views.register, name='register'),
    path("clothes/", views.ClothesListView.as_view(), name='clothes_list'),
    #path("add/clothes/", views.AddClothingView.as_view(), name='new_clothing_item'),
    path("products/", views.add_clothes, name="new_clothing_item"),
    path("category/", views.CategoryView.as_view(), name="add_category"),
    #path("delete/category/", views.CategoryDeleteView.as_view(), name="delete_category")
]