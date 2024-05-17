warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

user = input("입력:")

if user in warn_investment_list:
    print("투자경고종목입니다.")
else:
    print("투자경고종목이 아닙니다.")