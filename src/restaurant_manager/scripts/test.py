from products.models import Product, Category
from bar.models import SpiritCategory, DetailCategory, BeerDetail, WineDetail, SpiritDetail, liqueurDetail, GarnishDetail
from django.db import connection

def run():
    Category.objects.all()
    
    new_product = Product.objects.create(
        product_name='Test Spirit 6',
        category=Category.objects.get(category_name='Spirit')
    )

    new_spirit = Product.objects.get(product_name='Test Spirit 6')
    
    if new_spirit.category.category_name == 'Spirit':
        SpiritDetail.objects.create(
            name=new_spirit,
            distillery='Test Distillery',
            origin='Test Origin',
            proof=80.0,)
    

    else:
        print("no new spirit product created")
    