from django.shortcuts import render, redirect
from django.contrib.auth import logout

def homepage_view(request):
    return render(request, 'homepage.html')

def logout_user(request):
    logout(request)
    return redirect('homepage')