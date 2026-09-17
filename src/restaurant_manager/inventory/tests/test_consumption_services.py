from django.test import TestCase

from inventory.models import StockItem, InventoryStock
from inventory.services import consume_product_inventory, get_total_available_quantity, get_available_skus, get_sku_available_quantity, calculate_sku_consumption
from products.models import Product

class ConsumptionServicesTestCase(TestCase):
    def setUp(self):
            self.stock_item = StockItem.objects.create(product=Product.objects.create(product_name="Test Product"),
                                                size="750",
                                                units="ml",
                                                current_average_unit_cost=8
                                                )
            self.inventory_stock = InventoryStock.objects.create(stock_item=self.stock_item, 
                                                          quantity=10)
            self.stock_item2 = StockItem.objects.create(product=self.stock_item.product,
                                                size="1",
                                                units="l",
                                                current_average_unit_cost=12
                                                )
            self.inventory_stock2 = InventoryStock.objects.create(stock_item=self.stock_item2, 
                                                          quantity=5)
    
    def test_get_total_available_quantity(self):
        available_quantity = get_total_available_quantity(self.stock_item.product)
        self.assertEqual(available_quantity, 12500)  # 750 ml * 10 quantity + 1 l * 5 quantity = 12500 ml
    
    def test_get_available_skus(self):
        available_skus = get_available_skus(self.stock_item.product)
        self.assertIn(self.stock_item, available_skus)
        self.assertIn(self.stock_item2, available_skus)
    
    def test_get_sku_available_quantity(self):
        sku_quantity = get_sku_available_quantity(self.stock_item)
        self.assertEqual(sku_quantity, 7500)  # 750 ml * 10 quantity
        sku_quantity2 = get_sku_available_quantity(self.stock_item2)
        self.assertEqual(sku_quantity2, 5000)  # 1 l * 5 quantity
    
    def test_calculate_sku_consumption_when_consuming_more_than_available(self):
        remaining_quantity_to_consume, remaining_quantity_available = calculate_sku_consumption(self.stock_item, 1000)  # consume 1000 ml
        self.assertEqual(remaining_quantity_to_consume, 0)
        self.assertEqual(remaining_quantity_available, 6500)  # 7500 - 1000 = 6500
    
    def test_calculate_sku_consumption_when_consuming_less_than_available(self):
        remaining_quantity_to_consume, remaining_quantity_available = calculate_sku_consumption(self.stock_item, 8000)  # consume 8000 ml
        self.assertEqual(remaining_quantity_to_consume, 500)  # 8000 - 7500 = 500
        self.assertEqual(remaining_quantity_available, 0)  # 7500 - 8000 = 0
    
    def test_consume_product_inventory_consuming_first_sku_only(self):
        initial_quantity = get_total_available_quantity(self.stock_item.product)
        consume_product_inventory(self.stock_item.product, 100)
        remaining_quantity = get_total_available_quantity(self.stock_item.product)
        amount_consumed = initial_quantity - remaining_quantity
        self.assertAlmostEqual(amount_consumed, 
                                   100,
                                   delta=1)
    
    def test_consume_product_inventory_consuming_multiple_skus(self):
        initial_quantity = get_total_available_quantity(self.stock_item.product)
        consume_product_inventory(self.stock_item.product, 8000)  # consume 8000 ml
        remaining_quantity = get_total_available_quantity(self.stock_item.product)
        amount_consumed = initial_quantity - remaining_quantity
        self.assertAlmostEqual(amount_consumed, 
                                   8000,
                                   delta=1) # Attempt to consume more than available