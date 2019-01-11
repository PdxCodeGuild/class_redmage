from . import views
from django.urls import path


urlpatterns = [
    path('', views.add_form, name='add-form'),
    path('<str:url_path>/', views.short_path)
]
