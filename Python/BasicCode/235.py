def covert_int(string):
    result = int(string.replace(",",""))
    return result
    

a = covert_int("1,234,567")

print(type(a))