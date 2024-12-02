from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

#view for createview
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticated]
    def perform_create(self, serializer):
        # Custom logic before saving (e.g., associating the current user with the book)
        serializer.save(created_by=self.request.user)
 
 
 
 
 
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = filters.CharFilter(field_name='author', lookup_expr='icontains')  # Filter by author's name
    publication_year = filters.NumberFilter(field_name='publication_year') # Filter by year       
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year'] 

# view for Listview
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = BookFilter  # Assign the custom filter class
    ordering_fields = ['publication_year', 'title']  # Specify the fields that can be ordered
    ordering = ['publication_year']
    search_fields = ['title', 'author']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes= [IsAuthenticated]
    def get_object(self):
        # Ensure that only the user who created the book can update it
        obj = super().get_object()
        if obj.created_by != self.request.user:  # Permission check
            raise PermissionDenied("You do not have permission to edit this book.")
        return obj
    
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    
