from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse  #<-- session change 1
from .models import Post
from nltk.corpus import wordnet as wn  # used by wordfinder
from .speller_web import WordFinder

# -------------------  #
#       BLOG           #
#----------------------#
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


def blog_list(request):
    #Use this on separate html link
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    return render(request, 'blog/blog_trial.html', {'posts':posts})


#----------------------------------#
# Experiment, language setting     #
#----------------------------------#
def language(request, language='en-gb'):  #<-- session change 5 change 6 in (urls.py)
    response = HttpResponse('setting language to: %s' % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language #<-- session change 9
    return response

## ============================  ##
##        Word Finder            ##
## ============================  ##

def get_definition(request):
    """
    Use nltk wordnet to check for a word in synsets
    If word is found in synsets, return first listed definition
    """
    result = "No result"
    if request.method == "GET":
        word = request.GET.get("get_word", None)
        syns = wn.synsets(word)
        if len(syns) > 0:
            result = syns[0].definition()
        else:
            result = "no result for word:" + word
    return render(request, "blog/re_definition.html", {'result': result, 'word': word})

def spell_checker(request):
    correction = " "
    error = " "
    alist = ['NONE']
    if request.method == "GET":
       arg = request.GET.get('user_input', None)
       wf = WordFinder()
       valid = wf.validate_string(arg)


       if arg != '' and valid:
           error, correction, alist = wf.get_suggestions(arg)
       else:
           correction = " Invalid input from user into text field. "

    return render(request, "blog/word_finder.html", {'correction' : correction, 'error': error, 'args': alist})

def word_finder(request):
    """
    Using the speller_web.py class WordFinder
    return a list of spelling suggestions if a word is misspelled
    or a message of 'correct', if the word is correct.
    """
    correction = " "
    error = " "
    alist = ["NONE"]
    if request.method == "GET":
        spell_checker(request)

    return render(request, "blog/word_finder.html", {'correction' : correction, 'error': error, 'args': alist})


