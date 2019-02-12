from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [ #gosterilecek alanlarin sirasi
            'title',
            'content',
            'image',
        ]