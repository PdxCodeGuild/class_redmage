from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name="home"),
    path('post/user/<str:author>/', views.BlogUserView.as_view(), name="post_user"),
    path('post/new/', views.BlogCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/edit/', views.BlogEditView.as_view(), name="post_edit"),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name="post_delete"),
]
