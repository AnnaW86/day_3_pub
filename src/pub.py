class Pub:
    def __init__(self, name, till, drinks, employees):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.employees = employees
    
    def add_to_till(self, amount):
        self.till += amount
    
    def add_to_drunkenness(self, customer, drink):
        customer.drunkenness += drink.alcohol_level

    def sell_drink(self, customer, drink):
        if self.drinks[drink] == 0:
            return "Sorry, we're all out of that"
        if customer.age >= 18 and customer.drunkenness <= 8 and self.drinks[drink]:
            self.add_to_till(drink.price)
            customer.buy_drink(drink)
        if customer.age < 18:
            return "Go home, kid!"
        if customer.drunkenness > 8:
            return "Go home, you're drunk"
    
    def check_stock(self, drinks, drink_to_check):
        return drinks[drink_to_check]
    
    def check_total_stock_value(self, drinks):
        total_value = 0
        for drink in drinks:
            total_value += drink.price * drinks[drink]
        return total_value
    
    def pay_employees(self, employees, hours_worked):
        for employee in employees:
            employee.wallet += hours_worked * employee.wage

    def add_drink(self, drink, quantity = 1):
        if drink in self.drinks:
            self.drinks[drink] += quantity
        else:
            self.drinks[drink] = quantity