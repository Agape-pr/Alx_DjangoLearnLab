from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.http import HttpRequest
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile



from django.shortcuts import render
from django.http import HttpResponseForbidden
def viewmodel(request):
    books = Book.objects.all()
    books_list= "\n".join([f"{book.title} by {book.author.name}"for book in books])  
    context = {"books_list" : books_list }
    return render(request, "relationship_app/list_books.html", context )

# Create your viewhere.

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        library = self.get_object() 
        context['books_in_library'] = library.books.all()
        
        return context
    

class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'



from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Admin view that only users with the 'Admin' role can access
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin(request):
    return render(request, 'admin_view.html')

# Librarian view that only users with the 'Librarian' role can access
@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Member view that only users with the 'Member' role can access
@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'member_view.html')





# Assuming you have a UserProfile model with a 'role' field
def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    # Your view logic here
    return render(request, 'admin_dashboard.html')
