''' Urls for Blog Views '''
from django.conf.urls import url

from blog.views import PostDetailView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post-detail'),
]
