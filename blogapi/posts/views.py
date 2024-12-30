# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView # genric views
from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly # built-in permissions
from.permissions import IsOwner
from rest_framework.viewsets import ModelViewSet 


# using generic views

# class PostCreateAPI(ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailsAPI(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsOwner]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class UserCreateAPI(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# using viewset

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



        

    




