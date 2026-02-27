from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list") #where you are redirected after deleting an article

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) #sets the author to the existing user rather than it
                                        #being set to anyone who chooses to from the users.
