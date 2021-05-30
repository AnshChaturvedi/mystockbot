import finnhub

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

finnhub_client = finnhub.Client(api_key="c2m2riaad3idnodd63tg")

print(finnhub_client.quote('AAPL'))