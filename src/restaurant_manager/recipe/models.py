from django.db import models
from products.models import Product
from units.choices import RECIPE_UNITS

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    ingredients = models.ManyToManyField(Product, through='RecipeItem', related_name='recipes')

    def __str__(self):
        return self.recipe_name

class RecipeItem(models.Model):
    item_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=50, choices=RECIPE_UNITS)

    def __str__(self):
        return f"{self.quantity} {self.units} of {self.item_name.product_name} for {self.recipe.recipe_name}"