from django.forms import ModelForm 
from post.models import Post
from django.contrib.auth.models import User 

#Register user
from django.contrib.auth.forms import UserCreationForm


class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['author'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = 'Post title ..'
        self.fields['description'].widget.attrs['placeholder'] = 'Deescriptions ..'

    class Meta:
        model = Post
        verbose_name="Пост"
        fields = "__all__"

class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Username ..'
        self.fields['email'].widget.attrs['placeholder'] = 'Email ..'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password ..'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password ..'


    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']