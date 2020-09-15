from django.shortcuts import render
from django.http import HttpResponse 
from post.models import Post

def index(request):
    return render(request, 'post/index.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'post/posts.html', {'posts':posts})

def post_show(reqeust, id):
    post = Post.objects.get(pk=id)
    return render(reqeust, 'post/show.html', {'post':post})