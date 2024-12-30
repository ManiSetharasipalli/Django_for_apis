from django.urls import path, include
# from .views import PostCreateAPI, PostDetailsAPI, UserCreateAPI   # Generic view APIs
from .views import PostViewSet, UserViewSet  # ViewSet APIs
from rest_framework.routers import DefaultRouter  # For dynamic routing
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Generic view routes (commented out for now)
# urlpatterns = [
#     path('posts/<int:pk>/', PostDetailsAPI.as_view(), name='post_details'),
#     path('posts/', PostCreateAPI.as_view(), name='post_create'),
#     path('token/', TokenObtainPairView.as_view(), name="get_token"),
#     path('token/refresh', TokenRefreshView.as_view(), name="get_refresh_token"),
#     path('register/', UserCreateAPI.as_view(), name='register')
# ]

# ViewSet router for dynamic routing
router = DefaultRouter()
router.register('posts', PostViewSet, basename="posts")  # Registering PostViewSet for posts endpoint
router.register('user', UserViewSet, basename="user")  # Registering UserViewSet for user endpoint

urlpatterns = [
    path('', include(router.urls)),  # Include the dynamic URL routes from the router
    # These endpoints are for JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name="get_token"),  # Endpoint to obtain a JWT token
    path('token/refresh', TokenRefreshView.as_view(), name="get_refresh_token")  # Endpoint to refresh the JWT token
]
