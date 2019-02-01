from django.urls import path

from . import views

app_name='grocerylist'
urlpatterns = [
  path('', views.IndexView.as_view(), name="index"),
  path('addItem/', views.addItem, name="addItem"),
  path('completedItem/', views.completedItem, name="completedItem")
]