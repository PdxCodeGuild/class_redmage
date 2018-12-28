from django.shortcuts import render

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutUsPage(TemplateView):
    template_name = 'about_us.html'