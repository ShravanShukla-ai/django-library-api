from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    """
    Represents a book in the library.
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Borrowing(models.Model):
    """
    Represents a record of a user borrowing a book.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowings')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowings')
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        # Ensures a user cannot borrow the same book multiple times if it hasn't been returned
        unique_together = ('user', 'book', 'return_date')

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
