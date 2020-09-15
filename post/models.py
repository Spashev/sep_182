from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    IS_PUBLISHED = [
        ('pub', 'published'),
        ('unpub', 'unpublished')
    ]
    title = models.CharField(max_length=150, verbose_name="Название поста")
    description = models.TextField(verbose_name="Описание поста")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=IS_PUBLISHED, default="unpub")
    created_at = models.DateTimeField(verbose_name="Дата создание", auto_now_add=timezone.now())