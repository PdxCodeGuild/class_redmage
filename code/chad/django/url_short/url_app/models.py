from django.db import models


class UrlModel(models.Model):
    url_long_path = models.TextField()
    url_short_path = models.TextField()
