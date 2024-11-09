from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.http import HttpRequest
from .models import Book
from .models import Library

def viewmodel(request):
    books = Book.objects.all()
    books_list= "\n".join([f"{book.title} by {book.author.name}"for book in books])  
    context = {"books_list" : books_list }
    return render(request, "relationship_app/list_books.html", context )

# Create your viewhere.

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        library = self.get_object() 
        context['books_in_library'] = library.books.all()
        
        return context