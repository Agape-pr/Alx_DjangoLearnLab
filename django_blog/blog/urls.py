from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import registration, profile_view, home_view,post_view, logout_success_view,custom_logout, ChangeEmailView




urlpatterns = [
    path('register/',registration, name = 'register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
   
    path('profile/',profile_view, name='profile'),
    path('home/', home_view, name='home'),
    path('posts/', post_view, name='posts' ),
    path('logout/',custom_logout, name='logout'),
    path('logout_success/',logout_success_view, name='logout_success'),
    path('profileupdate/', ChangeEmailView.as_view(), name='profileupdate')
]

