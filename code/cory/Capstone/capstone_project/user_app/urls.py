from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.NewUserView.as_view(), name="create-new-user"),
]