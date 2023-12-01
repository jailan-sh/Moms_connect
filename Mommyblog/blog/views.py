from django.shortcuts import render


posts = [
    {
        'author': 'jailan',
        "title": 'post 1',
        'content': 'mommyblog',
        'date_posted': '25-8'
    }
]


def home(request):
    """ home page """
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    """about page for blog"""
    return render(request, 'blog/about.html', {'title': 'About'})
