from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book, Borrowing

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model, used for registration.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')

    def create(self, validated_data):
        # Creates a new user with an encrypted password.
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', '')
        )
        return user

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'isbn', 'is_available')

class BorrowingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Borrowing model.
    Includes nested book and user details for read operations.
    """
    book = BookSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source='book', write_only=True
    )

    class Meta:
        model = Borrowing
        fields = ('id', 'user', 'book', 'book_id', 'borrow_date', 'return_date')
        read_only_fields = ('user', 'borrow_date', 'return_date')