def numSubarrayProductLessThanK(nums, k):
  count = 0
  j = 0
  prod = 1
  for i in range(len(nums)):
    prod *= nums[i]
    
    while prod >= k and j <= i:
      prod /= nums[j]
      j += 1
    
    count += i - j + 1
   

  print(count)
  return count

	
	
  
nums = [1,2,3]
k = 0
numSubarrayProductLessThanK(nums, k)
