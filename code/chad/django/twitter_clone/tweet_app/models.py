from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class TwitterModel(models.Model):
    tweet_text = models.CharField(max_length=128, null=False, blank=False)
    # author = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title