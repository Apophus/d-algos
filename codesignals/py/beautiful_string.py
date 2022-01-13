def isBeautifulString(inputString):
    chars = [x for x in inputString]
    unique_chars = set(chars)
    cha_count = {x:chars.count(x) for x in unique_chars}
    print(cha_count)
    res = []

    for char in unique_chars:
        if ord(char) == 97:
            continue
        else:
            previous = ord(char)-1
            previous_c = chr(previous)
            if previous_c in unique_chars:
                print(previous_c, True)
                if cha_count[previous_c] >= cha_count[char]:
                    print('yes')
                    res.append('t')
                else:
                    res.append('f')
            else:
                if previous_c not in unique_chars:
                    res.append('f')
    # print(res)
    if 'f' in res:
        return False
    else:
        return True
        
    
print(isBeautifulString('aabbb'))