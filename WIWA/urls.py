from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('WIWA', views.wiwa_page, name='WIWA'),
    path('wiwa_respond', views.wiwa_answer, name='responses'),
    path('rm_background', views.remove_bg, name='rm_background'),
    path('add_image', views.bg_replace, name="add_image"),

]
