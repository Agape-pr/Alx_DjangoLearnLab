from django.db import models

# Create your models here.

class Book(models.Model):
    """This model maps to a database table with name Book as defined
    subclass meta.
    
    It has two attributes and these are:
        title a varchar field
        author a varchar field"""
    class Meta:
        db_table = 'book'
        ordering = ['title']


    title = models.CharField(max_length=100)
    author = models.CharField(max_length=55)

    def __str__(self) -> str:
        """Returns the title of a book obj"""
        return self.title
