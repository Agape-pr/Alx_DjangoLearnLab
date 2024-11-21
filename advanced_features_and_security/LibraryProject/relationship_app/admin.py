from django.contrib import admin
from .models import UserProfile, CustomUser
from django.contrib.auth.admin import UserAdmin

from django.contrib import admin
from .models import Author, Book, Librarian, Library, UserProfile, CustomUser

# Define a custom admin class to control how models appear in the admin interface
class RelationAdmin(admin.ModelAdmin):
    # Customize the list display for the admin panel
    list_display = ('name',)  # Modify fields to match each model (e.g., 'title' for Book)
    search_fields = ('name',)  # Enable search by name
    list_filter = ('name',)  # Add filters to narrow down the list

# Register each model with the custom RelationAdmin class
@admin.register(Author)
class AuthorAdmin(RelationAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(RelationAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author_name')
    list_filter = ('author',)

@admin.register(Librarian)
class LibrarianAdmin(RelationAdmin):
    list_display = ('name', 'library')
    search_fields = ('name', 'library_name')
    list_filter = ('library',)

@admin.register(Library)
class LibraryAdmin(RelationAdmin):
    list_display = ('name',)
    search_fields = ('name', 'books')

@admin.register(UserProfile)
class UserProfileAdmin(RelationAdmin):
    list_display = ("role", "user")
    list_filter = ('role',)


# Register your models here.


    
admin.site.register(CustomUser)