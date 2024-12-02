
from django.urls import path
from .views import BookCreateView, BookListView, BookDeleteView, BookDetailView, BookUpdateView

urlpatterns = [
    path('add/',BookCreateView.as_view(), name = 'add_books' ),
    path('list/', BookListView.as_view(), name = 'list_books'),
    path('retrieve/<int:pk>/', BookDetailView.as_view(), name = 'search_book'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update_book'),
    path('remove/<int:pk>/', BookDeleteView.as_view(), name= 'remove_book'),
]
