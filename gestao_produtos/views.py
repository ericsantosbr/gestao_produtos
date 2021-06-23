from django.shortcuts import render
from django.contrib.auth import logout

def homepage_view(request):
    return render(request, 'homepage.html')

def logout_user(request):
    return logout(request)