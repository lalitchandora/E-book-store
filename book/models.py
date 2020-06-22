from django.db import models
from django.contrib.auth.models import User
from home.models import Book

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book_title = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        s = self.user.username + ", " + self.book_title.title
        return s

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book_title = models.ForeignKey(Book,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
