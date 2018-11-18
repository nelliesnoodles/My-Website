from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    return render(request, 'blog/under_construction.html', {})

def blog_list(request):
    #Use this on separate html link
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/blog_trial.html', {'posts':posts})
