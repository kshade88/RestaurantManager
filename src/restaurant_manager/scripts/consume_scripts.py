from inventory.models import StockItem, InventoryStock, OrderItem
from products.models import Product
# from bar.services import get_available_quantity_in_milliliters, consume_product_inventory
# from restaurant_manager.bar.services import get_available_quantity_in_milliliters
from inventory.services import consume_product_inventory
from units.conversions import convert_volume
from inventory.services import get_available_skus, get_total_available_quantity, normalize_quantity, calculate_sku_consumption

def run():
    # Example usage of the get_available_quantity function      
    product = Product.objects.get(id=21)  # Replace with the actual product ID you want to check
    available_quantity = get_total_available_quantity(product)
    print("Available quantity:", available_quantity)

    # Example usage of consuming product inventory
    try:
        consume_product_inventory(product, 500)  # Replace 100 with the quantity you want to consume in milliliters
    except ValueError as e:
        print(str(e))

    remaining_quantity = get_total_available_quantity(product)
    print("Remaining quantity:", remaining_quantity)
