def solve(s):
    strings = s.split(' ')
    capitalized = [x.capitalize() for x in strings]
    result = ' '.join(capitalized)
    return result