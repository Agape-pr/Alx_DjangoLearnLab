from .models import Book, Library
from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
    path('book/', views.viewmodel,name = 'bookd' ),
    path('library/', LibraryDetailView.as_view(), name = 'list' )
]
