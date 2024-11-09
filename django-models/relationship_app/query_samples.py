from .models import Author, Library


objects.filter(author=author)
Author.objects.get(name=author_name)

books = Library.objects.all()
Library.objects.get(name=library_name)
books.all()

Library.objects.get(Library="
