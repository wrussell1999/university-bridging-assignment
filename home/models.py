from django.conf import settings
from django.db import models
from django.utils import timezone

class Bio(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, default='Hello!')
    text = models.TextField()

    def __str__(self):
        return self.title

class Socials(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    github = models.TextField()
    twitter = models.TextField()
    linkedin = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.email