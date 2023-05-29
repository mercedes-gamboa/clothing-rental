from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

from products.models import Clothes, ClothingItem, ClothingConfiguration, Category
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

class CategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("clothes_list")
    template_name = "add_category.html"

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("delete_category")
    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        success_url = self.get_success_url("add_category.html")
        self.object.delete()
        return HttpResponseRedirect(success_url)
