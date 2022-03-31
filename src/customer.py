from src.person import Person

class Customer(Person):
    def __init__(self, name, wallet, age, drunkenness):
        super().__init__(name, wallet, age)
        self.drunkenness = drunkenness

    def buy_item(self, item):
        self.wallet -= item.price

    def buy_drink(self, drink):
        if self.wallet >= drink.price:
            self.buy_item(drink)
            self.drunkenness += drink.alcohol_level

    def buy_food(self, food):
        if self.wallet >= food.price:
            self.buy_item(food)
            self.drunkenness -= food.rejuvination_level