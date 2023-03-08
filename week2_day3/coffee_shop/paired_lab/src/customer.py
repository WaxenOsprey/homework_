class Customer:
    def __init__(self, name, age, wallet_total, energy):
        self.name = name
        self.age = age
        self.wallet = wallet_total
        self.energy = energy

    def pay_for_drink(self, drink):
        price = drink.price
        self.wallet -= price

          