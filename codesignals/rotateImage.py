def solution(a):
    res = [[] for i in range(len(a))]

    for row in range(len(a)-1, -1, -1):
        for index, column in enumerate(res):
            res[index].append(a[row][index])

    return res


if __name__ == '__main__':
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print(solution(a))
