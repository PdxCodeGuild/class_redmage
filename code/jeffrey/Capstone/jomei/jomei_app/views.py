from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"