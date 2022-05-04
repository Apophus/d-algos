def arrayManipulation(n, queries):
    # Write your code here
    list_ = [0 for i in range(n)]
    print(list_)
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        for j in range(a-1, b):
            list_[j] += k

    ans = max(list_)

    return ans

queries = [[1,5,3,],[4,8,7],[6,9,1]]
n= 10

print(arrayManipulation(n, queries))
