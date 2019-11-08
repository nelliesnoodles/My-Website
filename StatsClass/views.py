from django.shortcuts import render

def index(request):
    #landing page for stat's class
    return render(request, 'stats_index.html')
