from django.db import models
from products.models import Product

# Create your models here.
class Distributor(models.Model):
    distributor_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=20, null=True, blank=True)
    manager_name = models.CharField(max_length=100, null=True, blank=True)
    manager_email = models.EmailField(null=True, blank=True)
    manager_phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.distributor_name} - {self.contact_name}"

# represents a specific Sku (Stock Keeping Unit) for a product
class  StockItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=50)
    # Will more than likely remove unit_cost
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2) 
    # last ordered unit cost
    last_purchased_unit_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # weighted average cost
    current_average_unit_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_purchased_at = models.DateTimeField(null=True, blank=True)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)
    par_level = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.product.product_name  # Access the name of the related BarProduct instance

# represents the inventory stock (quantity on hand) for a specific stock item
class InventoryStock(models.Model):
    stock_item = models.OneToOneField(StockItem, on_delete=models.CASCADE, related_name='inventory_stock')
    quantity = models.DecimalField(max_digits=10, decimal_places=1)     

    def __str__(self):
        return f"{self.stock_item.product.product_name} - {self.quantity}"

# represents an order placed to a distributor
class Order(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order - {self.order_date}"

# represents an item within an order, linking a stock item to an order with quantities
class OrderItem(models.Model):
    stock_item = models.ForeignKey(StockItem, on_delete=models.CASCADE, related_name='order_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    quantity_received = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    quantity_ordered = models.DecimalField(max_digits=10, decimal_places=1, default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    unit_cost_at_purchase = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True, blank=True)

    # Automatically set the unit cost at purchase if not provided when creating a new order item.
    def save(self, *args, **kwargs):
        if self._state.adding and self.unit_cost_at_purchase is None:
            self.unit_cost_at_purchase = self.stock_item.last_purchased_unit_cost
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.stock_item.product.product_name} - {self.quantity_received} - {self.quantity_ordered} - {self.order_date}"

