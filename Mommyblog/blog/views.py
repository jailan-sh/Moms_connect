from django.shortcuts import render
from .models import Post


def home(request):
    """ home page """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    """about page for blog"""
    return render(request, 'blog/about.html', {'title': 'About'})
