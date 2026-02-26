from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

class ArticleDeleteView(DeleteView):
    model = Article
    template_engine = "article_delete.html"
    success_url = reverse_lazy("article_list") #where you are redirected after deleting an article

class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        "author",
    )
