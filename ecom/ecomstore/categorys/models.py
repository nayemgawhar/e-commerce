from django.db import models

# Create your models here.

# the category model with its fields


class Category(models.Model):
    name = models.CharField(max_length=200)
    tags = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # this is the string representation
    # what to display after querying
    def __str__(self):
        return f'{self.name}'

    # this will order the books by date created
    class Meta:
        ordering = ['-created_at']
