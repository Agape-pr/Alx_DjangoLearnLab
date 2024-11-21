from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length= 30)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name= 'books')
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
        
    def __str__(self):
        return self.title
class Library(models.Model):
    name = models.CharField(max_length=40)
    books = models.ManyToManyField(Book, related_name= 'libraries')
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=30)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name= 'library')
    def __str__(self):
        return self.name
    
    

class UserProfile(models.Model):
    class Role(models.TextChoices):
        admin = "Admin"
        librarian = "Librarian"
        member = "Member"
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name= 'userprofile')
    role = models.CharField(choices=Role, max_length=10, default=Role.member)
    
    def __str__(self) -> str:
        return f"{self.user.username}'s profile. Role: {self.role}"
    
    
   


    


    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_photos/')



class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError("Users must have a username")
        if not password:
            raise ValueError("users must have a password") 
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user
    def create_superusers(self, username, password):
        user = self.create_user(username, password)
        user.is_stuff = True
        user.is_superuser = True
        user.save()

