import random

class Account:

    acc_cnt = 0

    def __init__(self,name,money):
        self.deposit_cnt = 0
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
            
            self.deposit_cnt += 1
            if self.deposit_cnt % 5 == 0:
                self.money = self.money * 1.01


    def withdraw(self,amount):
        if amount < self.money:
            self.money -= amount


    def display_info(self):
        print("은행이름: " + self.bank)
        print("예금주: " + self.name)
        print("계좌번호: " + self.accountnum)
        print("잔고: " + str(self.money) + "원")



p = Account("파이썬", 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.money)