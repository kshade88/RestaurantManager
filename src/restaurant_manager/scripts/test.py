from products.models import Product
from bar.models import SpiritCategory, DetailCategory, Spirit
from inventory.models import Distributor, StockItem, InventoryStock, OrderItem, Order
from inventory.services import process_order, check_low_stock, calculate_item_inventory_value, calculate_moving_average_cost, update_current_average_unit_cost
from django.db import connection
from django.db.models.functions import Upper
from django.db.models import Count

# def run():
#     Category.objects.all()
    
#     new_product = Product.objects.create(
#         product_name='Test Spirit 6',
#         category=Category.objects.get(category_name='Spirit')
#     )

#     new_spirit = Product.objects.get(product_name='Test Spirit 6')
    
#     if new_spirit.category.category_name == 'Spirit':
#         SpiritDetail.objects.create(
#             name=new_spirit,
#             distillery='Test Distillery',
#             origin='Test Origin',
#             proof=80.0,)
    

#     else:
#         print("no new spirit product created")

# def run():
    
    # order = Order.objects.last()
    # process_order(order)
    # for order_item in order.order_items.all():
    #     stock_item = order_item.stock_item
    #     inventory_value = calculate_item_inventory_value(stock_item)
    #     print(f"Inventory value for {stock_item}: {inventory_value}")

def run():

    # value = calculate_moving_average_cost(
    #     unit_cost_at_purchase=10.0,
    #     quantity_received=5,
    #     current_average_unit_cost=8.0,
    #     quantity=0,        
    # )
    # print(f"Calculated moving average cost: {value}")

    # order_item = OrderItem.objects.last()
    # if order_item:
    #     stock_item = StockItem.objects.get(id=order_item.stock_item.id)
    #     print(f"Retrieved stock item: {stock_item}")
    #     print(f"Unit Cost: {stock_item.current_average_unit_cost}")
    # else:
    #     print("No order items found.")
    # update_current_average_unit_cost(stock_item, order_item)
    # print(f"Updated unit cost for {stock_item}: {stock_item.current_average_unit_cost}")

    order = Order.objects.last()
    process_order(order)