from django import forms
from .models import GroceryItem

class GroceryForm(forms.ModelForm):

    class Meta:
        model = GroceryItem
        fields = "item_text"