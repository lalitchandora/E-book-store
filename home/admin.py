from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Book


admin.site.site_header = 'Online Book Store' #changes the title of the admin page

class BookAdmin(admin.ModelAdmin):
    fields = ('title','price')
    list_filter = ('price')

admin.site.register(Book)
