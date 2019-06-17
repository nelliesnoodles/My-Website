from django.shortcuts import render


def index_page(request):
    return render(request, 'PreWork2019/prework.html')