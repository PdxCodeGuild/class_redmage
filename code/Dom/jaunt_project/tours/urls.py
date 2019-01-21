from django.urls import path
from . import views

app_name= "tours"
urlpatterns = [
  path('new/', views.tour_proposal, name='tours_new'),
  path('<int:pk>/', views.TourView.as_view(), name='tours_detail'),

]