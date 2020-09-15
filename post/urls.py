from django.urls import path
from post.views import *
urlpatterns = [
    path('', index, name="home"),
    path('posts/', posts, name="blogs"),
    path('post/<int:id>', post_show, name="post.show")
]
