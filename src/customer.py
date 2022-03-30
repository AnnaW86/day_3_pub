from src.person import Person

class Customer(Person):
    def __init__(self, name, wallet, age, drunkenness):
        super().__init__(name, wallet, age)
        self.drunkenness = drunkenness

    def buy_drink(self, drink):
        self.wallet -= drink.price

    def buy_food(self, food):
        self.wallet -= food.price
        self.drunkenness -= food.rejuvination_level