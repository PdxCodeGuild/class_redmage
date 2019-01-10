from django.db import models
from django.utils import timezone
from django.core import validators

from grocery_list.choices import *

import datetime

class Item(models.Model):
    name = models.CharField(max_length=32)
    created_date = models.DateTimeField('date_created')
    completed_date = models.DateTimeField('date completed', null=True, blank=True)
    quantity = models.IntegerField(choices=QUANTITY_CHOICES,default=1)
    obtained = models.BooleanField(default=False)

    def __str__(self):
        return self.name

