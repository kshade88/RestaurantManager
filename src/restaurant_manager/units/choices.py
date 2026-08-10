from django.db import models

class VolumeUnit(models.TextChoices):
    MILLILITER = 'ml', 'Milliliter'
    LITER = 'l', 'Liter'
    TEASPOON = 'tsp', 'Teaspoon'
    TABLESPOON = 'tbsp', 'Tablespoon'
    CUP = 'cup', 'Cup'
    PINT = 'pt', 'Pint'
    QUART = 'qt', 'Quart'
    GALLON = 'gal', 'Gallon'

class WeightUnit(models.TextChoices):
    GRAM = 'g', 'Gram'
    KILOGRAM = 'kg', 'Kilogram'
    OUNCE = 'oz', 'Ounce'
    POUND = 'lb', 'Pound'

class CountUnit(models.TextChoices):
    PIECE = 'pc', 'Piece'
    DOZEN = 'doz', 'Dozen'
    PAIR = 'pair', 'Pair'

class CulinaryUnit(models.TextChoices):
    DASH = 'dash', 'Dash'
    PINCH = 'pinch', 'Pinch'
    SPRINKLE = 'sprinkle', 'Sprinkle'
    CUBE = 'cube', 'Cube'

RECIPE_UNITS = VolumeUnit.choices + WeightUnit.choices + CountUnit.choices + CulinaryUnit.choices