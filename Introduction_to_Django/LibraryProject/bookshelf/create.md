## Create Operation

### Command
```python
from myapp.models import Book
book1 = Book.objects.create(title='Rich dad, poor dad',author='Robert Kiyosaki',publication_year=1990)
print(book1)
Book object (2)
#successful creation