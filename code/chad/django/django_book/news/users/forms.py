from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . models import CustomerUser

class CustomUserCreationForm(UserCreationForm):

        class Meta(UserCreationForm):
            model = CustomerUser
            fields = ('username', 'email', 'age',)


class CustomerUserChangeForm(UserChangeForm):

        class Meta:
            model = CustomerUser
            fields = ('username', 'email', 'age',)

