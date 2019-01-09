from django.db import models
from django.utils import timezone
from django.core import validators

import datetime

class Item(models.Model):
    name = models.CharField(max_length=32)
    created_date = models.DateTimeField('date_created')
    completed_date = models.DateTimeField('date completed')
    quantity = models.PositiveSmallIntegerField(validators.MaxValueValidator(10))
    obtained = models.BooleanField(default=False)

    def __str__(self):
        return self.name

