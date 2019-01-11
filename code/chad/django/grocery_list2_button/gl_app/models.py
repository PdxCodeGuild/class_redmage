from django.db import models


class GroceryListModel(models.Model):
    gc_item = models.TextField(null=False, blank=False,)
    gc_submit_date = models.DateTimeField(auto_now_add=True,)
