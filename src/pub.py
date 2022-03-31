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

    def check_stock(self, drink_to_check):
        return self.drinks[drink_to_check]

    def can_serve(self, customer, drink):
        if customer.not_old_enough():
            return False, "Go home, kid!"
        if customer.too_drunk():
            return False, "Go home, you're drunk"
        if self.check_stock(drink) == 0:
            return False, "Sorry, we're all out of that"
        return True, ""


    def sell_drink(self, customer, drink):
        if self.can_serve(customer, drink)[0]:
            self.add_to_till(drink.price)
            customer.buy_drink(drink)
        else:
            return self.can_serve(customer, drink)[1]
    
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