from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ profile of user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Bio = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_photos')

    def __str__(self):
        """return string about username profile"""
        return '{} profile'.format(self.user.username)
