def checkSubarraySum(nums, k):
	remainder = {0: -1}
 
	total = 0
	for i, n in enumerate(nums):
		total += n
		r = total % k
		print('r', r)
		print('r', remainder)
		if r not in remainder:
			remainder[r] = i
		elif i - remainder[r] > 1:
			print(i)
			print(remainder[r])
			return True

	return False

nums = [42, 1, 4]
k = 6
print(checkSubarraySum(nums, k))