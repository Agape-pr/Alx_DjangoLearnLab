from .models import Author, Library


book = Author.objects.filter(name = 'agape')
books = Library.objects.all()
Library.objects.get(name=library_name)
books.all()
