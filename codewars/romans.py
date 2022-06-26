def solution(number):
    # TODO finish this
    roman_ob = {'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}
    roman_translation = ''
    for key in roman_ob.keys():
        if roman_ob[key] == number:
            roman_translation += key
            break
    filtered = [key for key in roman_ob if roman_ob[key] >=number]


    return roman_translation