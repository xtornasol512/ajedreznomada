from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Post

def home(request):
    ''' First Landing page '''
    blog_posts = Post.objects.all().order_by('-id')
    return render(request, "landing.html", {'blog_posts': blog_posts})

def welcome(request, name=''):
    ''' Say hello to users '''
    if not name.strip() != '':
        name = "visitante"
    return render(request, 'welcome.html', {'name': name})

def logout_page(request):
    ''' Logout users '''
    logout(request)
    return redirect('home')


''' Custom error pages '''
def bad_request(request):
    response = render(request, '_error_codes.html', {
                                    'error_title': '400 Bad request',
                                    'error_msg':'Aceptamos que podemos tener errores pero este fue que introdujiste mal datos',
                                    'error_alt':'Bad response 400'})
    response.status_code = 400
    return response

def permission_denied(request):
    response = render(request, '_error_codes.html', {
                                    'error_title': 'ERROR 403',
                                    'error_msg':'No tienes permisos, contacta un administrador',
                                    'error_alt':'Permission denied 403'})
    response.status_code = 403
    return response


def page_not_found(request):
    response = render(request, '_error_codes.html', {
                                    'error_title': 'Error 404 Chess Not Found',
                                    'error_msg':'Chess Not FOUND! OMG!',
                                    'error_alt':'Page not found 404'})
    response.status_code = 404
    return response

def server_error(request):
    response = render(request, '_error_codes.html', {
                                    'error_title': '500 Internal Server Error',
                                    'error_msg':'Nuestros circuitos chocaron con algo inesperado, intenta contactar tu administrador',
                                    'error_alt':'Server error 500'})
    response.status_code = 500
