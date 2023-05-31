from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

from products.models import Clothes, ClothingItem, ClothingConfiguration, Category, Variation, VariationOption
from .forms import ClothesForm, CategoryForm

# Create your views here.
# class AddClothingView(CreateView):
#     model = Clothes
#     fields = ('category', 'clothing_name', 'description', 'clothing_image')
#     success_url = reverse_lazy("clothes_list")
#     template_name = "new_clothing_item.html"

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

class ClothesListView(ListView):
    model = Clothes
    template_name = "clothes_list.html"
    context_object_name = "clothes"

class ClothesDeleteView(DeleteView):
    model = Clothes
    success_url = reverse_lazy("clothes_list")
    template_name = "delete-clothes-item.html"

class ClothingItemDetailView(DetailView):
    model = ClothingItem
    template_name = "products/clothes-detail.html"
    context_object_name = "clothing"

"""Category Views"""
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")
    template_name = "add_category.html"

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("clothes_list")
    template_name = "delete_category.html"

class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"

# class CategoryDetailView(DetailView):
#     model = Category
#     template_name = "detail_category.html"
#     context_object_name = "category"

class CategoryUpdateView(UpdateView):
  model = Category
  template_name = "update_category_form.html"
  fields = ["category_name",]

"""Variation Views"""
class VariationCreateView(CreateView):
    model = Variation
    template_name = "add_variation.html"
    fields = ["variation_name", "category"]
    context_object_name = "variation"
    success_url = reverse_lazy("variation_list")

class VariationDeleteView(DeleteView):
    model = Variation
    success_url = reverse_lazy("variation_list")
    template_name = "delete_variation.html"

class VariationDetailView(DetailView):
    model = Variation
    template_name = "variation_detail.html"
    context_object_name = "variation"

class VariationListView(ListView):
    model = Variation
    template_name = "variation_list.html"


class VariationUpdateView(UpdateView):
  model = Variation
  template_name = "update_variation.html"
  fields = ["variation_name", "category"]

"""VariationOptions Views"""
class VariationOptionsCreateView(CreateView):
    model = VariationOption
    template_name = "add_variationoptions.html"
    fields = ["variation_name", "category"]
    context_object_name = "variationoption"

class VariationOptionDeleteView(DeleteView):
    model = VariationOption
    success_url = reverse_lazy("variationoptions_list")
    template_name = "delete_variationoptions.html"

class VariationOptionDetailView(DetailView):
    model = VariationOption
    template_name = "variationoptions_detail.html"
    context_object_name = "variationoption"

class VariationOptionListView(ListView):
    model = VariationOption
    template_name = "variationoptions_list.html"

class VariationOptionUpdateView(UpdateView):
  model = VariationOption
  template_name = "update_variationoptions.html"
  fields = ["value", "variation"]