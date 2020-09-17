from django.contrib import admin
from post.models import Post, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','description','status', 'author', 'created_at']
    list_filter = ('title','status', 'author', 'created_at')
    search_fields = ['title', "description"]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
