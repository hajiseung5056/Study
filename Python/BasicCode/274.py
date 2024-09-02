import random

class Account:

    acc_cnt = 0

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

        Account.acc_cnt += 1
    
    @classmethod
    def get_account_num(cls):
        return cls.acc_cnt
    
    def deposit(self,amount):
        if amount >= 1: 
            self.money += amount

kim = Account("김민수",100)
print(kim.money)
kim.deposit(10)
print(kim.money)