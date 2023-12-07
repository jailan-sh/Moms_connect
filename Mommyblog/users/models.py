from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    """ profile of user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Bio = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_photos')

    def __str__(self):
        """return string about username profile"""
        return '{} profile'.format(self.user.username)

    def save(self):
        """edit some fatures before saving instancd """
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
