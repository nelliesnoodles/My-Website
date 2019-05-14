from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('language', views.language, name='SET_language'),  #<-- session change 6
    path('blog', views.blog_list, name='blogger'),
    re_path(r'^language/(?P<language>[a-z\-]+)/$', views.language, name="re-matchSETlanguage"), #<---session change 10
    path('blog/find_word', views.spell_checker, name="word_finder"),
    path('blog/word_finder', views.word_finder, name="word_finder_page"),
    path('re_definition', views.get_definition, name="re_definition"),

]
