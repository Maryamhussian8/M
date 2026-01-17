from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Course API Documentation",
        default_version='v1',
        description="",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),

    #APIs endpoints
    path('api/', include('courses.api_urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),       
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),     
    #path('api/auth/social/', include('allauth.socialaccount.urls')),  #for Google login
    path('api/auth/', include('dj_rest_auth.urls')),  # login, logout, password change
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('chaining/', include('smart_selects.urls')),
    # Frontend pages
    path('', include('courses.front_urls')),
]
