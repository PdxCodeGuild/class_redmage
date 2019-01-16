from django.db import models
from django.urls import reverse

# class Layer(models.Model):
#     name = models.CharField(max_length = 21)

#     def __str__(self):
#         return self.name

class Point(models.Model):
    name = models.CharField(max_length = 32)
    tag = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    distance_away = models.PositiveIntegerField()
    # layer = models.ForeignKey(Layer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name