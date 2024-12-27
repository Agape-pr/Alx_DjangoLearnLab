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
from .models import Post , Comment
from .forms import PostForm, CommentForm
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
    template_name = "blog/listing.html"
    
    
    
class PostDetailView(DetailView):
    model = Post
    template_name ="blog/viewing.html"
    context_object_name = "post"
    
    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = self.object
                comment.author = request.user   
                comment.save()
                return redirect('post_details', pk=self.object.pk)
            
        else:
            return redirect('login')
                
    
    
    

    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/creating.html"
    #success_url = reverse_lazy('post_detail', pk = self.object.pk )
   # return redirect('detail_view', )
    
    def form_valid(self, form):
        self.object = self.get_object
        form.instance.author = self.request.user
        post = form.save()  # Save the post
        #return super().form_valid(form)
        return redirect('post_detail', pk=post.pk)
        

   

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/editing.html"
    success_url = reverse_lazy("all_post")
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "blog/deleting.html"
    success_url = reverse_lazy('all_post')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
  
  
class CommentView(ListView):
    model = Comment
    template_name = "blog/viewing.html"
    

