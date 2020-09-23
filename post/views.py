from django.shortcuts import render, redirect
from post.models import Post, Tag
from post.forms import PostForm, UserForm
from django.urls import reverse_lazy

#Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#CBS(class based view)
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

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

# @login_required(login_url="login")
# def index(request):
#     return render(request, 'post/index.html')
class IndexView(TemplateView):
    template_name = 'post/index.html'

# @login_required(login_url="login")
# def posts(request):
#     tags = Tag.objects.all()
#     posts = Post.objects.filter(status = 'pub')
#     return render(request, 'post/posts.html', {'posts':posts, 'tags': tags})
class PostListView(ListView):
    template_name = "post/posts.html"
    model = Post 
    # queryset = Post.objects.all()
    # context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["posts"] = Post.objects.all()
        return context
    
# @login_required(login_url="login")
# def create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts')
#     form = PostForm()
#     return render(request, 'post/create.html', {'form': form})
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/create.html'
    success_url = reverse_lazy('posts')
    # fields = "__all__"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# @login_required(login_url="login")
# def post_filter(request, slug):
#     tag_slug = Tag.objects.get(slug=slug)
#     posts = tag_slug.post_set.all()
#     context = {
#         'posts': posts,
#         'tags': Tag.objects.all()
#     }
#     return render(request, 'post/posts.html', context=context)
class PostFilterView(ListView):
    model = Post
    template_name = 'post/posts.html'

    def get_context_data(self, **kwargs):
        context = super(PostFilterView, self).get_context_data(**kwargs)
        context["tags"] = Tag.objects.all() 
        slug = self.kwargs.get('slug', None)
        tag = Tag.objects.get(slug=slug)
        context['posts'] = tag.post_set.all()
        return context
    

# @login_required(login_url="login")
# def post_show(reqeust, id):
#     post = Post.objects.get(pk=id)
#     return render(reqeust, 'post/show.html', {'post':post})
class PostDetailView(DetailView):
    template_name = 'post/show.html'
    model = Post
    pk_url_kwarg = 'id'

# @login_required(login_url="login")
# def post_update(request, id):
#     post = Post.objects.get(id=id)
#     if request.method == "POST":
#         print(request.POST, request.FILES)
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('posts')
#     form = PostForm(instance=post)
#     return render(request, 'post/post_update_form.html', {'form': form})
class PostUpdateView(UpdateView):
    template_name = 'post/post_update_form.html'
    model = Post
    form_class = PostForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('posts')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# @login_required(login_url="login")
# def post_delete(request, id):
#     post = Post.objects.get(pk=id)
#     post.delete()
#     return redirect('posts')
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    pk_url_kwarg = 'id'

    def get(self, *args, **kwargs):
        print(args, kwargs)
        return self.post(*args, **kwargs)