def print_5xn(string):
    leng = len(string)
    cnt = int(leng/5)
    
    if leng%5 != 0:
        cnt += 1
    
    for i in range(cnt):
        print(string[i*5:i*5+5])

print_5xn("아이엠어보이유알어걸")
print_5xn("아이엠어보이유알어걸")

def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1) :
        print(line[x * 5: x * 5 + 5])
print_5xn("아이엠어보이유알어걸")
print_5xn("아이엠어보이유알어걸")
