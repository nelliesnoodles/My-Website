from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse  #<-- session change 1
from .models import Post
#import nltk as nltk
#from nltk.corpus import wordnet
#import re
#import enchant
from .WW_online import Wiwa

def post_list(request):  #home page
    language = 'en-gb'   # <-- session change 2
    session_language = 'en-gb'  #<-- session change 2
    if 'lang' in request.COOKIES:  #<--session change 3
        language = request.COOKIES['lang']
    if 'lang' in request.session:  #<--session change 7
        session_language = request.session['lang']


    return render(request, 'blog/under_construction.html',
                 {'language': language,
                  'session_language' : session_language }) #<-- session change 8

def language(request, language='en-gb'):  #<-- session change 5 change 6 in (urls.py)
    response = HttpResponse('setting language to: %s' % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language #<-- session change 9
    return response

def blog_list(request):
    #Use this on separate html link
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    return render(request, 'blog/blog_trial.html', {'posts':posts})

def return_answer(arg):
    if arg != None and arg != '':
        try:
            wiwa = Wiwa()
            response = wiwa.run_wiwa(arg)
            if response:
                return response
            else:
                return "Something went wrong with Wiwa interface."
        except:
            broken = "Whispering wall is being modified or is broken."
            return broken
    else:
        no_words = "No search results to give."
        return no_words

def wiwa_page(request):
    return render(request, 'blog/wiwa_experiment.html', {})

def wiwa_answer(request):
    if request.method == "GET":
        user_input = request.GET.get('user_words', None)
        if user_input != None and len(user_input) > 0:
            if type(user_input) == list:
                user_input = ' '.join(user_input)
                answer = return_answer(user_input)
            else:
                answer = return_answer(user_input)


            return render(request, 'blog/wiwa_experiment.html', {'wiwa_answer' : answer})
        else:
            answer = "Not enough input for Whispering Wall to process"
            return render(request, 'blog/wiwa_experiment.html', {'wiwa_answer' : answer})
    else:
        answer = "No definition found -- No GET given"
        return render(request, 'blog/wiwa_experiment.html', {'wiwa_answer' : answer})
