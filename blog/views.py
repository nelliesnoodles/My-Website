from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse  #<-- session change 1
from .models import Post
import random
from .WW_online import Wiwa
from .speller_web import WordFinder

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

def get_preference(request): #used in Wiwa page
    if 'bg_preference' not in request.session:
        bg_string = "background-image: url('/static/images/card_3.png'); background-repeat: no-repeat; background-size: 100% 100%; opacity: 0.85; font-family: Tahoma, Verdana, Segoe, sans-serif;"
        request.session['bg_preference'] = bg_string
        bg_preference = bg_string
    else:
        bg_preference = request.session['bg_preference']
    return bg_preference

def remove_bg(request):
    if 'bg_preference' not in request.session:
        bg_string = "background: #c3c2c4;"  #<-- change to something like blue to see definite change
        request.session['bg_preference'] = bg_string
    else:
        bg_string = 'background: #c3c2c4;' #<-- make sure you have what you want here.
        request.session['bg_preference'] = bg_string

    bg_preference = request.session['bg_preference']
    #print("bg preference changed to:", bg_preference)
    return render(request, 'blog/wiwa_experiment.html', {'bg_preference': bg_preference})

def bg_replace(request):
    if 'bg_preference' not in request.session:
        bg_string = "background-image: url('/static/images/card_3.png'); background-repeat: no-repeat; background-size: 100% 100%; opacity: 0.85; font-family: Tahoma, Verdana, Segoe, sans-serif;"
        request.session['bg_preference'] = bg_string
        bg_preference = bg_string
    else:
        bg_string = "background-image: url('/static/images/card_3.png'); background-repeat: no-repeat; background-size: 100% 100%; opacity: 0.85; font-family: Tahoma, Verdana, Segoe, sans-serif;"
        request.session['bg_preference'] = bg_string
        bg_preference = bg_string

    bg_preference = request.session['bg_preference']
    #print("bg preference changed to:", bg_preference)
    return render(request, 'blog/wiwa_experiment.html', {'bg_preference': bg_preference})

def reset_session(request):
    print("setting session wiwa keys")
    a_list = []
    session_keys = list(request.session.keys())
    if len(session_keys) > 1:
        for key in session_keys:
            if key == 'bg_preference':
                pass
            else:
                del request.session[key]
    for x in range(0, 24):
        a_list.append(x)

    random.shuffle(a_list)

    request.session['list_index'] = a_list
    request.session['line_numb'] = 0
    request.session.modified = True


def return_answer(arg, request):

    if request.session['line_numb'] > 22:
        reset_session(request)

    if arg != None and arg != '':
        line_numb = request.session['line_numb']
        the_list = request.session['list_index']
        print('line_numb =', line_numb)
        print('the_list = ', the_list)
        new_line = the_list[line_numb]
        print('session item retrieved')
        print('line_numb = ', line_numb)
        try:
            print('try block')
            wiwa = Wiwa()
            print('wiwa initiated')
            wiwa.line_get = new_line
            print("****  getting wiwa_response *****")
            response = wiwa.run_wiwa(arg)
            #print("response =", response)
            if response:
                request.session['line_numb'] += 1
                return response
            else:
                broken = "Wiwa's code is broken"
                return broken
        except:
            return "something is wrong with Wiwa's code."
    else:
        no_words = "that is not enough information"
        return no_words

def wiwa_page(request):
    reset_session(request)
    bg_preference = get_preference(request)
    return render(request, 'blog/wiwa_experiment.html', {'bg_preference': bg_preference})

def wiwa_answer(request):
    if 'line_numb' not in request.session and 'list_index' not in request.session:
        reset_session(request)
    bg_preference = get_preference(request)
    if request.method == "GET":
        user_input = request.GET.get('user_words', None)
        if user_input != None and len(user_input) > 0:
            if type(user_input) == list:
                user_input = ' '.join(user_input)
                answer = return_answer(user_input, request)
            else:
                answer = return_answer(user_input, request)


            return render(request, 'blog/wiwa_experiment.html', {'wiwa_answer' : answer, 'bg_preference': bg_preference})
        else:
            answer = "Not enough input for Whispering Wall to process"
            return render(request, 'blog/wiwa_experiment.html', {'wiwa_answer' : answer, 'bg_preference': bg_preference})
    else:
        answer = "No definition found -- No GET given"
        return render(request, 'blog/wiwa_experiment.html', {'wiwa_answer' : answer, 'bg_preference': bg_preference})

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


