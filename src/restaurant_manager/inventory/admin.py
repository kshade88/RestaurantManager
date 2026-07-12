from django.contrib import admin
from .models import InventoryStock, StockItem, Distributor, Order, OrderItem

# Register your models here.

admin.site.register(Distributor)
admin.site.register(StockItem)
admin.site.register(InventoryStock)
admin.site.register(Order)
admin.site.register(OrderItem)
