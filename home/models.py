from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
	title = models.CharField(max_length = 50)
	genre = models.CharField(max_length = 10)
	language = models.CharField(max_length = 10)
	bookformat = models.CharField(max_length = 10)
	price = models.IntegerField()
	author = models.CharField(max_length = 30)
	page = models.IntegerField()
	description = models.TextField(default = '')
	book_image = models.ImageField(blank = True, upload_to = 'book/')

	def __str__(self):
		return self.title

		