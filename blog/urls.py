from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('blog', views.blog_list, name='blogger'),
    path('wiwa', views.wiwa_page, name='wiwa'),
    path('wiwa_respond', views.wiwa_answer, name='responses'),
]
