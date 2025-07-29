from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Setup for Swagger/ReDoc documentation
schema_view = get_schema_view(
   openapi.Info(
      title="Library Management API",
      default_version='v1',
      description="API for managing books and borrowings in a library.",
      contact=openapi.Contact(email="contact@library.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# This is the corrected urlpatterns list
urlpatterns = [
    path('admin/', admin.site.urls),

    # API URLs
    path('api/', include('api.urls')),

    # JWT Token Authentication URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API Documentation URLs
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
