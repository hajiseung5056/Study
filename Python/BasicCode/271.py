import random

class Account:

    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.bank = "SC은행"
        
        acc1 = random.randint(0,999)
        acc2 = random.randint(0,99)
        acc3 = random.randint(0,999999)

        acc1 = str(acc1).zfill(3)
        acc2 = str(acc2).zfill(2)
        acc3 = str(acc3).zfill(6)
        
        self.accountnum = acc1 + "-" + acc2 + "-" + acc3

kim = Account("김민수",100)
print(kim.name)
print(kim.money)
print(kim.bank)
print(kim.accountnum)

