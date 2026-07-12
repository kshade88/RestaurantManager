"""Service functions for managing inventory stock."""

def receive_order(order):
    """Update inventory stock based on a received order.

    Args:
        order: An order object containing stock_item and quantity.

    Returns:
        The updated inventory stock object.
    """
    inventory_item = InventoryStock.objects.get(stock_item=order.stock_item)
    inventory_item.quantity += order.quantity
    inventory_item.save()
    return inventory_item

