from django.contrib import admin
from .models import Category, Distributor, InventoryItem, InventoryStock, StockMovement

# Register your models here.

admin.site.register(Category)
admin.site.register(Distributor)
admin.site.register(InventoryItem)
admin.site.register(InventoryStock)
admin.site.register(StockMovement)
