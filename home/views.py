import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Product
from .forms.edit_product_form import EditProduct


# Create your views here.
@login_required
def home_view(request):
    return render(request, 'home_index.html')


@login_required
def list_products(request):
    lista = Product.objects.filter(owner=request.user)
    return render(request, 'home_list_objects.html', {'data': lista})


@login_required
def edit_products(request, product_id):
    #product = get_object_or_404(Product, pk=product_id)
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return render(request, 'home_edit_objects.html', {'product_found': False})

    if(product.active == False):
        return render(request, 'home_edit_objects.html', {'product_found': False, 'product_active': False})


    form = EditProduct(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('list_products')
    print(product.photo)
    return render(request, 'home_edit_objects.html', {'product_found': True, 'product_active': True,'form': form, 'image_url': product.photo})


@login_required
def add_products(request):
    form = EditProduct(request.POST or None, request.FILES)
    if form.is_valid():
        form.instance.owner = request.user
        form.save()
        return redirect('list_products')
    return render(request, 'home_add_object.html', {'form': form})

@permission_required('home.delete_product', raise_exception=True)
def delete_products(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.POST:
        product.delete()
        return redirect('list_products')

    return render(request, 'home_delete_object.html', {'data': product})

@permission_required('home.change_product', raise_exception=True)
def deactivate_products(request, product_id):
    product:Product = get_object_or_404(Product, pk=product_id)

    if request.POST:
        product.active = False
        product.save()
        return redirect('homepage')

    return render(request, 'home_deactivate_object.html', {'data': product})
