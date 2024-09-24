f = open("C:/Users/하지승/Desktop/test/매수종목1.txt", mode='r')
lines = f.readlines()

codes = []

for line in lines:
    code = line.strip()
    codes.append(code)


print(codes)

f.close