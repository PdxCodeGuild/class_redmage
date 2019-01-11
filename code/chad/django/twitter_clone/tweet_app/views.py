from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import TwitterModel


class tweet_list_view (ListView):
    model = TwitterModel
    template_name = 'home.html'
    fields = ['tweet_text']


class tweet_detail_view(DetailView):
    model = TwitterModel
    template_name = 'tweet_detail_view.html'

