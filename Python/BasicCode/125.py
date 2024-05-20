comp = {"011":"SKT","016":"KT","019":"LGU","010":"알수없음"}

phone = input("입력:")

phone1 = phone[:3]

comp1 = comp[phone1]

print("당신은",comp1,"사용자입니다.")