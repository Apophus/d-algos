from collections import Counter
import snoop

# @snoop
def runoff(voters):
    first, last = [x[0] for x in voters], [x[-1] for x in voters]
    # if all tie, return None.
    if len(first) == len(list(set(first))):
        return None

    # check if there's a run-off
    tally = Counter(first).most_common(1)[0]

    win = True if tally[1] > len(first) // 2 else False

    if win:
        return tally[0]
    # at this point there's a run-off
    loss_tally = Counter(last).most_common(1)[0][1]
    last_position = [x for x in last if Counter(last)[x] == loss_tally]

    for voter in voters:
        for candidate in voter:
            if candidate in last_position:
                voter.remove(candidate)
            continue

    return runoff(voters)

# worked
@snoop
def runoff_(voters):
    while True:
        lss = [ls[0] for ls in voters]
        dc = dict(Counter(lss))
        for x in voters[0]:
            if x not in dc:
                dc[x] = 0
        for i in dc:
            if dc[i]>(len(lss)/2):
                return i
            if dc[i]==min(list(dc.values())):
                for ls in voters:
                    ls.remove(i)
        if len(dc)>1 and len(set(list(dc.values())))==1:
            return None


if __name__ == '__main__':
    # test cases
    voters = [["a", "c", "d", "e", "b"],
              ["e", "b", "d", "c", "a"],
              ["d", "e", "c", "a", "b"],
              ["c", "e", "d", "b", "a"],
              ["b", "e", "a", "c", "d"]]

    voters2 = [['a', 'c', 'b', 'e', 'd'],
               ['c', 'a', 'e', 'b', 'd'],
               ['e', 'c', 'b', 'd', 'a'],
               ['a', 'e', 'c', 'd', 'b'],
               ['d', 'c', 'e', 'a', 'b']]

    voters3 = [['b', 'c', 'e', 'a', 'd'],
               ['b', 'c', 'a', 'd', 'e'],
               ['a', 'd', 'c', 'e', 'b'],
               ['b', 'e', 'a', 'd', 'c'],
               ['b', 'c', 'a', 'e', 'd']]

    voters4 = [['b', 'a', 'e', 'd', 'c'],
               ['a', 'd', 'e', 'c', 'b'],
               ['c', 'a', 'd', 'b', 'e'],
               ['c', 'a', 'e', 'b', 'd'],
               ['d', 'c', 'e', 'a', 'b']]

    print(runoff_(voters4))

[['b', 'a', 'e', 'd', 'c'], ['a', 'd', 'e', 'c', 'b'], ['c', 'a', 'd', 'b', 'e'], ['c', 'a', 'e', 'b', 'd'], ['d', 'c', 'e', 'a', 'b']]
[['a', 'e', 'd', 'c'], ['a', 'd', 'e', 'c'], ['c', 'a', 'd', 'e'], ['c', 'a', 'e', 'd'], ['d', 'c', 'e', 'a']]
[['a', 'e', 'd'], ['a', 'd', 'e'], ['a', 'd', 'e'], ['a', 'e', 'd'], ['d', 'e', 'a']]