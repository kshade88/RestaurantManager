from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    # detail_type = models.CharField(max_length=100, null=True, blank=True, default='None')

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.product_name