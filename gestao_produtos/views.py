from django.shortcuts import render, redirect
from django.contrib.auth import logout
from home.models import Product
from django.shortcuts import get_object_or_404

def homepage_view(request):
    products = Product.objects.all()
    return render(request, 'homepage.html', {'products': products})

def logout_user(request):
    logout(request)
    return redirect('homepage')