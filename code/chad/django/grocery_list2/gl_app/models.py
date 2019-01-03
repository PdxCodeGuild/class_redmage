from django.db import models

class GroceryListModel(models.Model):
    gc_item = models.TextField()
    gc_submit_date = models.DateTimeField()
