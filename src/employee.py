from src.person import Person

class Employee(Person):
    def __init__(self, name, wallet, age, wage):
        super().__init__(name, wallet, age)
        self.wage = wage