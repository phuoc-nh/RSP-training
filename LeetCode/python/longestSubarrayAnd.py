def longestSubarray(nums) -> int:
    first = nums[0]
    for i in range(1, len(nums)):
        first = first & nums[i]
        
        print('first', first)
    
    
nums = [1,2,3,3,2,2]

longestSubarray(nums)