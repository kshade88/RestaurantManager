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
    price = models.DecimalField(max_digits=10, decimal_places=2) #think about a way to make price unique per stock item object of the same product
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product.product_name  # Access the name of the related BarProduct instance
    
class InventoryStock(models.Model):
    stock_item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)     

    def __str__(self):
        return f"{self.stock_item.product.product_name} - {self.quantity}"

class Order(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order - {self.order_date}"

class OrderItem(models.Model):
    stock_item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    quantity_received = models.IntegerField(default=0)
    quantity_ordered = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stock_item.product.product_name} - {self.quantity_received} - {self.quantity_ordered} - {self.order_date}"

# class StockMovement(models.Model):
#     MOVEMENT_TYPE_CHOICES = [
#         ('IN', 'Stock In'),
#         ('OUT', 'Stock Out'),
#     ]

#     stock_item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
#     movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPE_CHOICES)
#     quantity = models.DecimalField(max_digits=10, decimal_places=1)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.stock_item.product.product_name} - {self.movement_type} - {self.quantity}"
