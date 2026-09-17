"""Service functions for managing inventory stock."""
from datetime import timedelta
from django.utils import timezone
from django.db.models import Aggregate, Avg
from django.db import transaction
from decimal import Decimal

from .models import InventoryStock, Order, OrderItem, StockItem
from units.choices import VolumeUnit, WeightUnit
from units.conversions import convert_volume, convert_weight


def calculate_moving_average_cost(
        *,
        unit_cost_at_purchase,
        quantity_received,
        current_average_unit_cost,
        quantity,
):
    
    unit_cost_at_purchase = Decimal(unit_cost_at_purchase)
    quantity_received = Decimal(quantity_received)
    current_average_unit_cost = Decimal(current_average_unit_cost)
    quantity = Decimal(quantity)
    
    if quantity_received < 0:
        raise ValueError("Received quantity must be greater than zero")
    
    if quantity < 0:
        raise ValueError("Current quantity cannot be negative")
    
    if unit_cost_at_purchase is None:
        raise ValueError("Unit cost at purchase is required")
    
    total_quantity = quantity_received + quantity
    current_value = current_average_unit_cost * quantity
    received_value = unit_cost_at_purchase * quantity_received
    new_average_unit_cost = (received_value + current_value) / total_quantity
    return new_average_unit_cost

def update_current_average_unit_cost(stock_item, order_item):
    stock_item.current_average_unit_cost = calculate_moving_average_cost(
        unit_cost_at_purchase=order_item.unit_cost_at_purchase,
        quantity_received=order_item.quantity_received,
        current_average_unit_cost=stock_item.current_average_unit_cost or 0,
        quantity=stock_item.inventory_stock.quantity or 0,
    )
    stock_item.save(update_fields=['current_average_unit_cost'])

def update_inventory_stock_quantity(order_item):
    stock_item = order_item.stock_item
    inventory_stock = stock_item.inventory_stock
    inventory_stock.quantity += order_item.quantity_received
    inventory_stock.save(update_fields=['quantity'])

@transaction.atomic
def process_order(order):
    if order.processed:
        raise ValueError("Order has already been processed.")
    order.order_processed_at = timezone.now()
    for order_item in order.order_items.all():
        stock_item = order_item.stock_item
        update_current_average_unit_cost(stock_item, order_item)
        update_inventory_stock_quantity(order_item)
        stock_item.last_purchased_at = order.order_processed_at
        stock_item.last_purchased_unit_cost = order_item.unit_cost_at_purchase
        stock_item.save(update_fields=['current_average_unit_cost', 'last_purchased_at', 'last_purchased_unit_cost'])
    order.processed = True
    order.save()


def get_available_skus(product):
    skus = StockItem.objects.filter(product=product).select_related('inventory_stock') 
    available_skus = []
    
    for sku in skus:
        if hasattr(sku, 'inventory_stock') and sku.inventory_stock.quantity > 0:
            available_skus.append(sku)
    
    return available_skus

def normalize_quantity(quantity, unit):
    if unit in VolumeUnit.values:
        quantity = convert_volume(quantity, from_unit=unit, to_unit='ml')
        return Decimal(quantity)
    elif unit in WeightUnit.values:
        quantity = convert_weight(quantity, from_unit=unit, to_unit='g')
        return Decimal(quantity)
    else:
        raise ValueError(f"Unsupported unit type: {unit}")

def get_sku_available_quantity(sku):
    normalized_size = normalize_quantity(sku.size, sku.units)
    quantity = sku.inventory_stock.quantity if hasattr(sku, 'inventory_stock') else 0
    return normalized_size * quantity

def get_total_available_quantity(product):
    skus = StockItem.objects.filter(product=product).select_related('inventory_stock')
    total_quantity = sum(get_sku_available_quantity(sku) for sku in skus)
    return total_quantity

def calculate_sku_consumption(sku, quantity_to_consume):
    available_quantity = get_sku_available_quantity(sku)
    quantity_consumed = min(quantity_to_consume, available_quantity)
    remaining_quantity_to_consume = quantity_to_consume - quantity_consumed
    remaining_quantity_available = available_quantity - quantity_consumed
    return remaining_quantity_to_consume, remaining_quantity_available

def consume_product_inventory(product, quantity_to_consume):
    available_product_quantity = get_total_available_quantity(product)
    if quantity_to_consume > available_product_quantity:
        raise ValueError(f"Not enough inventory to consume {quantity_to_consume} units of {product.product_name}. Available: {available_product_quantity} units.")

    available_skus = get_available_skus(product)

    for sku in available_skus:
        if quantity_to_consume <= 0:
            break

        remaining_quantity_to_consume, remaining_quantity_available = calculate_sku_consumption(sku, quantity_to_consume)

        # Update the inventory stock for the SKU
        normalized_size = normalize_quantity(sku.size, sku.units)
        new_quantity = remaining_quantity_available / normalized_size

        sku.inventory_stock.quantity = new_quantity
        sku.inventory_stock.save(update_fields=['quantity'])

        quantity_to_consume = remaining_quantity_to_consume







