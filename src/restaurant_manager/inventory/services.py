"""Service functions for managing inventory stock."""
from .models import InventoryStock, Order, OrderItem

def process_order(order):
    """Update inventory stock based on a received order.

    Args:
        order: An order object representing the received order.

    Returns:
        The updated inventory stock object.
    """
    if order.processed:
        return False
    for order_item in order.order_items.all():
        inventory_item = InventoryStock.objects.get(stock_item=order_item.stock_item)
        inventory_item.quantity += order_item.quantity_received
        inventory_item.save()
    order.processed = True
    order.save()
    return inventory_item




