from django import forms
from .models import AppyModel


class TenantForm(forms.Form):
    first_name = forms.CharField()


