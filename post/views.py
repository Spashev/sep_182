from django.shortcuts import render, redirect
from post.models import Post, Tag
from post.forms import PostForm, UserForm

#Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'post/login.html')

def registerPage(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context =  {
        'form': form
    }
    return render(request, 'post/register.html', context=context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def index(request):
    return render(request, 'post/index.html')

@login_required(login_url="login")
def posts(request):
    tags = Tag.objects.all()
    posts = Post.objects.filter(status = 'pub')
    return render(request, 'post/posts.html', {'posts':posts, 'tags': tags})

@login_required(login_url="login")
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = PostForm()
    return render(request, 'post/create.html', {'form': form})

@login_required(login_url="login")
def post_filter(request, slug):
    tag_slug = Tag.objects.get(slug=slug)
    posts = tag_slug.post_set.all()
    context = {
        'posts': posts,
        'tags': Tag.objects.all()
    }
    return render(request, 'post/posts.html', context=context)

@login_required(login_url="login")
def post_show(reqeust, id):
    post = Post.objects.get(pk=id)
    return render(reqeust, 'post/show.html', {'post':post})

@login_required(login_url="login")
def post_update(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        print(request.POST, request.FILES)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts')
    form = PostForm(instance=post)
    return render(request, 'post/post_update_form.html', {'form': form})

@login_required(login_url="login")
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('posts')