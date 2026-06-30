from django.db import models
from bar_products.models import BarProduct

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Distributor(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    manager_name = models.CharField(max_length=100)
    manager_email = models.EmailField()
    manager_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class  InventoryItem(models.Model):
    inventory_name = models.ForeignKey(BarProduct, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.inventory_name.product_name  # Access the name of the related BarProduct instance
    
class InventoryStock(models.Model):
    product = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)     

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

class StockMovement(models.Model):
    MOVEMENT_TYPE_CHOICES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    ]

    product = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPE_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.movement_type} - {self.quantity}"
