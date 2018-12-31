from django.urls import URLPattern, path, include
from . import views

app_name = 'grocery_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.new_grocery, name='create'),
]