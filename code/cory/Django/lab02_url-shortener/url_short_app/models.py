from django.db import models

class UrlShortener(models.Model):
    url = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    click_counter = models.IntegerField(default=0)
    ip_address = models.GenericIPAddressField(default="0.0.0.0", protocol="IPv4")

    def __str__(self):
        return self.code

