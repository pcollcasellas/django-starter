from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static


class User(AbstractUser):
    image = models.ImageField(upload_to="avatars/", null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.email)

    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except:
            avatar = static("images/avatar.svg")
        return avatar
