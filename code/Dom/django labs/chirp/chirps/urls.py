from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChirpListView.as_view(), name = 'home'),
    path('post/<int:pk>/', views.ChirpDetailView.as_view(), name = 'post_detail'),
    path('post/new/', views.ChirpCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/delete', views.ChirpDeleteView.as_view(), name='post_delete'),
]