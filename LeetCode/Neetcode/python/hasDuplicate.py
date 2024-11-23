def hasDuplicate(self, nums: List[int]) -> bool:
    dup = set()
    
    for n in nums:
        if n in dup:
            return True
        
        dup.add(n)
    
    
    return False
nums = [1, 2, 3, 3]

hasDuplicate(nums)
