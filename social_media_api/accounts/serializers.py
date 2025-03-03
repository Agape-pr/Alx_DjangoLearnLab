from .models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True) 
    class Meta:
        
        model = CustomUser
        
        fields = ['id','username','bio','profile_picture','password']