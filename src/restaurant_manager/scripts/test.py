from products.models import Product
from bar.models import SpiritCategory, DetailCategory
from inventory.models import Distributor, StockItem, InventoryStock, OrderItem, Order
from inventory.services import process_order
from django.db import connection

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

def run():
    
    order = Order.objects.get(id=1)

    # if order.processed:
    #     print("Order has already been processed.")
    # else:
    #     print("Order has not been processed yet.")

    # if not order.processed:
    process_order(order)
    for order_item in order.order_items.all():
        inventory_item = order_item.stock_item.inventory_stock
        print(f"Stock Item: {order_item.stock_item}, Updated Quantity: {inventory_item.quantity}")
    print("Order processing complete.")