# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(A):
    # write your code in Python 3.6
    result = 1
    for a in A:
        result *=a
    return result
A = [1, 2, 3]
print(solution(A))