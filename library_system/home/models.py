from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Book (models.Model):
    Name = models.CharField(max_length=40)
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=15)
    availabilty = models.BooleanField(default=True)
    ISBN = models.CharField(max_length=15)
    Publish_year = models.DecimalField(max_digits=4,decimal_places=0)

    def __str__(self):
        return self.Name + ' | ' +self.author+ ' | '+self.category

    def get_absolute_url(self):
        return reverse('Home')





class Order (models.Model):
    UserName = models.CharField(max_length=16)
    BookName = models.CharField(max_length=20)
    Operation_needed = models.CharField(max_length=15)

    def __str__(self):
        return self.UserName+ ' | ' +self.BookName+ ' | '+self.Operation_needed

    def get_absolute_url(self):
        return reverse('Home')
