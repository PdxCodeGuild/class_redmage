from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from . forms import CustomUserCreationForm, CustomerUserChangeForm
from . models import CustomerUser


class CustomerUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomerUserChangeForm
    model = CustomerUser
    list_display = ['email', 'username', 'age', 'is_staff', ]


admin.site.register(CustomerUser, CustomerUserAdmin)


