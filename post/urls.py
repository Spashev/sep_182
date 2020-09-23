from django.urls import path
from post.views import *


urlpatterns = [
    path('login', loginPage, name="login"),
    path('register', registerPage, name="register"),
    path('logout', logoutPage, name="logout"),
    path('', IndexView.as_view(), name="home"),
    path('posts/', PostListView.as_view(), name="posts"),
    path('post/create', PostCreateView.as_view(), name="create"),
    path('post/<int:id>', PostDetailView.as_view(), name="post.show"),
    path('post/<int:id>/update', PostUpdateView.as_view(), name="post.update"),
    path('post/<int:id>/delete', PostDeleteView.as_view(), name="post.delete"),
    path('post/<slug:slug>', PostFilterView.as_view(), name="post.tag")
]
