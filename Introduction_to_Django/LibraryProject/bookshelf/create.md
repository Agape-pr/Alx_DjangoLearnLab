## Create Operation

### Command
```python
from myapp.models import Book
book1 = Book.objects.create(title='1984',author='George Orwell',publication_year=1949)
print(book1)
Book object (2)
#successful creation