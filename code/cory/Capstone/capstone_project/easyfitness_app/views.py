from django.shortcuts import render

def indexView(request):
    return render(request, "home.html")