def minOperations(nums, k):
	finalXor = 0
 
	for n in nums:
		finalXor ^= n
  
	res = 0

	while finalXor or k:
		lastBitK = k % 2
		lastBitFXor = finalXor % 2
  
		if lastBitK != lastBitFXor:
			res += 1
   
		finalXor //= 2
		k //= 2
	print(res)
	return res
nums = [2,1,3,4]
k = 1
minOperations(nums, k)
 