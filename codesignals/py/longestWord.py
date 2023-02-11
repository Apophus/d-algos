import string


def solution(text):
    cleaned = ''
    for i in text:
        if i in string.ascii_letters:
            cleaned += i
        else:
            cleaned += ' '

    res = cleaned.split()

    return max(res, key=len)


if __name__ == '__main__':
    text = "Ready[[[, steady, go!"
    print(solution(text))
