from django.forms import ModelForm 
from post.models import Post

class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['author'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = 'Post title ..'
        self.fields['description'].widget.attrs['placeholder'] = 'Deescriptions ..'

    class Meta:
        model = Post
        verbose_name="Пост"
        fields = "__all__"

