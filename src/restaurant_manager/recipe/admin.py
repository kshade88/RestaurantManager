from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeItem

admin.site.register(Recipe)
admin.site.register(RecipeItem)

