from django.shortcuts import render, redirect
from django.http import HttpResponse 
from post.models import Post
from post.forms import PostForm

def index(request):
    return render(request, 'post/index.html')

def posts(request):
    posts = Post.objects.filter(status = 'pub')
    return render(request, 'post/posts.html', {'posts':posts})

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = PostForm()
    return render(request, 'post/create.html', {'form': form})

def post_show(reqeust, id):
    post = Post.objects.get(pk=id)
    return render(reqeust, 'post/show.html', {'post':post})