from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

from products.models import Clothes, ClothingItem, ClothingConfiguration, Category, Variation, VariationOption, Inventory
from .forms import ClothesForm, CategoryForm, VariationForm, ClothingItemForm, VariationOptionForms,\
    ClothingConfigurationForm, InventoryForm

from accounts.models import ShoppingCart, Favourite

# Create your views here.
class AccessMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, "new_clothing_item.html")

def add_clothes(request):
    if request.method == 'POST':
        form = ClothesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("clothes_list")
    else:
        form = ClothesForm()
    return render(request, "new_clothing_item.html",{
        "form": form
    })


# class AddClothes(View):
#     def get(self, request):
#         form = ClothesForm()
#         return render(
#             request,
#             "add_clothes.html",
#             {"form": form}
#         )
#
#     def post(self, request):
#         form = ClothesForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("clothes_list")


class ClothesListView(View):
    def get(self, request):
        clothes = Clothes.objects.all()
        categories = Category.objects.all()
        data = request.GET
        category = data.get("category")

        if category:
            clothes = clothes.filter(category__id=category)
        return render(
            request,
            "clothes_list.html",
            {
                "clothes": clothes,
                "categories": categories,

            }
        )


class ClothesDeleteView(AccessMixin, DeleteView):
    model = Clothes
    success_url = reverse_lazy("clothes_list")
    template_name = "delete-clothes-item.html"

class ClothesDetailView(DetailView):
    model = Clothes
    template_name = "products/clothes-detail.html"
    context_object_name = "clothes"


class ClothesUpdateView(AccessMixin, UpdateView):
    model = Clothes
    template_name = "products/clothes_update.html"
    form_class = ClothesForm

# class ClothingItemVariatyView(View):
#     def get(self, request):


"""ClothingItem Views"""

class ClothingItemDetailView(DetailView):
    model = ClothingItem
    template_name = "clothing_item.html"
    context_object_name = "clothing"

class ClothingItemListView(ListView):
    model = ClothingItem
    template_name = "clothing_list.html"

class AddClothingView(AccessMixin, CreateView):
    model = ClothingItem
    form_class = ClothingItemForm
    success_url = reverse_lazy("clothing_list")
    template_name = "new_clothing_item.html"


class ClothingItemDeleteView(AccessMixin, DeleteView):
    model = ClothingItem
    success_url = reverse_lazy("clothing_list")
    template_name = "delete-clothes-item.html"


class ClothingItemUpdateView(AccessMixin, UpdateView):
    model = ClothingItem
    template_name = "update_clothing_item.html"
    form_class = ClothingItemForm

