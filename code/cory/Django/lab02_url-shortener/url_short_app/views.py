from django.shortcuts import render
from .models import UrlShortener
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from . import config

# Python Imports
import random
import string

def randomGenerator():
    random_letters = list(string.ascii_letters)
    outstring = ''
    for x in range(6):
        outstring += random.choice(random_letters)
    return outstring

def index(request):
    if request.method == "POST":
        new_url = request.POST["new_url"]
        short_url = randomGenerator()
        UrlShortener.objects.create(url=new_url, code=short_url)
        return HttpResponseRedirect(reverse('url_short:index'))
    if request.method == "GET":
        code = UrlShortener.objects.all()
        context = {
            'code': code
        }
        return render(request, 'url_short_app/index.html', context)

def redirect(request, code):

    def getIp(get_url):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')
        get_url.ip_address = ipaddress
        get_url.save()
    
    get_url = UrlShortener.objects.get(code=code)
    
    get_url.click_counter += 1
    
    # function
    getIp(get_url)

    get_url.save()

    # Used as full url for redirect
    long_url = str(get_url.url)

    # If website doesn't have a http(s), adds the // to let django know the site is elsewhere
    if 'http://' in long_url or 'https://' in long_url:
        return HttpResponseRedirect(long_url)
    else:
        long_url = '//' + long_url
        return HttpResponseRedirect(long_url)

def delete(request, pk):
    UrlShortener.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('url_short:index'))
    
