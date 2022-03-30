import unittest

from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Duncan Cole", 45, 40, 5)
        self.drink1 = Drink("Coke Zero", 1.5, 0)
        self.food1 = Food("pizza", 8, 3)


    def test_customer_has_name(self):
        self.assertEqual("Duncan Cole", self.customer1.name)
    
    def test_customer_has_money(self):
        self.assertEqual(45, self.customer1.wallet)
    
    def test_customer_can_buy_drink(self):
        self.customer1.buy_drink(self.drink1)
        self.assertEqual(43.5, self.customer1.wallet)
    
    def test_customer_can_buy_food(self):
        self.customer1.buy_food(self.food1)
        self.assertEqual(37, self.customer1.wallet)
        self.assertEqual(2, self.customer1.drunkenness)