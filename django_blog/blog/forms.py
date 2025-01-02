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
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        if content and len(content) < 20:
            raise forms.ValidationError("The comment should not be less than 20 characters.")
        return cleaned_data
        
    