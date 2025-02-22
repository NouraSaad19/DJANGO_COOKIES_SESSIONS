from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=512)
    desc = models.TextField()

    # To represent the model as a string
    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=124)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
