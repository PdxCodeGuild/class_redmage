from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Shorten
import string
import random

# Create your views here.
def index(request):

  def generate_code():
    ShortUrl =""
    for char in range(0, 4):
      ShortUrl = ShortUrl + random.choice(string.ascii_lowercase)
    ShortUrl = ShortUrl + random.choice(string.ascii_uppercase) + random.choice(string.octdigits)
    ShortUrl = list(ShortUrl)
    random.shuffle(ShortUrl)
    ShortUrl = ("".join(ShortUrl))
    return ShortUrl

  if request.method == "GET":
    return render(request, 'url_shortener/index.html')
  if request.method == "POST":
    code = generate_code()
    url_text = request.POST["long_url"]
    shorten =Shorten(Url = url_text, ShortUrl = code)
    shorten.save()
    latest_Url = shorten
    context = {
      'latest_Url' : latest_Url,
    }
    return render(request,'url_shortener/index.html', context)

def redirector(request, ShortUrl):
  if request.method =="GET":
    address = get_object_or_404(Shorten, ShortUrl=ShortUrl)
    long_url = address.Url
    address.Xs_used += 1
    address.save()
    return HttpResponseRedirect(long_url)