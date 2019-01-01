
from django.http import HttpResponse #For loading pure html without using a template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import GroceryItem
from django.urls import reverse


def index(request):
    template = loader.get_template('index.html')
    context = {
        'items': GroceryItem.objects.all()
    }
    grocery_text = request.POST['gcname']
    GroceryItem.objects.create(gcname=grocery_text)
    return HttpResponse(template.render(context, request))


