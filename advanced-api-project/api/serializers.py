from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Author
        fields = ['name']


    #serialization for the relationship btn Book and Author models, named valiable , 
    # equate to the serializer class of the author class , define its two variable "many and read_only to True"
class BookSerializer(serializers.ModelSerializer):
        
    author_name = AuthorSerializer(many = True , read_only = True)
    class Meta:
        model = Book
        fields = '__all__' 
        def validate(self,data):
        # publication_yeaar < date.now or  publication_year = date.now
            if not (data['publication_year'] < datetime.now().year or data['publication_year'] == datetime.now().year ):
                raise serializers.ValidationError("Year should be current year")
            return data
            
        
    