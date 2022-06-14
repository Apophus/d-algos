class CustomInt(int):
    def __call__(self, v):
        return CustomInt(self + v)


def add(n):
    return CustomInt(n)


if __name__ == '__main__':
     k = add(2)(3)
     print(k)
