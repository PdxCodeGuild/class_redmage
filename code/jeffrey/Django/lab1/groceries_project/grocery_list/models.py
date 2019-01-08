from django.db import models
from django.utils import timezone

import datetime

class Item(models.Model):
    item_text = models.CharField(max_length=50)
    created_date = models.DateTimeField('date_created')
    completed_date = models.DateTimeField('date completed')
    quantity = models.PositiveSmallIntegerField(max_value=10)
    in_basket = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text

