from django.urls import path
from products import views

urlpatterns = [

    #path("add/clothes/", views.AddClothingView.as_view(), name='new_clothing_item'),
    path("add/clothing-item/", views.AddClothingView.as_view(), name="new_clothing_item"),
    path("clothing-item/<int:pk>/", views.ClothingItemDetailView.as_view(), name="clothing_item"),
    path("list/clothing-item/", views.ClothingItemListView.as_view(), name="clothing_list"),
    path("delete/clothing-item/<int:pk>/", views.ClothingItemDeleteView.as_view(), name="delete_clothing_item"),
    path("update/clothing-item/<int:pk>/", views.ClothingItemUpdateView.as_view(), name="update_clothing_item"),

    path("delete/clothes/<int:pk>/", views.ClothesDeleteView.as_view(), name="delete_clothe"),
    path("clothes/", views.ClothesListView.as_view(), name="clothes_list"),
    path("update/clothes/<int:pk>/", views.ClothesUpdateView.as_view(), name="clothes_update"),
    path("detail/clothes/<int:pk>/", views.ClothesDetailView.as_view(), name="detail_clothes"),
    path("add/clothes/", views.add_clothes, name="new_clothes"),
    #path("clothes/item-variaty", views.ClothingItemVariatyView.as_view(), name="clothes_variaty_item")

    path("category/", views.CategoryCreateView.as_view(), name="add_category"),
    path("delete/category/<int:pk>/", views.CategoryDeleteView.as_view(), name="delete_category"),
    path("list/category/", views.CategoryListView.as_view(), name="category_list"),
    path("detail/category/<int:pk>/", views.CategoryDetailView.as_view(), name="category_detail"),
    path("update/category/<int:pk>/", views.CategoryUpdateView.as_view(), name="category_update"),

    path("add/variation/", views.VariationCreateView.as_view(), name="add_variation"),
    path("list/variation/", views.VariationListView.as_view(), name="variation_list"),
    path("delete/variation/<int:pk>/", views.VariationDeleteView.as_view(), name="delete_variation"),
    path("detail/variation/<int:pk>/", views.VariationDetailView.as_view(), name="detail_variation"),
    path("update/variation/<int:pk>/", views.VariationUpdateView.as_view(), name="update_variation"),

    path("add/variation-option/", views.VariationOptionsCreateView.as_view(), name="add_variationoption"),
    path("list/variation-option/", views.VariationOptionListView.as_view(), name="variationoption_list"),
    path("delete/variation-option/<int:pk>/", views.VariationOptionDeleteView.as_view(), name="delete_variationoption"),
    path("detail/variation-option/<int:pk>/", views.VariationOptionDetailView.as_view(), name="detail_variationoption"),
    path("update/variation-option/<int:pk>/", views.VariationOptionUpdateView.as_view(), name="update_variationoption"),

    path("add/clothing-configuration/", views.ClothingConfigurationCreateView.as_view(), name="add_clothing_configuration"),
    path("list/clothing-configuration/", views.ClothingConfigurationListView.as_view(), name="clothing_configuration_list"),
    path("delete/clothing-configuration/<int:pk>/", views.ClothingConfigurationDeleteView.as_view(), name="delete_clothing_configuration"),
    path("detail/clothing-configuration/<int:pk>/", views.ClothingConfigurationDetailView.as_view(), name="detail_clothing_configuration"),
    path("update/clothing-configuration/<int:pk>/", views.ClothingConfigurationUpdateView.as_view(), name="update_clothing_configuration"),

    path("add/inventory-item/", views.InventoryCreateView.as_view(), name="add_item_inventory"),
    path("list/inventory/", views.InventoryListView.as_view(), name="inventory_list"),
    path("delete/inventory-item/<int:pk>/", views.InventoryDeleteView.as_view(), name="delete_inventory_item"),
    path("detail/inventory-item/<int:pk>/", views.InventoryDetailView.as_view(), name="detail_inventory_item"),
    path("update/inventory/<int:pk>/", views.InventoryUpdateView.as_view(), name="update_inventory_item"),

    path("add-to-cart/<int:pk>/", views.AddToCartView.as_view(), name='add_to_cart'),
    path("list/cart/", views.CartListView.as_view(), name='cart_list'),

    path("add/favourite/", views.AddToFavouritesView.as_view(), name='add_to_favourites'),
    path("delete/favourite/<int:pk>/", views.RemoveFavoriteView.as_view(), name='remove_favourite'),
    path("list/favourites/", views.FavouritesListView.as_view(), name='favorites_list'),
    ]