def print_score(list):
    sum = 0
    avg = 0
    for val in list:
        sum += val
    
    avg = sum / len(list)

    print(avg)

print_score([1,2,3])


#def print_score(score_list) :
#    print(sum(score_list)/len(score_list))