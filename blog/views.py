from django.shortcuts import render
from django.utils import timezone
from .models import Post
import nltk
from nltk.corpus import wordnet

def post_list(request):
    return render(request, 'blog/under_construction.html', {})

def blog_list(request):
    #Use this on separate html link
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    return render(request, 'blog/blog_trial.html', {'posts':posts})

def return_answer(arg):
    if arg != None and arg != '':
        alist = arg.split(' ')
        first = alist[0]
        syn = wordnet.synsets(first)
        if len(syn) != 0:
            defi_nition = (syn[0].definition())
            if len(defi_nition) == 0:
                no_words = "No results found in NLTK search"
                return no_words
            else:
                return defi_nition
        else:
            no_words = "No results found in NLTK search"
            return no_words
    else:
        no_words = "No search results to give."
        return no_words

def wiwa_page(request):
    return render(request, 'blog/wiwa_experiment.html', {})

def wiwa_answer(request):
    if request.method == "GET":
        user_input = request.GET.get('user_words', None)
        if len(user_input) > 0:
            alist = user_input.split(' ')
            search_word = alist[0]
            answer = return_answer(search_word)
            completed = search_word + ' : ' + answer
            return render(request, 'blog/wiwa_experiment.html', {'wiwa_answer' : completed})
        else:
            answer = "Not enough input for NLTK to process"
            return render(request, 'blog/wiwa_experiment.html', {'wiwa_answer' : answer})
    else:
        answer = "No definition found -- No GET given"
        return render(request, 'blog/wiwa_experiment.html', {'wiwa_answer' : answer})
