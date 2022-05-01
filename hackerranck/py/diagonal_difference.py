
def get_diagonals(size, reverse=False):
    diagonals = []
    if reverse:
        for i in range(size):
            coords = (i, i)
            diagonals.append(coords)
    else:
        for i in range(size):
            coords = (i, size-(i+1))
            diagonals.append(coords)

    return diagonals

def diagonalDifference(arr):
    # Write your code here
    
    size = len(arr)
    # primary_diagonal =[(0,0),(1,1),(2,2)]
    # seconday_diagonal = [(0,2), (1,1), (2,0)]
    primary_diagonals = get_diagonals(size, reverse=False)
    seconday_diagonal = get_diagonals(size, reverse=True)
    print(seconday_diagonal, '|||', primary_diagonals)
    
    p_values = [arr[i[0]][i[1]] for i in primary_diagonals]
    s_values = [arr[i[0]][i[1]] for i in seconday_diagonal]

    res = sum(p_values) - sum(s_values)
    return abs(res)

"""
    11 2 4
    4 5 6
    10 8 -12

    11 2  4  5
    4  5  6  3
    10 8 -12 1
    12 1  6  4
    
    """
arr = [[11,2,4], [4,5,6],[10,8,-12]]

print(diagonalDifference(arr))