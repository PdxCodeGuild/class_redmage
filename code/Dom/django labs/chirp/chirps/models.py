from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime

class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField(max_length=128)
    pub_date = models.DateTimeField(default= timezone.now)

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])
