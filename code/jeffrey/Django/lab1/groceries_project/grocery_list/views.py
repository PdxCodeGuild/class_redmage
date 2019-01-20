from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.template import loader
from django.urls import reverse

from .models import Item

from .forms import GroceryForm



def index(request):
    form = GroceryForm
    template = loader.get_template('grocery_list/index.html')
    context = {
        "latest_grocery_list": Item.objects.filter(obtained = False).order_by('name'),
        "in_basket_list": Item.objects.filter(obtained = True).order_by('quantity','completed_date').reverse(),
        "form":form
    }

    print(context)

    return HttpResponse(template.render(context, request))

def AddView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GroceryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            Item.objects.create(name=form.cleaned_data['name'],
            created_date=timezone.now(),
            completed_date=None,
            quantity=form.cleaned_data['quantity'],
            obtained=form.cleaned_data['obtained'])
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('grocery_list:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GroceryForm()

    return render(request, 'grocery_list/index.html', {'form': form})

def delete(request, pk):
    tbd = Item.objects.get(pk=pk)
    tbd.delete()

    return HttpResponseRedirect(reverse('grocery_list:index'))

def obtain(request, pk):
    tbo = Item.objects.get(pk=pk)

    if tbo.obtained:
        tbo.obtained=False
        tbo.completed_date=None
    else:
        tbo.obtained=True
        tbo.completed_date=timezone.now()
    tbo.save()

    return HttpResponseRedirect(reverse('grocery_list:index'))

# def obtain(request):
#     if request.POST.get('obtain'):

#     return HttpResponseRedirect(reverse('grocery_list:index'))