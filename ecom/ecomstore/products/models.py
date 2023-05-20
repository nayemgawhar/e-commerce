from django.db import models

from categorys.models import Category

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # this is the image for a product, the image will be uploaded to images folder
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # this is the string representation
    # what to display after querying
    def __str__(self):
        return f'{self.title}'

    # this will order the products by date created
    class Meta:
        ordering = ['-created_at']
