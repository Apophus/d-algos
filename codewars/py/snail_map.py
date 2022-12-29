def snail(snail_map):
	list_of_numbers = []

	while snail_map:
		# top section of array
		for i in snail_map[0]:
			list_of_numbers.append(i)
		snail_map.pop(0)
		# a 1x1 array will end here
		if not snail_map:
			break
		# right side of array
		for j in snail_map:
			list_of_numbers.append(j[-1])
			j.pop()
		# The bottom part of the array
		for k in range(len(snail_map[-1]) - 1, -1, -1):
			list_of_numbers.append(snail_map[-1][k])
		snail_map.pop()
		if not snail_map:
			break
		# The remainder of the elements reversed
		for l in reversed(snail_map):
			list_of_numbers.append((l[0]))
			l.pop(0)

	return list_of_numbers


if __name__ == '__main__':
	snail_map = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	snail(snail_map)
