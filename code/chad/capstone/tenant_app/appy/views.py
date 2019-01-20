from django.shortcuts import render
from .forms import TenantForm
from .models import AppyModel
from django.http import HttpResponse
from django.views.generic import View
from appy.utils import render_to_pdf
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class TenantAppys(LoginRequiredMixin, generic.ListView):
    model = AppyModel
    template_name = 'tenant_apps.html'

    def get_queryset(self):
        return


@login_required
def tenant_create_form_view(request):
    tenant_form = TenantForm()
    if request.method == 'POST':
        print(request.user)

        tenant_form = TenantForm(request.POST)
        if tenant_form.is_valid():
            tenant_form.save(tenant_form.author_id = request.user)
            
            print(tenant_form.cleaned_data)
            AppyModel.objects.create(**tenant_form.cleaned_data)

        else:
            print(tenant_form.errors)
    context = {
        'form': tenant_form
    }

    return render(request, 'fill_appy.html', context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('fill_appy.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('fill_appy.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")