from django.db import models

# Create your models here.
class Library(models.Model):
    Book_Name = models.CharField(max_length=100)
    Description = models.TextField(blank=True)
    Language = models.CharField(max_length=100)
    Book_Author = models.CharField(max_length=100)

    def __str__(self):
        return self.Book_Name
