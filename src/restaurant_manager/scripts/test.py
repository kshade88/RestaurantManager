from products.models import Product, Category
from bar.models import SpiritCategory, DetailCategory, BeerDetail, WineDetail, SpiritDetail, liqueurDetail, GarnishDetail
from inventory.models import Distributor, StockItem, InventoryStock, StockMovement
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
    product = Product.objects.get(product_name='Test Spirit 6')
    quantity = 10
    stock_item = StockItem.objects.get(product=product)

    def add_item_to_stock(stock_item, quantity):
        inventory_stock = InventoryStock.objects.get_or_create(stock_item=stock_item)[0]
        inventory_stock.quantity += quantity
        inventory_stock.save()


    add_item_to_stock(stock_item, quantity)

