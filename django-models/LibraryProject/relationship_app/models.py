from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length= 30)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name= 'books')
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
    
    






