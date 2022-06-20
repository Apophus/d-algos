from collections import Counter


def solution(s):
    tally = Counter(s)
    res = []
    res_index = []
    for char in tally:
        if tally[char] == 1:
            res.append(char)

    for i in res:
        res_index.append(s.find(i))
    print(tally, res, res_index)
    print(s[min(res_index)])
    return s[min(res_index)]

if __name__ == '__main__':
    solution('abacabad')