from django.shortcuts import render, redirect
from .forms import TenantForm, MaintForm
from .models import AppyModel, MaintyModel
from django.http import HttpResponse
from django.views.generic import ListView
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeTemplateView(ListView):
    model = AppyModel
    template_name = 'home.html'

@login_required
def tenant_create_form_view(request):
    tenant_form = TenantForm()
    items = AppyModel.objects.filter(author=request.user)
    print(items)
    if request.method == 'POST':
        print(request.user)

        tenant_form = TenantForm(request.POST)
        if tenant_form.is_valid():
            usr = request.user
            AppyModel.objects.create(**tenant_form.cleaned_data, author=usr)
            return redirect('home')
            print(tenant_form.cleaned_data)

        else:
            print(tenant_form.errors)
    context = {
        'tenant_form': tenant_form,
        'items': items,
    }

    return render(request, 'fill_appy.html', context)

@login_required
def mainty_form_view(request):
    maint_form = MaintForm()
    items = MaintyModel.objects.filter(author=request.user)
    if request.method == 'POST':
        print(request.user)
        maint_form = MaintForm(request.POST)
        if maint_form.is_valid():
            usr = request.user
            MaintyModel.objects.create(**maint_form.cleaned_data, author=usr)
            return redirect('home')
    context = {
        'maint_form': maint_form,
        'items': items,
    }
    return render(request, 'maint_request.html', context)

#reserved for a paged for apps created by user
@login_required
def tenant_apps_view(request):
    app_list = AppyModel.objects.filter(author=request.user).values_list('first_name')
    return render_to_response('tenant_apps.html', {'object_list': app_list})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

