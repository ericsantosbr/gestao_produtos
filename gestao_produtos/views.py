from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, CommentForm
from home.models import Product, Comment
from django.shortcuts import get_object_or_404

def homepage_view(request):
    products = Product.objects.filter(active=True)
    return render(request, 'homepage.html', {'products': products})

def product_view(request, id):
    if(request.method == 'POST'):
        comment_form = CommentForm(request.POST)
        if (comment_form.is_valid()):
            obj = comment_form.save(commit=False)
            obj.author = User.objects.get(id=request.user.id)
            obj.post_id = id
            obj.save()

            redirect(f'produto/{id}')
    
    else:
        comment_form = CommentForm()

    try:
        product = Product.objects.get(id=id)
        comments = Comment.objects.filter(post_id=id, active=True)
        
    except Product.DoesNotExist:
        return redirect('homepage')
    
    except Comment.DoesNotExist:
        comments = {}
    
    return render(request, 'product_page.html', {'product': product, 'comments': comments,'comment_form': comment_form})
    

def register_user(request):
    if request.user.is_authenticated:
        redirect('homepage')
    
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        print('form.is_valid() :' + str(form.is_valid()))
        print('form_errors: ' + str(form.errors))
        if form.is_valid():
            form.save()
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