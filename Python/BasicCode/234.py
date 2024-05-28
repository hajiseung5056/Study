def pickup_even(list):
    result = []
    for val in list:
        if val%2 == 0:
            result.append(val)
    return result

pickup_even([3, 4, 5, 6, 7, 8])