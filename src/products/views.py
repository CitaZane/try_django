from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description
    # }
    context = {"object": obj}
    return render(request, "products/detail.html", context)


def product_create_view(request):
    # give initial data / defaults
    initial_data = {'title': "COOL"}
    form = ProductForm(request.POST or None, initial=initial_data)
    
    # example for editing 
    # obj = Product.objects.get(id=1)
    # form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {"form": form}
    return render(request, "products/create.html", context)

def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id) # handle error
    context = {"object": obj}
    return render(request, "products/detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../../')
    context = {"object": obj}

    return render(request, "products/delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all() #list of objects
    context = {"object_list": queryset}
    return render(request, "products/list.html", context)