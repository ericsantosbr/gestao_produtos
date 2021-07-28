import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms.edit_product_form import EditProduct


# Create your views here.
@login_required
def home_view(request):
    return render(request, 'home_index.html')


@login_required
def list_products(request):
    lista = Product.objects.filter(owner=request.user)
    # lista2 = Product(owner=request.user)
    # print('Lista: '+ str(lista2) + '\nObjects: ' + str(lista2.objects))
    return render(request, 'home_list_objects.html', {'data': lista})


@login_required
def edit_products(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = EditProduct(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request, 'home_edit_objects.html', {'form': form})

    return render(request, 'home_edit_objects.html')


@login_required
def add_products(request):
    form = EditProduct(request.POST or None, request.FILES)
    if form.is_valid():
        form.instance.owner = request.user
        form.save()
        return redirect('list_products')
    return render(request, 'home_add_object.html', {'form': form})

@login_required
def delete_products(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.POST:
        product.delete()
        return redirect('list_products')

    return render(request, 'home_delete_object.html', {'data': product})