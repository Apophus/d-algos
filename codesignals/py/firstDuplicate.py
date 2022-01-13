from collections import Counter

def solution(a):

    num_counts = Counter(a)
    duplicates = [x for x in num_counts if num_counts[x]>1]
    res_dict = {}

    if not duplicates:
        return -1

    for index, number in enumerate(a):
        if number in duplicates and number not in res_dict:
            res_dict[number] = [index]
        elif number in duplicates and number in res_dict:
            res_dict[number].append(index)
            # break
            # return number
        else:
            continue
    
    sorted_values = sorted(res_dict.items(), key=lambda e: e[1][1])
    res = sorted_values[0][0]
    return res

def solution(a):
    mySet=set()
    for el in a:
        if el in mySet:
            return el
        mySet.add(el)
    return -1

a = [2, 1, 3, 5, 3, 2]
print(solution(a))
