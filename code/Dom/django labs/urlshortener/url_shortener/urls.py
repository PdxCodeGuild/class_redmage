from django.urls import path
from . import views


app_name = 'url_shortener'
urlpatterns = [
  path('', views.index, name = 'index'),
  path('<str:ShortUrl>/', views.redirector, name="redirector")
]
