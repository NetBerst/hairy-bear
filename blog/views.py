from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class PostsListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.order_by('-datetime')

class PostDetailView(DetailView):
    model = Post
