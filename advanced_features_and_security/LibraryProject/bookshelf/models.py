from django.db import models
from django.contrib.auth.models import AbstractUser
from  django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser, BaseUserManager
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
# Create your models here.

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_photos/')


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username :
            raise ValueError("Username is required")
        if not password :
            raise ValueError("password is required")
        user = self.model(username = username)
        user.set_passwod(password)
        user.save()
        return user
    def create_superuser(self,username, password):
        if not username :
            raise ValueError("username required")
        if not password :
            raise ValueError("Password is required")
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user