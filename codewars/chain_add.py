class CustomInt(int):
    def __call__(self, v):
        return CustomInt(self + v)


def add(n):
    return CustomInt(n)

class add(int):
    __call__ = lambda self, value: add(self + value)

add = type('', (int,), {'__call__': lambda s,n: add(s+n)})


if __name__ == '__main__':
     k = add(2)(3)
     print(k)
