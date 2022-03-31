import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.employee import Employee

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Duncan Cole", 45, 40, 5)
        self.customer2 = Customer("Chancer", 6, 17, 1)
        self.customer3 = Customer("Drunk Duncan", 12, 40, 13)
        self.drink1 = Drink("Coke Zero", 1.5, 0)
        self.drink2 = Drink("white wine", 5, 2)
        self.drink3 = Drink("gin and tonic", 6.5, 1)
        self.drink4 = Drink("red wine", 5, 2)
        self.drink5 = Drink("beer", 5.5, 3)
        self.drinks = {
            self.drink1: 50,
            self.drink2: 35,
            self.drink3: 40,
            self.drink4: 35,
            self.drink5: 60}
        self.employee1 = Employee("Jane", 60, 22, 6)
        self.employee2 = Employee("Joe", 14, 24, 6)
        self.employees = [self.employee1, self.employee2]
        self.pub1 = Pub("The Pub", 100, self.drinks, self.employees)

    def test_pub_has_name(self):
        self.assertEqual("The Pub", self.pub1.name)
    
    def test_pub_has_money(self):
        self.assertEqual(100, self.pub1.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual(5, len(self.pub1.drinks))
    
    def test_can_sell_drink__to_over_18(self):
        self.pub1.sell_drink(self.customer1, self.drink3)
        self.assertEqual(106.5, self.pub1.till)
        self.assertEqual(38.5, self.customer1.wallet)

    def test_can_sell_drink__to_under_18(self):
        result = self.pub1.sell_drink(self.customer2, self.drink3)
        self.assertEqual(100, self.pub1.till)
        self.assertEqual(6, self.customer2.wallet)
        self.assertEqual("Go home, kid!", result)
    
    def test_can_sell_drink__not_too_drunk(self):
        self.pub1.sell_drink(self.customer1, self.drink3)
        self.assertEqual(106.5, self.pub1.till)
        self.assertEqual(38.5, self.customer1.wallet)
        self.assertEqual(6, self.customer1.drunkenness)
    
    def test_can_refuse_drink_to_drunkard(self):
        result = self.pub1.sell_drink(self.customer3, self.drink5)
        self.assertEqual("Go home, you're drunk", result)
    
    def test_can_check_stock_of_drink(self):
        result = self.pub1.check_stock(self.drinks, self.drink1)
        self.assertEqual(50, result)
    
    def test_can_check_stock_value(self):
        result = self.pub1.check_total_stock_value(self.drinks)
        self.assertEqual(1015, result)
    
    def test_can_pay_employees(self):
        self.pub1.pay_employees(self.employees, 8)
        self.assertEqual(108, self.employee1.wallet)
        self.assertEqual(62, self.employee2.wallet)
    
    def test_can_restock_drink(self):
        self.pub1.add_drink(self.drink1)
        self.assertEqual(51, self.drinks[self.drink1])
    
    def test_can_add_new_drink(self):
        drink6 = Drink("Coke", 1.8, 0)
        self.pub1.add_drink(drink6, 50)
        self.assertEqual(50, self.drinks[drink6])