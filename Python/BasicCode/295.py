f = open("C:/Users/하지승/Desktop/test/매수종목2.txt", mode='r')
lines = f.readlines()

data = {}
item = []

for line in lines:
    item = line.split()
    key = item[0].strip()
    value = item[1].strip()
    data[key] = value

    


print(data)

f.close