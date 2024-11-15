## Delete Operation

### Command

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by retrieving all books
books = Book.objects.all()
print("Books in database:", list(books))