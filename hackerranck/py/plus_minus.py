def plusMinus(arr):
    # Write your code here
    size = len(arr)
    p = 0
    n = 0
    z = 0

    for i in arr:
        if i == 0:
            z += 1
            continue
        elif i > 0:
            p += 1
            continue
        else:
            n += 1
            continue

    print(f'{(p/size) :.6f}')
    print(f'{(n/size) :.6f}')
    print(f'{(z/size) :.6f}')


arr = [-4, 3, -9, 0, 4, 1]
print(plusMinus(arr))