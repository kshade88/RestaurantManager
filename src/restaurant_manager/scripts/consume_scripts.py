from inventory.models import StockItem, InventoryStock, OrderItem
from products.models import Product
from bar.services import get_available_quantity_in_milliliters, get_available_skus, get_sku_available_quantity_in_milliliters, get_available_quantity_for_each_available_sku_in_milliliters
from units.conversions import convert_volume

def run():
    # Example usage of the get_available_quantity function      
    product = Product.objects.get(id=1)
    total = get_available_quantity_in_milliliters(product)

    print("Total available quantity in milliliters:", total)

    skus_available = get_available_skus(product)
    print("Available SKUs for product:", [sku.id for sku in skus_available]) 

    sku_available_quantity = get_sku_available_quantity_in_milliliters(skus_available[0]) if skus_available else 0
    print("Available quantity for the first available SKU in milliliters:", sku_available_quantity)

    available_quantities_for_each_sku = get_available_quantity_for_each_available_sku_in_milliliters(skus_available[0]) if skus_available else {}
    print("Available quantities for each available SKU in milliliters:", available_quantities_for_each_sku)