from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
    paginate_by = 5

class PostDetailView(DetailView):
    """class to present every post alone"""
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    """class to create post by authenticated users"""
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """set author of post"""
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """class to update post"""
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """set author of post"""
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        """to allow only owner of post can update it """
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """class to delete post"""
    model = Post
    success_url = '/'

    def test_func(self):
        """to allow only owner of post change it """
        post = self.get_object()
        return self.request.user == post.author



def about(request):
    """about page for blog"""
    return render(request, 'blog/about.html', {'title': 'About'})
