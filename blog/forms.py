from django import forms
from .models import Post

# Form to create a new blog post
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)