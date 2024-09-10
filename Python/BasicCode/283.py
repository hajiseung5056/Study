class car:
    def __init__(self,wheel,price):
        self.wheel = wheel
        self.price = price


class bicycle(car):
    def __init__(self,wheel,price):
        self.wheel = wheel
        self.price = price





bicycle1 = bicycle(2,100)
print(bicycle1.price)