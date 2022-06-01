def remov_nb(n):
    """
    Second iteration
    Faster because:
        * we only iterate over 'the rest of the list' on second loop
        * sum is calculated once in the beginning and we just substract
          x and y from it
    < O(n^2)
    """
    result = []
    sequence_sum = sum(range(1, n + 1))
    for x in range(1, n):
        for y in range(x + 1, n + 1):
            if x * y == sequence_sum - (x + y):
                result.append((x, y))
                result.append((y, x))
    return result

print(remov_nb(26))