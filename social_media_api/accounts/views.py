from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=self.request.user.id)
       
    
    # def list(self,request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer_data = self.get_serializer(queryset, many=True)
    #     return Response(serializer_data.data, status=status.HTTP_200_OK)
        
        
        
    def perform_create(self, serializer):
       user=  serializer.save()
       refresh = RefreshToken.for_user(user)
       return Response(
           {
               "refresh":str(refresh),
               "access":str(refresh.access_token),
               "user": UserSerializer(user).data
           },
           status=status.HTTP_201_CREATED
       )
        
        
class UserRetrieveUpdateDestyroAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset
        
        return CustomUser.objects.filter(id=self.request.user.id)
        
    