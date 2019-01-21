from django import forms
from django.forms import widgets
from . import models
from artist_profile.models import ArtistProfile
from users.models import CustomUser

VENUE_SIZE_CHOICES = [
  ( "30- 100", "SM (30- 100)"),
  ("101 - 300", "MD (101 - 300)"),
  ("301-600", "LG (301-600)")
]

REGION_CHOICES = [
  ("NW", "NorthWest"),
  ("CA", "California"),
  ("SW", "SouthWest"),
  
  ]

class CreateTour(forms.Form):
  
  artist = forms.ModelChoiceField(queryset= ArtistProfile.objects.all())
    
  tour_name = forms.CharField(
    max_length= 200, 
    label= "Tour Name",
    )
  performers = forms.CharField(
    max_length= 200
    )
  guarantee = forms.IntegerField(
    label="Guarantee $"
    )
  door_split = forms.BooleanField(required= False)
  hotel_needed = forms.BooleanField(required= False)
  venue_size = forms.CharField(
    widget=forms.Select( 
    choices=VENUE_SIZE_CHOICES)
    )
  date_start = forms.DateField(widget= forms.SelectDateWidget, label= "Start Date")
  date_end = forms.DateField(widget= widgets.SelectDateWidget, label= "End Date")
  region = forms.MultipleChoiceField(
    widget=forms.CheckboxSelectMultiple,
    choices=REGION_CHOICES)


 