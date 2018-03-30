from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    ''' First Landing page '''
    return render(request, "landing.html", {})

def logout_page(request):
    ''' Logout users '''
    logout(request)
    return redirect('home')


