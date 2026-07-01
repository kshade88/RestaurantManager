from django.contrib import admin
from .models import Distributor, InventoryStock, StockItem, StockMovement

# Register your models here.

admin.site.register(Distributor)
admin.site.register(StockItem)
admin.site.register(InventoryStock)
admin.site.register(StockMovement)
