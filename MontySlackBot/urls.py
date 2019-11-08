
from django.conf.urls import url
from . import views


urlpatterns = [
    url('MontySlackBot', views.index),
    url('events', views.post),
]
