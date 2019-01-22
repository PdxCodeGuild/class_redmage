from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.AboutView.as_view(), name = 'about'),
    path('newmarker/', views.newMarker, name = 'newmarker'),
    path('deletemarker/<int:pk>/', views.deleteMarker, name= 'deletemarker')
]