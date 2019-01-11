from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import GroceryListModel
from django.urls import reverse
from django import forms


def index(request):
    gl_model_object = GroceryListModel.objects.all()
    print(gl_model_object[1])
    context = {'gl_name': gl_model_object}
    if request.method == 'POST':
        data = request.POST['add_item']
        GroceryListModel.objects.create(gc_item=data)
    return render(request, 'gl_app/index.html', context)



def delete_view(request, pk):
    book = get_object_or_404(GroceryListModel, pk=pk)
    book.delete()
    return HttpResponseRedirect(reverse('gl_app:home'))