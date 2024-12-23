from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser

from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import logout

from .api.serializer import ChangeEmailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

    


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('profile')
       
            
    else:
        form = CustomUserCreationForm()
    return render(request,'blog/register.html', {'form' : form})

def profile_view(request):
    return render(request,'blog/profile.html')

def home_view(request):
    return render (render,'blog/home.html')

  
def post_view(request):
    return render(request,'blog/post.html')  

def custom_logout(request):
    logout(request)
    return redirect('logout_success')

def logout_success_view(request):
    return render(request,'blog/logs.html')   

  
class ChangeEmailView(generics.UpdateAPIView):
    serializer_class = ChangeEmailSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
