def printmxn(string,num):
    cnt = int(len(string)/num)

    if len(string)%num != 0:
        cnt += 1
    
    for i in range(cnt):
        print(string[i*num:i*num+num])


printmxn("아이엠어보이유알어걸", 3)
printmxn("아이엠어보이유알어걸", 3)