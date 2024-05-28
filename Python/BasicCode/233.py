def make_list(string):
    list = []
    for i in range(len(string)):
        list.append(string[i-1])

    return list

make_list("abcd")