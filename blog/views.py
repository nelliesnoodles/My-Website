from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse  #<-- session change 1
from .models import Post
import random
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

def get_preference(request): #used in Wiwa page
    if 'bg_preference' not in request.session:
        bg_string = "background-image: url('/static/images/unicorn4_12-22-18.png'); background-repeat: no-repeat; background-size: 100% 100%; opacity: 0.85; font-family: Tahoma, Verdana, Segoe, sans-serif;"
        request.session['bg_preference'] = bg_string
        bg_preference = bg_string
    else:
        bg_preference = request.session['bg_preference']
    return bg_preference

def remove_bg(request):
    if 'bg_preference' not in request.session:
        bg_string = "background: white;"  #<-- change to something like blue to see definite change
        request.session['bg_preference'] = bg_string
    else:
        bg_string = 'background: white;' #<-- make sure you have what you want here.
        request.session['bg_preference'] = bg_string

    bg_preference = request.session['bg_preference']
    #print("bg preference changed to:", bg_preference)
    return render(request, 'blog/wiwa_experiment.html', {'bg_preference': bg_preference})

def bg_replace(request):
    if 'bg_preference' not in request.session:
        bg_string = "background-image: url('/static/images/unicorn4_12-22-18.png'); background-repeat: no-repeat; background-size: 100% 100%; opacity: 0.85; font-family: Tahoma, Verdana, Segoe, sans-serif;"
        request.session['bg_preference'] = bg_string
        bg_preference = bg_string
    else:
        bg_string = "background-image: url('/static/images/unicorn4_12-22-18.png'); background-repeat: no-repeat; background-size: 100% 100%; opacity: 0.85; font-family: Tahoma, Verdana, Segoe, sans-serif;"
        request.session['bg_preference'] = bg_string
        bg_preference = bg_string

    bg_preference = request.session['bg_preference']
    #print("bg preference changed to:", bg_preference)
    return render(request, 'blog/wiwa_experiment.html', {'bg_preference': bg_preference})

def make_list():
    a_list = []
    for x in range(1, 22):
        a_list.append(x)
    random.shuffle(a_list)
    request.session['list_index'] = a_list

def return_answer(arg, request):
    if arg != None and arg != '':
        if 'line_numb' not in request.session:
            request.session['line_numb'] = 0

        if 'list_index' not in request.session:
            a_list = []
            for x in range(1, 21):
                a_list.append(x)
            random.shuffle(a_list)
            request.session['list_index'] = a_list


        try:


            wiwa = Wiwa() #
            #return "line 85"
            alist = request.session['list_index']
            #rep = str(alist)
            #return rep
            line_numb = request.session['line_numb']
            #return "line_numb, before if block"
            #astring = str(alist) + "line_numb =" + str(line_numb)
            #return astring
            if line_numb > 21:
                #return "if block"
                request.session['line_numb'] = 0
                line_numb = 0
                make_list()
                alist = request.session['list_index']
            #rep_2 = str(line_numb)
            #return rep_2
            new_line = alist[line_numb]
            #return new_line

            #wiwa.line_get = request.session['line_numb']
            wiwa.line_get = new_line
            #return new_line
            response = wiwa.run_wiwa(arg)
            if response:

                request.session['line_numb'] += 1
                cap = request.session['line_numb']
                if cap > 22:  #shortest script file is 22 lines
                    request.session['line_get'] = 0

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
    if 'line_numb' not in request.session:
        request.session['line_numb'] = 0
    bg_preference = get_preference(request)
    return render(request, 'blog/wiwa_experiment.html', {'bg_preference': bg_preference})

def wiwa_answer(request):
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
