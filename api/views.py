from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, BookSerializer
from .models import Book


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
