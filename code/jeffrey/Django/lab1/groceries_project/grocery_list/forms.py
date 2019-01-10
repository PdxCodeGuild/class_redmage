from django import forms
from django.utils import timezone
from grocery_list.choices import *

class GroceryForm(forms.Form):
    name = forms.CharField(label="New grocery item", max_length=32)
    quantity = forms.ChoiceField(choices=QUANTITY_CHOICES,initial='',widget=forms.Select(),required=True)
    obtained=forms.BooleanField(required=False)