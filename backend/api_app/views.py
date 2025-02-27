from django.shortcuts import render
from rest_framework import viewsets
from api_app.models import Book
 
from api_app.serializers import BookSerializer
 
class BookViewSet(viewsets.ModelViewSet):
    queryset= Book.objects.all()
    serializer_class = BookSerializer