from rest_framework import serializers
from .models import  Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['id','username', 'password']
        read_only_feilds = ['id','username']

    def create(self, validated_data):
        user = User.objects.create_user(
            username  = validated_data['username'],
            password = validated_data['password']
        )    
        return user