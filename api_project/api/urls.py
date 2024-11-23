from django.urls import path, include
from .views import UserViewSet, BookList, BookCreateSet, BookViewSet, TokenObtainView

from rest_framework import routers




#to automatically determine the url path for our viewsets
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books_all', BookViewSet, basename='book_all')



urlpatterns = [
    #using the auto url path generator for user viewset??
    path('', include(router.urls)),

    #manually configuring my viewset with a class based view and determined url path
    path('books/', BookList.as_view(), name='book-list'),
    path('books/create/', BookCreateSet.as_view(), name='book-create'),

    #for authenticating users for the views, can also use default django login views 
    path('api-auth/', include('rest_framework.urls'), name= 'rest_framework'),

    path('token/', TokenObtainView.as_view(), name='tokens')
] 