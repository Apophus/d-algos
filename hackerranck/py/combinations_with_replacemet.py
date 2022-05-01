from itertools import combinations_with_replacement

def comb_with_replacements(string_, length):

	res = list(combinations_with_replacement(string_, length))

	for elements in res:
		print(''.join(elements))

if __name__ == '__main__':
	string_, length = input().split(' ')
	comb_with_replacements(sorted(string_), int(length))

# if __name__ == '__main__':
# 	string_='Hack'
# 	length = '2'
# 	comb_with_replacements(string_, length)
