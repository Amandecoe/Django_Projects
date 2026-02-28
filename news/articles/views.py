from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
# Create your views here.

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs): #adds information to the template by updating the context
        context = super().get_context_data(**kwargs) #pull all the existing information into the context using super()
        context ["form"] = CommentForm() # added the variable name form with teh value of Commentform
        return context #return the updated content

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

    def test_func(self): #is the function used by the UserPassesTestMixin to test the user
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list") #where you are redirected after deleting an article

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

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
