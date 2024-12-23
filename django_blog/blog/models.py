from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser, BaseUserManager
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profilre')
    bio = models.TextField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
# Create your models here.

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError("email is required")
#         email = self.normalize_email(email=email)
#         user = self.model(email=email)
#         if not password :
#             raise ValueError("password is required")
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
        
#     def create_superuser(self, email,password=None):
        
#         user = self.create_user(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
    
    
# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(unique=False, max_length=10)
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#     objects = CustomUserManager()
    
    
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content  = models.TextField(max_length=500)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
   
