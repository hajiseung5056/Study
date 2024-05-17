number1 = int(input())
number2 = int(input())
number3 = int(input())

max = number1

if max < number2:
    max = number2

if max < number3:
    max = number3

print(max)
