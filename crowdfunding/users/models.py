from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    about = models.TextField(blank=True)
    profile_pic = models.URLField(blank=True)

    def __str__(self):
        return self.username