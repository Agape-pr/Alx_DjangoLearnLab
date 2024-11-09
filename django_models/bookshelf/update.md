# Retrieve the book with the title "1984"
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"

# Save the changes to the database
book.save()

# Display the updated title to confirm
print(f"Updated Title: {book.title}")
#Updated Title: Nineteen Eighty-Four