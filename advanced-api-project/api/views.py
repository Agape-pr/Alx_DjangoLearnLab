from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
#view for createview
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticated]
    def perform_create(self, serializer):
        # Custom logic before saving (e.g., associating the current user with the book)
        serializer.save(created_by=self.request.user)
        
# view for Listview
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
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
    queryset = Book.objects.alll()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    
