from django.urls import path
from products import views

urlpatterns = [
    # path("register/", views.register, name='register'),

    path("clothes/", views.ClothesListView.as_view(), name='clothes_list'),
    #path("add/clothes/", views.AddClothingView.as_view(), name='new_clothing_item'),
    path("products/", views.add_clothes, name="new_clothing_item"),
    path("<int:pk>/delete/", views.ClothesDeleteView.as_view(), name="delete_clothes_item"),
    path("<int:pk>/clothing-item", views.ClothingItemDetailView.as_view(), name="clothing_item"),

    path("category/", views.CategoryCreateView.as_view(), name="add_category"),
    path("delete/category/<int:pk>", views.CategoryDeleteView.as_view(), name="delete_category"),
    path("list/category", views.CategoryListView.as_view(), name="category_list"),
    #path("detail/category/<int:pk>", views.CategoryDetailView.as_view(), name="category_detail"),
    path("update/category/<int:pk>", views.CategoryUpdateView.as_view(), name="category_update"),

    path("add/variation", views.VariationCreateView.as_view(), name="add_variation"),
    path("list/variation", views.VariationListView.as_view(), name="variation_list"),
    path("delete/variation/<int:pk>", views.VariationDeleteView.as_view(), name="delete_variation"),
    path("detail/variation/<int:pk>", views.VariationDetailView.as_view(), name="detail_variation"),
    path("update/variation/<int:pk>", views.VariationUpdateView.as_view(), name="update_variation"),

    path("add/variation-option", views.VariationOptionsCreateView.as_view(), name="add_variationoption"),
    path("list/variation-option", views.VariationOptionListView.as_view(), name="variationoption_list"),
    path("delete/variation-option/<int:pk>", views.VariationOptionDeleteView.as_view(), name="delete_variationoption"),
    path("detail/variation-option/<int:pk>", views.VariationOptionDetailView.as_view(), name="detail_variationoption"),
    path("update/variation-option/<int:pk>", views.VariationOptionUpdateView.as_view(), name="update_variationoption"),

]