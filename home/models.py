from django.conf import settings
from django.db import models
from django.utils import timezone

class Bio(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, default='Hello!')
    text = models.TextField()

    def __str__(self):
        return self.title

class Social(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    github = models.CharField(max_length=39, default="octocat")
    twitter = models.CharField(max_length=15, default="tweet")
    linkedin = models.CharField(max_length=50, default="will")
    email = models.EmailField()

    def __str__(self):
        return self.email
