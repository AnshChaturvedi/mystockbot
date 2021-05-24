class Trade_Account:
    
    def __init__(self, name):
        self.name = name
        self.money = 0
    
    def add_money(self, amount):
        self.money += amount
        return self.money

    def remove_money(self, amount):
        self.money -= amount
        return self.money

