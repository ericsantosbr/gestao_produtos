from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from home.models import Product
from django.shortcuts import get_object_or_404

def homepage_view(request):
    products = Product.objects.all()
    return render(request, 'homepage.html', {'products': products})

def register_user(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        print('form.is_valid() :' + str(form.is_valid()))
        print('form_errors: ' + str(form.errors))
        if form.is_valid():
            form_return = form.save()
            print('form_return: ' + str(form_return))
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
        
        else:
            register_form = UserCreationForm()
            return render(request, 'auth/register.html', {'form': register_form, 'errors': [form.errors]})

    
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': register_form})

def logout_user(request):
    logout(request)
    return redirect('homepage')