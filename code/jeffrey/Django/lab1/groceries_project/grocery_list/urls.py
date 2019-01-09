from django.conf.urls import url

from grocery_list import views

app_name = "grocery_list"

urlpatterns = [
    url(r'^$', views.index, name='index'),

]