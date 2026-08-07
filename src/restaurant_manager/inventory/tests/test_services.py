from django.test import TestCase

from inventory.services import calculate_moving_average_cost, update_current_average_unit_cost, update_inventory_stock_quantity, process_order
from inventory.models import Distributor, StockItem, InventoryStock, Order, OrderItem
from products.models import Product
import decimal
from decimal import Decimal

class TestOrderProcessingSuccess(TestCase):
    def setUp(self):
        self.stock_item = StockItem.objects.create(product=Product.objects.create(product_name="Test Product"),
                                    size="1",
                                    units="kg",
                                    current_average_unit_cost=8
                                    )
        self.inventory_stock = InventoryStock.objects.create(stock_item=self.stock_item, 
                                              quantity=10)
        self.order = Order.objects.create()
        self.order_item = OrderItem.objects.create(stock_item=self.stock_item,
                                    order=self.order,
                                    quantity_received=5,
                                    quantity_ordered=5,
                                    unit_cost_at_purchase=10)

    def test_inventory_stock_increase(self):
        process_order(self.order)
        self.inventory_stock.refresh_from_db()
        self.assertEqual(self.inventory_stock.quantity, 15)

    def test_updates_current_average_unit_cost(self):
        process_order(self.order)
        decimal.getcontext().prec = 3
        expected_average = Decimal(8 * 10 + 10 * 5) / Decimal(10 + 5)
        self.stock_item.refresh_from_db()
        self.assertEqual(self.stock_item.current_average_unit_cost, Decimal(expected_average))

    def test_update_to_last_purchased_at(self):
        process_order(self.order)
        self.stock_item.refresh_from_db()
        self.assertEqual(self.stock_item.last_purchased_at, self.order.order_processed_at)

    def test_order_processed_flag(self):
        process_order(self.order)
        self.order.refresh_from_db()
        self.assertEqual(self.order.processed, True)

class TestOrderProcessingFailure(TestCase):
    def setUp(self):
        self.stock_item = StockItem.objects.create(product=Product.objects.create(product_name="Test Product"),
                                    size="1",
                                    units="kg",
                                    current_average_unit_cost=8
                                    )
        self.inventory_stock = InventoryStock.objects.create(stock_item=self.stock_item, 
                                              quantity=10)
        self.order = Order.objects.create()
        self.order_item = OrderItem.objects.create(stock_item=self.stock_item,
                                    order=self.order,
                                    quantity_received=5,
                                    quantity_ordered=5,
                                    unit_cost_at_purchase=10)

    def test_process_order_failure_with_invalid_quantity_received(self):
        self.order_item = OrderItem.objects.create(stock_item=self.stock_item,
                                    order=self.order,
                                    quantity_received=-5,
                                    quantity_ordered=5,
                                    unit_cost_at_purchase=10)
        with self.assertRaises(ValueError):
            process_order(self.order)
        self.inventory_stock.refresh_from_db()
        self.assertEqual(self.order.processed, False)

    def test_process_order_failure_for_already_processed_order(self):
        self.order.processed = True
        self.order.save()
        
        with self.assertRaises(ValueError):
            process_order(self.order)

    def test_process_order_failure_database_rollback_with_value_error(self):
        self.order_item = OrderItem.objects.create(stock_item=self.stock_item,
                                    order=self.order,
                                    quantity_received=-5,
                                    quantity_ordered=5,
                                    unit_cost_at_purchase=10)
        try:
            process_order(self.order)
        except ValueError:
            pass
        self.inventory_stock.refresh_from_db()
        self.assertEqual(self.inventory_stock.quantity, 10)
        self.stock_item.refresh_from_db()
        self.assertEqual(self.stock_item.current_average_unit_cost, 8)
        
