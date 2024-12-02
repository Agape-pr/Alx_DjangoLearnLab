
from django.urls import path
from .views import BookCreateView, BookListView, BookDeleteView, BookDetailView, BookUpdateView

urlpatterns = [
    path('books/create/',BookCreateView.as_view(), name = 'add_books' ),
    path('books/list/', BookListView.as_view(), name = 'list_books'),
    path('books/retrieve/<int:pk>/', BookDetailView.as_view(), name = 'search_book'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='update_book'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name= 'remove_book'),
]
