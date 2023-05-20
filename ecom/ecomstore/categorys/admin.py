from django.contrib import admin

# Register your models here.

# from the models.py file import Book
from .models import Category

# registering the Book to the admin site
admin.site.register(Category)
