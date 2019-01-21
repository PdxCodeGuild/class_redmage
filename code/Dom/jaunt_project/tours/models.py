from django.db import models
from django.urls import reverse
from users.models import CustomUser
from artist_profile.models import ArtistProfile, ArtistImage

class Tour(models.Model):
  artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE)
  tour_name = models.CharField(max_length= 200)
  performers = models.CharField(max_length= 200)
  # the asking price for the tour
  guarantee = models.IntegerField()
  # check boxes in form 
  door_split = models.BooleanField(default=False)
  hotel_needed = models.BooleanField(default= False)
  # will be represented as ranges in drop down
  venue_size = models.CharField(max_length= 20)
  #estimate of when tour will start and end
  date_start = models.DateField()
  date_end = models.DateField()
  # will be represented in drop down with different regions  ie (NW, Cal, SW, South, MidWest, NE)
  region = models.CharField(max_length= 10) 
  #ability to add a tour poster to the proposal 
  tour_pic= models.IntegerField(null=True, blank=True)

  def __str__(self):
    return self.tour_name
  
  def get_absolute_url(self):
        return reverse('home')


class Venue(models.Model):
  name = models.CharField(max_length= 30)
  capacity = models.IntegerField()
  address= models.CharField(max_length = 200)
  city = models.CharField(max_length= 20)
  state = models.CharField(max_length = 2)
  region = models.CharField(max_length = 10)
  