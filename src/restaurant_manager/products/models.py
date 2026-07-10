from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.product_name