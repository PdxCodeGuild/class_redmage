from django.shortcuts import render_to_response,render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User, AnonymousUser
from django.utils.dateparse import parse_datetime

from django.core import serializers

from .models import Point

import itertools

from .forms import MarkerPopUpForm

class AboutView(TemplateView):
    template_name = "about.html"

class ExamplesView(TemplateView):
    template_name = "examples.html"

def index(request):
    template = loader.get_template("home.html")

    if request.user.is_anonymous:
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        user = request.user

        data_user = list(Point.objects.values().filter(owner = user))
        data_others = list(Point.objects.values().exclude(owner = user))


        context = {
            "data_user":data_user,
            "data_others":data_others
        }

        return HttpResponse(template.render(context, request))

@csrf_exempt
def newMarker(request):
    coordinates = json.loads(request.body.decode('utf-8'))
    Point.objects.create(
        owner = request.user,
        name=coordinates['name'],
        tag=coordinates['tag'],
        latitude=coordinates['lat'],
        longitude=coordinates['lng'],
        distance_away=coordinates['distance_away'],
        # layer="test"
        )

    return HttpResponse('New marker created successfully!')

@csrf_exempt
def deleteMarker(request, pk):
    if request.method == 'POST':
        tbd = Point.objects.get(pk=pk)
        tbd.delete()
        return HttpResponse('Marker deleted.')
    else:
        return HttpResponse('New Marker did not delete.')