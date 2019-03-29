from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('language', views.language, name='SET_language'),  #<-- session change 6
    path('blog', views.blog_list, name='blogger'),
    path('wiwa', views.wiwa_page, name='wiwa'),
    path('wiwa_respond', views.wiwa_answer, name='responses'),
    re_path(r'^language/(?P<language>[a-z\-]+)/$', views.language, name="re-matchSETlanguage"), #<---session change 10
    path('rm_background', views.remove_bg, name='rm_background'),
    path('add_image', views.bg_replace, name="add_image"),
    path('blog/find_word', views.spell_checker, name="word_finder"),
    path('blog/word_finder', views.word_finder, name="word_finder_page"),

]
