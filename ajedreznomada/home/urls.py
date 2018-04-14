''' Urls for Home Views '''
from django.conf.urls import url
from .views import home, logout_page, welcome

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^welcome/$', welcome, name='welcome_alone'),
    url(r'^welcome/(?P<name>[\w.@+-]+)/$', welcome, name='welcome_email'),
    url(r'^welcome/(?P<name>[A-Za-z]*)/$', welcome, name='welcome'),
    url(r'^logout/$', logout_page, name='logout_page'),
]
