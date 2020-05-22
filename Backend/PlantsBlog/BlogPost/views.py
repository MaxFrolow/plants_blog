from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView

from .models import PlantPost

class PostListView(ListView):
    model = PlantPost
    queryset = PlantPost.objects.all()[2:]
    context_object_name = 'post_list'
    paginate_by = 6
    template_name = 'bloglist/list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['thumb_sec'] = PlantPost.objects.all()[:2]
        return context

