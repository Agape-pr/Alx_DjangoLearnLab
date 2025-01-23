from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestyroAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    
    path('register/', UserListCreateView.as_view(), name='register'),
    path('login/',TokenObtainPairView.as_view, name='login-token'),
    path('profile/<int:pk>/', UserRetrieveUpdateDestyroAPIView.as_view(), name='profile'),
   

]
