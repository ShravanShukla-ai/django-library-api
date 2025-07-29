from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BorrowingHistoryViewSet, UserCreateAPIView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'history', BorrowingHistoryViewSet, basename='borrowing-history')

# The API URLs are now determined automatically by the router.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('', include(router.urls)),
]
