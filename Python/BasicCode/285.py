class car:
    def __init__(self,wheel,price):
        self.wheel = wheel
        self.price = price


class scar(car):
    def __init__(self,wheel,price):
        super().__init__(wheel,price)

    def info(self):
        print("바퀴수 " + str(self.wheel))
        print("가격 " + str(self.price))

car1 = scar(4,1000)
car1.info()
    