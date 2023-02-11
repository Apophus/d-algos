import snoop
# @snoop
def solution(n):
    num_str = str(n)
    stack = [int(num) for num in num_str]

    for index, number in enumerate(stack):
        print(index, number)
        if index < len(num_str)-1 and number >= stack[index+1]:
            continue
        stack.remove(number)
        break

    res = ''.join([str(n) for n in stack])
    return int(res)


if __name__ == '__main__':
    n = [1001, 44435, 218616, 861452, 222219,  100]
    for i in n:
        print(f'Solition for {i} is {solution(i)}')

