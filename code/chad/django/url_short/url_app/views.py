from django.shortcuts import render, HttpResponseRedirect
from .forms import UrlForm
from .models import UrlModel
import random, string
from django.shortcuts import get_object_or_404


def make_shortlink():
    short_link = f'{random.randint(0,9)}{random.choice(string.ascii_letters)}{random.randint(0,9)}' \
        f'{random.choice(string.ascii_letters)}'
    return short_link


def add_form(request):
    short_link = make_shortlink()
    form = UrlForm(request.POST or None)

    if form.is_valid():
        # form.save()
        UrlModel.objects.create(url_short_path=short_link, url_long_path=form.cleaned_data['url_long_path'])
        return HttpResponseRedirect('/')

    data = UrlModel.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'home.html', context)

def short_path(self, url_path):
    print(url_path)
    x = get_object_or_404(UrlModel, url_short_path=url_path)
    return HttpResponseRedirect(f'{x.url_long_path}')











