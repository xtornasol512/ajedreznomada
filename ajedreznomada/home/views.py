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


''' Custom error pages '''
def bad_request(request):
    response = render(request, '400.html', {})
    response.status_code = 400
    return response

def permission_denied(request):
    response = render(request, '403.html', {})
    response.status_code = 403
    return response


def page_not_found(request):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response

def server_error(request):
    response = render(request, '500.html', {})
    response.status_code = 500
