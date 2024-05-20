num = input("입력:")

num = num.replace("-","")

sum = 0

sum += int(num[0]) * 2
sum += int(num[1]) * 3
sum += int(num[2]) * 4
sum += int(num[3]) * 5
sum += int(num[4]) * 6
sum += int(num[5]) * 7
sum += int(num[6]) * 8
sum += int(num[7]) * 9
sum += int(num[8]) * 2
sum += int(num[9]) * 3
sum += int(num[10]) * 4
sum += int(num[11]) * 5

if int(num[12]) == 11-(sum%11):
    print("유효")
else:
    print("오류")


