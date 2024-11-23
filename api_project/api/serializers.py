from rest_framework import serializers
from .models import Book

from django.contrib.auth import get_user_model


class BookSerializer(serializers.ModelSerializer):
    """This is a Book serializer class that converts information about Book objects
    into a workable format."""
    class Meta:
        model = Book
        fields = '__all__'

    

User = get_user_model()  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """A serializer for the available users in this project"""
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'groups']