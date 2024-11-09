from .models import Author, Library


book = Author.objects.filter(name = 'agape')
books = Library.objects.all()
libraryp = Library.objects.get(name = 'name')
