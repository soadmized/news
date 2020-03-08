from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models


class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'article_detail.html'


class ArticleEditView(UpdateView):
    model = models.Article
    template_name = 'article_edit.html'
    fields = ['title', 'body']


class ArticleDeleteView(DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
