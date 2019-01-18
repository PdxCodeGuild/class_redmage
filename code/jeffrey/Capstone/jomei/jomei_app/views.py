from django.shortcuts import render_to_response,render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User, AnonymousUser

from django.core import serializers

from .models import Point

import itertools

class HomeView(ListView):
    template_name = "home.html"

    context_object_name = "marker_data_for_js"


    def get_queryset(self):
        if self.request.user.is_anonymous:
            pass
        else:
            data = list(Point.objects.values().filter(owner = self.request.user))
            # data_dict = {x for x in data}
            # print(data_dict)
            print(data)
            print(type(data))
            print(self.get_context_object_name)
            # data_list = list(data)
            return data

class AboutView(TemplateView):
    template_name = "about.html"

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