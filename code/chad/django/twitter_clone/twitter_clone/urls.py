from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from tweet_app.views import tweet_list_view

app_name = 'tweet_app'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('', include('tweet_app.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),

]
