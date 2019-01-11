from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Item
from .forms import ItemForm

def index(request):


    # A ValueError will be raised if the data in the form doesn’t validate – i.e., if form.errors evaluates to True.
    
    if request.method == 'POST':

        f = ItemForm(request.POST)

        tempitem = f.save(commit = False)

        if tempitem.completed:
            tempitem.complete_date = timezone.now()

        tempitem.save()

        return HttpResponseRedirect(reverse('index'))

    context = {
        "items": Item.objects.all(),
        "form": ItemForm
    }

    return render(request, 'groclist/index.html', context)
 
