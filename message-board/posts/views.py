from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all() #database query to get all objects of the model, objects is a manager which gives access to the db
    return render (request, "post_list.html", {"posts": posts}) #the context dictionary here displays our posts from the db in a "post": hello world format

