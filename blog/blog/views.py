from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
