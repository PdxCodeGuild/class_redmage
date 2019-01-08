from django.shortcuts import render
from django.http import HttpResponse
from django.view import generic
from django.utils import timezone

from .models import Item

from .forms import GroceryItem


class IndexView(generic.ListView):
    return HttpResponse("Hello, world. You're at the grocery_list index.")

