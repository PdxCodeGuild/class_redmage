from django.shortcuts import render
from .forms import TenantForm
from .models import AppyModel


def tenant_create_form_view(request):
    tenant_form = TenantForm()  #render with get method so you can see the form
    if request.method == 'POST':
        tenant_form = TenantForm(request.POST)  #Pass in the request data as you initialize the form
        if tenant_form.is_valid():
            print(tenant_form.cleaned_data)
            AppyModel.objects.create(**tenant_form.cleaned_data)
        else:
            print(tenant_form.errors)
    context = {
        'form': tenant_form
    }

    return render(request, 'fill_appy.html', context)



