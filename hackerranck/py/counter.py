# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
from collections import Counter

def total_sales(no_of_shoes, sizes, customers, sales):
	"""
	10 
	[2, 3, 4, 5, 6, 8, 7, 6, 5, 18] 
	6 
	[(6, 55), (6, 45), (6, 55), (4, 40), (18, 60), (10, 50)]
	"""
	initial_stock = Counter(sizes)
	
	money_earned = 0
	for item in sales:

		# print(initial_stock, '---- stock')
		size_remaining = initial_stock[item[0]]
		
		if size_remaining > 0:
			money_earned += int(item[1])
			initial_stock[int(item[0])] -= 1
			continue
		else:
			
			continue
	print(money_earned, 'moneys')
	return money_earned

if __name__ == '__main__':
	no_of_shoes = int(input())
	sizes = list(map(int, input().split()))
	customers = int(input()) 
	sales = [tuple(map(int, input().split(' '))) for i in range(customers)]
	total_sales(no_of_shoes, sizes, customers, sales)

no_of_shoes = 10
sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
customers = 6
sales = [(6, 55), (6, 45), (6, 55), (4, 40), (18, 60), (10, 50)]

print(total_sales(no_of_shoes, sizes, customers, sales))