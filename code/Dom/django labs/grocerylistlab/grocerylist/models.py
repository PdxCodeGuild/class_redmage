from django.db import models

class Item(models.Model):
  item_text = models.CharField(max_length=100)
  qty = models.IntegerField(default=1)
  completed = models.BooleanField(default =False)

  def __str__(self):
    return self.item_text


