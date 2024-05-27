data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for list in data:
    for val in list:
        print(val+(val*0.00014))
    print("----")