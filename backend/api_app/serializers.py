from rest_framework import serializers
from api_app.models import Book
 
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id','book_title','book_author','published_date']