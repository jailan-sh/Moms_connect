from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    """posts model for the blog"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """return  a string represent post title"""
        return self.title

    def get_absolute_url(self):
        """redirect to the post page after creation"""
        return reverse('blog-post-detail', kwargs={'pk': self.pk})
