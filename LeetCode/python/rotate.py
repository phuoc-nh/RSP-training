def rotate(nums, k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	k = k % len(nums)

	print(k)
	print(k-len(nums))
	print(nums[0:len(nums)- k])
	print(nums[len(nums)- k:])

	nums[:] = nums[len(nums)- k:] + nums[0:len(nums)- k]
 

nums = [1,2,3,4,5,6,7]
k = 3

nums = [-1,-100,1,3,99]
k = 2
rotate(nums, k)