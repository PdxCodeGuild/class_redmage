from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from .forms import CreateTour
from artist_profile.models import ArtistProfile, ArtistImage
from artist_profile.forms import ImageForm
from .models import Tour, Venue

def tour_proposal(request): 
  if request.method == "POST":
    form = CreateTour(request.POST)
    if form.is_valid():
      artist = form.cleaned_data["artist"]
      tour_name = form.cleaned_data["tour_name"]
      performers = form.cleaned_data["performers"]
      guarantee = form.cleaned_data["guarantee"]
      door_split = form.cleaned_data["door_split"]
      venue_size = form.cleaned_data["venue_size"]
      date_start = form.cleaned_data["date_start"]
      date_end = form.cleaned_data["date_end"]
      region = form.cleaned_data["region"]
      days = (date_end) - (date_start)
      print(days)
      tour = Tour(
        artist= artist,
        tour_name=tour_name, 
        performers =performers,
        guarantee = guarantee,
        door_split = door_split,
        venue_size = venue_size,
        date_start = date_start,
        date_end = date_end,
        region = region,
      )
      tour.save()
      form = CreateTour()
      return HttpResponseRedirect(reverse('tours:tours_detail', args=(tour.id,) ))
  elif request.method == "GET":
    form = CreateTour()
  return render(request, "tour_create.html", {'form': form} )
    
class TourView(LoginRequiredMixin, DetailView):
  model = Tour
  template_name = "tours_detail.html"


# class TourList(LoginRequiredMixin, ListView):


  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   if Tour.objects.get(pk= self.kwargs['pk']).profile_pic:
  #     profile_pic_id = ArtistProfile.objects.get(pk= self.kwargs['pk']).profile_pic
  #     context['profile_pic'] = ArtistImage.objects.get(pk= profile_pic_id)
  #     print(context['profile_pic'].image.url)
  #   return context


# def tourview(request):
#   return # detail view of the tour that shows tour and show search results

# def touredit(request):
#  return "place to edit the tour details  "