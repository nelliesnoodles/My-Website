from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import random
from .WW_online import Wiwa
from nltk.corpus import wordnet as wn
from django.http import HttpResponse

import logging


log = logging.getLogger('logdna')
log.setLevel(logging.INFO)


# database not on my CPU

wiwa = Wiwa()

def get_preference(request): #used in Wiwa page
    if 'bg_preference' not in request.session:
        bg_string = "background-image: url('/static/images/pexels-brick.jpg'); background-repeat: no-repeat; background-size: 100% 100%; opacity: 0.95;"
        request.session['bg_preference'] = bg_string
        bg_preference = bg_string
    else:
        bg_preference = request.session['bg_preference']
    return bg_preference

def remove_bg(request):
    log.info("request to remove whispering wall background image")
    if 'bg_preference' not in request.session:
        bg_string = "background: black;"  #<-- change to something like blue to see definite change
        request.session['bg_preference'] = bg_string
    else:
        bg_string = 'background: black;' #<-- make sure you have what you want here.
        request.session['bg_preference'] = bg_string

    bg_preference = request.session['bg_preference']
    #print("bg preference changed to:", bg_preference)
    return render(request, 'WIWA/wiwa_experiment.html', {'bg_preference': bg_preference})

def bg_replace(request):
    if 'bg_preference' not in request.session:
        bg_string = "background-image: url('/static/images/pexels-brick.jpg'); background-repeat: no-repeat; background-size: 100% 100%; opacity: 0.95;"
        request.session['bg_preference'] = bg_string
        bg_preference = bg_string
    else:
        bg_string = "background-image: url('/static/images/pexels-brick.jpg'); background-repeat: no-repeat; background-size: 100% 100%; opacity: 0.95;"
        request.session['bg_preference'] = bg_string
        bg_preference = bg_string

    bg_preference = request.session['bg_preference']
    #print("bg preference changed to:", bg_preference)
    return render(request, 'WIWA/wiwa_experiment.html', {'bg_preference': bg_preference})

def reset_session(request):
    #print("setting session wiwa keys")
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
        #print('line_numb =', line_numb)
        #print('the_list = ', the_list)
        new_line = the_list[line_numb]
        #print('session item retrieved')
        #print('line_numb = ', line_numb)
        try:


            wiwa.line_get = new_line
            #print("****  getting wiwa_response *****")
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
    return render(request, 'WIWA/wiwa_experiment.html', {'bg_preference': bg_preference})

def wiwa_answer(request):
    if 'line_numb' not in request.session and 'list_index' not in request.session:
        reset_session(request)
    bg_preference = get_preference(request)
    if request.method == "GET":
        user_input = request.GET.get('user_words', None)
        # TODO: stop chatbot from responding to any GET that doesn't have user_input submitted.
        if user_input != None and len(user_input) > 0:
            #print("user_input ==," , user_input)
            if type(user_input) == list:
                user_input = ' '.join(user_input)
                answer = return_answer(user_input, request)
            else:
                answer = return_answer(user_input, request)
            print("answer ==", answer)
            if answer == 'wiwa: ':
                pass
            else:
                return render(request, 'WIWA/wiwa_experiment.html', {'wiwa_answer' : answer, 'bg_preference': bg_preference})
        else:
            answer = "Not enough input for Whispering Wall to process"
            return render(request, 'WIWA/wiwa_experiment.html', {'wiwa_answer' : answer, 'bg_preference': bg_preference})
    else:
        answer = "No definition found -- No GET given"
        return render(request, 'WIWA/wiwa_experiment.html', {'wiwa_answer' : answer, 'bg_preference': bg_preference})
