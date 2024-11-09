# Retrieve all books
Book.objects.get(title=1984)
# Display all attributes of each book
for book in books:
    print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")