from django.shortcuts import render



def run_app(request):
    return render(request, 'nim/ex5.html')