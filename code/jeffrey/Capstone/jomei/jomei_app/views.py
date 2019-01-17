from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Point

class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

@csrf_exempt
def newMarker(request):
    coordinates = json.loads(request.body.decode('utf-8'))
    Point.objects.create(
        name="test",
        tag="test",
        latitude=coordinates['lat'],
        longitude=coordinates['lng'],
        distance_away=coordinates['distance_away'],
        # layer="test"
        )

    return HttpResponse('string called empty string')