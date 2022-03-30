class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def sell_drink(self, customer, drink):
        if customer.age >= 18 and customer.drunkenness <= 8:
            self.till += drink.price
            customer.buy_drink(drink)
            customer.drunkenness += drink.alcohol_level
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