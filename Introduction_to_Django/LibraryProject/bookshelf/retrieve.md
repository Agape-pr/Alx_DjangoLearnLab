# Retrieve all books
books = Book.objects.all()

# Display all attributes of each book
for book in books:
    print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")