from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import Group, User
admin.site.register(UserProfile)