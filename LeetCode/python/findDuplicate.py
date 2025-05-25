def findDuplicate(nums) -> int:
    slow = 0
    fast = 1
    
    while nums[fast] != nums[slow]:
        slow += 1
        fast += 2
        
        if slow >= len(nums):
            slow = slow % len(nums)
        
        if fast >= len(nums):
            fast = fast % len(nums)
    
    print(nums[fast], fast, slow)
    
    return nums[fast]
    
    
nums = [4,3,1,4,2]



findDuplicate(nums)