from inventory.models import StockItem, InventoryStock, OrderItem
from products.models import Product
from units.conversions import convert_volume

def get_available_quantity_in_milliliters(product):
    skus = StockItem.objects.filter(product=product).select_related('inventory_stock') 
    
    total = 0
        
    for sku in skus:
        size_in_ml = convert_volume(sku.size, 
                                from_unit=sku.units, 
                                to_unit='ml')
        quantity = sku.inventory_stock.quantity if hasattr(sku, 'inventory_stock') else 0
        total += size_in_ml * quantity
    
    return total

def get_available_skus(product):
    skus = StockItem.objects.filter(product=product).select_related('inventory_stock') 
    available_skus = []
    
    for sku in skus:
        if hasattr(sku, 'inventory_stock') and sku.inventory_stock.quantity > 0:
            available_skus.append(sku)
    
    return available_skus

def get_sku_available_quantity_in_milliliters(sku):
    size_in_ml = convert_volume(sku.size, from_unit=sku.units, to_unit='ml')
    quantity = sku.inventory_stock.quantity if hasattr(sku, 'inventory_stock') else 0
    return size_in_ml * quantity

def get_available_quantity_for_each_available_sku_in_milliliters(product):
    available_skus = get_available_skus(product)
    available_quantities = {}
    
    for sku in available_skus:
        available_quantities[sku.id] = get_sku_available_quantity_in_milliliters(sku)

    return available_quantities

def consume_from_individual_sku(sku, quantity_to_consume):

    available_quantity_in_ml = get_sku_available_quantity_in_milliliters(sku)

    quantity_consumed = min(quantity_to_consume, available_quantity_in_ml)

    remaining_quantity_to_consume = quantity_to_consume - quantity_consumed

    remaining_quantity_available = available_quantity_in_ml - quantity_consumed

    return remaining_quantity_to_consume, remaining_quantity_available


def consume_product_inventory(product, quantity_to_consume):
    available_product_quantity = get_available_quantity_in_milliliters(product)
    if quantity_to_consume > available_product_quantity:
        raise ValueError(f"Not enough inventory to consume {quantity_to_consume} ml of {product.product_name}. Available: {available_product_quantity} ml.")

    available_skus = get_available_skus(product)

    for sku in available_skus:
        if quantity_to_consume <= 0:
            break
        remaining_quantity_to_consume, remaining_quantity_available = consume_from_individual_sku(sku, quantity_to_consume)

        # Update the inventory stock for the SKU
        size_in_ml = convert_volume(sku.size, from_unit=sku.units, to_unit='ml')
        new_quantity = remaining_quantity_available / size_in_ml
        sku.inventory_stock.quantity = new_quantity
        sku.inventory_stock.save(update_fields=['quantity'])
        quantity_to_consume = remaining_quantity_to_consume



    

        

def consume_product_inventory_old_function(product, quantity_to_consume):
    skus = StockItem.objects.filter(product=product).select_related('inventory_stock').order_by('id') 

    for sku in skus:
        if quantity_to_consume <= 0:
            break

        size_in_ml = convert_volume(sku.size, from_unit=sku.units, to_unit='ml')
        available_quantity = sku.inventory_stock.quantity if hasattr(sku, 'inventory_stock') else 0
        available_quantity_in_ml = size_in_ml * available_quantity

        if available_quantity_in_ml >= quantity_to_consume:
            # Consume the required quantity from this SKU
            new_quantity_in_ml = available_quantity_in_ml - quantity_to_consume
            percentage_to_consume = new_quantity_in_ml / available_quantity_in_ml
            new_quantity = available_quantity * percentage_to_consume
            sku.inventory_stock.quantity = new_quantity 
            # quantity_to_consume -= available_quantity_in_ml
            # new_quantity = available_quantity - (quantity_to_consume / size_in_ml)
            # sku.inventory_stock.quantity = new_quantity
            sku.inventory_stock.save()
        else:
            # Consume all available quantity from this SKU and move to the next one
            quantity_to_consume -= available_quantity_in_ml
            sku.inventory_stock.quantity = 0
            sku.inventory_stock.save()