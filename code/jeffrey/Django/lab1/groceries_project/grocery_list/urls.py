from django.urls import path

from grocery_list import views

app_name = "grocery_list"

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.AddView, name='AddView'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('obtain/<int:pk>/', views.obtain, name='obtain')
]