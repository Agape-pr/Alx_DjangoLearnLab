from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
    def clean(self):
        content = self.cleaned_data.get('content')
        if len(content)<20:
            raise forms.ValidationError("the comment should not exceeds the 300 characters")
        
        return content
    