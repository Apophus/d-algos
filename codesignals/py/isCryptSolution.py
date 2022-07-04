def solution(crypt, solution):
    solution_map = {k: v for k, v in solution}
    res = []
    leading_zeros = [_ for _ in solution_map.keys() if solution_map[_] == '0']
    for word in crypt:
        if word[0] in leading_zeros:
            return False
        continue

    for index, word in enumerate(crypt):
        decrypt = ''
        for char in word:
            decrypt += solution_map[char]
        res.append(int(decrypt))
    check = res[0] + res[1]
    if check == res[2]:
        return True
    return False


if __name__ == '__main__':
    solution_ = [["A", "0"]]
    crypt = ["A",
             "A",
             "A"]

    print(solution(crypt, solution_))