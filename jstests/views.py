from django.shortcuts import render



def run_app(request):
    return render(request, 'JSindex.html')
