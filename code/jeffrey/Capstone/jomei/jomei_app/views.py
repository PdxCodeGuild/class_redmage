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

def index(request):
    template = loader.get_template("home.html")

    if request.user.is_anonymous:
        pass
    else:
        data = list(Point.objects.values().filter(owner = request.user))
        print(data)
        print(type(data))

    context = {
        "data":data,
    }

    return HttpResponse(template.render(context, request))

@csrf_exempt
def newMarker(request):
    coordinates = json.loads(request.body.decode('utf-8'))
    Point.objects.create(
        owner = request.user,
        name="",
        tag="test",
        latitude=coordinates['lat'],
        longitude=coordinates['lng'],
        distance_away=coordinates['distance_away'],
        # layer="test"
        )

    return HttpResponse('New marker created successfully!')

def deleteMarker(request, pk):
    if request.method == 'POST':
        tbd = Point.objects.get(pk=pk)
        tbd.delete()
        return HttpResponseRedirect(reverse('jomei_app:index'))
    else:
        return HttpResponseRedirect(reverse('jomei_app:index'))