from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import GroceryItem

class IndexView(generic.ListView):
    template_name = 'grocery_app/index.html'
    context_object_name = 'grocery_list'

    def get_queryset(self):
        return GroceryItem.objects.all()

def new_grocery(request):
    grocery_text = request.POST['item_text']
    GroceryItem.objects.create(item_text=grocery_text)
    return HttpResponseRedirect(reverse('grocery_app:index'))