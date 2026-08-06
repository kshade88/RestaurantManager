"""Service functions for managing inventory stock."""
from datetime import timedelta
from django.utils import timezone
from django.db.models import Aggregate, Avg
from django.db import transaction
from decimal import Decimal

from .models import InventoryStock, Order, OrderItem, StockItem


# def process_order(order):
#     """Update inventory stock based on a received order.

#     Args:
#         order: An order object representing the received order.

#     Returns:
#         The updated inventory stock object.
#     """
#     if order.processed:
#         return False
#     for order_item in order.order_items.all():
#         inventory_item = InventoryStock.objects.get(stock_item=order_item.stock_item)
#         inventory_item.quantity += order_item.quantity_received
#         inventory_item.save()
#     order.processed = True
#     order.save()
#     return inventory_item

# def check_low_stock(stock_item):
#     """
#     Take the inventory stock and par level and check if the stock is below the par level.
    
#     Args:
#         stock_item: The stock item to check for low inventory.

#     Returns:
#         True if the inventory stock is below the par level, False otherwise.
#     """
#     inventory_stock = InventoryStock.objects.get(stock_item=stock_item)

#     if inventory_stock.quantity < stock_item.par_level:
#         return True
#     return False

# # refactor for more accutate value
# def calculate_item_inventory_value(stock_item):
#     """
#     Calculate the total inventory value for a given stock item.

#     Args:
#         stock_item: The stock item for which to calculate the inventory value.

#     Returns:
#         The total inventory value (quantity * unit cost) for the stock item.
#     """
#     inventory_stock = InventoryStock.objects.get(stock_item=stock_item)

#     past_thirty_days = timezone.now() - timedelta(days=30)
#     recent_orders = OrderItem.objects.filter(
#         stock_item=stock_item,
#         order_date__gte=past_thirty_days
#     )
#     average_unit_cost = recent_orders.aggregate(average=Avg('unit_cost_at_purchase'))



#     return inventory_stock.quantity * (average_unit_cost['average'] or 0)

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
    """
    Calculate the moving average cost for a stock item.

    Args:
        unit_cost_at_purchase: The unit cost of the newly received stock.
        quantity_received: The quantity of the newly received stock.
        current_average_unit_cost: The previous weighted average cost of the stock item.
        quantity: The previous quantity on hand of the stock item.

    Returns:
        The updated moving average cost.
    """
    if quantity_received <= 0:
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
        print("Order has already been processed.")
        return True
    for order_item in order.order_items.all():
        stock_item = order_item.stock_item
        print(f"Processing order item for stock item: {stock_item.product}")
        print(f"Average unit cost before update: {stock_item.current_average_unit_cost}")
        print(f"Quantity before update: {stock_item.inventory_stock.quantity}")
        print(f"Quantity received for this order item: {order_item.quantity_received} at cost: {order_item.unit_cost_at_purchase}")
        update_current_average_unit_cost(stock_item, order_item)
        update_inventory_stock_quantity(order_item)
        print(f"Average unit cost after update: {stock_item.current_average_unit_cost}")
        print(f"Quantity after update: {stock_item.inventory_stock.quantity}")
        stock_item.last_purchased_at = timezone.now()
        stock_item.last_purchased_unit_cost = order_item.unit_cost_at_purchase
        stock_item.save(update_fields=['current_average_unit_cost', 'last_purchased_at', 'last_purchased_unit_cost'])
    order.processed = True
    order.save()




