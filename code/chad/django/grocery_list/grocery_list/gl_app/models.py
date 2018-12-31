from django.db import models
from django.utils import timezone


#This can be done with a single app called grocery_list and model called GroceryItem which contains a 
# text description, a created date, a completed date, and a boolean representing whether it was completed.

class GroceryItem(models.Model):
    name = models.CharField(max_length=32) #name of grocery item
    create_date = models.DateTimeField(default=timezone.now) #created date
    complete_date = models.DateTimeField(null=True, blank=True) #completed date
    done = models.BooleanField(default=False) #is completed?

    def __str__(self):  #returns the string representation of self name
        return self.name
