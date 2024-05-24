apart = [ [101, 102], [201, 202], [301, 302] ]

for i in range(len(apart)):
    for j in apart[len(apart)-i-1]:
        print(j)

for i in apart[::-1]:
    for j in i:
        print(j)