from django import forms
from django.utils import timezone

class GroceryForm(forms.Form):
    name = forms.CharField(label="New grocery item", max_length=32)
    quantity = forms.ChoiceField()
    created_date=timezone.now()
    completed_date=null
    obtained=forms.CheckboxInput()