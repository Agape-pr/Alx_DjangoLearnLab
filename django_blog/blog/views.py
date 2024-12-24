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
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post 
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    
class PostListView(ListView):
    model = Post
    template_name = "blog/view_all.html"
    
    
    
class PostDetailView(DetailView):
    model = Post
    template_name ="blog/detail.html"
    context_object_name = "post"
    
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/create_post.html"
    success_url = reverse_lazy('all_post') 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
   

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_update.html"
    success_url = reverse_lazy("all_post")
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "blog/post_delete_conf.html"
    success_url = reverse_lazy('all_post')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
