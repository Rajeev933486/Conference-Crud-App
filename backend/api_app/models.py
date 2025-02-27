from django.db import models
 
# Create your models here.
class Book(models.Model):
    book_id = models.BigAutoField(primary_key=True)
    book_title= models.CharField(max_length=50)
    book_author= models.CharField(max_length=50)
    published_date=models.DateField()
 
    def __str__(self):
        return self.book_title