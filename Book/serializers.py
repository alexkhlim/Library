from django.contrib.auth.models import User

from .models import Book
from rest_framework.serializers import ModelSerializer

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'description', 'author']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username']