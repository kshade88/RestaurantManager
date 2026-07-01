from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class BarProduct(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product_name

class BeerDetail(models.Model):
    name = models.OneToOneField(BarProduct, on_delete=models.CASCADE, primary_key=True)
    brewery = models.CharField(max_length=100, null=True, blank=True)
    origin = models.CharField(max_length=100, null=True, blank=True)
    abv = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    style = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name.product_name

class WineDetail(models.Model):
    name = models.OneToOneField(BarProduct, on_delete=models.CASCADE, primary_key=True)
    winery = models.CharField(max_length=100, null=True, blank=True)
    varietal = models.CharField(max_length=100, null=True, blank=True)
    vintage = models.CharField(max_length=4, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name.product_name

class SpiritCategory(models.Model):
    category_name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name

class DetailCategory(models.Model):
    category_name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name

class SpiritDetail(models.Model):
    name = models.OneToOneField(BarProduct, on_delete=models.CASCADE, primary_key=True)
    distillery = models.CharField(max_length=100, null=True, blank=True)
    origin = models.CharField(max_length=100, null=True, blank=True)
    proof = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    spirit_category = models.ForeignKey(SpiritCategory, on_delete=models.CASCADE, null=True, blank=True)
    detail_category = models.ForeignKey(DetailCategory, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name.product_name

class liqueurDetail(models.Model):
    name = models.OneToOneField(BarProduct, on_delete=models.CASCADE, primary_key=True)
    distillery = models.CharField(max_length=100, null=True, blank=True)
    origin = models.CharField(max_length=100, null=True, blank=True)
    proof = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    detail_category = models.ForeignKey(DetailCategory, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name.product_name

class IngredientDetail(models.Model):
    name = models.OneToOneField(BarProduct, on_delete=models.CASCADE, primary_key=True)
    made_in_house = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name.product_name

class MixerDetail(models.Model):
    name = models.OneToOneField(BarProduct, on_delete=models.CASCADE, primary_key=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    made_in_house = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name.product_name

class GarnishDetail(models.Model):
    name = models.OneToOneField(BarProduct, on_delete=models.CASCADE, primary_key=True)
    made_in_house = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name.product_name

