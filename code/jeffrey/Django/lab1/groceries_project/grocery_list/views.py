from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import Item

from .forms import GroceryForm


def index(request):
    template = loader.get_template('grocery_list/index.html')
    context = {
        "latest_grocery_list": Item.objects.all(),
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
            Item.objects.create(item_text=request.POST['name'], created_date=timezone.now())
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('grocery_list:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GroceryForm()

    return render(request, 'grocery_list/index.html', {'form': form})

# class EditView(generic.DetailView):
    # return HttpResponse('grocery_list:index')