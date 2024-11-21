from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager

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
    books = models.ManyToManyField(Book, related_name= 'books')
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=30)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name= 'library')
    def __str__(self):
        return self.name
    
    
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')])
  
    def __str__(self):
        return f"{self.user.username} - {self.role}"

class UserProfile(models.Model):
    class Role(models.TextChoices):
        admin = "Admin"
        librarian = "Librarian"
        member = "Member"
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'userprofile')
    role = models.CharField(choices=Role, max_length=10, default=Role.member)
    
    def __str__(self) -> str:
        return f"{self.user.username}'s profile. Role: {self.role}"
    
    
   

# relationship_app/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    
    


    
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
    def create(self, username, password):
        user = self.create_user(username, password)
        user.is_stuff = True
        user.is_superuser = True
        user.save()

