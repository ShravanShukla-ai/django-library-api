from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from .models import Book, Borrowing
from .serializers import BookSerializer, BorrowingSerializer, UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    Accessible by anyone.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    - `list`: Returns all books.
    - `retrieve`: Returns a single book.
    - `create`, `update`, `destroy`: Admin-only actions (or for authenticated users).
    - `borrow`: Allows a user to borrow an available book.
    - `return_book`: Allows a user to return a borrowed book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # More restrictive permissions can be set here if needed, e.g., IsAdminUser

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def borrow(self, request, pk=None):
        """
        Action to borrow a book.
        """
        book = self.get_object()
        if not book.is_available:
            return Response({'error': 'This book is not available.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if user already has an active borrowing for this book
        if Borrowing.objects.filter(book=book, user=request.user, return_date__isnull=True).exists():
            return Response({'error': 'You have already borrowed this book.'}, status=status.HTTP_400_BAD_REQUEST)

        Borrowing.objects.create(book=book, user=request.user)
        book.is_available = False
        book.save()
        return Response({'status': 'Book borrowed successfully'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def return_book(self, request, pk=None):
        """
        Action to return a borrowed book.
        """
        book = self.get_object()
        try:
            borrowing = Borrowing.objects.get(book=book, user=request.user, return_date__isnull=True)
        except Borrowing.DoesNotExist:
            return Response({'error': 'You have not borrowed this book or it has already been returned.'}, status=status.HTTP_400_BAD_REQUEST)

        from django.utils import timezone
        borrowing.return_date = timezone.now().date()
        borrowing.save()
        book.is_available = True
        book.save()
        return Response({'status': 'Book returned successfully'}, status=status.HTTP_200_OK)


class BorrowingHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view borrowing history.
    Users can only see their own borrowing history.
    """
    serializer_class = BorrowingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the borrowings
        for the currently authenticated user.
        """
        user = self.request.user
        return Borrowing.objects.filter(user=user).order_by('-borrow_date')
