"""

"""

#https://www.hackerrank.com/challenges/crush/forum/comments/255515
def dynamicArray(n, queries):
    # Write your code here
    """
    n [int] - the number of empty arrays to
        initialize in arr
    string queries[q]: query strings that contain 3 space-separated integers
    [[1, 0, 5], [1, 0, 5]]
    """
    arr = [[] for i in range(n)]

    answers = []
    last_answer = 0

    for query in queries:
        x = query[1]
        y = query[2]

        if query[0] == 1:
            id_x = (x ^ last_answer) % n
            arr[id_x].append(y)
            continue
        else:
            id_x = (x ^ last_answer) % n
            size_ = y % (len(arr[id_x]))
            last_answer = arr[id_x][size_]
            answers.append(last_answer)
            # query_type_2(query[1], query[2])
            continue

    return answers


queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]

n = 2

print(dynamicArray(n, queries))


#https://www.hackerrank.com/challenges/crush/forum/comments/255515

from collections import Counter

def arrayManipulation(n, queries):
    c = Counter()
    for a,b,k in queries:
        c[a]  +=k
        c[b+1]-=k
    arrSum = 0
    maxSum = 0
    for i in sorted(c)[:-1]:
        arrSum+= c[i]
        maxSum = max(maxSum,arrSum)
    return maxSum
