from django.shortcuts import render, redirect
from django.http import HttpResponse 
from post.models import Post, Tag
from post.forms import PostForm

def index(request):
    return render(request, 'post/index.html')

def posts(request):
    tags = Tag.objects.all()
    posts = Post.objects.filter(status = 'pub')
    return render(request, 'post/posts.html', {'posts':posts, 'tags': tags})

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = PostForm()
    return render(request, 'post/create.html', {'form': form})

def post_filter(request, slug):
    tag_slug = Tag.objects.get(slug=slug)
    posts = tag_slug.post_set.all()
    context = {
        'posts': posts,
        'tags': Tag.objects.all()
    }
    return render(request, 'post/posts.html', context=context)
def post_show(reqeust, id):
    post = Post.objects.get(pk=id)
    return render(reqeust, 'post/show.html', {'post':post})