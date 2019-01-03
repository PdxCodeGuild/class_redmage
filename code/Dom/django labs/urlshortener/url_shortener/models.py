from django.db import models

# Create your models here.
class Shorten(models.Model):
  Url = models.CharField(max_length =200)
  ShortUrl = models.CharField(max_length = 20)

  def __st__(self):
    return self.name