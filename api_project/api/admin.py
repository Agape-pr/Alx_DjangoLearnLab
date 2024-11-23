from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    """This is the Book Model admin class
    it registers the Book model in the default django admin page so
    as to perform some ORM related operations.
    
    for now we will configure the list display, search and filter methods only"""

    list_display = ['title', 'author']
    search_fields = ['title', 'author']
    list_filter = ['title']

admin.site.register(Book, BookAdmin)