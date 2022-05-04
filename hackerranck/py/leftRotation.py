def rotateLeft(d, arr):
    # Write your code here

    # n == len(arr) || len(arr)%n return n
    return arr[d:] + arr[0:d]
