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

kim = Account("김민수",100)
lee = Account("이민수",200)
print(kim.get_account_num())
print(Account.get_account_num())