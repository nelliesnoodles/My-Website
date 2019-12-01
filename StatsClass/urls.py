from django.urls import path
from . import views

urlpatterns = [
    path('StatsClass', views.index),
    path('BasicProbability', views.basic_prob),
]
