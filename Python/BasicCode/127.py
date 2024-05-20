num = input("입력:")

num = num.split("-")[1]

num = num[:1]

if num in ["1","3"]:
    print("남자")
elif num in ["2","4"]:
    print("여자")