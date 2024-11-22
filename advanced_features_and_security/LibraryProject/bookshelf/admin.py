from django.contrib import admin
from .models import Book, CustomUser


class BookAdmin(admin.ModelAdmin):
    list_display =  ('title', 'author', 'publication_year')
    list_filter = ['title']
    search_fields = ('title', 'author')
    
    
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth')
    
    
    
    
admin.site.register(Book, BookAdmin, CustomUserAdmin,CustomUser,)
# Register your models here.
