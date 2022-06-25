import pprint
from operator import itemgetter


def solution(names, time, netValue, isOnVacation):
    employee_dicts = []
    for employee in zip(names, time, netValue, isOnVacation):
        if employee[3]:
            continue
        employee_dict = {'name': employee[0],
                         'time': employee[1],
                         'netValue': employee[2],
                         'isOnVacation': employee[3],
                         'score': employee[2] * (employee[1] / 365)}
        employee_dicts.append(employee_dict)
    sorted_dicts = list(sorted(employee_dicts, key=itemgetter('score', 'time', 'name'), reverse=True))
    pprint.pprint(sorted_dicts)
    res = []

    for i in sorted_dicts:
        res.append(i['name'])
    for i in range(len(res) - 2):
        if sorted_dicts[i]['name'] > sorted_dicts[i + 1]['name'] and (
                sorted_dicts[i]['score'] == sorted_dicts[i + 1]['score']):
            print(True)
            res[i], res[i + 1] = res[i + 1], res[i]

    return res

names = ["abcd", "dba", "abc", "abcdd", "abcc", "abd", "abcde", "abcda", "abca", "abcbc", "bba"]
time = [20, 20, 20, 20, 10, 20, 10, 10, 20, 20, 10]
netValue = [1000, 1200, 1000, 1000, 1000, 1200, 1200, 1200, 1000, 1000, 1100]
isOnVAcation = [False, False, False, False, False, True, False, False, True, False, False]

if __name__ == '__main__':
    print(solution(names, time, netValue, isOnVAcation))