def sum_strings(x, y):
    if not x:
        return y
    elif not y:
        return x

    elif (x and y):
        s = int(x) + int(y)
    
    return str(s)
