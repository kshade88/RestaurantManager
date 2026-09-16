from inventory.models import StockItem, InventoryStock, OrderItem
from products.models import Product
from bar.services import get_available_quantity_in_milliliters, get_available_skus, get_sku_available_quantity_in_milliliters, calculate_sku_consumption, consume_product_inventory
from units.conversions import convert_volume

def run():
    # Example usage of the get_available_quantity function      
    product = Product.objects.get(id=1)  # Replace with the actual product ID you want to check
    available_quantity = get_available_quantity_in_milliliters(product)
    print("Available quantity in milliliters:", available_quantity)

    # Example usage of consuming product inventory
    try:
        consume_product_inventory(product, 100)  # Replace 100 with the quantity you want to consume in milliliters
    except ValueError as e:
        print(str(e))

    remaining_quantity = get_available_quantity_in_milliliters(product)
    print("Remaining quantity in milliliters after consumption:", remaining_quantity)
