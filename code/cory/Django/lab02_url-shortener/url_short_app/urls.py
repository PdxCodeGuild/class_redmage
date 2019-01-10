from django.urls import path
from . import views

app_name = "url_short"

urlpatterns = [
    path('', views.index, name="index"),
    path('redirect/<str:code>/', views.redirect, name="redirect"),
    path('<int:pk>/delete/', views.delete, name="delete")
]
