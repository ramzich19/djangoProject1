from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormMixin
from hitcount.views import HitCountDetailView

class HomeListView(ListView):
    model = Articles
    template_name = 'projects.html'
    context_object_name = 'list_articles'
    paginate_by = 2


class HomeDetailView(HitCountDetailView):
    model = Articles
    template_name = 'detail2.html'
    context_object_name = 'get_article'
    count_hit = True
