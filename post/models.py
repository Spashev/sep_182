from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tag(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=200)
    created_at = models.DateTimeField(verbose_name="Дата создание", auto_now=True)

    def __str__(self):
        return f'Тег: {self.title}'

class Post(models.Model):
    IS_PUBLISHED = [
        ('pub', 'published'),
        ('unpub', 'unpublished')
    ]
    title = models.CharField(max_length=150, verbose_name="Название поста")
    description = models.TextField(verbose_name="Описание поста")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    image = models.ImageField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=IS_PUBLISHED, default="unpub")
    tag = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(verbose_name="Дата создание", auto_now_add=timezone.now())

    def __str__(self):
        return f"Посты: {self.title}"