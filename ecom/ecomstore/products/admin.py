from django.contrib import admin

# Register your models here.

# from the models.py file import Product
from .models import Product

# registering the Product to the admin site
admin.site.register(Product)

