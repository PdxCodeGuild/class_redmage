from django import forms
from django.forms import widgets
from . import models
from artist_profile.models import ArtistProfile
from users.models import CustomUser

VENUE_SIZE_CHOICES = [
  ( "50- 150", "SM (50- 150)"),
  ("151 - 500", "MD (151 - 500)"),
  ("500-1000", "LG (500-1000)")
]

REGION_CHOICES = [
  ("NorthWest", "NorthWest"),
  ("California", "California"),
  ("SouthWest", "SouthWest"),
  
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


  def __init__(self, user, *args, **kwargs):
    super(CreateTour, self).__init__(*args, **kwargs)
    self.fields['artist'].queryset = ArtistProfile.objects.filter(user=user)