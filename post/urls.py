from django.urls import path
from post.views import *


urlpatterns = [
    path('login', loginPage, name="login"),
    path('register', registerPage, name="register"),
    path('logout', logoutPage, name="logout"),
    path('', index, name="home"),
    path('posts/', posts, name="posts"),
    path('post/create', create, name="create"),
    path('post/<int:id>', post_show, name="post.show"),
    path('post/<int:id>/update', post_update, name="post.update"),
    path('post/<int:id>/delete', post_delete, name="post.delete"),
    path('post/<slug:slug>', post_filter, name="post.tag")
]
