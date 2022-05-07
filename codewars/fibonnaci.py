def fibonacci(n):
    mem_dict = {1:1, 2:1}

    if n in mem_dict:
        return mem_dict[n]
    ans = fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    def fib_memo(n, m):
        if n in m:
            return m[n]

        answer = fib_memo(n - 1, m) + fib_memo(n - 2, m)
        m[n] = answer
        return answer

    m = {1: 1, 2: 1}
    return fib_memo(n, m)


def fibonacci(m):
    cache = {0:0,1:1}
    def fib(n):
        if n not in cache:
            cache[n] = fib(n-1)+fib(n-2)
        return cache[n]
    return fib(m)

memoize = {0:0,1:1}
def fibonacci(n):
    if n not in memoize:
        memoize[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memoize[n]