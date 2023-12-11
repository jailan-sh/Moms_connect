from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, userPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-post-detail'),
    path('post/new/', PostCreateView.as_view(), name='blog-post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-post-delete'),
    path('user/<str:username>/', userPostListView.as_view(), name='blog-user-posts'),
    path('about/', views.about, name='blog-about'),
]
