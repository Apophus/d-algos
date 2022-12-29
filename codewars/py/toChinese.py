
def to_chinese_numeral(n):
    numerals = {
        "-": "负",
        ".": "点",
        0: "零",
        1: "一",
        2: "二",
        3: "三",
        4: "四",
        5: "五",
        6: "六",
        7: "七",
        8: "八",
        9: "九",
        10: "十",
        100: "百",
        1000: "千",
        10000: "万"
    }

    num_str = str(abs(n))
    in_chinese = ''
    is_positive = True if n > 0 else False

    def whole_nos(num_str):
        res = ''

        for index, char in enumerate(num_str):

            place_value = 10**(len(num_str[index+1:]))

            if index == 0:
                res += numerals[int(char)]
                if len(num_str) > 1:
                    res += numerals[place_value]
                continue

            if len(set(num_str[index:])) == 1 and list(set(num_str[index:]))[0] == '0':
                break

            if place_value == 1:
                res += numerals[int(char)]
                break

            if char != '0':
                res += numerals[int(char)]
                if place_value - 1:
                    res += numerals[place_value]
                continue

            if char == '0' and res[-1] != numerals[0]:
                res += numerals[0]
                continue

        return res

    if n in numerals.keys() and len(num_str) <= 2:
        in_chinese += numerals[n]

    elif len(num_str) == 2 and n < 20:
        in_chinese += numerals[10]
        in_chinese += numerals[int(num_str[1])]
        if is_positive:
            return in_chinese
        return numerals['-'] + in_chinese

    elif '.' in num_str:
        # Taking care of decimals
        left = whole_nos(num_str.split('.')[0])
        right = ''.join(numerals[int(n)] for n in num_str.split('.')[1])
        in_chinese = left + numerals['.'] + right

    else:
        in_chinese = whole_nos(num_str)
        print('++++')

    if is_positive:
        print(True)
        return in_chinese
    in_chinese =  numerals['-'] + in_chinese


if __name__ == '__main__':
    n = 20
    res = to_chinese_numeral(n)
    print(res)