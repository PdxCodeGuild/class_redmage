from django import forms
from django.utils import timezone

class MarkerPopUpForm(forms.Form):
    name = forms.CharField(label = "Marker name", max_length = 27, required = True)
    tags = forms.Textarea()
    layer = forms.BooleanField(label="Public", required=False)
