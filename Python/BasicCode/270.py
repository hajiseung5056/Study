class Stock:
    def __init__(self,name,code,per,pbr,dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend


    def set_name(self,name):
        self.name = name

    def set_code(self,code):
        self.code = code

    def set_per(self,per):
        self.per = per

    def set_pbr(self,pbr):
        self.pbr = pbr

    def set_dividend(self,dividend):
        self.dividend = dividend


    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
    

삼성 = Stock("삼성전자","005930",15.79,1.33,2.83)
현대 = Stock("현대차","005380",8.70,0.35,4.27)
LG = Stock("LG전자","066570",317.34,0.69,1.37)

list1 = [삼성, 현대, LG]

for i in list1:
    print(i.code)
    print(i.per)