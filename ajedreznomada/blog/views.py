from django.views.generic.detail import DetailView
from django.utils import timezone

from blog.models import Post

class PostDetailView(DetailView):

    model = Post
    slug_field = 'permanent_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
