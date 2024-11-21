from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display =  ('title', 'author', 'publication_year')
    list_filter = ['title']
    search_fields = ('title', 'author')
    
admin.site.register(Book, BookAdmin)
# Register your models here.