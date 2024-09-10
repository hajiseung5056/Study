class car:
    def __init__(self,wheel,price):
        self.wheel = wheel
        self.price = price


class bicycle(car):
    def __init__(self,wheel,price,name):
        self.wheel = wheel
        self.price = price
        self.name = name





bicycle1 = bicycle(2,100,"시마노")
print(bicycle1.name)