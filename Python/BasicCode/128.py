num = input("입력:")

num = num.split("-")[1]

num = num[1:3]

num1 = int(num)

if num1 <= 8:
    print("서울")
else:
    print("서울아님")