from django import forms

class GroceryItem(forms.Form):
    newItem = forms.CharField(label="New grocery item", max_length=50)