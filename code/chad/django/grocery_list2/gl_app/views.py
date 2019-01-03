from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryListModel
from django import forms


def index(request):
    gl_model_object = GroceryListModel.objects.all()
    context = {'gl_name': gl_model_object}
    if request.method == 'POST':

    return render(request, 'gl_app/index.html', context)



