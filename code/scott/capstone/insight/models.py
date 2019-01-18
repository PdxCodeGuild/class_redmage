from django.db import models

class IP(models.Model):
    ip_address = models.GenericIPAddressField(protocol="both", unpack_ipv4=True)
    time_searched = models.TimeField(auto_now=True, auto_now_add=False)
    censys_result = models.TextField(blank=True)
    shodan_result = models.TextField(blank=True)
    def __str__(self):
        return f"{self.ip_address}\t\tSearched: {self.time_searched}"