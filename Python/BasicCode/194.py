data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]


data2 = []

for list in data:
    data1 = []
    for val in list:
        data1.append(val*1.00014)
    data2.append(data1)


print(data2)