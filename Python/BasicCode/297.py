per = ["10.31", "", "8.00"]

new_per = []

for i in per:
    try:
        new_per.append(float(i))
    except:
        new_per.append(0)

print(new_per)