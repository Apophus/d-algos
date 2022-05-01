# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
from collections import Counter

def total_sales(no_of_shoes, sizes, customers, sales):

	initial_stock = Counter(sizes)
	# print(initial_stock)
	money_earned = 0
	for item in sales:
		# print(initial_stock, '---- stock')
		size_remaining = initial_stock[int(sales[0])]
		# print(f'remainder  -- {size_remaining}')
		if size_remaining > 0:
			money_earned += int(sales[1])
			print('sale ', sales[0], sales[1])
			initial_stock[int(sales[0])] -= 1
		else:
			print(sales[0], 'finished')
			continue
	print(money_earned)
	return money_earned

if __name__ == '__main__':
	no_of_shoes = int(input())
	sizes = map(int, input().split())
	customers = int(input()) 
	sales = input().split()
	total_sales(no_of_shoes, sizes, customers, sales)
