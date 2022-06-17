from itertools import product


def cartesian_product(a, b):
	print(*product(a, b))

if __name__ == '__main__':
	a = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]
	cartesian_product(a, b)