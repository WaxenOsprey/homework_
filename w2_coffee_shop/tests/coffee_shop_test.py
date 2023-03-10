from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer
import unittest

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Latte", 7.5, 2)
        self.drink_2 = Drink("Mocha", 9, 3)
        self.stock = {self.drink_1: 20, self.drink_2: 100}
        self.coffeeshop_1 = CoffeeShop("tarbucks", 200, self.stock)
        self.customer_1 = Customer("Paul", 34, 100, 1)
        self.customer_2 = Customer("John", 23, 100, 6)
    def test_coffeeshop_has_a_name(self):
        self.assertEqual("tarbucks", self.coffeeshop_1.name)

    def test_coffeeshop_has_a_till(self):
        self.assertEqual(200, self.coffeeshop_1.till)

    def test_coffee_has_drinks(self):
        self.assertEqual(2, len(self.coffeeshop_1.stock))

    def test_can_add(self):
        self.coffeeshop_1.make_sale(self.drink_1, self.customer_1)
        self.assertEqual(207.5, self.coffeeshop_1.till)

    def test_check_age(self):
        can_drink = self.coffeeshop_1.check_age(self.customer_1)
        self.assertEqual(True, can_drink)

    def test_check_caffeine(self):
        can_drink = self.coffeeshop_1.check_caffeine(self.drink_1, self.customer_1)
        self.assertEqual(True, can_drink)
        can_drink = self.coffeeshop_1.check_caffeine(self.drink_1, self.customer_2)
        self.assertEqual(False, can_drink)

    def test_make_sale(self):
        self.coffeeshop_1.make_sale(self.drink_1, self.customer_1)
        self.assertEqual(3, self.customer_1.energy)
        self.assertEqual(92.5, self.customer_1.wallet)
        self.assertEqual(207.5, self.coffeeshop_1.till)
    
#    def test_stock_value(self):
#        result = self.coffeeshop_1.stock_value(self.coffeeshop_1.stock)
#        self.assertEqual(1050 ,result)