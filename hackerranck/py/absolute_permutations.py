def absolutePermutation(n, k):
    # Write your code here
    if k == 0:
        res = [str(x) for x in range(1,n+1)]
        return ' '.join(res)
    elif (n/k)%2 != 0:
        return '-1'
    else:
        res = []

        for i in range(1,n, k*2):
            swaps = list(range(i, i+k*2))
            res += swaps[k:] + swaps[:k]
        ans = ' '.join(str(x) for x in res)
        return ans

def absolutePermutation(n, k):
    if k == 0:
        return [i+1 for i in range(n)]
    elif n % (2*k) != 0 or 2*k > n: 
        return [-1]
    return [(i+1)+(1 if (i//k)%2==0 else -1)*k for i in range(n)]

print(absolutePermutation(4, 2))