#django related imports
from django.shortcuts import render
from django.contrib.auth import get_user_model

#returning the default user model configured for this project
User = get_user_model()

#project imports
from .models import Book
from .serializers import BookSerializer, UserSerializer

#rest framework imports
from rest_framework import generics, viewsets, permissions, views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#create your views here
class BookList(generics.ListAPIView):
    """API endpoint to allow books to be viewed"""
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

#this class view is for performing creating model instances
class BookCreateSet(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#this class view for all crud operations
from rest_framework.authentication import TokenAuthentication

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class TokenObtainView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get or create a token for the authenticated user
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({
            "token": token.key,
            "created": created,  # True if the token was just created
        })
    
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         token, created = Token.objects.get_or_create(user=request.user)
    #         return Response({'token':token.key})
    #     else:  
    #         return super().post(request, *args, **kwargs)



class UserViewSet(viewsets.ModelViewSet):
    """Following Tutorials on REST page
        API EndPoint to allow users to be viewed or edited"""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly] 