"""Category Views"""
class CategoryCreateView(AccessMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")
    template_name = "add_category.html"


class CategoryDeleteView(AccessMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("clothes_list")
    template_name = "delete_category.html"


class CategoryListView(AccessMixin, ListView):
    model = Category
    template_name = "category_list.html"


class CategoryDetailView(AccessMixin, DetailView):
    model = Category
    template_name = "detail_category.html"
    context_object_name = "category"


class CategoryUpdateView(AccessMixin, UpdateView):
    model = Category
    template_name = "update_category_form.html"
    form_class = CategoryForm

"""Variation Views"""
class VariationCreateView(AccessMixin, CreateView):
    model = Variation
    template_name = "add_variation.html"
    fields = ["variation_name", "category"]
    context_object_name = "variation"
    success_url = reverse_lazy("variation_list")


class VariationDeleteView(AccessMixin, DeleteView):
    model = Variation
    success_url = reverse_lazy("variation_list")
    template_name = "delete_variation.html"


class VariationDetailView(AccessMixin, DetailView):
    model = Variation
    template_name = "variation_detail.html"
    context_object_name = "variation"


class VariationListView(AccessMixin, ListView):
    model = Variation
    template_name = "variation_list.html"


class VariationUpdateView(AccessMixin, UpdateView):
    model = Variation
    template_name = "update_variation.html"
    form_class = VariationForm

"""VariationOptions Views"""
class VariationOptionsCreateView(AccessMixin, CreateView):
    model = VariationOption
    template_name = "products/add_variationoptions.html"
    form_class = VariationOptionForms


class VariationOptionDeleteView(AccessMixin, DeleteView):
    model = VariationOption
    success_url = reverse_lazy("variationoptions_list")
    template_name = "delete_variationoptions.html"


class VariationOptionDetailView(AccessMixin, DetailView):
    model = VariationOption
    template_name = "variationoptions_detail.html"


class VariationOptionListView(AccessMixin, ListView):
    model = VariationOption
    template_name = "variationoptions_list.html"


class VariationOptionUpdateView(AccessMixin, UpdateView):
    model = VariationOption
    template_name = "update_variationoptions.html"
    form_class = VariationOptionForms

"""Variation Views"""
class VariationCreateView(AccessMixin, CreateView):
    model = Variation
    template_name = "add_variation.html"
    fields = ["variation_name", "category"]
    context_object_name = "variation"
    success_url = reverse_lazy("variation_list")


class VariationDeleteView(AccessMixin, DeleteView):
    model = Variation
    success_url = reverse_lazy("variation_list")
    template_name = "delete_variation.html"


class VariationDetailView(AccessMixin, DetailView):
    model = Variation
    template_name = "variation_detail.html"
    context_object_name = "variation"


class VariationListView(AccessMixin, ListView):
    model = Variation
    template_name = "variation_list.html"


class VariationUpdateView(AccessMixin, UpdateView):
    model = Variation
    template_name = "update_variation.html"
    form_class = VariationForm

"""ClothingConfiguration Views"""

class ClothingConfigurationListView(AccessMixin, ListView):
    model = ClothingConfiguration
    template_name = "clothing_configuration_list.html"

    def get_queryset(self):

        query = ClothingConfiguration.objects.all()[:1]
        return query

class ClothingConfigurationCreateView(AccessMixin, CreateView):
    model = ClothingConfiguration
    template_name = "add_clothing_configuration.html"
    form_class = ClothingConfigurationForm
    context_object_name = "clothing_configuration"
    success_url = reverse_lazy("clothing_configuration_list")


class ClothingConfigurationDeleteView(AccessMixin, DeleteView):
    model = ClothingConfiguration
    success_url = reverse_lazy("clothing_configuration_list")
    template_name = "delete_clothing_configuration.html"


class ClothingConfigurationDetailView(AccessMixin, DetailView):
    model = ClothingConfiguration
    template_name = "clothing_configuration_detail.html"
    context_object_name = "clothing_configuration"


class ClothingConfigurationUpdateView(AccessMixin, UpdateView):
    model = ClothingConfiguration
    template_name = "update_clothing_configuration.html"
    form_class = ClothingConfigurationForm


"""Inventory Views"""

class InventoryListView(AccessMixin, ListView):
    model = ClothingConfiguration
    template_name = "products/inventory_list.html"


class InventoryCreateView(AccessMixin, CreateView):
    model = Inventory
    template_name = "add_item_inventory.html"
    form_class = InventoryForm
    context_object_name = "inventory"
    success_url = reverse_lazy("inventory_list")


class InventoryDeleteView(AccessMixin, DeleteView):
    model = Inventory
    success_url = reverse_lazy("inventory_list")
    template_name = "delete_inventory-item.html"


class InventoryDetailView(DetailView):
    model = Inventory
    template_name = "inventory_item_detail.html"
    context_object_name = "inventory"


class InventoryUpdateView(AccessMixin, UpdateView):
    model = ClothingConfiguration
    template_name = "update_inventory_item.html"
    form_class = InventoryForm


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, pk):
        cart = get_object_or_404(ShoppingCart, user=request.user)
        clothing_item = get_object_or_404(ClothingItem, id=pk)
        cart.clothing_items.add(clothing_item)
        messages.add_message(
            request=self.request, level=messages.SUCCESS, message="The item has been added to the cart succesfully!"
        )
        return redirect("clothing_list")

class AddToFavouritesView(LoginRequiredMixin, View):
    def post(self, request, pk):
        favourite = get_object_or_404(Favourite, user=request.user)
        clothing_item = get_object_or_404(ClothingItem, id=pk)

        if favourite.exists():
            messages.warning(request=self.request, message="This item is already in your favourites list.")
        else:
            favourite.clothing_items.add(clothing_item)
            messages.add_message(
                request=self.request, level=messages.SUCCESS, message="The item has been added to your favourite's list!"
            )
        return redirect("clothing_item")

class RemoveFavoriteView(LoginRequiredMixin, View):
    def get(self, request, favourite_id):
        favourite = get_object_or_404(Favourite, id=favourite_id, user=request.user)

        favourite.delete()
        messages.add_message(request=self.request, level=messages.SUCCESS, message="Favourite item removed succesfully.")
        return redirect("favourites_list")

class FavouritesListView(LoginRequiredMixin, View):
    def get(self, request):
        favourites = Favourite.objects.filter(user=request.user)
        context = {"favourites": favourites}
        return render(request, "products/favourites_list.html", context)

class CartListView(LoginRequiredMixin, View):
    def get(self, request):
        cart_items = ShoppingCart.objects.filter(user=request.user)
        context = {"cart_items": cart_items}
        return render(request, "products/cart_list.html", context)


