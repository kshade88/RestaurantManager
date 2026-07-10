from django.db import models
from products.models import Product

# Create your models here.
class Distributor(models.Model):
    distributor_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    manager_name = models.CharField(max_length=100)
    manager_email = models.EmailField()
    manager_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.distributor_name


class  StockItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product.product_name  # Access the name of the related BarProduct instance
    
class InventoryStock(models.Model):
    product = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)     

    def __str__(self):
        return f"{self.product.product.product_name} - {self.quantity}"

class StockMovement(models.Model):
    MOVEMENT_TYPE_CHOICES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    ]

    stock_item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPE_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stock_item.product.product_name} - {self.movement_type} - {self.quantity}"
