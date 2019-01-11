from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from tweet_app.views import tweet_list_view, tweet_detail_view


app_name = 'tweet_app'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('', tweet_list_view.as_view()),
    path('post/<int:pk>/', tweet_detail_view.as_view(), name='post_detail'),

]

