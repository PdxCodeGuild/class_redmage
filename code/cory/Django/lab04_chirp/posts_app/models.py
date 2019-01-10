from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post_detail', args=[str(self.id)])