from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


def home(request):
    """ home page """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    """ class based view to list posts in home page """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    """class to present every post alone"""
    model = Post

class PostCreateView(CreateView):
    """class to create post"""
    model = Post
    fields = ['title', 'content']


def about(request):
    """about page for blog"""
    return render(request, 'blog/about.html', {'title': 'About'})
