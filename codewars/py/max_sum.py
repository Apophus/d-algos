"""
The maximum sum subarray problem
consists in finding the maximum sum of
a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum 
is the sum of the whole array. 
If the list is made up of only negative numbers, return 0 instead.
"""
def max_sequence(arr):

	if len(arr) == 0:
		return 0
	max_currnt = max_averall = arr[0]
	print(arr)
	for i in range(0,len(arr)-1):
		print(f'max curr: {max_currnt}')
		max_currnt = max(arr[i], max_currnt+arr[i])
		if max_currnt > max_averall:
			print(f'index {i} -- curr {max_currnt} || overall {max_averall} cuur > overaa')
			max_averall = max_currnt
	return max_averall if max_averall > 0 else 0

arr = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]

print(max_sequence(arr))
