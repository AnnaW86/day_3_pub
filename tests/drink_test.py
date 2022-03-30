import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Coke Zero", 1.5, 0)
    def test_drink_has_name(self):
        self.assertEqual("Coke Zero", self.drink1.name)
    
    def test_drink_has_price(self):
        self.assertEqual(1.5, self.drink1.price)