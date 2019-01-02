from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Item

class IndexView(generic.ListView):
  template_name = 'grocerylist/index.html'
  context_object_name = "grocery_list_items"
  
  def get_queryset(self):
    return Item.objects.filter(completed = False).order_by('id')


def addItem(request):
  if request.method == "POST":
    item_text = request.POST["item_text"]
    qty = request.POST['qty']
    Item.objects.create(item_text= item_text, qty=qty, completed=False)
    # newItem.save()
  return HttpResponseRedirect(reverse('grocerylist:index'))

def completedItem(request):
  for item in Item.objects.filter(completed = False).order_by('id'):
    try:
      completed_item = Item.get_queryset.get(pk=request.POST["item_text"])
    except (KeyError, Item.DoesNotExist):
      return render(request, 'index.html',{
        "error_message" : "No items completed"
      })
    else:
      completed_item_completed = True
      completed_item.save()
      return HttpResponseRedirect(reverse('grocerylist:index'))
     
