from django.db import models

class Item(models.Model):
    description = models.CharField(max_length=50)
    create_date = models.DateField(auto_now = True)
    complete_date = models.DateField(null = True, blank = True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
