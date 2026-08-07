from django.test import TestCase
from django.core.exceptions import ValidationError
from inventory.models import Distributor, StockItem, InventoryStock, Order, OrderItem

class TestOrderModel(TestCase):
    def setUp(self):
        self.distributor = Distributor(distributor_name="Test Distributor")
        self.order = Order(distributor=self.distributor)

    def test_order_processed_false_on_creation(self):
        self.assertFalse(self.order.processed)
        
    