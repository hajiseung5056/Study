user = int(input("입력:"))

user1 = user-20

if user1 < 0:
    print(0)
elif user1 > 255:
    print(255)
else:
    print(user1)