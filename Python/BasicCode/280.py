import random

class Account:

    account_count = 0

    def __init__(self,name,balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        
        acc1 = random.randint(0,999)
        acc2 = random.randint(0,99)
        acc3 = random.randint(0,999999)

        acc1 = str(acc1).zfill(3)
        acc2 = str(acc2).zfill(2)
        acc3 = str(acc3).zfill(6)
        
        self.accountnum = acc1 + "-" + acc2 + "-" + acc3

        Account.account_count += 1
    
    @classmethod
    def get_account_num(cls):
        return cls.account_count
    
    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)


k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()